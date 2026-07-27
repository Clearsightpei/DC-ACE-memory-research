# Errata Scan — position 300 (G4 grid-bank)

Scan performed at curriculum position 300 (B5 → B6 boundary, right
after B5 batch judgment). This is the FIRST scan of B6 and the
FOURTH scan under the v7 MANDATORY LOOKUP CHECKLIST regime.

The B5-review portion of this file (retrospective outcome table,
canonical-primitive rationale) was written at position 300 by the
same curator. See `evolution.md` @ 2026-07-24 for the change log.
This section adds the **prospective errata plan for B6** — which
items are retried in positions 301-350 and why.

## B5 outcome table (retrospective)

| Batch | Main | Retries | Cumulative | Notable |
|-------|-----:|--------:|-----------:|---------|
| B1    | 35/50 (70%) | 4/6 (67%) | 70% | Baseline (v6) |
| B2    | 20/50 (40%) | 2/9 (22%) | 55% | Regression → v7 split |
| B3    | 29/50 (58%) | 3/10 (30%) | 56% | Checklist added |
| B4    | 31/50 (62%) | 4/8 (50%)  | 58% | Best batch under v7 |
| **B5**| **26/50 (52%)** | **0/11 (0%)** | **57.1%** | Collapse + canonical primitives |

## B5 investigation summary (retrospective)

1. **Citation rate**: 26/50 main use the literal "MANDATORY LOOKUP
   CHECKLIST" header string (52%). All 50 cite success_bank + errata
   + form_catalog inline. Header ritual is a false signal — drawers
   dropped the header, kept the substance. Citation discipline from
   position 200 still holds.

2. **Retry FAILs at retry_n=3 (chronic cluster)**: two distinct
   patterns.
   - **Willful override** (丿 retry_3): docstring quotes the errata
     verbatim, then code writes different anchors with the comment
     "GT shows a more vertical sweep."
   - **Mechanical compliance without success** (马 retry_2): every
     errata rule applied (TR8, TR9, primitive reuse, hook up-left),
     9 pre-render asserts pass, panel still FAILs.

3. **Main FAILs pattern**: char-heavy B5 exposes a synthesis
   failure mode different from B2's radical-heavy retrieval failure.
   FAILs cluster around characters where NO structurally-close bank
   primitive exists AND MMH anchors give a tilted layout the drawer
   can't correct without inventing.

4. **B5 vs B2 comparison**: different failure floors. B2 was
   solved by mandatory-lookup discipline (checklist at position 200).
   B5 exposes a synthesis-ceiling that discipline alone can't lift.

## Curator changes recorded at position 300

- **Created `success_bank/code/chronic/`** with 5 hand-written
  canonical primitives: `pie_radical.py` (丿), `dao_char.py` (刀),
  `jiong_frame.py` (冂), `gong_bow.py` (弓), `ma_horse.py` (马).
  Each is a no-arg `draw_<x>(draw)` baking the anchor plan.
- **Retired retry mechanism** for the 5 chronic items. Their
  retry_n freezes at 3. Errata entries stay for record with
  "SUPPLANTED" marker.
- **26 B5 main PASSes** recorded in `p3_char_bank_b5.py` aggregator
  (data records, not 26 thin-wrapper files).
- **35 FAIL diagnoses** added to `errata.md` (24 main + 11 retry).
- **`memory_index.md`** step 1 updated to direct drawers to
  chronic-cluster canonical primitives.
- **`form_catalog.md`** B5 additions with new char-context patterns.
- **`sandbox.md`** B5 diagnosis appended with "citation floor,
  synthesis ceiling" model.

## Self-evolution decision (retrospective)

Adopted **canonical hand-written primitives** for the chronic
cluster. Rejected alternatives:
- ~~Retire retry mechanism wholesale~~ — the mechanism still works
  for fresher errata items (B4 mid-batch graduated 4).
- ~~Aggressive memory prune~~ — no file has crossed a "too big"
  threshold; form_catalog + joint_atlas + principles_meta each fit
  in one drawer read window.
- ~~Force-type-out errata at citation site~~ — evidence from 马
  retry_2 shows perfect literal application can still fail; the
  mechanism doesn't address the ceiling.

## Falsifiable B6 prediction

- Chronic 5 canonical primitives PASS → mechanism validated;
  chronic-cluster retry pass rate jumps from 0/5 → 5/5.
- If any FAILs, **edit the primitive (not the errata)** — still
  cheaper than free-form retry.
- B6 main-pass rate 50–60% (no lever applied to main-batch
  synthesis floor yet).
- B6 retry pass rate ≥50% (canonical primitives lift chronic 5;
  new-retry 6 still face the interpretation gap).

---

# Prospective — B6 retry plan (positions 301-350)

## Upcoming curriculum (301-350) — all Phase-3 chars, 3-5 stroke

301 化, 302 刅, 303 比, 304 刈, 305 水, 306 礻, 307 反, 308 办,
309 区, 310 勻, 311 风, 312 勿, 313 队, 314 卅, 315 书, 316 升,
317 引, 318 卞, 319 元, 320 卬, 321 他, 322 必, 323 们, 324 甲,
325 出, 326 申, 327 可, 328 甴, 329 生, 330 丱, 331 对, 332 乍,
333 去, 334 乎, 335 用, 336 疋, 337 发, 338 疒, 339 只, 340 仔,
341 主, 342 仕, 343 平, 344 仗, 345 外, 346 付, 347 打, 348 仝,
349 正, 350 仞

## Chronic 5 — EXCLUDED (mechanism-supplanted)

丿, 刀, 冂, 弓, 马 are OFF the active retry list at position 300.
Their canonical primitives in `success_bank/code/chronic/` are the
answer. Drawers hitting these items in B6 call
`draw_pie_radical(draw)` / `draw_dao_char(draw)` /
`draw_jiong_frame(draw)` / `draw_gong_bow(draw)` /
`draw_ma_horse(draw)` directly per `memory_index.md` step 1.

**B6 collision points** (chronic primitives called as sub-parts of
B6 chars):
- 引 (pos 317) → `draw_gong_bow(draw)` + right 丨.
- Any 内-family or 冂-frame char in B6 → `draw_jiong_frame(draw)`.
- 化 (pos 301) etc. do NOT touch chronic 5 directly.

If any chronic primitive FAILs panel in B6, edit the primitive file
— NOT the errata. Per B5 falsifiable prediction protocol.

## Direct-match errata items (STRONG (a)) — 6 retries

These errata items map to a B6 curriculum position 1:1, so retrying
the radical during B6 builds the exact primitive the char version
will need. All at **retry_n=0**, no cool-down.

### 1. `p2_radical_086_比` — B6 pos 303 是 char-level 比. **RETRY.**
- (a) STRONG: 比 IS pos 303.
- (b) STRONG: B2 errata fix (TR9 span — left half x∈[0.1,0.5], right
  half x∈[0.55,0.95]; visible s4 up-flick) is a mechanical
  transformation the drawer can apply literally.
- Reason: If radical 比 PASSes as retry, char 比 becomes trivial.
- retry_n: 0 → 1.

### 2. `p2_radical_094_风` — B6 pos 311 是 char-level 风. **RETRY.**
- (a) STRONG: 风 IS pos 311.
- (b) STRONG: B2 errata fix (push 横斜钩 hook_pt down to BR(0.50,
  0.80); s4 as proper 捺; enlarge enclosure x∈[70,280] y∈[100,260])
  is a specific anchor override.
- Reason: If radical 风 PASSes, char 风 near-trivial. 风's
  横斜钩 body is the same chronic 横斜钩 pattern from p1_stroke_19
  (which is ALSO in errata but not directly in B6) — a PASS here
  would give evidence about the 横斜钩 family too.
- retry_n: 0 → 1.

### 3. `p2_radical_116_礻` — B6 pos 306 是 char-level 礻. **RETRY.**
- (a) STRONG: 礻 IS pos 306.
- (b) STRONG: B2 errata fix (extend stem upward to head C(0.55,
  0.35); shorten 横撇 horizontal; two flanking 点 symmetric) is
  concrete.
- retry_n: 0 → 1.

### 4. `p2_radical_119_水` — B6 pos 305 是 char-level 水. **RETRY.**
- (a) STRONG: 水 IS pos 305.
- (b) STRONG: B3 errata fix (竖钩 spine + two flanking short 撇 +
  short 捺; reference GT for exact stroke pattern) is compositional.
  Bank has `shu_gou` and pie/na primitives.
- retry_n: 0 → 1.

### 5. `p2_radical_045_寸` — B6 pos 331 对 = 又+寸. **RETRY.**
- (a) STRONG: 对 contains 寸 as right component.
- (b) STRONG: B1 errata fix (place 点 in the crotch near C(0.60,
  0.55) → C(0.80, 0.75), NOT upper-right corner) is a specific
  anchor override. Bank has `shi_ten.py` or 十-family for the top
  cross; 丶 primitive for the dot.
- retry_n: 0 → 1.

### 6. `p2_radical_075_夕` — B6 pos 345 外 = 夕+卜. **RETRY.**
- (a) STRONG: 外's left component is 夕.
- (b) MODERATE: B2 errata fix (shorten s2 heng, lengthen pie tip)
  is a concrete anchor tweak.
- retry_n: 0 → 1.

## New-retry set (retry_n=1 → retry_n=2, B5 curator prescribed)

Per B5 curator instructions and evolution.md @ position 300 entry,
the 6 items that FAILed at retry_n=1 in B5 advance to retry_n=2 in
B6. All have literal errata fixes prescribed. Cool-down from B5
retry (mid-B5 ≈ pos 275) expires around pos 325 — retry any time
after that inside B6 is valid.

### 7. `p2_radical_088_长` — retry_n=1 → 2. **RETRY.**
- (b) STRONG: B5 literal fix — `shu_ti.py` VERBATIM with head=('C',
  0.55, 0.30), knee=('BC', 0.55, 0.85), tip=('BR', 0.35, 0.55). No
  local tuning.
- (a) WEAK: 长 not in B6 window (pos 293 already past).

### 8. `p2_radical_093_方` — retry_n=1 → 2. **RETRY.**
- (b) STRONG: B5 literal fix — `heng_zhe_gou.py` as-is with corner
  ('MR', 0.65, 0.55), tail ('BR', 0.65, 0.75), tip ('BC', 0.65,
  0.55). No local belly.
- (a) WEAK: 方 not in B6 window.

### 9. `p2_radical_100_见` — retry_n=1 → 2. **RETRY.**
- (b) STRONG: B5 literal fix — s4 head=('MR', 0.30, 0.80), hook_pt=
  ('BR', 0.30, 0.60), tip=('BR', 0.25, 0.25).
- (a) WEAK: 见 not in B6 window.

### 10. `p2_radical_111_气` — retry_n=1 → 2. **RETRY.**
- (b) STRONG: B5 literal fix — distinct y-bands (s2 0.35, s3 0.55,
  s4 0.15); ONE `stroke_variable_width` polyline for compound
  spine.
- (a) WEAK: 气 not in B6 window.

### 11. `p2_radical_124_文` — retry_n=1 → 2. **RETRY.**
- (b) STRONG: B5 literal fix — define APEX=('BC', 0.50, 0.30) as a
  shared tuple; pass identical tuple to pie head and na head.
- (a) WEAK: 文 not in B6 window.

### 12. `p2_radical_135_无` — retry_n=1 → 2. **RETRY.**
- (b) STRONG: B5 literal fix — reuse `wang_lame.py` UNCHANGED for
  尢 base + `heng.py` row-locked for top 一.
- (a) WEAK: 无 not in B6 window.

## B4 carry-overs at retry_n=3 — one more attempt (B5 curator note)

B5 curator prescribed ONE more B6 attempt for these 4. If they FAIL
at retry_n=3 in B6, they escalate to canonical primitives at
position 350 (same mechanism as chronic 5). Cool-down from B4 retry
(scan pos 250) has fully expired.

### 13. `p2_radical_070_纟` — retry_n=2 → 3. **RETRY (final).**
- (b) STRONG: B4 literal fix — distinct y-bands (top 撇折 tail y∈
  [80,130]; middle 撇折 tail y∈[150,210]) with pivots in DIFFERENT
  rows.
- Escalation: if FAIL, promote to canonical `chronic/si_silk.py`.

### 14. `p2_radical_081_夂` — retry_n=2 → 3. **RETRY (final).**
- (b) STRONG: B4 literal fix — derived-anchor technique: precompute
  s2 pie body pixel at t=0.35 (~px 130, 130); place s3.head there
  via inverse `anchor_to_xy`. Do NOT use static ('C', ...) anchor.
- Escalation: if FAIL, promote to canonical `chronic/zhi_go.py`.

### 15. `p2_radical_082_子` — retry_n=2 → 3. **RETRY (final).**
- (b) STRONG: B4 literal fix — s1 head=('TL', 0.55, 0.20); s2 head=
  ('TC', 0.45, 0.20), belly=('C', 0.65, 0.60) [push right hard],
  hook_pt=('BC', 0.25, 0.70) [far left], tip=('BC', 0.35, 0.35).
  Do NOT symmetrize.
- Escalation: if FAIL, promote to canonical `chronic/zi_child.py`.

### 16. `p2_radical_084_夊` — retry_n=2 → 3. **RETRY (final).**
- (b) STRONG: B4 literal fix — s1 as quad_bezier from TC(0.50,
  0.10) → belly TC(0.70, 0.35) → tail ML(0.25, 0.55) (real curl);
  s3.head at ('C', 0.05, 0.15) via derived-anchor at s1 body t≈0.7.
- Escalation: if FAIL, promote to canonical `chronic/sui_walk.py`.

## Not retried at position 300 — reasons

Errata items considered but NOT retried this scan. Reasons follow
the shared_rules v6 "balance, not minimalism" clause — no retry
without an (a) or (b) reason.

- **`p1_stroke_19_横斜钩`** (retry_n=2): no B6 curriculum char with
  横斜钩 as primary compound (气 has it but 气 is p2_radical_111,
  already in retry set — 气's compound spine subsumes the same
  fix). (b) has no NEW insight since B3 retry.
- **`p1_stroke_25_横折弯钩`** (retry_n=2), `p1_stroke_29_横折折撇`
  (retry_n=2): occur in 乙/九/及/廷/建, none in B6 window.
- **`p2_radical_023_卩`** (retry_n=0): 卬 (pos 320) has 卩-family
  right side, weak (a). Deferred to B7 scan — no B5 lever addresses
  the 3-vs-2 stroke-count confusion yet.
- **`p2_radical_038_㔾`** (retry_n=1): cool-down from B2 retry
  (~pos 100) fully expired, but no B6 char uses 㔾. Defer.
- **`p2_radical_047_飞`** (retry_n=2): 飞 not in B6, chronic
  interpretation gap. Bundled with 气 retry — if `stroke_variable_width`
  polyline works for 气 in B6, promote 飞 fix by transfer at B7 scan.
- **`p2_radical_053_己`** (retry_n=2): no B6 char uses 己 directly.
  Bundled with 弓 (SUPPLANTED) — the 3-tier composition family is
  effectively deferred; if canonical `gong_bow.py` PASSes B6, 己
  becomes a candidate for canonical treatment at pos 350.
- **`p2_radical_055_彑`, `_062_犭`, `_085_贝`, `_090_歹`, `_091_斗`,
  `_092_厄`, `_096_戈`, `_097_户`, `_098_火`, `_099_旡`, `_101_斤`,
  `_102_耂`, `_105_肀`, `_107_爿`, `_109_攴`, `_112_欠`, `_115_氏`,
  `_117_手`, `_118_殳`**: none of these radicals map to B6 chars
  (301-350 are 3-5 stroke chars; these radicals appear in higher
  stroke-count chars downstream). Defer without (a); no B5 lever
  changes (b).
- **`p2_radical_120_瓦`, `_125_毋`, `_127_牙`, `_130_月`, `_131_爫`,
  `_132_支`, `_134_爪`**: same — no B6 collision.
- **B5 main FAILs (24 items, retry_n=0)**: none in B6 curriculum
  window. Fresh chronic-canonical mechanism at pos 300 is the
  B6-relevant lever for cross-referenced sub-parts (chronic 5). The
  24 items become retry candidates at pos 325 mid-scan or pos 350.
- **`p3_char_0011_人`** (retry_n=0): B6 has 9 亻-family chars (化
  们 仔 仕 仗 付 仝 他 仞), so P-apex weld discipline is heavily
  reused. But retrying char 人 as errata is unlikely to help those
  — 亻 is a well-defined side radical with its own bank entry, not
  a re-derivation of 人. Skip; rely on 亻 bank primitive.

## Retry list summary

**16 retries queued for B6** (positions 301-350):

Direct-match (6): `p2_radical_086_比`, `p2_radical_094_风`,
`p2_radical_116_礻`, `p2_radical_119_水`, `p2_radical_045_寸`,
`p2_radical_075_夕`.

New-retry advance (6): `p2_radical_088_长`, `p2_radical_093_方`,
`p2_radical_100_见`, `p2_radical_111_气`, `p2_radical_124_文`,
`p2_radical_135_无`.

B4 carry-over final attempt (4): `p2_radical_070_纟`,
`p2_radical_081_夂`, `p2_radical_082_子`, `p2_radical_084_夊`.

## Retry-rate self-assessment

Total active errata pool ≈ 60 items (excluding 5 SUPPLANTED and 4
GRADUATED). 16/60 = 27% retry rate this scan.

Compare to prior scans: pos-250 was 11/20 pending = 55%; pos-200
was 7/14; pos-150 was 3/9. This scan's 27% is intentionally lower
than pos-250 because (i) chronic 5 exclusion removes the most
obvious repeat candidates, (ii) B5 main FAILs (24 new items) are
too fresh to have (a) coverage in B6. Under the "balance not
minimalism" clause this feels right — we retry every item with a
strong (a) match to B6 curriculum (6/6 possible) plus every item
the B5 curator explicitly prescribed for B6 (10 more).

If the direct-match set (6 items) PASSes at ≥4/6, that validates
the "(a) is a strong signal" rule and gives evidence for tightening
future scans around curriculum-collision.

If the B4 carry-over final attempts (4 items) FAIL at ≥2/4, that
gives the position-350 scan a bank of items ready for
canonical-promotion, extending the chronic-cluster mechanism.
