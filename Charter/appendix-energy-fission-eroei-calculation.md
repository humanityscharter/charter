---
letter: H
slug: appendix-energy-fission-eroei-calculation
title: 'Fission EROEI Calculation: Inputs and Limits'
subtitle: Current AP1000 evidence, scenario limits, and a separate ESBWR material study
---

# Fission EROEI Calculation: Inputs and Limits

## Current AP1000 result and limits (2026-09-25)

Strict AP1000 EROEI: **NOT ESTABLISHED**. People supported: **NOT ESTABLISHED**.
The figure **109,206** is a hypothetical annual arithmetic scenario, not a measured
number of people supplied. It combines one observed year of net generation with
assumed lifecycle energy, delivery, and service-budget inputs. A complete AP1000
physical-energy ledger, same-service demand, hourly reliability, successor
construction, and material/resource feasibility have not been established.

| Input | Value and status | Source or boundary |
|---|---|---|
| Vogtle Unit 4 net generation | **7,831,892 MWh = 28.1948112 PJ** observed for calendar 2025 | EIA's [final 2025 EIA-923 generator file](https://www.eia.gov/electricity/data/eia923/xls/f923_2025.zip), plant 649, nuclear unit 4. One observed year does not establish lifetime output. |
| Net summer capacity and annual capacity factor | **1,114 MW** and **80.255978% (80.26%)** observed for 2025 | EIA's [final 2025 EIA-860 generator file](https://www.eia.gov/electricity/data/eia860/xls/eia8602025.zip), generator 4. The annual factor describes 2025 only. |
| Lifecycle energy reserve | **1.5 PJ/year** assumed: 0.5 capital/successor, 0.5 fuel cycle, 0.25 operation/maintenance/refueling, 0.125 waste/decommissioning, and 0.125 grid/storage equipment | Scenario assumption, not measured Vogtle input. Net generation already subtracts station-service electricity, so it is not charged again. |
| Delivery and storage | **90% delivered** assumed | A judgment buffer, not a measured plant-specific transmission, storage, or firming factor. |
| Annual service budget | **220 GJ/person-year** assumed | Delivered-electricity-equivalent budget for services associated with a 2024 U.S. standard of living. The [EIA 2024 end-use balance](https://www.eia.gov/totalenergy/data/monthly/) and [2024 Census population estimate](https://www.census.gov/newsroom/facts-for-features/2025/fourth-of-july.html) provide context; they do not validate same-service substitutions or the budget. |

The displayed arithmetic is `floor(((28.1948112 − 1.5) × 0.90) ÷ 0.000220) = 109,206`. The result is an annual scenario quotient, not a people-supported count. Equal joules do not establish equal services, and the arithmetic does not test outage timing or hourly demand. The lifecycle reserve is an assumption; a [Lawrence Livermore study of a conventional 1,000-MWe light-water reactor](https://digital.library.unt.edu/ark:/67531/metadc827635/m2/1/high_res_d/1073129.pdf) provides only an order-of-magnitude comparison, not AP1000 inputs.

The [2018 AP1000 dissertation](https://www.cmu.edu/ceic/assets/docs/publications/phd-dissertations/2018/travis-carless-phd-thesis-2018.pdf) gives modeled materials, fuel-process inputs, and lifecycle *greenhouse-gas* results. Emissions do not provide a physical-energy inventory. A complete, non-overlapping record is still needed for materials, construction, the fuel cycle, operation, maintenance, waste, and decommissioning.

For today's U.S. service basket, [EIA's 2024 electricity table](https://www.eia.gov/electricity/annual/table.php?t=epa_02_02.html) records 4,110,422,353 MWh of final electricity use, including direct use. That is 14,797.5204708 PJ of electricity, **not** the electricity needed to supply every current service. Heating, transportation, industrial processes, and public services still need careful fuel-to-useful-service conversions; the commercial electricity row already includes public-service electricity and must not be counted again. The [Census 2024 population estimate](https://www.census.gov/newsroom/facts-for-features/2025/fourth-of-july.html) supplies a matching-year denominator, but dividing by it now would turn missing services into zero. For a separate future sensitivity, [NREL models about 6,700 TWh of 2050 high-electrification electricity use](https://www.osti.gov/servlets/purl/1785329), while electricity is only about 36% of final energy in that scenario. It is not today's lifestyle and not an all-services total.

Any future people-supported estimate would require a complete service-equivalent demand and the ability to meet it hour by hour, including outages, storage or other firming, successor construction, and material, land, water, skills, ecological, safety, and waste limits. An annual quotient would be an upper bound, not proof that one reactor independently supplies all those services.

## Separate design evidence: ESBWR material estimate

Peterson, Zhao, and Petroski's 2005 [UC Berkeley material-input study](https://fhr.nuc.berkeley.edu/wp-content/uploads/2014/10/05-001-A_Material_input.pdf), Table 4, estimates **104,231 m³ of concrete** and **50,099 metric tons of total metal** for a **1,500 MWe ESBWR**, a Generation III+ design. These are approximate design estimates, some derived by scaling, not an as-built bill of materials. “Total metal” already includes reinforcing steel; adding a separate rebar line would double-count it. The study does not provide a complete lifecycle-energy inventory. These ESBWR material estimates are not AP1000 inputs.

## Historical within-study comparison

[Weißbach and colleagues (2013)](https://festkoerper-kernphysik.de/Weissbach_EROI_Energy.pdf) used one exergy-based calculation method, without converting electrical output into a fossil-fuel “primary-energy equivalent.” Under that paper's **unbuffered, technology-level** cases, it reported **4.0** for German rooftop polycrystalline PV (Table 3), **16** for an E-66 wind turbine at its specified German site (Table 5), and **75** for its reference nuclear plant with the paper's mixed enrichment assumption (**105** with its 100%-centrifuge alternative; Table 8). These are the paper's 2013 scenarios, not current technology values, Charter results, or estimates for either the ESBWR or AP1000. The cases have different sites and lifetimes, and the wind table says decommissioning energy is unknown. The unbuffered comparison omits load matching, storage, backup, curtailment, and a shared-grid boundary. The paper provides buffered PV and wind variants, but not a symmetrically buffered or load-matched whole-system case for every technology.

## Common lifecycle boundary

A defensible result for a named plant and period needs material masses and embodied-energy factors without double-counting; mining grade and method; fuel conversion, enrichment technology and electricity mix; fabrication and refueling schedule; construction and transport; operation and maintenance; waste management; decommissioning; and any storage or grid additions needed to compare delivered electricity. Each input needs a source, unit, uncertainty, and designation as primary energy, heat, or electricity. The [EROEI framework](#appendix-appendix-energy-eroei-framework) sets out the common boundary.

Published nuclear EROEI figures, including studies summarized by the [World Nuclear Association](https://world-nuclear.org/information-library/energy-and-the-environment/energy-return-on-investment), cannot be ranked against each other merely because they are ratios. A comparison needs the same delivered-electricity point and lifetime, the same lifecycle phases and electricity-quality convention, and the same treatment of storage, curtailment, and grid work. This appendix establishes no cross-technology ranking.
