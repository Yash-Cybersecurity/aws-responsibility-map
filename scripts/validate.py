import sys, glob, json, yaml, os
from jsonschema import Draft202012Validator

schema = json.load(open("schema/entry.schema.json"))
v = Draft202012Validator(schema)
bad = 0
AI_DOMAINS = {"prompt-and-data-handling", "guardrails-and-output-filtering"}

for path in glob.glob("data/services/**/*.yaml", recursive=True):
    try:
        entry = yaml.safe_load(open(path))
    except Exception as e:
        print(f"{path}: YAML parse error: {e}")
        bad += 1
        continue
    for err in v.iter_errors(entry):
        print(f"{path}: {err.message}")
        bad += 1
    # service folder matches service field
    folder = os.path.basename(os.path.dirname(path))
    if entry.get("service") != folder:
        print(f"{path}: service folder '{folder}' != service '{entry.get('service')}'")
        bad += 1
    if not entry.get("sources"):
        print(f"{path}: no sources")
        bad += 1
    if not entry.get("review", {}).get("reviewed_on"):
        print(f"{path}: no review date")
        bad += 1
    # AI entries must carry deployment_scope, sub_feature, layer
    if entry.get("control_domain") in AI_DOMAINS or entry.get("deployment_scope"):
        for f in ("deployment_scope", "sub_feature", "layer"):
            if entry.get(f) is None and entry.get("control_domain") in AI_DOMAINS:
                print(f"{path}: AI entry missing {f}")
                bad += 1
    # non-null model_provider requires quote + source_type
    mp = entry.get("responsibility", {}).get("model_provider")
    if mp:
        for s in entry.get("sources", []):
            if not s.get("quote") or not s.get("source_type"):
                print(f"{path}: model_provider set but source lacks quote/source_type")
                bad += 1
    # contractual entries must link a terms page (url containing terms)
    if entry.get("contractual"):
        if not any("terms" in (s.get("url") or "").lower() for s in entry.get("sources", [])):
            print(f"{path}: contractual entry must link a terms page")
            bad += 1

sys.exit(1 if bad else 0)