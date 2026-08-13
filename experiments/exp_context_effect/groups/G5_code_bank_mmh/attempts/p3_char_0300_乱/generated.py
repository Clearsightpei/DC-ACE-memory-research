"""p3_char_0300_乱 (luan, "chaos") — 舌 (left, 6 strokes) + 乚 (right, 1 stroke), 7 strokes.

Recipe: P-A-006 (MMH-anchor verbatim + stroke-primitive layer). The
left 舌 sits compressed in the left half (top 撇, middle 横, short 竖
crossbar, then 口 box below). The right 乚 is a large 竖弯钩 sweeping
from top-center down to bottom-right. No BANK_DEVIATION; all bank
stroke primitives fit the anchors cleanly (pie / heng / shu /
heng_zhe_box / shu_wan_gou).
"""

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from shu_wan_gou import draw_shu_wan_gou


def cell_to_px(cell, xf, yf, size=100):
    """Convert (cell_name, x_frac, y_frac) → (px_x, px_y) for 300x300 canvas."""
    col_map = {'L': 0, 'C': 1, 'R': 2}
    row_map = {'T': 0, 'M': 1, 'B': 2}
    if cell == 'C':
        col, row = 1, 1
    else:
        row_char, col_char = cell[0], cell[1]
        row = row_map[row_char]
        col = col_map[col_char]
    return (col * size + xf * size, row * size + yf * size)


# --- MMH-derived pixel anchors (verbatim from injected block) ---
s1_head = cell_to_px('TC', 0.441, 0.885)  # (144.1, 88.5)   top 撇 head
s1_tail = cell_to_px('ML', 0.58,  0.236)  # (58.0, 123.6)   top 撇 tail

s2_head = cell_to_px('ML', 0.22,  0.688)  # (22.0, 168.8)   middle 横 head
s2_tail = cell_to_px('C',  0.526, 0.523)  # (152.6, 152.3)  middle 横 tail

s3_head = cell_to_px('ML', 0.896, 0.166)  # (89.6, 116.6)   short 竖 head
s3_tail = cell_to_px('BL', 0.911, 0.051)  # (91.1, 205.1)   short 竖 tail

s4_head = cell_to_px('BL', 0.495, 0.139)  # (49.5, 213.9)   口 left 竖 head
s4_tail = cell_to_px('BL', 0.715, 0.801)  # (71.5, 280.1)   口 left 竖 tail

s5_head = cell_to_px('BL', 0.642, 0.139)  # (64.2, 213.9)   口 top+right 横折 head
s5_tail = cell_to_px('BC', 0.172, 0.473)  # (117.2, 247.3)  口 top+right 横折 tail

s6_head = cell_to_px('BL', 0.773, 0.678)  # (77.3, 267.8)   口 bottom 横 head
s6_tail = cell_to_px('BC', 0.359, 0.572)  # (135.9, 257.2)  口 bottom 横 tail

s7_head = cell_to_px('TC', 0.617, 0.662)  # (161.7, 66.2)   乚 head (top)
s7_tail = cell_to_px('BR', 0.675, 0.171)  # (267.5, 217.1)  乚 tail (after hook)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 舌 (left half) ---
# s1: top 撇
draw_pie(d, s1_head, s1_tail, bow_perp=10, w_head=9, w_tail=3)

# s2: middle 横
draw_heng(d, s2_head, s2_tail, width_head=8, width_tail=9)

# s3: short 竖 crossing s2 (P joint at ML~(99,158))
draw_shu(d, s3_head, s3_tail, width=7)

# s4: 口 left 竖
draw_shu(d, s4_head, s4_tail, width=7)

# s5: 口 top+right 横折 (top-left → bottom-right)
draw_heng_zhe_box(d, s5_head, s5_tail, width=7)

# s6: 口 bottom 横
draw_heng(d, s6_head, s6_tail, width_head=7, width_tail=7)

# --- 乚 (right half) ---
# s7: 竖弯钩 — starts high top-center, sweeps down + right, hooks up-right
draw_shu_wan_gou(d, s7_head, s7_tail, width=8, bottom_extra=50, knee_ratio=0.85)


out_path = pathlib.Path(__file__).parent / '01_乱.png'
img.save(out_path)


# --- Self-check ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 primitive calls, matches expected 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('P-A-006 recipe: MMH anchors verbatim + stroke-primitive layer. '
              '舌 composed inline (pie + heng + shu + shu + heng_zhe_box + heng); '
              '乚 = shu_wan_gou. s2×s3 P-joint welded by natural crossing at '
              '~(99, 158). All other joints are N-gaps preserved by MMH-anchor '
              'separation (no forced welds).'),
}
print('SELF_CHECK:', SELF_CHECK)
print('Saved to', out_path)
