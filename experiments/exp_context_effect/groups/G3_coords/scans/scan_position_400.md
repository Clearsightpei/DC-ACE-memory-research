# Errata scan @ position 400 (B7 end / B8 start) — G3 curator

**Regime**: v9 visual-diff retry prompt (new). Under this prompt the
B7r rerun graduated 3/10 retries — 大 (retry_5), 主 (retry_1), 疒
(retry_1). B8 retries continue under v9.

**Cooldown-50 rule**: no item may be retried within 50 curriculum items
of its last retry. Items retried at position 350 (B7r) are cooldown
until position 400 — B8 (401-450) is the earliest eligible re-window
for the 7 that FAILed the v9 rerun.

## Retry candidates for B8 (positions 401-450)

### (a) Prospective — prereqs for 401-450

Peek at upcoming items 401-450 (from curriculum ordering):
- **矢-family** — 矢 FAILed in B7 with X-crossing apex issue. 大 now has
  the tapered-bezier recipe (bank #201). Retry as first-round for 矢
  and its close cousin 失 (both B7 FAILs).
- **乔** — B7 FAIL, same X-crossing family as 大. Retry with 大 recipe
  as template.
- **也 sub-radical** — needed for upcoming 池/驰/她. Not in bank; B7
  rerun FAIL for 他 shows 也 still unsolved. Attempt as a fresh
  Phase-2-style sub-item under a placeholder id? — deferred; keep in
  the 化/他 pool for now.

### (b) Retrospective — items now more likely to pass under v9 recipe

- **p3_char_0197_矢** (B7 FAIL) — Apply 大 (bank #201) tapered-bezier
  X-crossing recipe. Highest-confidence retry candidate.
- **p3_char_0216_失** (B7 FAIL) — Same as 矢. X-crossing bottom + short
  top.
- **p3_char_0226_乔** (B7 FAIL) — Same X-crossing family (夭 top).
- **p3_char_0193_癶** (B7 FAIL) — Bilateral X-crossing symmetric mirror;
  needs kiss_apex re-attempt now that 大's fresh-render recipe exists.
- **p2_radical_011_匕** (retry_5 by now) — Still needs solving; blocks
  化/花/华. B7r rerun FAIL was execution not diagnosis; try once more
  under v9 with explicit reference to 匕's sandbox diagnosis.
- **p3_char_0134_化** (retry_2) — Depends on 匕. Chain retry AFTER 匕
  passes. Skip B8 unless 匕 passes first.
- **p3_char_0173_仔** (retry_2) — B7r rerun FAIL because drawer inlined
  fresh 子 instead of calling `zi_char` (bank #122). Retry with
  EXPLICIT instruction to call zi_char verbatim at ox=+40, scale=0.65.
- **p3_char_0176_平** (retry_2) — B7r rerun diagnosed correctly but
  render still off. One more retry with 主 (bank #202) as template.

### Freeze / skip

- **p2_radical_028_人**, **p2_radical_030_入** — Both TERMINAL_FREEZE
  AGAIN after v9 rerun FAIL. Two independent prompt-generation lifts
  (v8 signature freedom + v9 visual diff) both failed. Format ceiling
  on X-crossing for these two specific items is now empirically
  confirmed. **Do not schedule for B8 or later**. Note that 大's PASS
  shows the format ISN'T universally the ceiling — the difference is
  probably that 人/入 have only two strokes, so every calligraphic
  detail is load-bearing; 大 has a 3rd stroke (heng) that carries the
  read.
- **p3_char_0154_他** — B7r rerun FAIL on 也 sub-component. Keep in
  retry pool for B9+ AFTER 也 solved as sub-item.
- Cursive hook family (刀, 弓, 己, 马, 长, 见, 巛, 幺) — unchanged from
  scan_position_350; format ceiling still holds.
- **B7 mains left in errata** — 34 items; most are single-shot fails.
  Only the 4 X-crossing candidates above and the 3 v9-recipe-retryable
  ones get B8 slots to keep retry queue lean.

## Retry queue for B8 (in dispatch order — 10 slots max)

1. p3_char_0197_矢 (retry_1) — X-crossing, 大-recipe template
2. p3_char_0216_失 (retry_1) — X-crossing, 大-recipe template
3. p3_char_0226_乔 (retry_1) — X-crossing family
4. p3_char_0193_癶 (retry_1) — bilateral X-crossing
5. p2_radical_011_匕 (retry_5) — one more shot; unblocks 化/花/华
6. p3_char_0173_仔 (retry_2) — EXPLICIT zi_char call
7. p3_char_0176_平 (retry_2) — 主-recipe template
8. p3_char_0174_主 — GRADUATED B7r; skip
9. p3_char_0171_疒 — GRADUATED B7r; skip
10. Slot free — reserve for a B8-main FAIL if it turns up an obvious
    prereq.

## Measurement plan for B8 retry channel

- Grep retry `generated.py` files for `VISUAL DIFF` header (v9 signal).
  Goal: 7/7 include it (the prompt now mandates it).
- Retry PASS rate: goal ≥ 30% (matches B7r baseline; > 20% keeps v9
  earning its keep).
- Bank template propagation: for the 3 X-crossing candidates (矢/失/乔),
  goal is ≥ 2 that visibly cite bank #201 (大_char.py) in their
  generated.py. If 0/3 cite the template, the "learnable recipe
  propagates" hypothesis is falsified in-batch.
- If retry pass rate < 15% and no template propagation: memory format
  IS the ceiling for these items — recommend the head curator consider
  a v10 intervention (e.g., add a bezier/tapered-stroke primitive
  library to the bank, or explicitly allow numpy raster ops).
