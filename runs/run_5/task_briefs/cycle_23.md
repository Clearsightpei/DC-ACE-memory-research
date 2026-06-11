# Cycle 23 — 升 + 千 + 正

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Slate rationale

Diversify into chars with small 撇 + heng/shu. The 木 c14 lesson: small diagonals (scale ~0.45) clear visual gate. Apply that pattern to 升/千/正.

## Tasks

1. **升** (shēng, 4 strokes): 撇 (top-left small) + heng + heng + shu. Two stacked heng with a short pie on top-left and a shu on the right.
2. **千** (qiān, 3 strokes): small 撇 (top) + heng + shu. Simplest. The 撇 is short above the heng.
3. **正** (zhèng, 5 strokes): heng (top) + shu (left) + heng + shu (right shorter) + bottom heng (long). Looks like 工 with a top heng. Effectively heng + 止 or heng + heng + shu + heng + shu.

## Reuse
- heng, shu, pie
- existing chars in INDEX.md

## Renderer (turtle + postscript, no subprocess)

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
```

## Approach
Measure GTs, place strokes via (ox, oy, scale). Keep 撇 small (~0.30).

## Output
`attempts/cycle_23/generated.py` + 3 PNGs (CHINESE filenames).
