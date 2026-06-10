# Cycle 17 — 七 (c12 carry) + 口 (c15 carry) + 中

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Tasks

1. **七** (2 strokes, carry-over): 横 (slight tilt) + 竖弯钩 (vertical drop + curve right + small upward hook). c12 attempt used heng + shu_wan_gou. Visual was 0.76 — the shu_wan_gou's wide brushwork over-painted the GT skeleton. Consider using a smaller scale for shu_wan_gou OR using a finer Bezier path.

2. **口** (3 strokes, carry-over from c15): box of left-shu + heng_zhe + bottom heng. c15 attempt used shu(scale 0.44) + heng_zhe(0.85) + heng(0.385). Visual was 0.68. Could the box be drawn tighter? Try heavier strokes or different scales.

3. **中** (4 strokes, new): vertical 口 (smaller box) + vertical 竖 (long, piercing through the box). Effectively 口 + central shu. The shu is the dominant vertical stroke.

## Reuse
- heng, shu, heng_zhe, shu_wan_gou, dian
- existing chars in INDEX.md

## Renderer (turtle + postscript, no subprocess)

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from heng_zhe import draw as draw_hz
from shu_wan_gou import draw as draw_swg
```

## Output
`attempts/cycle_17/generated.py` + 3 PNGs (CHINESE filenames).
