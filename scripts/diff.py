import json, difflib, pathlib, re
changes = json.loads(pathlib.Path("snapshots/changes.json").read_text())
KEYWORDS = ["responsib", "customer", "you are", "default", "encrypt", "enabled", "managed"]
out_lines = ["# Snapshot changes", ""]
for c in changes.get("changed", []):
    p = pathlib.Path(c["path"])
    new = p.read_text(encoding="utf-8").splitlines()
    # old from git not available here; just note
    out_lines.append(f"- {c['service']}: {c['url']}")
print("\n".join(out_lines))
pathlib.Path("snapshots/changes.md").write_text("\n".join(out_lines), encoding="utf-8")