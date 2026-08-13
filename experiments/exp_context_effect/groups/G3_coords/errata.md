# 错题集 — G3 (coord-bank)

## v8 UN-FREEZE (2026-07-25 @ position 350)

Per INTERVENTIONS.md §v8, the terminal freezes on p2_radical_028_人,
p2_radical_030_入, p2_radical_046_大 (retry_n=5 in B5) are LIFTED for
one more attempt each. These freezes were caused by the format
ceiling that v8 unlocks (the `(ox, oy, scale)` convention that
couldn't express X-crossing composition geometry). retry_n is reset
to 4 so each item has one shot remaining before re-freeze.

Curator: at next errata scan, these three items become retry
candidates under the v8-unlocked convention (richer function
signatures + free-form drawer_memory.md + bank-as-reference).

---


## TERMINAL FREEZE — B5 (2026-07-24)

Per shared_rules.md terminal-freeze rule (retry_n=5 all FAILED, permanently unsolvable).
These items are moved OUT of the active retry pool. Do NOT re-retry.

- **p2_radical_028_人** — X-crossing (apex-kiss). All 4 retries (r1, r3, r4) failed.
  B5 retry_4 used kiss_apex(u_pie=0.0) with full checklist compliance. Apex still
  didn't read as a proper 人 in the panel judgment. Diagnosis: the callable-Python
  format can guarantee two strokes share a pixel, but the resulting silhouette
  doesn't match the calligraphic expectation of a "kiss" — the strokes touch
  without visually flowing into each other.

- **p2_radical_030_入** — X-crossing (head-on-shaft at u_pie=0.3). Same finding.

- **p2_radical_046_大** — X-crossing (crossing at heng midpoint). B5 retry_4
  abandoned kiss_apex in favor of inline PIL with retry_3 geometry + thin widths,
  because kiss_apex's abstraction places apex AT heng but drawer needed apex
  ABOVE heng. Still failed. The abstraction the helper exposes is not the
  abstraction the calligraphic form requires.

**Meta-diagnosis (see evolution.md 2026-07-24)**: 17/17 B5 retries followed
the RETRY-TIME CHECKLIST and imported helpers. Only 丷 passed, and it passed
by REJECTING its recommended helper. The B4→B5 retrieval fix worked; the
underlying helper hypothesis is falsified.

Items the human marked FAIL. Each has a self-diagnosis (from the PNG)
and a specific coord-format fix idea to try on retry. All three fails
from batch 1 are hook strokes — a real pattern.

## GRADUATED (batch-3 retry PASS)

- **p1_stroke_14_竖钩** — retry PASSED. Now bank primitive `shu_gou.py`.
- **p1_stroke_23_竖弯钩** — retry PASSED. Now bank primitive `shu_wan_gou.py`.

Removed from errata; see Success Bank entries #43, #44.

## GRADUATED (batch-4 retry PASS)

- **p2_radical_024_冂** — retry PASSED. Now bank primitive `jiong_radical.py`
  (bank #54). The inlined-three-segments recipe (fang_radical pattern)
  worked verbatim — this validates P11 for open-frame radicals.

Removed from errata.

## GRADUATED (B1 retry PASS)

- **p2_radical_014_厂 (chang)** — retry_1 PASSED. Now bank entry
  `chang.py` (bank #67). Retry recipe (widened heng + inlined nearly-
  vertical 丿) worked. Removed from errata.

## GRADUATED (B4 retry PASS) — 2026-07-23

- **p2_radical_082_子 (zǐ)** — retry_1 PASSED. Now bank entry
  `zi_char.py` (bank #122; the same file also serves the p3 char).
  Recipe = fully-inline recipe (3 hand-tuned tapered polylines): 横撇
  top, thicker-mid 弯钩 shaft with visible hook flick, thin ~5px
  crossing 一. **The drawer did NOT use kiss_apex or bezier_point** — it
  followed the errata fix idea verbatim ("inline whole 弯钩 fresh with
  matched taper"). This is a lesson: for compact 2–3 stroke radicals,
  well-diagnosed inline hand-tuning beats helper composition. Removed
  from errata; retry_n reset (item is mastered).

## GRADUATED (B5 retry PASS) — 2026-07-24

- **p2_radical_021_丷 (bā-top)** — retry_4 PASSED. Now bank entry
  `ba_dot.py` (bank #161). GRADUATED via ba_dot.py, bank #161. Recipe:
  asymmetric hand-render (LEFT tiny 点 + RIGHT short 撇), thin ~4px
  widths per P12. Explicitly rejected mirror_dian_pair — GT is not a
  mirror pair. Lesson: when the recommended helper contradicts GT
  observation, believe GT. Removed from active retry pool.

## p1_stroke_16_斜钩 (xie gou)

- Batch: 1
- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_16_斜钩/01_斜钩.png`
- Diagnosis (from vision):
  - The main body reads as a nearly-straight diagonal line from
    upper-left to lower-right, with only the faintest curve.
  - The "hook" is a small filled circular blob at the lower-right end
    with essentially no upward flick visible.
  - Real 斜钩 needs (a) a distinct rightward BULGE in the middle-lower
    of the body (belly curves outward toward lower-left of the chord —
    the arc is much more pronounced), and (b) a visible tapered flick
    UP (not up-left; classic 斜钩 hook rises nearly vertically or
    slightly leftward from the tail).
- Fix idea for retry:
  - Increase the cubic bezier's outward curvature: move p1 from
    `(140, 140)` toward `(105, 165)` (further from the chord) so the
    belly is unmistakable.
  - Redraw the hook as a proper tapered segment (width 10 -> 2 over
    ~35 px), heading up and slightly left from `p3`. Do NOT collapse it
    into a single ellipse.

## p1_stroke_19_横斜钩 (heng xie gou)

- Batch: 1
- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_19_横斜钩/01_横斜钩.png`
- Diagnosis (from vision):
  - The shape reads as a plain angled "V" or bent stick: short horizontal
    top-left segment meets a long thick diagonal going down-right, and
    then simply stops. No hook is visible at the bottom-right tip.
  - Missing: the characteristic upward flick (钩) at the end of the
    diagonal. Also missing: the smooth curve of the 斜 segment (the
    stroke should CURVE, not just angle sharply).
  - Uniform ink thickness throughout — no calligraphic taper anywhere.
- Fix idea for retry:
  - Draw three explicit segments in coord form:
    1. 横 as a short tapered line from `(-90, +55)` to `(-30, +60)`
       (thin -> slightly thicker).
    2. 斜 as a quadratic bezier from `(-30, +60)` through
       `(+20, +5)` to `(+70, -55)` with tapered width (11 -> 7).
    3. 钩 as a short tapered flick from `(+70, -55)` to `(+45, -25)`
       (width 8 -> 2). This flick UP is essential.
  - Don't render with turtle+PostScript: canvas resizing losslessly
    tends to blur the hook. Use direct PIL ImageDraw like the other
    passing strokes.

## Cross-fail pattern

All three fails are hook (钩) strokes. Shared failure mode: the hook
either was omitted, collapsed into a blob, or drawn as a
downward/wrong-direction spike. See `principle_bank.md` P1 for the
derived principle.

## p1_stroke_21_横折弯 (heng zhe wan) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_21_横折弯/01_横折弯.png`
- Diagnosis (vision): rendered as 横 + right-angle drop + tiny bottom-
  right corner blob. The 弯 (final sweeping curve to the right along
  the base) is essentially invisible — the quarter-arc I coded lands
  in a stubby ⌐-like L, and the "short horizontal tail" is only 5 px
  wide so it doesn't read as the horizontal sweep that defines this
  stroke.
- Fix idea (coord form):
  - Extend the final horizontal a LOT: `p_h_end = (140, -60)` not
    `(95, -60)`. The 弯 tail should be visually LONGER than the top
    横.
  - Make the arc bigger: `arc_r = 45 * scale` (was 30) so the curve
    is unmistakably an arc, not a rounded corner.
  - Widen the final segment relative to the vertical (11 → 13) so it
    reads as ink-heavy on the sweep.

## p1_stroke_25_横折弯钩 (heng zhe wan gou) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_25_横折弯钩/01_横折弯钩.png`
- Diagnosis (vision): reads as a top 横 + short vertical + a big
  bulging arc that swings LEFT along the bottom, but the arc's belly
  goes DOWN too far and the terminal hook flicks LEFT-and-UP instead
  of pointing up-and-inward. Envelope is roughly correct but the
  arc reads as a sagging bag rather than the crisp 弯 of 也/巴.
- Fix idea (coord form):
  - Flatten the arc: `p_arc_ctrl = (30 * scale, -55 * scale)` (was
    (55, -70) — pull the control point up and center-ward so the arc
    bottom rises).
  - Shorten the arc's leftward reach: `p_arc_end = (-30, -70)` (was
    (-55, -75)) — the tail should stop under the top 横's start, not
    extend past it.
  - Hook up-and-slightly-RIGHT from that endpoint: `hook_tip = (-15,
    -40)`. The classic 横折弯钩 hook points INWARD toward the enclosed
    area, not outward left.

## p1_stroke_26_横折折 (heng zhe zhe) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_26_横折折/01_横折折.png`
- Diagnosis (vision): rendered as a clean ⊐ shape (top horizontal +
  right vertical + bottom horizontal going left). Geometry is correct
  but the corner blobs are oversized ellipses that dominate the
  visual mass — the human likely read it as three disconnected line
  segments with three dots rather than one continuous stroke. Also
  the bottom horizontal ends flat rather than continuing the ink
  taper.
- Fix idea (coord form):
  - Shrink corner blobs: `r1 = r2 = 6 * scale` (was 8). Cap at ~ink/2
    so they visually merge with the line rather than punctuate it.
  - Use `_stroke_line` (stamped-circle taper) for all three segments
    instead of `_stroke_line` with heavy uniform width — the current
    code already does this but with too-wide (12) width. Drop to 10.
  - Kill the terminal blob at (-50, -40); let the bottom 横 taper to
    its natural end.

## p1_stroke_31_竖折折钩 (shu zhe zhe gou) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_31_竖折折钩/01_竖折折钩.png`
- Diagnosis (vision): rendered as vertical + horizontal + short
  vertical, with a triangular blob glued to the bottom of the second
  vertical. The hook reads as pointing DOWN-and-LEFT, not UP-and-LEFT
  (P1 violation). Second vertical also too short — the hook has no
  room to originate from the shaft, so it grew off the corner blob
  instead (P9 violation).
- Fix idea (coord form):
  - Lengthen the second vertical: `D = (60, -90)` not (60, -70) — add
    20 px so the hook can flick from its base.
  - Hook: `hook_base = (60, -88)` and `hook_tip = (30, -68)`. Both
    endpoints in math coords, +y up — hook_tip.y is HIGHER than
    hook_base.y so the direction is genuinely up-and-left.
  - Remove the corner-blob-at-D and let the tapered shaft itself
    form the hook root.

## p1_stroke_32_横折折折钩 (heng zhe zhe zhe gou) — batch 2

- Verdict: FAIL
- Attempt PNG: `attempts/p1_stroke_32_横折折折钩/01_横折折折钩.png`
- Diagnosis (vision): reads as a compact 3 or a broken乙-like scribble.
  I tried to draw the shape by 4 straight segments (short 横 + down-
  left diag + down-right belly + short drop + hook) but the second
  diagonal down-LEFT is wrong — the canonical 横折折折钩 (as in 乃, 及)
  runs 横 → down (short 竖) → sweeping-left 撇 curve → tiny 折 back
  right → up-left hook. My down-left-then-down-right zig-zag reads as
  a "Z" cursor, not the 乃 shape.
- Fix idea (coord form):
  - Redesign as 4 anchors + hook: `A(-70, 90)` 横 to `B(30, 95)`, then
    `B` down to `C(30, 30)` (short 竖), then quadratic bezier
    C→ctrl(0, -30)→D(-70, -70) as the sweeping 撇 (the belly of 乃),
    then `D` to `E(-30, -50)` as the terminal 钩 up-and-right.
  - Use a Bezier (not straight segments) for the belly — this is the
    only stroke in the batch that genuinely curves like a hairpin.
  - Match against 乃's right side visually before committing.

## p1_stroke_26_横折折 — STALE (retry_n=2)

Failed twice on retry (batch 3 and batch 4). Both errata fixes were
cosmetic tweaks (blob size, calligraphic slope) that clearly do not
address the underlying failure mode. If not solved by scan #4
(items #100+), freeze permanently per shared_rules.md terminal-freeze
rule. Do not spend a third retry attempt on cosmetic-only fixes.

---

# Batch-4 new fails (main curriculum, 11 items)

---

# Batch B1 new fails (main curriculum, 23 items) — 2026-07-18

Per-item fix ideas summarised in `sandbox.md` "B1 fail summaries"
section. All are primitive-reflex-vulnerable per TR8 (except 丷, 讠,
032_厶 which are inline-recipe fidelity issues).

## p2_radical_015_刀 (dao) — retry_1 FAIL (retry_n=1)

- Batch: B1 (retry)
- Verdict: FAIL (still — despite retry-1 fix of widened 横折钩 + inlined
  crossing 撇). Crossing geometry improved but hook still reads as
  slightly detached from the shaft.
- Fix idea for retry_2 (post-cooldown 50 items):
  - Draw the whole 刀 as ONE continuous polyline: wide 横 head → 折
    corner → 竖 → 钩 up-left, with a separate 撇 crossing at the
    horizontal's ~60% mark.
  - Verify hook shares last 5 px of shaft (P9).

## p2_radical_020_阝 (fu) — FAIL
## p2_radical_021_丷 (ba_top) — FAIL (G3-unique)
## p2_radical_024_冂 (jiong) — FAIL (second time — but bank now has jiong_radical.py from earlier retry; this indicates a re-derivation or scan-window fail rather than absence of recipe)
## p2_radical_025_力 (li) — FAIL
## p2_radical_028_人 (ren) — FAIL
## p2_radical_030_入 (ru) — FAIL
## p2_radical_032_厶 (si) — FAIL
## p2_radical_035_讠 (yan) — FAIL (G3-unique)
## p2_radical_036_廴 (yin) — FAIL
## p2_radical_038_㔾 (jie_variant) — FAIL
## p2_radical_040_屮 (che) — FAIL (G3-unique)
## p2_radical_041_彳 (chi) — FAIL
## p2_radical_042_巛 (chuan) — FAIL
## p2_radical_046_大 (da) — FAIL (G3-unique)
## p2_radical_047_飞 (fei) — FAIL
## p2_radical_050_弓 (gong_bow) — FAIL
## p2_radical_053_己 (ji_self) — FAIL
## p2_radical_055_彑 (ji_snout) — FAIL
## p2_radical_056_巾 (jin) — FAIL
## p2_radical_058_马 (ma) — FAIL
## p2_radical_059_门 (men) — FAIL
## p2_radical_061_女 (nu) — FAIL (G3-unique)
## p2_radical_062_犭 (quan) — FAIL

Fix strategies per item live in `sandbox.md` — most (18/23) call for
inline-fresh per TR8. Retry priority for next scan window: 大, 人, 入
(prerequisites for many upcoming characters); 门 (prerequisite for
问/间); 女 (prerequisite for 好/妈).

---

# Batch B2 retries (positions 101–150, retry_n=1 → 2) — ALL FAILED

The 8 items retried in B2 (人, 入, 大, 女, 犭, 己, 㔾, 丷) all failed
their retry_1 attempt. TR8 INLINE-FRESH TEST — the principle added at
end of B1 explicitly to save these items — did NOT rescue them.
Increment retry_n to 2 for each. See `sandbox.md` "Batch B2
diagnostic" for the root-cause hypothesis (rigid `(ox, oy, scale)`
signature can't vary angle/taper/curvature) and `evolution.md` for
the memory restructuring done in response.

- **p2_radical_021_丷 (bā_top)** — retry_1 FAIL, retry_n=2
- **p2_radical_028_人 (rén)** — retry_1 FAIL, retry_n=2
- **p2_radical_030_入 (rù)** — retry_1 FAIL, retry_n=2
- **p2_radical_038_㔾 (jié_variant)** — retry_1 FAIL, retry_n=2
- **p2_radical_046_大 (dà)** — retry_1 FAIL, retry_n=2
- **p2_radical_053_己 (jǐ)** — retry_1 FAIL, retry_n=2
- **p2_radical_061_女 (nǚ)** — retry_1 FAIL, retry_n=2
- **p2_radical_062_犭 (quǎn)** — retry_1 FAIL, retry_n=2

All 8 remain in errata with cooldown-50 before next retry eligible.

---

# Batch B2 new fails (main curriculum, 33 items) — 2026-07-18

Batch B2 pass rate = 17/50 = 34% — worst run yet (G1 no-memory: 38%).
Per-item diagnosis kept concise; the deep root cause is analysed in
`sandbox.md` §"Batch B2 diagnostic — signature restriction hypothesis".

Fix idea common across most: use the new adaptive `variant_pie /
variant_na / variant_dian` helpers in `_shared_helpers.py` (v7
addition) with hand-tuned angle / taper / curvature per composition,
instead of force-fitting frozen bank primitives. See `form_catalog.md`
for the stroke × context lookup that indexes when each variant applies.

## p2_radical_074_兀 (wù) — FAIL
Two legs (撇 + 竖弯钩) rendered with primitives; leg widths mismatched
and the 竖弯钩 base sweep too flat. Fix: inline both legs with matched
widths via `variant_pie` + inline bezier for curve+hook.

## p2_radical_077_忄 (heart-side) — FAIL
Mirrored dot pair; the mirrored right dot didn't match left dot's
weight. Fix: use `variant_dian` for BOTH dots with same w_head/w_tail,
swap head/tail positions for the mirror.

## p2_radical_078_幺 (yāo) — FAIL
Small compound with 撇折 + dian; angles wrong at the fold. Fix: inline
the whole compound as one continuous polyline with hand-picked corner.

## p2_radical_079_弋 (yì) — FAIL
斜钩 with cross dot; the 斜钩 lost its belly. `variant_na` with tuned
belly_u could work; or inline a bezier with strong perpendicular bow.

## p2_radical_080_尢 (yóu) — FAIL
横 + short pie + 竖弯钩 with leg forms different from 兀. Same as 074.

## p2_radical_081_夂 (zhǐ) — FAIL
Two crossing 撇/捺-like strokes; apex geometry lost. Fix: inline both,
sharing an apex pixel (like 父/木).

## p2_radical_082_子 (zǐ) — FAIL
横撇 primitive at scale + wan_gou primitive; the wan_gou hook came out
detached. Fix: inline whole 弯钩 fresh with matched taper.

## p2_radical_083_丬 (piece-left) — FAIL
Short upper 撇/点 misplaced; primitive dian too heavy. Fix:
`variant_dian` with w_tail ≈ 5 at compact position.

## p2_radical_084_夊 (suī) — FAIL
Same family as 夂; apex geometry lost.

## p2_radical_085_贝 (bèi) — FAIL
Box + two inner strokes; box aspect wrong (used kou at natural aspect
but 贝 is taller than wide, like 日). Fix: inline as tall rectangle
(reuse `ri.py` template), then add two inner strokes.

## p2_radical_086_比 (bǐ) — FAIL
Two 匕-like components; each 匕 needs specific 撇-into-shu junction that
primitives can't express. Inline both compounds.

## p2_radical_088_长 (zhǎng) — FAIL
5-stroke complex radical with distinctive 竖提 + long swept 捺. Force-fit
lost the long 捺 sweep. Fix: inline 捺 with `variant_na`, bow_perp≈+12.

## p2_radical_089_车 (chē) — FAIL
4-stroke cab shape; the small "cab" atop needs specific 撇折 that wasn't
in bank. Inline the cab as one continuous polyline.

## p2_radical_091_斗 (dǒu) — FAIL
2 dots + 横 + 竖. Dots misaligned with each other. Fix: `variant_dian`
for both with symmetric placement.

## p2_radical_093_方 (fāng) — FAIL
点 + 横 + 横折钩 + 撇. The 横折钩 corner was too sharp; 撇 slope wrong.
Fix: inline 横折钩 with rounded corner + `variant_pie` for 撇.

## p2_radical_094_风 (fēng) — FAIL
Distinctive curved envelope (横折弯钩) + inner strokes. Envelope
misshapen. Fix: inline envelope as one bezier polyline.

## p2_radical_096_戈 (gē) — FAIL
斜钩 dominant + 撇 + 点. 斜钩 lost its bow. Same as 弋.

## p2_radical_097_户 (hù) — FAIL
Similar to 尸 but with dian on top. Bank `shi_radical` template close.
Fix: prepend a dian at correct position on 尸 layout.

## p2_radical_098_火 (huǒ) — FAIL
2 side dots + central 人-shape (pie + na). Pie/na apex-kiss failed
same as 人/入 (which are in errata already). Fix: inline both with
shared apex pixel — validated in `fu.py` (父) recipe.

## p2_radical_099_旡 (jì_lack) — FAIL
Compact 4-stroke; proportions wrong.

## p2_radical_100_见 (jiàn) — FAIL
Box top + two bottom-descender strokes. Box shu/heng_zhe proportions
off, 撇 head not welded to box floor. Fix: inline the box (like ri.py
but square), then hand-place the two descenders welding to bottom.

## p2_radical_101_斤 (jīn) — FAIL
撇 + 撇 + 横 + 竖. Two 撇s at different angles.

## p2_radical_105_肀 (yù) — FAIL
Similar to 手 with 横 + shu + shu_gou. Alignment wrong.

## p2_radical_107_爿 (piece-full) — FAIL
Mirror of 丬 but taller. Same signature failure.

## p2_radical_108_片 (piàn) — FAIL
Similar to 爿 with box on right. Compound challenging.

## p2_radical_109_攴 (pū) — FAIL
Compound; 又-like bottom + 卜-like top. Layout wrong.

## p2_radical_110_攵 (variant of 攴) — FAIL
Similar to 攴.

## p2_radical_111_气 (qì) — FAIL
横撇 + inner 乙-like sweep. Complex curl.

## p2_radical_112_欠 (qiàn) — FAIL
Similar to 火 but with 横钩 across top. Force-fit 横钩 too wide
(primitive's x-span is fixed at 190px regardless of scale). Fix:
inline 横钩 with configurable span.

## p2_radical_113_犬 (quǎn) — FAIL
Literally 大 + dian. Since 大 is in errata and 犬 fails too, both need
the inline-crossing-X recipe (see fu.py 父 PASS as template).

## p2_radical_115_氏 (shì) — FAIL
4 inline strokes; 斜钩 arc wrong direction.

## p2_radical_117_手 (shǒu) — FAIL
Similar to 扌 (which is in bank) but with additional 撇 at top.
扌 (shou_pang) works, but the added top 撇 changes proportions.
Fix: start from shou_pang recipe, prepend a `variant_pie` at top.

## p2_radical_118_殳 (shū) — FAIL
Compound with 几-like top + 又-like bottom. Complex.

## Retry priority for next scan (positions 150+)

**Highest priority** (retrospective — new form_catalog/variant_helpers
directly address the failure mode):
- 犬 (113): use `fu.py` X-crossing template + dian
- 火 (098): same as 犬
- 手 (117): extend shou_pang with top pie

**High priority** (prospective — prerequisites for common Phase-3):
- 见 (100): needed for many 觉/规/视 compounds
- 车 (089): common radical
- 方 (093): common radical
- 长 (088): common radical

**Skip until further insight**: 幺 078, 弋 079, 旡 099, 攴 109,
攵 110, 气 111, 殳 118, 长 088-if-inline-fails — these have no
clear new lever.

---

# Batch B3 (2026-07-22, positions 151–200) new main-curriculum FAILs (21)

Common diagnostic thread: many are Phase-2 tail items (water/王/瓦-family)
that share the "many-parallel-hengs" or "distinctive-hook" pattern the
bank still can't reuse. Plus a few Phase-3 chars whose 撇/捺 crossing
proportions were off.

## p2_radical_119_水 (shuǐ) — FAIL
5-stroke water character with dominant 竖钩 shaft and 2 pies + na
crossings. Attempt's 撇/捺 heads didn't land on shaft. Fix: place both
side-strokes' heads at shaft's u=0.35 (mid-upper) exactly, using
variant_pie/na with computed weld pixel.

## p2_radical_120_瓦 (wǎ) — FAIL
4-stroke tile radical; distinctive top 横 + slanted 竖 + 竖折 hook
combo. No matching primitive; inline attempt got proportions wrong.

## p2_radical_121_尣 (wāng) — FAIL
Similar to 儿 but with a top horizontal cap. Fix: er_ren base + top heng.

## p2_radical_122_王 (wáng) — FAIL
3 hengs + 1 竖. Attempt used ~11 px thick uniform hengs — GT shows
lighter middle heng and heavy bottom. Fix: match tu.py pattern
(short-top / short-mid / long-bottom, decreasing thickness inside).

## p2_radical_123_韦 (wéi) — FAIL
Complex 4-stroke radical (looks like 4). No matching primitive; inline
recipe missed the distinctive 竖折 corner.

## p2_radical_125_毋 (wú) — FAIL
Complex 4-stroke with dominant 横折钩 + interior dots. Aspect wrong.

## p2_radical_127_牙 (yá) — FAIL
Fang shape with 撇 + 竖钩. Attempted pie + shu_gou, but crossing angle
off.

## p2_radical_132_支 (zhī) — FAIL
Cross-radical: top 十 + bottom 又. Composition of two mastered items
in principle; attempt didn't align them well.

## p2_radical_133_止 (zhǐ) — FAIL
Standing character; 4 strokes. Attempt hengs too thin, cross
proportions off. Fix: match GT — bottom heng widest+heaviest, top
short and slightly angled.

## p2_radical_134_爪 (zhǎo) — FAIL
Similar to 爫 (which PASSED as zhao_top.py) but a standalone
character with a longer bottom 竖. Fix: reuse zhao_top + append 竖.

## p2_radical_135_无 (wú) — FAIL
Distinctive top-heng + 撇 + 竖弯钩. No primitive fit.

## p3_char_0007_乛 (yi_variant) — FAIL
Single stroke 横钩. Bank has heng_gou_radical (PASSED as radical);
attempt didn't reuse cleanly. Fix: use heng_gou_radical at (0,0,1.0).

## p3_char_0011_人 (rén) — FAIL
Classic 人 (pie + na kissing at apex). Same failure mode as B1's
p2_radical_028_人 — heads didn't converge. Even with variant_pie/na
available. Fix: use variant_pie for 撇 and variant_na for 捺 with
EXPLICIT shared apex pixel (compute apex first, then head of both
strokes = that pixel).

## p3_char_0012_丷 (bā_top) — FAIL
Mirror-pair dots. Same as B1 fail p2_radical_021_丷. Persistent
failure — variant_dian helpers exist but the mirror is subtle.

## p3_char_0016_乃 (nǎi) — FAIL
Complex 2-stroke with 横折折折钩 + 撇. This stroke family is one of
the hardest (see errata: p1_stroke_32_横折折折钩 STALE at retry_n=2).
Skip until further insight.

## p3_char_0018_乜 (miē) — FAIL
2-stroke: 横折 + 竖弯钩. Attempt didn't join the two cleanly.

## p3_char_0023_九 (jiǔ) — FAIL
2-stroke: 撇 + 横折弯钩. The 弯钩 is one of the hardest stroke
families (errata: p1_stroke_25_横折弯钩 FAIL). Skip.

## p3_char_0025_力 (lì) — FAIL
Same failure mode as B1 p2_radical_025_力 (both retries). See errata.

## p3_char_0026_冂 (jiōng) — FAIL
Enclosing frame. Bank has jiong_radical (PASSED in B1 retry). Should
have reused it. Fix: use jiong_radical at (0,0,1.05).

## p3_char_0029_入 (rù) — FAIL
Same failure mode as B1 p2_radical_030_入. See errata.

## p3_char_0033_刀 (dāo) — FAIL
Same failure mode as B1 p2_radical_015_刀 (both retries). Persistent.

---

# Batch B3 (2026-07-22) retry increments (13, all remained FAIL)

- **p2_radical_015_刀** → retry_n=3 (fail mode SAME as retry_1/2:
  heng_zhe_gou + pie disconnection)
- **p2_radical_021_丷** → retry_n=4 (variant_dian used but mirror
  didn't read; fail mode SHIFTED slightly — now dots are wrong direction,
  not disconnected)
- **p2_radical_025_力** → retry_n=2 (variant_pie used for 撇 but corners
  still disconnected from heng_zhe_gou — fail mode SAME)
- **p2_radical_028_人** → retry_n=4 (heads still don't kiss at apex —
  fail mode SAME across all retries)
- **p2_radical_030_入** → retry_n=4 (same as 人)
- **p2_radical_046_大** → retry_n=4 (heng + crossing pie+na still don't
  converge on heng midpoint — fail mode SAME)
- **p2_radical_077_忄** → retry_n=2 (variant_dian used for BOTH dots as
  the fix idea suggested; still failed because the dots' angles are
  subtly wrong and shaft dominates — fail mode SHIFTED: was
  "wrong-weight" now is "wrong-angle+off-position")
- **p2_radical_083_丬** → retry_n=2 (variant_dian used with w_tail=5;
  compact form still off — the two dots+提 don't visually merge into
  the 丬 shape. Fail mode SHIFTED to "distance-from-shaft-too-large".)
- **p2_radical_088_长** → retry_n=2 (variant_na used; 捺 sweep is now
  present but the top-heng and 撇 don't compose into 长. Fail mode
  SHIFTED: 捺 fixed but composition still wrong.)
- **p2_radical_098_火** → retry_n=2 (no variant helpers used; drawer
  went inline-fresh. Fail mode SAME.)
- **p2_radical_100_见** → retry_n=2 (variant_pie used; box aspect still
  wrong. Fail mode SHIFTED slightly — box is tall now but interior
  proportions off.)
- **p2_radical_113_犬** → retry_n=2 (variant_pie + variant_na used for
  the 大 body + dian; body is now reasonable but dian too far off. Fail
  mode SHIFTED: pie/na fixed, dian position wrong.)
- **p2_radical_117_手** → retry_n=2 (no variants used; inline. Fail
  mode SAME.)

**Meta-pattern**: 7 of 13 retries USED the variant helpers (see the
b3 helper-usage grep in evolution.md). Of those 7, fail mode SHIFTED
in 5 cases — the specific stroke targeted by the helper improved,
but a DIFFERENT part of the character now fails. The helpers work in
isolation; they don't help with composition/joint geometry. That's
the next lever.

## Retry priority for scan #4 (positions 200+)

Deprioritise all 13 above unless the second-pass evolution (see
evolution.md 2026-07-22) provides a specific new lever. Retry-cap of
retry_n≥4 for 大, 人, 入, 丷 — these are approaching the terminal-freeze
line under shared_rules.md.

---

# Batch B4 (2026-07-23) retry increments (7 remained FAIL, 1 GRADUATED)

**Zero helper adoption**: `grep -l "kiss_apex|pie_point|mirror_dian_pair"
attempts/*__retry_*/generated.py` returns nothing for B4. Even 夂/夊/兀
whose B3 pending-reasons explicitly called for kiss_apex went inline
with hand-rolled `_tb` helpers.

- **p2_radical_082_子** → GRADUATED (see above). retry_n reset.
- **p2_radical_047_飞** → retry_n=2. Envelope still too "乙-like"
  (bowl-shaped) vs GT's OPEN right side. Interior 撇/点 rendered too
  small. Fail mode SAME. (No dedicated helper; recipe still hand-rolled.)
- **p2_radical_059_门** → retry_n=2. Fixed hook direction on
  横折钩; but 竖 left leg and dot render as three disconnected
  primitives with no shared visual style. Fail mode SHIFTED slightly
  (hook right; composition still off). *Note*: p3_char_0063_门 PASSed
  as a char with a different recipe (inline dian + inline 竖 + inline
  横折钩 all in one function). Consider back-porting men_char.py to
  the radical retry.
- **p2_radical_061_女** → retry_n=3. **APPROACHES terminal-freeze**
  (retry_n=3 is the cap). Still fails: 撇点 V is thinner than GT and
  long 撇 crosses at wrong point vs GT. Fail mode SHIFTED (was
  disconnected legs, now legs correct but crossing point wrong). One
  more chance under shared_rules terminal-freeze rule.
- **p2_radical_074_兀** → retry_n=2. Used variant_pie + tapered_line
  for legs (matched widths) — the widths ARE matched now but overall
  ink weight is calligraphic ~10px while GT is MMH thin ~4px. **P12
  violation** (didn't check GT weight profile before choosing brush).
  Fail mode SHIFTED (widths matched but wrong weight). *Note*: 兀 as
  a char PASSed with lighter recipe — back-port wu_char.py widths.
- **p2_radical_080_尢** → retry_n=2. Same family as 兀; ink too heavy
  (P12 violation), pie tail bow too shallow. Fail mode SHIFTED.
- **p2_radical_081_夂** → retry_n=2. Retry rationale said "use
  kiss_apex" but drawer used inline `_tb` and got apex geometry right
  visually — but the top pie is disconnected from the X body (looks
  like 攵 not 夂). Fail mode SHIFTED (apex OK; top pie position wrong).
- **p2_radical_084_夊** → retry_n=2. Similar to 夂; body geometry
  approximately correct but the 3-stroke composition doesn't cohere
  as 夊. Fail mode SHIFTED. Same as 夂: kiss_apex not used despite
  being the specific recipe.

## Retry priority for scan #5 (positions 250+)

**Terminal-freeze candidates** (retry_n ≥ 3 after B4):
- 女 (retry_n=3). One more chance; if fails, freeze.
- 大, 人, 入, 丷, 忄, 己, 㔾, 犭 (retry_n=4 from B3). ALREADY OVER
  the retry cap. Should be terminal-frozen unless explicit new lever
  emerges. Per shared_rules.md, do NOT retry these in B5.

**Prioritise instead**:
- Radicals whose char version already PASSed (兀, 门, 子): back-port
  the char recipe. Highest-confidence rescue.
- Items whose fail-mode SHIFTED in B4: they are close. 飞, 尢, 夂, 夊
  candidates for B5 if new lever appears.

---

# Batch B4 new main FAILs (23 items) — 2026-07-23

Common threads: (a) X-crossing family stays hard (大 char, 亾 char);
(b) hook family stays hard (匕, 丸, 也, 及, 飞, 已); (c) MMH thin-line
GTs mis-rendered with calligraphic brush (P12 violations recur).

## p3_char_0038_匕 (bǐ) — FAIL
Same failure mode as p2_radical_011_匕 (which is in errata, retry_3).
Bank shu_wan_gou + variant_pie: 撇 crossed above shaft not through
junction. Fix: 撇 must terminate exactly on the shaft, not float above.

## p3_char_0041_大 (dà) — FAIL
Used kiss_apex at u_pie=0.5 (X-crossing recipe). Legs kiss at apex,
but the shared apex sits ABOVE the heng crossbar instead of ON it.
GT shows the 撇/捺 heads meet AT the heng midpoint. Fix: compute
heng-midpoint pixel first, then set pie_head = that pixel.

## p3_char_0042_丬 (bàn) — FAIL
Similar to p2_radical_083_丬 (in errata). Compact form still off.

## p3_char_0043_个 (gè) — FAIL
X-crossing character (人-roof + 竖). Used kiss_apex. Roof reads OK
but bottom 竖 didn't weld to apex; visible gap.

## p3_char_0044_丸 (wán) — FAIL
Body 横斜钩 came out as continuous "乙" curve, but too enclosed
(reads as 乙, not 丸). Fix: open the top-right of the envelope.

## p3_char_0047_也 (yě) — FAIL
3-stroke with distinctive 竖弯钩 envelope. Used shu_wan_gou + inline
横折钩 + 竖 — the middle 竖 sits inside the envelope but shu_wan_gou
was too small. Bank primitive aspect mismatch (same class as p2 见).
Fix: inline the full envelope larger.

## p3_char_0048_乇 (tuō) — FAIL
Similar to 千 but with 竖钩 base. Composition of pie + heng + shu_gou
didn't cohere; hook direction wrong.

## p3_char_0056_亾 (variant of 亡) — FAIL
Composition of shu + pie + na + heng — the pie+na 人-like piece
tucked to the right didn't align with the outer shu/heng frame.

## p3_char_0059_么 (me) — FAIL
Small compound 撇 + 撇折 + 点. Similar family to 幺 (in errata).

## p3_char_0060_卂 (xùn) — FAIL
Rare 3-stroke with 横折折 body + interior. Bank has no matching form.

## p3_char_0061_与 (yǔ) — FAIL
3-stroke with distinctive 横 + 竖折折钩 body + bottom 横. The
中間 stroke is one of the hardest (see errata: p1_stroke_31_竖折折钩
STALE).

## p3_char_0065_及 (jí) — FAIL
Used kiss_apex helper. Top 横折折撇 too small + main 撇 too straight
+ 捺 tail too short (drawer's own self-diagnosis in header). Fix
attempted but proportions still off after revision.

## p3_char_0068_纟 (sī) — FAIL
Identity alias of si_zi_pang initially collapsed the two upper hooks;
revised to inline with more vertical spacing but hooks still merge.

## p3_char_0070_夂 (zhǐ) as char — FAIL
Same failure mode as radical 夂. Used kiss_apex. Body OK; top pie
position wrong.

## p3_char_0072_夊 (suī) as char — FAIL
Same as 夂 char.

## p3_char_0073_飞 (fēi) — FAIL
Envelope 横斜钩 rendered inline; too flat top, hook underdeveloped,
interior 撇/点 too small. Same family as radical 飞.

## p3_char_0075_千 (qiān) — FAIL
Bank composition (heng + shu + pie) with proportions similar to 干.
The 撇 top curl was too subtle; reads more like 干. Fix: emphasise the
short 撇 curl at top (bow_perp more negative).

## p3_char_0076_孓 (jué) — FAIL
Similar family to 孑 (which PASSed as jie_char.py) and 子 (mastered).
Attempt used similar recipe but 孓 has NO middle 提 — instead an
inverted 提 (rising left, not right). Fix: mirror the direction.

## p3_char_0077_习 (xí) — FAIL
2-stroke: 横折钩 + 冫-like. Hook direction and dots misaligned.

## p3_char_0079_已 (yǐ) — FAIL
Similar to 己 (which is in errata retry_n=4, terminal-freeze).
Distinctive terminal hook curl. Force-fit didn't preserve the curl.

## p3_char_0081_女 (nǚ) — FAIL
Same failure family as radical 女 (retry_n=3). Char version rendered
similarly; distinctive 撇点 V shape lost.

## p3_char_0082_尢 (yóu) — FAIL
Same family as radical 尢 (retry_n=2). Char version rendered similar
composition problem.

## p3_char_0083_才 (cái) — FAIL
Bank composition (heng + shu_gou + pie). The 撇 originates from the
wrong point on the heng/shaft junction. Fix: pie head at (heng ∩ shaft)
pixel exactly.

## Fix-idea reuse table (B4 → B5)

| item | rescue lever | source |
|------|-------------|--------|
| 匕 char | terminate pie ON shaft (compute weld pixel) | pie_point helper |
| 大 char | apex at heng-midpoint pixel FIRST, then kiss_apex | needs new heng_midpoint helper OR explicit comment |
| 亾, 千, 才 | inline whole char at target GT proportions; bank composition wrong | inline-fresh |
| 也 | inline envelope larger; bank shu_wan_gou aspect wrong | inline |
| 兀 (radical), 门 (radical), 子 done | back-port CHAR recipe to radical | success cross-transfer |
| 夂, 夊 chars | top pie must not float above X body — welded position | pie_point |
| 飞 char, 丸 | envelope open on right (not enclosed 乙) | recipe rewrite |
| 女 char | see radical retry_3 rationale | shared |
| 孓 | mirror 孑 recipe | jie_char.py mirror |

---

# Batch B5 (2026-07-24) retry increments (13 remained FAIL, 1 GRADUATED, 3 TERMINAL FREEZE)

**Full helper adoption**: 17/17 retries wrote the RETRY-TIME CHECKLIST
(Q1/Q2/Q3) and imported at least one helper from `_shared_helpers.py`
(mean 6.5 helper calls each). B4→B5 retrieval fix confirmed working.
But only 丷 PASSed — and it passed by explicitly REJECTING its
recommended helper. Falsification of the helper-composition hypothesis;
see sandbox.md "B5 diagnostic" and evolution.md 2026-07-24.

- **p2_radical_021_丷** → GRADUATED (bank ba_dot.py, see top section). retry_n reset.
- **p2_radical_028_人** → TERMINAL_FREEZE (retry_n=5, see top section).
- **p2_radical_030_入** → TERMINAL_FREEZE (retry_n=5, see top section).
- **p2_radical_046_大** → TERMINAL_FREEZE (retry_n=5, see top section).

### B5 retry_3 update — p2_radical_015_刀
Used continuous-polyline recipe (P9-inspired) with pie_point for the
crossing 撇. Hook geometry now correct AND weld correct. Panel still
failed — kou-corner + hook composition doesn't cohere as 刀. Fail mode
SHIFTED (recipe closer, still no PASS). Composition ceiling.

### B5 retry_1 update — p2_radical_040_屮
First retry (retry_n=0 → 1). Used chu_radical_char.py's recipe pattern
(the p3 char PASSed) as back-port target. Recipe applied — but panel
still failed on radical GT. Fail mode: back-port did not carry over.
Consider: the radical GT is subtly different from the char GT (aspect
or ink weight).

### B5 retry_1 update — p2_radical_042_巛
First retry (retry_n=0 → 1). Used chuan_char.py-style thin uniform
lines. Panel still failed — the 3-stroke curved verticals of 巛 have a
distinctive scoop that the chuan (川) recipe lacks. Composition
mismatch: 巛 ≠ 川.

### B5 retry_2 update — p2_radical_058_马
Used bezier-composition helpers per checklist. The curly bottom loop
of 马 still misrenders — the shape is too continuous-cursive for
callable-Python discrete strokes. Fail mode: same as retry_1. Format
ceiling for cursive-body characters.

### B5 retry_2 update — p2_radical_077_忄
Used variant_dian for both mirror dots + tapered shu. Dot weights
match, spacing correct — but the whole radical reads as too airy vs
GT's tighter cluster. Fail mode SHIFTED (weights OK, cluster spread
wrong). One more retry possible before terminal-freeze.

### B5 retry_1 update — p2_radical_079_弋
First retry (retry_n=0 → 1). Used the yi_ge.py (p3 char PASSed)
recipe as back-port. Recipe applied but radical GT is more compact
and the 斜钩 belly reads differently. Fail mode: back-port aspect
mismatch. Same lesson as 040_屮.

### B5 retry_2 update — p2_radical_083_丬
Used mirror_dian_pair with compact spread≈15 + shaft per the pending
rationale. Dot weights and shaft OK — panel failed on stroke ORDER /
proportion cue. Fail mode SHIFTED.

### B5 retry_2 update — p2_radical_088_长
Used variant_na with bow_perp≈+12 for the long 捺. Sweep now bows —
but the 竖提 head geometry still lost. Fail mode SHIFTED (捺 OK, 竖提
still weak). Composition of the 5-stroke complex remains beyond
helper reach.

### B5 retry_2 update — p2_radical_093_方
Inlined 横折钩 with rounded corner + variant_pie for 撇 per B2
diagnosis. Corner rounder now — but 点+横 top cluster still misaligned.
Fail mode SHIFTED. Consider terminal-freeze at retry_n=3.

### B5 retry_2 update — p2_radical_098_火
Used kiss_apex for the interior 人 + variant_dian for the two flanking
dots. Apex touches — but dots sit too far from the 人 legs vs GT.
Same X-crossing family concerns as terminal-frozen items.

### B5 retry_2 update — p2_radical_100_见
kou + 人 composition. Used kiss_apex(u_pie=0.0) for interior 人 +
inlined kou frame. 人 apex present but shu_wan_gou tail of the 儿
component (final stroke) reads as detached from the box. Fail mode
SHIFTED. Watch: 见 shares family with terminal-frozen 人/入/大 —
candidate for terminal-freeze at retry_n=5.

### B5 retry_1 update — p2_radical_111_气
First retry (retry_n=0 → 1). Used tapered_bezier for the continuous
top 横撇 + inner 乙-sweep. Envelope shape reads plausibly — but the
final internal 乙 stroke's rightward hook direction still reads wrong
(too closed). Fail mode SHIFTED slightly.

### B5 retry_1 update — p2_radical_135_无
First retry (retry_n=0 → 1). Used variant_pie + kiss_apex for the
crossing at the top. Apex touches — bottom 儿-legs from er_ren base
too thick vs GT. P12 violation persists. Fail mode SHIFTED.

---

# Batch B5 new main FAILs (31 items) — 2026-07-24

Batch B5 pass rate = 19/50 = 38% — worst yet (G1 no-memory: ~53%).
Cumulative 49.6% (first sub-50% batch). Family clusters:
- **X-crossing family**: 义, 天 (2 fails — adjacent to terminal-frozen 人/入/大).
- **亻-radical right-side variation**: 仂, 仄, 仇, 仑, 仓 (5 fails — 亻+X compose,
  but the right component recipe drifts per-character).
- **Envelope/冂 frame + interior**: 内, 內, 冗, 冘, 円, 冈 char class
  variants (5 fails — 冂 frame OK-ish, interior always off).
- **Compact cursive radicals**: 马, 巛, 幺, 乡, 为, 乌, 予, 长 (8 fails —
  no stable inline recipe).
- **Other**: 义 (X), 天 (X), 亢 (亠+乙), 方 (top+bottom), 分 (八+刀), 公
  (八+厶), 从 (2 apex-kissing 人), 见 (kou+人), 五 (unique), 兮 (八+丂),
  切 (七+刂), 五 (X-body), 龶 char PASSed but 五/龶 near.

## p3_char_0085_马 (mǎ) — FAIL
Cursive body with curly bottom loop. Callable-Python discrete strokes
can't capture the continuous cursive flow. Fix idea: inline whole
character as ONE long bezier polyline — but may hit format ceiling
(same class as 马 radical which is stuck at retry_n=2 with no PASS).

## p3_char_0086_巛 (chuān variant) — FAIL
Same as 巛 radical retry (see above). Distinctive scoop of 3 curved
verticals. Fix: inline scoop bezier per column — but back-port of
chuan (川) recipe failed. Composition mismatch.

## p3_char_0089_义 (yì) — FAIL
X-crossing family. 点 (top) + 撇 + 捺 crossing. Same failure mode as
terminal-frozen 人/入/大. Fix idea: kiss_apex — but empirically kiss_apex
doesn't rescue this family. Likely format ceiling.

## p3_char_0090_幺 (yāo) — FAIL
Compact 3-stroke cursive (撇折 + dian). Same failure mode as 幺 radical
(078). Fix: inline whole compound as one continuous polyline with
hand-picked corners; may still hit ceiling.

## p3_char_0091_乡 (xiāng) — FAIL
Similar to 幺 but with an additional 撇 tail. Same cursive-format
ceiling.

## p3_char_0096_为 (wéi) — FAIL
Complex cursive with 点 + curved envelope + interior. No stable recipe
in bank. Fix idea: inline whole envelope as bezier — but shape is
distinctive enough that back-port from other characters won't help.

## p3_char_0097_乌 (wū) — FAIL
Similar envelope-with-interior structure to 为. Same format-ceiling
concerns.

## p3_char_0099_予 (yǔ) — FAIL
Compact folded shape (横撇 + 横折 + 竖钩-like). Composition of 3-4
folded segments hard to align. Fix: inline all folds as one continuous
polyline; hook shares last 5 px of shaft (P9).

## p3_char_0102_天 (tiān) — FAIL
X-crossing family (2 hengs + 撇 + 捺). Adjacent to terminal-frozen 大.
Fix: kiss_apex at u_pie=0.24 on lower heng (太 recipe worked); may not
transfer since 天 has 2 hengs and different aspect. Likely format ceiling.

## p3_char_0103_亢 (kàng) — FAIL
亠 + 几. Top-cap composition OK-ish; 几 shu_wan_gou tail geometry off.
Fix: back-port ji.py recipe with tighter tail.

## p3_char_0104_方 (fāng) — FAIL
Same as 方 radical (093, retry_2 also failed). 点+横+横折钩+撇.
Composition mismatch persists across radical and char.

## p3_char_0105_仂 (lè) — FAIL
亻 + 力. 亻 identity alias OK; 力 (横折钩+撇) misrenders — 力 has no
bank entry. Fix: build 力 inline first, then compose.

## p3_char_0108_无 (wú) — FAIL
Same as 无 radical (135, retry_1 also failed). 横+X-crossing+hook.
Family: X-crossing. Format ceiling.

## p3_char_0109_仄 (zè) — FAIL
厂 envelope + interior 人. Envelope OK; interior 人 has the same
X-crossing weakness. Composite fail.

## p3_char_0110_分 (fēn) — FAIL
八 (top) + 刀 (bottom). 八 OK from bank; 刀 (which is stuck at
retry_n=3, no PASS) drags the composite down.

## p3_char_0111_仇 (chóu) — FAIL
亻 + 九. 亻 OK; 九 (short 撇 + hook) needs precise 撇/hook weld. Same
composition-ceiling as other 亻 chars.

## p3_char_0114_见 (jiàn) — FAIL
kou + 儿 (人-like bottom). kou OK; 儿 shu_wan_gou detaches from kou
frame. Adjacent to terminal-frozen X-crossing family. Watch for
terminal-freeze at retry_n=5.

## p3_char_0116_公 (gōng) — FAIL
八 (top) + 厶. 八 OK; 厶 has no bank entry and its distinctive 撇折 +
dian composition mis-renders. Fix: inline 厶 fresh.

## p3_char_0117_仑 (lún) — FAIL
人 (top) + 匕 (bottom). Top 人 X-crossing family; bottom 匕 hook
composition. Both weak individually; composite fails.

## p3_char_0118_从 (cóng) — FAIL
Two 人 side-by-side. Both need X-crossing kiss_apex; format ceiling
recurs twice. Fix: back-port 仌 (bing_ren.py) which PASSed by using
kiss_apex(u_pie=0.0) for stacked 人 — but 从's 人 are side-by-side
and may need a different lever.

## p3_char_0119_仓 (cāng) — FAIL
人 (top) + 巳 (bottom). Top 人 X-crossing; 巳 available from bank but
composition misaligned.

## p3_char_0120_气 (qì) — FAIL
Same as 气 radical (111, retry_1 also failed). Envelope with internal
sweep. Fix idea: bezier envelope; format ceiling on curved envelopes.

## p3_char_0121_內 (nèi) — FAIL
冂 frame + 入 (interior). 冂 OK; interior 入 is X-crossing family
(terminal-frozen). Composite fails at interior.

## p3_char_0122_五 (wǔ) — FAIL
5-stroke box-and-cross. Frame + interior 乂 composition; the interior
乂 uses variant_pie + variant_na but proportions to the frame are off.
Fix: reuse 冈 (gang.py) 乂-inside-frame pattern with tuned proportions.

## p3_char_0123_兮 (xī) — FAIL
八 (top) + 丂 (bottom). 八 OK; 丂 has no bank entry — needs 横+竖折钩
composition inline.

## p3_char_0125_円 (jiān variant) — FAIL
Frame + interior. Same class as 内/內/冋. Composition mismatch.

## p3_char_0126_长 (cháng) — FAIL
Same as 长 radical (088, retry_2 also failed). 竖提 + long 捺 + cross
strokes. Complex 5-stroke composition. Format ceiling.

## p3_char_0130_切 (qiē) — FAIL
七 + 刂. 七 from bank OK; 刂 identity alias OK. Composition alignment
off — the 刂 sits too low vs 七. Fix: raise 刂 by ~15 px.

## p3_char_0131_冗 (rǒng) — FAIL
冖 + 几. 冖 identity alias OK; 几 mostly OK from bank. Composition
alignment issue — 几 too small under 冖 cap. Fix: bump 几 scale.

## p3_char_0132_内 (nèi) — FAIL
Same as p3_char_0121_內 (traditional variant). Same X-crossing
interior. Composite fails at interior.

## p3_char_0133_冘 (yóu) — FAIL
冖 + 儿 with an extra 撇. Composition of cap + legs + extra stroke
misaligns. Fix: inline 儿 with the extra 撇 as one function.

## Fix-idea reuse table (B5 → B6)

| item family | rescue lever | notes |
|-------------|-------------|-------|
| 亻 + variable right | build the right component inline first, THEN compose | 亻 identity works; right component is the bottleneck |
| 冂 frame + interior 乂 | reuse gang.py PIL-pixel frame + 乂 pattern | 冈 PASSed; 内/内/内/内 may transfer |
| X-crossing family (义/天/从) | **likely format ceiling — G3 callable-Python can't render "kiss"** | prefer inline PIL like tai_char (which PASSed) but expect low yield |
| Cursive body (马/巛/幺/乡/为/乌) | one long bezier polyline | format ceiling suspected |
| Missing atomic radicals (力/厶/丂) | build inline first before composing | prerequisite gap |
| Recommended helper contradicts GT | **PREFER GT observation** (ba_dot lesson) | new B5 principle |

---

# Batch B6 (2026-07-26, positions 301–350) new main FAILs — 27 items

Batch B6 pass rate = 23/50 = **46%** — recovery from B5's 38% but still
under G1 no-memory control. Cumulative through 350 items: ~49%.
No retries were run (killed at B5 curator). Fail-family clusters:

- **亻 + variable right (5)**: 化 (亻+匕), 他 (亻+也), 仔 (亻+子), 仕
  (亻+士), 仗 (亻+丈), 仞 (亻+刃), 付 PASSed as one of the 6. The 亻
  identity aliases cleanly on the left; failure is always in the right
  component — the right is a compound not in bank (匕, 也, 士 without
  bank primitives, or bank primitives at wrong composition scale).
- **Small-box + protruding + interior (5)**: 甴, 生, 平, 主, 正 — box
  + heng + shu combinations where relative heights of hengs / shu
  extension were off. The interior middle heng often merged with box
  frame or drifted vertically.
- **Envelope + interior (2)**: 反 (厂+又), 疒 (broken frame + dots).
- **Cursive/complex hook (5)**: 书, 引, 必, 发, 乎 — all involve
  distinctive hook curls or 竖弯钩-like elements that the callable-Python
  format keeps missing.
- **Multi-component composition (5)**: 水 (中心shaft+4 side strokes),
  刅 (scale collapse — rendered ~30% target size), 队 (β + 人),
  升 (千-like base + 卅 cross), 出 (2 stacked 山).
- **Rare/hard (5)**: 丱 (paired hooks), 乍 (乍-hook), 去 (土+厶
  losing 厶), 疋 (足-like), 仞 (亻+刃).

## p3_char_0134_化 (huà) — FAIL
Left 亻 shows a short pie floating with no shu; the right 匕 rendered as
a disconnected 竖弯钩 with the pie head sitting well below the top of
the 竖弯钩 — the 匕 doesn't cohere. The 亻 pie also floats disconnected
from any shu. Fix idea: use `ren_pang` at scale ~0.6 for 亻 (proven
identity), then inline 匕 as 撇 landing ON the 竖弯钩 shaft top per
sandbox bootstrap 匕 fix.

## p3_char_0135_刅 (chuāng) — FAIL
Entire character rendered at ~30% of canvas — collapsed into upper-right
quadrant. Looks like a tiny 尔. Scale error. Fix idea: use canvas-fill
scale ~1.0 for 3-4 stroke chars; do not shrink into a corner.

## p3_char_0138_水 (shuǐ) — FAIL
Central 竖钩 shaft present but strokes 2-4 (short 撇 top-left, 撇 mid-left,
捺 mid-right) don't converge on the shaft; heads float in open space and
right 捺 tail sits at wrong angle. Fix idea: compute shaft ∩ u=0.30 pixel
first, then place each side-stroke's tail AT that pixel (weld) rather
than approximating.

## p3_char_0140_反 (fǎn) — FAIL
Top 厂 shape correct-ish but the 又 below rendered as a large flat X with
tails extending past the 厂 envelope; the 又 should be a compact
横撇+捺 with apex touching the underside of 厂. Fix idea: compose as
`chang` (厂) + shrunk `you` (又) with 又's apex placed under 厂's midpoint
by ~15 px.

## p3_char_0146_队 (duì) — FAIL
Left β (阝) shape approximately readable; right 人 rendered too small and
apex sits well below the β's midpoint. The two components look
disconnected. Fix idea: enlarge 人 (kiss_apex u_pie=0.0) to at least
match β's height and align 人's apex with β's midpoint.

## p3_char_0148_书 (shū) — FAIL
Rendered as boxy 千-like frame + fragmentary hook. The distinctive
竖折折钩 shaft with cross-heng is missing. This is a hook-family fail
adjacent to `p1_stroke_31_竖折折钩` which is STALE at retry_n=2.
Format ceiling likely.

## p3_char_0149_升 (shēng) — FAIL
Rendered as 千-like + X-cross. 升's characteristic top-撇 + heng + 竖
+ tick pattern lost. The right vertical dominates and the top pie
overshoots. Fix idea: shorten right 竖 to match left 撇 length; place
crossbar at ~35% from top.

## p3_char_0150_引 (yǐn) — FAIL
Left 弓 rendered as a zigzag Z with broken corners (no continuous
sweep). Right 竖 present but too far right and disconnected. 弓 is a
hard 3-stroke shape (see errata: p2_radical_050_弓 FAIL). Format
ceiling for double-curl shapes.

## p3_char_0154_他 (tā) — FAIL
Left 亻 approximately correct; right 也 rendered with disconnected
横+竖弯钩+竖 (three floating segments). 也's envelope must be one
continuous 竖弯钩 with an inserted heng and shu. Fix idea: inline whole
也 as one bezier-envelope + interior strokes; do NOT compose three
separate primitives.

## p3_char_0155_必 (bì) — FAIL
All 5 strokes present but scattered — the central 心-body arc is thin
and the three surrounding dots + pie float without visible
composition anchor. Fix idea: compute the arc's u=0.5 pixel first,
then place the two side dots at ±20 px from it; the crossing 撇 must
originate from ABOVE the arc's apex.

## p3_char_0158_出 (chū) — FAIL
Rendered as two stacked outline boxes, no central 竖 hook. 出 requires
central vertical of upper 山 to be TALL and DOMINANT (extending well
above), with lower 山 wider. Fix idea: draw upper 山's central 竖
extending to y=+120, lower 山 as separate wider frame with own tick
pattern.

## p3_char_0161_甴 (yóu variant) — FAIL
Box + shu-protrusion approximately readable but the interior middle
heng missing/collapsed. Fix idea: like 申 recipe but with only one
interior heng (not two like 田).

## p3_char_0162_生 (shēng) — FAIL
Middle heng and bottom heng both too heavy/wide; top 撇 too short and
sits above 生's natural cap. The horizontal cluster reads as "土
above ‖" not 生. Fix idea: match `sheng`-family GT — top pie starts
higher, three hengs decreasing widths downward.

## p3_char_0163_丱 (guàn) — FAIL
Rendered as three verticals with tiny pies. 丱's paired-hook pattern
(two 竖弯 stemming from a central bulge) not captured. Rare char;
format ceiling likely.

## p3_char_0165_乍 (zhà) — FAIL
Top pie fine but the middle 横 + 竖 + bottom 横 stacking is disjointed —
the strokes read as three parallel lines rather than 乍's characteristic
top-hook + descending strokes. Fix idea: use single continuous 横折
for top-right corner, add descending 竖 through it.

## p3_char_0166_去 (qù) — FAIL
Top 土 renders as horizontals + shu OK, but the bottom 厶 collapsed to
just a horizontal line + fragment — the 撇折+dian curl is missing. Fix
idea: inline 厶 as a 撇折 bezier + dian per bootstrap sandbox fix for
032_厶.

## p3_char_0167_乎 (hū) — FAIL
Top strokes (short 撇 + dian + short heng cluster) collapsed into a
small triangle; long horizontal crossbar + shu present. The
characteristic 3-stroke top cap of 乎 is lost. Fix idea: draw top as
short pie left + short pie right + short heng between them
(triangular apex), then long crossbar, then long shu with terminal
弯钩.

## p3_char_0169_疋 (pǐ) — FAIL
Top box + fragmentary bottom strokes. 疋 needs 一 + 竖 + 撇+捺-like
legs. Legs missing/collapsed. Fix idea: reuse `zu` (足) pattern —
top box + 儿-like legs.

## p3_char_0170_发 (fā/fà) — FAIL
Big X in center + fragmentary strokes above. 发's top-右-hook + 又-body
+ dot cluster all lost. Complex 5-stroke cursive form — format ceiling
likely (adjacent to 反).

## p3_char_0171_疒 (nè) — FAIL
Only fragmentary top: a diagonal + short dot. The 广 outer frame's
vertical descender and the two internal dots (冫-like) are all missing.
Attempt is essentially blank. Fix idea: reuse `guang` (广) primitive +
inline two dots inside; check that the shu descender is drawn.

## p3_char_0173_仔 (zǐ) — FAIL
Left 亻 correct; right 子 rendered as 横撇 + shu + tiny bottom curl —
the terminal hook curl is disconnected from the crossing heng. Fix
idea: use `zi_char` (bank #122) verbatim on the right, at scale ~0.65,
ox=+40.

## p3_char_0174_主 (zhǔ) — FAIL
Top dot too small; three hengs stacked but too close together with
bottom heng disproportionately wider. Central shu present. Fix idea:
match GT spacing — top dot standalone, top heng short, middle heng
same width, bottom heng only slightly wider; shu passes through all
three.

## p3_char_0175_仕 (shì) — FAIL
Left 亻 pie disconnected from shu (pie floats above shu tip); right 士
correctly stacked but the whole char reads as three disconnected
elements. Fix idea: use `ren_pang` for 亻 (weld guaranteed) at
ox=-45, scale=0.55.

## p3_char_0176_平 (píng) — FAIL
Top pair of "dots" rendered as long slashes descending; horizontals
correct. The 丷-style dots should be small mirror-slanted dots ON TOP
of the horizontal, not descending strokes. Fix idea: use `variant_dian`
mirror pair with tiny w_tail=3 sitting at y≈+60 (above the top heng).

## p3_char_0177_仗 (zhàng) — FAIL
Left 亻 present; right 丈 rendered as an X (pie + na) without the top
heng and with na sweep too straight. Missing the top-heng cap. Fix
idea: draw right 丈 as top 一 (short heng at y=+80) + 撇 crossing + 捺
sweeping; the top heng is essential to distinguish 丈 from 乂.

## p3_char_0182_正 (zhèng) — FAIL
Frame renders but the shu descenders don't connect to top heng; bottom
heng detached. Reads as scattered frame. Fix idea: build strictly as
5 strokes with pixel-shared corners: 一(top) → 一(mid) → 竖(left) →
竖(mid, extending) → 一(bottom-wide).

## p3_char_0183_仞 (rèn) — FAIL
Left 亻 OK; right 刃 rendered too small in upper-right, hook detached.
Fix idea: enlarge right 刃 to full-height; use `dao_pang_char` template
+ add a dot at hook shoulder for the distinguishing mark of 刃.

## Cross-fail pattern (B6)

The 亻-family failures (化, 他, 仔, 仕, 仗, 仞) all follow one recipe:
`ren_pang` on left composes cleanly (identity), but the right component
is either an in-bank primitive at wrong scale or a compound that has
no bank primitive. The composition itself works; the right-component
recipe is missing. This is a CONTENT gap not a FORMAT ceiling. Under
v8's free-form drawer_memory.md, curator can now write natural-language
recipes for these right-components without needing to formalize as
callable functions — a genuinely new lever.

## Retry priority under v8 (positions 351–400)

**Prospective (a)** — 亻-family right components needed downstream:
- Build 也 (as inline envelope with weld interior) — needed for 池/驰/她.
- Build 士 (2-heng+shu) — needed for 志/吉/结.
- Build 子 (already bank #122 zi_char) — should have been reused for 仔; retry.
- Build 丈 (top heng + X-cross with sweep) — needed for 杖.

**Retrospective (b)** — items whose fail mode looks addressable under
v8's format unlock:
- 平, 主 — proportion/dot-placement issue; new free-form principle
  "small dots ABOVE heng, not descending" would fix.
- 卩-family (卬, PASSed) — same recipe should back-port to 印.
- 疒 — call `guang` (广) explicitly; drawer omitted the whole envelope.

**Format ceiling — skip**:
- 书, 引, 发, 丱, 乎, 出, 刅 — hooks/cursive/scale collapses that don't
  admit a stable inline recipe.


---

## B7 fails (positions 351–400) — main-curriculum

### p3_char_0184_业
5-stroke top-heavy char; two side pies + two side verticals + bottom heng. Drawer rendered but proportions collapse (2/3 judges NO). Fix: verify the two verticals actually touch bottom heng and side pies form clear ∨ opening.

### p3_char_0187_仡
亻+乞 compound. Right 乞 (乙+heng+short pie) is not in bank; drawer hand-rendered but 乙 hook shape failed. Fix: inline 乙 as one continuous heng→shu→sweep-right stroke, not 3 segments.

### p3_char_0190_加
力+口 L-R. Drawer inlined 力 (横折钩 + 撇) with draw_kou. Composition read but 力's hook geometry was off (hook tail didn't kick left). Fix: 横折钩 needs clear left-flick at hook end.

### p3_char_0191_仫
亻+幺. 幺 (small pie + 撇折 + 点) rendered as unconnected loops. Fix: 幺 top-loop must close cleanly; the 折 mid-stroke needs a sharp elbow.

### p3_char_0192_代
亻+弋. 弋's 斜钩 (diagonal-shu-hook) is the defining stroke and drawer's arc + hook combination was too gentle. Fix: 斜钩 must have a distinct upward hook flick at the bottom-right terminus.

### p3_char_0193_癶
Bilateral radical: mirror halves. Drawer attempted but left half's long 撇 and right half's long 捺 didn't converge at the correct apex point. Fix: use kiss_apex (or hand-compute) for the shared upper-center pixel; mirror-halve symmetry matters.

### p3_char_0194_世
5-stroke horizontal-and-vertical grid. Drawer inlined top heng + 3 shus + wrap-around bottom. Fix: the rightmost vertical must turn INTO the bottom heng as a 竖折; drawing 4 disconnected strokes fails the topology.

### p3_char_0196_东
Cursive/simplified char. Drawer's inline decomposition (5 short strokes) didn't reproduce GT's crossing 十 + 小 layout. Fix: 东 = short top pie + long heng + central shu-gou + two side dots — recompose.

### p3_char_0197_矢
Arrow: top pie + top heng + heng + long pie + long na. Drawer produced 大-family X-crossing at bottom; symmetric X apex issue similar to 大. Fix: apex needs to sit ON the middle heng, not above.

### p3_char_0198_立
5-stroke stack: top dot + heng + heng + two side legs. Drawer got the stack but bottom heng landed too high; dots/legs proportion off. Fix: bottom heng at y≈240; legs at y=180..235 span.

### p3_char_0201_冉
5-stroke frame with 横折钩 + interior shu + hengs. Drawer's inline 横折钩 hook was too small. Fix: 冉's 横折钩 has a distinct tall right-shu descending, not a tiny elbow.

### p3_char_0203_冊
Twin-frame + crossbar. Drawer used two 冂 frames but the crossbar didn't align through both frames at same y. Fix: single long heng passing through both frames at y≈150.

### p3_char_0204_由
Box + protruding central shu (below only). Drawer rendered box + shu but shu didn't clearly protrude below box. Fix: shu extends from y=90 through box to y=270 (well below box floor y=210).

### p3_char_0208_北
Two-halves L-R. Drawer adapted bi_char but swapped top stroke; result reads scattered. Fix: 北 left = 短横+竖+提 (三-stack tilted), right = 撇+竖弯钩 (人-legged); use bi_char verbatim with correct signs.

### p3_char_0209_冎
Complex 冋-like frame with interior verticals + hook. Drawer inlined but the 横折钩 got flattened. Fix: reduce interior clutter — 冎 is essentially 冋 + short interior 竖.

### p3_char_0211_冯
冫+马 L-R. Drawer inlined thin 马 (3 strokes) but 马's 竖折折钩 shape is too complex for pure line segments. Fix: 马 needs a proper 3-corner turn — inline as polyline with 4 corners not 3.

### p3_char_0212_处
5-stroke: 夂-top + 卜. Drawer's 夂 was correct but 卜 (bottom-right dot pair) landed inside the 夂 envelope. Fix: 卜 sits BELOW the 夂 envelope, dot to the right of a small central shu.

### p3_char_0213_処
処 = 几+夂 (几 outside, 夂 inside). Drawer inlined but the 几 envelope's top-left corner was open. Fix: 几 top must be one continuous 横折弯钩; left leg starts from that horizontal.

### p3_char_0214_记
讠+己. Drawer had no bank; hand-rendered but 己's 竖弯钩 body was too small. Fix: 己 fills right 60% width; its 竖弯钩 sweeps wide.

### p3_char_0216_失
5-stroke similar to 矢 but with different top. Drawer used pie + heng + heng + pie + na; bottom X apex same failure as 矢. Fix: same as 矢 — apex on middle heng.

### p3_char_0217_凹
Rectangular notch. Drawer used continuous outline with 8 segments (v8 signature freedom). Read but proportions collapsed. Fix: the notch depth ≈ half box height; use exact GT coords y=100..160 for notch bottom.

### p3_char_0218_刍
5-stroke: small pie + curved top 横折 + interior 横 + long 横. Drawer's 折 was too gentle. Fix: 折 needs a sharp right-angle elbow, not a curve.

### p3_char_0219_在
6-stroke: 横+撇+竖+士. Drawer rendered but 士 bottom-right component too small. Fix: 士 (3 strokes) is 30% of char width, sits in lower-right; heng-shu-heng stack with clear widths.

### p3_char_0220_丢
6-stroke: 千-top + 一 + 厶. Drawer's 厶 (bottom loop) was open. Fix: 厶 must close on itself — inline as curved bezier ending at start.

### p3_char_0222_乑
Three-人 radial: heng-hook + central shu + long left pie + bottom-right 人 (pie+na). Drawer positions off; reads as 4 scattered marks. Fix: this is 众-like — central shu is the spine, pies fan out symmetrically.

### p3_char_0223_地
土+也. Drawer's 也 rendered as scattered strokes (right rectangle + divider + hook), not as one 竖弯钩 envelope. Fix: 也 = 横 + 竖 + 竖弯钩 where the 竖弯钩 forms the whole right envelope (per drawer_memory 亻+也 recipe).

### p3_char_0224_乓
丘+丿-like. Drawer's top-丘 rendered but bottom-right 丿 sweep was too short. Fix: bottom-right stroke is a long 撇 or 捺 (乓 has 撇 sweep-out-lower-right).

### p3_char_0225_而
6-stroke: heng + heng-zhe + 3 interior shus. Drawer rendered but interior shus didn't visually connect to top frame. Fix: shus start ON the underside of the top heng-zhe, not floating below.

### p3_char_0226_乔
6-stroke: 夭-top + 小-bottom. Drawer's top 夭 pie+na crossing failed like 大. Fix: 夭 apex through top heng; bottom 小 needs 3 clear separated strokes.

### p3_char_0227_年
6-stroke with multiple hengs on a central shu. Drawer stacked hengs OK but the central shu didn't extend clearly through all hengs. Fix: shu from y=60 to y=260 passing through 3 hengs.

### p3_char_0229_自
6-stroke: 撇 + shu + heng-zhe + 3 interior hengs. Drawer's interior hengs were unevenly spaced. Fix: 3 interior hengs at y=140, 175, 210 (equal spacing).

### p3_char_0231_会
6-stroke: 人-roof + 云-body. Drawer's roof pie+na crossing failed at apex; 云 body was tiny. Fix: roof pie+na is wide (spans full width); 云 sits under it at 60% scale.

### p3_char_0232_亙
亘 variant. Drawer's middle 日-like body was rectangular but not curved. Fix: 亙 middle body is a rounded oval, not a rectangle — use bezier for the 亙-belly.

### p3_char_0233_那
7-stroke L-R: 冄-like left + 阝 right. Drawer's left was too tall vs right. Fix: L-R at 0.55/0.55; right 阝 is compact 2-stroke.


## B7r fails (v9 reruns that still FAILed)

### p2_radical_028_人__retry_5__G3__rerun
V9 rerun FAIL despite correct visual diagnosis (apex gap + uniform weight + straight legs). Hand-render still short. Two-stroke X-crossing calligraphy is beyond callable-Python line-primitive expressiveness. Terminal-freeze AGAIN.

### p2_radical_030_入__retry_5__G3__rerun
V9 rerun FAIL. Drawer correctly identified topology (捺 emerges from side of 撇, not apex) but hand-render didn't reproduce hood. Terminal-freeze AGAIN.

### p2_radical_011_匕__retry_4__G3__rerun
V9 rerun FAIL. Drawer diagnosed 撇 crossing + upward hook + top horizontal missing; render addressed some but hook + horizontal alignment still off.

### p3_char_0154_他__retry_1__G3__rerun
V9 rerun FAIL. Drawer correctly rejected rectangle-collapse of 也 but hand-rendered 也 still reads as compound of small strokes rather than one envelope. 也 sub-recipe unsolved.

### p3_char_0173_仔__retry_1__G3__rerun
V9 rerun FAIL. Drawer correctly rejected liao_char's shoulder-blob and used inline thin ink but 子's 横 width + 亻 shu length still off. Bank #122 zi_char never actually invoked — try it verbatim on next retry.

### p3_char_0176_平__retry_1__G3__rerun
V9 rerun FAIL. Drawer correctly identified top-tent vs 丷-pair issue but the reconstruction still didn't cleanly render 丷 + short heng + main heng + shu descending only below main heng.

### p3_char_0134_化__retry_1__G3__rerun
V9 rerun FAIL. Drawer diagnosed 亻 shu disconnected + 匕 too small; render extended 匕 but hook still degenerate. 匕 sub-radical unsolved → 化 blocked.



## Batch B8 (2026-07-27, positions 401–450) — 41 main FAILs

Compact per-item diagnosis. Full attempt PNGs at
`attempts/p3_char_02XX_<char>/01_<char>.png`. Common patterns discussed
in the "Fail-mode clusters" section immediately after this list; drawer
should read the cluster analysis before per-item.

### p3_char_0234_亚 (yà)
Symmetric 6-stroke block. Attempt has correct top/bottom heng but the
inner "vertical + wing + vertical" is muddled — the pair of arms reads
as two verticals rather than the mirror slant. Inline PIL, no bank.

### p3_char_0235_后 (hòu)
Attempt has 厂 top + 口 bottom but the middle 一 (heng) is missing or
merged with the upper 撇, leaving the wrong 5-stroke silhouette.

### p3_char_0236_亥 (hài)
6-stroke top-down: 亠 top + 幺 middle-like + 人-swirl bottom. Attempt
reads as a stack of 3 disconnected pieces; the diagonal cross-strokes
in the middle collapse into parallel diagonals.

### p3_char_0237_行 (xíng)
Left 彳 + right 亍. Attempt renders both halves too thin and too
similar; the right 亍's short-heng-over-long-heng-over-shu-gou is
compressed into a single vertical, losing the double-heng signal.

### p3_char_0238_亦 (yì)
Top 亠 + bottom 4-arm splay. Attempt gets 亠 but the 4-arm splay
reads as 亅+丶+丶+丿 rather than the wider mirror arms + inner shu +
dot. Arm-length ratios wrong.

### p3_char_0240_仰 (yǎng)
亻 + 卬 (right). Attempt reuses ren_pang left; right 卬 inline is
missing its distinctive top-hook flick — reads as a plain 卩.

### p3_char_0241_如 (rú)
女 (left, inline) + 口 (right). 女's 撇点 fold is too shallow; the
right 口 is centered too low. Reads as ambiguous compound.

### p3_char_0243_成 (chéng)
7-stroke with 戈-body + 丿 + interior 一. Attempt renders 戈's 斜钩
as a near-straight diagonal with a stubby hook; the interior 一 is
missing. Format ceiling on 斜钩 arc.

### p3_char_0244_仳 (pǐ)
亻 + 比 (right). Right 比 inline reads as two blocks side-by-side
rather than the mirrored 匕+匕 pair. 匕 sub-radical remains unsolved
(see TERMINAL_FREEZE).

### p3_char_0246_仵 (wǔ)
亻 + 午 (right). 午's top 撇 too long, second 一 too short; the
overall right-side proportion reads as 千 not 午.

### p3_char_0247_军 (jūn)
宀 top + 车 bottom. 车 body inline is over-simplified — the interior
crossbar geometry (two 横 crossed by one 竖) reads as a single tic-tac.

### p3_char_0248_伄 (diào)
亻 + 弔 (right). 弔's 弓 body inline is degenerate — the three
horizontal loops don't render as three tiers, and the central 竖 (or
弔's 丨) doesn't pierce cleanly.

### p3_char_0251_当 (dāng)
Simplified 5-stroke with 小 top + 彐-like body. Attempt's top 3 dots
read as symmetric but GT has the middle dot LONGER/skewed. Bottom
彐-frame proportion wrong.

### p3_char_0252_伊 (yī)
亻 + 尹 (right). Right 尹 inline is short one horizontal — reads as
彐 not 尹. Extra 撇 missing.

### p3_char_0253_好 (hǎo)
女 + 子. Both sub-radicals inline; drawer noted "shorten dot bounce"
in comments but the 女's 撇点 fold still doesn't read as a V; and 子's
shu-hook is too weak. Same failure mode as B7's 妃/她 fails.

### p3_char_0254_伎 (jì)
亻 + 支 (right). 支's top 十 + bottom 又 inline compress into a plus
+ triangle; 又's 撇/捺 spread too wide.

### p3_char_0255_此 (cǐ)
止 (left) + 匕 (right). 匕 unsolved → right side of 此 fails
identically to 仳/比. Left 止 is passable but the pair reads as
disconnected halves rather than L-R composition.

### p3_char_0256_伐 (fá)
亻 + 戈 (right). Same 斜钩 arc issue as 成 — the diagonal is straight
and the hook is stubby.

### p3_char_0258_伕 (fū)
亻 + 夫 (right). 夫's X-crossing (top 一 + long 一 + 撇 + 捺 crossing)
sits in the same format-ceiling family as 大/矢/失/乔. Attempt
inlines but 撇 and 捺 don't kiss visibly.

### p3_char_0260_伙 (huǒ)
亻 + 火 (right). 火's mirror-dot + big X inline reads as 4 straight
diagonals; the fire silhouette is lost.

### p3_char_0261_再 (zài)
6-stroke box with top-heng crossing + interior 冂 + long central shu.
Attempt has the wrong proportions — top heng too short, box too tall,
central shu doesn't protrude below.

### p3_char_0263_她 (tā)
女 + 也. 也 sub-radical unsolved (same as 他 v9 rerun fail); the
right side reads as scribble of 3 arcs. 女 passable.

### p3_char_0264_伢 (yá)
亻 + 牙 (right). 牙 inline is degenerate — the 竖-with-hook + 二 +
short-撇 topology doesn't emerge; reads as a hash mark.

### p3_char_0265_名 (míng)
夕 top + 口 bottom. dxi bank primitive used at compressed scale; the
attempt has 夕 too tall AND 口 too small — total silhouette reads as
2-stack rather than 名's fluid dxi-over-kou.

### p3_char_0266_伥 (chāng)
亻 + 长 (right). 长's 斜钩 + 捺 + interior strokes inline — the
右 side reads as an over-thin cross rather than 长's characteristic
sweeping bottom.

### p3_char_0267_西 (xī)
6-stroke with top 一 + 冂 body + interior 儿-like. Attempt collapses
the interior into two diagonals; the top 一 sits AT the frame instead
of ABOVE.

### p3_char_0268_伦 (lún)
亻 + 仑 (right). 仑's 人-top + 匕-body inline is doubly-affected by
the X-crossing AND 匕-hook ceiling issues.

### p3_char_0269_合 (hé)
Top 人 (or 亼) + 一 + 口. Attempt reads as 合 but the 人-roof kiss is
missing (apex-kiss format ceiling); the roof looks like two disjoint
diagonals. See TERMINAL_FREEZE cluster.

### p3_char_0270_伧 (cāng)
亻 + 仓 (right). 仓's inline top-人 + 巳-like body — same apex-kiss
ceiling.

### p3_char_0271_老 (lǎo)
耂 top + 匕 bottom. 匕 unsolved. Even though耂 (bank lao_radical) is
mastered, the drawer chose to inline it fresh for "thin uniform" per
P12 and the fresh render didn't match the bank's mastered geometry.

### p3_char_0272_伪 (wěi)
亻 + 为 (right). 为 inline's four-part structure (top-dot + top-撇 +
mid-envelope + bottom-dot) is compressed and reads as scribble.

### p3_char_0273_次 (cì)
冫 (left, bank san_dian_shui-like) + 欠 (right). 欠's top 撇 + 横钩 +
撇 + 捺 has the same apex-kiss ceiling as 人-family.

### p3_char_0274_伫 (zhù)
亻 + 宁 (right). 宁 inline: 宀 top + 丁 bottom. 宀-top's cross-shape
lid doesn't render cleanly; 丁's shu-gou too thin.

### p3_char_0275_任 (rèn)
亻 + 壬 (right). 壬 inline three-tier hengs + shu reads as 王 (missing
the 撇 top).

### p3_char_0276_佤 (wǎ)
亻 + 瓦 (right). 瓦's compound hooks + envelope + interior dot inline
— the two hooks don't disambiguate cleanly.

### p3_char_0277_先 (xiān)
6-stroke with 土-like top + 儿 bottom. Attempt fails at 儿's
er_ren-kiss geometry (see xiong_char PASS for the recipe of REJECTING
er_ren bank and rendering thin) — same cluster.

### p3_char_0278_齐 (qí)
Simplified: 亠 top + 4-diagonal splay bottom. Attempt's bottom four
diagonals don't converge upward — reads as 4 parallel lines.

### p3_char_0279_色 (sè)
Top 刀-like curl + 巴 bottom. 巴 inline's continuous envelope +
interior hengs is degenerate; the curl top reads as two dots.

### p3_char_0280_兆 (zhào)
Mirror-symmetric 4-arm splay + interior verticals. Same mirror-arm
problem as 亦/齐/亦: the mirror pair doesn't render as mirror.

### p3_char_0281_设 (shè)
讠 (left) + 殳 (right). Both sides inline. 讠's dot + heng-shu-ti
compresses; 殳's top 几-like + 又 bottom compresses. Reads as scribble.

### p3_char_0283_传 (chuán)
亻 + 专 (right). 专's compound zig-zag + interior + 寸-bottom is a
5-stroke right side that doesn't decompose cleanly; the interior
horizontal is missing.

## Fail-mode clusters — B8

Of 41 main fails:
- **19 are 亻 + right-component** (仰, 仳, 仵, 伄, 伊, 伎, 伐, 伕, 伙,
  伢, 伥, 伦, 伧, 伪, 伫, 任, 佤, 传, 伧). The 亻 left is well-handled
  (bank ren_pang at compressed scale) — the failure is always in
  the RIGHT component. Root causes vary:
    - Right needs a sub-radical not in bank (匕, 也, 牙, 尹, 弔, 支,
      戈-arc, 长-arc, 瓦, 为, 壬 — 11 items).
    - Right needs X-crossing / apex-kiss (夫, 火, 欠, 大-family — 4 items).
    - Right is bank-mastered but drawer inlined fresh unnecessarily
      (仝-like 亻+bank patterns — 2 items).

- **6 are X-crossing / apex-kiss family** (成, 伐, 合, 次, 伧, 伙 — plus
  the 4 亻-family items above). Continues the 大/矢/失/乔/会 pattern
  observed in B7. `xiong_char` PASS (B8 entry #212) shows the recipe
  (thin inline + reject bank er_ren) DOES work on the 兇 case but the
  strokes need to sit in a specific 儿-context to read.

- **5 are mirror-symmetric splay** (亚, 亦, 齐, 兆 + 亦 counted twice).
  4-arm outward mirror splay. No bank support; inline attempts always
  degenerate to "4 parallel diagonals."

- **4 are frame-with-interior** (再, 西, 军, 色). Wrong interior
  aspect ratio — the frame is right, the interior element is placed
  at wrong scale/offset. `hui_char` PASS (回, entry #210) shows the
  recipe works when both frame AND interior have bank mastered
  aliases; fails when either must be inlined fresh.

- **3 are unsolved-sub-radical** (她, 好, 亥). Compound needs 也 or
  子's inline recipe; sub-radicals still don't render.

- **4 miscellaneous** (亚, 后, 亥, 251_当). Frame/proportion.

The dominant pattern is **compound with an unsolved right-side
sub-radical**. This confirms drawer_memory's B7 note that "右 side
sub-radicals not in bank" is the primary B8 content gap. Adding bank
entries for 匕 / 也 / 尹 / 牙 / 支 / 戈-arc would unblock ~15 of B8's
fails on a hypothetical B8-rerun. Under v10 trajectory-view, drawers
that see multiple failed 亻-family attempts may triangulate the right
side better; but the sub-radical itself remains the ceiling.

## Batch B9 (2026-07-30, positions 451–500) — 36 main FAILs, 0 A

**B9 pass rate: 14/50 = 28% (down from B8's 18%; still well below G4's
40% and 11 A verdicts on the same batch).** Item-pool composition
remains 亻-family heavy (positions 451–500 stay in the 伊/伍-band of
Phase-3 characters) plus a run of 7-stroke compound chars.

### Cluster A — 亻 + right-component (still the dominant fail mode)

12 of 36 fails follow the exact same pattern noted in B8: bank
`ren_pang` (L side) works fine; the RIGHT sub-radical is not in bank
and inline rendering degenerates. New in B9:

### p3_char_0297_你 (nǐ) — 亻 + 尔
尔 = the 3-stroke arrow + 小 bottom. Inline reads as scribble; the
top pie/heng joint doesn't disambiguate from 你 vs 尓 vs 尒.

### p3_char_0312_伲 (ní) — 亻 + 尼
尼 has no bank primitive; the 尸 top (bank shi_radical) + 匕-bottom
composition fails on the 匕 (匕 is TERMINAL_FROZEN).

### p3_char_0313_位 (wèi) — 亻 + 立
立's top dian + 3-line body renders correctly BUT the panel does not
accept the character — likely 亻+立 spacing plus dian orientation.

### p3_char_0314_伶 (líng) — 亻 + 令
令 = 人 top (X-crossing) + 冫-like middle + 亅 hook. Top X-crossing
alone is enough to fail (same format ceiling as 大/夭/矢).

### p3_char_0316_伺 (sì) — 亻 + 司
司 has 3-stroke enclosure + interior — no bank; inline enclosure
+ inner 一+口 degenerates.

### p3_char_0318_伽 (jiā) — 亻 + 加
加 = 力 + 口 side-by-side. 力 (bank #NA — TERMINAL) + kou identity fails
because 力's hook doesn't compose cleanly with kou's box at reduced
scale.

### p3_char_0320_伾 (pī) — 亻 + 丕
丕 = 一 + 不 (with double-crossing 撇+捺). Inline sinks into 大-family
X-crossing failure.

### p3_char_0328_佈 (bù) — 亻 + 布
布 = 𠂉 (short pie + heng) + 巾. 巾 has no bank; inline 冂+shu fails
on the enclosure aspect.

### p3_char_0330_佉 (qū) — 亻 + 去
去 = 土 top + 厶 bottom (bank tu.py + 厶 is TERMINAL). 厶 unsolved
sub-radical.

### Cluster B — enclosure + interior with un-mastered interior

### p3_char_0298_丽 (lì) — top 一 + 2 mirrored small boxes (冂+内-dot ×2)
Mirror-symmetric enclosure pair. Same 4-arm mirror problem as
亚/齐/兆 in B8 (mirror pair doesn't render as mirror).

### p3_char_0309_两 (liǎng) — top 一 + envelope 冂 + interior 从
从 (twin 人) inside 冂 needs X-crossing rendering ×2. Format ceiling.

### p3_char_0317_员 (yuán) — 口 top + 贝 bottom
贝 unsolved sub-radical; bottom's box + splay reads as 见 rather than 贝.

### Cluster C — cursive envelope with hook (unsolved family)

### p3_char_0311_身 (shēn) — narrow-tilted body + top 撇 + big descender 撇
Body-with-tilted-verticals unsolved; the big descending 撇 sweeps
beyond canvas.

### p3_char_0300_乱 (luàn) — 舌 + 乚 (shu_wan_gou)
舌 top's 千-like + kou-bottom composition doesn't read; 乚 works.

### p3_char_0288_凫 (fú) — 乌 top + 几 bottom
乌 unsolved (cursive envelope + interior dot). Bank ji_char below
works; top does not.

### p3_char_0319_听 (tīng) — 口 + 斤
斤 unsolved sub-radical. Bank kou on left; inline 斤 on right degenerates.

### p3_char_0321_把 (bǎ) — 扌 + 巴
巴 unsolved. Bank shou_pang works; 巴 inline continuous envelope +
interior heng ambiguous vs 已/己/巳.

### p3_char_0323_形 (xíng) — 开 + 彡
开 has no bank; inline reads as 二+两-shu. Bank shan_radical works
on the right.

### p3_char_0325_状 (zhuàng) — 丬 (left) + 犬 (right)
Both unsolved. 丬 TERMINAL; 犬 has 大-family X-crossing + dot.

### p3_char_0327_识 (shí) — 讠 + 只
讠 TERMINAL; 只 = 口+八 works partially but 讠 sinks it.

### p3_char_0331_更 (gèng) — top 一 + 曰-box (with mid bar) + 撇 + 捺
Bottom X-crossing (撇+捺 from box corners) — same 大 family. Inline
fresh; 撇/捺 don't meet cleanly at box base.

### p3_char_0333_条 (tiáo) — 夂 top + 木 bottom
夂 unsolved (TERMINAL). 木 works on bottom but 夂 top is scribble.

### Cluster D — miscellaneous first-time fails

### p3_char_0284_龹 (yǎn) — rare char: 丷+两hengs+shu+八 stacked
No decomposition maps to bank; inline fresh degenerates on the
stacked geometry.

### p3_char_0285_师 (shī) — 帅-like left + 帀 right
Left is compound short heng + long pie-shu; right is 一+巾. Both
un-mastered. Reads as scribble.

### p3_char_0286_冱 (hù) — 冫 + 互
互 unsolved compound (two hengs + zigzag). 冫 (bank bing) works.

### p3_char_0289_我 (wǒ) — 7-stroke cursive with 戈-arc
Same 斜钩 arc problem as 成/伐/戈-family in B8. Format ceiling.

### p3_char_0292_甹 (pīng) — 由 top + 亏-like bottom
由 top box shape not directly in bank (shen_extend closest); bottom
亏-like reads as 与.

### p3_char_0293_来 (lái) — top heng + 丷 + long heng + shu + pie + na
Bottom X-crossing (撇+捺) — same 大 family format ceiling.
Additionally 丷 dots require the mirror-dot recipe.

### p3_char_0295_时 (shí) — 日 (bank ri) + 寸 (bank cun)
BOTH sides have bank aliases. This should have PASSed as an identity
composition (like 佃 or 但). Diagnosis: drawer inlined 寸 instead of
calling `cun.draw_cun`; the fresh 寸 rendered without hook. **Bank-
composition retrieval failure — not a format ceiling.** Retry candidate
for B10.

### p3_char_0296_串 (chuàn) — 2 stacked 口 + long central 竖
Bank kou ×2 + central shu — SHOULD have worked. Diagnosis: drawer
made the boxes too small (0.42 scale) and the shu doesn't visibly
protrude above/below. Retry candidate for B10.

### p3_char_0304_疖 (jiē) — 疒 + 卩
Bank ne_sick (疒) OK; 卩 (bank jie_radical) not called — drawer inlined.
Retry candidate.

### p3_char_0305_还 (hái) — 辶 + 不
Bank zou_zhi OK; 不 has 大-family X-crossing bottom. Format ceiling
on 不.

### p3_char_0306_亨 (hēng) — 亠+口+了
亠 (bank tou_char) + kou + 了 (bank liao). All bank but stacked
proportions off — kou too wide, 了 too small. Retry candidate.

### p3_char_0307_没 (mò) — 氵 + 殳
殳 unsolved compound (几 top + 又 bottom). 氵 (bank san_dian_shui) OK.

### p3_char_0315_声 (shēng) — 士 top + 尸 bottom
Bank shi_male (士) + shi_radical (尸). Stacked composition SHOULD
have worked; drawer's proportions cramped the 尸 hook. Retry candidate.

### p3_char_0329_运 (yùn) — 辶 + 云
Bank zou_zhi OK; 云 inline fresh (二 + 厶). 厶 sub-radical unsolved
(TERMINAL) — 云 always fails when 厶 needed.

## Fail-mode clusters — B9

Of 36 main fails:
- **12 亻 + unsolved-right** (你, 伲, 位, 伶, 伺, 伽, 伾, 佈, 佉,
  伪-family). Same B8 pattern.
- **6 X-crossing / apex-kiss family** (伶, 伾, 我, 来, 更, 305_还-bottom).
  大 recipe still not transferring at scale.
- **6 unsolved sub-radicals holding compounds hostage** (厶, 巴, 匕, 讠,
  丬, 夂, 斤, 巴, 巾) — no protocol path to master these; they gate
  ~30% of Phase-3.
- **5 bank-composition-retrieval failures** (295_时, 296_串, 304_疖,
  306_亨, 315_声) — items whose ALL parts had bank aliases but drawer
  still inlined. These are the highest-value B10 retry candidates:
  under v10 trajectory-view, the correct bank-call pattern should
  surface.
- **4 mirror-symmetric splay / bilateral X** (298_丽, 293_来, 309_两,
  289_我). New B9 problem: 丽 requires a mirror-box pair (like 亚's
  mirror-arm pair from B8).
- **3 misc first-time compounds** (龹, 甹, 285_师).

**Dominant B9 mode: sub-radical gate + composition-retrieval leak.**
The gate items (12 sub-radicals TERMINAL) cannot be unblocked without
a new mechanism. The composition-retrieval items (5) are the retryable
lever for B10.

## G3 vs G4 gap on B9 — code-format ceiling diagnosis

G4 posted 40% (20/50) with 11 A verdicts on identical B9 items. G3
posted 28% (14/50) with 0 A. The differential structural feature:

- G4 memory unit: **米字格 grid anchors + P/T/N/S joint specs** — a
  calligraphic-structure grammar operating at the STROKE-JOINT layer.
- G3 memory unit: **callable Python functions rendering via PIL line
  primitives** — a pixel-drawing grammar operating at the LINE layer.

The G4 anchor+joint grammar encodes where two strokes meet (weld
type, apex position, cell alignment) in a way judges can pattern-match
to calligraphic conventions. G3's PIL line/bezier code has no
vocabulary for "these two strokes should share a pixel at a
30-degree joint" other than hand-computed geometry. Even when the
drawer computes it correctly, PIL rasterisation smooths joints as
straight-line intersections rather than modulated ink meetings —
which reads as "machine-drawn" and never earns an A verdict.

**Conclusion: G3's code-format IS hiding calligraphic quality.** The
drawers frequently produce structurally correct characters (28% pass
rate demonstrates this) but the rendering is stuck at "reads as the
character, does not read as calligraphy." The 0-A verdict count is
not a diagnosis-ceiling — it is a rendering-vocabulary ceiling.

Actionable in drawer_memory.md: acknowledge the ceiling and orient
G3's remaining effort toward what IS still winnable at the
structural-recognition layer:
- Identity-alias composition (bank-part + bank-part with copy-paste
  scale table) — 佃/但/伯/佐-style. Highest hit rate.
- Envelope + bank-mastered interior (回, 甸-style). Second-highest.
- 亻 + bank-right-radical (仲, 伉-style). Third-highest.

Give up chasing A verdicts on genuinely cursive items (X-crossing,
mirror-splay, cursive envelopes) — pursue them ONLY if the composition
lets us stack bank aliases. Retry channel should prioritize
composition-retrieval failures (295_时, 296_串, 306_亨, 315_声)
which have the highest retry ROI.

---

## B10 additions (2026-07-31, position 500)

### FAIL (main channel, 33 items)

- **p3_char_0336_佗** — 亻 + 它 (它 unmastered). Right reads as boxy;
  needs 宀 top + 匕-like bottom hook. Fix: import bao_gai_tou for 宀.
- **p3_char_0337_张** — 弓 + 长. 长 X-crossing format ceiling.
- **p3_char_0338_佘** — 亠 + 尔-like bottom. Both unmastered as stack.
- **p3_char_0339_每** — 母 X-crossing (dots+X). Format ceiling.
- **p3_char_0340_佚** — 亻 + 失. 失 X-crossing (retry_3 also failed).
- **p3_char_0342_佛** — 亻 + 弗. 弗 (two-shu-with-弓-fragment) unmastered.
- **p3_char_0343_即** — BANK_DEVIATION on jie_radical (weight). Left 皀
  proportions off. Fix idea: 皀-left thin ~4px matches deviation intent.
- **p3_char_0344_佝** — 亻 + 句. 句 (勹+口) — 勹 bank exists but
  interior placement drifted.
- **p3_char_0345_志** — **C**. See sandbox B10 diagnostic. Retry candidate
  with tightened 卧钩 + 3 dots inside concavity.
- **p3_char_0346_佞** — 亻 + 妟-like. Multi-radical right, no clear
  decomp. Content gap.
- **p3_char_0347_证** — BANK_DEVIATION (讠 and 正 both terminal errata).
  Both unmastered; deviation was forced but couldn't succeed.
- **p3_char_0348_佟** — 亻 + 冬. 冬 (folded-envelope + 2 dots) unmastered.
- **p3_char_0349_改** — BANK_DEVIATION (己 vs bank 巳; 攵 unmastered).
  Both sub-radicals unmastered. Fresh render legible but too spread.
- **p3_char_0351_步** — 止 + 少. Cursive 少 bottom unmastered.
- **p3_char_0352_佥** — 亽 + 从 stacked. Multi-radical stack unmastered.
- **p3_char_0353_找** — BANK_DEVIATION (弋 vs 戈). 戈 X-crossing +
  bezier-arc format ceiling.
- **p3_char_0355_块** — 土 + 夬. 夬 X-crossing.
- **p3_char_0358_盯** — **C**. BANK_DEVIATION (both ri and ding_char
  don't fit L-R slot geometry). Retry candidate with 目 widened to 28%.
- **p3_char_0360_並** — 立-family with double stack. Unmastered.
- **p3_char_0361_到** — 至 + 刂. 至 (multi-heng stack + 土) unmastered
  as compound.
- **p3_char_0362_甾** — **C**. BANK_DEVIATION (chuan straight vs 巛 curly).
  Retry candidate with curled scoop tails + 15px gap.
- **p3_char_0365_和** — **C**. Non-deviation. 禾 pie/na spread too wide;
  口 too small. Retry candidate.
- **p3_char_0366_畅** — 申 + 昜. Multi-radical right unmastered.
- **p3_char_0367_事** — Multi-part stack (一+口+彐+丨with hook). Frame
  proportions drift.
- **p3_char_0368_乖** — 禾-variant + mirror strokes. Cursive; unmastered.
- **p3_char_0369_其** — 甘 + 二 stack. Frame proportions drift.
- **p3_char_0370_乶** — BANK_DEVIATION (Korean-ideographic 甫 nested over
  乙). Unusual glyph; no bank support.
- **p3_char_0371_所** — Uses shi_radical bank; 斤-right proportions off.
- **p3_char_0372_疌** — BANK_DEVIATION (no direct match; 聿 not in bank).
  Content gap.
- **p3_char_0374_疙** — BANK_DEVIATION (qi_ji is 亓 not 乞). 乞 unmastered.
- **p3_char_0375_经** — 纟 + 圣. 纟 (silk radical) unmastered; 圣 (又+土)
  stack unmastered.
- **p3_char_0376_疚** — 疒 + 久. 久 (dented X) unmastered.
- **p3_char_0377_法** — **C**. Non-deviation. 氵 too small; 厶 as separate
  strokes. Retry candidate.
- **p3_char_0379_学** — BANK_DEVIATION (zi_char needs vertical shift).
  ⺌ + 冖 + 子 stack proportions drift.
- **p3_char_0380_疟** — 疒 + 虐-fragment. 虐 unmastered.
- **p3_char_0381_定** — BANK_DEVIATION (bao_gai_tou coord-system mix).
  疋 unmastered.
- **p3_char_0382_疠** — 疒 + 万. 万 unmastered as compound bottom.
- **p3_char_0383_些** — 此 + 二. 此 (止+匕) unmastered as compound.

### FAIL (retry channel, 5 items)

- **p3_char_0304_疖** (retry_1) — B9 leak candidate. Even with bank
  ne_sick + jie_radical, narrow-column proportions drift. B11:
  add explicit "疒 in left 40%, 卩 in right 40%, both thin" hint.
- **p3_char_0306_亨** (retry_1) — B9 leak candidate. 3-stack proportions
  (亠 small / 口 medium / 了 large) hard to encode without joint specs.
  B11: try again with explicit y-band hints per component.
- **p3_char_0315_声** (retry_1) — B9 leak candidate. 士 + 尸 envelope
  proportion drift.
- **p3_char_0197_矢** (retry_3) — X-crossing family. TERMINAL_FREEZE
  watch at retry_5 (B12). B11 retry_4: da_char recipe as template.
- **p3_char_0216_失** (retry_3) — X-crossing family. TERMINAL_FREEZE
  watch at retry_5 (B12). B11 retry_4: da_char recipe as template.

### PASS (bank additions — see success_bank/INDEX.md rows 213–226)

12 mains + 2 retries promoted. 3 v13 BANK_DEVIATION variants promoted
(rows 227–229). All original primitives untouched.

## Batch B11 (2026-08-03, positions 551–600 judged + 5 retries)

### TERMINAL_FROZEN at B11 (retry_4 hit C, no PASS)

Per shared_rules.md terminal-freeze rule (retry exhausted with progressive
format unlocks; C at last-chance retry proves format-ceiling structural).
X-crossing format ceiling family, joins B5's 人/入/大 and B8's 匕.

- **p3_char_0197_矢** — X-crossing (dai-family, apex-in-heng geometry).
  Retry trajectory: R1 FAIL, R2 FAIL, R3 FAIL (v9 visual-diff), R4 **C**
  (v13 explicit-bank-call with da_char template). C means readable but
  not panel PASS. Diagnosis: PIL line-segments produce the crossing pixel
  but not the joint modulation the panel expects. Move OUT of active
  retry pool.

- **p3_char_0216_失** — X-crossing (matched fate to 矢). Same trajectory.
  Move OUT of active retry pool.

### FAIL (main channel, 32 items)

- **p3_char_0384_疡** — 疒 + 昜. Multi-radical right unmastered.
- **p3_char_0385_物** — **C**. See sandbox B11 diagnostic. Retry candidate
  with sharpened ti and parallel 勿 arms.
- **p3_char_0386_亞** — BANK_DEVIATION (no 亞 primitive). Mirror-envelope
  4-arm splay format ceiling.
- **p3_char_0388_亟** — Multi-component compound with bumpy interior.
  Content gap.
- **p3_char_0390_佬** — 亻 + 老-bottom. BANK_DEVIATION on ren_pang for
  joint-scale mismatch. 老-bottom unmastered.
- **p3_char_0392_佯** — 亻 + 羊. BANK_DEVIATION on ren_pang. 羊 unmastered.
- **p3_char_0393_实** — 宀 + 头-body. BANK_DEVIATION on bao_gai_tou + da_char.
  Fresh render legible but proportions drift.
- **p3_char_0394_佰** — 亻 + 百. Bank primitives only; drift in 百-body.
- **p3_char_0395_金** — 5-stroke roof + 王-body. Multi-radical, roof
  proportion drift.
- **p3_char_0396_佴** — 亻 + 耳. 耳 unmastered as bank; inline drifts.
- **p3_char_0398_併** — 亻 + 并. 并 (双 4-stroke) unmastered.
- **p3_char_0401_取** — BANK_DEVIATION (耳 not in bank; inlined). 又 bank
  used. Fresh 耳 legible but composition drift.
- **p3_char_0402_佻** — BANK_DEVIATION (no 兆 primitive). 兆 mirror-splay
  format ceiling.
- **p3_char_0403_放** — BANK_DEVIATION (方 and 攵 both in errata). Both
  unmastered.
- **p3_char_0404_佼** — 亻 + 交. 交 X-crossing family fail.
- **p3_char_0405_治** — 氵 + 台 = 厶 + 口. No 厶 bank; inline drifts.
- **p3_char_0406_佽** — 亻 + 次 = 冫+欠. BANK_DEVIATION (no 欠/次).
  Fresh legible but 欠 stroke sequence off.
- **p3_char_0407_规** — 夫 + 见. BANK_DEVIATION (no 夫 or 见). Both
  unmastered as bank; inline drifts.
- **p3_char_0408_佾** — **C**. See sandbox B11 diagnostic. Retry candidate
  with shrunk ba (0.55 scale) and compressed 月.
- **p3_char_0410_侃** — 亻 + 冂-with-儿. BANK_DEVIATION (no 侃-family).
  Frame-with-pillars format ceiling.
- **p3_char_0411_受** — **C**. See sandbox B11 diagnostic. Retry candidate
  with compressed 爫 and lowered 冖.
- **p3_char_0412_來** — Non-deviation. 木 base + 从 top. 从 X-crossing.
- **p3_char_0415_转** — BANK_DEVIATION (no 车 or 专). Both novel; fresh
  fails.
- **p3_char_0416_侉** — BANK_DEVIATION (no 夸). Fresh 夸 legible but
  proportion drift.
- **p3_char_0417_单** — Bank 単-family bank exists but proportions off.
- **p3_char_0418_例** — 亻 + 列 = 歹+刂. 歹 in bank, 刂 in bank; composition
  drift.
- **p3_char_0420_侌** — BANK_DEVIATION (no 今 or 云 in bank; hui_char
  unrelated). Novel top+bottom stack fails.
- **p3_char_0421_或** — Non-deviation. 戈 X-crossing fail.
- **p3_char_0426_侔** — 亻 + 牟. 牟 unmastered.
- **p3_char_0427_线** — BANK_DEVIATION (si_zi_pang has baked coords,
  cannot slot into L-R). Fresh 纟 legible but 戋 (long 斜钩) format
  ceiling.
- **p3_char_0428_侖** — BANK_DEVIATION (ji_meet_char turtle math-coord;
  need PIL px). Compact 亼-over-frame drift.
- **p3_char_0429_是** — BANK_DEVIATION (ri.py canvas-fill; 是 needs
  compressed 日). Fresh 日 OK but 疋 hanging bottom drifts.
- **p3_char_0430_畈** — BANK_DEVIATION (no 田/反 for L-R). Frame drift.
- **p3_char_0431_说** — **C**. BANK_DEVIATION (讠 TERMINAL + no 兑). See
  sandbox B11 diagnostic. Retry candidate with compressed 讠 and
  er_ren_for_bottom_stack for 儿.
- **p3_char_0432_畋** — BANK_DEVIATION (田 baked to canvas; 攵 novel).
  Fresh 田 compressed OK, 攵 fails.
- **p3_char_0433_要** — Non-deviation. 西 top + 女 bottom. 女 unmastered.

### FAIL (retry channel, 3 items — 疖/亨/声 continuing; NOT terminal)

- **p3_char_0304_疖** (retry_2, FAIL) — B9 leak candidate, B10 R1 FAIL
  with bank ne_sick+jie_radical, B11 R2 FAIL again. Narrow-column
  proportion drift persists per P-DEV2. B12 R3: explicit y-band hint
  (疒 in y=60-240 left 40%, 卩 in y=90-200 right 40%). Last try.
- **p3_char_0306_亨** (retry_2, FAIL) — B9 leak, B10 R1 FAIL, B11 R2 FAIL.
  3-stack proportions still drift. B12 R3: explicit y-band hint
  (亠 y=40-90, 口 y=100-170, 了 y=180-280). Last try.
- **p3_char_0315_声** (retry_2, FAIL) — B9 leak, B10 R1 FAIL, B11 R2 FAIL.
  士+尸 envelope proportion drift. B12 R3: explicit column-width hint.
  Last try.

### PASS (bank additions — see success_bank/INDEX.md rows 230-247)

14 mains promoted (no retry graduates). 4 v13 BANK_DEVIATION variants
promoted (rows 244-247). All original primitives untouched.

## B12 additions (2026-08-04, position 601)

### A (main curriculum, 1 item — ★★★ FIRST-EVER A FOR G3 ★★★)

- **p3_char_0434_畎** — 畎 (quǎn), 9 strokes = 田 (5) + 犬 (4). L-R
  composition. Verdict provenance: judgments/batch_B12/labels.json att1
  → G3 → A. Recipe: BANK_DEVIATION (skipped bi_field_over_ji + da_char);
  fresh `quan_tian_for_LR_left` + `quan_dog_for_LR_right`. Explicit
  x-slot decomposition + shared-pixel cross-apex + thin uniform ink.
  Codified as **P-DEV4** compression pathway. Promoted rows 248-250.

### PASS (main curriculum, 6 items)

- **p3_char_0447_信** — 亻 + 言 (inline yan_speech_inline). PASS.
- **p3_char_0448_疥** — bank ne_sick + inline 介. PASS.
- **p3_char_0455_相** — bank mu + inline 目 (3-inner-heng). PASS.
- **p3_char_0457_思** — BANK_DEVIATION inline 田-top + inline 心-bottom.
  PASS.
- **p3_char_0465_选** — BANK_DEVIATION inline 辶-compact + inline 先.
  PASS.
- **p3_char_0479_保** — bank ren_pang + bank kou + bank mu (3-bank
  identity-alias). PASS.

### C (main curriculum, 14 items — retry candidates for B13)

- **p3_char_0437_种** — 禾+中. BANK_DEVIATION (skipped mu). Fix: promote
  a compressed 禾-left variant if a second cousin appears; for now
  inline with slant-heng-top + shu + na-becoming-dian left-radical
  form.
- **p3_char_0438_畐** — 一+口+田 vertical stack (no dev). Proportion
  drift on middle 口 too small. Fix: bump 口 to same width as 田 below.
- **p3_char_0441_前** — BANK_DEVIATION (skipped yue + dao_pang). 前 has
  fused 月+刂 bottom. Fix: try inline with slightly wider 月-with-刂
  attached at right shu.
- **p3_char_0445_点** — BANK_DEVIATION (skipped zhan_char baked-into-
  亻+占). Fix: inline 占 (卜 over 口) + explicit 4-dot 灬 bottom band
  at y=240-275.
- **p3_char_0451_给** — 纟+合. BANK_DEVIATION (si_zi_pang baked). Fix:
  compressed inline 纟 (2-scoops-tapered + 提) at x=40-100 + bank kou
  inside 合 recipe on right. **RANK 3 retry candidate.**
- **p3_char_0463_神** — 礻+申. BANK_DEVIATION (shen_extend canvas-abs).
  Fix: inline compressed 申 in right slot; adapt jia_first's shu-below
  topology to shu-through. **RANK 5 retry candidate.**
- **p3_char_0466_盃** — 不+皿 stack. BANK_DEVIATION (bu_char and
  min_dish both fail slot). Fix: promote inline compressed 皿-bottom;
  4-vertical grid at y=180-260. **RANK 6 retry candidate.**
- **p3_char_0467_结** — 纟+吉. BANK_DEVIATION (si_zi_pang). Fix: same
  纟 fix as 给 + bank shi_male (士) + bank kou vertical for 吉.
  **RANK 4 retry candidate.**
- **p3_char_0468_盅** — 中+皿. BANK_DEVIATION (min_dish module-level).
  Fix: same 皿-bottom variant as 盃.
- **p3_char_0470_侶** — 亻+呂 (口+口 stack). Fix: bank ren_pang + 2
  stacked bank kou at kou_scale ≈ 0.55, tighter vertical gap.
  **RANK 7 retry candidate.**
- **p3_char_0474_係** — 亻+系 (7-stroke 系). Fix: bank ren_pang +
  inline 系 with top-scoop + 幺-body carefully rendered. **RANK 8
  retry candidate.**
- **p3_char_0475_战** — 占+戈 (right X-crossing). 戈 is X-crossing
  family. Might be P-DEV4-eligible if compressed enough. Try in
  B13 as ambitious A candidate.
- **p3_char_0482_俎** — 仌+且. BANK_DEVIATION (bing_ren math-coords).
  Fix: inline compressed 仌 + bank ri-like for 且.
- **p3_char_0483_草** — 艹+早 (no dev). 早 = 日+十. Fix: bank cao_zi_tou
  + bank ri + bank shi_male-lookalike (十).

### FAIL (main curriculum, 31 items — abbreviated per cluster in sandbox)

- **p3_char_0435_看** — 手+目. 手 unmastered.
- **p3_char_0436_畏** — 田+ﾋ-hooked. Novel bottom.
- **p3_char_0439_将** — 爿+夕+寸. Multi-piece.
- **p3_char_0440_畑** — 火+田 L-R. 火 unmastered as left.
- **p3_char_0442_乹** — 乾-variant. Complex.
- **p3_char_0443_面** — 3-段 stack. P-DEV2 fail.
- **p3_char_0444_疣** — 疒+尤. Interior novel.
- **p3_char_0446_疤** — 疒+巴. Interior novel.
- **p3_char_0449_美** — 羊+大 stack. 羊 unmastered + X-crossing bottom.
- **p3_char_0450_疫** — 疒+殳. Interior novel.
- **p3_char_0452_疬** — 疒+力. Interior novel.
- **p3_char_0453_度** — 广+又+又. 3-piece.
- **p3_char_0454_疭** — 疒+从. Interior X-crossing.
- **p3_char_0456_疮** — 疒+仓. Interior novel.
- **p3_char_0458_癸** — 癶+天. Novel top + X-crossing.
- **p3_char_0459_带** — 共-top + cloth-bottom. Novel body.
- **p3_char_0460_皅** — 白+巴. 巴 novel.
- **p3_char_0461_亲** — 立+木-hanging. Composition drift.
- **p3_char_0462_皈** — 白+反. 反 novel.
- **p3_char_0464_侯** — 亻+侯-body. Body novel.
- **p3_char_0469_便** — 亻+更. 更 novel.
- **p3_char_0471_总** — 忄+悤. Novel top.
- **p3_char_0472_侷** — 亻+局. 局 novel.
- **p3_char_0473_城** — 土+成. 成 X-crossing.
- **p3_char_0476_俅** — 亻+求. 求 novel.
- **p3_char_0477_南** — 十+冉-body. Body novel.
- **p3_char_0478_俉** — 亻+吾. 吾 = 五+口, 五 novel.
- **p3_char_0480_俊** — 亻+夋. 夋 novel.
- **p3_char_0481_济** — 氵+齐. 齐 X-crossing bottom.

### FAIL / TERMINAL_FROZEN (retry channel, 3 items)

- **p3_char_0304_疖** (retry_3 → **C**) — B9 leak. Trajectory
  main→R1→R2→R3: FAIL→FAIL→FAIL→C. All hints applied (BANK_DEVIATION
  + Q1/Q2/Q3 + TRAJECTORY DIFF + explicit y-bands + column widths).
  Envelope OK, 卩 finally legible; panel: not-quite-PASS. **TERMINAL_FROZEN.**
  Joins terminal pool with 人/入/大/矢/失/匕. Recipe preserved in
  attempts/p3_char_0304_疖__retry_3/.
- **p3_char_0306_亨** (retry_3 → **FAIL**) — B9 leak. FAIL→FAIL→FAIL→FAIL.
  y-band hints applied but 了-hook curl still non-discriminable from
  子/子-like tails. **TERMINAL_FROZEN.**
- **p3_char_0315_声** (retry_3 → **FAIL**) — B9 leak. FAIL→FAIL→FAIL→FAIL.
  士 middle 竖 rendered outside discriminable region despite explicit
  fix-promise. **TERMINAL_FROZEN.**

Terminal-freeze pool after B12: **人, 入, 大, 匕, 矢, 失, 疖, 亨, 声**
(9 items). Composition-retrieval-leak hypothesis fully falsified —
retrieval channel works but format ceiling holds for narrow-column,
3-stack, and stacked-envelope compositions.

## B13 additions (2026-08-05, position ~651)

### PASS (main curriculum, 10 items)

- **p3_char_0489_指** — 扌+旨. BANK_DEVIATION (skipped shou_pang turtle);
  inline `zhi_finger_inline`. PASS. Not promoted.
- **p3_char_0492_俚** — 亻+里. BANK_DEVIATION (skipped ren_pang turtle);
  inline `ren_pang_pil_for_LR_left`. PASS. **PROMOTED row 251.**
- **p3_char_0493_适** — 辶+舌. BANK_DEVIATION (skipped zou_zhi turtle +
  hua_speak pointer); inline `shi_go_char_inline` (envelope + interior).
  PASS. Envelope portion **PROMOTED row 252** (`zou_zhi_thin_pil_envelope`).
- **p3_char_0497_响** — 口+向. No BANK_DEVIATION. Bank-clean. PASS.
- **p3_char_0507_高** — 亠+口+冂+口 tower. BANK_DEVIATION (skipped
  tou_radical + kou for sizing); inline. PASS. Not promoted (whole-char).
- **p3_char_0515_原** — 厂+白+小. BANK_DEVIATION (skipped chang +
  bai_char_for_top_stack for weight mismatch); inline. PASS. Not promoted.
- **p3_char_0516_疰** — 疒+主. No BANK_DEVIATION. `ne_sick` + inline 主. PASS.
- **p3_char_0522_疴** — 疒+可. No BANK_DEVIATION. `ne_sick` + inline 可. PASS.
- **p3_char_0524_疸** — 疒+旦. No BANK_DEVIATION. `ne_sick` + inline 旦. PASS.
- **p3_char_0530_痂** — 疒+加. No BANK_DEVIATION (no bank for 加).
  `ne_sick` + inline 加. PASS.

### C (main curriculum, 11 items — retry candidates for B14)

- **p3_char_0484_俏** — 亻+肖. Mixed coord systems (ren_pang turtle + PIL
  right). Fix: use new `ren_pang_pil_for_LR_left` + inline PIL 肖 uniformly.
- **p3_char_0486_俐** — 亻+利 (3-column 亻|禾|刂). BANK_DEVIATION.
  Fix: tighter 3-column layout + new `ren_pang_pil_for_LR_left`.
- **p3_char_0499_能** — 厶+匕 top / 月+匕 bottom. BANK_DEVIATION
  (yue_for_neng_BL). Near-miss. Fix: thinner ink; sharper bottom-匕 curl.
  **RANK 1 retry candidate.**
- **p3_char_0503_都** — 者+阝 L-R. BANK_DEVIATION. Fix: adapt 阝 from 那.
  **RANK 4 retry candidate.**
- **p3_char_0504_畛** — 田+㐱 L-R. BANK_DEVIATION (skipped shan_radical).
  Uses new `quan_tian_for_LR_left`. Fix: 㐱 needs explicit 人-apex + 3
  cascading pies with clearer separation.
- **p3_char_0506_畜** — 亠+幺+田 3-stack. BANK_DEVIATION. Fix: explicit
  y-bands per piece (P-DEV2 rule for 3+-stacks).
- **p3_char_0510_畟** — 田-over-夊 (splayed base). BANK_DEVIATION
  (sui_bottom_for_ji fresh). Fix: 夊 splay-arm needs longer 捺 crossing right.
- **p3_char_0525_部** — 咅+阝 L-R. BANK_DEVIATION. Fix: same 阝 recipe as 都.
  **RANK 6 retry candidate.**
- **p3_char_0526_疹** — 疒+㐱. No BANK_DEVIATION (envelope OK). Fix:
  interior 㐱 needs apex-kissed 人-top + 3 cascading pies clearer.
  **RANK 3 retry candidate.**
- **p3_char_0528_疽** — 疒+且. No BANK_DEVIATION (envelope OK). Fix:
  interior 且 as compact 5-stroke rectangle in belly slot.
  **RANK 2 retry candidate.**
- **p3_char_0532_亳** — 亠+口+冖+乇 4-stack. BANK_DEVIATION. Fix: explicit
  y-band per piece. **RANK 5 retry candidate.**

### FAIL (main curriculum, 29 items — abbreviated)

- **p3_char_0485_怎** — 乍+心 stack. Novel bottom, cluttered.
- **p3_char_0487_孩** — 子+亥 L-R. 亥 novel.
- **p3_char_0488_俑** — 亻+甬. 甬 novel.
- **p3_char_0490_俘** — 亻+孚. 孚 novel.
- **p3_char_0491_除** — 阝+余. 除 topology drift.
- **p3_char_0494_俛** — 亻+免. 免 novel.
- **p3_char_0495_复** — top+日+夊 3-stack. Content-gap.
- **p3_char_0496_俜** — 亻+甹. 甹 novel.
- **p3_char_0498_俞** — 亼+一+月/刂 3-stack. Novel top.
- **p3_char_0500_丵** — dense vertical char. Novel body.
- **p3_char_0501_家** — 宀+豕. 豕 novel.
- **p3_char_0502_畚** — 亠+ム+田 3-stack. Content-gap.
- **p3_char_0505_起** — 走+己. 走 novel.
- **p3_char_0508_畝** — 亩+攵 (or 畝 archaic). 攵 novel (same fail as 畋).
- **p3_char_0509_特** — 牜+寺. 牜 unmastered.
- **p3_char_0511_海** — 氵+每. 每 novel.
- **p3_char_0512_畢** — 田+華-bottom. Novel bottom.
- **p3_char_0513_通** — 辶+甬. 甬 novel — sibling for `zou_zhi_thin_pil_envelope`.
- **p3_char_0514_乘** — dense stack. Novel body.
- **p3_char_0517_真** — dense hengs stack. Novel body.
- **p3_char_0518_疱** — 疒+包. 包 novel.
- **p3_char_0519_候** — 亻+侯-body. Novel body.
- **p3_char_0520_疳** — 疒+甘. 甘 novel-simple.
- **p3_char_0521_验** — 马+佥. 马 unmastered.
- **p3_char_0523_被** — 衤+皮. Both novel.
- **p3_char_0527_造** — 辶+告. 告 novel (sibling for `zou_zhi_thin_pil_envelope`).
- **p3_char_0529_热** — 执+灬 U-D. Novel top.
- **p3_char_0531_速** — 辶+束. 束 novel (sibling for `zou_zhi_thin_pil_envelope`).
- **p3_char_0533_值** — 亻+直. 直 novel-simple.

### Retry channel (8 R1s → 1 PASS, 3 C, 4 FAIL)

- **p3_char_0466_盃__retry_1** — **PASS** (recovery). Recipe: 不 + inline
  compressed 皿-bottom. Not variant-promoted (single instance).
- **p3_char_0463_神__retry_1** — **C**. 礻+申. Interior 申 still not
  quite right. R2 candidate (defer to B15).
- **p3_char_0470_侶__retry_1** — **C**. 亻+呂. Bank ren_pang + 2 stacked
  kou; slot alignment off. R2 candidate.
- **p3_char_0474_係__retry_1** — **C**. 亻+系. Interior 系 top-scoop off.
  R2 candidate.
- **p3_char_0430_畈__retry_1** — **FAIL**. 田 clean via new bank primitive,
  but 反 collapsed to a curl. **Variant post-mortem in sandbox.md** —
  led to P-DEV5 (sibling-slot verification rule).
- **p3_char_0432_畋__retry_1** — **FAIL**. Same story: 田 clean, 攵 broken.
  Both 反 and 攵 are content-gap X-crossing family with no bank recipe.
  Not queued for R2 per P-DEV5.
- **p3_char_0451_给__retry_1** — **FAIL**. 纟 still not decoded.
- **p3_char_0467_结__retry_1** — **FAIL**. Same 纟 issue.

Terminal-freeze pool after B13: **人, 入, 大, 匕, 矢, 失, 疖, 亨, 声**
(9 items, unchanged from B12; 畈/畋 not frozen — content-gap, not
format-ceiling; they may re-enter the queue once a 反/攵 recipe exists).
