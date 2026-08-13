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

## Batch B2 diagnostic — signature restriction hypothesis (2026-07-18)

**G3 collapsed to 34% in B2 (17/50). Bootstrap → B1 → B2: 78% → 54%
→ 34%. Cumulative 49% through 118 items — WORST of the four groups.
All 8 retries failed (retry_1s for 人, 入, 大, 女, 犭, 己, 㔾, 丷).**

### Diagnosis (root cause, not the symptom)

TR8 INLINE-FRESH TEST was added at end of B1 to force drawers away
from primitive-reflex. Drawers largely complied in B2 (most B2
attempts contain "inline-fresh" comments and reason explicitly about
whether primitives fit). Yet the pass rate DROPPED further.

The failure is no longer "drawer force-fit a bad primitive". The
failure is that even when the drawer inlines fresh:

1. Each inlined stroke is a one-off hand-tuned bezier the drawer
   invented from scratch — no bank memory helps.
2. When a bank primitive IS a shape match (e.g. `dian` for 忄's left
   dot), it can't produce the mirrored right dot because the signature
   `(ox, oy, scale)` supports only uniform rescaling — not angle
   reflection, taper variation, or curvature bow.
3. The `principle_bank.md` TR1-TR9 rules are all META ("call
   primitives deliberately") — they tell the drawer *when* to reach
   for the bank but not *what stroke form fits where*.
4. Success Bank entries are frozen concrete instances (e.g. `kou.py`
   only draws 口 at one exact aspect ratio). When 日 needs a tall
   version, the drawer has no way to derive it from the frozen
   instance — it has to inline from scratch.

**User diagnosis** (verbatim from Curator brief): "The problem isn't
they don't know the strokes, but rather how to change them into the
proper form or put them into the correct position. There are many
types of 点, 撇, they all look different and have different angles.
Memory is restricting them too much."

This confirms the signature-restriction hypothesis. The right response
is not another meta-cognitive rule (TR10 would just add noise). It is
to add EXPRESSIVE POWER to the memory format itself, within G3's
callable-Python constraint.

### v7 memory restructuring (see evolution.md 2026-07-18 @ position 150)

Curator response for B2 → B3 transition:

1. **Split `principle_bank.md`** by knowledge type:
   - `principles_meta.md` — TR1-TR7 (retire TR8-TR9, which fired but
     didn't help)
   - `principles_stroke_family.md` — P1-P11 (P11 new: adaptive-signature
     rationale)
   - `form_catalog.md` — NEW: stroke × context lookup (e.g.
     "撇 in left-radical position: length 60-90px, angle 70-85° from
     horizontal, w_head 8, w_tail 1, bow_perp -4 to -8")
2. **Add adaptive helpers** in `success_bank/code/_shared_helpers.py`:
   `variant_pie(t, head, tail, bow_perp, w_head, w_tail)`,
   `variant_na(...)`, `variant_dian(...)`. These expose the knobs the
   `(ox, oy, scale)` signature hides. Callable Python — G3 core
   constraint preserved.
3. **Retire TR8 / TR9** — TR8 was added at end of B1 to save the
   primitive-reflex fails. In B2 drawers complied but the fails
   continued (root cause was deeper: signature restriction). TR9
   "budget your reach" never fired usefully. Both removed with a
   documented rationale in `evolution.md` so we can compare B3 with
   and without.
4. **Reshape `memory_index.md`** to point drawers at
   `form_catalog.md` FIRST for stroke-in-context lookup, then the
   variant helpers, then the frozen bank entries, then the meta rules
   last. Reverses the previous read order (which put meta first).

### Watch for B3 (positions 151–200)

- Fail count: does splitting principle_bank + adaptive helpers reduce
  fails from 33/50 to <20/50?
- Look at whether drawers actually invoke `variant_pie` /
  `variant_dian` (grep new B3 attempts for import lines).
- If B3 still 30%+ fail: the constraint may be even deeper — perhaps
  bank entries should be parameterised by context tags (top / bottom /
  left / right / enclosing) at storage time, not just at call time.

### Signature-restriction fails in B2 (specifically primitives-with-
### uniform-rescale-only)

- 077_忄: mirrored dot needed reflection, not scale.
- 083_丬: dian at compact position too heavy (default weight profile).
- 100_见: box needed non-uniform aspect (tall).
- 112_欠: 横钩 primitive's x-span fixed at 190px regardless of scale.
- 098_火: pie/na apex-kiss needs shared apex pixel (primitive can't).
- 113_犬: same as 火 (犬 = 大 + dian).
- 117_手: extension of 扌 needs an added top 撇 that shou_pang can't
  express.
- 088_长: 捺 sweep needs bow_perp that primitive can't vary.

These 8 fails are ALL signature-restriction, not knowledge gaps.
Fixing the signature (adaptive helpers) directly addresses them.

### B2 fails where problem is DEEPER than signature (composition
### structure lost)

- 094_风: envelope curvature must be one continuous bezier — no
  helper alone fixes; need a composed helper (`variant_envelope`
  possibly, future work).
- 091_斗: two dots' relative placement is an alignment problem,
  not a per-dot form problem — needs composition memory (also future).

## Meta note (v7 memory evolution first use)

This is the first time G3's curator has used the v7 self-evolution
unlock. Chose to split principle_bank + add adaptive helpers rather
than radically restructure (e.g. converting Success Bank to markdown)
because:
- The callable-Python constraint is the point of G3 as a group.
- Adaptive helpers work WITHIN the callable-Python constraint — they
  add expressive knobs without changing the storage unit.
- Splitting principle_bank is a low-risk cleanup that reduces
  retrieval noise (287-line wall of meta-rules → 3 focused files).
- form_catalog.md is a NEW file type — its usefulness will be
  measurable at B3 judgment (do drawers cite it? does citing it
  correlate with PASS?).

If B3 still underperforms G1, the next lever will be more radical:
either (a) auto-generate form_catalog entries from every PASS as a
context-tagged parameterised recipe, or (b) reorganise bank
subdirectories by position role (`code/left_position/`,
`code/top_position/`, etc.) so drawers can find "the 撇 that fits
here" by directory walk rather than name guess.

## Batch B3 diagnostic (2026-07-22) — helpers used but retries still 0/13

### Numbers
- Main: 29/50 = 58% PASS (recovery from B2's 34%, aided by easy
  Phase-3 chars which alias to bank primitives).
- Retries: 0/13 = 0% PASS.
- Cumulative through position 200: 52%. G1 no-memory: 54%. G3 still
  below control.

### Helper-usage investigation (grep of retry generated.py)

7 of 13 retries USED the new variant helpers:
  - 077_忄 → variant_dian (both dots)
  - 083_丬 → variant_dian, variant_pie
  - 088_长 → variant_pie, variant_na (for the sweep)
  - 100_见 → variant_pie
  - 021_丷 → variant_dian (both dots)
  - 025_力 → variant_pie
  - 113_犬 → variant_pie, variant_na, variant_dian

6 of 13 did NOT use helpers (015_刀 retry_2, 028_人 retry_3,
030_入 retry_3, 046_大 retry_3, 098_火, 117_手) — those drawers
went inline-fresh with hand-tuned recipes.

### Fail-mode breakdown (visual comparison of retry PNG vs GT)

- **Helper-used retries where fail mode SHIFTED (5/7)**: the specific
  stroke targeted by the helper improved (e.g., 忄's left dot now
  mirrored correctly), but a DIFFERENT part of the character became
  the failure mode (dot position wrong, or shaft dominates). The
  helpers do fix per-stroke form; they don't fix composition.
- **Helper-used retries where fail mode SAME (2/7)**: 025_力 and
  083_丬 — the helper was called with numbers that still didn't match
  the target. Numbers came from form_catalog rows that pointed at
  similar-but-not-identical contexts.
- **Non-helper retries (6/6 SAME fail mode)**: these are the
  X-crossing family (人, 入, 大, 刀) where the failure isn't per-stroke
  form but joint geometry — the two strokes need to share an exact
  pixel and the drawer's mental simulation is off.

### The B3 root cause (evidence-based)

**The variant helpers solve the per-stroke-form problem** (angle,
taper, mirror). They do NOT solve two other problems:

1. **Joint/composition geometry** — where two strokes must meet at
   an exact pixel (X-cross apex for 人/入/大; hook base for 力;
   crossing for 刀). The drawer knows *which* variant to call but
   still doesn't compute the shared weld pixel explicitly.

2. **Number retrieval discipline** — form_catalog has rows but the
   drawer sometimes copies numbers from a nearby context that
   doesn't quite fit (e.g. 丬 used the 忄 numbers because there's no
   dedicated 丬 row).

### Second-pass response (see evolution.md 2026-07-22)

Options considered:
  - a) Add a joint/weld helper (`compute_weld(strokeA, u)`) that
       returns the exact pixel where a second stroke should start.
       PRO: directly addresses the X-crossing fails.  CON: opens the
       "composition" door which was intentionally kept simple.
  - b) Add worked examples in form_catalog showing when to use
       variant vs frozen, with an actual code snippet per row.
       PRO: reduces "copy-from-similar-context" errors.  CON: bloats
       the catalog.
  - c) Auto-generate form_catalog entries from every PASS (each
       new PASS should trigger a catalog row automatically).
       PRO: catalog grows organically.  CON: doesn't fix retries.
  - d) Rewrite the variant helpers with the B3 fail evidence —
       especially variant_dian for mirror-pair contexts (忄, 丷, 丬).
       Fail cases show the helper's `bow_perp` sign convention is
       hard to reason about for a mirror.
  - e) Retire the retry mechanism entirely — with 0/13 PASS across
       two batches of retries, the retry loop isn't adding value.
       Replace with "if fail, add to a permanent-freeze list and
       move on".

Chosen: **b + d + a-minimal**. See evolution.md for the specific
changes made.

### Watch for B4

- Do retries move at all? If still 0/N: kill the retry mechanism (option e).
- Do X-cross fails (人, 入, 大, 犬, 火) improve with the joint-weld
  helper? If yes: the "composition" problem is real and needs its
  own toolkit.
- Do the reorganised form_catalog entries with worked examples
  reduce copy-from-similar-context errors?

## Batch B4 diagnostic (2026-07-23) — helpers exist but retries STILL don't use them

### Numbers
- Main: 27/50 = **54%** (down from B3's 58%; B2 was 34%, B1 54%, bootstrap 78%).
- Retries: **1/8 = 12%** (finally non-zero after B2 0/8 and B3 0/13).
  The lone PASS: **子** — via hand-inlined recipe with matched taper,
  NOT via kiss_apex or any B3 helper.
- Cumulative through position 250: **52%** — still ~3pp below G1 no-memory (~55%).
- G3 has now underperformed the control for FOUR consecutive batches
  (B1 -6, B2 -4, B3 -2, B4 -3). This is not a fluke; it's a structural
  gap.

### The helper-adoption finding

`grep -l "kiss_apex\|pie_point\|mirror_dian_pair" attempts/*__retry_*/generated.py`
returns **ZERO files**. Not one B4 retry imported the B3-second-pass
composition helpers.

- 夂 retry: rationale explicitly said "kiss_apex helper was designed
  to fix" — drawer wrote inline `_tb` helper instead.
- 夊 retry: same.
- 兀 retry: rationale said "pie_point helper enables explicit joint
  pixel" — drawer imported variant_pie + tapered_line only.
- 门 retry: no helper (inline tapered lines).
- 女 retry_2: inline everything.

Meanwhile 6 of 50 **main** attempts DID import kiss_apex (大, 个, 久,
亼, 夂, 及). So the retrieval works on main-curriculum prompts but
NOT on retry prompts. Hypothesis: the retry dispatcher prompt has a
heavier "fresh from GT / errata fix idea" injunction that overrides
the memory_index step-2 pointer to helpers.

### The lone retry PASS: 子

- Recipe: fully inline, hand-tuned tapered polylines. 3 strokes: top
  横撇 (thin taper 3→5 with 顿笔 blob + short pie continuation),
  vertical 弯钩 (bezier body with visible hook flick, thin ~5px), and
  crossing 一 (thin uniform 4px).
- What worked: followed errata fix idea VERBATIM ("inline whole 弯钩
  fresh with matched taper"). No helper composition.
- What this tells us: the failure mode of the ORIGINAL 子 (detached
  hook, dominant crossing heng) was ALREADY well-diagnosed in errata.
  A drawer who literally reads the errata fix idea and executes it
  will pass. Retries fail when the errata idea is vague or when the
  drawer improvises without reading it.

### Fail-mode categorisation for the 7 retry FAILs

- **P12-violation family (2)**: 兀, 尢 — calligraphic 10px widths on
  MMH thin-line GTs. Both had "matched widths" (per errata fix idea)
  BUT chose the wrong overall weight. The rescue exists in bank (see
  wu_char.py at lighter widths) but was not consulted.
- **Composition-junction family (3)**: 夂, 夊, 女 — apex/junction
  geometry approximately right but strokes don't quite compose. The
  B3 kiss_apex helper would help but WAS NOT USED.
- **Envelope-shape family (1)**: 飞 — envelope too enclosed (乙-shape)
  vs GT's open right side. No dedicated helper exists.
- **Composition asymmetry (1)**: 门 — char version PASSes with a
  specific inline recipe (see men_char.py); radical retry uses a
  slightly different inline recipe and fails. Cross-transfer between
  char and radical bank entries is not happening automatically.

### The four persistent gap explanations (checked against B4 evidence)

**1. Content — is memory missing specific stroke × context combos?**
   Partially. form_catalog.md has ~35 entries after B3; several B4
   fails (X-cross at heng midpoint, envelope shapes like 飞/丸, curl
   terminals like 己/已, mirror 提 like 孓) genuinely lack rows. Adding
   rows helps main attempts but NOT retries (see #2).

**2. Retrieval — do drawers actually cite memory?**
   MAIN: ~24% import from _shared_helpers (36 of ~150 non-retry
   attempts). MODERATE.
   RETRY: 0% (0 of 8 in B4, 0 of 8 in B2, 7 of 13 in B3 but B3's
   variant_* uses; kiss_apex specifically: 0 of 8 B4 retries).
   RETRY IS BROKEN. This is now the biggest lever.

**3. Format — is callable-Python the wrong storage unit?**
   Ambiguous. The 27 main PASSes worked fine as callable Python (8
   were 1-line identity aliases — the format's happy path). The
   composition helpers (kiss_apex, mirror_dian_pair) exist in that
   format. What's missing is not FORMAT expressiveness but retrieval
   discipline. NOT the primary problem.

**4. Radical evolution — new categories, auto-generation, subdirs?**
   Considered. Auto-generation from every PASS would explode
   form_catalog to ~140 rows, drowning the drawer. Per-radical-class
   subdirs might help retrieval but no evidence yet. Deferring.

### The B4 core lesson

**G3's gap is now diagnostically clear**: retries do not consult
memory (specifically the composition helpers). The helpers, form
catalog, and errata are all doing their job for MAIN curriculum — the
main pass rate has stabilised around 54-58% since v7. The gap
against G1 is now almost entirely in the RETRY channel.

**Options for B5 (see evolution.md 2026-07-23)**:
- **Option A**: modify the retry-dispatcher to inject a "MEMORY FIRST
  CHECKLIST" (require the drawer to answer three questions before
  writing code: "does form_catalog have a row for this stroke×context?
  does memory_index recommend a helper for this composition? does
  bank have a matching primitive?").
- **Option B**: kill the retry mechanism (0/8, 0/13, 1/8 — the one
  PASS was via inline, no memory used, so memory contributed nothing
  to retry PASSes). Redirect the retry budget to more main-curriculum
  items.
- **Option C**: **auto-graduate the char→radical direction**. B4
  showed 兀, 门, 子 (radical) failing while the corresponding CHAR
  PASSes. When a char passes, automatically write both `<name>_char.py`
  AND if radical is in errata, back-port the recipe as a radical
  retry candidate.
- **Option D**: fail-mode-aware retry prompts. Look up errata's
  fail-mode category (P12-violation, composition-junction, envelope,
  etc.) and inject an explicit recipe pointer per category.

Curator chose **A + C** for B4→B5 (see evolution.md).

## PASS notes (B4)

- **8 identity aliases** (刂, 囗, 山, 干, 口, 艹, 宀, 小) — the "look up
  radical, wrap in one line" pattern is now robust. About 30% of
  Phase-3 chars in the 034-083 range are radicals in disguise.
- **kiss_apex WORKED** on the ONE main-curriculum char that used it
  correctly at u_pie=0.0 (亼). It failed on 大 (u_pie=0.5) because the
  apex wasn't placed on the heng crossbar — a placement problem
  ABOVE the helper's abstraction.
- **inline recipes still dominate for tall/narrow chars** (门, 子, 孑,
  卄, 亡). The bank's aspect ratios don't match; inlining fresh with
  target-proportion coords is the reliable path.

## B4 signature-restriction fails NOT resolved by B3 evolution

- 大 char: kiss_apex used but apex is not on the heng — need explicit
  heng-midpoint computation.
- 匕, 才: pie endpoint should land ON a specific pixel of another
  stroke — pie_point helper exists but was never used.
- 丸, 飞: envelope shape must be OPEN vs CLOSED — no envelope helper
  and no worked example in form_catalog for open-envelope family.

## B5 diagnostic (2026-07-24) — the retrieval fix worked but the ceiling held

### Raw B5 numbers
- Main: 19/50 = 38% (WORST of any batch — down from B4's 54%).
- Retries: 1/17 = 6% (only 丷 passed).
- Cumulative through 300 items: 49.6% (BELOW 50% for the first time; -3.8pp vs G1 no-memory ~53%).

### Retrieval measurement (B4→B5 checklist compliance)
- 17/17 retries wrote the Q1/Q2/Q3 checklist header. 100% compliance.
- 17/17 retries imported at least one helper from `_shared_helpers.py`.
  Mean helper-import call count: 6.5.
- Compare B4 retry helper-import rate: 0/8.
- The retrieval fix ABSOLUTELY worked. The helpers were consulted.

### But only 丷 PASSed. And it PASSed by REJECTING its recommended helper.
- 丷 retry_4's checklist Q3 said "mirror_dian_pair — NO (GT is asymmetric)".
- 大 retry_4 similarly abandoned kiss_apex mid-attempt in favor of inline.
- 人 retry_4 and 入 retry_4 followed kiss_apex to the letter and failed.

### The falsification
Three v7 passes assumed successive missing ingredients:
- v7 pass 1 (B3): "wrong form" — added variant_pie/na/dian + form_catalog.
- v7 pass 2 (B4): "wrong composition" — added kiss_apex/pie_point/mirror_dian_pair.
- v7 pass 3 (B5): "wrong retrieval" — added RETRY-TIME CHECKLIST.

B5 result falsifies the pass-2 hypothesis: the helpers were retrieved and
they did not produce PASSes. The one PASS came from IGNORING the helper.

### What the retry channel actually surfaces
Retries are FAILURE-INVERTED main attempts. If the main FAILed and the helper
existed at main time, it would already have been used (in main, drawers cite
helpers at 24% — one of them would have hit). The retry is running because
the composition class doesn't admit a callable helper that captures its
calligraphic essence. Adding more helpers won't fix this class.

### Format ceiling (honest naming)
The X-crossing family (人, 入, 大, 义, 从, 天, 太-crotch, 火, 见, 长-捺) is
where callable-Python coordinates hit their ceiling. A "kiss" is not a
shared pixel — it's a visual continuity of ink flow. Two variant_pie/na
calls that share head coords produce two brushstrokes that meet at a
point but don't flow into each other. G4 (米字格 + joint spec) may
have the same problem; G1 (no memory) may have the same problem too —
but G3's memory PRETENDS to solve it and the pretense is what makes
G3 lose vs G1.

### Options for B6 evolution (see evolution.md 2026-07-24 for decision)
- KILL the retry mechanism. 1/17 in B5 (helper-rejecting recipe). B3=0/13,
  B4=1/8, B5=1/17. Cumulative retry rate across v7 = 2/38 = 5%. Below noise.
- Freeze form_catalog (~50+ rows now). Prune unhelped rows.
- Add a "helper skepticism" principle: when recommended helper contradicts
  GT observation, PREFER GT observation.
- Explicit paper finding: G3's callable-Python format has a structural
  ceiling for context-varying calligraphy at ~50% vs G1's ~53%.

### PASS notes (B5)
- 4 identity aliases (心=xin, 文=wen, 日=ri) — the alias play still works.
- 3 X-crossing PASSes on MAIN (太, 文, 冈-inner-乂) — main channel uses
  helpers productively where retries can't.
- 5 kou/frame chars (中, 日, 冈, 不, 丹) — the box+shaft compositions
  remain the reliable Phase-3 harvest.
- Retry PASS 丷 is the only lesson: trust GT over recommended helper.

### FAIL family clusters (B5 main)
- 亻-radical family: 仂 仄 仇 仑 仓 (5 fails) — right-side component
  variation was too wide for identity-alias reuse.
- X-crossing family: 义 天 (2 fails) — same class as terminal-freeze 3.
- Envelope/frame: 内 內 冗 冘 円 (5 fails) — 冂-frame + interior recipe
  keeps missing.
- Compact radical shapes: 马 巛 幺 乡 为 乌 予 长 (8 fails) — none have
  a stable inline recipe yet.
- Adjacent to terminal-freeze: 见 (kou + 人) failed at retry_2; watch
  for its own terminal freeze at retry_5.

---

## B10 diagnostics (2026-07-31, position 500)

**Main pass 12/50 = 24% (down 4pp from B9). Retry 2/7 = 29%.
Zero A cumulative through 500 items (the code-format ceiling continues).**

### The two retry PASSes — v13 explicit-bank-call worked

Both retries that graduated had explicit-bank-call instructions from the
B9 curator's leak analysis:
- **295_时** — B9 fail: inlined 寸, lost hook. B10 retry: called bank
  `ri` (日) + bank `cun` (寸). PASS.
- **296_串** — B9 fail: bank kou boxes at 0.42 scale, shu didn't
  protrude. B10 retry: same bank kou but scale up + tall shu. PASS.

**The other 3 leak candidates (304_疖, 306_亨, 315_声) still FAILED**
even with bank-call instructions. Pattern: leak-fix works when the
composition is stack/mirror (時=日+寸 side-by-side, 串=口 stack), fails
when composition needs vertical-3-stack proportion tuning (亨=亠+口+了)
or narrow-column proportion (疖=疒+卩, 声=士+尸).

### C attempts diagnosed (5 items)

C = close-but-not-panel-PASS. Distinct from FAIL: judges could read the
character but hit a specific readability gap. Each C is a promising
retry candidate in B11 with a targeted fix.

- **345_志** — top 土 + bottom 心. Rendered OK but heart bottom too
  spread out; bottom sweeps read as separate strokes not one 卧钩.
  Fix: tighter 卧钩 with the 3 dots INSIDE its concavity.
- **358_盯** — 目 (left) + 丁 (right). BANK_DEVIATION for both:
  `ri.py` doesn't compress narrow, `ding_char.py` is canvas-centered.
  Result reads clean but 目 is drawn too narrow (~20%) and 丁's heng
  spans FULL width — makes 目 look attached to 丁's heng not below it.
  Fix: 目 to ~28%, 丁's heng starts at x=100 not x=0.
- **362_甾** — 巛 top + 田 bottom. The 巛 curly scoops are readable but
  each terminates in a straight line (no calligraphic hook curl); 田
  below is centered too high, no gap between them.
  Fix: curl the scoop tails; add 15px vertical gap.
- **365_和** — 禾 (left) + 口 (right). 禾 rendered with excessive
  triangular pie/na spread at bottom; 口 too small and too far right,
  reads as a disconnected box. Fix: 禾's pie/na widths thinner + shorter;
  口 tighter to 禾's shu.
- **377_法** — 氵 + 去. 氵 dots too small relative to 去; the 去 has 土
  top OK but 厶 bottom reads as separate 撇+点 not a linked stroke.
  Fix: 氵 dots larger; 厶 as one continuous polyline.

### FAIL clusters (33 mains + 5 retry-fails)

**Cluster 1: 亻/亽/宀-family with unmastered right (12 fails)** — 佗,
佚, 佛, 佝, 佞, 佟, 佥, 佤 (implied), 佗 dup, 亨, 佔-adjacent. Same
B8/B9 pattern: 亻 left is easy (bank ren_pang works), right is unmastered
(它, 失-implied, 弗, 句, 女, 冬, 佥, 甲-narrow, 亭). No new content —
same content-gap ceiling.

**Cluster 2: X-crossing / apex-kiss (5 fails)** — 张 (弓+长: 长 has X),
每 (母 X-family), 佚 (亻+失), 找 (扌+戈), 197_矢 retry_3, 216_失
retry_3. Same format ceiling as 大-family. **矢 and 失 both hit
retry_3 → retry_4 next batch → retry_5 = TERMINAL_FREEZE watch.**

**Cluster 3: envelope/frame errors (5 fails)** — 佟 (亻+冬-envelope),
畅 (申+日-swapped-order), 事 (frame + interior + shu), 学 (⺌+冖+子),
定 (宀+疋). Envelope proportions keep drifting when the interior is
non-bank.

**Cluster 4: cursive/curly primitives (6 fails)** — 步 (止+少 with
curly bottom), 乖 (禾-variant with 3 mirror strokes), 其 (甘 with 二
below), 乶 (unusual Korean-ideographic), 疟 (疒+虐-fragment), 疠
(疒+万). Bank has no cursive envelope primitives; inline degenerates.

**Cluster 5: 亠/⺀-top compositions (3 fails)** — 亨 retry, 步-shared,
定 retry-candidate, 亽 (implied). 亠 is bank but the top-cap placement
under it is where the composition breaks.

**Cluster 6: mismatched sub-radical primitives (7 fails)** — 改 (己 vs
bank 巳), 疙 (乞 vs bank 亓), 疌 (聿 not in bank), 皃 top-only-first-try
(bank 白 too big), 甾 top (巛 vs straight 川), 证 (讠 and 正 both
errata), 找 (弋 vs 戈), 盯 (目 narrow vs bank ri wide), 皃 bottom
(儿 wide vs bank narrow), 的 (白 wide vs bank standalone), 畀 (丌 not
in bank). **9 BANK_DEVIATION notes; 3 became PASSes (皃/的/畀)** —
proving the deviation channel adds value in ~33% of cases. The other 6
deviations either FAILed the fresh render or were C.

### Meta: the code-format ceiling reflection (500-item milestone)

Zero A verdicts across 500 items × 10 batches. G4 has 11+ A in B9-B10
alone. The gap is now measurable across two independent judgment axes:

1. **G3 pass rate**: ~40% cumulative vs G1 ~52%. Deficit -12 pp.
2. **G3 A rate**: 0% vs G4 ~15% in B9-B10. Structural.

The B9 curator named this correctly: G3's PIL-line-primitive operates
at the LINE layer, G4's 米字格 anchors + P/T/N/S joints operates at the
STROKE-JOINT layer. Panel judges reward joint modulation. B10 confirms
this — the ONE bright signal (retry graduates 时/串) came from
composition-retrieval fixes, not from any calligraphic improvement.

**Can memory unlock an A in B11?** Diagnostic: A requires calligraphic
weight modulation AND joint fluency. Current bank stores line coords
+ width. No amount of memory reorganization changes this. The three
routes not yet exhausted:

- **Route A**: adopt Bezier-with-taper as the primary primitive (not
  raw d.line). B7's 大 graduate used a tapered bezier — got PASS but
  no A. Suggests taper helps but is not sufficient.
- **Route B**: encode joint-share explicitly (which strokes share a
  pixel, which endpoint-hangs-off-which). This is basically G4's
  approach — adopting it invalidates the comparison.
- **Route C**: give up chasing A; declare "A" out-of-scope for the
  callable-Python format and publish the ceiling as the finding.

Recommendation to head curator: publish Route C as the paper finding
after B11 confirms no A. The intervention log through B10 already
demonstrates 3 rounds of format freedom (v8/v9/v10) + 1 round of
retrieval-channel fix (v13) failed to move the A rate.

### B11 pipeline suggestions

- Retry queue: 197_矢, 216_失 (both retry_3 → retry_4 with bank-call
  hint), 345_志 / 358_盯 / 362_甾 / 365_和 / 377_法 (5 C→retry_1 with
  targeted geometric fixes above).
- Watch for TERMINAL_FREEZE on 矢/失 (their retry_4 in B11 → retry_5
  in B12 possible).
- Don't add speculative variants. Only promote fresh_components with
  PASS evidence.
- The BANK_DEVIATION channel is working (3 promotions this batch).
  Continue observing which deviations succeed vs fail.

## B11 diagnostics (2026-08-03, position 550)

**Main pass 14/50 = 28% (up 4pp from B10; best G3 since B9's 28% - matches).
Retry 0/5 (2 C at R4 for 矢/失 → TERMINAL_FROZEN this batch).
Zero A cumulative through 550 items (11 consecutive batches).**

### The 4 C attempts (main channel)

C = close-but-not-panel-PASS. Distinct from FAIL — each is a promising
retry candidate in B12 with a targeted geometric fix.

- **385_物** — 牜 (compressed left) + 勿 (right). BANK_DEVIATION from
  niu.py and wu_neg.py — both had bake issues. Fresh render is legible
  but the compressed 牜 lost the ti-strokes distinction; reads as 牛
  with a small right addition. Fix for B12 retry: sharpen the ti stroke
  (rising sweep) and make 勿's descending arms visibly parallel not
  splayed.
- **408_佾** — 亻 + 八/月 stack right. Recipe used bank ren_pang + ba
  small top + yue bottom (no deviation). Reads close to 佾 but the ba
  dots sit AT the top of 月, obscuring the top-heng of 月; also 月 slightly
  wide for the right column. Fix for B12: shrink ba to 0.55 with more
  vertical gap above 月; compress 月 width by ~15%.
- **411_受** — 爫 top + 冖 middle + 又 bottom stack. Used bank
  zhao_top + mi_radical + you (no deviation). Reads as 受 but 爫 is too
  wide (spans full canvas) and 冖 cap is too high, leaving a gap between
  it and 又. Fix for B12: compress 爫 to 0.85 width, drop 冖 by 20px.
- **431_说** — 讠 (TERMINAL) + 兑 right (丷+口+儿). BANK_DEVIATION for
  both sub-radicals. Fresh render OK but 讠 is placed too tall (spans
  full height) and 兑's 儿 legs are drawn as separate sticks not a
  continuous 儿. Fix for B12: 讠 compressed to y=80-220, 儿 as bank
  er_ren_for_bottom_stack (row 229) with reduced scale.

### The retry_4 C for 矢 and 失 — decision to TERMINAL_FREEZE

Both hit C on retry_4 under v13 explicit-bank-call with da_char (bank
#201) as template. C means the panel read the character but didn't cross
PASS. Same X-crossing format ceiling as B5's terminal-frozen 人/入/大.

Analysis of the retry trajectory (4 attempts each under progressive
unlocks):
- retry_1 (v7): FAIL, followed helper composition, apex-position off.
- retry_2 (v7): FAIL, hand-tuned tapered_bezier, taper too heavy.
- retry_3 (v9 visual-diff): FAIL, correct visual diagnosis of gap.
- retry_4 (v13 explicit-bank-call with da_char template): **C** —
  finally readable but panel still says not-quite-PASS.

The trajectory shows monotonic improvement (FAIL→FAIL→FAIL→C) but the
last mile (C→PASS) requires the calligraphic joint-modulation that
line primitives can't render. One more retry would land in C again
per format ceiling logic.

**Decision**: TERMINAL_FREEZE both. Logged to retry_log.jsonl and
errata.md. Moved to X-crossing terminal-freeze family (now: 人, 入,
大, 匕, 矢, 失). Recipe is preserved in attempts/ for research record.

### Fail clusters (32 mains + 3 retry fails)

**Cluster 1: 亻/氵-family with unmastered right (10 fails)** — 佬, 佯,
佻, 佽, 侃, 侉, 侌, 侖, 侍 (PASSED), 侑 (PASSED). Same B8-B10 pattern:
left is easy (bank ren_pang works), right is unmastered (老-bottom,
羊, 兆, 欠, 冂-with-儿, 夸, 今+云, 命-frame). Content gap continues.
`shi_serve` and `you_help` PASSes show that when a right composition
CAN be worked out, deviate-and-promote is producing variants.

**Cluster 2: Multi-radical stack with unmastered pieces (7 fails)** —
是 (日 top + 疋 hanging), 畈 (田+反), 畋 (田+攵), 转 (车+专), 규 (夫+见),
放 (方+攵), 实 (宀+头-body). Bank has the top or the base but not the
adjacent piece; deviation is forced but the fresh sub-radical fails.

**Cluster 3: Unmastered top-cap / envelope (5 fails)** — 亞 (mirror
envelope), 亟 (bumpy compound), 苦 (PASSED), 表 (PASSED), 空 (PASSED),
话 (PASSED). Half of this cluster PASSed by fully inline — the ones
where the 8-stroke composition happens to have clean geometry (艹-top
compact, 讠 recipe from prior, 龶+衣 top+bottom split).

**Cluster 4: X-crossing / apex-kiss (5 fails)** — 佾-adjacent, 佻,
放 (放's 攵), 亟 (X in middle), 采 (PASSED — bank zhao_top+mu identity
carried it). Continued format ceiling.

**Cluster 5: Composition-retrieval leak (unchanged)** — 疖/亨/声 still
FAILing on R2 despite bank-call. See P-DEV2. B12 retry with explicit
y-bands is the last try before terminal-freezing this cluster too.

### Meta reflection — the 11-batch ceiling milestone

**Zero A verdicts across 550 items × 11 batches × 4 format unlocks
(v8/v9/v10/v13) × 2 prose overlays.** G4 米字格 continues to earn A
at ~15% in the same batches. The A gap is now impossible to attribute
to sample noise.

This confirms the B10 curator's recommendation: publish "callable
Python + PIL line primitive" as the ceiling and stop iterating format
unlocks. The v13 channel is producing steady variant flow (7 variants
in 100 items) but that's a MEMORY-STRUCTURE emergence signal, not a
PANEL-VERDICT lift signal. Both matter for the paper — separately.

**Bank health at 550 items**:
- Total entries: 247 (rows 1-247).
- v13 variants: 7 (rows 227-229 from B10, 244-247 from B11).
- Original primitives untouched: all 240 pre-variant entries preserved.
- Deviation rate: 34% (of mains, B10+B11 combined).
- Variant promotion rate: 7% of items (a stable emergence rate).
- P-DEV1/P-DEV2/P-DEV3 codified the deviation+promotion rules.

The memory is emerging into a two-tier structure: (1) frozen originals
that continue to serve identity-alias compositions, (2) contextual
variants for composition slots where the original doesn't slot cleanly.
This is the cleanest emergent structure any G3 batch has produced. It
does not close the A gap, but it's the finding to lead the paper with.

### B12 pipeline suggestions

- Retry queue R3: 疖/亨/声 (last try with y-band hints per P-DEV2).
- Retry queue C→R1 for B11 C-attempts: 物, 佾, 受, 说 (each with
  specific fix per section above).
- Do NOT retry: 矢, 失 (TERMINAL_FROZEN this batch).
- Watch for: 3+ more mirror-splay / X-crossing / cursive-envelope items
  in B12 pool — no new mechanisms will close these; classify as
  format-ceiling and move on.
- Continue v13 channel — expect 2-4 more variant promotions per 50-item
  batch at current rate.
- Start research write-up in parallel: G3's 11-batch ceiling +
  variant-emergence structure is the paper's central figure.

---

## B12 diagnostic (2026-08-04, position 601, curator B12)

**B12 main pass rate: 7/50 = 14% (1 A + 6 PASS). Down from B11's 28%.
Retry: 0/3 all R3 → 疖/亨/声 TERMINAL_FROZEN.**

### ★★★ THE 畎 A VERDICT — FIRST-EVER FOR G3 ★★★

After 600 items / 12 batches / 4 format unlocks (v8/v9/v10/v13) / 2
prose overlays / 2 retry-mechanism cycles / cumulative zero A —
**畎 broke through**. Verdict provenance: `judgments/batch_B12/labels.json`
att1 → G3 → "A". Rendered PNG:
`groups/G3_coords/attempts/p3_char_0434_畎/01_畎.png`.

**What made it work** (per direct inspection of GT vs render):

1. **Explicit x-slot decomposition**: drawer computed hard boundaries
   `x_left=30, x_right=125` for 田 (left ~40%) and `x_left=150, x_right=275`
   for 犬 (right ~55%). No overlap, no drift.

2. **BANK_DEVIATION cleanly named**: skipped `bi_field_over_ji.py`
   (canvas-full 田 with 丌 base underneath — wrong topology + wrong
   position) and `da_char.py` (canvas-full 大 with own draw+save).
   Fresh components named `quan_tian_for_LR_left` +
   `quan_dog_for_LR_right`. Follows P-DEV1 perfectly.

3. **Thin uniform ink** (w=5, wm=4). No calligraphic embellishment.
   Matches MMH GT weight.

4. **Explicit cross-apex weld**: pie and na share the EXACT SAME pixel
   `cross = (215, 143)` on heng. The drawer computed this as a variable
   before invoking the strokes. This is the mechanism that P-DEV4 codifies.

5. **Two-cubic pie form**: 撇 rendered as (a) head segment above heng
   `pie_top → pie_neck` + (b) body segment `pie_neck → pie_tail`. Gives
   continuous curve through the crossing without visible kink.

6. **Small dian upper-right** (245,82) → (268,118) as a slight cubic
   taper — this is what makes 犬 (not 大). Placement is at the "correct"
   6-o'clock-of-the-dot-family visual expectation.

**Why this is significant**: the 大-family (人/入/大/矢/失) is
TERMINAL_FROZEN at C after R4 in three prior batches. Standalone
full-canvas X-crossing does not cross the calligraphic-joint threshold.
But **compressed into an L-R right slot, the same X-crossing recipe
achieved A**. The pixel-area of the crossing sits under the panel's
discrimination threshold when the character is compressed.

**Codified as P-DEV4**: X-crossing family may unlock A when compressed
into a sub-slot with explicit shared-pixel cross-apex. Restricted
pathway — does NOT unfreeze standalone 大/矢/失.

**Promoted**: rows 248 (quan_char.py wrapper) + 249 (quan_tian_for_LR_left)
+ 250 (quan_dog_for_LR_right). Motivating context 畎; templates for
略/畔/畝/畦/畯/畹 (from tian variant) and 猷 + 大-family-right-radical
compressions (from dog variant).

### The 14% dip — noise or real drift?

Trajectory: B10 24% → B11 28% → **B12 14%** (7/50 = A+6 PASS). Below
G1 no-memory control (~20% for B12 sample).

**Signals that suggest noise**:
- Sample is 50 items — 3-4 borderline flips would swing 6-8pp.
- BANK_DEVIATION rate was 120% (60 devs / 50 mains) — significantly
  higher than B10 (32%) or B11 (36%). This is item-pool dependent:
  the 800-block range hit item classes (亻+unmastered rights,
  皿-bottom stacks, 系-full-radical rights) where more novel shapes
  are needed than in the B10/B11 pool.
- **First-ever A** in the same batch: hard to reconcile "regression"
  with breakthrough. More likely: the batch hit a harder item pool
  AND had one favorable composition unlock.

**Signals that suggest drift**:
- v13 channel produced FEWER promotions than expected — only 2
  variants (vs B10=3, B11=4). Combined with the low PASS count, the
  bank isn't growing as fast this batch.
- Cluster 1 (亻/氵-family with unmastered right) continues to dominate
  fails — same B8-B11 pattern (10 fails in B12: 侯, 便, 侷, 俅, 俉,
  俊, 侶(C), 係(C)). Content gap persistent.

**Curator judgment**: **primarily noise + item-pool difficulty spike;
partly a bank-growth slowdown**. Two things I will monitor in B13:
(a) does the item pool return to 亻+mastered-right density, and (b)
does the v13 channel resume producing 3-4 variants. If B13 is
20%+ with 3+ variants, the dip was noise. If B13 stays ≤ 20% with
< 2 variants, the bank is saturating on the compound densities we've
already seen and needs strategic densification. Not raising alarm yet.

### Fail clusters (31 mains FAIL + 3 retry R3 FAIL)

**Cluster A: 亻-family with unmastered right (10)** — 侯 (侯-body),
便 (更 as body), 侷 (局), 俅 (求), 俉 (吾), 俊 (夋), plus C's 侶 (呂)
and 係 (系). Bank has ren_pang mastered; the right components are
either novel or have baked-canvas primitives that don't slot LR.
Actionable: BANK_DEVIATION with compressed inline is the right approach
but the fresh sub-radicals fail 4-of-5 times (matches B10 novel-shape
FAIL rate).

**Cluster B: 皿-bottom stacks (3 C)** — 盃 (不+皿), 盅 (中+皿), plus
FAIL 益/塩-adjacent. `min_dish.py` is module-level (not callable-into-
composition) and `bu_char.py` is canvas-centered. Both C's drew
plausibly (top OK, 皿 legible) but proportions drifted. **Best variant
candidate for B13**: promote a compressed 皿-for-bottom-stack from any
B13 PASS in this cluster. Note for drawer: try inline 皿 with 4-column
grid (left|inner|inner|right shu) at y=180-260, width ~120px.

**Cluster C: 疒/疒-family (5)** — 疣, 疤, 疫, 疬, 疭, 疮. `ne_sick` has
compact envelope but interior novel shapes fail. Also 疥 PASSED with
inline 介 — the envelope+介 recipe is the pattern to imitate for
interior recipes: keep envelope bank, inline the interior.

**Cluster D: 田-family (5)** — 畏 (田+ﾋ hooked bottom), 畑 (火+田), 皅
(白+巴), 皈 (白+反), plus 畈/畋/畐 continuing from B11. `bi_field_over_ji`
is canvas-baked; **`quan_tian_for_LR_left` (B12 new)** is now available
for L-R lefts. B13 retry candidates: 畈, 畋, 畐 with the new variant.

**Cluster E: 亻/艹/占 right-heavy (6)** — 侶 (呂), 侷 (局), 战 (戈 with
X-crossing), 俎 (且 stack), 草 (早), 亲 (立+木-hanging).

**Cluster F: 3+ part vertical stacks (3)** — 面 (三段), 美 (羊+大), 前
(丷+一+月+刂), continuing B11 3-stack difficulty (P-DEV2 signals this
is unwinnable without y-band hints; C-attempts might unlock with hints).

**Cluster G: Novel body shapes (5)** — 度 (广+又+又), 亲 (立+木), 癸
(癶+天), 带 (共-top with cloth), 疭 (疒+从). These are the "no bank
sibling family" cases P-DEV1 rule 2 says NOT to deviate on — but the
drawer had no choice (no primitives to call). Format ceiling.

### C-attempt retry candidates for B13 (with specific fix ideas)

Rank-ordered by likely retry-PASS probability:

1. **p3_char_0430_畈** (B11 FAIL, B12 no retry) — 田+反. Now that
   `quan_tian_for_LR_left` is banked, R1 with the new variant + inline
   compressed 反 should PASS.
2. **p3_char_0432_畋** (B11 FAIL) — 田+攵. Same variant + inline 攵.
3. **p3_char_0451_给** (B12 C) — 纟+合. Retry with explicit compressed
   纟 (skip si_zi_pang baked coords per errata) + bank kou for 口
   inside 合.
4. **p3_char_0467_结** (B12 C) — 纟+吉. Same 纟 fix + bank shi_male
   (士) + bank kou for 吉 stack.
5. **p3_char_0463_神** (B12 C) — 礻+申. Skip shen_extend (canvas-abs)
   and inline compressed 申 in right slot; can adapt jia_first's
   topology by moving shu.
6. **p3_char_0466_盃** (B12 C) — 不+皿. Compressed 皿-bottom fix idea
   above; may need a new inline 皿 recipe.
7. **p3_char_0470_侶** (B12 C) — 亻+呂. Two stacked bank kou for 呂
   with narrower kou_scale ~0.55.
8. **p3_char_0474_係** (B12 C) — 亻+系. 系 = 7-stroke; inline the
   top-scoop + 幺 body carefully.

### Fresh diagnostic on the retry TERMINAL_FROZENs

**疖/亨/声** — all R3 executed with all documented hints (BANK_DEVIATION
blocks, RETRY MEMORY CHECKLIST Q1/Q2/Q3, TRAJECTORY DIFF, explicit
y-bands from B11 curator, explicit column widths):

- **疖 R3 → C**: envelope OK, 卩 interior finally legible; panel says
  "still not there". Trajectory main→R1→R2→R3: FAIL→FAIL→FAIL→C.
- **亨 R3 → FAIL**: 亠+口+了 stack; 了's hook curl still not
  discriminable from 子/子-like tails. FAIL→FAIL→FAIL→FAIL.
- **声 R3 → FAIL**: 士 middle 竖 still missing despite fix promise in
  R3 header — drawer computed but rendered outside the discriminable
  region. FAIL→FAIL→FAIL→FAIL.

Per B10/B11 curator plan, R3 was declared the last try for the leak
candidates. All three failed/C. **TERMINAL_FREEZE all three.** Join
the terminal-freeze pool with 人/入/大/矢/失/匕. The compositional-
retrieval-leak hypothesis is now fully falsified: retrieval is
fixed but format ceiling holds for narrow-column (疖), 3-stack (亨),
and stacked-envelope (声) compositions.

### Meta-observation on the 12-batch record

Pass-rate trajectory: 54, 34, 58, 54, 38, 46, 32, 18, 28, 24, 28, **14**.
Cumulative through 600: ~42% (down slightly from B11's 44%).
**A verdicts: 1 (畎, B12)**. Trajectory: 0/50 × 11 → 1/50 at batch 12.

The A verdict does NOT overturn the format-ceiling finding — it's a
narrow structural pathway (P-DEV4: L-R-slot-compressed X-crossing with
explicit cross-apex). The paper writes: **G3's callable-Python +
PIL-line-primitive vocabulary sustains ~42% cumulative pass rate over
600 items with 1 A verdict; the 1 A came from a compression-pathway
exception (P-DEV4) that does not generalize to standalone characters.
G4's 米字格 A-rate advantage remains structural.**

### B13 pipeline suggestions

- New retries R1: 畈, 畋 (use `quan_tian_for_LR_left`); 给, 结, 神, 盃,
  侶, 係 (with specific fixes above).
- TERMINAL_FROZEN: 疖, 亨, 声 (this batch).
- Watch for 猷 (酉+犬) to validate `quan_dog_for_LR_right` variant.
- Watch for any 略/畔/畝/畦/畯 to validate `quan_tian_for_LR_left`.
- Continue v13 channel — expect 2-5 variants per batch at steady state
  (B12 dip to 2 is within noise).
- Continue paper write-up: P-DEV4 now needs a paragraph as the ONE
  A-verdict exception with pathway analysis.

---

## 2026-08-05 — B13 curator note (position ~651)

### B13 tally

Mains (50): 0 A + 10 PASS + 11 C + 29 FAIL = **20% pass rate** (up
from B12's 14%; back to normal band ~20-28%). Retries (8 R1s): 1 PASS
(盃) + 3 C (神/侶/係) + 4 FAIL (畈/畋/给/结) = **12% recovery**.

Cumulative: 1 A + ~285 successful/650 items ≈ **44%** cumulative pass
rate. Cumulative A rate: 1/650 = **0.15%**.

### ★ First batch G3 beat G5 on PASS rate (20 vs 18)

Item-level counts (mains only):
- **G3 > G5 (13 items)**: 指(PASS/C), 适(PASS/FAIL), 响(PASS/FAIL),
  能(C/FAIL), 都(C/FAIL), 畜(C/FAIL), 高(PASS/C), 畟(C/FAIL),
  原(PASS/C), 疰(PASS/C), 疴(PASS/C), 疸(PASS/FAIL), 亳(C/FAIL).
- **G5 > G3 (12 items)**: 怎(FAIL/C), 俐(C/PASS), 俘(FAIL/C),
  俛(FAIL/C), 丵(FAIL/PASS), 畛(C/PASS), 特(FAIL/PASS), 真(FAIL/PASS),
  部(C/PASS), 痂(PASS/A ★), 速(FAIL/C), 值(FAIL/PASS).
- **Tie PASS**: 俚 (both PASS).

**Pattern in G3 wins**: dominated by 疒-envelope family (疰/疴/疸 —
all G3 PASS while G5 C or FAIL) and by items where G3 has a
crystallized composition mode (适 with 辶+interior; 响 with 口+向).
Sub-pattern: 5 of G3's 10 PASSes are 疒-family (疰/疴/疸/痂 + also
0516/0522/0524/0530). This IS the mode where G3's bank has fully
converged — envelope call + inline interior.

**Pattern in G5 wins**: X-crossing / novel-body chars (特 has 牛+寺
with cross-strokes; 值 亻+直 straight lines; 真 has stacked hengs;
特/真/值 all G5 PASS but G3 FAIL). Also compressed compound-radical
chars (俐 亻+利, 丵). MMH median coords appear to help exactly the
class that our bank has NOT yet crystallized (novel bodies, X-crossings
without a matched right-radical recipe).

**Research signal**: G3's bank-driven memory now *compensates for*
MMH absence on the specific class of items where the bank has a
mature envelope. On classes without a bank envelope, MMH is a lifeline
G3 lacks. G5 does not strictly dominate G3 — the two systems
distribute over disjoint item classes. This is a paper-worthy
observation about *interaction* between memory format and external
cue availability. Not enough evidence to write it as a robust finding
yet — need B14, B15 to confirm the sign holds when the item mix
shifts. If it holds across three batches, section 4.3 of the paper
gets a "when does bank-memory replace MMH?" table.

### ★ Variant post-mortem: 畈 R1 FAIL + 畋 R1 FAIL

B12 curator promoted `quan_tian_for_LR_left` and listed 畈, 畋 among
reuse targets. B13 R1 result: BOTH FAILED. Root-cause analysis:

- **畈 (田+反)**: `quan_tian_for_LR_left` rendered the 田 cleanly as a
  compact rectangle (see attempts/p3_char_0430_畈__retry_1/01_畈.png —
  the box is correct). The FAIL is entirely in the 反: drawer inlined
  a fresh `draw_fan_right_for_LR` with 4 strokes but the topology
  collapsed — the 又's 横撇 tick + 捺 emerge as one continuous curl
  that reads as some abstract shape, not 反. GT 反 has a distinct
  短撇, distinct 横, long 撇 that sweeps down-left, and a 捺 that
  crosses the 撇 mid-height. The R1 attempt's coords made the 长撇
  and 捺 meet too high (near y=200 with junction at 215,200) and
  the 又's inner tick landed disconnected — reads as a stray line.

- **畋 (田+攵)**: same story — 田 clean, 攵 broken. Drawer computed
  a shared junction pixel (200,150) and inlined 4 strokes but they
  all landed in the upper half; the long 撇/捺 spread from junction
  downward as two lines meeting at the TOP, not the middle. Reads as
  a small ㄨ + floating tick. GT 攵 has the junction near mid-slot
  and strokes fan out radially.

**Common failure mode**: the right radical (反, 攵) is X-crossing-like
with no bank primitive. Fresh inline of X-crossing shapes without a
matched recipe fails — same content-gap as standalone 大/矢/失/入 in
TERMINAL_FROZEN. **P-DEV4 (X-crossing compression) works only when
the crossing is EXPLICITLY welded as a shared pixel AND has been
verified by a prior PASS.** For 反/攵 no such prior exists.

**Lesson for future variant promotions** (codified as P-DEV5):
- The promoted variant covers ONE SLOT. Do NOT list "reuse targets"
  whose SIBLING slot is unmastered.
- 畈, 畋 were never realistic R1 candidates — the sibling radicals
  (反, 攵) were unmastered. B12 curator's over-projection cost 2 R1
  slots that could have gone to more recoverable C's.

### C cluster diagnosis (11 items)

Prioritized by recovery probability:
- **0499 能** — visually near (see attempts/…/01_能.png vs GT). Composition
  is right (厶/匕 top-row + 月/匕 bottom-row); ink is too thick, hooks
  slightly off. **HIGH recovery** on retry with thinner width + tighter
  bottom-匕 curl.
- **0528 疽** — 疒 + 且. 疒 envelope is proven; 且's rectangular grid
  should be trivial. Fix: use `ne_sick` cleanly, inline 且 as 5-stroke
  compact rectangle (left竖 + 横折 + 3 hengs) in belly slot. **HIGH recovery.**
- **0526 疹** — 疒 + 㐱 (人-top + 3 descending pies). Envelope OK;
  㐱 is the novel piece. Fix: inline 人 (pie+na apex-kissed) then 3
  cascading pies at (x_right, y_low). **MEDIUM recovery.**
- **0503 都** — 者+阝 L-R. 者 was inlined; 阝 recipe adapted from 那.
  Fix: verify 阝 recipe matches GT (right ear with high 横折折/竖钩);
  compress 者 to left 60%. **MEDIUM recovery.**
- **0532 亳** — 亠+口+冖+乇 4-stack tower. Fix: cite explicit y-band
  per piece (亠 y=25-70, 口 y=80-130, 冖 y=140-170, 乇 y=180-275) per
  P-DEV2 rule for 3+-stacks. **MEDIUM recovery.**
- **0525 部** — 咅+阝 L-R (同 pattern as 都). Use same 阝 recipe.
- **0484 俏, 0486 俐, 0504 畛, 0506 畜, 0510 畟** — content-gap
  novel-body cases. Lower priority.

### B14 retry queue (final selection, 6 R1s)

1. p3_char_0499_能 — near-miss; thinner width, tighter 匕 curl.
2. p3_char_0528_疽 — 疒 + 且; ne_sick + compact rectangle interior.
3. p3_char_0526_疹 — 疒 + 㐱; ne_sick + inline apex-kissed 人 + 3 pies.
4. p3_char_0503_都 — 者+阝; adapt 阝 from 那 recipe.
5. p3_char_0532_亳 — 4-stack tower; explicit y-band per piece.
6. p3_char_0525_部 — 咅+阝; same 阝 recipe as 都.

NOT queuing 畈/畋 for R2 (sibling radicals still unmastered per P-DEV5).
NOT queuing FAILs from B13 for R1 (recovery rate on FAILs → R1 is
historically ~5%; C → R1 is ~15% and worth the drawer cycles).

### Language for paper (updated post-B13)

"After 650 items across 13 batches, G3 has produced 1 A verdict
(0.15%) via the P-DEV4 L-R-slot-compression pathway, and cumulative
pass rate ~44%. Beginning at B13 (position 651+), the ablation
comparison G3 vs G5 shows G3 winning on 疒/辶/亻 crystallized-envelope
families while G5 (G3 memory + MMH) wins on X-crossing and novel-body
families. This suggests memory format and external cue availability
interact: crystallized memory can replace MMH within its coverage,
while MMH remains critical outside it. Full-canvas X-crossing format
ceiling for G3 remains structurally intact — the 1 A is a narrow
compression exception, not a break."
