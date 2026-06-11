# Cycle 24 — 丰 + 丘 + 里

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Tasks

1. **丰** (fēng, 4 strokes): three heng + shu through all. Like 王 but more clearly evenly-stacked AND the shu protrudes both above the top heng AND below the bottom heng (in some renderings). 4 strokes.
2. **丘** (qiū, 5 strokes): 撇 (top-left short) + heng + heng + shu (left middle) + heng (long bottom). Like 兵's top portion.
3. **里** (lǐ, 7 strokes): 日 + 土. Has 口 components (which have failed visual gate in c15/c17). Risky but useful data point.

## Reuse
- heng, shu, pie, heng_zhe
- wang.py (c15) for 王-like portion
- existing chars

## Renderer (turtle + postscript, no subprocess)

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from heng_zhe import draw as draw_hz
from wang import draw as draw_wang
from tu import draw as draw_tu
```

## Approach
Measure GT, place strokes. Same approach as c11-c22.

For 里: could decompose as 日 (top 口-like box with internal heng) + 土 (below). Use `draw_tu(t, oy=-X)` for the bottom + 口-like box at top.

## Output
`attempts/cycle_24/generated.py` + 3 PNGs (CHINESE filenames).
