# 错题集 — G3 (coord-bank)

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
