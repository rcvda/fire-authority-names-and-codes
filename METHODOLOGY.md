# Methodology

How the register is built. Every row is reproducible from authoritative, openly-licensed sources, not hand-keyed.

## Sources

1. **UK fire & rescue authority list and governance model** — `source/fra_authorities.json`. The 49 UK fire and rescue authorities and which governance model each sits under (combined / metropolitan fire authority; county or unitary council as FRA; Police, Fire & Crime Commissioner; mayoral combined authority; national service). Governance models from the Home Office *Fire and Rescue National Framework for England* (May 2018) and the LGA fire-governance guide; current PFCC-fire and mayoral-fire assignments from the Association of Police and Crime Commissioners (2026). Held copies in `evidence/`.
2. **Find That Charity bulk cache (2026-09-13)** — used to establish that no territorial fire and rescue authority holds a usable existing identifier. The cache confirms: **zero** fire authorities in the local-authority register (`GB-LAE`); the only fire body in the government-organisation register (`GB-GOR`) is the Fire Authority for Northern Ireland (`GB-GOR-OT759`); Leicestershire's FRA appears only under a ROR id; every other "fire" registration is a satellite (museum trust, benevolent fund, or a trading arm such as Cleveland Fire Brigade Risk Management Services CIC `GB-COH-07583911`), not the statutory authority.
3. **UK government-organisation register (GB-GOR)** — held in `source/gb_gor_government-organisation.csv`, used to (a) reference bodies that already have a code and (b) cross-check that no mint duplicates an existing identifier.
4. **ONS Fire and Rescue Authorities (December 2025) Names and Codes** (Open Geography Portal) — held in `source/fra_names_codes_2025.csv`; provides `FRA25CD`, joined by authority area (with a small alias map) to populate `ons_fra_code`. Vintage changes annually.

## Build

`build_register.py` reads `source/fra_authorities.json` and the frozen codes in `source/code_assignments.csv`, applies the mint-vs-reference rule per governance model, joins the ONS FRA code from `source/fra_names_codes_2025.csv` by area name (with a small alias map for the shorter ONS labels — e.g. York & North Yorkshire → North Yorkshire, Staffordshire → Stoke-on-Trent and Staffordshire), and emits `data/register.csv`.

Reproduce:

```
python3 source/build_register.py source/fra_authorities.json data/register.csv
```

## Mint-vs-reference rule, by governance model

- **Combined / metropolitan fire authority** (standalone statutory body) → **mint** `GB-FRA` (genuine gap).
- **National service** (Scottish Fire and Rescue Service; the Welsh combined authorities) → **mint** (devolved bodies not in GB-GOR; no company/charity id).
- **London Fire Commissioner** (corporation sole) → **mint** — a genuine gap, the direct parallel of MOPAC (`GB-OPCC-00023`) on the police side; the function is held by the Mayor of London *through* the Commissioner, not by the GLA corporate body, so it is not referenced to `GB-LAE-GLA`.
- **County / unitary council is the FRA** → **reference** the council's `GB-LAE`.
- **Police, Fire & Crime Commissioner (single-employer)** → **reference** the commissioner's `GB-OPCC` code; the same corporation sole already minted in the police register. Recorded in `paired_police_id`.
- **Mayoral combined authority holds fire** → **reference** the combined authority's `GB-LAE` / `GB-UKLA` id.
- **Northern Ireland** → **reference** `GB-GOR-OT759` (parallels PSNI → `GB-GOR-OT657`).

## GB-GOR cross-check

Every mint was checked against the GB-GOR register (held in `source/`) and the Find That Charity bulk cache. Findings applied: the Fire Authority for Northern Ireland holds `GB-GOR-OT759` → referenced, not minted; ROR (`XI-ROR`) matches (Leicestershire) are not treated as usable principal identifiers; satellite charities/companies carrying "fire" in their name are not the statutory authority and are disregarded.
