# Cycle 13 — 王 / 主 / 生

Hard gate (4): OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Tasks

1. **王** (wáng, 4 strokes): three stacked 横 + one 竖 piercing all. Equivalent to 三 + 竖. Top heng shortest, middle short, bottom long; 竖 through their midpoints.
2. **主** (zhǔ, 5 strokes): 王 with a 点 on top. = 点 + 王.
3. **生** (shēng, 5 strokes): 撇 + 横 + 横 + 竖 + 横. The defining feature: short 撇 stroke at the top-left, then three 横 stacks with a 竖 piercing through the middle two.

## Reuse opportunities

- `san.py` (三) for 王's three heng — translate down slightly + add a 竖.
- `wang` once it exists for 主.
- `heng.py`, `shu.py`, `dian.py`, `pie.py` — primitives.

## Renderer
turtle + postscript. NO subprocess. `t.reset()` between tasks.

```python
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from dian import draw as draw_dian
```

## Approach
Same c11/c12 pattern: measure GT pixel coords, convert to math, set (ox, oy, scale). For 王/主, the 三-like heng stack will need (oy_top, oy_mid, oy_bottom, scales) values; measure from the GT.

## Tips
- 王 horizontal strokes are usually evenly spaced.
- 主 adds a 点 above the top heng.
- 生 has the 撇 at top-left going down-left into the first 横.

## Output

`attempts/cycle_13/generated.py` + 3 PNGs at `attempts/cycle_13/0K_<char>.png` (use the CHINESE char in the filename, not pinyin — judge looks them up by char).
