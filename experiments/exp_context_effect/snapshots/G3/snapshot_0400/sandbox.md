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
