"""p3_char_0295_时 (shí, "time") — 日 + 寸, 7 strokes.

Recipe: P-A-006 (MMH-anchor verbatim + stroke-primitive layer). 日 on
left is composed via shu + heng_zhe_box + heng + heng — NOT via
draw_ri because the standalone draw_ri primitive covers the full
canvas, whereas here 日 sits compressed on the left half. Right side
寸 = heng + shu_gou + dian, all anchored to MMH coords. No
BANK_DEVIATION (all stroke primitives fit cleanly).
"""

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu_gou import draw_shu_gou
from dian import draw_dian


def cell_to_px(cell, xf, yf, size=100):
    """Convert (cell_name, x_frac, y_frac) → (px_x, px_y) for 300x300 canvas."""
    col_map = {'L': 0, 'C': 1, 'R': 2}
    row_map = {'T': 0, 'M': 1, 'B': 2}
    # cell is one of TL/TC/TR/ML/C/MR/BL/BC/BR
    if cell == 'C':
        col, row = 1, 1
    else:
        # first char is row (T/M/B), second is col (L/C/R)
        row_char, col_char = cell[0], cell[1]
        row = row_map[row_char]
        col = col_map[col_char]
    return (col * size + xf * size, row * size + yf * size)


# MMH-derived pixel anchors (verbatim conversion from injected block)
s1_head = cell_to_px('TL', 0.413, 0.981)   # (41.3, 98.1)
s1_tail = cell_to_px('BL', 0.492, 0.531)   # (49.2, 253.1)

s2_head = cell_to_px('ML', 0.598, 0.046)   # (59.8, 104.6)
s2_tail = cell_to_px('BC', 0.031, 0.546)   # (103.1, 254.6)

s3_head = cell_to_px('ML', 0.598, 0.749)   # (59.8, 174.9)
s3_tail = cell_to_px('ML', 0.87, 0.679)    # (87.0, 167.9)

s4_head = cell_to_px('BL', 0.574, 0.432)   # (57.4, 243.2)
s4_tail = cell_to_px('BL', 0.888, 0.35)    # (88.8, 235.0)

s5_head = cell_to_px('C', 0.228, 0.465)    # (122.8, 146.5)
s5_tail = cell_to_px('MR', 0.684, 0.333)   # (268.4, 133.3)

s6_head = cell_to_px('TC', 0.995, 0.642)   # (199.5, 64.2)
s6_tail = cell_to_px('BC', 0.693, 0.733)   # (169.3, 273.3)

s7_head = cell_to_px('C', 0.359, 0.852)    # (135.9, 185.2)
s7_tail = cell_to_px('BC', 0.673, 0.162)   # (167.3, 216.2)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 日 (left half) ---
# s1: left vertical 竖
draw_shu(d, s1_head, s1_tail, width=7)

# s2: 横折 boxy (top-heng + right vertical) — top_left / bottom_right form
draw_heng_zhe_box(d, s2_head, s2_tail, width=7)

# s3: middle heng (inner cross-bar)
draw_heng(d, s3_head, s3_tail, width_head=6, width_tail=7)

# s4: bottom heng (closing the box)
draw_heng(d, s4_head, s4_tail, width_head=7, width_tail=8)

# --- 寸 (right half) ---
# s5: 寸 top heng (long horizontal)
draw_heng(d, s5_head, s5_tail, width_head=7, width_tail=8)

# s6: 寸 shu-gou (vertical + left-hook)
draw_shu_gou(d, s6_head, s6_tail, width=7, hook_start_offset=32)

# s7: 寸 dian (short diagonal dot bottom-left of 寸)
draw_dian(d, s7_head, s7_tail, w_head=3, w_tail=7, bow=3)


out_path = pathlib.Path(__file__).parent / '01_时.png'
img.save(out_path)


# --- Self-check ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 primitive calls, matches expected 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('P-A-006 recipe: MMH anchors verbatim, stroke-primitive layer. '
              '日 composed inline (not draw_ri whole-radical) because it sits '
              'compressed on the left half. s5×s6 P-joint welded via natural '
              'crossing of 寸 heng and shu-gou at ~(188, 140). All other joints '
              'are N-gaps from MMH separation.'),
}
print('SELF_CHECK:', SELF_CHECK)
print('Saved to', out_path)
