# Errata Scan — position 100 (G4 grid-bank)

Scan performed at curriculum position 100 (end of B1 batch, before B2
begins at position 101). Cooldown rule: an item retried at curriculum
position P is on cooldown until P+50.

Reviewed each active errata entry against:
- (a) Prospective — upcoming items 101-150 whose success would depend on
  or benefit from mastering this item.
- (b) Retrospective — new memory (principle bank / bank primitives /
  sandbox rules) since last attempt that specifically addresses the
  prior failure mode.

## New memory since previous scan (position 50)

- **TR12 (new)** — Horizontal endpoints share a cell ROW; vertical
  endpoints share a cell COLUMN. Directly diagnoses 彐's B1 failure
  (s3 head in row 2, tail in row 1 → 100 px diagonal tilt).
- **TR11 empirical update** — Named-agreement compliance did NOT
  correlate with pass rate on B1 main (63% TR11-compliant pass vs 74%
  non-TR11-compliant). Retries hit 4/6 without TR11. Keep TR11 as
  epistemic-honesty rule, do NOT treat it as a pass predictor.
- **Sandbox rule: long compound strokes = one inlined polyline** —
  Pattern E in B1 diagnosis. Applies to 弓, 飞, 马-family. Directly
  addresses the "fragmented compound stroke" failure mode.
- **Sandbox rule: TR9 span for enclosing radicals** — x_frac 0.05-0.95
  AND y_frac 0.05-0.95. Applies to 冂, 门, 马.
- **Sandbox rule: stroke-count parity check** — if MMH stroke count ≠
  drawer's mental count, STOP and re-decompose. Diagnoses 卩 (rendered
  as 3 instead of 2).
- **Sandbox derived-anchor pattern (from 犭 B1 diagnosis)** — compute
  s2's curved-body pixel midpoint FIRST, then set s3.head to match via
  inverse anchor_to_xy. Static ('C', ...) anchors ignore how curved
  strokes bow.

## Cooldown status

B1 retries (丿 retry_n=1 at position ~60; 刀 retry_n=1 at position ~60)
are still on cooldown until roughly position 110. **SKIP both**. The
15 main B1 FAILs are all at retry_n=0 (main-batch first attempts),
NOT on cooldown, and eligible.

Phase-1 items (横斜钩, 横折弯钩, 横折折撇): last attempt was batch 6
refresh (curriculum position ~32) at retry_n=2. Cooldown expires at
~position 82. Now past cooldown, but no new primitive addresses the
compound-stroke gap and no upcoming 101-150 item uses these as
components. **SKIP all three** for lack of both (a) and (b).

---

## Item-by-item decisions (B1 main FAILs)

### p2_radical_023_卩 — SKIP
- **(a) Prospective**: No 卩-family or P-hook + 竖 composition in
  positions 101-150. Weak.
- **(b) Retrospective**: Stroke-count parity rule (new) does address
  the "rendered as 3 not 2" failure, but that's a discipline rule not
  a new primitive.
- Verdict: **SKIP — weak prospective + only meta-rule retrospective.**

### p2_radical_024_冂 — RETRY
- **(a) Prospective — STRONG**: 囗 (073) is an enclosing radical in
  the exact same family; mastering 冂's TR9-span override is a direct
  prerequisite for 囗. 门 will also re-benefit.
- **(b) Retrospective — STRONG**: Sandbox rule (TR9 for enclosing —
  x_frac 0.05-0.95, y_frac 0.05-0.95) is new. Errata prescribes
  concrete anchors (竖 at ('TL', 0.10, 0.15), 横折 at ('TL', 0.20,
  0.15), span to y_frac 0.85+) never applied.
- Verdict: **RETRY.**

### p2_radical_025_力 — SKIP
- **(a) Prospective**: No 力-family composition (勺/勾/勿) in upcoming
  batch. Weak.
- **(b) Retrospective**: TR4/T-weld is not new since batch B1; already
  in bank at time of B1 attempt. No new primitive since.
- Verdict: **SKIP — weak prospective, no genuinely new memory.**

### p2_radical_038_㔾 — RETRY
- **(a) Prospective — VERY STRONG**: 巳 (071) is in the exact 卩/㔾/巳
  family (top piece + bottom 竖弯钩 bowl). 㔾 mastery directly builds
  the anchor plan for 巳.
- **(b) Retrospective — MODERATE**: Errata gives concrete anchor recipe
  (tiny top piece in upper-left of bowl + full-canvas 竖弯钩) that
  never previously applied. TR12 tangentially helps (top piece is
  small horizontal).
- Verdict: **RETRY.**

### p2_radical_039_艹 — SKIP
- **(a) Prospective**: No upcoming item uses 艹 as component (纟, 忄
  etc. are not grass-tops). Weak.
- **(b) Retrospective**: Errata fix (use 竖 not 撇 for the two
  descenders) is a discipline note; no new primitive.
- Verdict: **SKIP — both axes weak.**

### p2_radical_045_寸 — SKIP
- **(a) Prospective**: 寸-family (对/村/守) not in upcoming batch. Weak.
- **(b) Retrospective**: Fix is anchor tuning for the 丶 position; no
  new principle.
- Verdict: **SKIP.**

### p2_radical_047_飞 — RETRY
- **(a) Prospective — MODERATE**: No direct 飞-family in 101-150, but
  长 (088) and 气 (111) both have long compound-sweep top pieces that
  would benefit from the "single inlined polyline" discipline. 欠
  (112) and 手 (117) also involve compound-sweep gestures.
- **(b) Retrospective — STRONG**: NEW sandbox rule "long compound
  strokes = one inlined polyline, not two stubs" directly diagnoses
  the B1 failure (fragmentation into stubs). This is a genuinely new
  principle promoted at end of B1.
- Verdict: **RETRY.**

### p2_radical_050_弓 — RETRY
- **(a) Prospective — MODERATE**: 弓 itself doesn't appear in 101-150,
  but the 3-tier stacked-loop structure recurs in 目/日 patterns and
  the compound-stroke discipline (bootstrap 乙 → shu_zhe_zhe_gou)
  applies broadly.
- **(b) Retrospective — STRONG**: Same "long compound strokes = one
  inlined polyline" rule from B1 sandbox, plus errata's explicit
  vertical-separation fix (s1 y 0-0.35, s2 y 0.45-0.50, s3 y 0.65-1.0)
  never applied.
- Verdict: **RETRY.**

### p2_radical_053_己 — RETRY
- **(a) Prospective — VERY STRONG**: 巳 (071) is essentially 己 with a
  different top-loop closure — same 竖弯钩 up-hook bottom, same
  3-stroke count. Direct prerequisite.
- **(b) Retrospective — STRONG**: TR12 (new) addresses the diagonal-
  horizontal failure mode. Errata prescribes shu_wan_gou with corner
  in BC and tip flicking UP (tip.y < hook_pt.y) — canonical up-hook
  recipe. Sandbox "stroke-count parity" reinforces the 3-stroke plan.
- Verdict: **RETRY.**

### p2_radical_054_彐 — RETRY
- **(a) Prospective — WEAK**: No 彐/彑/ヨ upcoming in 101-150.
- **(b) Retrospective — VERY STRONG**: TR12 is a NEW principle
  written specifically because of 彐's B1 failure. This is the
  textbook case for retrospective retry. Positive calibration case
  (drawer honestly flagged visual_ok=False) — the drawer will trust
  the new rule and apply the literal errata fix (s3 head ('BL', 0.35,
  0.0), s3 tail ('BC', 0.90, 0.0) — both row 2).
- Verdict: **RETRY** (retrospective-only; balance permits when the
  new principle is a bulls-eye fit).

### p2_radical_055_彑 — SKIP
- **(a) Prospective**: No 彑-family upcoming.
- **(b) Retrospective**: Errata fix (compact top-triangle P-weld apex)
  is not backed by a new principle. TR4 was already in bank.
- Verdict: **SKIP — under-attempt is fine here, no new memory + no
  prospective use.**

### p2_radical_058_马 — RETRY
- **(a) Prospective — WEAK-MODERATE**: 马-family (驰/驱) not in
  101-150, but the compound-descender-plus-hook motif (shu_zhe_zhe_gou)
  recurs in 长 (088) and 车 (089) which both have compound descenders.
- **(b) Retrospective — STRONG**: Sandbox "long compound strokes = one
  inlined polyline" applies directly (B1 diagnosis Pattern F). Errata
  prescribes 3-stroke plan reusing existing `shu_zhe_zhe_gou.py` from
  bank. TR2 enclosing-span discipline (also new sandbox rule) fixes
  the "scattered strokes across canvas" defect.
- Verdict: **RETRY.**

### p2_radical_059_门 — RETRY
- **(a) Prospective — STRONG**: 囗 (073) is an enclosing radical — 门
  mastery builds the enclosing-frame discipline (TR2 + TR9 span).
  Both radicals require the same "left wall + top bar + right wall
  spanning ~90% of canvas" pattern.
- **(b) Retrospective — STRONG**: New sandbox rule "TR9 for
  enclosing/large radicals (x_frac 0.05-0.95 AND y_frac 0.05-0.95)"
  directly addresses the "compressed shape floating in a corner"
  defect. Errata prescribes concrete anchor plan (T-weld between
  left 竖 head and heng_zhe_gou head).
- Verdict: **RETRY.**

### p2_radical_061_女 — SKIP
- **(a) Prospective — WEAK**: 女-radical composition doesn't appear as
  a component in 101-150. 妃/妈 etc. not upcoming.
- **(b) Retrospective — WEAK**: Errata fix is anchor tuning (撇点
  pivot up-mid, arm at y_frac 0.60); no new principle beyond what was
  already in bank at B1 time.
- Verdict: **SKIP.**

### p2_radical_062_犭 — RETRY
- **(a) Prospective — STRONG**: 犬 (113) is the sibling radical — same
  bowed 撇 body + short cross-strokes. Also 木 (104), 手 (117) have
  P-cross patterns benefiting from the "shared-pixel P-cross"
  discipline.
- **(b) Retrospective — VERY STRONG**: NEW sandbox pattern (from B1
  犭 diagnosis) — "enforce P-cross with shared pixel not just close
  anchors" AND "N-joint on curved spine needs derived anchor" — is
  the exact fix. Positive calibration case (drawer flagged
  overall_pass=False). Ready to be validated.
- Verdict: **RETRY.**

---

## Summary

- **RETRY (8)**: 冂, 㔾, 飞, 弓, 己, 彐, 马, 门, 犭 — actually **9**
  items. Listing again to be sure:
  - p2_radical_024_冂
  - p2_radical_038_㔾
  - p2_radical_047_飞
  - p2_radical_050_弓
  - p2_radical_053_己
  - p2_radical_054_彐
  - p2_radical_058_马
  - p2_radical_059_门
  - p2_radical_062_犭

- **SKIP (main B1)**: 卩, 力, 艹, 寸, 彑, 女 (6 items) — no
  compelling (a) or (b).

- **SKIP (cooldown)**: 丿 (retry_n=1 during B1), 刀 (retry_n=1 during
  B1), plus Phase-1 items 横斜钩, 横折弯钩, 横折折撇 (post-cooldown
  but no new memory).

## Rationale for size (9 retries)

- Previous scan (position 50) attempted 6/6 eligible bootstrap items;
  4/6 passed. Aggressive retry is validated.
- Prior-run guidance: 2/18 was TOO conservative. Balance not
  minimalism.
- Of 15 B1 main FAILs eligible: 9 retries have a real (a) or (b) — 4
  have STRONG prospective matches to upcoming 101-150 items (冂→囗,
  㔾→巳, 己→巳, 门→囗, 犭→犬), 3 have STRONG retrospective from
  brand-new B1-derived principles (彐→TR12, 飞→"one inlined
  polyline", 弓/马→same + TR2 span). Skipping any of these 9 would
  leave downstream compositions unnecessarily hard.
- 6 SKIPs (卩, 力, 艹, 寸, 彑, 女) are honestly weak on BOTH axes —
  no direct upcoming component use and no genuinely new principle
  since B1.

Re-evaluate at scan position 125.
