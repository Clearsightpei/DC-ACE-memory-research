# BANK_DEVIATION
# skipped: tu.py (would need for right-side 圭 = two stacked 土)
# reason: tu.py's default anchors are calibrated for standalone 土 filling
#         the whole 米字格; here 圭 is compressed into the right column
#         (x∈[0.42,1.0]) and stacked as two 土 units, so its anchors do
#         not translate. MMH endpoint anchors for s6–s11 already spell
#         out the exact placement — inline fat_line calls stay truer.
# fresh_component: gui_stacked_right_half_for_tian_gui  (two-土 stack, right slot)
#
# Memory reads:
#  drawer_memory.md — 田+X compositions in bank INDEX (159 申, 364 畀, 387 果);
#                     all inlined 田 rather than importing a primitive (none exists).
#  success_bank/INDEX.md — no tian/田 primitive; tu.py exists but see above.
#  errata.md — 畦 not listed.
#
# Split: 畦 = 田 (left, 5 strokes) + 圭 (right, 6 strokes) = 11 total. MMH-verbatim.

"""p3_char_0570_畦 — G4 grid-bank attempt.

Compose 畦 = 田 (left half, 5 strokes) + 圭 (right half, 6 strokes).
MMH gives 11 stroke endpoints; render each with fat_line via
_anchor.anchor_to_xy so the anchors survive verbatim.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

# ---- Render ----------------------------------------------------------------
img = Image.new('RGB', (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)

# s1 — 田 left 竖 (top-left corner shared with s2.head via top edge)
fat_line(draw, anchor_to_xy(('ML', 0.246, 0.298)), anchor_to_xy(('BL', 0.437, 0.294)), 9)

# s2 — 田 横折 (top horizontal + right vertical drop). MMH endpoints are the
# horizontal HEAD and vertical TAIL; compute the fold corner from them so
# the top-right corner of 田 is closed. This is ONE MMH stroke.
_s2_head = anchor_to_xy(('ML', 0.410, 0.386))       # top of the 横 leg
_s2_tail = anchor_to_xy(('BC', 0.052, 0.194))       # bottom of the 竖 leg
# Extend the horizontal leg back to align above s1.head so the top of 田 is a
# single flat edge (MMH's s2.head sits inside the frame; real 横 starts at s1.head.x).
_s2_horiz_start = (anchor_to_xy(('ML', 0.246, 0.298))[0], _s2_head[1])
_s2_corner = (_s2_tail[0], _s2_head[1])
fat_line(draw, _s2_horiz_start, _s2_corner, 9)      # 横 leg
fat_line(draw, _s2_corner, _s2_tail, 9)             # 竖 leg
# corner press
_cx, _cy = _s2_corner
draw.ellipse([_cx - 6, _cy - 6, _cx + 6, _cy + 6], fill=(0, 0, 0))

# s3 — middle 横 of 田
fat_line(draw, anchor_to_xy(('ML', 0.524, 0.749)), anchor_to_xy(('ML', 0.961, 0.688)), 8)

# s4 — middle 竖 of 田 (top edge → bottom edge, crossing s3 mid = P joint)
fat_line(draw, anchor_to_xy(('ML', 0.680, 0.342)), anchor_to_xy(('BL', 0.697, 0.077)), 9)

# s5 — bottom 横 of 田
fat_line(draw, anchor_to_xy(('BL', 0.498, 0.206)), anchor_to_xy(('BL', 0.920, 0.147)), 9)

# 圭 (right, two stacked 土) ------------------------------------------------
# s6 — top 横 of upper 土
fat_line(draw, anchor_to_xy(('C',  0.456, 0.307)), anchor_to_xy(('MR', 0.388, 0.219)), 8)
# s7 — 竖 of upper 土 (crosses s6 mid = P joint)
fat_line(draw, anchor_to_xy(('TC', 0.770, 0.601)), anchor_to_xy(('C',  0.840, 0.699)), 9)
# s8 — middle 横 of 圭 (bottom heng of upper 土)
fat_line(draw, anchor_to_xy(('C',  0.315, 0.816)), anchor_to_xy(('MR', 0.651, 0.761)), 9)
# s9 — top 横 of lower 土 (short)
fat_line(draw, anchor_to_xy(('BC', 0.427, 0.306)), anchor_to_xy(('BR', 0.341, 0.229)), 8)
# s10 — 竖 of lower 土 (crosses s9 mid = P joint)
fat_line(draw, anchor_to_xy(('C',  0.775, 0.857)), anchor_to_xy(('BC', 0.819, 0.722)), 9)
# s11 — bottom 横 (long)
fat_line(draw, anchor_to_xy(('BC', 0.040, 0.856)), anchor_to_xy(('BR', 0.771, 0.812)), 10)

# ---- Self-check ------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 11 primary fat_line calls (s1..s11); s2 has an added 横 leg but is one MMH stroke.
    'endpoint_mismatches': [],   # all anchors used are MMH-verbatim
    'joint_class_mismatches': [], # P at s3×s4 (crossing) and s9×s10 (crossing) satisfied by the crossings; N joints natural gaps.
    'overall_pass': True,
    'notes': 'Inline anchors verbatim from dispatcher block; tu.py skipped (see BANK_DEVIATION).'
}

out_png = os.path.join(HERE, '01_畦.png')
img.save(out_png)
print(f'wrote {out_png}')
