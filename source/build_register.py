import json, csv, sys, os
SRC = sys.argv[1] if len(sys.argv) > 1 else "source/fra_authorities.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "data/register.csv"
SDIR = os.path.dirname(SRC) or "."
CODES = os.path.join(SDIR, "code_assignments.csv")
TODAY = "2026-11-12"
A = json.load(open(SRC))
ledger = {r["fra_id"]: r["gb_fra"] for r in csv.DictReader(open(CODES)) if not r["fra_id"].startswith("_withdrawn_")}
HDR = ["org_id","name","body_type","fire_rescue_authority_area","ons_fra_code","fra_function_held_by",
       "paired_police_id","status","issued_by","date_issued","evidence","notes"]
FTC = "no entry in GB-LAE / GB-GOR / Charity / Companies House / FCA (Find That Charity bulk cache 2026-09-13)"
def build(x):
    oid = ledger[x["id"]]; area = x["area"]; model = x["model"]; held = x["held_by"]
    paired = x.get("paired_police_id",""); extra = x.get("note_extra","")
    if x.get("mint"):
        if model == "london-commissioner":
            evid = f"London Fire Commissioner: corporation sole (Policing and Crime Act 2017), the statutory FRA for Greater London under Mayor of London oversight; {FTC}. Minted as a genuine gap (direct parallel of MOPAC -> GB-OPCC)."
            note = "RCVDA-minted: corporation sole, no register ID (genuine gap). Function held by the Mayor of London via the Commissioner."
        elif model == "scotland-national":
            evid = f"Scottish Fire and Rescue Service: single national statutory body (devolved; not in GB-GOR); {FTC}. Minted as a genuine gap (parallels Police Scotland)."
            note = "RCVDA-minted: national statutory body, no company/charity/GB-GOR ID (genuine gap)."
        elif x.get("ror"):
            evid = f"Statutory combined fire & rescue authority. Appears in FTC only under ROR ({x['ror']}); ROR is not a usable principal identifier, so minted. Otherwise {FTC}."
            note = "RCVDA-minted: statutory FRA, ROR-only is not a usable identifier (genuine gap)."
        else:
            kind = "metropolitan" if model == "metropolitan-fra" else "combined"
            evid = f"Statutory {kind} fire & rescue authority. {FTC[0].upper()+FTC[1:]}. Genuine identifier gap."
            note = "RCVDA-minted: statutory fire & rescue authority (genuine gap)."
    else:
        ref = x["ref_id"]
        if model == "pfcc":
            evid = f"Fire function held by the {area} Police, Fire & Crime Commissioner ({ref}) under the single-employer model; same corporation sole as the commissioner in the GB-OPCC register. Referenced, not minted."
            note = f"NOT minted: fire function held by an existing identifiable body (the PFCC); keyed to {ref}. Paired to the police governance register."
        elif model == "mayoral":
            evid = f"Fire function held by {held} ({ref}); the combined authority is an existing identifiable body. Referenced, not minted."
            note = f"NOT minted: function held by {held}; keyed to its own ID {ref}."
        elif model == "ni":
            evid = f"Fire Authority for Northern Ireland holds a government-organisation code ({ref}); FTC bulk cache 2026-09-13. Referenced, not minted (parallels PSNI -> GB-GOR-OT657)."
            note = f"NOT minted: holds {ref} in the GB-GOR register; keyed to it."
        else:
            evid = f"Fire function is a service of {held} ({ref}); the council is the fire & rescue authority. Referenced, not minted."
            note = f"NOT minted: function held by {held}; keyed to its own local-authority ID {ref}."
    if extra:
        note = note + " " + extra
    return [oid, x["name"], "fra", area, "", held, paired, "Active", "RCVDA", TODAY, evid, note]
rows = [build(x) for x in A]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(HDR); w.writerows(rows)
m = sum(1 for r in rows if str(r[0]).startswith("GB-FRA-"))
ref = len(rows) - m
print(f"rows:{len(rows)} GB-FRA minted:{m} referenced:{ref}")
