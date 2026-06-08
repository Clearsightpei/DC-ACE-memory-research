# Cycle 4 — Focus: 捺 (na, the right-diagonal sweep with flat kick)

## Phase
1 — atomic strokes. Single-phase (no GT, eval=vision).

## Prerequisites
None (atomic).

## What 捺 is

The right-diagonal companion to 撇, sweeping from **upper-left
(thin)** to **lower-right (heaviest)**, ending with a distinctive
**flat kick** (顿笔 + slight horizontal release) rather than a fine
taper point. Forms the right limb of 人, 入, 大, 八, 木, 不, 个, 介,
etc. — appears in essentially every character that has 撇.

Canonical 楷书 form (this is the **斜捺** — long diagonal — variant):

- **Direction:** upper-left (head) → lower-right (tail).
- **Length:** comparable to 撇, ~400 px diagonal.
- **Tilt:** ~30–45° below horizontal, mirroring 撇 by reflecting
  across the vertical axis.
- **Brushwork (this is what distinguishes 捺 from 撇):**
  - **THIN entry** at the upper-left head (~4–6 pensize) — almost
    starting from a point, opposite of 撇.
  - **Progressively thickening shaft** as it sweeps down-right.
  - **Heaviest at the tail** (pensize 18+) at the lower-right.
  - **Flat horizontal kick (顿笔 + 出锋)**: at the very end, the
    brush pivots and releases roughly horizontally to the right.
    This is the visual signature of 捺. Without it, it reads as 撇
    reflected — wrong.
- **Curvature (`hudu`):** gentle concave-up arc (centerline bows
  down-right slightly relative to the straight head-to-tail line).
  Not a tight spiral; large-radius shallow curve.

## How 捺 differs from 撇 (since this is the natural confusion)

| feature | 撇 (c3) | 捺 (this cycle) |
|---------|--------|----------------|
| head    | HEAVY (18), upper-RIGHT | THIN (~5), upper-LEFT |
| shaft   | thinning 14→11 | thickening 8→14 |
| tail    | TAPER to point (3) | HEAVIEST (18) with flat kick |
| direction | upper-R → lower-L | upper-L → lower-R |
| curvature | concave-DOWN | concave-UP |

The width profile is essentially **reversed** vs 撇's — thin entry,
thick exit, with a final little horizontal flat-press at the tail.

## Suggested numeric targets

- Head: ~(-150, +200) (upper-left area, mirror of 撇's head).
- Just before the flat kick: ~(+170, -180).
- After the flat kick: ~(+220, -170) (the brush releases right and
  very slightly up — about a 35 px horizontal kick with a tiny lift).
- Peak pensize: 18 at the kick base; head ~5; shaft 8→14.

For the flat kick at the very end, the cleanest implementation is to
draw the main 捺 as one Bézier with the width profile climbing to 18
just before s=1.0, then draw a SECOND short Bézier from the kick base
out to the kick tip with a width profile going 18→3. Two segments,
one continuous-looking stroke.

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
- `attempts/cycle_4/generated.py`
- `attempts/cycle_4/01_捺.png`

Marker: `# ── Task 01 | 捺 | na`

On mastery: `success_bank/code/na.py` with tag:atomic-stroke tag:捺 tag:斜捺 tag:flat-kick-tail.
