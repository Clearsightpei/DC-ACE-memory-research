# Cycle 1 — Focus: 横 (heng, horizontal stroke)

## Phase

1 — atomic strokes.

## Cycle structure

**Single phase only.** Atomic strokes have no GT (eval = `vision`
only, by Teacher choice — `runs/run_2/POSTMORTEM.md` showed
hand-coded stroke GTs are weaker than the model's own strokes, so we
score by the reference-free Claude-vision rubric directly). With no
GT there is nothing to compare a skeleton against; the stroke IS
its own composition. So:

- The Drawer renders the brushed stroke directly into
  `attempts/cycle_1/01_横.png` via `attempts/cycle_1/generated.py`.
- No skeleton sub-phase.
- The Curator scores the calligraphy rubric on the brushed PNG.

## Prerequisites

None — this is an atomic stroke, the foundation.

## What 横 is

A horizontal stroke (heng). The single most-used brush primitive in
Chinese characters; appears as the top/middle/bottom bar of dozens
of simple characters (一, 二, 三, 十, …) and inside hundreds of
compound ones.

Canonical brush form (楷书):

- **Direction:** left to right.
- **Length:** moderate — about 400–500 px on this 800×600 canvas.
- **Center y:** at the canvas origin (0, 0).
- **Tilt:** slight upward tilt is canonical (~3–6 degrees rising
  to the right), but a fully horizontal line is acceptable for a
  reference-free rubric.
- **Brushwork (`dunbi`):** weighted entry on the left (the
  pen-press as the brush touches down), thinner shaft through the
  middle, then a stronger weighted press at the right end
  (the 收笔 / closing pause). Both ends are slightly heavier than
  the middle; the right end is typically the heaviest point.
- **Taper:** middle width ≥ 50% of the peak width; ends weighted.
- **Curvature (`hudu`):** essentially straight, or with a very
  gentle gently-rising arc. Not bowed.

## Suggested numeric targets

- Start: ~(-200, 0)
- End: ~(+200, 0)  (or +3 to +12 px in y for a gentle rise)
- Peak pensize: 16–18 at the entry and the closing press.
- Shaft pensize: 10–12 through the middle (≥ 50% of peak).
- Use the `brushed_bezier` pattern with `t.pensize(max(3, w_profile(s)))`.

## Eval

```
eval: "vision"
use_ocr: false (this is a stroke, not a character)
```

Mastery gate: rubric `total ≥ 7/10` with no criterion `== 0`. If
mastered, the Curator promotes the code to
`success_bank/code/heng.py` with tag set including
`tag:atomic-stroke tag:heng`.

## Self-preview budget

The Drawer may write `generated.py`, render the PNG, view its own
PNG, refine — **max 2 internal iterations** — then commit.

## File outputs

- `attempts/cycle_1/generated.py`
- `attempts/cycle_1/01_横.png`

Marker comment: `# ── Task 01 | 横 | heng`
