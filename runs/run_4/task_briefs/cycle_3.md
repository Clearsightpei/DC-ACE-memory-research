# Cycle 3 — Focus: 撇 (pie, diagonal sweep)

## Phase
1 — atomic strokes. Single-phase (no GT, eval=vision).

## Prerequisites
None (atomic).

## What 撇 is

A diagonal stroke sweeping from upper-right to lower-left, tapering
to a fine point. The third atomic stroke after 横 and 竖. Appears as
the left limb of 人, 入, 八, 大, 木, 不, 个, 介, 仁, and many more —
arguably the most-reused diagonal in Chinese.

Canonical 楷书 form (this is the **斜撇** — long diagonal — variant; the short 平撇 is a separate primitive):
- **Direction:** upper-right (head) → lower-left (tail).
- **Length:** comparable to 横 / 竖 — about 400 px diagonal.
- **Tilt:** ~30–45° below horizontal, the head points up-and-slightly-right.
- **Brushwork:**
  - **Heavy weighted head** at the upper-right (16–17 peak).
  - **Shaft** narrows progressively as it sweeps down-left.
  - **Fine taper to a point** at the lower-left tail (this is the FIRST stroke
    with a real tapered tip — the tail goes thin, near the pensize floor of 3).
- **Curvature (`hudu`):** *gentle* concave-down arc (curving away from horizontal,
  so the path bows down from a straight diagonal). NOT a tight spiral; a
  large-radius shallow curve. The middle of the stroke sits slightly above
  the straight head-to-tail line.

## Suggested numeric targets
- Head: ~(+150, +200) (upper-right area).
- Tail: ~(-180, -180) (lower-left).
- Control points placed so the centerline bows up-and-left slightly
  (canonical 撇 curvature).
- Peak pensize: 17 at the head; shaft ~11; tip 3 (only at the last ~5% of s).

## Reuse pattern

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from heng import brushed_bezier
```

## Eval
`eval: "vision"`, `use_ocr: false`. Mastery: rubric ≥ 7, no criterion = 0.

## Self-preview budget
2 internal iterations.

## File outputs
- `attempts/cycle_3/generated.py`
- `attempts/cycle_3/01_撇.png`

Marker: `# ── Task 01 | 撇 | pie`

On mastery: `success_bank/code/pie.py` with tag:atomic-stroke tag:撇 tag:斜撇.
