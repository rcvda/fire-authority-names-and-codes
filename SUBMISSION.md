## Proposed list: GB-FRA — UK Fire & Rescue Authorities

### Proposed list code
`GB-FRA` — jurisdiction `GB` (ISO 3166, the United Kingdom incl. Northern Ireland) + list-name code `FRA`.

### Name
UK Fire & Rescue Authorities (RCVDA register)

### Managed by
Redcar & Cleveland Voluntary Development Agency (RCVDA), a UK charity (Charity No. 1135959). Published openly on GitHub.

### Description
Open identifiers for UK fire and rescue authorities — every statutory fire and rescue authority (FRA) in England, Wales, Scotland and Northern Ireland. A `GB-FRA` code is minted **only** where an FRA has no usable existing identifier; where the fire and rescue function is held by a body already in a standard register it is **referenced** to it, not minted (e.g. Northern Ireland Fire & Rescue Service → `GB-GOR-OT759`; a county council that is the FRA → its `GB-LAE` id; a Police, Fire & Crime Commissioner holding fire → its `GB-OPCC` id). Combined and metropolitan fire authorities, the Scottish Fire and Rescue Service and the London Fire Commissioner are statutory bodies / corporations sole with no charity number, company number or government-organisation code, so they otherwise fall through the gap of the existing identifier schemes.

### Geographic coverage
GB (the United Kingdom, including Northern Ireland).

### Legal structure
Statutory body / corporation sole (fire and rescue authority).

### Sector
Fire and rescue / public safety.

### List type
Third-party.

### Information about the list
https://github.com/rcvda/fire-authority-names-and-codes

### Looking up identifiers / open-data copy
Open CSV: https://github.com/rcvda/fire-authority-names-and-codes/blob/main/data/register.csv — look up the authority by name/area; the `org_id` column holds the `GB-FRA` code (or the referenced external id).

### Licence
Open Government Licence v3.0 (the data derives from the Find That Charity register, ONS geography, and Home Office / LGA / APCC public sources, all OGL).

### Example identifier (verified)
`GB-FRA-00006` — Cleveland Fire Authority. Minted by RCVDA; Cleveland Fire Authority has no charity number, company number, or government-organisation (GB-GOR) code — a genuine identifier gap (its trading arm, Cleveland Fire Brigade Risk Management Services CIC `GB-COH-07583911`, is a separate body). Also recorded in RCVDA's CRM.

### Relevance
Used for linking UK voluntary-sector and public-sector organisation data, in the same ecosystem as Find That Charity and 360Giving. Sibling to RCVDA's police force register (`GB-POL`) and police & crime commissioner register (`GB-OPCC`); where a Police, Fire & Crime Commissioner holds fire, the fire record references the same `GB-OPCC` body. Modelled on mySociety's `uk_local_authority_names_and_codes`.
