# Errata Scan — position 250 (G4 grid-bank)

Scan performed at curriculum position 250 (B4 → B5 boundary, right
after B4 batch judgment). This is the FIRST scan of B5 and the
SECOND scan under the v7 MANDATORY LOOKUP CHECKLIST regime.

## What B4 taught us

- **Retry PASS rate**: 4/8 (50%), up from B3's 3/10 (30%). Best
  retry-batch under v7 so far. The checklist demonstrably lifted
  citation rate from 18% → 100% (memory-citation grep across B4
  drawers) and delivered PASSes on the three items where the fix
  was one grep away:
    - `p3_char_0025_力` PASS (canonical bank-retrieval test: drawer
      cited just-promoted `li.py` → PASS on first checklist attempt).
    - `p3_char_0028_冖` PASS (drawer found `heng_gou_cover.py` via
      INDEX grep, applied errata's down-left flick).
    - `p3_char_0032_凵` PASS (same-col verticals + same-row bottom;
      form_catalog "enclosing left wall" entry transferred cleanly).
    - `p2_radical_039_艹` PASS (two column-shared 竖 piercing one
      wide 横; form_catalog + joint_atlas both cited).
- **Main-batch first-attempt accuracy**: 62% (best of all 4 groups
  this batch). Checklist is doing real work.
- **New failure mode surfaced**: **retrieval-to-implementation gap.**
  All 4 B4 retry FAILs (纟, 夂, 子, 夊) had 100% citation compliance
  (checklist filled out at top of `generated.py`) but the drawer
  soft-interpreted the retrieved fix at the code site:
    - 纟: cited "two compact 撇折 stacked" but rendered as one long
      staircase; distinct-y-band separation NOT enforced.
    - 夂: cited "derived-anchor on curved body" but rendered s3.head
      as static ('C', ...) anchor.
    - 子: cited "belly x further right in C" but belly x stayed
      symmetric.
    - 夊: cited "s1 as small ク-shape (real curl)" but rendered s1
      as near-straight short stroke.
  Citation count did NOT predict PASS (PASS 5.77 avg cites vs FAIL
  5.84). The bottleneck moved one step downstream: from "did the
  drawer look" to "did the drawer TYPE OUT THE SPECIFIC ANCHORS at
  the call site."
- **Wrong-primitive-pick**: `p3_char_0058_兀` FAILed because drawer
  picked `wu_lame.py` instead of composing `一 + er_legs.py`.
  Citation was correct-file but wrong-structural-equivalent.
  Motivates a B5 checklist addition: at the citation site, name
  the primitive by its FUNCTION not just filename.
- **VALIDATED-marker system introduced**: form_catalog now marks
  patterns with 3+ PASS confirmations as **VALIDATED** vs
  "provisional" (single PASS). Should reduce over-reliance on
  fragile one-off recipes.
- **Chronic 7-item cluster** (丿, 刀, 冂, 飞, 弓, 己, 马) all
  cooled since pos 200 → eligible at pos 250. All at retry_n=2.
  If they re-fail here (retry_n=3), escalate to sandbox as
  chronic literal-instruction violation and candidate for
  hand-written canonical primitives at pos 300.

## Cooldown status at position 250

- **Just-retried at pos 250 (cooldown until pos 300 → INELIGIBLE)**:
  纟 (retry_n=2 FAIL), 夂 (retry_n=2 FAIL), 子 (retry_n=2 FAIL),
  夊 (retry_n=2 FAIL). 艹, 力, 冖, 凵 PASSED and left errata.
- **Chronic cluster (retry_n=2 FAIL at pos 150, cooled at pos 200)**:
  丿, 刀, 冂, 飞, 弓, 己, 马 — cooldown lifted, eligible for retry_n=3.
- **B2 main FAILs with retry_n=0** — screen by (a)/(b) vs 251-300.
- **B3 main FAILs with retry_n=0** — screen by (a)/(b) vs 251-300.
- **Phase-1 items** (横斜钩, 横折弯钩, 横折折撇) at retry_n=2 — no
  new compound-stroke primitive since B2; 251-300 doesn't use them
  as visible components. SKIP.

## Upcoming curriculum 251-300 — direct errata overlaps

Position range: 251 屮 through 300 冘. All 3-4 stroke Phase-3
characters. Direct or component-level errata overlaps:

| pos | char | errata item                             | eligible? | notes |
|-----|------|-----------------------------------------|-----------|-------|
| 252 | 马   | p2_radical_058_马 (retry_n=2 FAIL)      | yes       | CHRONIC + direct char version |
| 257 | 幺   | (bank has yao_small.py)                 | —         | reuse |
| 260 | 弋   | (bank has yi_arrow.py — VALIDATED)      | —         | reuse |
| 271 | 方   | p2_radical_093_方 (B2 FAIL retry_n=0)   | yes       | direct |
| 273 | 日   | (already PASSED — ri.py)                | —         | reuse |
| 275 | 无   | p2_radical_135_无 (B3 FAIL retry_n=0)   | yes       | direct |
| 279 | 心   | (bank has xin.py)                       | —         | reuse |
| 281 | 见   | p2_radical_100_见 (B2 FAIL retry_n=0)   | yes       | direct |
| 287 | 气   | p2_radical_111_气 (B2 FAIL retry_n=0)   | yes       | direct |
| 291 | 文   | p2_radical_124_文 (B3 FAIL retry_n=0)   | yes       | direct |
| 293 | 长   | p2_radical_088_长 (B2 FAIL retry_n=0)   | yes       | direct |
| 298 | 冗   | (冖 just PASSED as mi_cover_char.py + er_legs.py) | — | compose |
| 299 | 内   | p2_radical_024_冂 (retry_n=2 FAIL, CHRONIC) | yes   | CHRONIC + component of 内 |

Chronic-cluster items with NO 251-300 direct char overlap: 丿, 刀,
飞, 弓, 己. Still eligible; screen by (b) — is there a new insight
since pos 200 that specifically addresses the retry_n=2 failure
mode?

## Item-by-item decisions

### RETRY (11)

**1. p2_radical_058_马 — (a) VERY STRONG + chronic cluster**
- (a) VERY STRONG — 马 IS pos 252. Direct.
- (b) MODERATE — no new spine primitive since B2, but the
  retrieval-to-implementation-gap diagnosis from B4 gives a specific
  instruction: the drawer must TYPE OUT `shu_zhe_zhe_gou.py` call
  site with LITERAL anchor tuples, not just cite the filename.
- Escalation clock: retry_n=3. If FAIL, sandbox chronic-list.

**2. p2_radical_100_见 — (a) STRONG**
- (a) STRONG — 见 IS pos 281. Direct.
- (b) STRONG — B2 errata fix explicit: enlarge box y∈[20,180];
  move s3 head to left edge of box (ML(0.9,0.7)); s4 head to right
  edge. TR9 span expansion. Bank has `er_legs.py` for the two legs
  (儿-family bottom).

**3. p2_radical_088_长 — (a) STRONG**
- (a) STRONG — 长 IS pos 293. Direct.
- (b) STRONG — B2 errata: s3 as strict 竖提 (straight vertical + 提
  flick), not curved zigzag. Bank has `shu_ti.py`. Move s1 to
  TC(0.55,0.20)→ML(0.65,0.40). form_catalog § 竖 col-shared invariant
  applies.

**4. p2_radical_093_方 — (a) STRONG**
- (a) STRONG — 方 IS pos 271. Direct.
- (b) STRONG — B2 errata: extend 横折钩 vertical
  (corner MR(0.65,0.55), tail BR(0.65,0.75), tip BC(0.65,0.55));
  ensure visible descent + up-left hook. joint_atlas P + form_catalog
  § 横折钩 in 门 apply as analogous idiom.

**5. p2_radical_135_无 — (a) STRONG**
- (a) STRONG — 无 IS pos 275. Direct.
- (b) STRONG — B3 errata: 无 = 一 + 尢-shape. Bank has `you.py` (尢);
  also `er_legs.py` (儿) is a close cousin per B4 form_catalog note.
  Errata: reuse `wang_lame.py` base + 一 top; enforce same-row 横.
  This is a TR1 override + TR8-rule-5 test.

**6. p2_radical_111_气 — (a) STRONG**
- (a) STRONG — 气 IS pos 287. Direct.
- (b) MODERATE — B2 errata: s4 top-heng at y=0.35 (C or ML row);
  extend descent to canvas bottom; separate s2/s3 to distinct rows.
  Distinct-y-band discipline (same lesson as 纟 retry) applies —
  and 气 is FRESH (retry_n=0) so drawer isn't fighting a chronic
  soft-interpret pattern.

**7. p2_radical_124_文 — (a) STRONG**
- (a) STRONG — 文 IS pos 291. Direct.
- (b) STRONG — B3 errata: enforce shared-pixel P at X apex per
  joint_atlas P rule. Bank has apex-shared patterns (`da.py`, `ren.py`,
  `mu.py` s3+s4). form_catalog § 撇 crossing § 捺 crossing directly
  apply.

**8. p2_radical_024_冂 — (a) STRONG + chronic cluster**
- (a) STRONG — 内 (pos 299) = 冂 + 入. If 冂 PASSes here, 内 becomes
  near-trivial compose. Also 冘 (pos 300) has related enclosing top.
- (b) MODERATE — Errata (retry_n=2 fix): hard-align s1 head y with
  s2 top-bar y both at y=15; reduce frame width to ~230; use
  `_shorten` helper. form_catalog 3-N-corner enclosure VALIDATED
  pattern (口/囗/曰/日/门) directly transfers.
- Escalation: retry_n=3. If FAIL, sandbox.

**9. p2_radical_003_丿 — (b) MODERATE + chronic cluster**
- (a) WEAK — no 丿 char in 251-300 (was pos 205 already, PASSed or
  FAILed as p3_char_0005_丿 in B3 FAIL).
- (b) MODERATE — the B4 retrieval-to-implementation-gap lesson
  applies with maximum force here. Errata has said `('TR',0.85,0.15)`→
  `('BL',0.15,0.85)` literally for 3 batches. B5 checklist should
  force "TYPE OUT the literal anchor tuple at the call site."
- Retry BECAUSE the escalation matters for the paper: 3rd retry
  of a literally-prescribed fix. If FAIL at retry_n=3, hard sandbox
  entry + hand-written canonical primitive at pos 300.

**10. p2_radical_015_刀 — (b) MODERATE + chronic cluster**
- (a) WEAK — no 刀 char in 251-300 (刀 char is p3_char_0038 already).
- (b) MODERATE — same escalation logic as 丿. Errata retry_n=2 fix:
  shorten 横 (corner MR 0.10, not 0.55); lengthen vertical descender
  (BC 0.60,0.60); 撇 tail slightly less far left (BL 0.35,0.85).
- Retry for escalation-clock parity with 丿.

**11. p2_radical_050_弓 — (b) MODERATE + chronic cluster**
- (a) WEAK — no 弓 char in 251-300.
- (b) MODERATE — errata fix (retry_n=2): rewrite every 横折 as
  {heng, straight down-drop sharing corner.x with tail.x}; redo s3
  as `shu_zhe_zhe_gou.py` composed. form_catalog § 竖 col-shared
  invariant (VALIDATED). B4 lesson about typing out anchors at call
  site applies.
- Retry for cluster completeness — bundles with 己 as tightly-related
  3-tier compositions.

### Items considered and SKIPPED

**Cooldown-blocked (retried at pos 250, cooldown to 300)**:
- p2_radical_070_纟 (retry_n=2 FAIL; also pos 234 — already drawn
  as p2 radical during 201-250)
- p2_radical_081_夂
- p2_radical_082_子
- p2_radical_084_夊

**Chronic cluster (eligible at pos 250) — skipped despite eligibility**:
- p2_radical_047_飞 — (a) WEAK (飞 was pos 239, no re-appearance in
  251-300). (b) The errata fix demands ONE polyline call, drawer has
  failed to comply 3 batches running. New B5 checklist ("type out
  the primitive at call site") is worth trying but bundle with 丿/刀/
  弓/己 already stress-tests it. Save 飞 for pos 300 canonical
  hand-write.
- p2_radical_053_己 — (a) WEAK, (b) MODERATE. Very tightly bound to
  弓 (same 3-tier composition family). Retrying 弓 is the higher-value
  bet because 弓 is the more common shape. If 弓 PASSes, 己 fix is
  transparent for pos-300 scan. SKIP 己 to keep retry list to 11.

**B2 main FAILs with no 251-300 (a) driver + no fresh (b)**:
- 卩, 寸, 彑, 犭, 㔾, 夕, 贝, 比, 歹, 斗, 厄, 风, 戈, 户, 火, 旡, 斤,
  耂, 肀, 爿, 攴, 欠, 氏, 礻, 手, 殳 — spot-checked all vs 251-300.
  None appear as chars or direct-component drivers. SKIP all.

**B3 main FAILs with no 251-300 (a) driver**:
- 水, 瓦, 毋, 牙, 爫, 支, 爪, p3_0007_乛, p3_0011_人, p3_0016_乃,
  p3_0018_乜, p3_0021_几, p3_0023_九, p3_0026_冂, p3_0005_丿.
  p3_0026_冂 covered by p2_024_冂 retry above. p3_0005_丿 covered by
  p2_003_丿 retry above. Others: no strong (a). SKIP.

**B4 main FAILs with no fresh (b) and no 251-300 (a) driver**:
- 丁, 匕, 之, 丸, 久, 也, 亾, 兀, 么, 卂, 与, 叉, 及, 孓, 女, 才 —
  most were pos 205-249 with retry_n=0. Screen vs 251-300:
  - 亾: no. 兀: pos 268 亓 has similar 一+bottom structure but
    亓 is 一+丌, not directly analogous. WEAK. SKIP.
  - 才 (pos 244 CJK): no 251-300 char reuse. SKIP.
  - 及, 卂: compound-stroke items; drawer keeps splitting beziers.
    Same failure family as 飞. Save for pos 300. SKIP.

**Phase-1 items** (横斜钩, 横折弯钩, 横折折撇): retry_n=2, no new
primitive since B2; 251-300 doesn't use them as visible components.
SKIP.

## Summary

**RETRY (11)** —
- 6 items with DIRECT 251-300 char overlap
  (马, 见, 长, 方, 无, 气, 文 — 7 direct listed but 文 counted separately
  below): **马 (252), 方 (271), 无 (275), 见 (281), 气 (287), 文 (291),
  长 (293)** — 7 direct char-version retries.
- 1 item with STRONG component-driver (冂 → 内 pos 299).
- 3 chronic-cluster items on ESCALATION CLOCK (丿, 刀, 弓) — retry_n=3
  test of B4-introduced "type-out-at-call-site" checklist addition.

Final list (11):

1. p2_radical_058_马   — (a) VERY STRONG pos 252 + CHRONIC
2. p2_radical_100_见   — (a) STRONG pos 281
3. p2_radical_088_长   — (a) STRONG pos 293
4. p2_radical_093_方   — (a) STRONG pos 271
5. p2_radical_135_无   — (a) STRONG pos 275
6. p2_radical_111_气   — (a) STRONG pos 287
7. p2_radical_124_文   — (a) STRONG pos 291
8. p2_radical_024_冂   — (a) STRONG pos 299 (内) + CHRONIC
9. p2_radical_003_丿   — (b) escalation-clock retry_n=3
10. p2_radical_015_刀  — (b) escalation-clock retry_n=3
11. p2_radical_050_弓  — (b) escalation-clock retry_n=3

**SKIP** — 4 cooldown-blocked (纟, 夂, 子, 夊); 2 chronic-cluster items
saved for pos 300 canonical hand-write (飞, 己); ~50 B2/B3/B4 main
FAILs with no 251-300 driver; 3 Phase-1 items. Total skipped ~60.

## Rationale for size (11 retries)

- Pos 100: 9 retries → 22%. Pos 150: 10 → 30%. Pos 200: 8 → 50%.
  Trend positive under the checklist. **B5 goal**: maintain or
  lift 50% while stress-testing the retrieval-to-implementation
  gap fix.
- 7 direct-char-overlap retries (马, 见, 长, 方, 无, 气, 文) —
  this is the largest direct-overlap cluster of any batch (pos
  250-300 is dense with 3-4 stroke chars that ARE their own
  radicals). Not retrying these would leave obvious wins on the
  table.
- 1 component-driver retry (冂 → 内 pos 299) — same logic as B4's
  冖 → 宀 attempt (which PASSed).
- 3 escalation-clock chronic retries (丿, 刀, 弓) — deliberately
  fewer than "all 5 remaining chronic items" to avoid diluting
  the signal. 丿 tests literal-anchor discipline (single-stroke
  radical, cleanest test). 刀 tests joint-weld + proportion
  discipline. 弓 tests 3-tier composition + bundle-transfer to 己.
  飞 and 己 saved for pos 300 (飞 needs a new inlining primitive;
  己 will inherit 弓's fix if 弓 PASSes).
- 11/~20 eligible-with-real-trigger ≈ 55% eligibility use. Slightly
  higher than pos 200's 53% because the direct-overlap cluster is
  unusually rich.

## What the B5 batch will tell us (research signal)

- **Direct-overlap retry PASS rate**: if 5-7 of the 7 direct-char
  retries (马/见/长/方/无/气/文) PASS, the checklist + retrieval
  discipline is now compounding across radical→char reuse. If <3
  PASS, retrieval-to-implementation gap is still the bottleneck
  even with a fresh (retry_n=0-1) target.
- **Component-driver test (冂 → 内)**: if 冂 PASSes, 内 (pos 299)
  should trivially PASS. Paired signal.
- **Escalation-clock test (丿/刀/弓 retry_n=3)**: if any of the
  three PASSes, the "type-out-at-call-site" checklist addition
  is working. If all 3 FAIL, the chronic cluster needs
  hand-written primitives at pos 300 (as flagged in memory_index).
- **Retrieval-to-implementation gap check**: B5 curator should grep
  for cases where the drawer cited the correct fix filename but
  used different anchors — that's the direct measurement of the
  gap.

Re-evaluate at scan position 275 (mid-B5).
