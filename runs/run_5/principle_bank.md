# Principle Bank (Part B of memory) — run_5 (after c5 hard-gate reset)

Curator-owned. Natural-language **positive rules** for producing a
render that looks unambiguously like the target character. Never
error logs. Never "don't do X". Always "to achieve Y, do Z".

A principle is graduated INTO this bank from the Sandbox once it
has worked on a real promotion.

---

## §0 — How the Drawer works (after c5 hard-gate reset)

The Drawer is dispatched as a fresh subagent and **is given the GT
PNG to look at**. Its job is to mimic the GT visually: open the GT,
sketch a turtle program, render its own PNG, open that PNG too,
and iterate until the render passes all three mastery gates.

The Success Bank (carried over from run_4) provides exemplary
turtle-based atomic and compound strokes — `heng.py`, `shu.py`,
`pie.py`, `na.py`, `ti.py`, `dian.py`, plus 7 compound strokes.
Reuse these via translate/scale rather than re-deriving brushwork.

`tools/` remains quarantined during the Drawer's turn. Only
`ground_truths/` is visible.

## §0.1 — Mastery gate (HARD, tightened after c5 review)

To promote an entry, the attempt must pass **ALL THREE**:

1. OCR identifies the character correctly with conf > 0.95
2. visual_score > 0.9 (from `tools/judge.py`)
3. Claude vision identifies the render unambiguously as target

Claude-vision alone is NOT sufficient. The c5 lesson: my vision
check called 人/入 unambiguous, but the renders had ugly disk-blob
apexes and messy 撇/捺 crossings that a human eye would call
poorly written. The numeric gates (OCR + visual) catch what a
misguided vision check waves through.

---

## §1 — Brushwork primitives

### §1.0 — Universal brushwork rules (run_4 canonical)

**To render any brushed stroke**: use a smooth cubic Bézier
centerline with per-sample pensize. The canonical helper, kept as
`brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220)`, walks
`s ∈ [0, 1]` and calls `t.pensize(max(3, w_profile(s)))` then
`t.goto(x, y)` at each sample. The `max(3, ...)` floor is
non-negotiable.

**Min sample count**: 200 for atomic strokes, 160 for short
hooks/segments.

### §1.1 — 横 (heng) — see `success_bank/code/heng.py`

Width profile: entry press 16 → 11 → shaft 11 → closing press 19.
Endpoints (-200, -3) → (+200, +3), gentle ~6 px upward tilt.

### §1.2 — 竖 (shu, 垂露) — see `success_bank/code/shu.py`

Endpoints (0, +200) → (0, -200). Width profile: symmetric barbell
— top press 16 → shaft 11 → bottom 垂露 press 18.

### §1.3 — 撇 (pie, 斜撇) — see `success_bank/code/pie.py`

Endpoints head (+150, +200) → tail (-180, -180). Control points
place centerline above the chord (concave-down arc). Width profile
head 18 → shaft 14 → 11 → tail 3.

**General tapered-tip pattern (撇 / 提 / etc.):** heavy head ~10%
(16–18 peak) → solid shaft ~76% (~11) → final 10–15% taper down to
floor 3. A 12% taper window reads smoother than a 5% window
(run_4 c3 verified).

### §1.4 — 捺 (na, 斜捺 with flat kick) — see `success_bank/code/na.py`

Two-segment stitched stroke. Main sweep: head (-150, +200) → kick
base (+170, -180); width 5 → 8 → 14 → 18. Flat kick: (+170,-180) →
(+240,-172); width 18 → 16 (hold 25%) → 3 (release 75%).

### §1.4b — 提 (ti) — see `success_bank/code/ti.py`

Endpoints (-100, -80) → (+150, +60). Width 14 → 11 → 9 → 3.
Same tapered-tip family as 撇.

### §1.5 — Two-segment stitched stroke pattern (run_4 c4)

When a stroke has a distinct terminal feature (kick, hook, turn)
with different width/direction than the main sweep, implement it as
**two Bézier segments stitched at a junction**:
- Segment A end's control toward Segment B's first control
  direction (tangential junction — eliminates angular notch).
- Segment A endpoint == Segment B start point.
- Independent `w_profile` per segment.

This is the basis for 横折, 竖钩, 横折钩, 竖弯钩, 横撇, 横折弯钩,
竖折 — all of which are now in the Success Bank as compound entries.

---

## §2 — Composition (translate, scale, position)

### §2.1 — Translate/scale reuse interface (run_4 turtle)

Every Success Bank `draw()` function takes `(t, ox=0, oy=0,
scale=1.0)` where `t` is a `turtle.Turtle`. Translation adds
`(ox, oy)` to every coordinate; scale multiplies coordinates but
does NOT scale the pensize.

To use a primitive inside a character, call e.g.
`draw_heng(t, ox=<x>, oy=<y>, scale=<s>)`.

(The PIL-renderer §2.1 from run_5 c2 is reverted with the c5 reset —
mixed renderers across the Success Bank produce inconsistent
compositions.)

---

## §3 — Slot reserved for run_5 character-composition rules

(Empty. The run_5 c1-c5 attempts at §2.2 — 竖 vs 横 patterns — and
§2.3 — 撇+捺 patterns — were not actually verified by promotions
that met the hard gate. They will need to re-emerge under the new
regime when a character actually passes OCR > 0.95 AND visual > 0.9
AND vision.)

---

## §4 — Hard-gate operating notes

- **A character that almost passes is still a fail.** Visual 0.89 is
  not 0.9. Carry over with specific Sandbox feedback (which gate
  failed, and by how much).
- **OCR misread is real signal.** If RapidOCR returns the wrong
  character or a low-conf result, the render IS ambiguous to that
  reader — that's evidence the brushwork has a real visual problem,
  not a RapidOCR vocab gap.
- **The base must be perfect.** Foundation characters are reused
  inside harder compositions; a sloppy 一 means every character
  containing 一 inherits the sloppiness. Aim for perfection.
