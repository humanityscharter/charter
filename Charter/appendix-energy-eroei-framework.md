---
letter: G
slug: appendix-energy-eroei-framework
title: EROEI Calculation Framework
subtitle: Lifecycle-Based Energy Return on Energy Invested Across Generation Technologies
---

# EROEI Calculation Framework

## Lifecycle-Based Energy Return on Energy Invested

---

## 1. Definition and Formula

**[EROEI (Energy Return on Energy Invested)](https://world-nuclear.org/information-library/energy-and-the-environment/energy-return-on-investment)** measures the ratio of energy obtained from a system to the energy invested in it. A ratio is meaningful only when output and inputs use a declared energy-quality convention and the same lifecycle boundary:

```
EROEI = E_out / E_in

Where:
- E_out = Total usable energy output over the system's lifetime at a stated plant-busbar or delivered-load point
- E_in = Total energy invested across all lifecycle phases
```

**Net Energy:**
```
E_net = E_out - E_in = E_out × (1 - 1/EROEI)
```

Here `E_in` means the full lifecycle energy investment, written as `E_in,life` in Appendix F.

For electricity, state whether the numerator is generated at the plant or delivered to a load. Do not silently compare electrical output with heat-equivalent or primary-energy inputs. If a system comparison needs storage, backup, curtailment, or grid construction, account for them consistently across technologies.

---

## 2. Lifecycle Phases

The total energy investment is the sum across all lifecycle phases:

```
E_in = E_mining + E_processing + E_construction + E_operation + E_maintenance + E_decommissioning
```

Record each input's source, unit, period, energy-quality convention, and assigned phase. Check whether an embodied-energy factor already includes extraction, refining, manufacturing, or transport, and count those steps once. Use either the factor for those covered steps or separate process estimates for them; other phases add only inputs outside that factor's boundary.

Distinguish the original equipment from later replacement and refurbishment cycles. Record replacement frequency and how recycled material is treated. If a lifetime maintenance estimate already includes replacement parts, do not add the same parts again through another factor or phase.

### Phase 1: Resource Extraction (E_mining)
- Energy to extract raw materials (ore, uranium, etc.)
- Energy for initial site preparation
- Transportation of extracted materials

### Phase 2: Material Processing (E_processing)
- Energy for refining, smelting, enrichment
- Manufacturing of components and equipment
- Energy intensity of materials (GJ/tonne)
- Fuel conversion and fabrication where the technology requires them

### Phase 3: Construction (E_construction)
- Energy for assembly and installation
- Heavy machinery operation
- On-site fabrication

### Phase 4: Operation (E_operation)
- Routine operational energy
- Staff transportation and facilities
- Administrative overhead
- Fuel deliveries and refueling activities, with upstream extraction and processing assigned to their own phases
- Operational waste handling and storage

### Phase 5: Maintenance (E_maintenance)
- Replacement parts manufacturing
- Scheduled maintenance activities
- Component refurbishment

### Phase 6: Decommissioning (E_decommissioning)
- Dismantling and demolition
- Waste transport and storage
- Site remediation

---

## 3. Material Energy Intensities

### Illustrative embodied-energy ranges

| Material | Energy Intensity | Unit |
|----------|-----------------|------|
| Steel (structural) | 20-35 | MJ/kg |
| Steel (reinforced) | 30-40 | MJ/kg |
| Concrete (standard) | 0.9-1.7 | MJ/kg |
| Concrete (reinforced) | 1.0-1.8 | MJ/kg |
| Aluminum | 150-220 | MJ/kg |
| Copper | 70-90 | MJ/kg |
| Glass | 15-25 | MJ/kg |
| Plastics | 70-100 | MJ/kg |

These are unsourced screening placeholders, not factors for a particular steel route, concrete mix, geography, or year. Before use, replace them with a dated lifecycle inventory and account for recycled content, process energy mix, and whether rebar is already included in a total-metal estimate. None validates a plant EROEI by itself.

---

## 4. Calculating EROEI

### Step 1: Define System Boundaries
- Plant capacity and design life
- Technology type and specifications
- Geographic and operational context

### Step 2: Quantify Material Inputs
```
For each material i:
  M_i = Mass of material i (tonnes)
  EE_i = Embodied energy per unit (GJ/tonne)
  E_material_i = M_i × EE_i
```

### Step 3: Calculate Phase Energies
```
E_mining = Σ (Energy for material extraction)
E_processing = Σ (M_i × Processing energy per unit)
E_construction = Energy for assembly + equipment
E_operation = Annual operational energy × Lifetime
E_maintenance = Σ (Replacement parts energy × Frequency)
E_decommissioning = Estimated dismantling energy
```

### Step 4: Sum Total Energy Investment
```
E_in = E_mining + E_processing + E_construction + E_operation + E_maintenance + E_decommissioning
```

### Step 5: Calculate Total Energy Output
```
E_out = Capacity (kW) × Capacity Factor × Hours_per_Year × Lifetime
```

This gives **kWh** when capacity is in kW. Divide by **1,000,000,000** for TWh, then multiply by **3.6** for PJ of electricity.

Capacity, capacity factor, and lifetime must describe the same system and output point. State whether output is gross or net. If net output already subtracts station-service electricity, do not charge that same electricity again as an invested-energy entry.

Convert phase inputs to a common unit before adding them. Before dividing, express `E_in` and `E_out` in the same energy unit under the declared energy-quality convention. For example, divide a GJ input total by **1,000,000** to express it in PJ. A numerical unit conversion alone does not account for the different usefulness of heat, primary energy, and electricity.

### Step 6: Compute EROEI
```
EROEI = E_out / E_in
```

---

## 5. Unit Conversions

| Unit | Conversion |
|------|------------|
| 1 GJ | 1,000 MJ ≈ 277.8 kWh |
| 1 PJ | 1,000,000 GJ |
| 1 TWh | 3.6 PJ |
| 1 tonne steel | Material-specific factor required; illustrative input: 32 GJ |
| 1 tonne concrete | Mix-specific factor required; illustrative input: 1.1 GJ |

---

## 6. Example: what a documented design gives us

The [UC Berkeley ESBWR material-input study](https://fhr.nuc.berkeley.edu/wp-content/uploads/2014/10/05-001-A_Material_input.pdf), Table 4, estimates **104,231 m³ concrete** and **50,099 tonnes total metal** for the **1,500 MWe Gen III+ ESBWR**. These approximate material estimates can populate part of a construction inventory. They do **not** identify this plant's complete fuel, operations, construction activity, maintenance, waste, or decommissioning energy. They also do not establish its lifetime capacity factor. See the [fission appendix](#appendix-appendix-energy-fission-eroei-calculation).

### Operating AP1000 check and demand boundary

The [public result summary](#appendix-appendix-energy-fission-eroei-calculation) uses operating Vogtle Unit 4 as the AP1000 reference, while keeping [EIA's reported electrical capacity](https://www.eia.gov/todayinenergy/detail.php?id=61963), [NRC's licensed thermal power and license dates](https://www.nrc.gov/reactors/new-reactors/large-lwr/col-holder/vog4), and a modeled 60-year design sensitivity separate. A lifecycle carbon-footprint study is useful evidence for its stated purpose, but tonnes of emissions are not PJ of invested energy. The named AP1000 does not yet have a complete comparable physical-energy input set, so the ratio is **not established**.

The same boundary discipline applies to the denominator in a people-supported calculation. [EIA's 2024 final-electricity total](https://www.eia.gov/electricity/annual/table.php?t=epa_02_02.html) is only one part of today's U.S. services; non-electric heating, transport, and industry need named replacement technologies and efficiency evidence. [NREL's 2050 high-electrification electricity projection](https://www.osti.gov/servlets/purl/1785329) is a separate future sensitivity with remaining non-electric demand. Until both service demand and hourly reliability are accounted for, this framework gives no reactor headcount. The current AP1000 result and its evidence limits appear in the [fission appendix](#appendix-appendix-energy-fission-eroei-calculation).

---

## 7. Other Energy Sources

The same framework applies to other energy sources. The solar and wind lifetime ranges below are illustrative design assumptions; a calculation for a named project must state its own lifetime basis. The listed inputs are starting entries for each technology, and the full lifecycle checklist above applies to every case:

### Solar PV
- E_in: Silicon purification, panel manufacturing, installation
- E_out: Generation over 25-30 year lifetime

### Wind
- E_in: Steel/concrete for towers, rare earths for magnets, manufacturing
- E_out: Generation over 20-25 year lifetime

### Fusion
- E_in: Superconducting magnets, vacuum vessels, specialized materials
- E_out: Hypothetical generation; no commercial plant lifecycle is yet measured

---

## 8. Uncertainty and Sensitivity

### Key Uncertainties
- Material quality and specifications
- Construction efficiency
- Actual capacity factor achieved
- Decommissioning complexity

### Sensitivity Analysis
The changes below are illustrative sensitivity test settings. Apply each percentage relative to a stated baseline and use feasible input values. They show how selected assumptions affect the calculated ratio; they are not measured uncertainty bounds or confidence intervals:
- ±20% on material quantities
- ±10% on capacity factor
- ±30% on decommissioning estimates

---

## 9. Quality Criteria

A robust EROEI calculation should:
1. **Be transparent** - All assumptions and data sources documented
2. **Be complete** - All lifecycle phases included
3. **Be consistent** - Same boundaries applied across comparisons
4. **Be verifiable** - Third-party review possible
5. **Include uncertainty** - Ranges provided where appropriate

---

*This framework explains the inputs needed to test EROEI claims. It does not verify the illustrative ratios in the energy-cost appendix.*
