# Cycle 14 — 大 / 木 / 不

Hard gate (4): OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Risk note from c13

生 (which contains a short 撇) passed at visual 0.86 because the 撇 is small (scale 0.32) so the brushwork pixel surplus is small. Full-sized 撇/捺 in 八/人/入 capped at visual 0.76. For 大/木/不 the 撇 and 捺 are mid-sized — visual_score is uncertain.

## Tasks

1. **大** (dà, 3 strokes): heng + 撇 + 捺. Heng spans high, 撇 sweeps down-left from apex below heng's center, 捺 sweeps down-right from same apex. Heng on TOP. This is the c5/c10 lesson chars + a horizontal cap.
2. **木** (mù, 4 strokes): heng + shu (through heng's midpoint) + 撇 (mid-shaft going down-left) + 点 (mid-shaft going down-right). Note: in standard 楷书 木 the last stroke is 点 not 捺, similar to 朩 stylistic.
3. **不** (bù, 4 strokes): heng + 撇 (through heng's right-middle going down-left) + 竖 (through heng's middle hanging) + 点 (to the right at bottom).

## Reuse opportunities

- `heng.py`, `shu.py`, `pie.py`, `na.py`, `dian.py`
- For 木: `sheng.py` (c13) has a similar pie+heng+heng+shu pattern; the layout differs.

## Renderer

Same turtle + postscript pattern. NO subprocess. `t.reset()` between tasks.

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from na   import draw as draw_na
from dian import draw as draw_dian
```

## Approach
Measure GT → set (ox, oy, scale). Use the same scipy.ndimage.label decomposition that worked in c12/c13.

## Self-preview
Max 2 iterations. Verify:
- 大: 撇 and 捺 meet at single apex below the heng (heng is HORIZONTAL CAP)
- 木: 4 strokes — heng at top + vertical shu + 撇 going lower-left + dot (or short 捺) going lower-right
- 不: heng at TOP, with 撇/竖/点 hanging below

## Output

`attempts/cycle_14/generated.py` + 3 PNGs at `attempts/cycle_14/0K_<char>.png` (CHINESE char filename, NOT pinyin).
