# Contributing

Corrections and additions welcome via issue or pull request.

## Principles

- **Mint only genuine gaps.** A body that already holds an identifier in a standard register (GB-GOR, GB-LAE, GB-OPCC, Companies House, Charity Commission) is referenced to it, never given a new code. ROR identifiers do not count.
- **Codes are permanent.** Never renumber or reissue. New bodies append the next number in `source/code_assignments.csv`. A withdrawn code is retained there and never reused.
- **Authoritative sources only.** The Find That Charity register, ONS geography, the GB-GOR register, and the Home Office / LGA / APCC governance sources over secondary lists. Cite the source for any change.

## Adding or changing a body

1. Add or amend the authority in `source/fra_authorities.json`, with its governance model and (for a reference) the external id it is keyed to.
2. Check it against `source/gb_gor_government-organisation.csv` and the Find That Charity cache — if it already holds a usable identifier, reference it; otherwise mint.
3. Add its frozen code to `source/code_assignments.csv` (next `GB-FRA` number for a mint; the external id for a reference).
4. Regenerate with `build_register.py` and verify.

## Governance change (reform / reorganisation)

When a fire function transfers (e.g. a county council merges into a unitary, or fire moves to a mayor), retire the superseded row (keep its code, update `status` and `notes`) and mint or reference the successor. Never renumber an existing code.
