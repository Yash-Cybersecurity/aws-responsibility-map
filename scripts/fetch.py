import yaml, pathlib, time, json
from normalize import fetch_html, normalize, digest

sources = yaml.safe_load(open("data/sources.yaml"))
manifest_path = pathlib.Path("snapshots/manifest.json")
manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
changed, errors = [], []
for service, urls in sources.items():
    for url in urls:
        slug = url.rstrip("/").split("/")[-1].replace(".html", "")
        out = pathlib.Path(f"snapshots/{service}/{slug}.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            text = normalize(fetch_html(url))
        except Exception as e:
            errors.append({"url": url, "error": str(e)})
            continue
        h = digest(text)
        if manifest.get(url) != h:
            changed.append({"service": service, "url": url, "path": str(out)})
            out.write_text(text, encoding="utf-8")
            manifest[url] = h
        time.sleep(2)
manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True))
pathlib.Path("snapshots/changes.json").write_text(json.dumps({"changed": changed, "errors": errors}, indent=2))
print(f"changed: {len(changed)}, errors: {len(errors)}")