# 错题集 — G3 (coord-bank)

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
