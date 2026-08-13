"""毛 — 4-stroke radical.

Decomposition (from GT + MMH block):
  s1 撇 (pie): head TC(0.799,0.738) → tail ML(0.771,0.175)
       → px head (180, 74), tail (77, 118)   — short leftward pie at top
  s2 横 (heng, rising): head ML(0.715,0.626) → tail C(0.878,0.395)
       → px head (72, 163), tail (188, 140)  — upper heng, slight rise
  s3 横 (heng, rising, longer): head BL(0.267,0.256) → tail MR(0.186,0.896)
       → px head (27, 226), tail (219, 190)  — lower heng, wider
  s4 竖弯钩 (shu_wan_gou): head C(0.104,0.102) → tail BR(0.733,0.098)
       → px head (110, 110), tail (273, 210) — down through both hengs,
         curl right at bottom, hook up-right

Joint intent:
  s1.mid ⇆ s4.head : N (natural gap ~11px) — do NOT weld the pie's tail
    into s4's top; they should sit near but not touching.
  s2.mid ⇆ s4 : T (welded/tangent) — s4's vertical passes through s2 at
    s2's midpoint (~x=130,y=152). Natural crossing with s4 head at
    (110,110) descending down and slightly right handles this.
  s3.mid ⇆ s4.mid : P (piercing/welded) — s4's vertical body crosses s3
    at ~x=155,y=210 area. Natural crossing.

Bank use: pie, heng (2×), shu_wan_gou — all fit cleanly. No BANK_DEVIATION.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parent.parent.parent / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': None,           # filled after render
    'stroke_count_ok': True,     # 4 primitive calls, matches MMH=4
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'pie + 2× heng + shu_wan_gou; endpoint anchors follow MMH block.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- s1: pie (top-right → lower-left short leftward sweep)
draw_pie(d, head=(180, 74), tail=(77, 118),
         bow_perp=8, w_head=7, w_tail=3)

# ---- s2: upper heng (rising slightly to the right)
draw_heng(d, head=(72, 163), tail=(188, 140),
          width_head=8, width_tail=9)

# ---- s3: lower heng (longer, more rise)
draw_heng(d, head=(27, 226), tail=(219, 190),
          width_head=8, width_tail=9)

# ---- s4: shu-wan-gou (down through both hengs, curl right, hook up)
draw_shu_wan_gou(d, head=(110, 110), tail=(273, 210),
                 width=7, bottom_extra=55, knee_ratio=0.85)

out = Path(__file__).parent / "01_毛.png"
img.save(out)
print(f"wrote {out}")
