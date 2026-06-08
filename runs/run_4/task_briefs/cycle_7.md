# Cycle 7 — Focus: 横折 (heng-zhe, the L-turn)

Phase 2 (compound strokes). Single-phase (eval=vision). Self-preview 2.

## What 横折 is

A compound stroke = horizontal heng followed by a 90° downward turn into a 竖. ONE continuous brushed path, NOT two separate strokes. The turn at the upper-right corner has a 顿笔 (thickening) before dropping down.

Appears in: 口, 日, 目, 田, 国, 月, 见, 国, ... — wherever you see the upper "L" frame of a box.

## Canonical form (Phase 2 simple variant — no hook at the end)

- **Heng arm**: from upper-left (-100, +120) to upper-right corner (+100, +120). Width 16 → 11 (canonical heng entry → shaft).
- **Corner 顿笔**: at (+100, +120), a thickening — width ~15.
- **Shu arm**: drops from (+100, +120) down to (+100, -80). Width 11 → 11 (steady).
- The whole thing is ONE continuous path — use the §1.5 two-segment stitched pattern (established by 捺 in c4).

## Implementation (two segments, tangential corner)

```
Segment A (heng arm):  (-100, +120) → (+100, +120)
  Control points colinear → essentially straight.
  w_profile: 16 (entry) → 11 (mid) → 15 (corner thickening)

Segment B (shu arm):  (+100, +120) → (+100, -80)
  Control points colinear → essentially vertical.
  w_profile: 15 (corner inherit) → 11 (shaft) → 13 (slight closing weight, not a needle)
```

Note: the corner thickening (顿笔) at width 15 is the visual signature of a 横折. Without it, the turn reads as two separate strokes glued together.

## Reuse
`from heng import brushed_bezier`. The compound is implemented as TWO `brushed_bezier` calls back-to-back.

## On mastery
`success_bank/code/heng_zhe.py` (tag:compound-stroke tag:横折 tag:multi-segment tag:corner-顿笔).

## Files
`attempts/cycle_7/generated.py` → `01_横折.png`. Marker `# ── Task 01 | 横折 | heng_zhe`.
