# Cycle 22 — 本 retry + 六 retry + 七 retry (all carry-overs)

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Tasks (from to_be_learned.md)

### Task 1 — 本 (c21 v=0.76, just under)

**Problem**: bottom heng dash + 木 base both at full brushwork width, plus the small dash adds little Dice gain. The character's pixel mass slightly outpaints the GT.

**Fix attempt**: shrink the bottom dash slightly to scale 0.22 (was 0.30) so it adds clean structural info without piling extra brushwork off the GT skeleton. Also try moving the dash closer to where the pie/na heads are (oy ~ -50 instead of -65) — see what the GT centerline says.

```python
draw_mu(t)  # base 木
draw_heng(t, ox=-2, oy=-50, scale=0.22)  # smaller bottom dash, slightly higher
```

### Task 2 — 六 (c19 v=0.74)

**Problem**: 撇 + dian at the bottom create some pixel surplus from diagonals. 六 has top dot + heng + bottom 撇/dian pair.

**Fix attempt**: scale down the 撇 to 0.22 (was 0.28) and the right dian to 1.5 (was 2.0). Keep the top heng and top dian as-is.

### Task 3 — 七 (c12 v=0.76, c17 v=0.79 — right at the boundary)

**Problem**: shu_wan_gou's brushwork over-paints the thin GT.

**Fix attempt**: shrink the shu_wan_gou to scale ~0.78 (was 0.96 in c17) so the brushwork covers less surplus area. Then re-position the crossing heng accordingly.

## Renderer (turtle + postscript)

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from dian import draw as draw_dian
from shu_wan_gou import draw as draw_swg
from mu import draw as draw_mu
```

## Output

`attempts/cycle_22/generated.py` + 3 PNGs (CHINESE filenames).
