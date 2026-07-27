# Sandbox — G3 (coord-bank)

Sandbox reset with Phase-2 restart. Persistent free-form memory — use
for observations that don't cleanly fit the Principle Bank.

## Carry-over notes from Phase-1

- All stroke primitives assume a 300x300 canvas and math-coord
  convention (center origin, +y up). If drawing on a different canvas,
  either compose on a fresh 300x300 and paste, or refactor `_to_pixel`
  to accept canvas size.
- `heng.py`, `shu.py`, `pie.py`, `na.py`, `dian.py`, `ti.py` are the
  cleanest bank entries — pure single-line or single-bezier
  definitions. Prefer these as composition primitives.

## Bootstrap batch (2026-07-17) — failure-mode analysis

Four radicals from bootstrap batch (positions 33–50) failed. Common
thread: **rounded, continuous, enclosing shapes** modeled with
straight-line + right-angle recipes. Coord-format bank has no arc
primitive, and drawers keep reaching for `heng` + `shu` + hook when
the target is one continuous curved envelope.

### p2_radical_010_勹 (bao) — FAIL

- Attempt: separate 撇 + 横折钩 rendered with SHARP right-angle corner.
- GT: one continuous smooth rounded envelope (like a bag). The
  horizontal top and the descending stroke are joined by a rounded
  arc, NOT a right angle. The 撇 head sits well left of the top.
- Failure mode: the bank's `heng_zhe_gou` primitive was rejected as
  "aspect mismatch", then a right-angle inlined recipe was used —
  losing exactly the roundedness that makes 勹 read as 勹.
- Fix for retry: draw the 横+折+钩 as ONE bezier (top-left horizontal
  head, smoothly curving down through the top-right shoulder, then
  descending vertically with slight leftward bow, ending in a
  hook). No sharp corner. See errata.

### p2_radical_011_匕 (bi) — FAIL

- Attempt: pie + shu_wan_gou. The pie crossed the shaft.
- GT: the vertical of 匕 has a strong horizontal-bottom (a proper
  竖弯 with long horizontal foot then hook up) — this the render
  captured. But the top of 匕 needs a 撇 that starts high-left,
  descends to meet the shaft, THEN a short horizontal 提 shoots
  up-right OFF the shaft. The render has 撇 crossing shu_wan_gou
  ABOVE the shaft top — reads as `匕` broken up top.
- Failure mode: 匕 is 撇 + 竖弯钩 where the pie ENDS at the shaft
  (joint), and the top-right "提" is really the head of the 竖弯钩
  (short pointed head before it descends). No composition in the
  bank captures this junction.
- Fix: shorten pie, land its tail on the shu_wan_gou shaft top; make
  shu_wan_gou's shaft top slightly rightward-scooping so it reads as
  the crossing arm. See errata.

### p2_radical_014_厂 (chang) — FAIL

- Attempt: heng shifted right + inline "pie" that curved as an arch
  going UP-then-LEFT (like a shepherd's crook). Result reads as ONE
  curving shape, not 厂.
- GT: a plain flat horizontal at the top + a straight-ish pie
  descending straight down from the LEFT end (only slight curl at
  the bottom). Two distinct strokes with a hard corner-join.
- Failure mode: the drawer picked a bezier control point that pulled
  the pie head LEFT of the heng end and DOWN, creating an arc
  instead of a mostly-vertical straight descent.
- Fix: reuse `heng` at scale ~0.65 centered high; draw pie as almost-
  vertical with only a shallow scoop near the tail (control point on
  the chord's midpoint, not offset left). Head anchored at heng's
  left end (weld). See errata.

### p2_radical_015_刀 (dao) — FAIL

- Attempt: heng_zhe_gou (right side) + pie (left side), both scaled
  down and separated with a visible gap at the top. Reads as 刂 or 刁
  with the top disconnected.
- GT: 刀 has 横折钩 whose top-horizontal spans WIDE across the upper
  portion, and the 撇 CROSSES the horizontal — its head starts above
  and to the right of the horizontal's midpoint, then sweeps down-
  left through the horizontal, exiting below-left. This crossing is
  what distinguishes 刀 from 刁.
- Failure mode: drawer welded the pie head to the horizontal's LEFT
  END, not letting it cross. Also, heng_zhe_gou at scale 0.55 gave
  the top a right-angle look rather than the softer rounded corner
  the GT shows.
- Fix: increase heng_zhe_gou scale (~0.8) so the top spans more of
  the canvas; place pie head ABOVE the horizontal (math y +75) with
  tail below-left the horizontal, so the two strokes CROSS. See errata.

## Batch B1 diagnostic — persistent G3 underperformance (2026-07-18)

**G3 finished B1 at 54% pass (27/50), worse than G1 no-memory (60%).
This is the SECOND consecutive batch of underperformance vs. control.**
Bootstrap: G3 78% vs G1 84%. B1: G3 54% vs G1 60%.

G3-unique fails this batch (items where G1/G2/G4 all PASSed but G3
FAILed): **丷, 讠, 屮, 大**.

### Diagnosis by category — 23 B1 fails

**A. Would likely have PASSed if drawn G1-style (fresh, no primitive).**
Primitive-reflex or force-fit was the failure cause; a fresh inline
bezier tuned to the target would have been simpler and more correct.

- **p2_radical_046_大 (dà)** — heng + pie + na all called from bank.
  The pie primitive's diagonal chord fought 大's required vertical-
  peak-with-crossing geometry; the head sat too high off the heng.
  G1 would have drawn 3 tapered beziers tuned to the target apex.
- **p2_radical_028_人 (rén)** — pie + na from bank at scale 0.9.
  The primitives' diagonal chord + head positions couldn't produce
  the two-strokes-KISS-AT-APEX geometry cleanly; heads ended up
  offset from each other.
- **p2_radical_030_入 (rù)** — same failure as 人: pie + na force-fit.
  The primitive's fixed head-at-corner-of-bounding-box logic can't
  represent "na head STARTS on pie shaft midway" — a fresh bezier
  starting at pie's u=0.3 anchor would have worked.
- **p2_radical_020_阝 (fù)** — attempted inlined loop but the "ear"
  is one continuous rounded stroke that G1 could bezier cleanly.
  G3 spent tokens deciding whether to reuse `heng_pie_wan_gou`.
- **p2_radical_061_女 (nǚ)** — 3-stroke radical with distinctive
  crossing 撇 and 横. Primitive-first thinking led to a stacked-and-
  crossed heng+pie+heng that didn't read as 女.
- **p2_radical_062_犭 (quǎn)** — 3-stroke curved animal-radical.
  Bank has no matching curl; force-fit primitives distorted it.
  G1 would draw one continuous curl bezier plus a dian.
- **p2_radical_059_门 (mén)** — 3-stroke door frame with distinctive
  hooks. Force-fit heng_zhe_gou at compressed scale flattened the
  hook. Fresh 3 hand-tuned strokes likely simpler.
- **p2_radical_041_彳 (chì)** — two 撇 stacked + shu. Pie primitive's
  diagonal chord too steep; small stacked pie needs shallower slope.
- **p2_radical_042_巛 (chuān)** — 3 wavy verticals. Bank has no wavy
  primitive; forced `shu` variations couldn't capture the wave.
- **p2_radical_058_马 (mǎ)** — 3 strokes with a distinctive box +
  bottom curl. Bank had no matching curl.
- **p2_radical_050_弓 (gōng)** — 3-stroke bow shape with double curl.
  Force-fit heng_zhe + shu_wan couldn't produce the bow silhouette.
- **p2_radical_053_己 (jǐ)** — 3 strokes forming a low "3"-like shape.
  Force-fit primitives didn't preserve the bottom curl-up.
- **p2_radical_055_彑 (jì)** — same family as 彐 (which PASSed via
  full inlining). This attempt used primitive-based approach and
  failed. Lesson: 彐's PASS via full inline is the right template.
- **p2_radical_056_巾 (jīn)** — 竖 + 横折钩 + 竖. Primitive-first
  gave wrong proportions between the frame and the internal 竖.
- **p2_radical_036_廴 (yǐn)** — 2-stroke swoosh (dian + long 弯钩).
  Force-fit bank primitives couldn't capture the sweeping 弯 tail.
- **p2_radical_038_㔾 (jié_variant)** — small hook-radical; primitive
  force-fit made corners too sharp.
- **p2_radical_047_飞 (fēi)** — 3 strokes including a distinctive
  hook. Force-fit heng_gou lost the curl.
- **p2_radical_040_屮 (chè)** — G3-unique fail. Used draw_shu twice
  + inlined 竖折. The two shu calls at radically different scales
  (0.95 vs 0.32) produced arms of visually-incompatible width
  because P4 says stroke thickness is stroke-specific and shu is
  tuned for standalone width. INLINE both verticals fresh with
  matched widths would have PASSed.
- **p2_radical_025_力 (lì)** — 2 strokes (横折钩 + 撇). Force-fit
  heng_zhe_gou primitive at radical scale + bank pie together read
  as disconnected. Inline as one composite stroke would work.

**Sum: ~18 of the 23 fails are primitive-reflex failures.** These are
the cases where the INLINE-FRESH TEST (new TR8) would have redirected
the drawer to a working solution.

**B. Genuinely hard (all groups likely failed) — inline-fresh wouldn't
have saved these.**

- **p2_radical_021_丷 (unique fail, but drawer DID inline)** — mirror-
  pair of tapered dots. Inlined bezier didn't render as recognizable
  "two dots slanting inward". Failure is in the bezier design itself,
  not primitive-reuse. Fix idea: use draw_dian for right dot, and
  inline a left-mirrored variant sharing dian's exact width profile.
- **p2_radical_035_讠 (unique fail, drawer used dian_radical + inlined
  heng_zhe_ti)** — the inlined compact 横折提 didn't read as one
  continuous stroke; the 折 and 提 corners were visually detached.
  Failure is inline-recipe geometry, not primitive-reuse.
- **p2_radical_024_冂 (already retry-PASSed)** — no additional fix.
- **p2_radical_032_厶 (sī)** — small pie + dian + curl. Curl geometry
  is inherently subtle at small scale; may be a rendering-fidelity
  ceiling of the format.

### Root cause hypothesis

**G3's coord-format bank encourages a "bank-first search" cognitive
loop**: on seeing a new radical, the drawer scans `INDEX.md` and picks
primitives that "kind of fit", then chooses (ox, oy, scale) to force
them into position. This is faster than deriving fresh but locks in
the WRONG shape when the primitive's standalone geometry doesn't match
the composition's needs. G1 (no memory) has no such loop — it just
draws what the target shows, which turns out to be more accurate more
often at this stage.

### Principle added to prevent this next batch

**TR8 (see principle_bank.md)** — The INLINE-FRESH TEST. Before every
primitive call, mentally ask "how would G1 draw this fresh?" and compare
to what the primitive at (ox, oy, scale) would emit. Only use the
primitive if its standalone shape matches the target after simple
uniform scaling. Otherwise inline fresh.

**TR9 (see principle_bank.md)** — Bank-size discipline. With 66+
primitives, resist "there must be one for this". Decide the target's
shape first (as G1 would), then check the bank.

### Watch for B2 (positions 101–150)

- Track fails: are they still ~18/25 primitive-reflex? Or has TR8
  redirected them? If TR8 works, expect the fail count to drop and
  the remaining fails to be genuinely-hard (category B) items.
- If B2 STILL underperforms G1, the bank-format itself may be the
  problem, not the discipline around it. Escalate to a wholesale
  bank reset (like Phase-2 restart).

## B1 fail summaries (per-item, for errata)

### p2_radical_020_阝 (fù) — FAIL
Force-fit + partial inline of the "ear" loop; ended up reading as an
irregular blob attached to a vertical. Retry: fully inline the loop as
one bezier with two smooth bumps; keep shu for descender.

### p2_radical_021_丷 (bā_top) — FAIL (G3-unique)
Two inlined mirror-dots; slants read as thin diagonals rather than
solid dots. Fix: use bank `dian` for right dot (rotated 0°), inline a
mirrored `dian` with the same width profile for left dot; both at
scale 0.5.

### p2_radical_024_冂 (jiōng) — FAIL
Enclosing frame with rounded top corners. Force-fit heng + shu +
right-shu produced sharp corners. Retry idea from bootstrap sandbox:
inline as ONE continuous 横折+shu tuple with rounded elbow.

### p2_radical_025_力 (lì) — FAIL
Force-fit heng_zhe_gou + pie. Corners disconnected. Inline: one
continuous 横折钩 with pie head touching at horizontal midpoint.

### p2_radical_028_人 (rén) — FAIL
Force-fit pie+na primitives — heads didn't kiss cleanly at apex. Fix:
inline both as tapered beziers sharing an exact apex pixel.

### p2_radical_030_入 (rù) — FAIL
Same as 人 but with na starting mid-shaft on pie. Primitive can't
express "head on another stroke's u=0.3". Inline both as fresh beziers.

### p2_radical_032_厶 (sī) — FAIL
Small pie + dian + terminal curl. Curl too small to render cleanly.

### p2_radical_035_讠 (yán) — FAIL (G3-unique)
Compact 横折提 corners visually detached. Fix: draw the compound as
one continuous tapered polyline with 顿笔 blobs, not as three
independent segments.

### p2_radical_036_廴 (yǐn) — FAIL
Long sweeping 弯钩 tail; force-fit primitive lost the sweep. Inline
as one long bezier with taper.

### p2_radical_038_㔾 (jié_variant) — FAIL
Sharp-corner hook radical; corners too sharp. Round the elbow.

### p2_radical_040_屮 (chè) — FAIL (G3-unique)
Two shu calls at incompatible scales (0.95 vs 0.32) — width mismatch
made the arms read as different characters. Inline both verticals with
matched ink widths.

### p2_radical_041_彳 (chì) — FAIL
Two stacked 撇 + long 竖; pie primitives at compressed scale sat at
wrong slope. Inline both 撇 with shallower slope.

### p2_radical_042_巛 (chuān) — FAIL
Three wavy verticals. No wavy primitive; force-fit shu straight.
Inline as three separate tapered sine-ish curves.

### p2_radical_046_大 (dà) — FAIL (G3-unique)
heng + pie + na all from bank; heads didn't converge properly on the
heng. Inline all three with hand-chosen crossing pixel.

### p2_radical_047_飞 (fēi) — FAIL
Distinctive hook lost in force-fit heng_gou. Inline the hook fresh.

### p2_radical_050_弓 (gōng) — FAIL
Bow shape with double curl; force-fit heng_zhe + shu_wan. Inline as
one bezier path with two curl inflections.

### p2_radical_053_己 (jǐ) — FAIL
Low "3"-like with terminal curl-up; force-fit lost the curl. Inline.

### p2_radical_055_彑 (jì) — FAIL
Same family as 彐 (which PASSed via full inline). Retry: use 彐's
inline template with different arm proportions.

### p2_radical_056_巾 (jīn) — FAIL
竖 + 横折钩 + 竖. Frame proportions off vs internal 竖. Inline all
three with correct relative widths.

### p2_radical_058_马 (mǎ) — FAIL
Box + bottom curl; no matching curl primitive. Inline curl.

### p2_radical_059_门 (mén) — FAIL
Door frame; force-fit heng_zhe_gou flattened the hook. Inline all
three strokes matching the sharp GT geometry.

### p2_radical_061_女 (nǚ) — FAIL (G3-unique)
Crossing 撇 + 横 didn't read as 女. Inline: 撇 first, then heng
crossing it at a specific x on the pie's u=0.5.

### p2_radical_062_犭 (quǎn) — FAIL
Continuous animal curl; no matching primitive. Inline as one bezier
+ dian.

## Meta-lesson from bootstrap FAILs

Three of four fails (勹, 厂, 刀) involve **junction/composition
geometry** that the bank can't express. The bank has good single-
stroke primitives but no "curve smoothly between primitives"
mechanism — every join is either a weld (endpoint-to-endpoint) or a
crossing (default overlay). For rounded envelopes (勹) and for
cross-junctions (刀's crossed pie) the drawer must inline. When the
target's silhouette contains a smooth curve that a straight-line
`heng` + right-angle `heng_zhe_gou` combination cannot approximate,
INLINE a bezier — do not force the composition.
