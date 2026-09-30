# Dependency Risk Scorer

Ranks named dependencies using supplied impact, likelihood, and exposure duration factors. It exposes a deterministic prioritisation score rather than predicting an outage.

## Architecture

```text
JSON payload → domain algorithm → evidence-backed findings → human review
                              └→ OpenAI / CrewAI / Claude Code / Lyzr export surfaces
```

The core implementation is `agent.py` and exposes `analyze(payload)`. Tests include valid, malformed, boundary, and domain-specific cases.

## Run

```bash
python3 agent.py examples/good-input.json
python3 -m unittest discover -s tests -v
python3 tools/audit-dependency-risk-scorer.py examples/good-input.json
```

## Limitations

The score is subjective and does not observe incidents, vulnerability data, reliability history, controls, or correlated failures. It cannot quantify probability, expected loss, compliance, or remediation effectiveness.
