# Cycle 21 — 末 retry + 本 + 卞

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Tasks

### Task 1 — 末 (carry-over from c18/c20)
- GT: `ground_truths/cycle_21/01_末.png`
- Output: `attempts/cycle_21/01_末.png`

**c20 lesson** (from `to_be_learned.md`): top heng was scale 0.62 vs middle 0.45 — only 38% wider, not visibly different. Panel correctly rejected.

**Fix**: top heng scale ~0.80, middle heng scale ~0.45. That's ~78% wider — unambiguous distinction.

Use the same composition as c20 (heng + shu + heng + pie + na — primitives, not draw_mu). Only the top heng's scale changes.

### Task 2 — 本 (new)
- GT: `ground_truths/cycle_21/02_本.png`
- Output: `attempts/cycle_21/02_本.png`

本 = 木 + a short bottom heng (a dash crossing the bottom portion of the shu). 5 strokes.

Stroke order: heng (top) + shu (vertical) + pie + na + short heng (bottom-cross).

Suggested: use `draw_mu(t)` as base, then add a small `draw_heng(t, ox=0, oy=-65, scale=0.30)` (positioned just below the heng+shu cross, crossing the shu near its lower-middle).

### Task 3 — 卞 (new)
- GT: `ground_truths/cycle_21/03_卞.png`
- Output: `attempts/cycle_21/03_卞.png`

卞 = a small 点/撇 dot at top + 下 (top heng + shu + dian). 4 strokes total: dian (above) + heng + shu + dian.

Suggested: reuse `draw_xia(t)` for the bottom 下 portion (which is heng + shu + dian), then add a small `draw_dian(t, ox=-5, oy=+150, scale=1.5)` above the top heng. May need to shift xia slightly down to make room.

## Renderer (turtle + postscript, NO subprocess)

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from na   import draw as draw_na
from dian import draw as draw_dian
from mu import draw as draw_mu
from xia import draw as draw_xia
```

## Output
`attempts/cycle_21/generated.py` + 3 PNGs (CHINESE filenames: 01_末.png, 02_本.png, 03_卞.png).

Self-preview ≤2 iterations. For 末, the critical check is: is the top heng visibly LONGER than the middle heng?
