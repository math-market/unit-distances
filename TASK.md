# Task — The Unit-Distance Problem (after the 2026 disproof)

*A Math Market board on Erdős's unit-distance problem. In **May 2026** an OpenAI reasoning model
**disproved** the 80-year-old conjecture that `n` points span at most `n^{1+o(1)}` unit distances —
exhibiting a family with `≥ n^{1+δ}` for a fixed `δ > 0` (verified in a 9-author companion paper;
Gowers said he'd recommend it for the Annals). The exact growth rate is now **wide open**, and there
is a live race to push the exponent up. This board hosts the checkable pieces of that race.*

Package: `TASK.md` · `check.py` (exact rational scorer, tested) · `generator_example.py` (baselines) · `examples/`.

---

## The problem

How many pairs of `n` points in the plane can be at distance **exactly 1**? Let `u(n)` be the max.
- **Upper bound:** `u(n) = O(n^{4/3})` (Spencer–Szemerédi–Trotter 1984) — exponent `≤ 4/3`.
- **Old belief (now false):** `u(n) = n^{1+o(1)}` (grid-like), Erdős's conjecture.
- **New lower bound (2026):** `u(n) ≥ n^{1+δ}`, `δ > 0` fixed. The true exponent `c` satisfies
  **`0.03583… ≤ c ≤ 1/3`** (Tao, Jul 2026) — a huge gap, and the surface area for this board.

## Tiers

### Tier A — the auto-verified board: **most unit distances among `n` rational points**
Submit a set of points with **exact rational coordinates**; `check.py` counts pairs at distance
exactly 1 (over the rationals — no floating point, ungameable) and reports the score. Beat the best
known for your `n`.

- **Submit:** `{"points": [[x, y], …]}`, each coordinate an integer, a fraction string `"p/q"`, or a
  pair `[num, den]`. Points must be distinct.
- **Check:** `python3 check.py your.json` → `score = <# unit distances>` in `O(n)` (spatial-bucketed).
- **Why rational?** It makes the check *exact and instant*. Rational configurations are also a genuine
  research object in their own right (the triangular lattice — optimal but irrational — is off-limits),
  studied directly by Rodis, *Algorithmic exploration of the unit distance problem in the rational
  plane* (arXiv:2606.29415). Baseline to beat: the integer grid gives only `2L(L−1) ≈ 2n`
  (`generator_example.py`); the optimum is superlinear.

### Tier B — the frontier: **improve the asymptotic exponent `δ`**
This is the famous problem the disproof reopened. A submission is a **unit-distance lower-bound
certificate** — a compact tuple `(T, S_Q, {k(p)}, R)` (ramified primes, split primes, integer
multiplicities, a rational parameter `R`) — plus the claimed exponent `1+δ`. It is verified by the
published **feasibility inequalities + closed-form** for `δ`, all in exact arithmetic.

- **Records:** verified **δ = 0.014114** (Sawin, arXiv:2605.20579) and **δ ≈ 0.031** (Emmerich,
  arXiv:2606.03419); **claimed δ ≈ 0.03583** (Naslund, unverified on the tracker). Target: `1/3`.
- **Live leaderboard:** Tao's optimization-problems tracker, [constant 84a](https://teorth.github.io/optimizationproblems/constants/84a.html).
- **Checker:** wrap Emmerich's open-source optimization+verification pipeline (arXiv:2606.03419) as the
  oracle — it self-tests by reproducing Sawin's `δ = 0.014114`. *(To finalize this tier, transcribe the
  exact feasibility inequality from arXiv:2606.03419 §nonlinear-integer-optimization.)*

### Tier C — expert-reviewed: **a genuinely new asymptotic construction**
A new family (not a re-parameterized certificate) is refereed by experts — as the 9-author *Remarks*
paper (arXiv:2605.20695) refereed the original AI construction. Not mechanically auto-checkable;
prestige/expert tier.

## How verification works

- **Tier A** is a pure deterministic scorer: exact rational arithmetic, no oracle, no review — the
  checker makes the reviewer's call trivial and lets you confirm your own score before submitting.
- **Tier B** is exact but wraps the certificate feasibility check (Emmerich's pipeline).
- **Tier C** needs human refereeing.

## Sourcing & attribution

The unit-distance problem is Erdős (1946). The 2026 disproof: an OpenAI reasoning model, verified in
Alon–Bloom–Gowers–Litt–Sawin–Shankar–Tsimerman–Wang–Wood, *Remarks on the disproof of the unit
distance conjecture* (arXiv:2605.20695); explicit exponent Sawin (arXiv:2605.20579); certificate
optimization Emmerich (arXiv:2606.03419); rational-plane experiments Rodis (arXiv:2606.29415);
synthesis Tao, *A digestion of unit distance constructions* (Jul 2026). The mathematical facts are
not copyrightable; do not copy others' code except per license. Records above are current to late
July 2026 — **re-verify before treating any as the bar** (the tracker distinguishes verified vs.
claimed). (See `../../problems-to-solicit.md` → Sourcing & attribution.)
