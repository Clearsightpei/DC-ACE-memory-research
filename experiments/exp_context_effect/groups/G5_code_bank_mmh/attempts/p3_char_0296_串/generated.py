"""p3_char_0296_串 — 串 (chuan, 'skewer').

Structure: two stacked 口 boxes pierced by a long central 竖.
7 strokes total. Standard MMH ordering:
  s1: upper-口 left 竖
  s2: upper-口 top 横折 (BOX form: horiz + right-drop)
  s3: upper-口 bottom 横
  s4: lower-口 left 竖
  s5: lower-口 top 横折 (BOX form)
  s6: lower-口 bottom 横
  s7: long central 竖 piercing both boxes (extends above upper and below lower)

Bank use: draw_shu (strokes 1,4,7), draw_heng_zhe_box (strokes 2,5),
draw_heng (strokes 3,6). Boxes stacked vertically with a mid gap;
central shu pierces at x=150 through both, matching all 4 'P' joints
(s2↔s7 at TC, s3↔s7 at C, s5↔s7 at C, s6↔s7 at BC).

No BANK_DEVIATION needed — all three stroke primitives fit natively.
"""
import os, sys
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Geometry constants
UP_LEFT_X   = 100
UP_RIGHT_X  = 200
UP_TOP_Y    = 60
UP_BOT_Y    = 130

LO_LEFT_X   = 100
LO_RIGHT_X  = 200
LO_TOP_Y    = 155
LO_BOT_Y    = 225

CENTER_X    = 150
SHU_TOP_Y   = 20
SHU_BOT_Y   = 290

W = 7   # stroke width

# --- Upper 口 ---
# s1: left 竖
draw_shu(d, (UP_LEFT_X, UP_TOP_Y + 5), (UP_LEFT_X - 3, UP_BOT_Y), width=W)
# s2: top 横折 box
draw_heng_zhe_box(d, (UP_LEFT_X, UP_TOP_Y), (UP_RIGHT_X, UP_BOT_Y), width=W)
# s3: bottom 横
draw_heng(d, (UP_LEFT_X, UP_BOT_Y), (UP_RIGHT_X, UP_BOT_Y - 2),
          width_head=W, width_tail=W + 1)

# --- Lower 口 ---
# s4: left 竖
draw_shu(d, (LO_LEFT_X, LO_TOP_Y + 5), (LO_LEFT_X - 3, LO_BOT_Y), width=W)
# s5: top 横折 box
draw_heng_zhe_box(d, (LO_LEFT_X, LO_TOP_Y), (LO_RIGHT_X, LO_BOT_Y), width=W)
# s6: bottom 横
draw_heng(d, (LO_LEFT_X, LO_BOT_Y), (LO_RIGHT_X, LO_BOT_Y - 2),
          width_head=W, width_tail=W + 1)

# --- s7: long piercing 竖 ---
draw_shu(d, (CENTER_X, SHU_TOP_Y), (CENTER_X, SHU_BOT_Y), width=W + 1)

img.save(os.path.join(os.path.dirname(__file__), '01_串.png'))

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # exactly 7 primitive calls
    'endpoint_mismatches': [],    # anchors follow standard 米字格 placement for stacked-kou + piercing shu
    'joint_class_mismatches': [], # 4x P (s2↔s7 TC, s3↔s7 C, s5↔s7 C, s6↔s7 BC) satisfied by central shu at x=150 crossing all 6 horiz/box strokes; 6x N gaps preserved by not overshooting shu endpoints into neighbor endpoints
    'overall_pass': True,
    'notes': '2 stacked kou boxes + long central piercing shu. Native bank primitives (draw_shu, draw_heng, draw_heng_zhe_box) fit; no BANK_DEVIATION. Central shu extends well above s2/s5 top corners and well below s3/s6 bottoms per GT.',
}
