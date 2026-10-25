---
letter: F
slug: appendix-energy-cost-formula
title: Energy Cost Formula in Post-Scarcity
subtitle: 'Mathematical Derivations: Labor, Capital, and Marginal Energy Accounting'
---

# Energy Cost Formula in Post-Scarcity

## Mathematical Analysis: Is Everything Just the Cost of Energy?

---

## Introduction

This appendix asks whether energy cost alone can describe the cost of producing goods in a post-scarcity world using fusion and fission. It provides physical-accounting detail for Chapter 6 (Economy and Funding), which governs funding, payments, and allocation. The equations and examples here do not adopt user prices, payment duties, tax rates, or allocation rules.

The model assumes an energy system with no profit margin and a positive lifecycle energy balance: it supplies more usable energy than it consumes. Materials and equipment still require energy to obtain and replace. The model also checks limits that energy alone cannot remove. Removing profit, interest, or rent from a price does not make a reactor, a factory, or a person's work physically costless. The question is whether the whole system can keep supplying the services people need, including the energy and resources required to rebuild itself.

---

## Step 1: Traditional Cost Structure

In a conventional economy, the price of a good typically includes:

```
Price_cur = Labor_cur + Materials_cur + Energy_cur + Capital_cur + Land_cur + Risk/Profit_cur + Scarcity_Premium_cur
```

| Component | Description | Illustrative ranges; not sector measurements |
|-----------|-------------|---------------|
| Labor | Wages, benefits | 30-60% |
| Materials | Raw inputs, components | 15-40% |
| Energy | Power for production | 2-10% |
| Capital | Equipment, facilities (depreciation) | 5-15% |
| Land | Rent, property costs | 2-8% |
| Risk/Profit | Margin for investors | 5-20% |
| Scarcity Premium | Monopoly pricing, patents | Variable |

---

## Step 2: What Changes in Post-Scarcity?

- AI and robotics handle most production (labor becomes optional)
- Public ownership could reduce profit motives for guaranteed essentials, while accountability and public choices still matter
- Direct guarantees could reduce some scarcity premiums; residual scarcity remains for land, materials, capacity, unique goods, and other constrained resources
- This scenario assumes public ownership of basic resources

---

## Step 3: The Energy-Only Hypothesis

**Alternative energy-only pricing hypothesis:**
> "All basic goods and services are priced at their marginal energy cost"
> "The marginal cost of producing basic goods approaches the cost of electricity alone"

**Question:** Is energy the ONLY cost, or are there other residual costs?

The fuller accounting rule used by this Charter is that energy accounting is one input alongside materials, land, labor and care, maintenance, storage and grid needs, waste, safety, ecological effects, and competing uses. The quotations above are hypotheses under examination, not a promise that energy alone determines price or allocation.

Throughout this appendix, kWh quantities and any currency-per-kWh conversion are illustrative calculations for physical-accounting analysis. They are not adopted user prices, payment duties, tax rates, or allocation rules, and they do not authorize charging for guaranteed essentials.

The [current AP1000 evidence check](#appendix-appendix-energy-fission-eroei-calculation) is a test of that question, not an answer by assertion. For an operating Vogtle Unit 4 reference, its plant EROEI and a U.S.-lifestyle people-supported count are **not established** because the physical lifecycle and service-demand ledgers are incomplete.

> **Important Distinction, EROEI vs. Energy-Cost Pricing:**
> EROEI (Energy Return on Energy Invested) measures whether an energy system produces a net positive energy balance across its full lifecycle. It is a measure of energy-system viability, not a production cost model. EROEI is an **input** to energy-cost pricing calculations. A higher EROEI means a smaller lifecycle energy-investment ratio, `I_supply = 1 / EROEI`, for the same boundary and energy-quality convention. Within the abundance framework's full decision structure, EROEI is one input alongside planetary boundary compliance, circular economy compatibility, governance fit, economic feasibility, and technology maturity. See the separate [EROEI Calculation Framework](#appendix-appendix-energy-eroei-framework) for the full method.

---

## Step 4: Mathematical Analysis

**For a specified automation/public-provision scenario, or as a separately labeled component of a larger monetary account, one illustrative subtotal is:**

```
C_monetary_subtotal,cur(G) = E_purchased,direct(G) × P_e,cur + C_material,cur(G) + C_cap,cur(G) + C_land,cur(G)
```

Where:
- `E_purchased,direct(G)` = Direct production energy purchased for G, in kWh at a stated delivery point; exclude upstream energy already represented in the monetary material or capital components
- `P_e,cur` = Optional illustrative conversion in the named currency per kWh at that delivery point and energy-quality convention
- `C_material,cur(G)` = Monetary material extraction/refining cost in that currency
- `C_cap,cur(G)` = Monetary capital depreciation or repayment for robotics and facilities in that currency
- `C_land,cur(G)` = Monetary land or resource rent in that currency
- `C_monetary_subtotal,cur(G)` = This bounded monetary subtotal; it is distinct from each component and is not a complete market price by definition

Step 1 also lists labor, risk/profit, and scarcity premium. If present in a conventional market price, those are additional monetary components shown separately; this subtotal does not silently absorb or omit them. The formula does not add currency to kWh: energy multiplied by the optional currency conversion is a currency amount, as are the other terms.

**Scenario assumption:** In mature post-scarcity, monetary material, capital, and land charges might approach zero without profit, rent, or private capital recovery. Their physical energy and material requirements do **not** approach zero by definition; those requirements belong in the full production-network accounting below. This equation does not set a user price or payment duty.

---

## Step 5: Examining Each Component

### 1. Energy (`E_use × P_e,cur`)
- Energy is ALWAYS required for production
- Even with abundant renewable energy, there's an underlying cost
- **This component remains**
- In a currency comparison, `E_use × P_e,cur` converts the named energy use to an illustrative currency amount; it remains separate from the physical energy ledger.

### 2. Materials (`C_material,cur`; physical input `E_material,emb`)
- Materials must be extracted, refined, transported
- These processes consume energy
- In post-scarcity, if materials are publicly owned and automated:
  - `E_material,emb = E_extraction + E_refining`
  - **Energy-only hypothesis:** Materials could be accounted for partly through extraction, refining, recycling, and transport energy, but finite stocks, losses, quality, ecological harm, and alternative uses do not automatically become energy costs.
- **Circular economy refinement:** Recycled materials have lower embodied energy than virgin materials (e.g., recycled steel vs. virgin steel reduces energy for extraction/refining significantly). For a fixed energy output, reducing the embodied energy of materials counted in the same lifecycle ledger lowers `E_in,life` and improves net energy return. However, recycling introduces diminishing returns, repeated recycling causes quality degradation (downcycling), and circular economy technologies at the required global scale remain emerging rather than fully proven. The circular economy framework (design for disassembly, product-as-service, right-to-repair) is a **necessary but not sufficient** condition for solving the materials problem; it must be combined with substitution research and throughput reduction.

### 3. Capital (`C_cap,cur`; physical input `E_capital,emb`)
- Robots, factories, machinery wear out
- They need maintenance, replacement
- In post-scarcity, if these are publicly owned:
  - `E_capital,emb = E_manufacturing + E_maintenance`
  - **Energy-only hypothesis:** Capital could be allocated partly by the energy used to make, repair, and replace it; component scarcity, fabrication time, skills, and capacity constraints remain.

### 4. Land (`C_land,cur`)
- Physical space for production
- This scenario assumes publicly owned production land with no rent
- **Public rent may become zero, but land's opportunity cost does not.** A site used for one purpose cannot always be used for housing, habitat, or farming at the same time.

---

## Step 6: Accounting Across Economic Phases

**Traditional Economy (illustrative monetary accounting):**
```
Price_cur = Labor_cur + Materials_cur + Energy_cur + Capital_cur + Land_cur + Profit_cur + Scarcity_cur
```

**Illustrative monetary transition accounting under Chapter 6 and Chapter 24's readiness gates (Years 0-8, 8-16, and 16-30):**
```
Price_cur = Energy_cur + Materials_cur + Capital_cur + Land_cur + Small_Tax_cur
```

**Illustrative mature post-scarcity accounting (Years 30+, subject to Chapter 24's readiness gates):**
```
E_signal(G) = E_direct(G) + E_embodied,production(G)
```

This is a physical energy-accounting signal, not a complete price or allocation rule. Its boundary must state whether energy-system construction, operation, maintenance, replacement, grid, and storage are included. Materials, land, labor and care, maintenance, storage and grid needs, waste, safety, capital, ecological effects, and competing uses can remain binding constraints. Energy accounting supplements rather than replaces fiscal and social accounting.

**A more complete physical energy definition under one declared production boundary:**

```
E_footprint(G) = E_direct(G) + E_embodied,production(G)
```

Where:
- **Direct energy**: Physical energy consumed during production
- **Embodied production energy**: Physical energy required to extract and refine materials; manufacture, maintain, and replace capital equipment; and build and maintain infrastructure, counting each included input once
- `E_footprint` is complete only for its declared boundary. If upstream energy generation, grid, or storage is outside that boundary, identify it as omitted; do not describe the result as a complete actual-system footprint. A separately measured omitted input may be added only in the load-only representation defined below.
- The transition `Price_cur` expressions remain monetary illustrations. They do not adopt `Small_Tax` or any price, payment, tax, or allocation rule.

---

## Step 7: Direct and Embodied Energy

```
E_footprint(G) = E_direct(G) + E_material,emb(G) + E_capital,emb(G) + E_infrastructure,emb(G)
```

This can be shortened to:

```
E_footprint(G) = E_total(G)
```

Where `E_total` is the physical energy footprint of producing one unit of G within the same declared boundary. Currency is not part of this energy sum. If a currency comparison is useful, show it separately as `C_energy,cur(G) = E_footprint(G) × P_e,cur`. The network and load-ledger alternatives below determine whether energy-supply investment is already included; do not add it twice.

---

## Step 8: Example Calculation - Producing 1 kg of Bread

**Illustrative accounting example only.** The kWh values and $0.05/kWh conversion below are placeholders, not a measured lifecycle assessment of bread. They omit crop and location, yields, fertilizer, water, packaging, losses, labor, capital lifetime, and grid boundary. The arithmetic totals the listed values; it does not validate them. The dollar column is a currency conversion for comparison only, not an adopted user price, payment duty, tax rate, or allocation rule.

| Component | Energy Required | Energy Cost (@ $0.05/kWh) |
|-----------|----------------|--------------------------|
| Growing wheat (farming robots) | 0.5 kWh | $0.025 |
| Harvesting | 0.1 kWh | $0.005 |
| Milling | 0.2 kWh | $0.01 |
| Baking | 1.0 kWh | $0.05 |
| Distribution | 0.3 kWh | $0.015 |
| **Embodied: Robot manufacturing** | **0.5 kWh** | **$0.025** |
| **Embodied: Facility maintenance** | **0.2 kWh** | **$0.01** |
| **Total** | **2.8 kWh** | **$0.14** |

### Can an energy-only model actually work?

Let a proposed production network include farming, robots, robot repair, factories, recycling, and power generation. For a demanded bundle of essentials `q`, let `A` record how much output of each activity every other activity requires. If the network is productive and the matrix inverse exists, total activity is `x = (I - A)^(-1) q`. Let `e` be direct energy per unit of activity with the same period and boundary as `x`. The full-network energy requirement is `E_network = eᵀx`. If this network includes power generation, grid, storage, upstream construction, maintenance, and replacement, those inputs are already in `E_network` and are not added again through a separate EROEI or overhead factor.

An alternative load-only ledger may end at delivered energy and exclude some energy-supply or grid inputs. In that case, call the result a load-ledger subtotal, identify the omitted inputs, and add only separately measured and allocated omitted energy once. A boundary that omits grid or storage is not a complete actual-system footprint. The two ledger representations are alternatives, not additive layers for the same entries.

This uses the standard [input-output method described by Eurostat](https://ec.europa.eu/eurostat/web/esa-supply-use-input-tables/methodology). The sectors, direct-energy factors, and feasible resource limits for this Charter have **not** been estimated; the equation is a proposed way to test the claim, not a computed result.

Energy alone would determine an allocation *only under restrictive conditions*: enough land and materials are available at the required quality and time; recycling losses and ecological limits are accounted for; labor and care are provided without coercion; production capacity can meet demand; and no alternative use of a scarce input has an uncounted cost. In a fuller model, constraints such as `Bx ≤ R` represent available minerals, land, water, emissions limits, skills, and factory capacity. If a constraint binds, its shadow value is not generally zero. Then an energy tally is useful information, but it is not a complete social cost or a fair allocation rule. This model supports testing an energy-accounting *component* of the Charter, not concluding that materials, capital, or land literally reduce to energy.

---

## Step 9: Limitations and Edge Cases

**When "energy only" breaks down:**

1. **Finite Resources**: Some materials are genuinely scarce (rare earth elements)
   - Solution: Recycling, substitution, or rationing

2. **Positional Goods**: Things that can't be reproduced (original art, beachfront property)
   - These retain scarcity value

3. **Energy Production Cost**: If energy itself requires resources (solar panels, turbines)
   - These embodied costs feed back into the energy price

4. **[Jevons Paradox (Rebound Effect)](https://doi.org/10.1016/j.erss.2021.101982)**: Energy efficiency improvements can lead to increased total energy consumption because lower effective cost stimulates higher demand. This paradox means that without explicit throughput caps, the energy savings from high-EROEI sources could be partially or fully offset by increased consumption. The abundance framework's Ch. 18 (Growth, Sustainability & Limits) addresses this through sufficiency culture, the three-tier "enough" model, and mandatory caps on total material throughput. Efficiency gains alone are insufficient without structural limits. See Ch. 18 for full treatment of Jevons Paradox and Circular Economy principles.

---

## Step 10: Energy Pricing with Fusion and Fission

### Illustrative energy-source comparison—not a common-boundary EROEI ranking

Published EROEI ranges come from studies with different lifecycle boundaries, energy-quality treatment, storage assumptions, and technology maturity. They cannot be ranked as if measured the same way. A comparison requires the same delivered-energy point, included lifecycle phases, quality adjustment, storage and grid treatment, and uncertainty method. Fusion remains theoretical for this purpose.

| Source | Upfront Cost | Marginal Cost | Lifespan | EROEI |
|--------|-------------|---------------|----------|-------|
| Solar PV | Project-specific | Project-specific | Design-specific | Recalculate with common boundary |
| Wind | Project-specific | Project-specific | Design-specific | Recalculate with common boundary |
| Fission (Gen III+ reference) | Project-specific | Project-specific | Design-specific | Recalculate from traced plant and fuel-cycle inputs |
| Fusion (future) | Unproven commercial cost | Unproven | Unproven | Theoretical; no commercial lifecycle EROEI measured |
| Hydro | Project-specific | Project-specific | Design-specific | Recalculate with common boundary |

### EROEI Analysis

**Energy Return on Energy Invested:**

```
EROEI = E_out / E_in,life
```

Where `E_out` is total energy output over the named lifetime at a stated plant-busbar or delivered-load point, and `E_in,life` is the total energy invested across the matching declared lifecycle. Both use the same stated energy-quality convention and compatible units. `E_in,life` includes applicable extraction, processing, construction, operation, maintenance, replacement, and decommissioning inputs. Construction energy is one component, not the complete denominator. Do not include any input twice; identify station-service treatment and output boundary. `EROEI` is dimensionless and is not a monetary price or a production-cost model.

The energy used to produce energy has a separate accounting ratio: lifecycle energy invested per unit of output.

```
I_supply = E_in,life / E_out = 1 / EROEI
```

`I_supply` is a dimensionless kWh-input-per-kWh-output ratio for the matched boundary. It is distinct from the full energy used to produce G and from a grid's gross-to-delivered multiplier `h_del`.

For a load-only ledger that excludes the whole supply-investment burden, a proportional accounting estimate is:

```
E_supply,attrib(G) = I_supply × E_at_same_output_point(G)
```

`E_at_same_output_point(G)` is the energy required for G at the same delivery point, quality convention and accounting period used in `I_supply`. This average attribution assumes the named supply system serves that load. If only part of the supply burden is omitted, trace that omitted part separately instead of applying the full ratio. If the production network already counts the supply inputs, use its total without adding this attribution.

Physical maintenance energy per unit of output is `E_maintenance,life / E_out`. It is a component of `I_supply`, already included in the full lifecycle denominator, rather than a second complete cost factor or a currency price.

This attribution describes energy accounting. Chapter 6 still governs service allocation, funding and any monetary comparison.

### Fission lifecycle evidence boundary

For the operating Vogtle Unit 4 AP1000 reference, plant EROEI remains **not established**. The [fission appendix](#appendix-appendix-energy-fission-eroei-calculation) distinguishes the observed 2025 net-generation record from scenario assumptions and identifies the physical lifecycle and service-demand evidence still needed. Its result does not establish that equal joules provide equal services.

The [UC Berkeley ESBWR study](https://fhr.nuc.berkeley.edu/wp-content/uploads/2014/10/05-001-A_Material_input.pdf) supplies approximate construction-material estimates for a named **Gen III+ ESBWR**. It is not a complete lifecycle-energy result, and those material estimates are not inputs for the AP1000.

### Traditional vs. Post-Scarcity Energy Pricing (illustrative technical comparison)

The price terminology and currency examples in this section describe conventional accounting or hypothetical scenarios. They do not set a tariff or user-facing payment; Chapter 6 governs any fiscal mechanism, while this appendix supplies only physical-accounting detail.

**Traditional View:**
```
Price_cur_per_kWh = Capital_Amortization_cur_per_kWh + OandM_cur_per_kWh + Fuel_cur_per_kWh + Profit_cur_per_kWh
```

**Fission Example:**
- Plant cost: $10-20 billion
- Capacity: 1 GW
- Capacity Factor: 90%
- Lifespan: 60 years
- Total output: 473,040 GWh (1,000 MW × 0.90 × 8,760 hrs × 60 yrs)
- ```
  Capital Cost = $10-20B / 473,040 GWh = $0.021-0.042/kWh
  ```

**Fusion Example (illustrative assumptions):**

The plant-cost range and per-kWh range below are separate illustrative assumptions. No lifetime-output calculation connects them here.
- Plant cost: $20-40 billion
- ```
  Cost ≈ $0.08-0.12/kWh
  ```

**Post-Scarcity View:**
```
E_marginal,use_per_kWh = E_operational,use_per_kWh
```

This is a physical-energy expression for the stated scenario, not a monetary marginal cost or universal rule. If a currency comparison is shown, define it separately as a currency amount using `P_e,cur`; the physical and monetary ledgers remain distinct.

This scenario assumes:
1. Infrastructure is publicly owned (no private capital repayment assumed)
2. Automation handles construction/maintenance (no production-wage cost assumed)
3. The "sunk cost" of infrastructure is spread across all humanity

These assumptions do not remove physical construction, maintenance, replacement, human work, or lifecycle energy inputs from the accounting.

---

## Step 11: The Self-Manufacturing Energy Loop

```
E_construction,plant(t+1) is supplied by E_output,plant(t)
```

This creates a **recursive energy accounting** problem:

```
E_net,available = E_gross,output - E_maintenance - E_replacement
```

Subtract maintenance or replacement here only when those inputs are not already reflected in the stated net output or included elsewhere in the same lifecycle ledger.

If automation builds the plants:

```
E_construction,plant = E_embodied,construction,plant
E_output = EROEI × E_in,life
```

**Net Gain:**
```
E_net = (EROEI - 1) × E_in,life
```

`E_embodied,construction,plant` is a construction component of `E_in,life`. The full-lifecycle identities above do not equate construction-only energy with the full EROEI input.

---

## Step 12: Numerical Example - Mixed Energy Grid

**Assume a fictional mixed grid to check the arithmetic only.** The EROEI values are placeholders, and fusion's value is theoretical. All are treated as if measured at the same plant-busbar boundary with lifecycle maintenance already included; this assumption is not established by the cited literature.

| Source | Capacity | Illustrative EROEI | Annual gross output |
|--------|----------|--------------------|---------------------|
| Solar | 50 GW | 15 | 96 TWh (CF=22%) |
| Wind | 30 GW | 20 | 92 TWh (CF=35%) |
| Fission | 20 GW | 80 | 158 TWh (CF=90%) |
| Fusion | 10 GW | 60, theoretical | 79 TWh (CF=90%) |

**Calculations:**

```
Solar: 96 TWh × (1 - 1/15) = 89.6 TWh net
Wind: 92 TWh × (1 - 1/20) = 87.4 TWh net
Fission: 158 TWh × (1 - 1/80) = 156.025 TWh net
Fusion: 79 TWh × (1 - 1/60) = 77.683 TWh net

Total gross = 425 TWh
Net at the assumed busbar boundary = 410.708 TWh
If distribution loses a separate 5% of busbar energy, delivered = 410.708 × 0.95 = 390.173 TWh
Gross generation per delivered kWh = 425 / 390.173 = 1.089 kWh (the displayed 1.089 is rounded to three decimal places; using the displayed inputs gives 1.0892604...)
```

**Energy-accounting conversion (not a user charge):**
```
If infrastructure is publicly owned and amortized:
E_supplement = E_supply,excluded + E_delivery,excluded

The illustrative 5% loss is applied once to busbar energy, not added to maintenance already inside EROEI. Actual storage losses and grid construction are not yet modeled. If those items are omitted, the figures are not a complete actual-system footprint.
```

---

## Step 13: Energy Accounting for the Illustrative Grid

**In mature post-scarcity:**

```
E_supplement,per_delivered_kWh = E_supply,excluded_per_delivered_kWh + E_distribution,excluded_per_delivered_kWh
```

Where these terms are physical energy quantities per delivered kWh for inputs excluded from the selected load ledger. Use this supplement only with a load-only ledger; a full-network ledger that already contains those entries receives no second supplement. `E_distribution` refers to measured delivery losses such as transmission and included storage losses; unmodeled storage or grid construction is not included.

**For the mixed grid above:**

```
Illustrative lifecycle energy investment difference at the stated busbar boundary = 425 - 410.708 = 14.292 TWh
Illustrative distribution loss = 410.708 - 390.173 = 20.535 TWh
Total gross-to-delivered difference = 34.827 TWh, or 8.19% of gross generation (34.827 / 425; using displayed inputs gives 8.194588...%)
Additional gross energy per delivered energy = 34.827 / 390.173 = 0.0892604... (8.926040...%, or 8.93% rounded, of delivered energy)
```

Thus this *particular arithmetic scenario* requires about 1.089 kWh gross generation per delivered kWh, using the displayed rounded ratio. It does not establish a real grid overhead: EROEI boundaries, quality adjustment, storage, curtailment, and grid construction still need comparable evidence. The 8.19% gross-share figure and the 8.93% delivered-denominator figure answer different questions.

---

## Step 14: Nuclear Special Considerations

**Fuel concentration and system planning:**

1. **Energy Density**:
   - [Fission fuel](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1754web-26894285.pdf) has high energy density. A quantitative coal comparison needs a named uranium fuel or isotope, its burnup, and a declared heat-to-electricity basis.
   - In a [published fuel-use illustration](https://www.iter.org/machine/supporting-systems/fuelling), ITER compares a 1,000 MW coal plant using 2.7 million tonnes of coal per year with a fusion plant of the same output using 250 kg of deuterium-tritium fuel per year. ITER does not specify a thermal-versus-electric output basis in that illustration. It is a proposed fuel-use comparison, not a measured commercial fusion result.

2. **Land Use**:
   - Compare direct plant area, total project area, and lifecycle land requirements separately, including the fuel cycle, transmission, and any storage.
   - State the site, design, period, nameplate capacity, and annual delivered energy. Use the same boundary and output basis for nuclear and solar.

3. **Observed Capacity Factors**:
   - **U.S. utility-scale fleet, calendar 2024:** Nuclear **90.8%**, solar photovoltaic **23.2%**, and wind **34.3%**.
   - [EIA's January 2026 Electric Power Monthly, Table 6.07.B](https://www.eia.gov/electricity/monthly/archive/january2026.pdf) identifies those 2024 values as final. They compare net generation with available time-adjusted capacity; they are fleet averages for that year.

**Post-Scarcity Implication:**

The proposed test is whether firm nuclear supply can improve stability, reduce storage needs, and lower infrastructure overhead per delivered kWh in a defined grid. Compare systems using the same hourly demand and reliability target, accounting for outages, generation mix, storage, transmission, materials, land, safety, and the full lifecycle.

---

## Step 15: Combining the Accounting Components

**For any good G in post-scarcity:**

```
E_footprint(G) = E_direct(G) + E_material,emb(G) + E_capital,emb(G) + E_infrastructure,emb(G) + E_distribution,emb(G)
```

Where each term is a physical energy quantity in the same stated unit, period, and declared boundary. Include each lifecycle or delivery input once. A full-network ledger that already includes generation, transmission, storage, construction, or maintenance does not receive a second supply multiplier. A load-only ledger may add a separately measured omitted input once, with its boundary and any allocation method stated.

If money is used for a separate illustrative comparison, show `C_energy,cur(G) = E_footprint(G) × P_e,cur`, where `P_e,cur` is a currency/kWh conversion. It is separate from the physical energy equation and does not create a tariff or user charge.

A usable `P_e,cur` comparison must name its currency and the energy delivery point. The physical ledger must state the load, generation mix, storage, transmission, system lifetime, and common lifecycle boundary. EROEI-derived lifecycle inputs must not be charged a second time as annual maintenance.

---

## Step 16: What This Means

In the Charter's proposed system, market price would no longer be the only guide to allocating essentials. Scarce materials, work, time, ecological limits, and competing uses would still require choices.

The question shifts from "how much does it cost?" to:

```
E_net,per_person,benchmark = E_net,total / N_people
```

An equal per-person energy share is one possible accounting benchmark, not an automatic allocation rule for every good:

```
E_net,per_person = E_net,total / N_people
```

Both expressions are physical energy per person over a named period. They are accounting benchmarks only; needs, ecological limits, service reliability, and the other stated constraints still apply.

**Resources are allocated by:**
1. Need (basics guaranteed)
2. Energy footprint (embodied energy tracked)
3. Sustainability limits (total budget constraint)

> **Planetary Boundaries Context:**
> The per-capita calculation above is an accounting benchmark. A sustainability assessment must also cover ecological constraints. Ch. 18 (Growth, Sustainability & Limits) establishes that the full sustainability framework requires compliance with [nine planetary boundaries](https://www.science.org/doi/10.1126/sciadv.adh2458): climate change, biosphere integrity (genetic + functional), land-system change, freshwater use, biogeochemical flows (nitrogen & phosphorus), novel entities (pollutants, plastics, radioactive waste), ocean acidification, atmospheric aerosol loading, and stratospheric ozone depletion. Energy throughput alone cannot capture all of these, for example, a society could be energy-efficient but still violate nitrogen/phosphorus cycles or accumulate novel entities beyond planetary limits. The Charter proposes addressing this through the "abundance within limits" model: guaranteeing essentials for all while operating within all nine planetary boundaries simultaneously, using circular economy, dematerialization, and new post-GDP metrics as implementation mechanisms. See Ch. 18 (Growth, Sustainability & Limits) for the complete frameworks on Abundance Within Limits, Planetary Boundaries, and Post-Growth Economics.

---

## An Illustrative Energy-Accounting Estimate

**With any generation mix evaluated on a common boundary:**

```
E_footprint(G) = E_load(G) × (1 + h_del)
```

Where:
- `E_load` = Physical energy used to produce G in a load-only ledger that explicitly excludes the supply and delivery overhead represented by `h_del`
- `h_del` = A dimensionless, measured or modeled additional-gross-energy-per-delivered-energy ratio for a defined system and boundary; no general 0.05–0.20 band is established here
- This multiplier applies only when `E_load` excludes those inputs. If the production-network or other ledger already includes generation, grid, storage, and upstream lifecycle inputs, use that ledger total directly and do not apply `h_del` again. If a declared boundary omits grid or storage, do not call it a complete actual-system footprint.

The mixed-grid example above calculates **1.089 gross kWh per delivered kWh** under its own assumptions (the displayed value is rounded; using the displayed inputs gives 1.0892604...). The corresponding additional gross energy per delivered energy is `h_del = (425 - 390.173) / 390.173 = 0.0892604...`, or 8.93% of delivered energy. This is not a general overhead factor for nuclear or any actual grid. The separate 8.19% value is the gross-to-delivered difference as a share of gross generation.

**In practice, if the system passes the energy and resource tests:**
- Basic needs: Supplied without a profit charge from a public energy budget, not without physical cost
- Luxuries: Tracked by energy footprint, rationed if needed
- Sustainability: Total consumption ≤ Total Net Energy

---

## Key Insights

1. **Count the full energy footprint** - Energy accounting must include direct and embodied energy

2. **Energy supply matters** - A demonstrated high net return can ease an energy constraint; fission must be evaluated by design and fusion remains unproven as a commercial supply

3. **Limits beyond energy** - With abundant energy, remaining constraints include:
   - Material constraints (rare earth elements)
   - Ecological boundaries (heat dissipation, waste)
   - Physical space (land for facilities)

4. **The Charter proposes a different allocation rule** - Guarantee essentials by need while testing real energy, material, and ecological constraints

---

## Future Exploration

- How does material scarcity (rare earth elements, etc.) interact with this energy model?
- What about genuinely finite resources that can't be recycled?
- How should energy be accounted for when it is supplied without a point-of-use charge (solar/wind with high upfront capital)?

---

*This appendix adds technical mathematical detail behind the lifecycle-energy accounting discussed in Chapter 6 (Economy and Funding). It does not itself adopt a user price, payment duty, tax rate, or allocation rule; guaranteed essentials remain free at the point of use under the Chapter 6 baseline.*
