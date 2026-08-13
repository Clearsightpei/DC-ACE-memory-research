"""p2_radical_029_亻 — G5 attempt.

Structure per MMH block:
  s1 (pie): head TC(0.588, 0.738) → (158.8, 73.8)
            tail BL(0.806, 0.112) → (80.6, 211.2)
  s2 (shu): head C (0.389, 0.582) → (138.9, 158.2)
            tail BC(0.441, 0.927) → (144.1, 292.7)

Joint: s1.mid(0.48) ⇆ s2.head at cell C — class N (neighbor gap).
We place s2's head where MMH says, which sits naturally offset from
the pie's midpoint (no welding required — the gap emerges).

Using bank primitives: pie.draw_pie, shu.draw_shu.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's1=pie via bank; s2=shu via bank. N joint emerges naturally from MMH anchors.',
}

import sys
import pathlib

HERE = pathlib.Path(__file__).resolve()
BANK = HERE.parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# stroke 1: 撇 (pie) — upper-right head sweeping down to lower-left tail
s1_head = (158.8, 73.8)
s1_tail = (80.6, 211.2)
draw_pie(d, s1_head, s1_tail, bow_perp=16, w_head=9, w_tail=3, steps=80)

# stroke 2: 竖 (shu) — short vertical dropping from mid to lower area.
# GT shows a soft top curl entry (like 丨's top_curl) — enable it.
s2_head = (138.9, 158.2)
s2_tail = (144.1, 292.7)
draw_shu(d, s2_head, s2_tail, width=7, top_curl=True)

out_png = HERE.parent / '01_亻.png'
img.save(out_png)
print(f'Wrote {out_png}')
