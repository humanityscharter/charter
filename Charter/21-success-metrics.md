---
num: 21
part_id: 4
part_title: 'Part IV: Global Dimensions & Planetary Stewardship'
title: Success Metrics & Indicators
full_title: 'Chapter 21: Success Metrics & Indicators'
subtitle: How we measure progress toward an abundance society
core_premise: 'GDP tells us how much an economy produces, not whether people are secure or ecosystems are healthy. The chapter proposes other measures to debate and test.'
key_pillars:
- '**What GDP Misses:** Spending after illness or environmental damage can add to GDP without showing that life improved.'
- '**Measures of Living Well:** Consider health, security, connection, education, and opportunities to create and contribute.'
- '**Ecological Measures:** Track changes in biodiversity, soil, carbon, and water using methods people can inspect and challenge.'
- '**Public Accountability:** Make results visible without letting a score replace the experiences of residents.'
breakthrough_mechanism: 'Chapter 21 defines the shared metrics dictionary and puts separate measures, ranges, gaps, and testimony first. Any combined index remains an experimental secondary summary, with public agreement on its data, weights, and revision rules; it cannot determine rights compliance, funding, sanctions, eligibility, or transition gates, or rank people, jurisdictions, or cultures.'
core_debate: 'How can we measure progress without rewarding officials for improving the score while people still struggle?'
---

# Chapter 21: Success Metrics & Indicators

*How we measure progress toward an abundance society*

---

## Introduction: GDP Does Not Measure a Good Life

> *"Our gross national product counts air pollution and cigarette advertising, and ambulances to clear our highways of carnage. It counts special locks for our doors and the jails for the people who break them. It counts the destruction of the redwood and the loss of our natural wonder in chaotic sprawl... Yet it measures neither our wit nor our courage, neither our wisdom nor our learning, neither our compassion nor our devotion to our country. It measures everything, in short, except that which makes life worthwhile."*  
> (**Robert F. Kennedy**), University of Kansas, March 18, 1968[^ch21-rfk-gdp-quote]

[^ch21-rfk-gdp-quote]: The John F. Kennedy Presidential Library's transcript of Robert F. Kennedy's March 18, 1968 University of Kansas remarks preserves this passage. The speech refers to gross national product, as the quotation states, rather than today's specific GDP measure: https://www.jfklibrary.org/learn/about-jfk/the-kennedy-family/robert-f-kennedy/robert-f-kennedy-speeches/remarks-at-the-university-of-kansas-march-18-1968

In 2024, world GDP was about $111 trillion in current U.S. dollars and grew 2.9% in real terms, according to the World Bank.[^ch21-world-gdp-2024] That same year, an estimated 673 million people experienced hunger, with an uncertainty range of 638–720 million in the UN food-security report.[^ch21-fao-hunger-2024] At the end of 2024, UNHCR estimated 123.2 million people were forcibly displaced because of persecution, conflict, violence, human-rights violations, or events seriously disturbing public order.[^ch21-unhcr-displacement-2024] That is not a count of people displaced only by climate change.

These numbers describe different hardships, not parts of one index. GDP alone cannot tell us whether mental health is improving, wealth is fairly shared, or species and ecosystems are recovering. Each of those questions needs its own measure and evidence. We should not turn different problems into one dramatic figure just to make the case feel stronger.

[^ch21-world-gdp-2024]: World Bank's World data page reports 2024 GDP of $110.98 trillion in current U.S. dollars and real GDP growth of 2.9%: https://data.worldbank.org/country/1w

[^ch21-fao-hunger-2024]: FAO's report on *The State of Food Security and Nutrition in the World 2025* gives a central estimate of 673 million people experiencing hunger in 2024, with a 638–720 million range: https://www.fao.org/newsroom/detail/global-hunger-declines--but-rises-in-africa-and-western-asia--un-report/en

[^ch21-unhcr-displacement-2024]: UNHCR, *Global Trends 2024*, estimates 123.2 million forcibly displaced people at year-end 2024 and specifies the categories included. It does not attribute the entire figure to climate or ecological causes: https://www.unhcr.org/publications/global-trends-2024

Gross Domestic Product gives a dangerously distorted picture. An oil spill can count as an economic gain because cleanup work costs money. Chronic disease can increase GDP because treatment creates revenue. At the same time, GDP assigns no value to clean air, parents caring for children, community mutual aid, or unpolluted rivers.

GDP measures economic output, not whether people are secure or ecosystems are healthy. To measure progress toward abundance, we need a broader scorecard.

This chapter proposes seven dimensions for measuring progress toward abundance:

1. **Basic Needs** - Are all human needs met?
2. **Well-being** - Are people flourishing?
3. **Sustainability** - Is the system environmentally viable?
4. **Equity** - Are benefits distributed fairly?
5. **Freedom** - Are people free to choose their path?
6. **Resilience** - Can the system withstand shocks?
7. **Meaning** - Do people find purpose and fulfillment?

**The goal:** Create a measurement system that makes abundance visible, tracks progress, and guides continuous improvement.

---

## Chapter 21 Metrics Dictionary: canonical ownership and taxonomy key

Chapter 21 is the canonical owner of the shared metric dictionary. It owns shared definitions, stable IDs, categories, registry statuses, card fields, lifecycle rules, comparison rules, and limits on any index or composite. Other chapters may keep their own questions, evidence, scenarios, and implementation context, but they must refer to this dictionary rather than silently creating a competing shared definition.

This chapter's `CORE` label means a proposed universal Charter core, not enacted law. A metric or target binds a jurisdiction only through a complete lawful adoption record; registration or inclusion in this chapter alone is not adoption. A public adoption record must state the definition, purpose, target rule, permitted and prohibited uses, steward, auditor, baseline status, scope, cadence, uncertainty, review or expiry date, and appeal route.

### Category and lifecycle status key

Category and registry status are separate axes. The category says what a measure is for; the status says where it stands in its lifecycle.

| Key | Category | Allowed role |
|---|---|---|
| `RF` | Rights Floor | Measures whether a lawfully adopted guaranteed right is delivered; a shortfall requires repair and remedy. |
| `OP` | Operational Indicator | Measures service, institutional, ecological, reliability, disparity, or civic functioning. |
| `LM` | Learning Measure | Answers a stated pilot, stress-test, or adaptation question and supports learning, not individual ranking. |
| `AS` | Aspirational End State | Tracks a long-term direction or voluntary population-level experience; it is not an individual duty. |

Registry status is recorded separately:

- **`CORE`**: proposed universal Charter core, not enacted law or a binding local target until lawfully adopted.
- **`LOCAL`**: a measure lawfully adopted in a defined jurisdiction under the shared standard.
- **`CANDIDATE`**: preserved proposal awaiting validation or adoption.
- **`PILOT`**: a design or exercise for time-bounded learning, with a stated question, safeguards, review date, and stop rules. Each registry entry identifies whether it is a proposed design or an active exercise; active use requires a recorded lawful approval and public activation record.
- **`RETIRED`**: kept in history but no longer active; its reason and prior results remain available.

For example, `AS-ME-001` may have status `CORE` as a proposed Charter designation. That example does not enact the measure, impose a target, or decide anything for a jurisdiction. A local extension uses a stable namespace and must not reuse a universal ID.

### Required metric-card schema and baseline rule

Every future core, local, candidate, pilot, or retired card must publish all of these fields. Omitted fields are defects. An explicit `unknown`, `not yet measured`, or `not yet adopted` value is honest status information and must remain visible.

1. **Category** and **Registry status** (with stable ID, name, version, and jurisdiction namespace where applicable).
2. **Dimension** and plain-language **Definition**, including inclusion and exclusion rules.
3. **Unit and calculation**, including numerator, denominator, reference population, normalization, aggregation, and inapplicable cases.
4. **Baseline**, with type, method, reference period, local and shared value or range when available, current status, source date, and comparability explanation.
5. **Scope**, including geography, population, time window, service boundary, and cultural limits.
6. **Stewardship**, naming data steward, response owner, independent auditor, publication owner, affected-community contact, and responsible assembly.
7. **Cadence**, matched to the purpose and collection method.
8. **Uncertainty and data quality**, including ranges or intervals, assumptions, missingness, known bias, and comparability limits.
9. **Disaggregation and privacy**, including relevant groups, intersectional views where safe, cell suppression, retention, and access controls.
10. **Evidence**, including methods, sources, audits, structured testimony, affected-community input, and Indigenous or local knowledge where relevant.
11. **Target rule**, including a value, direction, range, scenario, or learning question; baseline; adoption and review dates; owner; and revision or stop triggers.
12. **Use boundary**, including permitted and prohibited uses, warning thresholds, human-review route, and related rights rules.
13. **Version history**, including definition or method changes, old results, bridge calculations, decision records, and reasons for adoption, revision, pilot, or retirement.

Chapter 21 must not invent a local baseline. Jurisdictions measure or document their actual baseline before claiming progress. A baseline may honestly be `unknown` or `not yet measured`; an estimate must be labeled, separately reported, and accompanied by assumptions and uncertainty.

### Target behavior, decision roles, and adoption record

Category-specific targets have different meanings:

- **Rights Floor (`RF`):** after lawful adoption, 100% adequate delivery is the binding entitlement target. A gap triggers repair, support, and remedy; it never weakens or averages away the right.
- **Operational Indicator (`OP`):** a threshold or safe range is a warning and review trigger, not an automatic adverse decision.
- **Learning Measure (`LM`):** answers a stated learning question and cannot silently become a permanent target or make a guaranteed right optional.
- **Aspirational End State (`AS`):** expresses a directional, voluntary population-level aspiration, not an individual duty or coercive endpoint.

Roles remain separate. Citizen assemblies adopt indicators and permitted uses; an independent statistics office measures, validates, publishes, and corrects; service agencies respond to gaps; independent auditors verify methods and provenance; scientists and community knowledge holders inform ecological and cultural interpretation; and courts together with the Chapter 8 rights process decide rights and remedies. No new metric office or enforcement power is created merely by this chapter.

Demographic data are planning context, not a population target and never an individual eligibility tool. Public planning may use aggregate, privacy-protected population totals, age distributions, service demand, and ecological indicators to assess capacity and demographic adaptation. It may not create reproductive registries, fertility scores, pregnancy surveillance, or individual reproductive data for eligibility, enforcement, resource allocation, or pressure about whether to have children or pursue life extension. Population count alone is not sufficient evidence for a policy response.

Every adoption record is public and records the definition, purpose, target rule, permitted and prohibited uses, steward, auditor, baseline status, scope, cadence, uncertainty, review or expiry date, and appeal route. A warning requires investigation, affected-community input, public reasons, and a recorded human decision to continue, revise, pause, repair, or stop.

### Verified achievement rule

An **achievement claim** is reserved for a verified result, not for launching a program, reaching a calendar date, showing substantial progress, or reporting a favorable average. Before a result may be called achieved, the adopted metric definition must state its baseline, scope, threshold, uncertainty treatment, owner, audit route, and required duration. Measured results must meet that standard for the required duration, and **independent verification** must confirm the result, its data quality, and the relevant scope. The claim must also show that every applicable rights floor is satisfied.

A favorable average or aggregate cannot establish full achievement while a covered region or protected population remains below an applicable rights floor. An average may support a carefully scoped statement of broad progress, but rights-floor failures require repair, support, and remedy; they are never averaged away. Historical claims may use “achieved” when their evidence and scope are stated, and a scenario may use it only as an explicitly assumed condition.

### Universal Basic Resources (UBR) rights floor

The proposed UBR rights floor consists of ten separately measured cards: `RF-BN-001` Nutritious food and safe water; `RF-BN-002` Safe, adequate housing; `RF-BN-003` Comprehensive physical and mental healthcare; `RF-BN-004` Education and lifelong learning; `RF-BN-005` Adequate basic energy; `RF-BN-006` Transportation to essential services and community life; `RF-BN-007` Reliable connectivity; `RF-BN-008` Adequate personal computing access; `RF-BN-009` Necessary assistive technology; and `RF-BN-010` Repair, maintenance, accessibility support, and reasonable replacement. Their inclusion here does not enact them or adopt them for a jurisdiction.

UBR review separately measures **access**, **adequacy**, privacy-safe **disparities**, and whether each guaranteed service is free at the point of use, meaning no fee or charge is demanded from the person receiving it. Before lawful adoption, cost, affordability, and access evidence describe present conditions, service gaps, and transition burdens. After lawful adoption, 100% adequate delivery free at the point of use is the binding entitlement target for every person in scope. Any gap triggers documented **gap repair**, support, and remedy. A fee or charge for a guaranteed service is a rights gap and remains recorded for repair and remedy. Chapter 6 keeps energy, materials, labor, maintenance, infrastructure, and ecological impacts in public accounting. These measures cover the guaranteed UBR floor; they do not expand it to every luxury or extra. An average, success elsewhere, an index, or another metric cannot offset, hide, or average away a rights failure for a person or group.

## Proposed universal core metric cards and non-core registry

The following 33 cards are the proposed universal core. They are ordered by the approved registry map and grouped under the seven dimensions. Each card is a complete publication record in abbreviated reader-facing form: an implementation must add its jurisdictional baseline and adoption record before making a progress claim. `CORE` remains a proposed Charter designation, not enacted law.

### Basic Needs: rights floor

#### RF-BN-001 - Nutritious food and safe water

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures each person’s access to sufficient, safe, nutritious food and safe drinking water free at the point of use, including continuity and culturally appropriate options; it excludes satisfaction alone and counts an inaccessible or unsafe supply as a gap.
- **Unit and calculation:** Numerator is persons whose food and water meet the published access and adequacy standard and are provided free at the point of use; denominator is all persons in scope; report component results separately and never average away a failed component.
- **Baseline:** `unknown` / `not yet measured`; use a dated household and service-record assessment for a defined reference period, publish a value or range when measured, and block progress claims until populated.
- **Scope:** All persons in the adopted geography, including households, institutions, remote areas, disability access, seasonal continuity, and the food, water, and safety time window.
- **Stewardship:** Data steward: food-and-water records custodian; response owner: rights-gap repair lead; independent auditor: methods auditor; publication owner: public reporting editor; affected-community contact: accessible complaint route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous safety and outage records, quarterly access review, annual household validation, and event-triggered reporting after contamination or supply disruption.
- **Uncertainty and data quality:** Publish a range and data-quality rating with missingness, survey recall, informal supply, contamination detection, seasonal bias, and household undercoverage documented; do not treat unknown as zero need.
- **Disaggregation and privacy:** Review privacy-safe disparities by region, income, disability, age, household type, and intersecting groups; suppress small cells, minimize retention, and restrict person-level access.
- **Evidence:** Quantitative household food-security scales, water-quality tests, service records, and supply continuity measures plus qualitative testimony from residents, Indigenous and local knowledge holders, and affected communities.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for nutritious food and safe water for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate gap repair, service redesign, and public accountability; prohibited uses include punishment, eligibility denial, policing, immigration, employment, insurance, or individual ranking; warnings require recorded human review and an appeal through the statistics and rights process.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-002 - Safe, adequate housing

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures each person’s access to safe, secure, habitable, accessible, and adequate housing free at the point of use; it excludes ownership as a proxy and treats displacement, unsafe conditions, and inaccessible design as gaps.
- **Unit and calculation:** Numerator is persons in housing that meets every approved safety, adequacy, continuity, and accessibility component and is free at the point of use; denominator is persons in scope; publish each component and do not substitute satisfaction for adequacy.
- **Baseline:** `unknown` / `not yet measured`; use a dated housing census, inspection, and resident survey for the stated reference period; progress claims are blocked until a scoped value or range is populated.
- **Scope:** All residents and people without stable housing in the adopted geography, with seasonal, emergency, rental, institutional, disability, and neighborhood service boundaries stated.
- **Stewardship:** Data steward: housing records custodian; response owner: housing-gap repair lead; independent auditor: safety and sampling auditor; publication owner: public reporting editor; affected-community contact: tenant and resident appeal route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous safety incidents, quarterly vacancy and adequacy review, annual inspections and resident sampling, and event-triggered displacement reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document hidden homelessness, address duplication, informal housing, inspection selection, rent comparability, and nonresponse bias.
- **Disaggregation and privacy:** Review privacy-safe group and regional disparities by tenure, disability, age, household type, income, displacement, and intersectional status; suppress small cells and protect addresses.
- **Evidence:** Quantitative housing census, inspection, rent-burden, habitability, and accessibility records plus qualitative testimony from tenants, unhoused residents, disability communities, and local knowledge holders.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for safe, adequate housing for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate housing repair and accessibility planning; prohibited use includes eviction targeting, benefit denial, policing, immigration, employment, insurance, or individual ranking; a human reviewer and rights appeal must address warnings.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-003 - Comprehensive physical and mental healthcare

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures timely access to continuous, culturally safe, physically and mentally accessible preventive, acute, chronic, reproductive, rehabilitative, and palliative care free at the point of use; it excludes treatment volume as proof of access.
- **Unit and calculation:** Numerator is persons able to obtain adequate covered care free at the point of use when needed, with quality and continuity components reported separately; denominator is all persons in scope, with unmet need never averaged away.
- **Baseline:** `unknown` / `not yet measured`; use dated health-survey, service-use, wait-time, and outcome methods for a stated reference period; no progress claim until the scoped baseline value or range exists.
- **Scope:** All persons in the adopted geography and care boundary, including underserved, rural, institutionalized, disabled, migrant, and culturally distinct populations and the relevant care episode window.
- **Stewardship:** Data steward: health-records custodian; response owner: care-gap repair lead; independent auditor: clinical methods auditor; publication owner: public health reporting editor; affected-community contact: patient and advocate route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous urgent-care and safety monitoring, quarterly access and wait-time reporting, annual outcomes and equity review, and event-triggered outbreak or capacity reports.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document diagnostic variation, underreporting, care-seeking differences, coding changes, missing outcomes, and comparability across providers.
- **Disaggregation and privacy:** Review privacy-safe disparities by region, age, disability, sex, race or ethnicity where lawful, income, language, and intersectional groups; use minimum cells, retention limits, and role-based access.
- **Evidence:** Quantitative coverage, wait-time, morbidity, mortality, quality, and patient-reported measures plus qualitative testimony from patients, carers, clinicians, Indigenous communities, and affected groups.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for comprehensive physical and mental healthcare for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate capacity, accessibility, and remedy planning; prohibited use includes diagnosis or ranking of an individual, benefit denial, policing, immigration, employment, or insurance decisions; warnings require human clinical and rights review plus appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-004 - Education and lifelong learning

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures each person’s access to safe, inclusive, high-quality education and lifelong learning free at the point of use, including accessibility, foundational capability, and adult pathways; it excludes attendance alone as adequacy.
- **Unit and calculation:** Numerator is persons receiving learning opportunities that meet the approved accessibility and adequacy standard and are free at the point of use; denominator is persons in scope by age and learning need; report access, quality, and completion separately.
- **Baseline:** `unknown` / `not yet measured`; use dated enrollment, participation, accessibility, learning-outcome, and survey methods for a named reference period; progress claims remain blocked until measured.
- **Scope:** Children, youth, and adults in the adopted geography, including formal, informal, vocational, disabled, remote, language-minority, and culturally specific learning boundaries.
- **Stewardship:** Data steward: education-data custodian; response owner: learning-gap repair lead; independent auditor: assessment and sampling auditor; publication owner: public learning editor; affected-community contact: learner and family route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Term or quarterly participation reporting, annual safety and adequacy review, periodic learning assessment, and event-triggered continuity reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document attendance gaps, assessment bias, language and disability measurement limits, home-learning coverage, missingness, and cohort comparability.
- **Disaggregation and privacy:** Review privacy-safe disparities by region, age, disability, language, income, gender, and intersecting groups; suppress small cells and protect learner records.
- **Evidence:** Adequacy evidence combines access and support indicators, voluntary learner reports, anonymous aggregate samples, and qualitative testimony from learners, families, educators, Indigenous and local knowledge holders, and excluded groups. These components remain separately visible so one cannot conceal failure in another.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for education and lifelong learning for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate support, accessibility, and learning-environment improvement; individual portfolios and learner records remain outside Chapter 21. Public measurement has no curriculum control and cannot dictate curriculum. There is no permanent learner ID or standardized individual-testing database, and no learner, school, community, or regional ranking. Prohibited use includes eligibility, discipline, employment, or automated adverse decisions, as well as service denial, policing, immigration, or insurance decisions; no community's guaranteed education floor may be reduced. Human review and learner appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-005 - Adequate basic energy

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures reliable, safe, sufficient, and clean-enough household energy for essential needs, including heating, cooling, cooking, lighting, and medical equipment, free at the point of use; it excludes connection alone.
- **Unit and calculation:** Numerator is persons whose service meets every approved availability, safety, adequacy, and continuity component and is free at the point of use; denominator is persons in scope; report component gaps separately. Before lawful adoption, affordability evidence describes existing conditions and transition burdens.
- **Baseline:** `unknown` / `not yet measured`; use dated utility, outage, indoor-condition, affordability, and household methods for the reference period; block progress claims until a scoped value or range is measured.
- **Scope:** All persons and households in the adopted geography, including off-grid, rural, renters, disabled residents, seasonal extremes, and the essential-energy service boundary.
- **Stewardship:** Data steward: energy-service records custodian; response owner: energy-gap repair lead; independent auditor: reliability and affordability auditor; publication owner: public utilities editor; affected-community contact: resident access route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous outage and safety monitoring, monthly or quarterly adequacy and affordability review, annual household validation, and event-triggered extreme-weather reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document estimated consumption, hidden disconnections, informal fuels, weather variation, outage measurement, and meter or household undercoverage.
- **Disaggregation and privacy:** Review privacy-safe group and regional disparities by tenure, income, disability, rurality, climate exposure, and intersecting groups; suppress small cells and protect meter data.
- **Evidence:** Quantitative outage, connection, affordability, indoor-condition, safety, and usage measures plus qualitative testimony from residents, energy-poor households, disability communities, and local knowledge holders.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for adequate basic energy for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate service repair, efficiency, and resilience planning; prohibited use includes disconnection targeting, punishment, benefit denial, policing, immigration, employment, or individual ranking; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-006 - Transportation to essential services and community life

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures each person’s practical, safe, accessible ability to reach essential services and community life using guaranteed transportation free at the point of use, including public, paratransit, walking, cycling, and other lawful modes; it excludes route availability without usability.
- **Unit and calculation:** Numerator is persons able to reach the approved destinations within the adequacy and accessibility standard using guaranteed transportation free at the point of use; denominator is persons in scope; report time, cost, reliability, safety, and disability components separately. Before lawful adoption, cost evidence describes present conditions and transition burdens.
- **Baseline:** `unknown` / `not yet measured`; use dated travel-time, service-frequency, fare, accessibility, and resident methods for a defined reference period; progress claims are blocked pending a scoped value or range.
- **Scope:** All persons in the adopted geography, including rural, remote, disabled, older, low-income, car-free, and language-minority residents and the stated destination and time window.
- **Stewardship:** Data steward: mobility-data custodian; response owner: access-gap repair lead; independent auditor: accessibility and travel-time auditor; publication owner: public mobility editor; affected-community contact: rider and pedestrian route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous incident and service data, monthly reliability review, quarterly access and affordability reporting, annual resident validation, and event-triggered disruption reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document modeled routes, missed trips, seasonal travel, safety underreporting, disability needs, and rural sampling limits.
- **Disaggregation and privacy:** Review privacy-safe disparities by region, disability, age, income, gender, vehicle access, and intersecting groups; aggregate trips, suppress small cells, and limit location retention.
- **Evidence:** Quantitative travel-time, reliability, fare, collision, accessibility, and destination-access measures plus qualitative testimony from riders, disabled residents, rural communities, and local knowledge holders.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for transportation to essential services and community life for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate route, access, safety, and affordability repair; prohibited use includes policing, migration-risk scoring, punishment, benefit denial, employment, insurance, or individual ranking; human review and appeal are mandatory.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-007 - Reliable connectivity

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures reliable, safe, and usable access to communications connectivity free at the point of use and sufficient for essential services and community life, including accessible and language-appropriate interfaces; it excludes nominal coverage alone.
- **Unit and calculation:** Numerator is persons meeting the approved availability, speed or capacity, reliability, safety, and usability components with connectivity free at the point of use; denominator is persons in scope; report affordability evidence about existing conditions and transition burdens before adoption, and do not average away any component.
- **Baseline:** `unknown` / `not yet measured`; use dated network, outage, affordability, device, and household methods for the reference period; progress claims are blocked until a scoped value or range is populated.
- **Scope:** All persons and service locations in the adopted geography, including rural, remote, disabled, low-income, public-access, and mobile or fixed service boundaries.
- **Stewardship:** Data steward: connectivity records custodian; response owner: digital-access repair lead; independent auditor: network and privacy auditor; publication owner: public connectivity editor; affected-community contact: accessible digital route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous outage and capacity monitoring, quarterly affordability and reliability reporting, annual household validation, and event-triggered disruption reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document modeled coverage, shared-device access, service quality variation, outages, affordability nonresponse, and provider comparability.
- **Disaggregation and privacy:** Review privacy-safe disparities by region, income, disability, age, language, housing status, and intersectional groups; publish aggregates, suppress cells, minimize logs, and restrict access.
- **Evidence:** Quantitative coverage, speed, outage, affordability, usage, and accessibility measures plus qualitative testimony from residents, disability groups, remote communities, and local knowledge holders.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for reliable connectivity for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate network investment and accessibility repair; prohibited use includes surveillance, content policing, benefit denial, immigration, employment, insurance, or individual ranking; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-008 - Adequate personal computing access

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures each person’s practical access to an adequate personal computing device, software, maintenance, and secure use for essential services, learning, work, and participation, all free at the point of use; it excludes shared access that cannot meet the person’s needs.
- **Unit and calculation:** Numerator is persons with the approved device, performance, availability, accessibility, maintenance, and secure-use standard, with computing free at the point of use; denominator is persons in scope; report each component separately.
- **Baseline:** `unknown` / `not yet measured`; use dated household, device, accessibility, and service-need methods for a defined reference period; progress claims are blocked until the scoped baseline is measured.
- **Scope:** All persons in the adopted geography, including children, older adults, disabled residents, low-income households, institutional settings, and the device and time boundary required for essential use.
- **Stewardship:** Data steward: device-access records custodian; response owner: computing-access repair lead; independent auditor: accessibility and security auditor; publication owner: public digital editor; affected-community contact: user support route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Quarterly device availability and repair reporting, annual household and user-needs validation, and event-triggered security or access reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document self-report, shared-device assumptions, obsolescence, repair gaps, accessibility needs, nonresponse, and vendor comparability.
- **Disaggregation and privacy:** Review privacy-safe disparities by region, income, age, disability, household type, and intersecting groups; suppress small cells, minimize identifiers, and keep device-use logs private.
- **Evidence:** Quantitative device adequacy, uptime, repair, affordability, accessibility, and secure-use measures plus qualitative testimony from users, families, disability communities, and local knowledge holders.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for adequate personal computing access for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate provision, repair, accessibility, and security planning; prohibited use includes surveillance, individual scoring, punishment, benefit denial, policing, immigration, employment, or insurance decisions; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-009 - Necessary assistive technology

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures timely access to assistive technology, fitting, training, maintenance, and replacement needed for communication, mobility, learning, care, or participation, free at the point of use; it excludes a device counted without suitability or support.
- **Unit and calculation:** Numerator is persons whose assessed assistive-technology need is met with adequate, accessible, maintained support free at the point of use; denominator is persons in scope with a relevant need; report unmet need and continuity separately.
- **Baseline:** `unknown` / `not yet measured`; use dated needs assessment, service, wait-time, and user-report methods for a stated reference period; progress claims are blocked until a scoped value or range is populated.
- **Scope:** All persons with relevant needs in the adopted geography, across age, disability, language, cultural, institutional, home, school, work, and community settings.
- **Stewardship:** Data steward: assistive-technology service custodian; response owner: accessibility-gap repair lead; independent auditor: disability-methods auditor; publication owner: accessibility reporting editor; affected-community contact: disabled-persons route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous urgent-needs and safety reporting, quarterly wait-time and continuity review, annual user validation, and event-triggered replacement reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document underdiagnosis, changing needs, device fit, service exclusion, self-report barriers, and missing maintenance data.
- **Disaggregation and privacy:** Review privacy-safe disparities by disability type, age, region, income, language, setting, and intersections; suppress small cells and protect health and functional records.
- **Evidence:** Quantitative need, wait-time, fit, continuity, replacement, and user-outcome measures plus qualitative testimony from disabled people, carers, clinicians, Indigenous and local knowledge holders.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for necessary assistive technology for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate accessibility provision and repair; prohibited use includes diagnosis or ranking of an individual, benefit denial, employment, insurance, policing, or immigration decisions; human review and rights appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### RF-BN-010 - Repair, maintenance, accessibility support, and reasonable replacement

- **Category:** Rights Floor (`RF`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Basic Needs (`BN`)
- **Definition:** Measures whether people can keep rights-floor resources usable through repair, maintenance, accessibility support, and reasonable replacement across food/water, housing, care, learning, energy, mobility, connectivity, computing, and assistive technology, with guaranteed support free at the point of use.
- **Unit and calculation:** Numerator is persons whose required support request is resolved to the approved safety, adequacy, accessibility, and continuity standard with support free at the point of use; denominator is persons with a relevant service or repair need; report delay and recurrence separately.
- **Baseline:** `unknown` / `not yet measured`; use dated repair tickets, maintenance records, replacement intervals, and resident validation for the reference period; progress claims are blocked until a scoped baseline value or range is measured.
- **Scope:** All persons and rights-floor services in the adopted geography, including disability accommodations, rural access, language needs, service interruptions, and the stated repair-to-replacement window.
- **Stewardship:** Data steward: maintenance and support records custodian; response owner: cross-service repair coordinator; independent auditor: service-quality auditor; publication owner: public repair reporting editor; affected-community contact: accessible support route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous safety and urgent repair reporting, monthly unresolved-case review, quarterly adequacy and recurrence reporting, annual service audit, and event-triggered failure reporting.
- **Uncertainty and data quality:** Publish a range and data-quality rating; document unlogged requests, closure-without-restoration, recurrence, contractor differences, missing accessibility data, and survivorship bias.
- **Disaggregation and privacy:** Review privacy-safe disparities by service, region, disability, age, income, language, and intersectional groups; suppress small cells, minimize ticket identifiers, and restrict case access.
- **Evidence:** Quantitative response time, restoration, adequacy, replacement, recurrence, and unresolved-gap measures plus qualitative testimony from residents, carers, service users, and affected communities.
- **Target rule:** Before lawful adoption, `CORE` is proposed only, not enacted. After lawful adoption, 100% adequate delivery for repair, maintenance, accessibility support, and reasonable replacement for every person in scope is the binding entitlement target; any gap triggers support, repair, and remedy. Baseline, adoption date, review date, response owner, and component-specific repair or escalation triggers must be recorded publicly, with rights-protective revision only through lawful review.
- **Use boundary:** Permitted use is aggregate repair, maintenance, capacity, and remedy planning; prohibited use includes closing cases to deny service, punishment, policing, immigration, employment, insurance, or individual ranking; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

The ten rights-floor cards are the complete UBR component set. A derived UBR summary is non-substitutive: it may orient readers, but it cannot average away, offset, or hide any failed component or delay support, repair, and remedy.

### Well-being

#### OP-WB-001 - Healthy lifespan and preventable harm

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Well-being (`WB`)
- **Definition:** Measures population life expectancy, healthy lifespan, and preventable morbidity and mortality with age, cause, scope, and diagnostic/reporting limits stated; it describes population conditions, not an individual prognosis.
- **Unit and calculation:** Report age-standardized and age-specific lifespan plus preventable morbidity and mortality rates per defined population, with numerator, denominator, reference period, and causes kept separate.
- **Baseline:** `unknown` / `not yet measured`; use dated vital statistics, health surveys, and outcome methods for the selected population and reference period; progress claims are blocked pending a scoped baseline value or range.
- **Scope:** Defined populations, ages, geography, time window, causes, and preventability definition; exclude individual prediction and disclose diagnostic, registration, and access boundaries.
- **Stewardship:** Data steward: population-health statistician; response owner: prevention and care coordinator; independent auditor: epidemiology auditor; publication owner: health reporting editor; affected-community contact: patient and community route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual life-table and mortality reporting, quarterly preventable-harm surveillance where feasible, and event-triggered reporting for outbreaks or major hazards.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document cause-of-death coding, diagnostic access, age standardization, lag, missing registration, and regional comparability bias.
- **Disaggregation and privacy:** Publish privacy-safe disparities by age, sex, region, disability, income, race or ethnicity where lawful, and intersecting groups; suppress small cells and protect health records.
- **Evidence:** Quantitative vital statistics, survey, registry, and morbidity evidence plus qualitative testimony from patients, carers, clinicians, Indigenous and local knowledge holders, and affected communities.
- **Target rule:** Use a direction or safe-range review trigger with baseline, adoption date, review date, owner, and revision triggers; no forecast or individual clinical target is implied.
- **Use boundary:** Permitted use is population prevention, service improvement, and public accountability; prohibited use includes individual prognosis, eligibility denial, insurance, employment, policing, immigration, or ranking; warnings require recorded human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-WB-002 - Population mental health and distress

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Well-being (`WB`)
- **Definition:** Measures population prevalence of distress and mental-health conditions together with access, crisis support, social context, and recovery evidence; stigma, diagnostic variation, underreporting, and crisis testimony are material limits.
- **Unit and calculation:** Report survey prevalence, distress distributions, service access, crisis response, and relevant outcomes separately by defined population and period; no aggregate result diagnoses or ranks an individual.
- **Baseline:** `unknown` / `not yet measured`; use dated representative surveys, service records, and crisis methods for a stated reference period; progress claims are blocked until a scoped baseline value or range exists.
- **Scope:** Defined populations, age groups, geography, culturally adapted instruments, time window, crisis and service boundary, and exclusions or nonresponse are explicit.
- **Stewardship:** Data steward: mental-health survey custodian; response owner: distress-support coordinator; independent auditor: measurement and ethics auditor; publication owner: public health editor; affected-community contact: confidential support and complaint route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual population survey, quarterly service and crisis reporting, continuous urgent safety monitoring where justified, and event-triggered community testimony.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document stigma, diagnostic variation, underreporting, instrument translation, crisis nonresponse, sampling, and service-record bias.
- **Disaggregation and privacy:** Review privacy-safe disparities by age, region, disability, income, gender, language, and intersectional groups; suppress small cells, minimize retention, and never release identifiable crisis records.
- **Evidence:** Quantitative prevalence, distress, access, wait-time, crisis, and outcome measures plus qualitative crisis testimony, survivor and carer testimony, and affected-community input.
- **Target rule:** Use a directional reduction in avoidable distress and improved voluntary access with baseline, adoption and review dates, owner, and revision triggers; do not set an individual happiness or diagnosis target.
- **Use boundary:** Permitted use is aggregate prevention, access, and remedy planning; prohibited use includes diagnosing, ranking, policing, employment, insurance, immigration, or benefit decisions; recorded human review and a confidential appeal route are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### AS-WB-001 - Voluntary life-satisfaction reporting

- **Category:** Aspirational End State (`AS`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Well-being (`WB`)
- **Definition:** Measures a voluntary shared life-satisfaction question and its population distribution, range, refusal, and nonresponse; the historical `8.0+/10` and Cantril `0–10` figures remain candidate examples, never a required happiness score.
- **Unit and calculation:** Report the distribution, median or mean with uncertainty, range, and response/refusal rates for the shared question; denominator is respondents and separately the sampled population, with no individual score used.
- **Baseline:** `unknown` / `not yet measured`; use a dated comparable survey question and reference period, label any local or shared value, and block progress claims until a scoped range and response quality are populated.
- **Scope:** Voluntary adults or defined population, geography, time window, language, cultural adaptation, mode, and refusal boundary; no person is required to answer.
- **Stewardship:** Data steward: well-being survey custodian; response owner: community well-being coordinator; independent auditor: survey methods auditor; publication owner: public reporting editor; affected-community contact: confidential survey and complaint route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual or biennial population survey with rotating modules, publication of response and refusal, and event-triggered qualitative follow-up.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document nonresponse, adaptation, translation, scale anchoring, mood and context effects, mode effects, and cross-cultural comparability.
- **Disaggregation and privacy:** Review privacy-safe distributions by region and relevant groups only where safe; preserve refusal/nonparticipation, suppress small cells, and prohibit person-level disclosure or linkage.
- **Evidence:** Quantitative voluntary survey distributions and the Cantril 0–10 method plus qualitative testimony about interpretation, refusal, cultural context, and lived experience.
- **Target rule:** The `8.0+/10` proposal is a candidate threshold for public discussion only; any direction or range requires baseline, adoption date, review date, owner, and revision triggers and cannot become a happiness duty.
- **Use boundary:** Permitted use is aggregate learning and service reflection; prohibited use includes requiring happiness, ranking or diagnosing people, benefit denial, employment, insurance, policing, or immigration decisions; human review and survey appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-WB-003 - Time balance, involuntary overwork, and care burden

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Well-being (`WB`)
- **Definition:** Measures time-use hours, involuntary overwork, rest, unpaid care, and unequal care burdens while distinguishing chosen work and family or cultural commitments; it is not a judgment about an individual’s chosen lifestyle.
- **Unit and calculation:** Report distributions and ranges of paid work, unpaid care, rest, commuting, and involuntary overwork by population and period; denominators and voluntary-response categories remain explicit.
- **Baseline:** `unknown` / `not yet measured`; use dated time-use diaries and labor or care surveys for a stated reference period; progress claims are blocked until a scoped value or range is measured.
- **Scope:** Defined population, age, employment, caregiving, household, geography, season, and time window; distinguish paid, unpaid, chosen, and constrained activities.
- **Stewardship:** Data steward: time-use survey custodian; response owner: work-and-care conditions coordinator; independent auditor: sampling and labor-methods auditor; publication owner: public reporting editor; affected-community contact: worker and carer route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual or biennial time-use survey, quarterly labor context where feasible, and event-triggered care-burden review.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document diary recall, proxy reporting, unpaid-work undercount, seasonal bias, cultural interpretation, and nonresponse.
- **Disaggregation and privacy:** Review privacy-safe disparities by gender, age, disability, income, household, region, employment, and intersectional groups; suppress small cells and keep diaries private.
- **Evidence:** Quantitative time-use, hours, care, rest, and involuntary-burden measures plus qualitative testimony from workers, carers, disabled people, and affected communities.
- **Target rule:** Use a direction toward reduced involuntary burden and fairer time access with baseline, adoption and review dates, owner, and revision triggers; never set a correct lifestyle or family pattern.
- **Use boundary:** Permitted use is aggregate labor, care, transport, and service redesign; prohibited use includes judging chosen work or family life, benefit denial, employment, policing, immigration, or individual ranking; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

### Sustainability

#### OP-SU-001 - Greenhouse-gas budget alignment

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Sustainability (`SU`)
- **Definition:** Measures greenhouse-gas emissions and removals against a scientifically assessed, dated, equitable carbon budget at the applicable scale; independent physical assessment is distinct from democratic adoption of the response.
- **Unit and calculation:** Report tonnes of CO2-equivalent by gas, source, sink, consumption or production boundary, and per-capita or territorial denominator; do not collapse uncertainty into one false precision.
- **Baseline:** `unknown` / `not yet measured`; use a dated inventory and budget method for the stated reference period, publish value or range, and block progress claims until scope and comparability are populated.
- **Scope:** Declared geography, sectors, gases, accounting boundary, time window, budget horizon, consumption effects, and regional or temporal scale are explicit.
- **Stewardship:** Data steward: emissions-inventory custodian; response owner: mitigation coordinator; independent auditor: inventory auditor; publication owner: climate reporting editor; affected-community contact: frontline-community route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous or monthly monitoring where available, annual inventory, periodic budget reassessment, and event-triggered disclosure after material method or climate change.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document modeled emissions, land-use uncertainty, imported goods, offsets, temporal lag, scenario assumptions, and regional comparability.
- **Disaggregation and privacy:** Review privacy-safe sector, region, household, and distributional disparities without exposing premises or travel records; suppress small cells and minimize retention.
- **Evidence:** Quantitative inventories, atmospheric observations, energy and land-use data plus qualitative testimony and Indigenous or local knowledge where relevant.
- **Target rule:** Independent science proposes a budget-alignment direction; lawful authorities adopt a response after public review, with baseline, adoption/review dates, owner, and revision triggers; no vote can erase demonstrated danger or protected rights.
- **Use boundary:** Permitted use is aggregate mitigation, adaptation, and accountability; prohibited use includes individual punishment, benefit denial, policing, immigration, employment, insurance, or automatic transition gates; warnings require recorded human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-SU-002 - Material footprint and circular recovery

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Sustainability (`SU`)
- **Definition:** Measures material extraction, consumption footprint, toxicity, waste, reuse, repair, and circular recovery across the relevant life cycle; waste diversion is narrower and remains a non-core candidate submeasure.
- **Unit and calculation:** Report material tonnes and impacts by material class and life-cycle boundary, per person or service, with recovery, reuse, repair, and residual waste calculated separately; no single score hides toxicity.
- **Baseline:** `unknown` / `not yet measured`; use dated material-flow, life-cycle, and recovery methods for a named reference period; progress claims are blocked until measured values or ranges and comparability are documented.
- **Scope:** Declared geography, supply-chain boundary, materials, sectors, waste streams, time window, and regional/temporal scale; include informal and Indigenous/local knowledge where relevant.
- **Stewardship:** Data steward: material-flow custodian; response owner: circularity coordinator; independent auditor: life-cycle auditor; publication owner: environmental reporting editor; affected-community contact: waste-worker and resident route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Quarterly operational recovery reporting, annual material-flow accounts, periodic life-cycle review, and event-triggered contamination reporting.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document trade-flow estimates, hidden waste, informal recovery, recycling quality, toxicity, allocation assumptions, and regional comparability.
- **Disaggregation and privacy:** Review privacy-safe regional, sectoral, and distributional burdens; suppress small cells, protect commercial and household records, and publish aggregate exposure.
- **Evidence:** Quantitative material-flow, life-cycle, waste, repair, reuse, and recovery data plus qualitative testimony from waste workers, residents, Indigenous and local knowledge holders, and affected communities.
- **Target rule:** Use separately adopted safe ranges or directional recovery goals with baseline, adoption/review dates, owner, and revision triggers; the waste-diversion candidate cannot replace full material-footprint assessment.
- **Use boundary:** Permitted use is aggregate design, procurement, recovery, and remediation; prohibited use includes individual punishment, service denial, employment, insurance, policing, immigration, or automatic gates; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-SU-003 - Biodiversity and ecosystem integrity

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Sustainability (`SU`)
- **Definition:** Measures species, habitat, ecological function, connectivity, and integrity at an appropriate ecological scale; ecological regeneration activity is a narrower candidate complement, not proof of recovery.
- **Unit and calculation:** Report species and habitat indicators, ecological condition, connectivity, and pressure separately by ecosystem and reference period; do not collapse distinct ecological conditions into one score.
- **Baseline:** `unknown` / `not yet measured`; use dated ecological surveys, remote sensing, and knowledge-holder methods for the stated region and reference period; block progress claims until a scoped range is measured.
- **Scope:** Declared ecosystem, species, region, season, temporal trend, pressure, and restoration boundary, including protected rights and Indigenous/local knowledge where relevant.
- **Stewardship:** Data steward: ecological-monitoring custodian; response owner: habitat protection coordinator; independent auditor: ecological methods auditor; publication owner: biodiversity editor; affected-community contact: land and community route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Seasonal or annual species and habitat monitoring, periodic ecosystem assessment, continuous pressure monitoring where feasible, and event-triggered damage reporting.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document detectability, sampling gaps, taxonomic change, lagged response, model uncertainty, spatial scale, and regional comparability.
- **Disaggregation and privacy:** Review privacy-safe regional, ecosystem, species, and community impacts; protect sensitive species locations and cultural knowledge, suppress risky detail, and limit access.
- **Evidence:** Quantitative ecological surveys, habitat and remote-sensing data plus Indigenous and local knowledge, structured testimony, and affected-community evidence.
- **Target rule:** Independent scientific and knowledge-holder assessment identifies safe conditions; democratic adoption chooses lawful responses, with baseline, adoption/review dates, owner, and stop or revision triggers; a vote cannot erase demonstrated danger or protected rights.
- **Use boundary:** Permitted use is aggregate conservation, restoration, and repair; prohibited use includes displacement, individual punishment, benefit denial, policing, immigration, employment, insurance, or automatic transition gates; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-SU-004 - Air, water, soil, and regional ecological limits

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Sustainability (`SU`)
- **Definition:** Measures air, water, soil, and other regional ecological conditions against independently assessed health and ecosystem limits, preserving separate physical conditions and regional/temporal scale.
- **Unit and calculation:** Report pollutant or condition concentrations, exposure, flow, soil function, and exceedance duration by medium and place; do not collapse air, water, soil, or limits into one score.
- **Baseline:** `unknown` / `not yet measured`; use dated monitoring, exposure, and ecological-assessment methods for the named region and reference period; progress claims are blocked until values or ranges are populated.
- **Scope:** Explicit monitoring locations, populations, ecosystems, seasons, exposure routes, time window, and regional boundary, including culturally significant places and local knowledge.
- **Stewardship:** Data steward: environmental-monitoring custodian; response owner: ecological-risk coordinator; independent auditor: measurement auditor; publication owner: environmental reporting editor; affected-community contact: frontline and land-holder route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous or seasonal monitoring by medium, quarterly public exceedance reports, annual ecological assessment, and event-triggered contamination reporting.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document sensor coverage, episodic pollution, exposure modeling, detection limits, temporal lag, spatial scale, and regional comparability.
- **Disaggregation and privacy:** Review privacy-safe regional, exposure, income, age, disability, and community disparities; protect household location, suppress small cells, and preserve sensitive cultural knowledge.
- **Evidence:** Quantitative air, water, soil, exposure, and ecological monitoring plus Indigenous/local knowledge, qualitative testimony, and affected-community evidence.
- **Target rule:** Independent assessment establishes evidence and uncertainty; lawful democratic adoption selects response and review, with baseline, adoption/review dates, owner, and revision triggers; no citizen vote can vote away demonstrated danger or protected rights.
- **Use boundary:** Permitted use is aggregate prevention, remediation, and accountability; prohibited use includes individual punishment, policing, immigration, employment, insurance, or automatic transition gates; warnings require recorded human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

### Equity

#### OP-EQ-001 - Rights-floor disparities between groups and regions

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Equity (`EQ`)
- **Definition:** Measures component-specific differences in the ten rights-floor access and adequacy results between groups and regions without exposing people; disparity averages never substitute for an individual entitlement or repair.
- **Unit and calculation:** For each RF-BN component, report privacy-safe rates, gaps, ranges, and uncertainty by defined group/region and person-in-scope denominator; preserve worst gaps and do not average components into cancellation.
- **Baseline:** `unknown` / `not yet measured`; use dated linked-but-protected service and household methods for a stated reference period; progress claims are blocked until a scoped disparity value or range is measured.
- **Scope:** All RF components, persons and regions in the adopted geography, group definitions, intersectional plan, time window, and adequacy standard are explicit.
- **Stewardship:** Data steward: disparity-statistics custodian; response owner: rights-repair coordinator; independent auditor: equity and privacy auditor; publication owner: public accountability editor; affected-community contact: community review route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Quarterly rights-floor disparity review, annual method and intersectional review, and event-triggered reporting after a credible rights harm.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document denominator coverage, missing identity data, classification, small-area estimates, nonresponse, and comparability bias.
- **Disaggregation and privacy:** Require privacy-safe group and regional disparity review, intersectional views where safe, minimum-cell suppression, privacy threat assessment, retention limits, and controlled access.
- **Evidence:** Quantitative component-specific RF results and disparity analyses plus qualitative testimony from affected groups, rights advocates, Indigenous/local knowledge holders, and service users.
- **Target rule:** Any adopted disparity trigger prompts investigation and repair of the relevant RF component; baseline, adoption/review dates, owner, and revision triggers are required, and no average excuses a gap.
- **Use boundary:** Permitted use is aggregate repair, resource support, and accountability; prohibited use includes individual ranking, punishment, benefit denial, policing, immigration, employment, or insurance; warnings require human rights review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-EQ-002 - Income and wealth concentration

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Equity (`EQ`)
- **Definition:** Measures distribution of income and wealth, preserving the Gini `<0.3` and top 1% wealth share `<20%` as candidate thresholds rather than enacted values; tax and household-survey comparability limits are explicit.
- **Unit and calculation:** Report Gini, percentile shares, median and lower-tail resources, and top-share measures separately with tax-unit/household definitions, equivalence scale, denominator, and reference period stated.
- **Baseline:** `unknown` / `not yet measured`; use dated tax, survey, and wealth-account methods for a defined reference period; progress claims are blocked until a comparable value or range is populated.
- **Scope:** Declared geography, resident or tax population, household/unit definition, assets and debts, pre/post-tax boundary, time window, and cross-country comparability limit.
- **Stewardship:** Data steward: distributional-statistics custodian; response owner: equity policy coordinator; independent auditor: tax and survey auditor; publication owner: public distribution editor; affected-community contact: resident and worker route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Quarterly income indicators where feasible, annual distributional reporting, periodic wealth-survey and tax-method review, and event-triggered disclosure after major revisions.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document tax avoidance, missing top wealth, survey nonresponse, valuation, household comparability, imputation, and cross-country limits.
- **Disaggregation and privacy:** Review privacy-safe regional, age, household, gender, disability, and intersectional disparities; suppress small cells, protect tax records, and publish only aggregate results.
- **Evidence:** Quantitative tax, household-survey, wealth-account, Gini, and top-share evidence plus qualitative testimony from affected communities and workers.
- **Target rule:** Gini `<0.3` and top 1% wealth share `<20%` are preserved candidate thresholds for public debate; any adoption needs baseline, date, owner, review, uncertainty, and revision triggers and is not enacted here.
- **Use boundary:** Permitted use is aggregate distributional analysis and policy review; prohibited use includes individual credit, employment, insurance, benefit, policing, immigration, or punishment decisions; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; candidate thresholds retained for discussion, no jurisdictional adoption implied.

#### OP-EQ-003 - Discrimination, exclusion, and effective remedy

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Equity (`EQ`)
- **Definition:** Pairs reported discrimination and exclusion incidents with underreporting, access to remedy, resolution, reversal, restoration, and testimony; complaints alone are neither prevalence nor success.
- **Unit and calculation:** Report incidents per `10,000` as one normalized proposal alongside exposure, reporting, remedy access, resolution, reversal, and restoration measures; denominators and categories remain explicit.
- **Baseline:** `unknown` / `not yet measured`; use dated complaint, audit, survey, remedy, and testimony methods for a stated reference period; progress claims are blocked until scoped values or ranges exist.
- **Scope:** Defined sectors, geography, population, protected characteristics, reporting and remedy pathways, time window, and legal or cultural limits.
- **Stewardship:** Data steward: complaints and remedy custodian; response owner: anti-discrimination remedy coordinator; independent auditor: rights and sampling auditor; publication owner: public justice editor; affected-community contact: confidential advocate route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Quarterly incident and remedy reporting, annual prevalence and underreporting study, and event-triggered review after systemic evidence or harm.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document underreporting, fear, access barriers, duplicate complaints, changing definitions, resolution bias, and non-comparable denominators.
- **Disaggregation and privacy:** Review privacy-safe disparities by sector, group, region, disability, gender, and intersectional status; suppress small cells, protect complainants, and limit retention and access.
- **Evidence:** Quantitative incidents per 10,000, audits, surveys, remedy access, resolution, reversal, and restoration plus qualitative testimony from complainants, advocates, and affected communities.
- **Target rule:** Use improved remedy access and reduced preventable exclusion as directional review rules; baseline, adoption/review dates, owner, and revision triggers are required, and lower complaints alone is not success.
- **Use boundary:** Permitted use is aggregate prevention, remedy, and accountability; prohibited use includes retaliation, individual risk scoring, employment, insurance, policing, immigration, benefit denial, or punishment; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; the per-10,000 normalization remains a proposal, no jurisdictional adoption implied.

#### OP-EQ-004 - Global productive-capacity and essential-access gaps

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Equity (`EQ`)
- **Definition:** Measures dated gaps in infrastructure, productive capability, and essential access between defined country groups or regions without ranking countries or creating global coercive authority.
- **Unit and calculation:** Report infrastructure, capability, and essential-access measures separately with person-in-scope or service denominator, dated country-group definitions, uncertainty, and no league-table composite.
- **Baseline:** `unknown` / `not yet measured`; use dated international datasets and locally validated methods for a stated reference period; progress claims are blocked until comparable group values or ranges are populated.
- **Scope:** Defined country groups, regions, infrastructure and essential services, time window, local validation, cultural context, and limitations of international comparability.
- **Stewardship:** Data steward: international-gap statistician; response owner: capacity and access coordinator; independent auditor: comparability auditor; publication owner: public global-equity editor; affected-community contact: local partner route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual international reporting, periodic infrastructure and household surveys, and event-triggered review after crisis or classification change.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document dated group definitions, missing countries, model estimates, survey comparability, infrastructure quality, and reporting bias.
- **Disaggregation and privacy:** Review privacy-safe regional and group disparities without releasing personal records; suppress small populations, protect local data sovereignty, and publish methods and access controls.
- **Evidence:** Quantitative infrastructure, productive-capacity, service-access, and dated country-group evidence plus local testimony and Indigenous/local knowledge where relevant.
- **Target rule:** Use directional gap reduction or safe-access ranges with baseline, adoption/review dates, owner, and revision triggers; no country ranking, coercive global authority, or automatic allocation rule follows.
- **Use boundary:** Permitted use is cooperative learning, capacity support, and accountable investment; prohibited use includes country punishment, migration or policing decisions, service denial, employment, insurance, or individual ranking; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

### Freedom

#### AS-FR-001 - Dependence on survival labor and work voluntariness

- **Category:** Aspirational End State (`AS`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Freedom (`FR`)
- **Definition:** Measures voluntary population reporting about whether material security permits meaningful work choice, with income, hours, care, and dependency context; the `>80%` figure is a draft scenario, never an individual classification.
- **Unit and calculation:** Report voluntary population distributions plus material dependency, hours, and involuntary constraint context; preserve refusal/nonresponse and do not infer a person’s work choice from aggregate data.
- **Baseline:** `unknown` / `not yet measured`; use dated voluntary survey and time-use/labor context for a stated reference period; progress claims are blocked until scoped values or ranges and response quality exist.
- **Scope:** Defined working-age or relevant population, geography, work and care boundaries, cultural/labor context, time window, and voluntary-response protections.
- **Stewardship:** Data steward: voluntary work survey custodian; response owner: work-choice and security coordinator; independent auditor: survey and labor auditor; publication owner: public freedom editor; affected-community contact: confidential worker route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual or biennial voluntary survey, quarterly material and labor context, and event-triggered burden review.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document social desirability, income dependency, sampling, translation, involuntary-choice interpretation, underreporting, and nonresponse.
- **Disaggregation and privacy:** Review privacy-safe population disparities by income, disability, gender, age, region, care burden, and intersectional groups; suppress cells and protect work histories.
- **Evidence:** Quantitative voluntary survey, time-use, income-security, and labor measures plus qualitative testimony from workers, carers, disabled people, and affected communities.
- **Target rule:** The `>80%` figure is a draft scenario only; any directional aspiration requires baseline, adoption/review dates, owner, and revision triggers and cannot classify or pressure an individual’s work choice.
- **Use boundary:** Permitted use is aggregate material-security and work-condition learning; prohibited use includes forcing work, benefit denial, employment, insurance, policing, immigration, or individual ranking; human review and confidential appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; draft `>80%` scenario retained, no jurisdictional adoption implied.

#### OP-FR-001 - Civic participation and representative inclusion

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Freedom (`FR`)
- **Definition:** Measures access to civic participation, representative and lottery/assembly inclusion, accessibility, response, safety, and participation context; turnout alone is insufficient and nonparticipation is not punished.
- **Unit and calculation:** Report invitation/access, inclusion, accessibility, turnout or participation, response, deliberation, and representation distributions separately by eligible population and event; no individual civic score.
- **Baseline:** `unknown` / `not yet measured`; use dated participation records, surveys, accessibility audits, and testimony for a defined reference period; progress claims are blocked until scoped values or ranges exist.
- **Scope:** Defined civic process, eligible population, geography, time window, language, disability, childcare, transport, digital, safety, and nonparticipation boundaries.
- **Stewardship:** Data steward: civic participation custodian; response owner: inclusion coordinator; independent auditor: election and accessibility auditor; publication owner: public participation editor; affected-community contact: participant and dissent route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Per-process reporting, quarterly access review, annual inclusion and response audit, and event-triggered safety or accessibility review.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document registration, self-selection, turnout denominators, inaccessible processes, duplicate participation, nonresponse, and representation bias.
- **Disaggregation and privacy:** Review privacy-safe participation and representation disparities by region, age, disability, language, income, and intersecting groups; suppress small cells and protect ballots and identity.
- **Evidence:** Quantitative access, lottery/assembly inclusion, accessibility, turnout, response, and representation data plus qualitative testimony from participants, nonparticipants, dissenters, and affected communities.
- **Target rule:** Use access, inclusion, and public-response directions with baseline, adoption/review dates, owner, and revision triggers; turnout alone is not a sufficient target and nonparticipation cannot be punished.
- **Use boundary:** Permitted use is aggregate process improvement and representative accountability; prohibited use includes coercion, individual political ranking, benefit denial, policing, employment, insurance, or immigration decisions; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### AS-FR-002 - Personal autonomy and freedom from coercion

- **Category:** Aspirational End State (`AS`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Freedom (`FR`)
- **Definition:** Measures voluntary population-level reports of autonomy alongside rights, coercion, safety, and remedy evidence; government cannot define a correct family, work, religion, culture, identity, or lifestyle.
- **Unit and calculation:** Report voluntary shared-question distributions, rights incidents, remedy access, and contextual barriers separately; preserve refusal/nonresponse and never calculate a person’s autonomy score.
- **Baseline:** `unknown` / `not yet measured`; use dated voluntary survey and rights/remedy methods for a stated reference period; progress claims are blocked until a scoped value or range and quality rating exist.
- **Scope:** Defined population, geography, coercion and remedy boundary, cultural and legal context, survey language, time window, and voluntary participation.
- **Stewardship:** Data steward: autonomy survey custodian; response owner: rights and remedy coordinator; independent auditor: human-rights and survey auditor; publication owner: public rights editor; affected-community contact: confidential support route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual or biennial voluntary survey, quarterly remedy and incident reporting, and event-triggered review after credible coercion evidence.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document stigma, fear, interpretation, underreporting, survey mode, legal-context differences, and nonresponse.
- **Disaggregation and privacy:** Review privacy-safe population disparities by region, gender, disability, age, religion or culture only where voluntary and safe; suppress cells and protect sensitive responses.
- **Evidence:** Quantitative voluntary reports, rights/remedy records, access and safety measures plus qualitative testimony from affected people, advocates, and local knowledge holders.
- **Target rule:** Use a directional aspiration for autonomy and effective remedy with baseline, adoption/review dates, owner, and revision triggers; no government-defined correct life or individual target is permitted.
- **Use boundary:** Permitted use is aggregate rights protection and remedy planning; prohibited use includes coercion, belief or lifestyle scoring, benefit denial, policing, employment, insurance, immigration, or individual ranking; human review and rights appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-FR-002 - Freedom of movement and practical access barriers

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Freedom (`FR`)
- **Definition:** Measures lawful and practical mobility access, including disability, transport, document, cost, safety, and service barriers; it is never a migration-risk or policing score.
- **Unit and calculation:** Report access to lawful travel, residence, services, and community participation by barrier and population; denominators, destinations, time window, and rights limits remain explicit.
- **Baseline:** `unknown` / `not yet measured`; use dated mobility, accessibility, document, transport, and rights-review methods for a defined reference period; progress claims are blocked until measured.
- **Scope:** Defined geography, lawful movement boundary, routes, destinations, disability and document access, cost, safety, and time window; distinguish practical from legal barriers.
- **Stewardship:** Data steward: mobility and rights-data custodian; response owner: access-barrier coordinator; independent auditor: rights and accessibility auditor; publication owner: public mobility editor; affected-community contact: migrant, disabled, and resident route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Quarterly barrier and service reporting, annual accessibility and rights review, and event-triggered reporting after restrictions or displacement.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document unreported barriers, route modeling, document status, legal changes, disability needs, safety reporting, and sampling bias.
- **Disaggregation and privacy:** Review privacy-safe disparities by disability, income, age, region, document/access status, and intersectional groups; suppress small cells and never publish identifiable movement paths.
- **Evidence:** Quantitative travel, accessibility, cost, document, route, and rights-review measures plus qualitative testimony from migrants, disabled people, residents, and local knowledge holders.
- **Target rule:** Use lawful practical-access directions with baseline, adoption/review dates, owner, and revision triggers; any restriction requires rights review and cannot be inferred from a mobility score.
- **Use boundary:** Permitted use is aggregate barrier removal and accessibility planning; prohibited use includes migration-risk scoring, policing, surveillance, individual ranking, benefit denial, employment, insurance, or immigration decisions; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

### Resilience

#### OP-RS-001 - Essential-service reliability and outages

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Resilience (`RS`)
- **Definition:** Measures service-specific uptime, outage duration, person-time affected, restoration adequacy, and disparity context for essential services; nominal capacity alone is insufficient.
- **Unit and calculation:** Report uptime, outage events and duration, affected person-time, adequacy, and group/region disparity separately by service and reference period; do not hide long outages in averages.
- **Baseline:** `unknown` / `not yet measured`; use dated service logs, outage records, and resident validation for a defined reference period; progress claims are blocked until scoped values or ranges are populated.
- **Scope:** Named essential service, geography, population, service standard, outage definition, planned/unplanned boundary, and time window.
- **Stewardship:** Data steward: service-reliability custodian; response owner: outage response lead; independent auditor: reliability auditor; publication owner: public service editor; affected-community contact: resident and user route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Continuous service monitoring, monthly or quarterly reliability reporting, annual adequacy and disparity audit, and event-triggered outage reports.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document missing logs, planned outages, sensor failure, person-time estimation, service-quality differences, and underreported household impacts.
- **Disaggregation and privacy:** Review privacy-safe disparities by service, region, disability, age, income, and intersecting groups; aggregate affected person-time, suppress small cells, and protect premises data.
- **Evidence:** Quantitative uptime, outage duration, person-time, adequacy, and disparity records plus qualitative testimony from users, frontline workers, and affected communities.
- **Target rule:** Use service-specific reliability and adequacy ranges with baseline, adoption/review dates, owner, and revision triggers; a threshold is a warning and repair trigger, not automatic punishment or funding cuts.
- **Use boundary:** Permitted use is aggregate reliability investment and repair; prohibited use includes individual eligibility, punishment, policing, employment, insurance, immigration, or service denial; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-RS-002 - Crisis response and recovery time

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Resilience (`RS`)
- **Definition:** Measures time to protect life, restore adequate service, reach affected groups, and remedy harms after a crisis; fast closure without real restoration is not success.
- **Unit and calculation:** Report time-to-protection, time-to-access, time-to-adequate-restoration, affected-group reach, unresolved harm, and remedy separately by event and population.
- **Baseline:** `unknown` / `not yet measured`; use dated incident logs, service restoration, population reach, and remedy methods for a stated reference period; block progress claims until scoped ranges exist.
- **Scope:** Declared crisis type, geography, population, service boundary, response phases, adequacy standard, recovery endpoint, and time window.
- **Stewardship:** Data steward: crisis-record custodian; response owner: recovery coordinator; independent auditor: incident and remedy auditor; publication owner: public resilience editor; affected-community contact: survivor and community route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Event-level reporting, quarterly unresolved-harm review, annual exercise and recovery audit, and immediate public updates during a continuing crisis.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document missing event times, access and reach estimates, self-report, changing endpoints, survivor underreporting, and regional comparability.
- **Disaggregation and privacy:** Review privacy-safe response and recovery disparities by region, age, disability, income, language, and intersecting groups; suppress small cells and protect survivors.
- **Evidence:** Quantitative protection, restoration, reach, adequacy, and remedy times plus qualitative survivor, frontline, and affected-community testimony.
- **Target rule:** Use phase-specific response and recovery ranges with baseline, adoption/review dates, owner, and stop or revision triggers; closure without adequate restoration or remedy is not success.
- **Use boundary:** Permitted use is aggregate preparedness, response, restoration, and remedy; prohibited use includes individual blame, benefit denial, policing, employment, insurance, immigration, or ranking; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### OP-RS-003 - Reserves, redundancy, and replacement capacity

- **Category:** Operational Indicator (`OP`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Resilience (`RS`)
- **Definition:** Measures usable, maintained, accessible, and replaceable capacity for essential services under realistic scenarios; nominal inventory alone is not evidence of resilience.
- **Unit and calculation:** Report usable reserve, redundancy, maintenance status, lead time, replacement capacity, scenario demand, and person/service coverage separately by resource and period.
- **Baseline:** `unknown` / `not yet measured`; use dated inventories, maintenance records, stress scenarios, and access tests for the reference period; progress claims are blocked until scoped values or ranges are populated.
- **Scope:** Named service/resource, geography, realistic hazard scenario, capacity definition, maintenance and replacement boundary, time horizon, and affected population.
- **Stewardship:** Data steward: capacity-inventory custodian; response owner: continuity coordinator; independent auditor: stress and maintenance auditor; publication owner: public resilience editor; affected-community contact: user and worker route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Monthly or quarterly inventory and maintenance review, annual scenario test, periodic replacement review, and event-triggered capacity disclosure.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document nominal-versus-usable capacity, maintenance backlog, supplier dependence, scenario assumptions, lead-time uncertainty, and regional gaps.
- **Disaggregation and privacy:** Review privacy-safe service and regional coverage disparities; protect critical-infrastructure security details, suppress risky small cells, and limit access to operational data.
- **Evidence:** Quantitative reserve, redundancy, maintenance, replacement, scenario, and coverage evidence plus qualitative testimony from workers, users, and affected communities.
- **Target rule:** Use service-specific usable-capacity ranges with baseline, adoption/review dates, owner, and revision triggers; nominal inventory cannot satisfy the target and warnings do not authorize automatic expansion or cuts.
- **Use boundary:** Permitted use is aggregate continuity planning and maintained capacity; prohibited use includes individual eligibility, punishment, policing, employment, insurance, immigration, or service denial; warnings require human review and appeal.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### LM-RS-001 - Stress-test and adaptation learning

- **Category:** Learning Measure (`LM`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Resilience (`RS`)
- **Definition:** Records a declared learning question about stress, adaptation, or service design with scenario, safeguards, expected benefits and harms, review, and stop conditions; simulations and pilots are not proof of real-world reliability.
- **Unit and calculation:** Report scenario inputs, tested design, outcomes, harms, uncertainty, affected groups, comparison or learning method, and stop decision separately; no individual score or right is inferred.
- **Baseline:** `unknown` / `not yet measured`; state the pre-test baseline, scenario and reference period, or explicitly record not yet measured; progress and generalization claims are blocked until populated.
- **Scope:** Named pilot or simulation, participants or affected population, geography, scenario, duration, service boundary, safeguards, and external-validity limits.
- **Stewardship:** Data steward: learning-study custodian; response owner: adaptation lead; independent auditor: ethics and methods auditor; publication owner: learning-report editor; affected-community contact: participant route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Pre-test declaration, scheduled interim review, end-of-test report, and stop-condition review before continuation; no open-ended pilot is implied.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document model assumptions, selection, simulation limits, spillovers, harms, missingness, and transferability uncertainty.
- **Disaggregation and privacy:** Review privacy-safe participant and affected-group differences; use consent, minimum cells, retention limits, access controls, and independent privacy-threat assessment.
- **Evidence:** Quantitative scenario and pilot outcomes plus qualitative participant, worker, affected-community, and Indigenous/local knowledge testimony where relevant.
- **Target rule:** The target is a declared learning question, expected benefit and harm, review date, owner, and stop conditions; a learning result informs redesign, pause, continuation, or retirement and cannot prove reliability.
- **Use boundary:** Permitted use is bounded learning and redesign; prohibited use includes individual ranking, rights reduction, benefit denial, punishment, policing, employment, insurance, immigration, or automatic transition gates; human review and appeal are mandatory.
- **Version history:** Version 1.0; initial proposed core learning card; no jurisdictional adoption implied.

### Meaning

#### AS-ME-001 - Voluntary self-reported purpose and agency

- **Category:** Aspirational End State (`AS`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Meaning (`ME`)
- **Definition:** Measures voluntary population-level reports of purpose and agency using a shared question with culturally adapted additions; government cannot define the correct source of meaning or score an individual’s beliefs, religion, family, work, lifestyle, or nonparticipation.
- **Unit and calculation:** Report population distributions, ranges, refusal, nonresponse, and culturally adapted interpretations separately; denominators distinguish respondents from the sampled population and never produce an individual score.
- **Baseline:** `unknown` / `not yet measured`; use dated voluntary survey instruments and a stated reference period, publish ranges and translation limits, and block progress claims until populated.
- **Scope:** Voluntary defined population, geography, language, culture, time window, survey mode, and refusal/nonparticipation boundary; no required meaning response.
- **Stewardship:** Data steward: purpose and agency survey custodian; response owner: community well-being coordinator; independent auditor: cultural and survey auditor; publication owner: public meaning editor; affected-community contact: confidential participant route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual or biennial voluntary survey, rotating culturally adapted modules, and event-triggered qualitative interpretation review.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document translation, interpretation, cultural variation, nonresponse, social desirability, instrument validity, and comparability limits.
- **Disaggregation and privacy:** Review privacy-safe population distributions by region and voluntarily relevant groups; preserve refusal, suppress small cells, protect sensitive beliefs, and limit access.
- **Evidence:** Quantitative voluntary shared questions and adapted instruments plus qualitative testimony, cultural interpretation, and affected-community knowledge.
- **Target rule:** Use directional population learning or a range, never a required score; baseline, adoption/review dates, owner, and revision triggers are required and no government-defined purpose is adopted.
- **Use boundary:** Permitted use is aggregate reflection and support; prohibited use includes scoring beliefs, religion, family, work, lifestyle, nonparticipation, benefit denial, policing, employment, insurance, immigration, or ranking; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### AS-ME-002 - Belonging and social connection

- **Category:** Aspirational End State (`AS`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Meaning (`ME`)
- **Definition:** Measures voluntary population-level belonging, meaningful connection, isolation context, and access to community relationships; it does not prescribe a correct family, religion, culture, community, or level of participation.
- **Unit and calculation:** Report voluntary shared-question distributions, connection opportunities, isolation context, refusal, and nonresponse separately by population and period; do not score an individual’s social life.
- **Baseline:** `unknown` / `not yet measured`; use dated voluntary survey, access, and qualitative methods for a stated reference period; progress claims are blocked until scoped values or ranges are populated.
- **Scope:** Defined population, geography, culture, language, time window, social setting, accessibility, and voluntary nonparticipation boundary.
- **Stewardship:** Data steward: social-connection survey custodian; response owner: community-access coordinator; independent auditor: cultural and sampling auditor; publication owner: public belonging editor; affected-community contact: confidential participant route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Annual or biennial voluntary survey, periodic community-access review, and event-triggered testimony after displacement or isolation harms.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document translation, cultural interpretation, social desirability, nonresponse, network measurement limits, and unequal opportunity to connect.
- **Disaggregation and privacy:** Review privacy-safe distributions by region, age, disability, language, income, household, and intersectional groups; suppress small cells and protect relationship and contact data.
- **Evidence:** Quantitative voluntary reports and access measures plus qualitative testimony from residents, isolated people, community groups, Indigenous/local knowledge holders, and affected communities.
- **Target rule:** Use a directional aspiration for connection opportunity and belonging with baseline, adoption/review dates, owner, and revision triggers; nonparticipation remains valid and no correct social form is defined.
- **Use boundary:** Permitted use is aggregate barrier removal and community support; prohibited use includes ranking people, judging family/religion/culture, benefit denial, policing, employment, insurance, immigration, or coercion; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core definition; no jurisdictional adoption implied.

#### LM-ME-001 - Opportunities for learning, creativity, culture, and contribution

- **Category:** Learning Measure (`LM`)
- **Registry status:** `CORE`: proposed Charter designation, not enacted law
- **Dimension:** Meaning (`ME`)
- **Definition:** Measures access, barriers, and opportunity to learn, create, engage in culture, and contribute; it assesses opportunity rather than whether someone makes the “right” use of it.
- **Unit and calculation:** Report opportunity availability, affordability, accessibility, participation choice, barriers, and refusal separately by population and period; no individual cultural, creative, or contribution score is calculated.
- **Baseline:** `unknown` / `not yet measured`; use dated participation, access, barrier, and voluntary survey methods for a stated reference period; progress claims are blocked until a scoped value or range exists.
- **Scope:** Defined population, geography, learning/cultural setting, language, disability access, time window, public/private boundary, and voluntary participation.
- **Stewardship:** Data steward: learning and culture survey custodian; response owner: opportunity-access coordinator; independent auditor: cultural and sampling auditor; publication owner: public opportunity editor; affected-community contact: participant and creator route; responsible citizen assembly: lawful adopting assembly.
- **Cadence:** Quarterly opportunity and access reporting where available, annual or biennial participation survey, periodic cultural review, and event-triggered access review.
- **Uncertainty and data quality:** Publish ranges and a data-quality rating; document participation self-selection, translation, cultural interpretation, informal activity, opportunity versus use, nonresponse, and comparability limits.
- **Disaggregation and privacy:** Review privacy-safe disparities by region, age, disability, income, language, culture, and intersectional groups; suppress small cells, protect creative work and identity, and limit access.
- **Evidence:** Quantitative access, affordability, barrier, participation, and opportunity measures plus qualitative testimony from learners, creators, cultural communities, Indigenous/local knowledge holders, and nonparticipants. It measures opportunity and barriers, not personal worth, correct cultural use, or learner performance; private education assessment belongs to Chapter 7, while public education pilots route to the canonical Chapter 21 rules below.
- **Target rule:** The learning question concerns equitable opportunity and barriers, not correct use; baseline, expected benefits/harms, review date, owner, and stop or redesign triggers are required.
- **Use boundary:** Permitted use is aggregate access, barrier removal, and program learning; prohibited use includes ranking contribution, judging lifestyle or culture, benefit denial, policing, employment, insurance, immigration, or coercion; human review and appeal are required.
- **Version history:** Version 1.0; initial proposed core learning card; no jurisdictional adoption implied.

### Candidate registry and pilot measures

This candidate/pilot registry preserves proposals for examination and is separate from adoption. `LOCAL` means a measure lawfully adopted in a defined jurisdiction under the shared safeguards; `CANDIDATE` means it is registered for consideration and is not core or adopted; `PILOT` means a proposed design or active time-bounded learning exercise with a declared question, safeguards, review date, and stop conditions. Each `PILOT` entry identifies its stage. Registration does not enact a rule, create a target, or authorize adverse use. The stable IDs below do not collide with the 33 proposed core IDs.

| Stable ID | Name | Category | Status | Why non-core; evidence/measurement limits | Complements core card(s) |
|---|---|---|---|---|---|
| `AS-WB-002` | Self-reported happiness | AS | `CANDIDATE` | Overlaps voluntary life satisfaction; mood, wording, culture, and nonresponse limit comparability; no required happiness score. | `AS-WB-001` |
| `OP-WB-004` | Population stress burden | OP | `CANDIDATE` | Stress scales and cortisol are context-sensitive, underreported, and not a diagnosis; needs a dated population design. | `OP-WB-002`, `OP-WB-003` |
| `OP-SU-005` | Waste diversion and recycling | OP | `CANDIDATE` | Narrow operational submeasure that can reward downcycling or export without reducing material footprint or toxicity. | `OP-SU-002` |
| `LM-SU-001` | Ecological regeneration activity | LM | `CANDIDATE` | Restoration area or activity is not proof of biodiversity or ecosystem recovery; ecological lag and counterfactuals require study. | `OP-SU-003`, `OP-SU-004` |
| `OP-EQ-005` | Equal-opportunity access | OP | `CANDIDATE` | Composite access index needs protected-group definitions, denominator comparability, and remedy evidence; cannot replace RF entitlement. | `OP-EQ-001`, RF-BN family |
| `OP-EQ-006` | Intergenerational and social mobility | OP | `CANDIDATE` | Long lags, cohort definitions, migration, and opportunity measurement limit attribution and comparability. | `OP-EQ-004`, `OP-EQ-002` |
| `AS-FR-003` | Consumer and practical choice availability | AS | `CANDIDATE` | Choice counts can ignore affordability, coercion, accessibility, market power, and ecological limits. | `AS-FR-002`, RF-BN family |
| `AS-FR-004` | Voluntary creative-expression freedom | AS | `CANDIDATE` | Participation and censorship measures vary by culture and access; must remain voluntary and non-ranking. | `LM-ME-001`, `AS-FR-002` |
| `LM-RS-002` | Climate resilience and adaptation capacity | LM | `CANDIDATE` | Capacity and plans do not prove protection or recovery; scenarios, regional hazards, distribution, and stop rules are required. | `OP-RS-001`, `OP-RS-002`, `OP-RS-003`, `OP-SU-001`, `OP-SU-004` |
| `OP-RS-004` | Economic stability and shock exposure | OP | `CANDIDATE` | GDP volatility and unemployment omit household security, informal work, distribution, and shock exposure; context is needed. | `OP-RS-001`, `OP-RS-003`, `OP-EQ-002` |
| `AS-ME-003` | Voluntary spiritual well-being | AS | `CANDIDATE` | Spiritual instruments are culturally and religiously diverse; participation must remain voluntary and cannot define correct belief. | `AS-ME-001`, `AS-ME-002` |
| `OP-ME-001` | Stakeholder and institutional trust | OP | `CANDIDATE` | Trust surveys are context- and wording-sensitive; trust is not proof of rights delivery, remedy, or institutional performance. | `OP-FR-001`, `OP-EQ-003`, `AS-ME-002` |
| `OP-ED-001` | Timely and adequate learning support | OP | `PILOT` | Proposed pilot design: measure whether requested learning and accessibility support arrives adequately and on time; local operational evidence cannot score learners or replace the education rights floor. | `RF-BN-004` |
| `AS-ED-001` | Voluntary learner experience and self-defined progress | AS | `PILOT` | Proposed pilot design: use voluntary reports of agency, safety, belonging, and progress toward learner-chosen goals; nonresponse is valid and no correct personality, purpose, or pace is defined. | `RF-BN-004`, `AS-ME-001`, `AS-ME-002` |
| `LM-ED-001` | Anonymous foundational-ability sample | LM | `PILOT` | Proposed pilot design: use a voluntary rotating anonymous sample and a small shared research protocol; it is not an individual exam, learner record, curriculum mandate, or ranking instrument. | `RF-BN-004`, `LM-ME-001` |
| `OP-ED-002` | Education access, support, and outcome disparities | OP | `PILOT` | Proposed pilot design: use privacy-safe aggregates, context, uncertainty, and testimony to find group or regional gaps; small cells are protected and findings trigger support rather than punishment. | `RF-BN-004`, `OP-EQ-001` |

Registration alone makes no row `LOCAL` and does not activate a `PILOT`. A local adoption still requires its own scope, baseline, owner, review date, safeguards, and public record. Before a pilot exercise begins, a public activation record must document lawful approval under the applicable authority lane, purpose and scope, baseline and status, owner, safeguards, review date, and stop conditions. The four education `PILOT` entries are proposed designs, not active exercises.

#### Education pilot measurement rules

This subsection is the canonical Chapter 21 boundary for education-specific public measurement. It does not replace Chapter 7's private formative evidence, consent, credentials, or fair-access rules, or Chapter 9's learner-data privacy, local-only processing, retention, and breach remedies.

Education pilots use voluntary, privacy-protected public evidence. Learning communities perform local aggregation and send Chapter 21 only group summaries. Small or identifying cells then receive small-cell protection through combination, suppression, or qualitative reporting. Raw-sample deletion follows aggregate validation. Chapter 21 receives no individual learner record, portfolio, learner-held credential, or standardized individual-testing database. The anonymous foundational-ability pilot uses a low-burden rotating sample, not universal testing, and participation follows Chapter 7 consent rules. Refusal is consequence-free and cannot affect education, support, credentials, or opportunity. The independent statistics office addresses participation gaps through accessible outreach, transparent uncertainty, and additional volunteers, never coercion.

The independent statistics office proposes a protected reselection interval based on population, burden, evidence quality, and re-identification risk. A citizen assembly adopts and reviews that interval, and no learner is selected again within it unless they independently volunteer. A citizen assembly adopts a small shared foundation; local additions are allowed after consultation with learners, educators, developmental specialists, disability advocates, rights experts, and cultural communities, but cannot remove the shared rights-protecting floor or impose a worldview. The common research protocol examines aggregate trends and rights-floor gaps. It is not an individual exam, does not enter a learner record, has no curriculum control, and authorizes no ranking. In every report, uncertainty remains visible alongside testimony and local context.

The four bounded pilots remain separate: support timeliness and adequacy, voluntary learner experience and self-defined progress, anonymous foundational-ability sampling, and privacy-safe access, support, and outcome disparities. Evidence combines support/access indicators, voluntary learner experience, anonymous samples, privacy-safe disparities, and structured qualitative testimony. Each component remains separate; no combined score may hide failure in another component. The pilots are not universal, scientifically settled, or targets.

Governance is divided. The citizen assembly approves purpose, safeguards, permitted uses, interval, status, and review date. The independent statistics office designs methods, evaluates quality, reports uncertainty, and publishes aggregates. Communities collect voluntarily and locally. Administrators repair shortfalls but cannot control evaluation. The privacy authority and education-rights advocate audit and remedy, and courts hear rights cases. Promotion requires reliability for the limited purpose, accessibility, cultural fairness, privacy, anti-gaming evidence, meaningful affected-learner and community support or acceptance, independent rights review, and citizen-assembly approval. A credible unresolved rights violation blocks promotion; a failed pilot is revised, returned to pilot, or retired.

`RF-BN-004` remains the guaranteed education floor. Evidence can direct additional support only, such as educators, accessibility support, devices, transportation, facilities, or related help. There is no funding cut, closure, or punishment because of weak results, and no automatic formula. Accountable human review and local testimony are required. A breach or misuse triggers prompt notice, correction, deletion, harm-reduction help, compensation where warranted, and proportionate accountability; unsafe systems may be suspended. A breach never weakens continued education or support.

### Complete dimension-table crosswalk

The dimension tables below provide concise proposal crosswalks, not a second canonical metric set. Each row maps to a core card, a registered non-core ID, or an illustrative example; thresholds and examples retain their original proposal or evidence status.

| Dimension-table measure or proposal | Disposition |
|---|---|
| Basic Needs: Food Security | `RF-BN-001` |
| Basic Needs: Housing Adequacy | `RF-BN-002` |
| Basic Needs: Healthcare Access | `RF-BN-003` |
| Basic Needs: Energy Access | `RF-BN-005` |
| Basic Needs: Digital Access | `RF-BN-007` and `RF-BN-008` |
| Basic Needs: UBR Adequacy | `RF-BN-001` through `RF-BN-010`, non-substitutive component set |
| Well-being: Life Satisfaction | `AS-WB-001`; `8.0+/10` remains a candidate threshold and Cantril `0–10` a method example |
| Well-being: Mental Health | `OP-WB-002` |
| Well-being: Physical Health | `OP-WB-001` |
| Well-being: Happiness | `AS-WB-002` candidate |
| Well-being: Stress Levels | `OP-WB-004` candidate |
| Well-being: Work-Life Balance | `OP-WB-003` |
| Sustainability: Carbon Footprint | `OP-SU-001` |
| Sustainability: Resource Efficiency | `OP-SU-002` |
| Sustainability: Biodiversity | `OP-SU-003` |
| Sustainability: Waste Reduction | `OP-SU-005` candidate; narrower than material footprint |
| Sustainability: Regeneration | `LM-SU-001` candidate |
| Sustainability: Planetary Boundaries | `OP-SU-004` |
| Equity: Income Inequality | `OP-EQ-002`; Gini `<0.3` remains a candidate threshold |
| Equity: Wealth Inequality | `OP-EQ-002`; top 1% wealth share `<20%` remains a candidate threshold |
| Equity: Opportunity Access | `OP-EQ-005` candidate |
| Equity: Discrimination | `OP-EQ-003`; incidents per `10,000` remains a normalized proposal |
| Equity: Social Mobility | `OP-EQ-006` candidate |
| Equity: Global Equity | `OP-EQ-004` |
| Freedom: Work Voluntariness | `AS-FR-001`; `>80%` remains a draft scenario |
| Freedom: Choice Availability | `AS-FR-003` candidate |
| Freedom: Political Participation | `OP-FR-001` |
| Freedom: Personal Autonomy | `AS-FR-002` |
| Freedom: Creative Freedom | `AS-FR-004` candidate |
| Freedom: Freedom of Movement | `OP-FR-002` |
| Resilience: Economic Stability | `OP-RS-004` candidate |
| Resilience: Infrastructure Redundancy | `OP-RS-003` |
| Resilience: Social Cohesion | `AS-ME-002` and candidate `OP-ME-001` |
| Resilience: Adaptation Capacity | `LM-RS-002` candidate |
| Resilience: Crisis Response | `OP-RS-002` |
| Resilience: System Robustness | `OP-RS-001` and `OP-RS-003` |
| Meaning: Purpose Fulfillment | `AS-ME-001` |
| Meaning: Community Connection | `AS-ME-002` |
| Meaning: Creative Expression | `LM-ME-001` and candidate `AS-FR-004` |
| Meaning: Learning Engagement | `LM-ME-001` |
| Meaning: Spiritual Well-being | `AS-ME-003` candidate |
| Meaning: Contribution Feeling | `LM-ME-001` |

The crosswalk preserves the cited evidence sources, current cadences, international learning values, hypothetical 2024/2030 advisor scenario, qualitative `95% housing satisfaction` example, Abundance Index `>80/100` formulas and weights, hypothetical baseline/target values, and 25+ point worked-example gap below. None is an adopted baseline, forecast, binding target, or universal threshold merely because it appears in this chapter.

---

## Why Traditional Metrics Fail

### What GDP Misses

Gross Domestic Product grew out of national accounting work in the 1930s, including work by Simon Kuznets, and those accounts were used in wartime planning. GDP was designed to measure national economic output, not to provide a complete measure of human well-being.[^ch21-bea-national-accounts]

[^ch21-bea-national-accounts]: The U.S. Bureau of Economic Analysis traces national accounts to work led by Simon Kuznets for a 1934 report to Congress and explains their wartime planning use. GDP is an output measure; the conclusion that it is incomplete as a well-being measure follows from that definition and its exclusions: https://www.bea.gov/index.php/news/blog/2012-04-09/gdp-and-national-accounts-one-great-inventions-20th-century

**What GDP Measures:**
- Market transactions
- Economic output
- Production volume
- Income flows

**What GDP Misses:**
- Human well-being and flourishing
- Non-market value (care work, volunteering)
- Environmental degradation
- Inequality and distribution
- Quality of life
- Sustainability and long-term viability
- Freedom and autonomy
- Meaning and purpose

**The Result:** A society can have rising GDP while people become poorer, sicker, more stressed, and less free.

### Examples of GDP Failure

| GDP Measures | Reality It Misses |
|--------------|-------------------|
| Healthcare spending as "growth" | Poor health requiring treatment |
| Disaster reconstruction as "growth" | Devastation and loss |
| Prison construction as "growth" | Social failure and crime |
| Commuting fuel consumption as "growth" | Inefficient urban design |
| Long work hours as "growth" | Lack of leisure and family time |
| Advertising expenditure as "growth" | Artificial demand creation |

### What Bad Measures Encourage

Current metrics create perverse incentives:

1. **Growth at any cost** - Environmental destruction counts as economic progress
2. **Income and wealth distribution remain invisible** - GDP records aggregate output without showing how gains are distributed; output can rise while gains are concentrated among a small number of people.
3. **Most unpaid care and volunteer work is outside GDP** - GDP does not record most unpaid childcare, eldercare, and volunteer work as market output.
4. **Resource depletion counted as income** - Cutting down forests increases GDP
5. **Short-term focus** - Quarterly GDP masks long-term unsustainability

**The response:** Use several dimensions to measure what matters for a dignified life.

---

## The Seven Dimensions of Abundance

### The Abundance Metrics Framework

The framework organizes abundance measurement into seven dimensions, each containing specific indicators. The table below provides an overview; detailed metrics for each dimension follow below.

**Table 1:** The Seven Dimensions of Abundance Framework

| Dimension | Indicators |
|---|---|
| 1. Basic Needs | Food; Housing; Healthcare; Energy; Digital |
| 2. Well-being | Life satisfaction; Mental health; Happiness |
| 3. Sustainability | Carbon footprint; Biodiversity; Resource efficiency; Waste reduction |
| 4. Equity | Inequality; Opportunity; Mobility; Discrimination |
| 5. Freedom | Work voluntariness; Political participation; Autonomy |
| 6. Resilience | Economic stability; Social cohesion |
| 7. Meaning | Purpose fulfillment |

*Table 1: The seven dimensions form an integrated framework for measuring abundance. Each dimension contains multiple indicators that together provide a comprehensive view of societal health.*

Each dimension represents an aspect of abundance this Charter considers important. Together, they could give a broader view than GDP alone. The following metrics and thresholds are draft proposals for debate, not validated cutoffs; methods, data, uncertainty, and governance still need to be specified. In this chapter, a **target** is a proposed value or milestone that must name a baseline, scope, owner, review date, uncertainty, and revision or stop conditions. A target is not a forecast or guarantee.

> **Status guide:** Before lawful adoption, percentages such as 100% access, 80% work voluntariness, and other thresholds in this chapter are **proposals or draft targets for debate**, not current coverage findings or binding local targets. After lawful adoption, an RF target of 100% adequate delivery is a binding entitlement and any gap requires repair and remedy. Current measurements remain **established evidence** only when supported by a dated source and stated scope.

---

## Dimension tables and crosswalks (not a second canonical metric set)

The dimension tables below provide evidence, examples, and proposal context. They do not define a competing core or adopted targets: the cards and registry above own shared IDs, fields, status, baselines, and use boundaries. Read each row through the complete dimension-table crosswalk; its figures remain candidate thresholds, dated evidence, or illustrative scenarios with their original caveats.

### Dimension 1: Basic Needs

Without meeting basic needs, no other form of flourishing is possible. This dimension forms the foundation upon which all other aspects of abundance depend.

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Food Security** | 100% (access) | % with consistent access to nutritious food |
| **Housing Adequacy** | 100% (access) | % with safe, adequate housing |
| **Healthcare Access** | 100% (coverage) | % with comprehensive healthcare coverage |
| **Energy Access** | 100% (access) | % with reliable, clean energy |
| **Digital Access** | 100% (access) | % with high-speed internet access |
| **UBR (Universal Basic Resources) Adequacy** | 100% | % whose core necessities and universal enabling services meet the approved adequacy standard |

**Target Justification:** Before lawful adoption, access targets of 100% are draft proposals representing the moral imperative that basic needs should be universally guaranteed. After lawful adoption, an RF target of 100% adequate delivery is binding and a shortfall requires repair, support, and remedy. These rights checks differ from satisfaction metrics, which vary based on individual preferences and regional conditions and cannot substitute for access or adequacy.

**Data Sources:**
- Household surveys (e.g., Food Security Experience-Based Scales)
- Government statistics (housing census, utility records)
- Health records and coverage data
- Energy utility data and grid statistics
- Internet connectivity surveys and broadband deployment data

**Measurement Notes:** Access metrics track availability and coverage; satisfaction metrics capture quality and user experience. Regional variations in needs definitions should be accounted for through localized indicators.

**Why It Matters:** Basic needs are the foundation of human dignity. When everyone's basic needs are met, society shifts from survival to flourishing.

**Chen Family Example:** In one possible scenario, the Chen family lives in a community where 100% of residents have secure housing, nutritious food, and comprehensive healthcare. Their children receive free education, and the community has universal high-speed internet. This illustrates the proposed access floor, not measured coverage or an achieved result.

---

### Dimension 2: Well-being

Meeting basic needs is necessary but not sufficient. People need to feel good about their lives and experience positive psychological states.

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Life Satisfaction** | 8.0+/10 | Gallup World Poll scale |
| **Mental Health** | Low prevalence | Depression/anxiety rates |
| **Physical Health** | High | Life expectancy, disease rates |
| **Happiness** | High | Self-reported happiness |
| **Stress Levels** | Low | Stress surveys, cortisol levels |
| **Work-Life Balance** | High | Time use surveys |

**Data Sources:**
- World Happiness Report (Gallup World Poll data)
- National health surveys (e.g., NHIS, BRFSS)
- Mental health epidemiology studies (e.g., WHO World Mental Health Survey)
- American Time Use Survey, European Time Use Survey
- OECD Better Life Index, self-report well-being surveys

**Measurement Notes:** Life satisfaction uses the Cantril Ladder scale (0-10). Mental health prevalence tracked via DSM-5/ICD-11 diagnostic criteria. Stress measured through perceived stress scales and physiological indicators where available.

**Why It Matters:** Well-being is the subjective experience of flourishing. High well-being indicates that people are thriving.

**Key Insight:** Supportive relationships and a sense of purpose are important to well-being alongside material security.[^ch21-relationships-wellbeing][^ch21-purpose-wellbeing]

---

### Dimension 3: Sustainability

Abundance must be sustainable across generations. This dimension ensures that current prosperity does not compromise the ability of future generations to meet their needs.

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Carbon Footprint** | Net zero/negative | CO2 emissions per capita |
| **Resource Efficiency** | High | Material use per GDP |
| **Biodiversity** | Net positive | Species diversity, habitat |
| **Waste Reduction** | Near zero | Waste per capita, recycling rate |
| **Regeneration** | Positive | Ecosystem restoration metrics |
| **Planetary Boundaries** | Within evidence-informed limits | Boundary indicators appropriate to scale, with uncertainty and regional variation |

**Data Sources:**
- National carbon inventories, GHG protocol calculations
- Environmental monitoring networks (air, water, soil quality)
- Biodiversity surveys (e.g., IUCN Red List, Living Planet Index)
- Waste management statistics, circular economy indicators
- Satellite imagery (NASA Earth Observatory, ESA Sentinel)

**Measurement Notes:** Carbon footprint measured in CO2-equivalent per capita. The planetary-boundaries framework tracks nine Earth-system processes, but the Charter treats those boundaries as evidence-informed, uncertain, regionally varying, equity-sensitive constraints subject to formal revision rather than as one immutable number.[^ch21-planetary-boundaries] Regeneration measured through reforestation rates, soil health indices, and habitat restoration area.

[^ch21-planetary-boundaries]: The 2023 planetary-boundaries update assessed nine Earth-system processes and concluded that six boundaries were transgressed. The framework is a scientific model for assessing risk, not a complete measurement standard for every Charter sustainability target: https://www.stockholmresilience.org/research/research-news/2023-09-13-all-planetary-boundaries-mapped-out-for-the-first-time-six-of-nine-crossed.html

**Why It Matters:** Unsustainable abundance is an illusion. True abundance must be regeneratively produced and maintained.

**The Shift:** From value capture to regeneration, from waste to circularity, from depletion to renewal.

---

### Dimension 4: Equity

Abundance must be shared, not concentrated. Extreme inequality undermines social cohesion and prevents widespread flourishing.

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Income Inequality** | Low | Gini coefficient < 0.3 |
| **Wealth Inequality** | Low | Top 1% share < 20% |
| **Opportunity Access** | Equal | Equal Opportunity Index (education, employment, housing access across demographics) |
| **Discrimination** | Minimal | Reported discrimination incidents per 10,000 population (normalized across categories) |
| **Social Mobility** | High | Intergenerational mobility |
| **Global Equity** | Improving | Global inequality measures |

**Data Sources:**
- World Inequality Database (WID), Luxembourg Income Study (LIS)
- Equal Opportunity Index, Social Progress Index
- Equal Employment Opportunity Commission reports, discrimination audit studies
- Intergenerational mobility studies (e.g., Chetty et al. equality of opportunity project)
- World Inequality Report, global household survey data

**Why It Matters:** Extreme inequality undermines social cohesion, reduces economic efficiency, and concentrates political power.

**The Goal:** Equity of opportunity and dignity.

---

### Dimension 5: Freedom

Abundance expands freedom, not restricts it. True abundance gives people the capacity to choose their path rather than forcing survival labor.

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Work Voluntariness** | >80% | % working by choice, not necessity |
| **Choice Availability** | High | Consumer choice indices |
| **Political Participation** | High | Voter turnout, civic engagement |
| **Personal Autonomy** | High | Autonomy surveys |
| **Creative Freedom** | High | % of population participating in creative/cultural activities; censorship indices |
| **Freedom of Movement** | High | Travel and migration freedom |

**Data Sources:**
- Labor force surveys, work motivation questionnaires (e.g., Gallup Work and Well-being)
- Voter turnout data, civic engagement surveys
- Freedom House indices, World Justice Project Rule of Law Index
- Self-Determination Theory autonomy scales, general autonomy surveys
- Arts participation surveys, UNESCO cultural statistics
- Migration policy indices, passport power rankings

**Why It Matters:** True abundance expands human agency. People should be free to choose their path, not forced into survival labor.

**The Transformation:** From forced labor to chosen work, from constraint to possibility, from survival to self-determination.

---

### Dimension 6: Resilience

Abundance must persist through challenges. Resilient systems can withstand shocks, adapt to changing conditions, and recover from setbacks.

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Economic Stability** | High | GDP volatility, unemployment |
| **Infrastructure Redundancy** | High | Backup systems, capacity |
| **Social Cohesion** | High | Trust surveys, community metrics |
| **Adaptation Capacity** | High | Innovation, response time |
| **Crisis Response** | Effective | Response time, outcomes |
| **System Robustness** | High | Failure rates, recovery time |

**Data Sources:**
- Economic indicators (GDP volatility, unemployment rates, inflation)
- Infrastructure audits and reliability reports
- Social trust surveys (e.g., World Values Survey, General Social Survey)
- Innovation metrics (R&D investment, patent filings, startup formation)
- Crisis response data (disaster response times, recovery metrics)

**Measurement Notes:** Economic stability measured through coefficient of variation in GDP growth and unemployment volatility. Social cohesion assessed via trust surveys and community participation rates. Adaptation capacity evaluated through innovation indices and response time benchmarks.

**Why It Matters:** Fragile abundance collapses under pressure. Resilient systems adapt and persist.

**The Lesson:** The pandemic showed how fragile supply chains and social systems can be. Abundance must be built on redundancy and adaptability.

---

### Dimension 7: Meaning

Humans need more than material security. They need purpose. Meaning and connection are essential for psychological well-being and fulfillment.

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Purpose Fulfillment** | High | Purpose in life surveys |
| **Community Connection** | High | Social connection indices |
| **Creative Expression** | High | Participation in creative activities |
| **Learning Engagement** | High | Lifelong learning participation |
| **Spiritual Well-being** | High | Spiritual fulfillment surveys |
| **Contribution Feeling** | High | Sense of contributing to society |

**Data Sources:**
- Purpose in Life scales (e.g., Ryff Psychological Well-being Scales, Meaning in Life Questionnaire)
- Social Connectedness Index, General Social Survey social capital modules
- Arts and cultural participation surveys, UNESCO culture statistics
- PISA lifelong learning data, adult education participation rates
- Spiritual well-being scales (e.g., FACIT-Sp, Spiritual Transcendence Scale)
- Community contribution surveys, Bureau of Labor Statistics volunteer data

**Measurement Notes:** Purpose measured through validated psychometric instruments. Community connection assessed via social network size and frequency of meaningful interactions. Creative expression tracked through participation rates in arts, crafts, and cultural activities. Learning engagement measured through lifelong learning participation.

**Why It Matters:** Without meaning, material abundance leads to emptiness. Purpose is essential for psychological well-being.

**The Insight:** In a study of 12,998 U.S. adults over 50, higher purpose was associated with greater life satisfaction four years later after accounting for income, wealth, and other factors.[^ch21-purpose-wellbeing] Supportive social relationships are also linked with well-being.[^ch21-relationships-wellbeing]

[^ch21-relationships-wellbeing]: Ed Diener and Martin E. P. Seligman, “Beyond Money: Toward an Economy of Well-Being” (2004), review of research on social relationships and well-being: https://doi.org/10.1111/j.0963-7214.2004.00501001.x

[^ch21-purpose-wellbeing]: Eric S. Kim, Ying Chen, Julia S. Nakamura, Carol D. Ryff, and Tyler J. VanderWeele, “Sense of Purpose in Life and Subsequent Physical, Behavioral, and Psychosocial Health: An Outcome-Wide Approach” (2022). Prospective observational study of 12,998 U.S. adults over 50; higher purpose was associated with greater life satisfaction four years later after adjustment for income, wealth, and other factors. The association does not establish causation: https://doi.org/10.1177/08901171211038545

---

## The Abundance Index

### The Abundance Index Calculation

This Charter proposes a composite **Abundance Index** as a way to discuss progress. It is an illustrative design, not a measured global score or a validated decision rule. The weights below express draft priorities for different phases and need public debate, sensitivity testing, and a decision process before use.

**Illustrative target for debate:** Abundance Index > 80 (on a proposed 0–100 scale)

**Normalization still to be designed:** The example formulas assume each dimension can be placed on a 0–100 scale. Before anyone calculates a real score, the project must choose actual datasets, indicator definitions, baselines, normalization rules, aggregation methods, missing-data treatment, uncertainty reporting, and who can revise the weights. Z-scores and min-max normalization are options, not established methods for this index.

The **disaggregated dashboard comes first**: indicator-level results, trends, ranges, gaps, testimony, and data-quality ratings are presented before any composite. The Abundance Index remains a transparent, experimental, sensitivity-tested, secondary summary with published weights, normalization, missing-data rules, uncertainty, alternate-weight results, and version history. The index is not a rights-compliance test, and it cannot decide rights compliance, funding, sanctions, service eligibility, or automatic transitions or gates. It may not rank jurisdictions, countries, cultures, or people in a league table.

#### 1. The Transition Index (Chapter 24 transition periods: Foundation and Expansion)
*Focus: Systemic Stability and Foundation Building*
During the transition, the primary goal is to ensure the new systems are established without catastrophic failure. Basic Needs and Well-being share the highest illustrative weights at 20% each. Resilience's 10% weight reflects its role in managing transition risks and systemic shocks.

**Formula:**
```
Transition Abundance Index =
  (Basic Needs × 20%) +
  (Well-being × 20%) +
  (Sustainability × 15%) +
  (Equity × 15%) +
  (Freedom × 15%) +
  (Resilience × 10%) +
  (Meaning × 5%)
```

**Weight Rationale (Transition):**
- **Basic Needs (20%)** - Essential foundation; without food, shelter, and health, no other dimension can be realized.
- **Well-being (20%)** - Vital for social stability during rapid change; represents the subjective experience of the transition.
- **Sustainability (15%)** - Ensures the transition itself doesn't destroy the planetary foundations.
- **Equity (15%)** - Prevents the social fragmentation caused by extreme inequality during reorganization.
- **Freedom (15%)** - Protects human agency as old structures are dismantled.
- **Resilience (10%)** - Critical for surviving the "Transition Chaos" and systemic shocks.
- **Meaning (5%)** - While important, it is treated as a secondary focus compared to the immediate need for stability and survival.

#### 2. The Flourishing Index (Chapter 24: Global Floor and Maturity)
*Focus: Existential Fulfillment and Human Agency*
Once the material and stability foundations are secured, the focus shifts toward the psychological challenges of post-scarcity. Meaning and human agency remain central to progress: Meaning rises from 5% to 15%, while Freedom remains at 15%, alongside Well-being, Sustainability, and Equity. Basic Needs has the highest weight at 20%, and Resilience falls from 10% to 5%.

These indices are measurement workstreams, not transition gates by themselves. Their baselines, cadence, and thresholds inform Chapter 24 gate decisions alongside rights, safety, capacity, ecological, funding, and legitimacy evidence; no score or year boundary advances a community automatically.

**Formula:**
```
Flourishing Abundance Index =
  (Basic Needs × 20%) +
  (Well-being × 15%) +
  (Sustainability × 15%) +
  (Equity × 15%) +
  (Freedom × 15%) +
  (Resilience × 5%) +
  (Meaning × 15%)
```

**Weight Rationale (Flourishing):**
- **Meaning (15%)** - In a post-scarcity world, the "Meaning Crisis" is the primary challenge; it becomes a core metric for success.
- **Well-being (15%)** - Remains a core outcome, but the focus shifts from "survival/stability" to "thriving/fulfillment."
- **Resilience (5%)** - Once systems are mature and stable, the relative weight of resilience decreases as a primary management concern.
- **(All other dimensions maintain their baseline weights: Basic Needs: 20%, Sustainability: 15%, Equity: 15%, Freedom: 15%)**

### Shared-reference and local-cultural views

Comparisons use two visibly separate, non-substitutable views:

- **Shared-reference view:** a common transparent formula and common definitions for limited cross-jurisdiction learning where scope, baseline, and uncertainty make an indicator-by-indicator or trend comparison meaningful. It identifies practices to study; it does not create a best-to-worst ranking.
- **Local-cultural view:** locally selected questions, interpretations, or weights chosen through rights-respecting local processes, with culturally adapted additions and published translation and interpretation limits. It supplements rather than replaces the shared rights floor.

Local-cultural interpretation cannot override individual rights, silence internal dissenters, or turn a majority culture into a compulsory personal standard. Subjective well-being, purpose, autonomy, belonging, religion, spirituality, and cultural practice remain voluntary population-level evidence and never become an individual score.

---

### Example Dashboard: Current vs. Target

*Note: Every "current" value and status below is a hypothetical dashboard placeholder, not a measured 2024 world baseline. The proposed targets also need public debate. Real implementation requires data collection, verification, and a reproducible method.*

**Methodological Notes:**
- Current-column values are illustrative placeholders, not calculated global averages
- Status indicators: Yellow = making progress but below target; Red = significant gap requiring intervention
- Data confidence varies by metric; some estimates have wider margins of error

| KPI | Illustrative baseline, not measured | Draft target | Illustrative status |
|-----|----------------|--------|--------|
| **Basic Needs Coverage** | 70% | 100% | In Progress (Yellow) |
| **Life Satisfaction** | 6.5/10 | 8.0/10 | In Progress (Yellow) |
| **Carbon Footprint** | 4.5t/capita | Net Zero | Needs Improvement (Red) |
| **Gini Coefficient** | 0.45 | <0.30 | Needs Improvement (Red) |
| **Work Voluntariness** | 40% | >80% | Needs Improvement (Red) |
| **Social Trust** | 45% | >70% | In Progress (Yellow) |
| **Purpose Fulfillment** | 50% | >80% | In Progress (Yellow) |
| **Mental Health Rate** | 18% disorder | <10% | Needs Improvement (Red) |
| **Biodiversity Index** | -30% from baseline | Net Positive | Needs Improvement (Red) |
| **Political Participation** | 60% turnout | >80% | In Progress (Yellow) |

**Illustrative Abundance Index score:** ~55/100; not a measured current score

**Draft target Abundance Index:** >80/100

**Illustrative gap in this example:** 25+ points across multiple dimensions; not a measured global gap

---

## Implementation

### Data Collection Methods

Effective measurement requires systematic data collection across multiple methods and frequencies.

| Method | Use | Frequency |
|--------|-----|-----------|
| **Surveys** | Self-reported well-being | Annual |
| **Administrative Data** | Basic needs coverage | Continuous |
| **Environmental Monitoring** | Sustainability metrics | Continuous |
| **Economic Data** | Equity, freedom metrics | Quarterly |
| **Community Feedback** | Qualitative insights | Ongoing |
| **Independent Audits** | Verification | Annual |

### Transparency Requirements

Transparency ensures accountability and enables public trust in measurement systems.

**Public Dashboards:**
- Real-time access to key metrics
- Interactive visualizations
- Regional comparisons
- Historical trends

**Annual Reports:**
- Comprehensive progress review
- Analysis of trends
- Identification of problem areas
- Recommendations for improvement

**Independent Verification:**
- Third-party audits of data
- Methodology transparency
- Peer review of findings

**Community Input:**
- Local feedback mechanisms
- Participatory data collection
- Qualitative stories and experiences

---

### Global Policy Advisor Example: Using Metrics for Improvement

*Note: The data below is a hypothetical example demonstrating how the framework could be applied to track progress over time, not actual reported data.*

Nadia Okafor, a fictional policy advisor, uses the Abundance Index to track her local community's progress.

For this hypothetical example, treat percentages as 0–100 values, multiply Well-being's score out of 10 by 10, and leave values already out of 100 unchanged. Use the same Transition Index weights for both dates: Basic Needs 20%, Well-being 20%, Sustainability 15%, Equity 15%, Freedom 15%, Resilience 10%, and Meaning 5%. The normalization method for real-world use remains open.

**2024 Baseline:**
- Basic Needs: 85%
- Well-being: 6.8/10
- Sustainability: 45/100
- Equity: 52/100
- Freedom: 60/100
- Resilience: 55/100
- Meaning: 58/100
- **Overall Index: 62.55/100** (17 + 13.6 + 6.75 + 7.8 + 9 + 5.5 + 2.9)

**2030 Progress:**
- Basic Needs: 98%
- Well-being: 7.6/10
- Sustainability: 72/100
- Equity: 68/100
- Freedom: 75/100
- Resilience: 70/100
- Meaning: 72/100
- **Overall Index: 77.65/100** (19.6 + 15.2 + 10.8 + 10.2 + 11.25 + 7 + 3.6)

**Key Insights:**
- Basic needs nearly achieved through UBR implementation
- Well-being improved with mental health infrastructure
- Sustainability remains the biggest challenge
- Equity improved through wealth reallocation
- Freedom expanded with work transformation

**Next Priorities:**
1. Accelerate carbon reduction
2. Increase biodiversity restoration
3. Address remaining inequality gaps
4. Build more community connection spaces

**The Power of Metrics:** Nadia can see exactly where progress is happening and where more work is needed. The data guides policy decisions and resource allocation.

---

## Beyond Numbers

### Qualitative Measures

Numbers matter, but they do not capture everything. Qualitative measures add depth and context:

**Methods:**
- **Community Stories** - Personal narratives of change
- **Focus Groups** - Deep dives into specific issues
- **Ethnographic Research** - Observational studies of daily life
- **Artistic Expression** - Creative interpretations of well-being
- **Philosophical Dialogue** - Reflection on values and purpose

**Why Qualitative Matters:**
- Captures nuance that numbers miss
- Reveals unexpected outcomes
- Humanizes the data
- Provides context for quantitative findings
- Surfaces issues not captured in metrics

**Example:** A quantitative metric might show "95% housing satisfaction." Qualitative research reveals that while housing is adequate, many residents feel isolated in large complexes. This prompts investment in community spaces.

---

### The Danger of Metrics

Metrics can create problems when they are misused. Responsible measurement has to account for those risks.

**Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure."[^ch21-goodhart-law]

[^ch21-goodhart-law]: OECD uses this popular formulation when discussing measurement and target-setting. It is commonly called Goodhart's Law, although the exact wording is a later popular formulation rather than necessarily Goodhart's original sentence: https://www.oecd.org/en/publications/measuring-science-and-innovation-for-sustainable-growth_3b96cf8c-en/full-report/the-case-for-measuring-science-and-innovation-for-sustainable-growth_085c5592.html

**Risks:**
- **Gaming the system** - Optimizing for metrics rather than outcomes
- **Tunnel vision** - Focusing only on what's measured
- **Unintended consequences** - Metrics creating new problems
- **Reductionism** - Complex human experience reduced to numbers

**Mitigations:**
- Multiple metrics for each dimension
- Regular review and adjustment of metrics
- Qualitative checks on quantitative data
- Transparency about limitations
- Focus on progress, not perfection

**The Principle:** Metrics are tools for learning and improvement, not targets to hit at all costs.

---

## Data governance, evidence, privacy, and appeals

The dictionary uses the minimum-necessary data for the stated purpose. Personal records remain private. Public releases make definitions, formulas, methods, privacy-safe aggregates, uncertainty, data-quality ratings, audit findings, and version history inspectable without releasing raw personal records.

Missing data is shown as **unknown**, never as zero need or success. Modeled, imputed, or estimated values are separately labeled with their assumptions, range, and uncertainty. Every result publishes an uncertainty range or interval and a data-quality rating; an estimate alone cannot establish rights compliance, declare a target achieved, or authorize a restriction.

Where privacy permits, disaggregation includes relevant geography, age, disability, income, gender, race or ethnicity, Indigenous status, and locally meaningful groups. Intersectional views are used only where safe. Small or identifying cells are suppressed, combined, or otherwise protected, with retention and access controls documented. Open methods and aggregate results do not authorize surveillance or re-identification.

Numbers are accompanied by structured qualitative evidence and affected-community testimony, especially from affected and marginalized people. Testimony can reveal missing harms and test whether a construct matches lived experience; it is not converted into an individual sentiment score or treated as the sole proof of compliance.

AI may assist analysis as auditable **decision support only**. It cannot make final decisions, rank people, or determine eligibility, remedy, punishment, or transition. A warning or model output requires recorded human review, public reasons, and a route to challenge the data, meaning, or use.

Universal prohibited uses apply to every population metric and composite: no individual eligibility decision, benefit denial, punishment, policing, immigration decision, employment decision, insurance decision, credit decision, education ranking, surveillance, or other adverse decision; no funding cut to a struggling community; and no metric or composite may weaken rights, conceal disparities, or automate a transition gate.

### Correction and appeal route

The route is usable by residents, communities, stewards, and affected organizations:

1. A suspected data error goes to the statistics office, which preserves the disputed record and publishes a response, correction, affected versions, and public correction/version history where appropriate.
2. A disputed definition, sample, method, or data-quality rating goes to the independent auditor and statistics function for independent review and correction.
3. A dispute affecting an individual's or group's rights goes to the Chapter 8 rights and court process for binding remedy and further appeal.
4. A proposed change to a lawfully adopted core metric, target, or major policy use goes to a citizen assembly after public, expert, and affected-community review. Courts handle rights; assemblies handle major policy or core-rule changes.
5. A local measure remains challengeable through its local assembly and independent review and cannot weaken a universal guarantee.

### Local extensions and review lifecycle

Local indicators may supplement the shared dictionary under the same card, privacy, uncertainty, prohibited-use, correction, and appeal rules. Each local measure requires a stable local namespace, baseline status, named owner, independent auditor, geographic and population scope, review or expiry date, version history, and a path for proposing it for core consideration. Local status does not imply universal adoption.

Administrators and the statistics office publish at least annual reports. A newly selected citizen assembly reviews the dictionary, methods, targets, and misuse risks at least every four years. Earlier review is required after rights harm, a major data failure, material scientific change, credible evidence of systematic bias, or a qualifying public petition. Review may continue, revise, pause, replace, or retire a measure while preserving its stable ID and version history. Population size may inform a separate assembly-reselection cooldown but does not change this metric-review minimum.

---

## Measurement Feasibility, Scale, and Timing

### Data Availability and Feasibility

Not all proposed metrics are equally measurable with current data infrastructure:

**Readily Available Metrics:**
- Basic needs coverage (housing, healthcare, energy) - government statistics
- Carbon emissions - environmental monitoring agencies
- Income inequality - household surveys, tax data
- Education participation - education department records

**Metrics Requiring Enhanced Infrastructure:**
- Mental health prevalence - requires regular population surveys
- Work voluntariness - specialized employment surveys
- Social cohesion/trust - periodic social capital studies
- Purpose fulfillment - well-being surveys with validated instruments

**Emerging/Research Metrics:**
- Biodiversity net gain - requires ecological monitoring networks
- Creative expression participation - arts/culture participation surveys
- Freedom of movement - migration policy indices

**Data Collection Considerations:**
- Cost-effectiveness: Balance precision with collection costs
- Privacy: Publish privacy-safe aggregates, suppress or combine small cells, and protect against identification so personal records remain confidential
- Frequency: Match measurement cadence to metric dynamics
- Quality: Establish data validation and verification protocols

### Temporal Measurement Standards

**Tracking Frequency:**
- **Continuous:** Administrative data (basic needs coverage, energy access)
- **Quarterly:** Economic indicators (GDP, unemployment, inequality)
- **Annual:** Well-being surveys, environmental metrics, education outcomes
- **Biennial/Quinquennial:** Comprehensive household surveys, biodiversity assessments

**Temporal Comparability:**
- Maintain consistent methodologies across time periods
- Adjust for demographic changes using per-capita or age-standardized measures
- Document methodological changes and provide bridge calculations
- Establish baseline periods for trend analysis

### Geographical Scale Considerations

**Appropriate Measurement Scales:**
- **Individual/Household:** Well-being, basic needs satisfaction, time use
- **Community/Local:** Social cohesion, access to services, environmental quality
- **Regional:** Economic stability, infrastructure adequacy, employment opportunities
- **National:** Policy effectiveness, inequality, sustainability metrics
- **Global:** Climate impact, international equity, biodiversity

**Aggregation Principles:**
- Disaggregate data to identify inequities across demographics and regions
- Avoid masking disparities through excessive aggregation
- Use weighted averages that account for population size
- Report privacy-safe aggregate and disaggregated results

### Handling Metric Trade-offs

Some metrics may have tensions or require balancing:

**Known Trade-offs:**
- **Economic stability vs. Innovation:** Excessive stability may reduce dynamism; maintain buffers while encouraging experimentation
- **Equality vs. Achievement incentives:** Balance equity with recognition of exceptional contributions
- **Centralization vs. Local autonomy:** Coordinate at appropriate scales while preserving local flexibility

**Approach to Trade-offs:**
- Identify and explicitly acknowledge tensions
- Establish threshold levels below which neither goal is achievable
- Use deliberative processes to determine appropriate balances
- Monitor for unintended consequences of optimization

### Baseline Establishment Methodology

Before tracking progress:

1. **Assess Data Availability:** Identify existing data sources and gaps
2. **Set Initial Baselines:** Use a measured local or shared reference where available; where historical data is missing, record `unknown` or `not yet measured`, or use a separately labeled estimate only with assumptions and uncertainty. Chapter 21 never invents a jurisdictional baseline.
3. **Document Uncertainty:** Record confidence levels and margins of error
4. **Establish Measurement Protocols:** Standardize collection methods going forward
5. **Adjust for Quality:** Refine baselines as data quality improves

**Handling Missing Data:**
- Show missing values as `unknown`, not zero need or success
- Use proxy indicators or statistical estimation only when clearly labeled, with documented assumptions and uncertainty
- Prioritize data infrastructure development for critical gaps

### Technology Opportunities and Challenges

**Emerging Technologies:**
- **Big Data:** Real-time metrics from digital platforms, IoT sensors
- **AI/ML:** Pattern detection, predictive analytics, and data quality improvement, with predictive analysis limited to auditable advisory support, recorded human review, and the prohibited-use rules above
- **Blockchain:** Transparent, auditable data provenance
- **Satellite Imagery:** Environmental monitoring, development assessment

**Challenges:**
- **Privacy:** Detailed data collection raises surveillance concerns
- **Bias:** Algorithmic systems may perpetuate existing inequalities
- **Access:** Digital divides may exclude vulnerable populations
- **Security:** Centralized data repositories create attack targets

**Principles:**
- Collect minimum necessary data
- Ensure transparency in data use
- Protect individual privacy and autonomy
- Maintain human oversight of automated systems

### Stakeholder Engagement

**Participatory Measurement:**

Who should be involved in the measurement process:

- **Community Members:** Define what matters, interpret results, provide context
- **Subject Matter Experts:** Ensure methodological rigor, identify best practices
- **Policy Makers:** Align metrics with decision-making needs
- **Marginalized Groups:** Ensure metrics capture their experiences and needs
- **Civil Society:** Provide independent verification and advocacy

**Engagement Methods:**
- Community forums for metric selection and review
- Citizen assemblies for priority-setting
- Participatory data collection (citizen science)
- Regular feedback loops between data producers and users

**Benefits:**
- Increases legitimacy and trust in metrics
- Surfaces issues that experts might miss
- Builds capacity for data literacy and use
- Ensures metrics serve those they measure

---

## Global Comparison

### International Benchmarks

Abundance societies should compare themselves to each other to:
- Learn from successes and failures
- Establish best practices
- Encourage friendly, constructive learning without league tables
- Track global progress

**Non-ranked learning examples:** *The scores below are hypothetical prompts for discussion, not measured country scores, forecasts, or verified rankings. The values cannot decide rights, funding, eligibility, or transition.*

- **Nordic Model: illustrative 68/100:** study welfare institutions, income distribution, well-being, and basic-needs delivery while examining sustainability and growth-dependency trade-offs.
- **Bhutan: illustrative 62/100:** study meaning, sustainability, and cultural preservation alongside basic-needs and economic-capacity questions; its approach is not copied unchanged or compared directly with this proposed index.
- **Illustrative Abundance Community: hypothetical 77.65/100 in a projected 2030 example:** this illustration uses the 2030 score from Nadia’s fictional community above. Use indicator-level learning about basic needs and freedom while investigating sustainability and resilience; it is not a forecast or measured baseline.
- **Target Abundance Society: aspirational 85/100 example:** retain the proposal that all dimensions matter and that improvement is continuous; it is not an adopted target or a league-table destination.

**Learning from Others:**

- **Nordic countries** (Norway, Denmark, Sweden, Finland) are useful places to study welfare institutions and income distribution. The OECD's 2024 comparison found Nordic countries among those with the lowest disposable-income inequality in its dataset.[^ch21-oecd-nordic-inequality] That finding does not prove identical well-being outcomes across all four countries or settle their consumption and funding trade-offs.

- **Bhutan** has measured Gross National Happiness through a survey covering nine domains, including psychological well-being, health, education, time use, culture, and ecology. Its most recent national GNH survey was in 2022.[^ch21-bhutan-gnh] This is an example of a broader measurement design, not proof that it can be copied unchanged or compared directly with the Charter's proposed index.

- **Costa Rica** shows why a dated measure matters. Its electricity system has often had a high renewable share; the national utility reported that renewable sources met 86.8% of domestic electricity demand in 2024.[^ch21-costa-rica-electricity-2024] Forest recovery and biodiversity protection are separate outcomes that need their own time series before being presented as one combined success claim.

- **Singapore** is a case for studying housing policy and urban services. Its statistics office reports that 90.8% of **resident households** lived in owner-occupied homes in 2024; that is not ownership by every resident or a measure of housing affordability.[^ch21-singapore-housing-2024] Infrastructure, digital access, work-life balance, and autonomy need separate indicators before drawing a broader judgment.

- **New Zealand** organized its 2019 Wellbeing Budget around five wellbeing priorities and used a broader set of information than economic and fiscal indicators alone.[^ch21-new-zealand-wellbeing-budget] That documents a budgeting approach, not proof of its long-term outcomes or continued use in the same form.

- **Scotland** published a National Performance Framework with outcomes and indicators spanning health, education, environment, and communities. The Scottish Government says the version last updated in August 2024 has been archived while reforms are considered.[^ch21-scotland-npf] The framework's existence does not by itself establish improved outcomes.

[^ch21-oecd-nordic-inequality]: OECD, *Society at a Glance 2024*, reports that Nordic and some central European countries had the lowest levels of disposable-income inequality in its comparison. It does not give one common outcome for every Nordic country: https://www.oecd.org/en/publications/2024/06/society-at-a-glance-2024_08001b73/full-report/income-and-wealth-inequalities_7ac4178f.html

[^ch21-bhutan-gnh]: The Centre for Bhutan and GNH Studies describes periodic national surveys across nine domains and identifies 2022 as the latest survey: https://bhutanstudies.org.bt/%F0%9F%8C%8F-%F0%9D%90%88%F0%9D%90%A7%F0%9D%90%AD%F0%9D%90%9E%F0%9D%90%AB%F0%9D%90%A7%F0%9D%90%9A%F0%9D%90%AD%F0%9D%90%A2%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%9A%F0%9D%90%A5-%F0%9D%90%83%F0%9D%90%9A/ and https://www.gnhcentrebhutan.org/gnh-happiness-index/

[^ch21-costa-rica-electricity-2024]: Costa Rica's Instituto Costarricense de Electricidad, *Informe de atención de demanda y producción de electricidad con fuentes renovables, Costa Rica 2024*, reports 86.8% of domestic electricity demand met by renewable sources in 2024. Its definition includes imports as nonrenewable in the demand measure: https://apps.grupoice.com/CenceWeb/documentos/3/3008/23/INFORME%20GENERACION%20RENOVABLE%202024.pdf

[^ch21-singapore-housing-2024]: Singapore Department of Statistics reports 90.8% of resident households in owner-occupied dwellings in 2024. This is a household-tenure measure, not a claim about all people or affordability: https://www.singstat.gov.sg/modules/infographics/-/media/Files/visualising_data/infographics/Population/singapore-population29092025.pdf

[^ch21-scotland-npf]: Scottish Government's National Performance Framework collection says the framework last updated in August 2024 has been archived pending reform; its published framework lists outcomes and indicators across multiple domains: https://www.gov.scot/collections/national-performance-framework/ and https://nationalperformance.gov.scot/sites/default/files/documents/NPF_A4_Booklet.pdf

[^ch21-new-zealand-wellbeing-budget]: New Zealand Treasury's 2019 Wellbeing Budget organized new spending around five wellbeing priorities and described the budget as using a broader set of measures than economic and fiscal indicators alone. It does not establish long-term outcomes: https://www.treasury.govt.nz/publications/wellbeing-budget/wellbeing-budget-2019

**Regional Variations:**

Different regions face distinct challenges and opportunities. These are non-ranked discussion prompts, not measured regional scores; any comparison should be rebuilt from local data and the views of people who live there:

- **Northern Europe:** study social welfare and low inequality while examining high consumption and carbon footprint.
- **East Asia:** study infrastructure, education, and safety while examining work-life balance and aging populations.
- **Latin America:** study community cohesion and cultural richness while examining inequality and economic instability.
- **Sub-Saharan Africa:** study social capital and resource potential while examining basic-needs access and infrastructure.
- **North America:** study innovation capacity and resources while examining inequality and social fragmentation.

**The Goal:** Learn and adapt successful approaches from other regions to local contexts.

---

## Why Metrics Matter

**Metrics are values made visible.** What we measure signals what we value and determines what receives attention, resources, and policy priority.

**Traditional Metrics Signal:**
- Economic growth above all other considerations
- Individual consumption as the primary measure of success
- Short-term gains over long-term sustainability
- Market transactions only, ignoring unpaid and informal work

**Abundance Metrics Signal:**
- Human well-being and dignity as the ultimate goal
- Shared prosperity and coordinated well-being
- Long-term sustainability across generations
- Multiple dimensions of human experience beyond economics

### The Seven Dimensions Recap

| Dimension | Why It Matters |
|-----------|----------------|
| **Basic Needs** | Foundation of human dignity; prerequisite for all other flourishing |
| **Well-being** | Quality of life experience; the subjective outcome that matters most |
| **Sustainability** | Long-term viability; ensures abundance persists for future generations |
| **Equity** | Fair distribution; prevents concentration of power and opportunity |
| **Freedom** | Human agency; abundance should expand choice, not restrict it |
| **Resilience** | System robustness; ensures persistence through shocks and crises |
| **Meaning** | Purpose and fulfillment; addresses the human need for significance |

### Principles for Abundance Metrics

| Principle | Application |
|-----------|-------------|
| **Comprehensive** | Measure all dimensions of abundance, not just economic output |
| **Transparent** | Open methods and privacy-safe aggregate data, with personal records kept private, enable accountability |
| **Actionable** | Metrics inform accountable human decisions and support allocation; they do not trigger automatic action or adverse use |
| **Comparable** | Enable comparison across regions and over time |
| **Adaptive** | Evolve with new understanding and changing circumstances |
| **Human-Centered** | Focus on lived quality of life, not abstract aggregates |

---

## System Interconnections & Cross-References

These measures connect to and support the following chapters:

- **Chapter 1 (Day in Life)** - The Chen family's illustrative scenario can be considered through these metrics
- **Chapter 2 (Eight Systems)** - Each system has associated metrics
- **Chapter 6 (Economy)** - Economic metrics beyond GDP
- **Chapter 10 (Technology Access)** - Digital divide metrics
- **Chapter 24 (Transition Roadmap)** - Milestones measured by these indicators
- **Chapter 15 (Failure Modes)** - Early warning indicators
- **Chapter 18 (Sustainability)** - Environmental metrics in detail
- **Chapter 19 (Global Equity)** - International comparison metrics
- **Chapter 22 (What You Can Do)** - Local measurement and advocacy

---

## Measuring What Improves People's Lives

In an abundance society:

- **Metrics matter** - What we measure gets attention
- **Transparency** - Everyone can see progress
- **Continuous improvement** - Data drives better decisions
- **Holistic view** - Beyond GDP to genuine societal health
- **Accountability** - Public scrutiny of progress
- **Learning** - Metrics help us understand what works

**The goal is meaningful progress toward human dignity and well-being, not bureaucratic scorekeeping.**

We measure so we can learn, adapt, hold public institutions accountable, and ensure technology directly improves people's lives and repairs the planet. The next chapter turns to what individuals, organizers, and communities can do now.
