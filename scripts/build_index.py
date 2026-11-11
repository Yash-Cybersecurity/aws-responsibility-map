import glob, yaml, json, os
entries = []
for path in sorted(glob.glob("data/services/**/*.yaml", recursive=True)):
    e = yaml.safe_load(open(path))
    entries.append(e)
os.makedirs("site/public/data", exist_ok=True)
with open("site/public/data/index.json", "w") as f:
    json.dump(entries, f, indent=2)
# CSV export
import csv
with open("site/public/data/export.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["service", "control_domain", "overall", "review_status", "reviewed_on"])
    for e in entries:
        w.writerow([e.get("service"), e.get("control_domain"), e.get("overall"),
                    e.get("review", {}).get("status"), e.get("review", {}).get("reviewed_on")])
print(f"wrote {len(entries)} entries")