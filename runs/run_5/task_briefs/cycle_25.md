# Cycle 25 — 里 retry + 本 retry + 天

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Tasks

### 里 (carry from c24)
c24 panel 1/3 — skeptics caught the 土 component only had 2 horizontals visible (the 日's bottom heng was being read as the 土's top heng, leaving only one explicit 土 heng visible).

**Fix**: ensure THREE distinct horizontals in the 土 portion:
- 土 top heng (separated from 日's bottom)
- 土 middle heng (the one currently missing)
- 土 bottom long heng

So the full 里 has: 4 horizontals (top of 日, internal heng of 日, bottom of 日, top of 土 — this might be the same as bottom of 日 in MMH) + central shu (through 土) + middle heng of 土 + bottom long heng.

Looking again — MMH 里 has these strokes in order:
1. 竖 (left of 日)
2. 横折 (top + right of 日)
3. 横 (internal heng of 日)
4. 横 (bottom of 日 — also top of 土)
5. 竖 (central, through 土)
6. 横 (middle heng of 土)
7. 横 (bottom long heng)

The c24 drawer split 横折 into top heng + right shu, missed the middle heng of 土. Add it.

### 本 (carry from c21 and c22, both v=0.76)

**Fix attempt**: try `draw_mu(t, scale=0.92)` (slightly shrink 木) so there's more pixel-area headroom, then add the bottom dash at the appropriate position. The bottom dash needs to clearly cross the shu near its lower middle, distinct from the pie/na heads.

```python
draw_mu(t, scale=0.92)
draw_heng(t, ox=-2, oy=-58, scale=0.20)  # even smaller dash
```

### 天 (new)

天 (tiān, 4 strokes): heng (top, short) + heng (middle, longer) + 撇 (lower-left from mid heng's center) + 捺 (lower-right from same point). Looks like 大 with a heng cap on top.

Could decompose as: heng + 大. Or build from primitives: heng + heng + pie + na.

## Renderer (turtle + postscript, no subprocess)

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from na   import draw as draw_na
from mu import draw as draw_mu
```

## Output
`attempts/cycle_25/generated.py` + 3 PNGs (CHINESE filenames).
