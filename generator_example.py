#!/usr/bin/env python3
"""
Reference baselines for the rational unit-distance board — legitimate but NON-record.

  * grid   — the L×L integer grid: 2L(L-1) unit distances on L² points (~2n). Trivial baseline.
  * rotate — the same grid rotated by the rational orthonormal basis u=(3/5,4/5), v=(4/5,-3/5);
             still exact rational, same count — shows coordinates need not be axis-aligned.

Both are baselines only. The optimum is superlinear — n^{1+δ} unit distances — and the record
lives in cleverer rational constructions (see README: Rodis's rational-plane methods, and the
certificate approach behind the 2026 disproof). Beating ~2n substantially is the research.

    python3 generator_example.py grid 5 | python3 check.py /dev/stdin
"""
import json
import sys
from fractions import Fraction


def grid(L):
    return [[i, j] for i in range(L) for j in range(L)]


def rotate(L):
    u = (Fraction(3, 5), Fraction(4, 5))
    v = (Fraction(4, 5), Fraction(-3, 5))
    pts = []
    for m in range(L):
        for k in range(L):
            x = m * u[0] + k * v[0]
            y = m * u[1] + k * v[1]
            pts.append([[x.numerator, x.denominator], [y.numerator, y.denominator]])
    return pts


def main(argv):
    method = argv[1] if len(argv) > 1 else "grid"
    L = int(argv[2]) if len(argv) > 2 else 6
    pts = {"grid": grid, "rotate": rotate}.get(method)
    if pts is None:
        print("usage: python3 generator_example.py [grid|rotate] <L>", file=sys.stderr)
        return 2
    json.dump({"points": pts(L)}, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
