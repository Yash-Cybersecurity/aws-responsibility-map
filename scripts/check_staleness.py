import glob, yaml, datetime, sys
today = datetime.date.today()
stale = 0
for path in glob.glob("data/services/**/*.yaml", recursive=True):
    e = yaml.safe_load(open(path))
    d = e.get("review", {}).get("reviewed_on")
    if not d:
        continue
    try:
        rd = datetime.date.fromisoformat(d)
    except ValueError:
        print(f"{path}: bad date {d}")
        continue
    if (today - rd).days > 90:
        print(f"STALE: {path} (reviewed {d})")
        stale += 1
print(f"{stale} stale entries")
sys.exit(0)