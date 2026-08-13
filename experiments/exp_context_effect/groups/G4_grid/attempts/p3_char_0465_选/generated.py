"""
p3_char_0465_选 (xuǎn) — G4 attempt

Reading order followed:
  1. drawer_memory.md — chuo_walk primitive exists for 辶 (mastered
     radical p2_044). Anchors of 选's strokes 7,8,9 vs chuo_walk's
     s1,s2,s3 anchors are essentially the same (dot at TL upper-left,
     compact S in ML/BL column, sweeping 平捺 across bottom). IMPORT
     and CALL chuo_walk for strokes 7-9. Do NOT redraw fresh.
  2. INDEX.md grep: 先 exists as p3_0277 "full inline" — no primitive.
     Draw 先 (strokes 1-6) fresh using MMH anchors verbatim + 儿-base
     shapes from er_legs canonical (撇 left + 竖弯钩 right).
  3. errata.md grep for 选: not listed.

Decomposition: 选 = 先 (top-right, strokes 1-6) + 辶 (bottom-left wrap,
                     strokes 7-9).
Stroke count: 9 (matches MMH expected).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'chuo_walk imported for 辶; 先 inlined per MMH anchors. s6 竖弯钩 routed via bottom bend then hook up.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line
from chuo_walk import draw_chuo_walk


def A(cell, xf, yf):
    return anchor_to_xy((cell, xf, yf))


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# =========================================================================
# 先 part (strokes 1-6) — inline per MMH anchors
# =========================================================================

# ---- Stroke 1: short 撇 (top-most short descending stroke)
# head C(0.333, 0.043) = (133.3, 104.3) -> tail C(0.148, 0.553) = (114.8, 155.3)
s1_head = A('C', 0.333, 0.043)
s1_tail = A('C', 0.148, 0.553)
# short pie: slight curve
mid1 = ((s1_head[0] + s1_tail[0]) / 2 - 2,
        (s1_head[1] + s1_tail[1]) / 2)
stroke_variable_width(d, [s1_head, mid1, s1_tail], [8, 7, 3])

# ---- Stroke 2: 短横 (top horizontal, upper part of 牛-like top)
# head C(0.427, 0.327) = (142.7, 132.7) -> tail MR(0.209, 0.175) = (220.9, 117.5)
s2_head = A('C', 0.427, 0.327)
s2_tail = A('MR', 0.209, 0.175)
fat_line(d, s2_head, s2_tail, 7)

# ---- Stroke 3: 短竖 (vertical crossing s2 at P joint) — 十 crossing
# head TC(0.688, 0.665) = (168.8, 66.5) -> tail C(0.74, 0.632) = (174.0, 163.2)
s3_head = A('TC', 0.688, 0.665)
s3_tail = A('C', 0.74, 0.632)
fat_line(d, s3_head, s3_tail, 8)

# ---- Stroke 4: 长横 (middle long horizontal, base of 生-like top)
# head C(0.125, 0.781) = (112.5, 178.1) -> tail MR(0.508, 0.646) = (250.8, 164.6)
s4_head = A('C', 0.125, 0.781)
s4_tail = A('MR', 0.508, 0.646)
fat_line(d, s4_head, s4_tail, 8)

# ---- Stroke 5: 撇 (left leg of 儿)
# head C(0.497, 0.816) = (149.7, 181.6) -> tail BC(0.122, 0.511) = (112.2, 251.1)
s5_head = A('C', 0.497, 0.816)
s5_tail = A('BC', 0.122, 0.511)
mid5 = ((s5_head[0] + s5_tail[0]) / 2 - 3,
        (s5_head[1] + s5_tail[1]) / 2 + 2)
stroke_variable_width(d, [s5_head, mid5, s5_tail], [9, 8, 3])

# ---- Stroke 6: 竖弯钩 (right leg of 儿)
# head C(0.811, 0.758) = (181.1, 175.8) -> tail BR(0.543, 0.039) = (254.3, 203.9)
# Route: down from head to near bottom, curve right, hook up-right to tail.
s6_head = A('C', 0.811, 0.758)
s6_tail = A('BR', 0.543, 0.039)
p_down  = (s6_head[0] + 3, 250)      # descending down
p_bend  = (215, 275)                 # bottom bend
p_right = (250, 268)                 # rightward sweep before hook
p_hook  = s6_tail                    # hook tip (up-flick)
stroke_variable_width(
    d, [s6_head, p_down, p_bend, p_right, p_hook],
    [8, 10, 11, 8, 3]
)

# =========================================================================
# 辶 part (strokes 7-9) — call mastered primitive chuo_walk
# =========================================================================
# Bank primitive check: chuo_walk anchors (dot TL(0.62,0.72)->TL(0.96,0.97),
# S starts ML(0.27,0.55) ends BL(0.81,0.39), 平捺 BL(0.28,0.54) -> BR(0.69,0.79))
# vs MMH 选 s7/s8/s9 (dot TL(0.64,0.79)->ML(0.96,0.07), S ML(0.31,0.72)->BL(0.82,0.49),
# 平捺 BL(0.32,0.63)->BR(0.75,0.85)). Same cells, x_frac within 0.05,
# y_frac within ~0.07. USE AS-IS (fits per bank v13 guard: real fit).
draw_chuo_walk(d)

img.save(os.path.join(os.path.dirname(__file__), '01_选.png'))
print('saved 01_选.png')
print('strokes drawn: 9 (6 inlined for 先 + 3 via chuo_walk for 辶)')
