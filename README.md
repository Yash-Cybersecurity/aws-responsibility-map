# AWS Shared Responsibility Reference

> **Unofficial community project. Not affiliated with or endorsed by AWS. AWS documentation and AWS Artifact are authoritative.**

A public, change-tracked reference that answers, for a given AWS service and security control: **who owns it — AWS, the customer, or (for AI services) the model provider?**

Every cell ships with a source URL, a short verbatim quote, and a retrieval date. `not_stated` is a first-class value; we never guess.

## Quick links

- Legend (responsibility vocabulary)
- Matrix (services × controls)
- By service / By control
- What changed
- Evaluation results

## v1 scope

- Services: S3, EC2, IAM, RDS, Bedrock
- Control domains (~15): encryption at rest, encryption in transit, key management, identity and access, network exposure, logging and monitoring, patching, backup and recovery, data classification, vulnerability management, physical security, incident response, configuration management, prompt and data handling (AI), guardrails and output filtering (AI)
- Target ~75 reviewed entries

## Stack

Data: YAML validated by JSON Schema · Site: Astro + Pagefind · Automation: GitHub Actions · Scripts: Python 3.11+

## Local setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate.py
cd site && npm install && npm run dev
```

## Contributing

Open an issue using the error-report template, or submit a PR. Every entry must have a source URL, quote, and retrieval date.

## License

Code: MIT. Original data and text: CC BY 4.0. AWS documentation remains the property of Amazon Web Services.