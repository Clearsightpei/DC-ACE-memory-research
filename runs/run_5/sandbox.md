# Sandbox (Part C of memory) — run_5

Curator-owned. Short-term scratch space for whatever is currently
being worked on. Resets when a focus is mastered.

---

## Reset note (after c5 user review)

The Drawer should write characters by **composing the run_4-carried
turtle strokes** (`heng.py`, `shu.py`, `pie.py`, `na.py`, `ti.py`,
`dian.py` + 7 compound strokes) via translate/scale. These strokes
are immutable and exemplary (run_4 c1-c13 rubric 10/10).

The c1-c5 PIL renderer was abandoned — its primitives produced
visible disk-stamp artifacts at width transitions (apex blobs in
人/入, dog-bone shapes in 一). Stick with the turtle primitives.

## What to aim for in cycle 6+

To pass the hard gate on a character:
- Visual score > 0.9 against the MMH GT
- OCR confidence > 0.95
- Vision: unambiguous

The 0.9 visual bar is high. The Drawer should:
- Place strokes precisely at the MMH skeleton positions (read the
  GT carefully and match).
- Use the canonical Success Bank brushwork — those are tested.
- Keep stroke counts and proportions exact.

If the gate is unreachable after 2 internal iterations + 1 carry-over
cycle, that is information about the bar's feasibility and should be
reported to the operator, not papered over with weaker promotions.

(Empty for cycle-specific feedback — next cycle starts fresh.)
