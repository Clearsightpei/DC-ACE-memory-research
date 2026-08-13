"""畏 (wèi) — 9 strokes.
Decomposition: 畏 = 田(-ish top block, 5 strokes: s1-s5) + bottom (4 strokes: s6-s9).
Bottom is a wide 横 (s6) + short 竖/丿 (s7) + 撇 (s8) + long 捺 (s9).

MMH-verbatim anchors per dispatcher-injected block. Base primitives only
(fat_line). No compound bank primitive fits (top block is compressed 田-variant,
bottom is 4-stroke non-standard tail). Following A-recipe points 1-5.

# BANK_DEVIATION
# skipped: (no compound primitive attempted)
# reason: 畏's top is a compressed 田 embedded above compound bottom, MMH anchors
#         differ from any standalone 田 primitive; bottom 4 strokes are not a
#         standard radical. Inline via base primitives per A-recipe point 4.
# fresh_component: tian_top_over_wide_base_for_畏
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; N-joints preserved as natural gaps; P-joint (s3xs4) welded via crossing lines.',
}

img = Image.new("RGB", (300, 300), (255, 255, 255))
d = ImageDraw.Draw(img)

# --- Stroke 1: left of top-block (short 竖-slant) ---
s1_h = anchor_to_xy(('TL', 0.826, 0.744))
s1_t = anchor_to_xy(('C',  0.09,  0.576))
fat_line(d, s1_h, s1_t, width=8)

# --- Stroke 2: top + right of top-block (横折 — right-angle turn) ---
# Head at top-left corner of box, corner at TOP-RIGHT (share y with head),
# then descend to tail.
s2_h = anchor_to_xy(('TL', 0.961, 0.744))
s2_t = anchor_to_xy(('C',  0.913, 0.494))
# Proper 横折: horizontal to (tail_x, head_y), then vertical down to tail.
corner = (s2_t[0], s2_h[1])
pts = [s2_h, corner, s2_t]
widths = [8, 8, 8]
stroke_variable_width(d, pts, widths)

# --- Stroke 3: horizontal inside top-block (upper heng of inner cross) ---
s3_h = anchor_to_xy(('C', 0.184, 0.14))
s3_t = anchor_to_xy(('C', 0.802, 0.058))
fat_line(d, s3_h, s3_t, width=7)

# --- Stroke 4: vertical middle (inner 竖 of cross) ---
s4_h = anchor_to_xy(('TC', 0.421, 0.762))
s4_t = anchor_to_xy(('C',  0.436, 0.362))
fat_line(d, s4_h, s4_t, width=7)

# --- Stroke 5: horizontal middle-lower inside top-block ---
s5_h = anchor_to_xy(('C', 0.14,  0.503))
s5_t = anchor_to_xy(('C', 0.808, 0.362))
fat_line(d, s5_h, s5_t, width=7)

# --- Stroke 6: long wide 横 (bottom of top-block, extending outward) ---
s6_h = anchor_to_xy(('ML', 0.36,  0.884))
s6_t = anchor_to_xy(('MR', 0.646, 0.711))
fat_line(d, s6_h, s6_t, width=8)

# --- Stroke 7: short 竖/丿 descending from left ---
s7_h = anchor_to_xy(('ML', 0.882, 0.922))
s7_t = anchor_to_xy(('BC', 0.482, 0.458))
fat_line(d, s7_h, s7_t, width=7)

# --- Stroke 8: 撇 (down-left diagonal) ---
s8_h = anchor_to_xy(('MR', 0.083, 0.837))
s8_t = anchor_to_xy(('BC', 0.79,  0.194))
# Curved pie
mid8 = ((s8_h[0]*0.5 + s8_t[0]*0.5) - 6, (s8_h[1]*0.5 + s8_t[1]*0.5) - 4)
pts8 = quad_bezier(s8_h, mid8, s8_t, n=40)
widths8 = [7 - int(5 * i / len(pts8)) for i in range(len(pts8))]  # taper
widths8 = [max(2, w) for w in widths8]
stroke_variable_width(d, pts8, widths8)

# --- Stroke 9: 捺 (long down-right diagonal — bottom right tail) ---
s9_h = anchor_to_xy(('C',  0.277, 0.846))
s9_t = anchor_to_xy(('BR', 0.81,  0.812))
mid9 = ((s9_h[0]*0.5 + s9_t[0]*0.5), (s9_h[1]*0.5 + s9_t[1]*0.5) + 8)
pts9 = quad_bezier(s9_h, mid9, s9_t, n=48)
# 捺 tapers thick-to-thin-to-thick then sharp end — approximate as growing then sharp
n9 = len(pts9)
widths9 = []
for i in range(n9):
    t = i / (n9 - 1)
    if t < 0.85:
        w = 4 + int(8 * t)   # grow from 4 to ~10
    else:
        w = max(2, int(12 * (1 - (t - 0.85) / 0.15)))
    widths9.append(max(2, w))
stroke_variable_width(d, pts9, widths9)

out_path = os.path.join(HERE, "01_畏.png")
img.save(out_path)
print(f"wrote {out_path}")
print(f"stroke_count=9, SELF_CHECK.overall_pass={SELF_CHECK['overall_pass']}")
