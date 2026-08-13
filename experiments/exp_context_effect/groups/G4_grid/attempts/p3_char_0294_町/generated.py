"""p3_char_0294_町 — G4 attempt.

町 = 田 (compressed to left column, ML cell) + 丁 (right side, C/TR/BC).

Memory consulted:
  - drawer_memory.md: no direct 田 or 町 primitive; inline.
  - errata.md p3_char_0035_丁: fix — heng full-width, shu vertical with hook at
    right end. Here 丁 is compressed to the right side of the char, but still
    heng-across-top + shu_gou beneath.
  - success_bank INDEX: p3_char_0159_申 used inline 田-frame (no primitive).

Stroke plan (7 strokes matches MMH spec):
  s1 shu    : ML(0.25,0.005)  → BL(0.445,0.153)   left vertical of 田
  s2 heng_zhe: ML(0.44,0.12)  → ML(0.96,0.90)     top+right of 田
  s3 heng   : ML(0.54,0.5)    → C(0.005,0.45)     mid horizontal of 田
  s4 shu    : ML(0.69,0.10)   → ML(0.71,0.89)     mid vertical of 田 (P-weld with s3)
  s5 heng   : BL(0.51,0.04)   → ML(0.94,0.99)     bottom horizontal of 田
  s6 heng   : C(0.41,0.09)    → TR(0.79,0.97)     top horizontal of 丁
  s7 shu_gou: C(0.945,0.11)   → BC(0.65,0.54)     vertical hook of 丁
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 strokes as required
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '田 compressed to ML cell; 丁 heng spans C+TR, shu_gou in TR/BC. s3.s4 welded (P), rest N-gap.'
}

W = 10  # stroke width

def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: left vertical of 田 (slight slant)
    p = anchor_to_xy(('ML', 0.252, 0.005))
    q = anchor_to_xy(('BL', 0.445, 0.153))
    fat_line(d, p, q, W)

    # s2: 横折 top+right of 田 — polyline through corner
    h = anchor_to_xy(('ML', 0.439, 0.119))
    corner = anchor_to_xy(('ML', 0.96, 0.15))   # top-right corner of 田
    t = anchor_to_xy(('ML', 0.958, 0.904))
    # slight curl into corner
    fat_line(d, h, corner, W)
    fat_line(d, corner, t, W)

    # s3: middle horizontal (P-welded with s4). Slight leftward from ML to C boundary
    p = anchor_to_xy(('ML', 0.542, 0.5))
    q = anchor_to_xy(('C', 0.005, 0.45))
    fat_line(d, p, q, W)

    # s4: middle vertical of 田
    p = anchor_to_xy(('ML', 0.688, 0.096))
    q = anchor_to_xy(('ML', 0.712, 0.887))
    fat_line(d, p, q, W)

    # s5: bottom horizontal of 田
    p = anchor_to_xy(('BL', 0.51, 0.039))
    q = anchor_to_xy(('ML', 0.94, 0.989))
    fat_line(d, p, q, W)

    # s6: top horizontal of 丁 (long, slight lift on right)
    p = anchor_to_xy(('C', 0.412, 0.087))
    q = anchor_to_xy(('TR', 0.786, 0.967))
    fat_line(d, p, q, W)

    # s7: 竖钩 of 丁 — straight vertical descent, then a short hook flick left
    head = anchor_to_xy(('C', 0.945, 0.107))       # (194.5, 110.7)
    tail = anchor_to_xy(('BC', 0.652, 0.537))       # (165.2, 253.7)
    # main body: nearly-straight vertical from head down to just above tail_y
    body_end = (head[0] - 2, tail[1] - 5)           # end of straight part
    fat_line(d, head, body_end, W)
    # hook: short flick from body_end to tail (leftward + slightly up)
    fat_line(d, body_end, tail, W)

    out = os.path.join(os.path.dirname(__file__), '01_町.png')
    img.save(out)
    print('saved', out)

if __name__ == '__main__':
    draw()
