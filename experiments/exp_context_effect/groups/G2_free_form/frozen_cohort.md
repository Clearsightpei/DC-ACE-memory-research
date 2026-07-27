# G2 Frozen Retry Cohort (v7.3, pos 300)

*Created 2026-07-24 as part of B5 self-evolution decision (evolution.md
pos 326). These items reached `retry_n ≥ 3` with identical failure
modes across three separate batches (B3, B4, B5) and received no
transferable memory guidance. They are FROZEN from the active retry
scan cohort until UNFROZEN by explicit evidence.*

**Freeze policy**:
1. Items in this file are **NOT** candidates for the errata scan.
2. They remain in `errata.md` for provenance and cross-reference.
3. Their existence does NOT count against retry-pass-rate metrics
   (denominator now excludes them).
4. **Unfreeze condition**: if a structurally-adjacent character
   PASSes in a later batch (e.g. 攵 for the 夂 family, or a 二-lid
   compound for the 旡 family), the curator may explicitly unfreeze
   the item in evolution.md and return it to the active pool.

---

## Frozen items (as of B5 close, pos 300)

| item_id | target | retry_n | first_fail | frozen_at | failure pattern (invariant across retries) |
|---------|--------|---------|------------|-----------|---------------------------------------------|
| p2_radical_058_马 | 马 | 3 | B1 | B5/pos 250 | top-box + tail schema unstable; body-height fixes never transfer |
| p2_radical_080_尢 | 尢 | 3 | B2 | B5/pos 250 | missing top-一 lid → reads as 九 across 3 fixes |
| p2_radical_081_夂 | 夂 | 3 | B2 | B5/pos 250 | 捺 fails to dominate 撇; length-differential knob never sufficient |
| p2_radical_089_车 | 车 | 3 | B2 | B5/pos 250 | differential-横 lengths never distinctive; symmetric-王 collapse |
| p2_radical_094_风 | 风 | 3 | B2 | B5/pos 250 | 横折弯钩 boxy-corner persists; ambiguous with 冈 |
| p2_radical_099_旡 | 旡 | 3 | B2 | B5/pos 250 | copy-无-layout protocol fails; leg-pair splay ambiguous |
| p2_radical_106_牛 | 牛 | 3 | B2 | B5/pos 250 | 65-vs-165 differential never decisive vs 午 |

Additionally: **p2_radical_093_方** and **p2_radical_100_见** and
**p2_radical_042_巛** and **p2_radical_088_长** are at `retry_n=2` or
have crossed into retry_n=3 in prior fails but are NOT frozen yet.
They remain eligible for the active scan pool. If they fail again in
B6, they graduate into this file at that point.

---

## B6 duplicate-of-frozen guard

If a B6 curriculum item is itself one of the frozen chars (e.g.
**311 风** is a frozen radical item, drawn again as a P3 char), the
Drawer draws it normally as a P3 main attempt — the freeze applies
only to the RETRY mechanism, not to the main curriculum. Main-curriculum
attempts on frozen chars are watched for accidental unfreeze evidence
(if the fresh main attempt PASSes with no explicit retry effort, that's
a strong signal to unfreeze the corresponding radical retry).

**B6 items to watch for accidental-unfreeze signals**:
- pos 311 风 → if PASSes on main attempt, unfreeze p2_radical_094_风.

---

## Change log

- **2026-07-24 @ pos 300**: file created; 7 items frozen from B5 close
  (per evolution.md pos 326 decision).
