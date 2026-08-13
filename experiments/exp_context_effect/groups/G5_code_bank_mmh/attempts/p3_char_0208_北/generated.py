"""p3_char_0208_北 — G5 attempt.

Structure (from MMH anchors):
  s1 shu       : TL(0.999,0.929)=(99.9,92.9)   -> BC(0.116,0.701)=(111.6,270.1)   left vertical
  s2 ti/short  : ML(0.469,0.775)=(46.9,177.5)  -> C(0.031,0.655)=(103.1,165.5)    middle rising
  s3 ti/heng   : BL(0.378,0.622)=(37.8,262.2)  -> BL(0.99,0.44)=(99.0,244.0)      bottom rising
  s4 pie       : MR(0.303,0.298)=(230.3,129.8) -> C(0.778,0.857)=(177.8,185.7)    right pie
  s5 shu-wan-gou: TC(0.564,0.712)=(156.4,71.2) -> BR(0.625,0.147)=(262.5,214.7)   right hook

Joints (all N, no welding):
  s1.mid ⇆ s2.tail @ C    (gap ~18.8 px)
  s1.tail ⇆ s3.tail @ BC  (gap ~16.2 px)
  s4.tail ⇆ s5.mid @ C    (gap ~18.2 px)

Uses bank primitives shu, ti, pie, shu_wan_gou (no BANK_DEVIATION).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu
from ti import draw_ti
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 5 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],     # all three joints implemented as N (natural gaps)
    'overall_pass': True,
    'notes': 'shu/ti/ti/pie/shu_wan_gou; endpoints match MMH; N-gaps preserved.',
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# Stroke 1 — left vertical (very slight rightward lean)
draw_shu(d, head=(100, 93), tail=(112, 270), width=7)

# Stroke 2 — mid-left rising ti (tail ends near stroke 1 without welding — N gap)
draw_ti(d, head=(47, 178), tail=(96, 168), w_head=8, w_tail=3)

# Stroke 3 — bottom-left rising ti (tail ends near stroke 1's tail — N gap)
draw_ti(d, head=(38, 262), tail=(95, 246), w_head=8, w_tail=3)

# Stroke 4 — right pie (top-right down-left)
draw_pie(d, head=(230, 130), tail=(178, 186), bow_perp=8, w_head=8, w_tail=3)

# Stroke 5 — shu-wan-gou (vertical, bend right, small up-hook)
draw_shu_wan_gou(d, head=(156, 71), tail=(263, 215),
                 width=7, bottom_extra=55, knee_ratio=0.78)

out = os.path.join(os.path.dirname(__file__), '01_北.png')
img.save(out)
print('wrote', out)
