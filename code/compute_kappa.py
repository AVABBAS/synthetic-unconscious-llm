#!/usr/bin/env python3
"""Per-variable raw agreement + Cohen's kappa between Pass 1 and Pass 2 coding sheets.
Run after pass2-*.csv exist. Stdlib only. Kappa marked 'not estimable' when a
variable is constant in either pass (per coding-and-contrast-plan.md §5 caveat)."""
import csv, os, sys
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))

def load(path, key='session'):
    with open(path, newline='', encoding='utf-8') as f:
        return {r[key]: r for r in csv.DictReader(f)}

def kappa(pairs):
    n = len(pairs)
    if n == 0:
        return None, None
    po = sum(1 for a, b in pairs if a == b) / n
    ca = Counter(a for a, _ in pairs); cb = Counter(b for _, b in pairs)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in set(ca) | set(cb))
    if pe >= 1.0:
        return po, 'not estimable (constant variable)'
    return po, (po - pe) / (1 - pe)

def norm(col, v):
    """Normalise label-format differences between the two sheets (NOT content):
    Pass 1 wrote D2 as 'C'/'J', Pass 2 as 'C-Type'/'J-Type'; D6 capitalisation differed."""
    v = (v or '').strip()
    if col == 'D2':
        return {'C': 'C-Type', 'J': 'J-Type'}.get(v, v)
    if col == 'D6':
        return v.split(' (')[0].strip().lower()
    return v

def compare(label, p1, p2, cols):
    keys = sorted(set(p1) & set(p2))
    print(f"\n== {label} (n={len(keys)} sessions) ==")
    for col in cols:
        pairs = [(norm(col, p1[k].get(col, '')), norm(col, p2[k].get(col, ''))) for k in keys]
        po, k = kappa(pairs)
        dis = [kk for kk, (a, b) in zip(keys, pairs) if a != b]
        ks = f"{k:.3f}" if isinstance(k, float) else str(k)
        print(f"{col:8s} agreement={po*100:5.1f}%  kappa={ks:>28s}  disagreements: {', '.join(dis) if dis else 'none'}")

# Stage 1 (both arms): column names identical in pass1/pass2 files
s1_cols = ['D1', 'F1', 'F2', 'F3', 'F4', 'D2']
try:
    compare('Control Stage 1', load(f'{BASE}/pass1-control-stage1.csv'), load(f'{BASE}/pass2-control-stage1.csv'), s1_cols)
    compare('Original Stage 1', load(f'{BASE}/pass1-original-stage1.csv'), load(f'{BASE}/pass2-original-stage1.csv'), s1_cols)
except FileNotFoundError as e:
    print(f"missing file: {e}"); sys.exit(1)

# Control Stage 2/4: pass1 is split across two files; pass2 is one file.
p1s2 = load(f'{BASE}/pass1-control-stage2.csv'); p1s4 = load(f'{BASE}/pass1-control-stage4.csv')
p1c = {k: {**p1s2.get(k, {}), **p1s4.get(k, {})} for k in set(p1s2) | set(p1s4)}
try:
    p2c = load(f'{BASE}/pass2-control-stage24.csv')
except FileNotFoundError as e:
    print(f"missing file: {e}"); sys.exit(1)
compare('Control Stage 2/4', p1c, p2c, ['D11', 'D10', 'D5_count', 'D7', 'D8', 'D9', 'D12'])

# Original Stage 2/4
p1o2 = load(f'{BASE}/pass1-original-stage2.csv'); p1o4 = load(f'{BASE}/pass1-original-stage4.csv')
p1o = {k: {**p1o2.get(k, {}), **p1o4.get(k, {})} for k in set(p1o2) | set(p1o4)}
for k in p1o:  # Pass 1 sheet names the column D6_solicited_endorsement
    if 'D6_solicited_endorsement' in p1o[k]:
        p1o[k]['D6'] = p1o[k]['D6_solicited_endorsement']
try:
    p2o = load(f'{BASE}/pass2-original-stage24.csv')
except FileNotFoundError as e:
    print(f"missing file: {e}"); sys.exit(1)
compare('Original Stage 2/4', p1o, p2o, ['D5_count', 'D6'])
print("\nNote: D3/D4 are verbatim-text codes; compare them by reading the sheets, not by kappa on strings.")
