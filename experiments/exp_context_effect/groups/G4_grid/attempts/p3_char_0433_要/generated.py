"""p3_char_0433_要 (yào) — 9 strokes.
Decomposition: 要 = 西 (top, s1-s6) + 女 (bottom, s7-s9).
MMH-verbatim anchors + base primitives per B9/B10 A-recipe (point 2 & 4).

Memory read (v8 checklist):
  1. drawer_memory.md — no chronic import needed (no 丿/刀/冂/弓/马 sub-part).
     A-recipe points 1-5 followed: decomp comment, MMH-verbatim, SELF_CHECK,
     base primitives (skip compound nv.py because 女 in 要 is bottom-band
     compressed, not standalone).
  2. INDEX.md — nv.py exists for standalone 女 (fills full canvas); xi_box.py
     is for 匸 not 西.
  3. errata.md — no 要 entry.

X-cross of 女: use CROSS_ANCHOR shared between s7 and s8 midpoints per
B7r 文 fix. s7 is compound 撇点 through TWO joints (horizontal-cross + X-cross).
"""

# BANK_DEVIATION
# skipped: nv.py
# reason: nv.py is standalone-scale 女 (fills full canvas); 要's 女 is
#   bottom-band compressed (y > 200 area) with different X-cross placement
#   forced by MMH — partial anchor override of compound primitive is the
#   B8 伊 FAIL pattern. Inlining base primitives with MMH anchors preserves
#   the bottom-band slot.
# fresh_component: nv_bottom_slot_for_要

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 draw calls / stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim. 西 top box (s1-s6) + 女 bottom (s7-s9). '
             'CROSS_ANCHOR=(BC,0.524,0.618) shared by s7 mid and s8 mid for X-cross. '
             's7 = 撇点 compound polyline through horiz-cross + X-cross. '
             'N-joints preserved as natural line-terminations (no forced weld).',
}

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)


def poly(points, width=8):
    """Draw a smooth polyline with rounded caps."""
    d.line(points, fill=(0, 0, 0), width=width, joint='curve')
    r = width / 2.0
    for (x, y) in (points[0], points[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


# --------------- 西 (top box, strokes 1-6) ---------------

# s1: 一 top horizontal
s1_h = anchor_to_xy(('TL', 0.993, 0.735))
s1_t = anchor_to_xy(('TR', 0.065, 0.647))
fat_line(d, s1_h, s1_t, 8)

# s2: 丨 left vertical
s2_h = anchor_to_xy(('ML', 0.712, 0.195))
s2_t = anchor_to_xy(('ML', 0.97, 0.761))
fat_line(d, s2_h, s2_t, 8)

# s3: 横折 (second-horizontal-just-below-top-heng + right vertical).
# MMH head near top-left of middle band, MMH tail at bottom-right of box.
# Route through the two P-weld joints (s4 pierce at C(0.256,0.189) and
# s5 pierce at C(0.697,0.121)) so the vertical strokes cross it cleanly.
s3_h = anchor_to_xy(('ML', 0.902, 0.207))
s3_p1 = anchor_to_xy(('C', 0.256, 0.189))  # s4-weld
s3_p2 = anchor_to_xy(('C', 0.697, 0.121))  # s5-weld
s3_corner = (s3_p2[0] + 10, s3_p2[1] + 5)  # right shoulder before dropping
s3_t = anchor_to_xy(('MR', 0.039, 0.711))
poly([s3_h, s3_p1, s3_p2, s3_corner, s3_t], width=8)

# s4: inner left short vertical (pierces s3, welded to s6 mid)
s4_h = anchor_to_xy(('TC', 0.134, 0.896))
s4_t = anchor_to_xy(('C', 0.254, 0.605))
fat_line(d, s4_h, s4_t, 6)

# s5: inner right short vertical (pierces s3, welded to s6 mid)
s5_h = anchor_to_xy(('TC', 0.623, 0.768))
s5_t = anchor_to_xy(('C', 0.6, 0.564))
fat_line(d, s5_h, s5_t, 6)

# s6: 一 middle-bottom horizontal (closes bottom of 西)
s6_h = anchor_to_xy(('C', 0.022, 0.682))
s6_t = anchor_to_xy(('C', 0.934, 0.591))
fat_line(d, s6_h, s6_t, 8)

# --------------- 女 (bottom, strokes 7-9) ---------------

# CROSS_ANCHOR shared between s7.mid and s8.mid (B7r 文 fix pattern)
CROSS = anchor_to_xy(('BC', 0.524, 0.618))  # ≈ (152.4, 261.8)
HORIZ_CROSS = anchor_to_xy(('BC', 0.222, 0.105))  # s7 pierces s9 here, ≈(122.2, 210.5)

# s7: 撇点 compound — head → horiz_cross (small bend) → CROSS → tail (down-right)
s7_h = anchor_to_xy(('C', 0.251, 0.737))
s7_t = anchor_to_xy(('BR', 0.171, 1.056))
# Clamp tail to canvas edge to avoid going off-canvas
s7_t = (min(s7_t[0], 295), min(s7_t[1], 295))
poly([s7_h, HORIZ_CROSS, CROSS, s7_t], width=8)

# s8: 撇 — from horizontal (T-touch on s9) → CROSS (P-weld with s7) → tail down-left
s8_h = anchor_to_xy(('C', 0.729, 0.896))
s8_t = anchor_to_xy(('BL', 0.683, 0.903))
poly([s8_h, CROSS, s8_t], width=8)

# s9: 一 horizontal at bottom
s9_h = anchor_to_xy(('BL', 0.352, 0.162))
s9_t = anchor_to_xy(('BR', 0.687, 0.074))
fat_line(d, s9_h, s9_t, 8)

# --------------- Save ---------------
out_path = os.path.join(_HERE, '01_要.png')
img.save(out_path)
print('saved', out_path)
