# Cycle 14 — Focus: 一 (yi, the number one — single horizontal stroke)

## Phase 3 (single-component characters). **FIRST two-phase cycle.**

## Prerequisites (verified in Success Bank)

- 横 (heng) — `success_bank/code/heng.py`. Mastered c1, rubric 10/10.

That is the ONLY prerequisite. 一 IS a single 横.

## Why this character

The simplest possible Chinese character (1 stroke). Perfect to verify
the **two-phase Phase-3 architecture** (skeleton-vs-GT comparison →
brushwork) on minimal-complexity input. If 一 doesn't work, nothing
will. If it does, we have a working two-phase pipeline.

## Skeleton phase

The Drawer writes `attempts/cycle_14/generated_skel.py` using **uniform
pensize 3** (no brushwork) and saves `attempts/cycle_14/01_一_skel.png`.

For 一, the skeleton is literally just a horizontal line.

### Numeric targets (derived from graphics.txt)

一 is one stroke. The canonical MMH skeleton (after the `tx = (x-512)*0.4`
transform) sits at approximately:

- **Heng centerline: from (-160, -100) to (+160, -100).** ~320 px long.
  Note: positioned BELOW the canvas center (y = -100, not 0) — this
  is where MakeMeAHanzi places the 一 medians. Do NOT center on the
  canvas origin.

The brief gives the Drawer this numeric target. The Drawer renders
the skeleton accordingly and the Curator compares it against the GT.

### Composing from Success Bank

The mastered 横 in `success_bank/code/heng.py` defaults to centered
endpoints (-200, -3) → (+200, +3). To match the 一 skeleton:
- Translate down: `oy = -97` (target y -100 minus heng's own +3 → -97)
- Scale 320/400 = 0.8 to match the GT length.

Actually it's easier to just write the skeleton inline at the target
coordinates. Don't worry about composing for the skeleton phase —
just draw the centerline.

## Brushwork phase (only if skeleton approved)

The Drawer writes `attempts/cycle_14/generated.py` adding per-sample
pensize to the approved skeleton. Now you CAN use the mastered heng:

```python
from heng import draw as draw_heng
draw_heng(t, ox=0, oy=-97, scale=0.8)
```

This reuses the c1 mastered widths (peak 16 / shaft 11 / closing 19)
applied to the 一-positioned skeleton. **DO NOT change the endpoints
from the approved skeleton** — only add brushwork.

## Eval

```
eval: "gt+ocr+vision"
use_ocr: true
```

Mastery: `is_correct == true` AND `ocr_confidence >= 0.4` AND rubric
≥ 7 (no 0).

## Self-preview budget

2 internal iterations per phase.

## Files

Skeleton phase:
- `attempts/cycle_14/generated_skel.py`
- `attempts/cycle_14/01_一_skel.png`

Brushwork phase:
- `attempts/cycle_14/generated.py`
- `attempts/cycle_14/01_一.png`

Marker for both: `# ── Task 01 | 一 | yi`

On mastery → `success_bank/code/yi.py` with tag:character tag:1-stroke tag:heng tag:component-of(三, 二, 王, 工, 干, 上, 下, ...) — pretty much every horizontally-symmetric char with a horizontal bar.
