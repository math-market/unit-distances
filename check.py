#!/usr/bin/env python3
"""
Deterministic scorer for the unit-distance board (rational plane).

Given a set of distinct points with EXACT RATIONAL coordinates, count the pairs at
distance *exactly* 1.  The score to maximize is the number of unit distances; the record
for a given point count `n` is what a submission tries to beat.  This is the finite,
fully-checkable face of the Erdős unit-distance problem (the asymptotic exponent lives on
the certificate tier — see TASK.md).

Rational coordinates make the check exact: two points (x1,y1), (x2,y2) are at unit distance
iff (x1-x2)^2 + (y1-y2)^2 == 1, evaluated over the rationals — no floating point, ungameable.

Input JSON:
    {"points": [[x, y], ...]}
each coordinate is an integer, a fraction string "p/q", or a pair [num, den].

Output: number of points and unit distances (the score). Exit 0 on a well-formed set,
2 on malformed input.

Uses spatial bucketing (a unit distance forces |dx|,|dy| <= 1), so it stays near-linear.
"""
import json
import sys
from fractions import Fraction


def _coord(c):
    if isinstance(c, bool):
        raise ValueError("coordinate must be a number, not a bool")
    if isinstance(c, int):
        return Fraction(c)
    if isinstance(c, str):
        return Fraction(c)                       # "p/q" or "p"
    if isinstance(c, list) and len(c) == 2:
        return Fraction(c[0], c[1])              # [num, den]
    raise ValueError(f"bad coordinate {c!r}")


def score(obj):
    """Return (ok, message, unit_distance_count | None)."""
    pts = obj.get("points") if isinstance(obj, dict) else None
    if not isinstance(pts, list) or not pts:
        return (False, "input needs a non-empty 'points' list", None)
    P, seen = [], set()
    for k, p in enumerate(pts):
        if not isinstance(p, list) or len(p) != 2:
            return (False, f"point {k} must be [x, y]", None)
        try:
            x, y = _coord(p[0]), _coord(p[1])
        except (ValueError, ZeroDivisionError, TypeError) as e:
            return (False, f"point {k}: {e}", None)
        if (x, y) in seen:
            return (False, f"duplicate point {k}: ({x}, {y})", None)
        seen.add((x, y))
        P.append((x, y))

    # bucket by integer cell; a unit distance only connects same/adjacent cells
    buckets = {}
    for idx, (x, y) in enumerate(P):
        cx, cy = int(x // 1), int(y // 1)         # floor via Fraction
        buckets.setdefault((cx, cy), []).append(idx)

    count = 0
    neigh = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    for (cx, cy), members in buckets.items():
        for i in members:
            xi, yi = P[i]
            for dx, dy in neigh:
                for j in buckets.get((cx + dx, cy + dy), ()):
                    if j <= i:                     # count each pair once
                        continue
                    xj, yj = P[j]
                    if (xi - xj) ** 2 + (yi - yj) ** 2 == 1:
                        count += 1
    return (True, f"{len(P)} points, {count} unit distances", count)


def main(argv):
    if len(argv) != 2:
        print("usage: python3 check.py <points.json>", file=sys.stderr)
        return 2
    try:
        obj = json.load(open(argv[1]))
    except (OSError, json.JSONDecodeError) as e:
        print(f"malformed input: {e}", file=sys.stderr)
        return 2
    ok, msg, c = score(obj)
    if not ok:
        print(f"INVALID  {msg}")
        return 2
    print(f"OK  {msg}  (score = {c})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
