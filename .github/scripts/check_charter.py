"""Read-only checks for an exact public Charter text candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


READER_FILES = frozenset({
    "Charter/00-front-matter.md", "Charter/01-day-in-life.md", "Charter/02-eight-systems.md",
    "Charter/03-human-nature-purpose.md", "Charter/04-ai-robotics-infrastructure.md",
    "Charter/05-governance-decision-making.md", "Charter/06-economy-funding.md",
    "Charter/07-education-human-development.md", "Charter/08-crime-justice-safety.md",
    "Charter/09-privacy-security.md", "Charter/10-technology-access.md",
    "Charter/11-tradition-heritage.md", "Charter/12-competition-cooperation.md",
    "Charter/13-mortality-aging.md", "Charter/14-innovation-without-profit.md",
    "Charter/15-failure-modes-risks.md", "Charter/16-handling-resistance.md",
    "Charter/17-ai-alignment-safety.md", "Charter/18-growth-sustainability.md",
    "Charter/19-global-equity-development.md", "Charter/20-global-wealth-tax-enforcement.md",
    "Charter/21-success-metrics.md", "Charter/22-what-you-can-do.md",
    "Charter/23-call-to-action.md", "Charter/24-transition-roadmap.md",
    "Charter/25-district-regional-governance-implementation.md",
    "Charter/26-stakeholders-coalitions.md", "Charter/appendix-a-technical.md",
    "Charter/appendix-b-cases.md", "Charter/appendix-c-questions.md",
    "Charter/appendix-d-resources.md", "Charter/appendix-e-glossary.md",
    "Charter/appendix-energy-cost-formula.md", "Charter/appendix-energy-eroei-framework.md",
    "Charter/appendix-energy-fission-eroei-calculation.md",
    "Charter/play-based-development-research.md", "00-sincerity-statement.md",
    "README.md", "LICENSE-CHARTER.md",
})
REPOSITORY_METADATA = frozenset({
    ".github/scripts/check_charter.py",
    ".github/workflows/checks.yml",
    "charter-manifest.json",
})
WEBSITE_APPENDIX_ROUTES = {
    "appendix-appendix-energy-cost-formula": "Charter/appendix-energy-cost-formula.md",
    "appendix-appendix-energy-eroei-framework": "Charter/appendix-energy-eroei-framework.md",
    "appendix-appendix-energy-fission-eroei-calculation":
        "Charter/appendix-energy-fission-eroei-calculation.md",
}
_HEX_64 = re.compile(r"[0-9a-f]{64}\Z")
_WINDOWS_RESERVED = {
    "con", "prn", "aux", "nul",
    *(f"com{i}" for i in range(1, 10)),
    *(f"lpt{i}" for i in range(1, 10)),
}
_FORBIDDEN_BUNDLE_PATH = re.compile(
    r'(?i)(?:^|[\s\\\"\'`()\[\]=:,])(?:\.\.?/)*'
    r'(?:evidence/energy-model/|worker/|workers/|migrations/|tests/|private/|editorial/|\.superpowers/)'
    r'[^\s"\'`()\[\]<>]*|(?:^|[\s\\\"\'`()\[\]=:,])(?:\.\.?/)*'
    r'tools/[^\s"\'`()\[\]<>]+\.(?:py|js|sql|sh|toml|ya?ml)'
)
_HTTP_URL = re.compile(r"https?://[^\s\\<>\"'`]+", re.IGNORECASE)
_ESCAPED_WHITESPACE = re.compile(r"\\[nrt]")
_FENCE_START = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))")
_REFERENCE_LINK = re.compile(r"^ {0,3}\[(?!\^)[^\]]+\]:\s*(?:<([^>]+)>|(\S+))", re.MULTILINE)
_HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
_READER_DIRECTORIES = frozenset({"Charter"})


def _is_reparse(info: os.stat_result) -> bool:
    return bool(getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))


def _canonical_name(name: object) -> str:
    if not isinstance(name, str) or not name or "\\" in name or ":" in name:
        raise ValueError(f"Non-canonical or unsafe relative path: {name!r}")
    if name.startswith("/") or any(ord(char) < 32 or ord(char) == 127 for char in name):
        raise ValueError(f"Absolute or unsafe relative path: {name!r}")
    parts = name.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise ValueError(f"Non-canonical or escaped relative path: {name!r}")
    for part in parts:
        if part.endswith((".", " ")) or any(char in part for char in '<>"|?*'):
            raise ValueError(f"Non-portable relative path: {name!r}")
        if part.split(".", 1)[0].casefold() in _WINDOWS_RESERVED:
            raise ValueError(f"Reserved Windows path component: {name!r}")
    return name


def _plain_root(path: Path) -> Path:
    path = Path(path).absolute()
    for part in (path, *path.parents):
        try:
            info = part.lstat()
        except OSError as error:
            raise ValueError(f"Cannot inspect candidate path: {part}") from error
        if stat.S_ISLNK(info.st_mode) or _is_reparse(info):
            raise ValueError(f"Linked or reparse candidate path is not allowed: {part}")
        if part == path and not stat.S_ISDIR(info.st_mode):
            raise ValueError(f"Candidate must be a real directory: {path}")
    return path.resolve(strict=True)


def _entry_kind(info: os.stat_result, name: str) -> str:
    if stat.S_ISLNK(info.st_mode) or _is_reparse(info):
        raise ValueError(f"Linked or reparse entry is not allowed: {name}")
    if stat.S_ISDIR(info.st_mode):
        return "directory"
    if stat.S_ISREG(info.st_mode):
        return "file"
    raise ValueError(f"Special filesystem entry is not allowed: {name}")


def _expected_directories(names: set[str]) -> set[str]:
    return {
        "/".join(parts[:index])
        for name in names
        for parts in [name.split("/")]
        for index in range(1, len(parts))
    }


def _walk(root: Path) -> tuple[set[str], set[str]]:
    files: set[str] = set()
    directories: set[str] = set()
    folded: dict[str, str] = {}

    def visit(directory: Path, prefix: str = "") -> None:
        try:
            entries = sorted(os.scandir(directory), key=lambda entry: entry.name.casefold())
        except OSError as error:
            raise ValueError(f"Cannot scan candidate directory: {directory}") from error
        for entry in entries:
            name = f"{prefix}/{entry.name}" if prefix else entry.name
            _canonical_name(name)
            key = name.casefold()
            if key in folded and folded[key] != name:
                raise ValueError(f"Case-colliding inventory path: {folded[key]} and {name}")
            folded[key] = name
            try:
                kind = _entry_kind(entry.stat(follow_symlinks=False), name)
            except OSError as error:
                raise ValueError(f"Cannot inspect candidate entry: {name}") from error
            if kind == "directory":
                if name == ".git":
                    continue
                directories.add(name)
                visit(Path(entry.path), name)
            else:
                if name == ".git":
                    raise ValueError("A linked gitfile is not an allowed .git directory")
                files.add(name)

    visit(root)
    return files, directories


def _strict_json(raw: bytes):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"Charter manifest contains duplicate JSON key: {key}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"Charter manifest contains nonstandard JSON constant: {value}")

    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=reject_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("Malformed Charter manifest JSON") from error


def _manifest(raw: bytes) -> dict[str, str]:
    value = _strict_json(raw)
    if not isinstance(value, dict) or set(value) != {"schema_version", "files"}:
        raise ValueError("Charter manifest must contain exactly schema_version and files")
    if type(value["schema_version"]) is not int or value["schema_version"] != 1:
        raise ValueError("Charter manifest schema_version must be integer 1")
    if not isinstance(value["files"], dict):
        raise ValueError("Charter manifest files must be an object")
    hashes: dict[str, str] = {}
    folded: set[str] = set()
    for raw_name, digest in value["files"].items():
        name = _canonical_name(raw_name)
        if name.casefold() in folded:
            raise ValueError(f"Charter manifest contains duplicate or case-colliding path: {name}")
        folded.add(name.casefold())
        if not isinstance(digest, str) or not _HEX_64.fullmatch(digest):
            raise ValueError(f"Malformed SHA-256 hash for {name}")
        hashes[name] = digest
    if set(hashes) != READER_FILES:
        raise ValueError("Charter manifest must checksum exactly the 39 reader files")
    return hashes


def _check_public_text(text: str, name: str) -> None:
    cleaned = _ESCAPED_WHITESPACE.sub(" ", text)
    cleaned = _HTTP_URL.sub(" ", cleaned)
    match = _FORBIDDEN_BUNDLE_PATH.search(cleaned)
    if match:
        raise ValueError(f"Charter reader {name} contains forbidden internal path near: {match.group(0)!r}")


def _without_fenced_code(text: str) -> str:
    output = []
    fence_char = ""
    fence_length = 0
    for line in text.splitlines():
        match = _FENCE_START.match(line)
        if not fence_char and match:
            fence_char = match.group(1)[0]
            fence_length = len(match.group(1))
            output.append("")
        elif fence_char:
            stripped = line.lstrip(" ")
            if len(stripped) - len(stripped.lstrip(fence_char)) >= fence_length and not stripped.strip(fence_char).strip():
                fence_char = ""
                fence_length = 0
            output.append("")
        else:
            output.append(line)
    return "\n".join(output)


def _heading_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]*>", "", heading)
    heading = heading.replace("`", "")
    output = []
    for char in heading.casefold():
        category = unicodedata.category(char)
        if category.startswith("P") and char not in "-_":
            continue
        if category.startswith("S"):
            continue
        output.append(char)
    return re.sub(r"\s+", "-", "".join(output).strip())


def _heading_ids(text: str) -> set[str]:
    seen: dict[str, int] = {}
    identifiers = set()
    for line in text.splitlines():
        match = _HEADING.match(line)
        if not match:
            continue
        base = _heading_slug(match.group(2))
        occurrence = seen.get(base, 0)
        seen[base] = occurrence + 1
        identifiers.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return identifiers


def _markdown_targets(text: str):
    source = _without_fenced_code(text)
    for match in _INLINE_LINK.finditer(source):
        yield match.group(1) or match.group(2)
    for match in _REFERENCE_LINK.finditer(source):
        yield match.group(1) or match.group(2)


def _validate_link(root: Path, source_name: str, target: str, texts: dict[str, str]) -> None:
    if any(ord(char) < 32 or ord(char) == 127 for char in target) or "\\" in target:
        raise ValueError(f"Unsafe Markdown link in {source_name}: {target!r}")
    try:
        parts = urlsplit(target)
    except ValueError as error:
        raise ValueError(f"Malformed Markdown link in {source_name}: {target!r}") from error
    scheme = parts.scheme.casefold()
    if scheme in {"http", "https", "mailto"}:
        return
    if scheme:
        raise ValueError(f"Unsupported Markdown link scheme in {source_name}: {scheme}")
    if parts.netloc:
        raise ValueError(f"Scheme-less Markdown link authority is not allowed in {source_name}: {target!r}")
    if re.search(r"%(?![0-9a-fA-F]{2})", parts.path):
        raise ValueError(f"Malformed percent escape in Markdown link: {target!r}")
    path_text = unquote(parts.path, errors="strict")
    fragment = unquote(parts.fragment, errors="strict")
    if any(ord(char) < 32 or ord(char) == 127 for char in path_text + fragment) or "\\" in path_text:
        raise ValueError(f"Unsafe decoded Markdown link in {source_name}: {target!r}")
    if fragment in WEBSITE_APPENDIX_ROUTES and not parts.path and not parts.query:
        route_target = WEBSITE_APPENDIX_ROUTES[fragment]
        if route_target not in READER_FILES:
            raise ValueError(f"Unknown website appendix route: {fragment}")
        if route_target not in texts:
            raise ValueError(f"Missing website appendix route target: {route_target}")
        return
    if path_text.startswith("/") or path_text.startswith("//"):
        raise ValueError(f"Absolute Markdown link is not allowed in {source_name}: {target!r}")
    source_path = root.joinpath(*source_name.split("/"))
    base = source_path.parent if path_text else source_path.parent
    candidate = base.joinpath(*path_text.split("/")) if path_text else source_path
    resolved = candidate.resolve(strict=False)
    try:
        relative = resolved.relative_to(root).as_posix()
    except ValueError:
        raise ValueError(f"Markdown link escapes reader tree in {source_name}: {target!r}") from None
    if relative in READER_FILES:
        if fragment and fragment not in _heading_ids(texts[relative]):
            raise ValueError(f"Missing Markdown heading fragment in {source_name}: {target!r}")
        return
    if relative in _READER_DIRECTORIES:
        descendants = {name for name in READER_FILES if name.startswith(relative + "/")}
        if not (root / relative).is_dir() or not descendants:
            raise ValueError(f"Markdown directory link has no allowlisted reader descendants: {target!r}")
        if fragment:
            raise ValueError(f"Markdown directory link cannot carry a heading fragment: {target!r}")
        return
    raise ValueError(f"Markdown link does not target a reader file or allowed directory in {source_name}: {target!r}")


def _validate_links(root: Path, texts: dict[str, str]) -> None:
    for source_name, text in texts.items():
        for target in _markdown_targets(text):
            _validate_link(root, source_name, target, texts)


def check_candidate(checkout: Path) -> dict[str, str]:
    """Check self-consistency of the exact public candidate; this grants no approval."""
    root = _plain_root(Path(checkout))
    actual_files, actual_directories = _walk(root)
    expected_files = set(READER_FILES) | set(REPOSITORY_METADATA)
    expected_directories = _expected_directories(expected_files)
    if actual_files != expected_files or actual_directories != expected_directories:
        raise ValueError(
            "inventory mismatch: "
            f"missing files={sorted(expected_files - actual_files)}; "
            f"extra files={sorted(actual_files - expected_files)}; "
            f"missing directories={sorted(expected_directories - actual_directories)}; "
            f"extra directories={sorted(actual_directories - expected_directories)}"
        )
    manifest_hashes = _manifest((root / "charter-manifest.json").read_bytes())
    if set(manifest_hashes) != READER_FILES:
        raise ValueError("Charter manifest differs from reviewed reader inventory")
    actual_hashes: dict[str, str] = {}
    texts: dict[str, str] = {}
    for name in sorted(READER_FILES):
        data = (root / name).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        actual_hashes[name] = digest
        if digest != manifest_hashes[name]:
            raise ValueError(f"Charter manifest differs from reader bytes for {name}")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError(f"Charter reader is not UTF-8: {name}") from error
        _check_public_text(text, name)
        texts[name] = text
    _validate_links(root, texts)
    return actual_hashes


def _main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        check_candidate(args.checkout)
        return 0
    except (OSError, ValueError) as error:
        print(f"CHARTER CANDIDATE CHECK FAILED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(_main())
