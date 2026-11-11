import yaml, glob, json

gold = yaml.safe_load(open("eval/gold_labels.yaml"))
data = {}
for path in glob.glob("data/services/**/*.yaml", recursive=True):
    e = yaml.safe_load(open(path))
    data[(e["service"], e["control_domain"])] = e

correct = 0; total = 0
for g in gold:
    total += 1
    e = data.get((g["service"], g["control_domain"]))
    if e and e.get("overall") == g["expected_overall"]:
        correct += 1
acc = (correct / total * 100) if total else 0
print(f"overall accuracy: {correct}/{total} = {acc:.1f}%")
with open("eval/results.md", "w") as f:
    f.write(f"# Evaluation results\n\nOverall accuracy: {correct}/{total} = {acc:.1f}%\n")