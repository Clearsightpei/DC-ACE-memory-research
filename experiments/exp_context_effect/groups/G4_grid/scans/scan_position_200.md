# Errata Scan — position 200 (G4 grid-bank)

Scan performed at curriculum position 200 (B3 → B4 boundary, right
after B3 batch judgment). This is the SECOND scan under v7
self-evolution and the first under the new **MANDATORY LOOKUP
CHECKLIST** in `memory_index.md`.

## What B3 taught us

- **Retry PASS rate**: 3/10 (30%), up from 2/9 (22%) at pos 150.
  Modest lift, but the improvement clusters on items where the
  drawer HAD the exact fix in errata + a promoted sibling in the
  bank (力 got a fresh `li.py`-sibling recipe; 女 got the P-weld
  recipe; 日 got the wall-to-wall middle bar).
- **Chronic FAILs re-failed**: 丿, 刀, 冂, 飞, 弓, 己, 马 — all
  retry_n=2. Failure mode is now consistent across two retries:
  drawer SOFT-INTERPRETS the errata's literal pixel/anchor
  prescription. `p2_radical_003_丿` has now failed a literal
  errata instruction three times.
- **Memory retrieval discipline** (the B3 curator's diagnosis):
  a grep across B3 drawer files showed only 18% of drawers opened
  `form_catalog.md` or `joint_atlas.md` before writing code. The
  memory content was fine; the problem was that drawers weren't
  consulting it. B3 curator responded by adding the MANDATORY
  LOOKUP CHECKLIST to `memory_index.md` (5 numbered lookups,
  each requiring a one-line comment at the top of `generated.py`).
  **B4 (positions 201-250) is the first batch under the checklist
  regime** — this scan's retry list will be one of the signals of
  whether the checklist lifts citation rate and, by proxy, retry
  pass rate.

## Cooldown status at position 200

- **Just-retried at pos 200 (cooldown until pos 250 → INELIGIBLE)**:
  丿, 刀, 冂, 飞, 弓, 己, 马 (all retry_n=2 FAIL); 力, 女, 日 PASSED
  and left errata.
- **B2 retries at pos 100 → cooldown expired long ago; NOT re-retried
  at pos 150 (犭, 㔾) → still eligible**. But (a) drivers are weak:
  犬 (sibling of 犭) and 巳 (sibling of 㔾) already PASSed.
- **B1/B2/B3 main FAILs with retry_n=0** → eligible; screen by (a)/(b).
- **Phase-1 (横斜钩, 横折弯钩, 横折折撇)** at retry_n=2. No new
  compound-stroke inlining primitive since B2. Still SKIP.

## Upcoming curriculum 201-250 — direct errata overlaps

| pos | char | errata item                     | eligible? |
|-----|------|---------------------------------|-----------|
| 216 | 子   | p2_radical_082_子 (B2 FAIL)     | yes       |
| 229 | 门   | (already PASSED — men.py)       | —         |
| 232 | 囗   | (no direct — sibling of 冂 on cooldown) | — |
| 234 | 纟   | p2_radical_070_纟 (B2 FAIL)     | yes       |
| 236 | 夂   | p2_radical_081_夂 (B2 FAIL)     | yes       |
| 238 | 夊   | p2_radical_084_夊 (B2 FAIL)     | yes       |
| 239 | 飞   | p2_radical_047_飞 (COOLDOWN 250)| no        |
| 244 | 艹   | p2_radical_039_艹 (B1 FAIL)     | yes       |
| 246 | 宀   | (no direct — related p3_0028_冖 in errata) | — |
| 247 | 女   | (already PASSED — nv.py)        | —         |
| 248 | 尢   | (bank has wang_lame.py)         | —         |

## Item-by-item decisions

### RETRY (8)

**1. p2_radical_039_艹 — (a) STRONG**
- (a) 艹 IS pos 244. Direct prerequisite.
- (b) Errata fix concrete: two 竖 (not diagonals) piercing single
  wide 横 in a 卄-like pattern; verticals column-share (TR8 rule 6).
  `form_catalog.md` 竖-in-spine idiom + joint_atlas P shared-pixel
  rule both apply. Checklist forces both lookups.

**2. p2_radical_070_纟 — (a) STRONG**
- (a) 纟 IS pos 234.
- (b) B2 errata fix: two compact 撇折 stacked tightly along x=0.35
  with pivots in same column; s3 提 head directly under s2 tail,
  sweeping up-right. Model after `yao_small.py` (幺, already in
  bank as `yao.py`/`yao_small.py`). Bank retrieval + form_catalog
  stacked-fold pattern both directly apply.

**3. p2_radical_081_夂 — (a) STRONG**
- (a) 夂 IS pos 236.
- (b) Errata fix: s2 head TC(0.35,0.10) → BL(0.10,0.90); s3 (捺)
  head attaches ON s2 body mid (T-joint), sweeps to BR corner.
  `joint_atlas.md` § T rule (bowed 撇 body needs derived anchor,
  not chord midpoint — 夊 lesson noted explicitly) applies.
  Also see how `pu.py` handles 攵-family X.

**4. p2_radical_082_子 — (a) STRONG**
- (a) 子 IS pos 216.
- (b) Errata fix: raise s1 head to TL(0.55, 0.20); s2 belly x
  further right in C; hook_pt further left so tip sweeps well
  up-left. `wan_gou.py` in bank; `form_catalog.md` § 弯钩
  entries apply. Checklist grep on `success_bank/INDEX.md` will
  surface `wan_gou.py` directly.

**5. p2_radical_084_夊 — (a) STRONG (positive-calibration item)**
- (a) 夊 IS pos 238.
- (b) B2 errata: s1 as small ク-shape at top-center; s2 head just
  below s1 tail with N-gap ~15 px; s3 head T-welds s1 body at
  (~90, 150). Positive calibration case (drawer honestly flagged
  overall_pass=False in B2) — the fix diagnosis is clean and the
  drawer's judgment about failure was correct. Applying the fix
  literally should PASS.

**6. p3_char_0025_力 — (b) STRONG (fresh bank promotion)**
- (a) MODERATE — 力-family (勺/勿/办) not directly in 201-250, but
  the compound heng-zhe-gou + T-weld pie idiom recurs.
- (b) VERY STRONG — `li.py` was JUST promoted to Success Bank in
  the B3 retry PASS (p2_radical_025_力 at scan position 200).
  Errata explicitly notes p3_char_0025_力 FAILed precisely
  because the drawer didn't retrieve the just-promoted bank
  entry. The B3 checklist's lookup #1 (`success_bank/INDEX.md`
  grep) directly addresses that miss. This is a canonical test
  case for whether the checklist works.

**7. p3_char_0028_冖 — (a) STRONG**
- (a) 冖 (cover) is a direct prerequisite for 宀 (pos 246) — 宀
  is 冖 + 点 above. Also 冖 shape recurs implicitly in many
  covered-top characters. If 冖 PASSes and gets bank-promoted,
  宀 becomes near-trivial.
- (b) Bank has `heng_gou_cover.py` (mentioned in errata fix).
  Errata fix: short 点-like head + horizontal + short right-drop.
  Checklist forces bank INDEX grep → drawer will find
  heng_gou_cover.py directly.

**8. p3_char_0032_凵 — (a) MODERATE + (b) STRONG**
- (a) MODERATE — 凵 (bracket) is a container shape; 囗 (pos 232)
  and 山 (pos 233) both use enclosing/bracket geometry. 凵-body
  discipline (left 竖 + bottom 横 + right 竖, all N-joints small
  gap) is prerequisite discipline for 囗.
- (b) STRONG — `form_catalog.md` § 竖 "enclosing left wall" entry
  (from 口/门 PASSes) transfers. Errata fix explicit: same-col
  for verticals (TR8 rule 6) and same-row for bottom horizontal
  (TR8 rule 5). Checklist's form_catalog + joint_atlas lookups
  both apply directly.

### Items considered and SKIPPED

**Cooldown-blocked (retried at pos 200, cooldown to 250)**:
- p2_radical_003_丿 (also blocks p3_char_0005_丿 — sibling has just
  failed; retrying p3 char alone unlikely to succeed).
- p2_radical_015_刀
- p2_radical_024_冂 (also blocks p3_char_0026_冂).
- p2_radical_047_飞 — DIRECT pos 239 conflict, but strict cooldown
  rule applies. B4 main-item attempt at 飞 will draw on fresh
  errata note ("force ONE polyline call"); no retry option here.
- p2_radical_050_弓
- p2_radical_053_己
- p2_radical_058_马

**Retry-n=1 with weak (a) at pos 150 → still weak now**:
- p2_radical_062_犭 — 犬 sibling passed. No 犭-family in 201-250. SKIP.
- p2_radical_038_㔾 — 巳 sibling passed. No 㔾-family upcoming. SKIP.

**Retry_n=0 with no upcoming (a) driver**:
- p2_radical_023_卩 — no 卩-family upcoming. SKIP.
- p2_radical_045_寸 — no 寸-family (对/村/守) upcoming. SKIP.
- p2_radical_055_彑 — no 彑/彐-family upcoming. SKIP.
- 29 B2 main FAILs (夕/贝/比/长/歹/斗/厄/方/风/戈/户/火/旡/见/斤/耂/肀/爿/攴/气/欠/氏/礻/手/殳/月/…) —
  spot-checked each vs 201-250; ONLY 月 (pos 162) already passed. **None
  overlap with 201-250. SKIP all 29.**
- B3 main FAILs (水/瓦/文/毋/牙/爫/支/爪/无/p3_0007_乛/p3_0011_人/p3_0016_乃/
  p3_0018_乜/p3_0021_几/p3_0023_九) — none in 201-250 as component
  driver. p3_0011_人 (apex weld) has weak (b) via joint_atlas P
  rule but no strong (a). SKIP all.

**Phase-1 items** (横斜钩, 横折弯钩, 横折折撇): retry_n=2, no new
inlining primitive since B2. Downstream 201-250 doesn't use them
as visible components. SKIP.

## Summary

**RETRY (8)** — 5 items with direct pos-201-250 curriculum
prerequisite (纟, 夂, 夊, 子, 艹), 1 with direct child-radical
prerequisite (冖 → 宀), 1 with strong bracket-transfer (凵 → 囗),
and 1 canonical bank-retrieval test (p3_char_0025_力 with
freshly-promoted li.py).

1. p2_radical_039_艹  — (a) pos 244
2. p2_radical_070_纟  — (a) pos 234
3. p2_radical_081_夂  — (a) pos 236
4. p2_radical_082_子  — (a) pos 216
5. p2_radical_084_夊  — (a) pos 238
6. p3_char_0025_力    — (b) freshly-promoted li.py; canonical
                          checklist test case
7. p3_char_0028_冖    — (a) pos 246 宀 direct child
8. p3_char_0032_凵    — (a) pos 232 囗 bracket transfer + (b)
                          form_catalog enclosing recipe

**SKIP** — 7 chronic-cooldown items (丿, 刀, 冂, 飞, 弓, 己, 马);
2 weak-prospective retry_n=1 (犭, 㔾); 3 no-driver retry_n=0
(卩, 寸, 彑); 29 B2 main-FAIL no-overlap; ~15 B3 main-FAIL
no-overlap; 3 Phase-1 items. Total skipped ~59.

## Rationale for size (8 retries)

- Pos 100: retried 9 → 2 PASS (22%). Pos 150: retried 10 → 3 PASS
  (30%). Trend positive but modest. Balance not minimalism.
- 5 of 8 retries have STRONG (a) — the upcoming character IS the
  radical or shares its exact composition. This is the tightest
  (a) coupling possible.
- 1 retry (p3_char_0025_力) is a canonical test of the B3
  MANDATORY LOOKUP CHECKLIST: the failure mode was explicitly
  "drawer skipped bank retrieval." If the checklist works, this
  should PASS on first-checklist-batch retry.
- 1 retry (p3_char_0028_冖) unlocks pos 246 宀 as a near-trivial
  compose (冖 + 点).
- Chronic 7 items on cooldown; not eligible. If they re-fail
  eligibility at pos 250 (would be retry_n=3), consider escalating
  to sandbox as memory-retrieval-discipline chronic cases.
- 8/~15 eligible-with-real-trigger items ≈ 53% eligibility use.
  Higher than pos 150's 10/27 (37%) because the upcoming batch
  hits SO many radical-errata items directly (5 direct matches
  in 50 items — unusually rich cluster).

## What the B4 batch will tell us (research signal)

- **Retry PASS rate under the checklist**: if it lifts to 5/8+
  (≥60%), the checklist is doing real work. If it stays at 3/8
  (~30%, current baseline), memory retrieval was not the
  bottleneck — the bottleneck is drawer literal-instruction
  compliance (see chronic 丿/刀).
- **Bank-retrieval test (p3_char_0025_力)**: if this specific item
  PASSes, checklist item #1 is validated. If FAILs, drawer is
  ignoring the checklist even when the fix is one grep away.
- **Enclosing-radical transfer (冖 → 宀; 凵 → 囗)**: two paired
  tests of whether a mastered small enclosing shape lifts a
  larger sibling in the same batch.

Re-evaluate at scan position 225 (mid-B4).
