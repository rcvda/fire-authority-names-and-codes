# The GB-FRA code scheme

`GB-FRA` = **GB** (ISO 3166 — the United Kingdom, including Northern Ireland) **F**ire & **R**escue **A**uthorities. (Proposed org-id.guide scheme prefix; not yet registered.)

## What gets a code

A statutory **fire and rescue authority** is the entity. A `GB-FRA` code is minted for every FRA that has **no usable existing identifier**. Where the fire and rescue function is held by a body already in a standard register — a local authority (`GB-LAE`), a mayoral combined authority (`GB-LAE` / `GB-UKLA`), a Police, Fire & Crime Commissioner (`GB-OPCC`), or a government organisation (`GB-GOR`) — that body is **referenced**, not minted, and its `org_id` is the external code, not a `GB-FRA` number. ROR (`XI-ROR`) identifiers do not count as a usable principal identifier (see README).

## Code format

```
GB-FRA-#####
```

Five-digit, zero-padded sequence. Codes are:

- **Opaque.** They carry no geographic or alphabetical meaning. (The ONS Fire and Rescue Authority code, once sourced, is carried alongside in `ons_fra_code` as a lookup, never as the identifier.)
- **Permanent and frozen.** The assignment lives in [`source/code_assignments.csv`](source/code_assignments.csv). A code, once issued, is never reissued or renumbered — even if an authority is renamed, merged or dissolved. The builder reads the frozen ledger; new bodies append the next number. Adding a body never reshuffles existing codes.
- **Withdrawn codes are retained.** If a minted body is later found to hold an existing identifier (as happened with PSNI → `GB-GOR-OT657` on the police side), its `GB-FRA` number is marked withdrawn in the ledger and never reused; the sequence carries a deliberate gap.

## Referenced bodies (not minted)

| Body | Keyed to |
|---|---|
| Northern Ireland Fire & Rescue Service | `GB-GOR-OT759` |
| County / unitary councils that are the FRA (13) | that council's `GB-LAE-…` |
| PFCC single-employer FRAs (Cumbria, Essex, Northamptonshire, Staffordshire) | the commissioner's `GB-OPCC-…` |
| Mayoral combined authorities (Greater Manchester; York & North Yorkshire) | `GB-LAE-GMCA` / `GB-UKLA-YNYC` |

## Relationship to other schemes

- **Sideways:** `ons_fra_code` links to ONS Fire and Rescue Authority geography (to be added — see README roadmap).
- **Governance:** `paired_police_id` links a fire authority held by a Police, Fire & Crime Commissioner to that commissioner's `GB-OPCC` record, so the police↔fire governance link is explicit.

## Fields (`data/register.csv`)

`org_id`, `name`, `body_type` (`fra`), `fire_rescue_authority_area`, `ons_fra_code`, `fra_function_held_by`, `paired_police_id`, `status`, `issued_by`, `date_issued`, `evidence`, `notes`.
