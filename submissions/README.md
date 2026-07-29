# Submissions (Tier A — rational unit-distance board)

Add `submissions/<your-handle>.json` = `{"points": [[x, y], ...]}` via a PR from your fork.
Coordinates: integers, `"p/q"` fraction strings, or `[num, den]`. Points must be distinct.

CI runs [`../check.py`](../check.py) and reports your **unit-distance count** (the score to maximize).
Run it locally first: `python3 check.py submissions/your.json`.

Beat the best known count for your point total `n`. The integer grid gives only ~2n — the record is
superlinear (see [`../TASK.md`](../TASK.md)). Tier B (asymptotic exponent δ) is certificate-based —
see TASK.md.
