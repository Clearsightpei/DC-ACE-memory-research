# What MMH is doing in run_6

This doc exists because the role of MMH (the MakeMeAHanzi dataset)
kept drifting between sessions. Read this first before redesigning
anything that touches stroke data.

## What MMH is

**MMH = MakeMeAHanzi**, an open-source Chinese character dataset.
We use a single file from it: `draw_character/graphics.txt`.

For each Chinese character, MMH provides:

- `medians`: a list of stroke polylines (the centerline of each stroke
  as a sparse polyline of 5–11 sample points). Stroke ORDER matches
  canonical stroke order.
- The coordinate system is the **MMH coordinate space**: x ∈ [0, 1024],
  y ∈ [0, 1024], math convention (y grows UP, NOT image convention).
  The transform to our 800×600 canvas is `(x-512)*0.4, (y-512)*0.4`.
- A vector outline (we don't currently consume it).

That's it. MMH does NOT provide: stroke type labels (heng / shu / pie / …),
joint annotations, rendering instructions, or font weights. Everything
structural beyond "here is the centerline" is *derived* by our tools.

## What MMH does in run_6 (5 jobs)

1. **Stroke count** for the structural gate. The Drawer must produce
   exactly `len(medians)` top-level primitive calls. Single source of
   truth for "how many strokes does this character have".

2. **Per-stroke anchor extraction** (raw endpoints). For each stroke,
   `from = first median point`, `to = last median point`, transformed
   to canvas coords and rounded to (cell, x_frac, y_frac) via
   `_anchor.cell_relative_for_xy`. The Drawer uses these AS-IS — do
   NOT override them from joint analysis (that was the c43-c52
   regression).

3. **Compound-stroke internal corners** via `tools/joint_detector.find_corners`.
   For a stroke whose primitive needs a corner1 (e.g. `heng_zhe`,
   `heng_zhe_gou`), `find_corners` walks the median for a windowed
   direction-change > 45° and returns the bend point. This becomes
   the primitive's `corner1` argument.

4. **Inter-stroke joint topology** via `tools/joint_detector.find_joints`
   (segment-to-segment closest distance, eps_mmh=90). Joints are
   then **classified** by `tools/classify_joints.classify` into:

   - **P (Piercing)**: d<5, both labels mid → strokes cross through
     each other; raw endpoints render the crossing naturally.
   - **T (Tangent)**: d<10 with head/tail involvement → snap that tip
     to meeting_canvas. Rare.
   - **N (Neighbor)**: 10≤d<90 → small natural gap (canvas_px = d*0.4)
     IS correct calligraphy. Do NOT snap.

   The class determines panel/curator expectations, NOT anchor
   constraints (except class T's small snap).

5. **Pixel ground truth** for visual_score + OCR via `tools/make_char_gt.py`,
   which strokes the medians onto a PNG. This GT is what `judge.py`
   compares the Drawer's render to.

## What MMH does NOT do

- It does NOT say "this corner welds" vs "this corner has a gap".
  That's `classify_joints`'s job, derived from `dist_mmh` + `frac`.
- It does NOT match handwritten calligraphy exactly. MMH is a
  print/Kaiti reference. For some characters (人 入 八 大) the
  printed form's stroke heads sit at structurally different
  positions than handwritten canonical forms — those characters
  need an `apex_share` override in the brief (Drawer applies it,
  see DRAWER SKILL).
- It does NOT label stroke type. The Teacher maps MMH stroke
  index → primitive name (heng / shu / heng_zhe / …) when writing
  the brief, by inspecting the median's start direction + bend
  pattern.

## Why this matters

Two prior failure modes both traced to misunderstanding MMH's role:

- **c43–c52 joint-snap regression**: I treated `find_joints` output
  as anchor constraints (override `from`/`to` with `meeting_canvas`),
  flattening MMH's natural P/N variation. Result: 口 / 山 lost their
  correct neighbor gaps and `shu` 垂露 droplets protruded past forced
  snap points. Fix: stop overriding raw MMH endpoints.

- **c40 目 MMH-bend corner regression**: I used MMH median's max-x
  point as `corner1` for heng_zhe, but max-x sometimes occurs at
  the *bottom* of the vertical (after the corner) instead of at the
  L-bend. Fix (already in place): for L-corner compound strokes use
  geometric `(to_x, from_y)`; reserve MMH max-extent for 横撇-family
  mid-stroke bends.

## When to consult this doc

- Next session orientation ("what is MMH again?").
- Any time someone proposes "let's snap stroke endpoints to joints"
  or "let's use MMH max-x for the corner" — both have failure
  histories logged above.
- When adding a character with structurally-novel topology not seen
  in 又/口/中/半 — re-run `classify_joints` and confirm the class set
  matches the expected visual pattern before promoting.
