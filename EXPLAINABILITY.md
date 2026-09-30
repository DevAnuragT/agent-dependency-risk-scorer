# Decision and Reasoning

Dependencies are labelled low, medium, or high using fixed score thresholds and the highest score is returned. The result is a heuristic prioritisation signal and not a probability or causal forecast. The implementation returns structured findings so a reviewer can see how each result was derived.

# Inputs and Data Sources

The caller supplies unique dependency names, ordinal impact and likelihood values from one through five, and nonnegative exposure days. Scores include exposure growth capped at one year so very long durations do not grow without bound. The only data source is the caller-provided payload plus the checked-in rules and code; no network or private-file access is used.

# Known Limitations and Constraints

The score is subjective and does not observe incidents, vulnerability data, reliability history, controls, or correlated failures. It cannot quantify probability, expected loss, compliance, or remediation effectiveness. The result is a bounded pre-review aid and must not be presented as professional certification or an official HiDevs result.
