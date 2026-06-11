# Cycle 20 — 末 / 未 / 五 (carry-overs with specific fixes)

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## What went wrong before

- **末** (c18 v=0.63): Drawer used `draw_mu(t)` verbatim and added heng on top. But 木 in MMH 末 is positioned LOWER on the canvas to make room for the top heng. Calling draw_mu unchanged left 木 at its original position, overlapping the new top heng.
- **未** (c18 v=0.65): Same root cause as 末.
- **五** (c19 v=0.70, OCR'd as 左): Drawer's stroke decomposition was over-complex. Read the GT carefully — 五 is heng + 竖 + heng + 横折 (or actually heng + shu + heng + heng_zhe_gou with a closing heng).

## Tasks

### 末

The MMH 末 has the 木-component shifted DOWN. The top heng is at oy ~ +110-130 (above the original 木's heng at oy=13).

Suggested: shift the 木 component DOWN by ~30-50px and shrink slightly to ~scale 0.85:
```python
draw_mu(t, oy=-40, scale=0.85)
draw_heng(t, ox=-3, oy=120, scale=0.85)  # LONG top heng
```

### 未

Similar to 末 but the top heng is SHORTER than the middle heng. (末: top > middle; 未: top < middle.)
```python
draw_mu(t, oy=-40, scale=0.85)
draw_heng(t, ox=-3, oy=120, scale=0.50)  # SHORT top heng (under middle's 0.55-equivalent)
```

### 五

Read the GT. Standard MMH stroke decomposition for 五: heng (top) + shu (left vertical short slant) + heng (middle short) + heng_zhe (right side forming the closing right-vertical-and-bottom-heng).

Alternative simpler reading: heng + shu + heng + heng + heng_zhe (5 turtle calls). Try:
```python
draw_heng(t, ox=, oy=+90, scale=0.70)   # top heng
draw_shu(t,  ox=-100, oy=+10, scale=0.5)  # short left slant (might use pie scale ~0.3 for slant)
draw_heng(t, ox=, oy=0, scale=0.40)    # middle heng
draw_heng(t, ox=, oy=-130, scale=0.85)   # bottom heng
draw_shu(t,  ox=+100, oy=-65, scale=0.4)  # right closing shu
```
Or use heng_zhe for the right corner.

## Renderer
turtle + postscript, no subprocess.

```python
from heng import draw as draw_heng
from shu  import draw as draw_shu
from heng_zhe import draw as draw_hz
from heng_zhe_gou import draw as draw_hzg
from mu import draw as draw_mu
```

## Output
`attempts/cycle_20/generated.py` + 3 PNGs (CHINESE filenames: 01_末.png, 02_未.png, 03_五.png).
Self-preview ≤2 iterations. Measure GTs precisely.
