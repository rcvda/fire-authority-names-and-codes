# UK Fire & Rescue Authorities — Names and Codes (GB-FRA)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24170446.svg)](https://doi.org/10.5281/zenodo.24170446)

> **Status: work in progress.** The `GB-FRA` scheme is **not yet registered** with [org-id.guide](https://org-id.guide). See [Roadmap](#roadmap).

An open, coded register of **UK fire and rescue authorities** — every statutory fire and rescue authority (FRA) in England, Wales, Scotland and Northern Ireland — with an identifier for each body that has no usable identifier of its own.

## Why this exists

A statutory fire and rescue authority — a combined fire authority, a metropolitan fire authority, a national service, or a corporation sole such as the London Fire Commissioner — has no charity number, no company number, and no clean government-organisation code. They fall through the gap of the national identifier schemes, exactly the condition this register fills. It is the direct parallel of RCVDA's police register (`GB-POL`) and police & crime commissioner register (`GB-OPCC`), and is built on the same principles as mySociety's `uk_local_authority_names_and_codes`.

Where the fire and rescue function is **not** vested in a standalone authority but is held by an already-identified body — a county/unitary council, a mayoral combined authority, or a Police, Fire & Crime Commissioner — that body is **referenced**, not minted.

## Mint only genuine gaps

A `GB-FRA` code is minted **only** where an FRA has no usable existing identifier. A fire function that is held by a body already in a standard register is **referenced** to that identifier, not minted:

- **Northern Ireland Fire & Rescue Service** → referenced `GB-GOR-OT759` (the Fire Authority for Northern Ireland holds a government-organisation code).
- **County / unitary councils that are the FRA** (e.g. Oxfordshire, Kent, Cornwall) → referenced their own `GB-LAE-…` identifier.
- **Police, Fire & Crime Commissioners** holding fire under the single-employer model (Cumbria, Essex, Northamptonshire, Staffordshire) → referenced the commissioner's `GB-OPCC-…` code in the sibling register.
- **Mayoral combined authorities** holding fire (Greater Manchester, York & North Yorkshire) → referenced the authority's `GB-LAE-…` / `GB-UKLA-…` identifier.

ROR (Research Organization Registry) identifiers are **not** treated as a usable principal identifier: Leicestershire's FRA carries a `XI-ROR` id incidentally, but ROR is an international research-sector registry, not a UK statutory/principal register, so it is still minted. The **London Fire Commissioner** is minted — it is a corporation sole with no register ID, the exact fire parallel of MOPAC (`GB-OPCC-00023`) on the police side, and a genuine gap.

## Coverage

All 49 UK fire and rescue authorities — 44 in England, 3 in Wales, the Scottish Fire and Rescue Service, and the Northern Ireland Fire & Rescue Service. **29 `GB-FRA` mints, 20 referenced bodies.**

## Data

| File | What it is |
|------|-----------|
| [`data/register.csv`](data/register.csv) | The register: one row per fire & rescue authority, with its `GB-FRA` code (or the referenced external id), area, the body that holds the fire function, and — for PFCC areas — the paired `GB-OPCC` police-governance id. |
| [`source/fra_authorities.json`](source/fra_authorities.json) | The authoritative source list of UK fire & rescue authorities and their governance model. |
| [`source/code_assignments.csv`](source/code_assignments.csv) | The permanence ledger — the frozen code (or external reference id) assigned to each body. Codes are never reissued or renumbered. |
| [`source/fra_names_codes_2025.csv`](source/fra_names_codes_2025.csv) | ONS Fire and Rescue Authorities (December 2025) Names and Codes (Open Geography Portal), `FRA25CD` / `FRA25NM`. Joined by area to populate `ons_fra_code`. |
| [`source/gb_gor_government-organisation.csv`](source/gb_gor_government-organisation.csv) | Held copy of the GB-GOR government-organisation register, used to cross-check that no mint duplicates an existing identifier. |
| `evidence/` | Held copies of the governance-model sources (Home Office *Fire and Rescue National Framework for England*; APCC fire & emergency services; LGA guide). |

## How the data is built

`build_register.py` reads the source list and the frozen `code_assignments.csv`, applies the mint-vs-reference rule, and emits `data/register.csv`. See [METHODOLOGY.md](METHODOLOGY.md). Codes are **allocated once and frozen** — see [CODESCHEME.md](CODESCHEME.md).

To regenerate:

```
python3 source/build_register.py source/fra_authorities.json data/register.csv
```

## Licence

Open Government Licence v3.0 — see [LICENSE](LICENSE).

## Roadmap

1. Hold and maintain the register (done).
2. ONS **Fire and Rescue Authorities (December 2025) Names and Codes** geography added — `ons_fra_code` populated (`FRA25CD`), the fire equivalent of the ONS Police Force Area code in the `GB-POL` register (done).
3. Archived with a Zenodo DOI — [10.5281/zenodo.24170446](https://doi.org/10.5281/zenodo.24170446) (author Peter Neal / ORCID, publisher RCVDA, OGL v3.0) (done).
4. Register the `GB-FRA` scheme with [org-id.guide](https://org-id.guide), alongside the `GB-POL` and `GB-OPCC` submissions.

Note: the English Devolution and Community Empowerment Act 2026 and local government reorganisation are moving fire governance (county councils merging into unitaries; further mayoral transfers). Superseded bodies will be retired (code kept, status updated) and successors minted or referenced; nothing is renumbered.

## Relationship to other RCVDA registers

Sibling to [`police-force-names-and-codes`](../police-force-names-and-codes) (`GB-POL`) and [`opcc-names-and-codes`](../opcc-names-and-codes) (`GB-OPCC`). Where a Police, Fire & Crime Commissioner holds fire, the fire row references the same `GB-OPCC` body and records it in `paired_police_id`, making the police↔fire governance link explicit.

## Author and maintainer

Created and maintained by Peter Neal at Redcar & Cleveland Voluntary Development Agency (RCVDA). Corrections welcome via issues/PRs.
