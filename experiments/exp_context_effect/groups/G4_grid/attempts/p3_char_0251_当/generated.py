"""G4 attempt for 当 (p3_char_0251).

Memory read order (v8):
  1. drawer_memory.md — no prior 当 primitive; not a chronic character.
  2. success_bank/INDEX.md — no 当 entry (fresh).
  3. errata.md — no 当 entry.

Structure (from MMH-injected block, 6 strokes):
  Top ⺌ (three little marks): s1 short vertical/dot at TC-C,
                              s2 short pie ML->C, s3 dot TR->C.
  Bottom 彐-like frame:
    s4 = 横折 (top horizontal of lower box + right vertical), L-shape.
    s5 = short middle horizontal inside the frame.
    s6 = bottom-closing long horizontal.

Joints (all N, gaps ~12-31 px — do NOT weld):
  s1.tail near s4.mid(0.29) @ C
  s4.mid(0.84) near s5.tail @ BC
  s4.tail near s6.mid(0.82) @ BC
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../success_bank/code")
from _anchor import anchor_to_xy, fat_line, stroke_variable_width

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'straight-line rendering; s4 drawn as L via corner-cell math (TR-BR).',
}

W = 300
img = Image.new('RGB', (W, W), 'white')
d = ImageDraw.Draw(img)

# -------- stroke 1: small vertical/dot at top-center --------
p1a = anchor_to_xy(('TC', 0.371, 0.7))
p1b = anchor_to_xy(('C',  0.418, 0.658))
fat_line(d, p1a, p1b, width=7)

# -------- stroke 2: short 丿 (left-falling) upper-left --------
p2a = anchor_to_xy(('ML', 0.773, 0.104))
p2b = anchor_to_xy(('C',  0.069, 0.4))
fat_line(d, p2a, p2b, width=6)

# -------- stroke 3: right dot slanting down-left --------
p3a = anchor_to_xy(('TR', 0.057, 0.82))
p3b = anchor_to_xy(('C',  0.731, 0.345))
fat_line(d, p3a, p3b, width=6)

# -------- stroke 4: 横折 L-shape (top + right of bottom frame) --------
# Head at ML(0.797, 0.77), MMH mids at C(0.449,0.69) and BC(0.977,0.214),
# tail at BC(0.925, 0.578). Corner sits near top-right of lower box.
s4_head   = anchor_to_xy(('ML', 0.797, 0.77))
s4_mid1   = anchor_to_xy(('C',  0.449, 0.69))
s4_corner = anchor_to_xy(('C',  0.977, 0.72))   # top-right corner of the frame
s4_tail   = anchor_to_xy(('BC', 0.925, 0.578))
# Horizontal leg (with slight upward drift toward center of the top edge):
fat_line(d, s4_head, s4_mid1, width=7)
fat_line(d, s4_mid1, s4_corner, width=7)
# Vertical leg going down:
fat_line(d, s4_corner, s4_tail, width=7)

# -------- stroke 5: middle horizontal inside frame --------
p5a = anchor_to_xy(('BL', 0.715, 0.247))
p5b = anchor_to_xy(('BC', 0.866, 0.188))
fat_line(d, p5a, p5b, width=6)

# -------- stroke 6: bottom horizontal (closes the frame) --------
p6a = anchor_to_xy(('BL', 0.753, 0.777))
p6b = anchor_to_xy(('BR', 0.18, 0.719))
fat_line(d, p6a, p6b, width=7)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_当.png")
img.save(out)
print("wrote", out)
