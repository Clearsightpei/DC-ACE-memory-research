# Cycle 16 — 人 (user-requested) + 大 (c14 carry) + 不 (c14 carry)

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Known difficulty: brushed pie/na vs thin MMH GT

Full-size 撇/捺 (canonical scale 0.55+) creates a pixel surplus vs the thin MMH skeleton, which caps `visual_score` around 0.5–0.76. 木 (c14) cleared visual 0.85 because it has heng+shu mass to dilute the diagonal surplus, and pie/na were at scale 0.45.

For 人, 大, 不 — they're more diagonal-heavy. We'll try anyway. If visual < 0.8 they carry over again with structurally-correct renders.

## Tasks

1. **人** (2 strokes): 撇 dominant (long sweep upper-right → lower-left) + 捺 attached to 撇's mid-shaft going lower-right. The 捺 head is BELOW 撇's apex (not shared-apex — the GT has 撇 longer + apex highest).
2. **大** (3 strokes, carry-over): heng on top + 撇 (going down-left from heng's mid) + 捺 (going down-right from same apex). The 撇/捺 cross THROUGH the heng (apex AT the heng).
3. **不** (4 strokes, carry-over): heng on top + 撇 (from below heng's right portion going down-left) + 竖 (hanging from heng's right of center) + 点 (to the right at bottom).

## Hint to improve visual

Use the SHORTEST scales that still produce structurally correct renders. From c14 木: pie scale 0.45 + na scale 0.45 cleared visual 0.85. Aim for pie/na scales ≤ 0.50 for the diagonals.

For 人 specifically: 撇 might still need scale ~0.55-0.60 to span the character, and 捺 ~0.45. Visual likely just under 0.8 still — but try.

## Renderer
turtle + postscript, no subprocess.

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

## Output
`attempts/cycle_16/generated.py` + 3 PNGs with CHINESE filenames (01_人.png, 02_大.png, 03_不.png).
