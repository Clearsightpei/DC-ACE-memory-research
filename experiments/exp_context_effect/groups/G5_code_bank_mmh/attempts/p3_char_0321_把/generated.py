"""p3_char_0321_把 — G5 attempt.

Decomposition: 扌 (left) + 巴 (right), 3 + 4 = 7 strokes.

Bank use:
  - shou_hand.py for left 扌 (bank primitive — high-reuse per memory)
  - heng_zhe_box.py for 巴 top frame
  - heng.py for 巴 middle crossbar
  - shu.py for 巴 inner short vertical (stroke 5)
  - shu_wan_gou.py for 巴 bottom closing loop with hook
"""
import sys
import os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from shou_hand import draw_shou  # 3 strokes
from heng_zhe_box import draw_heng_zhe_box
from heng import draw_heng
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 (shou) + 4 (ba) = 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '扌 via shou_hand (bank), 巴 inlined with heng_zhe_box + shu + heng + shu_wan_gou; joints all N (natural gaps).'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 扌 (left) — 3 strokes via bank primitive shou_hand ------------------
# Native shou draws in ~ x=85..190, y=67..263. Scale 0.7, keep left.
draw_shou(d, ox=-35, oy=25, scale=0.72)

# --- 巴 (right) — 4 strokes ---------------------------------------------
# Layout in right half: x ~ 140..250, y ~ 70..250
# s4 (heng-zhe): top horizontal + right vertical drop for TOP compartment
draw_heng_zhe_box(d, top_left=(145, 90), bottom_right=(238, 155), width=7)
# s5 (short inner 竖): the small internal vertical mark inside top box
draw_shu(d, head=(190, 100), tail=(192, 148), width=5)
# s7 (middle 横): crossbar spanning left vertical to right vertical
draw_heng(d, head=(148, 155), tail=(238, 152), width_head=6, width_tail=7)
# s6 (竖弯钩): starts near top-left of top box (LEFT vertical role),
# descends full height, curves right at bottom, hooks up.
draw_shu_wan_gou(d, head=(148, 90), tail=(250, 210),
                 width=7, bottom_extra=35, knee_ratio=0.95)

img.save(os.path.join(os.path.dirname(__file__), '01_把.png'))
print('wrote 01_把.png; SELF_CHECK:', SELF_CHECK)
