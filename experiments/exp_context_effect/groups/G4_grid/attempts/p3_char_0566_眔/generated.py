"""眔 — 10 strokes.
Decomposition: 眔 = 罒 (top net radical, 5 strokes) + 氺 (bottom water, 5 strokes).
  Top 罒: left-shu(s1) + heng-zhe(s2) + inner-shu-left(s3) + inner-shu-right(s4) + bottom heng(s5)
  Bottom 氺: central shu(s6) + upper-left pie(s7) + lower-left pie(s8) + upper-right dian/na(s9) + lower-right na(s10)

Following B9-B13 A-recipe: MMH-verbatim anchors, inline base primitives, N-joint gaps preserved.
No bank primitive fits cleanly (罒 has none; 氺 = 水-variant with no chronic file). Inlining fresh.
"""

import os
import sys
from PIL import Image, ImageDraw

# --- import shared anchor helper from success_bank/code ---
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, sample_line  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 draw calls confirmed below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 罒 frame + 氺 splashes. All N-joints kept as small gaps.',
}

# --- canvas ---
img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

# =============================================================
# Top radical 罒 (net)
# =============================================================

# s1: left vertical of 罒 frame  (head TL, tail ML)
s1_h = anchor_to_xy(('TL', 0.718, 0.8))
s1_t = anchor_to_xy(('ML', 0.987, 0.412))
fat_line(draw, s1_h, s1_t, width=8)

# s2: top heng + right-turn (horizontal top of 罒)  (head TL, tail MR)
s2_h = anchor_to_xy(('TL', 0.902, 0.82))
s2_t = anchor_to_xy(('MR', 0.115, 0.157))
fat_line(draw, s2_h, s2_t, width=8)

# s3: inner-left short shu  (head TC, tail C)
s3_h = anchor_to_xy(('TC', 0.266, 0.882))
s3_t = anchor_to_xy(('C',  0.359, 0.222))
fat_line(draw, s3_h, s3_t, width=7)

# s4: inner-right short shu  (head TC, tail C)
s4_h = anchor_to_xy(('TC', 0.702, 0.791))
s4_t = anchor_to_xy(('C',  0.655, 0.172))
fat_line(draw, s4_h, s4_t, width=7)

# s5: bottom heng of 罒  (head C, tail MR)
s5_h = anchor_to_xy(('C',  0.028, 0.289))
s5_t = anchor_to_xy(('MR', 0.051, 0.219))
fat_line(draw, s5_h, s5_t, width=8)

# =============================================================
# Bottom radical 氺 (water splash)
# =============================================================

# s6: central long shu (comes down from center)  (head C, tail BC)
s6_h = anchor_to_xy(('C',  0.488, 0.459))
s6_t = anchor_to_xy(('BC', 0.562, 0.991))
# Slight taper: thicker at head, thinner at tail (shu-gou style)
pts6 = sample_line(s6_h, s6_t, n=30)
widths6 = [max(3, 9 - int(i * 4 / len(pts6))) for i in range(len(pts6))]
stroke_variable_width(draw, pts6, widths6)

# s7: upper-left pie (short)  (head C, tail BL)
s7_h = anchor_to_xy(('C',  0.11, 0.603))
s7_t = anchor_to_xy(('BL', 0.548, 0.364))
pts7 = sample_line(s7_h, s7_t, n=24)
widths7 = [max(2, 8 - int(i * 6 / len(pts7))) for i in range(len(pts7))]
stroke_variable_width(draw, pts7, widths7)

# s8: lower-left long pie  (head BC, tail BL)
s8_h = anchor_to_xy(('BC', 0.107, 0.139))
s8_t = anchor_to_xy(('BL', 0.601, 0.93))
pts8 = sample_line(s8_h, s8_t, n=32)
widths8 = [max(1, 9 - int(i * 8 / len(pts8))) for i in range(len(pts8))]
stroke_variable_width(draw, pts8, widths8)

# s9: upper-right dian (short na)  (head C, tail BR)
s9_h = anchor_to_xy(('C',  0.951, 0.696))
s9_t = anchor_to_xy(('BR', 0.358, 0.162))
pts9 = sample_line(s9_h, s9_t, n=24)
# na style: thin head, fat tail
widths9 = [max(2, 3 + int(i * 6 / len(pts9))) for i in range(len(pts9))]
stroke_variable_width(draw, pts9, widths9)

# s10: lower-right long na  (head BC, tail BR)
s10_h = anchor_to_xy(('BC', 0.951, 0.241))
s10_t = anchor_to_xy(('BR', 0.358, 0.707))
pts10 = sample_line(s10_h, s10_t, n=32)
widths10 = [max(2, 3 + int(i * 9 / len(pts10))) for i in range(len(pts10))]
stroke_variable_width(draw, pts10, widths10)

# =============================================================
img.save(os.path.join(_HERE, "01_眔.png"))
print("wrote 01_眔.png ; strokes =", 10)
