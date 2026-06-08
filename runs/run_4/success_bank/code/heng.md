# 横 (heng) — horizontal stroke

**Tags**: `tag:atomic-stroke` `tag:heng`

**Component-of**: (will be filled in as 横 appears inside mastered
characters — 一, 二, 三, 十, 工, 王, etc.)

**Mastered in**: run_4 cycle 1
**Rubric**: 10/10 (dunbi=2, hudu=2, taper=2, proportion=2, overall=2)

## Description

The canonical 楷书 horizontal stroke. Used as a top, middle, or
bottom bar in dozens of characters, and as a constituent stroke
inside hundreds more. This is the foundation primitive of Phase 1.

## How to reuse

```python
from heng import draw as draw_heng
draw_heng(t)                       # centered at origin
draw_heng(t, ox=0, oy=100)         # shift up 100 px (e.g. for top heng of 二)
draw_heng(t, ox=0, oy=-100)        # shift down 100 px (e.g. for bottom heng of 二)
draw_heng(t, ox=0, oy=0, scale=0.6)  # shrink to 60% (e.g. short top heng inside 王)
```

The function's internal parameters (control points, width profile)
are immutable per the Success Bank rule — to use a different
profile, write a new entry (e.g. `heng_short.py`) rather than
modifying this one.

## What this entry establishes

- The brushed-Bézier-with-per-sample-pensize pattern (the
  `brushed_bezier` helper).
- The min-pensize-3 floor (run_3 c17 lesson).
- The 楷书 weighted-entry / lighter-shaft / heavier-closing-press
  profile.
- The Success Bank's first `draw(t, ox, oy, scale)` interface
  convention.
