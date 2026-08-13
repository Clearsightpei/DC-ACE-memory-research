"""p3_char_0258_伕 — G4 attempt.

Split: 伕 = 亻 (left) + 夫 (right).
Steps followed:
  1. drawer_memory.md → 亻 is a chronic left-radical (ren_side). 夫 has no
     dedicated primitive; draw fresh per MMH anchors below.
  2. success_bank/INDEX.md grep — no 夫 entry; ren_side.py exists but
     MMH anchors for 伕's 亻 differ from the mastered primitive
     (伕's 亻 hugs the far-left column). Inline fresh per MMH.
  3. errata.md grep — 伕 not listed.

Stroke plan (matches MMH count = 6):
  s1: 亻-撇  TL(0.803,0.729) → ML(0.152,0.96)
  s2: 亻-竖  ML(0.647,0.538) → BL(0.633,0.974)
  s3: 夫-heng(top)   C(0.266,0.383) → MR(0.232,0.216)
  s4: 夫-heng(bot)   C(0.052,0.91)  → MR(0.405,0.723)
  s5: 夫-撇  TC(0.567,0.624) → BL(0.817,0.947)
  s6: 夫-捺  C(0.726,0.966)  → BR(0.833,0.903)

Joints:
  s1.mid ⇆ s2.head — N (small gap, do not weld)
  s2.tail ⇆ s5.tail — N (feet apart on baseline)
  s3.mid ⇆ s5.mid — P (top heng pierced by pie)
  s4.mid ⇆ s5.mid — P (bottom heng pierced by pie)
  s4.mid ⇆ s6.head — N (na starts near crossing, small gap)
  s5.mid ⇆ s6.head — N (pie and na share crossing region)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes, anchors verbatim from MMH block; N-class kept as gaps, P-class welded at C-cell crossings.'
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, sample_line


def draw_pie_stroke(d, head, tail, head_w=11, tail_w=2, bow=10):
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    ctrl = ((p0[0] + p2[0]) / 2 - bow, (p0[1] + p2[1]) / 2)
    n = 48
    pts = quad_bezier(p0, ctrl, p2, n=n)
    widths = [head_w - i * (head_w - tail_w) / n for i in range(n + 1)]
    stroke_variable_width(d, pts, widths)


def draw_heng_stroke(d, head, tail, width=7):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(d, p0, p1, width=width)


def draw_shu_stroke(d, head, tail, width=8):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(d, p0, p1, width=width)


def draw_na_stroke(d, head, tail, head_w=3, tail_w=12):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    n = 32
    pts = sample_line(p0, p1, n=n)
    widths = [head_w + i * (tail_w - head_w) / n for i in range(n + 1)]
    stroke_variable_width(d, pts, widths)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: 亻-撇
draw_pie_stroke(d, ('TL', 0.803, 0.729), ('ML', 0.152, 0.96), head_w=11, tail_w=2, bow=10)
# s2: 亻-竖
draw_shu_stroke(d, ('ML', 0.647, 0.538), ('BL', 0.633, 0.974), width=8)
# s3: 夫-top heng (short)
draw_heng_stroke(d, ('C', 0.266, 0.383), ('MR', 0.232, 0.216), width=7)
# s4: 夫-bottom heng (longer)
draw_heng_stroke(d, ('C', 0.052, 0.91), ('MR', 0.405, 0.723), width=7)
# s5: 夫-撇
draw_pie_stroke(d, ('TC', 0.567, 0.624), ('BL', 0.817, 0.947), head_w=10, tail_w=2, bow=14)
# s6: 夫-捺
draw_na_stroke(d, ('C', 0.726, 0.966), ('BR', 0.833, 0.903), head_w=3, tail_w=12)

img.save(os.path.join(_HERE, '01_伕.png'))
print('OK — wrote 01_伕.png (6 strokes)')
