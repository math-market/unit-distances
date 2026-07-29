# Unit Distances — a Math Market board (after the 2026 disproof)

In **May 2026** an OpenAI model [disproved](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)
Erdős's 80-year-old unit-distance conjecture, showing `n` points can span `n^{1+δ}` unit distances
(`δ>0`) — not `n^{1+o(1)}` as believed. The exact growth rate is now wide open
(`0.03583… ≤ c ≤ 1/3`), and there's a live race to push it. This board hosts the checkable pieces.

- **The task:** [`TASK.md`](TASK.md) — the problem, the tiers, the records.
- **The scorer:** [`check.py`](check.py) — counts unit distances among **exact rational** points
  (over the rationals, so the check is exact and instant). Tested.
- **Baselines:** [`generator_example.py`](generator_example.py) — the integer grid (`~2n`); the record is superlinear.

## Two tiers

- **Tier A (auto-verified board):** *most unit distances among `n` rational points.* Submit
  `{"points": [[x,y], …]}` (rationals); `check.py` reports the score; beat the best known for your `n`.
- **Tier B (the frontier):** *improve the asymptotic exponent `δ`* — submit a certificate tuple
  `(T, S_Q, {k(p)}, R)` + claimed `δ`, verified by the published feasibility inequalities. Records:
  verified `δ≈0.031` (Emmerich), claimed `≈0.03583` (Naslund); target `1/3`. Live tracker:
  [constant 84a](https://teorth.github.io/optimizationproblems/constants/84a.html).

## Submit (Tier A)

Fork → add `submissions/<handle>.json` = `{"points": [[x,y], …]}` → open a PR. CI runs `check.py`
and reports your unit-distance count.

```bash
python3 check.py submissions/your.json                    # score = # unit distances, exact
python3 generator_example.py grid 8 | python3 check.py /dev/stdin
```

Coordinates: integers, fraction strings `"p/q"`, or `[num, den]` pairs. Rational only — that's what
makes the check exact (and is a genuine research object; see the Rodis rational-plane paper in TASK.md).
