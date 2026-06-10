# Cycle 15 — 王 (carry-over) / 土 / 口

Hard gate (4): OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Slate rationale

- 王: c13 carry-over (v=0.77). The shu was scale 0.48 — short, creating mismatch with MMH's longer shu.
- 土: heng + shu + heng (very similar to 工 / simpler 干). 横-dominant, should clear easily.
- 口: heng + 横折 + heng (box). Tests the `heng_zhe.py` compound stroke. Could be tight on visual gate.

## Tasks

1. **王** (4 strokes — RETRY): three stacked 横 + one 竖 through midpoints. Top short, middle shorter, bottom long. Try a LONGER shu this time (scale ~0.65+ instead of 0.48) so its endpoints reach near the top and bottom heng — that should boost dice.
2. **土** (3 strokes): one heng (medium-short top) + one shu + one heng (long bottom). Shu through midpoints. Top heng shorter than bottom.
3. **口** (3 strokes): top heng + horizontal-fold (right side comes down) + bottom heng. Three strokes forming a small rectangle/box. Use `from heng_zhe import draw as draw_hz`.

## Reuse
- `heng.py`, `shu.py`, `heng_zhe.py`
- INDEX.md to see what's in the bank

## Renderer
turtle + postscript, NO subprocess.

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from heng_zhe import draw as draw_hz
```

## Approach
Same c11/c12/c13 measure-and-place pattern. For 王 specifically, push shu scale to span the GT shu length closer to 1:1 (not 0.48).

## Output
`attempts/cycle_15/generated.py` + 3 PNGs with CHINESE filenames (01_王.png, 02_土.png, 03_口.png).
