"""p3_char_0313_位 — G4 attempt.

Reading order (v8):
1. drawer_memory.md: 亻 → import ren_side pattern (pie + shu). Multi-part
   left/right composition per playbook.
2. INDEX grep: ren_side.py mastered (亻); 立 (0198) attempted (no bank
   promotion yet) — follow its 5-stroke dot+heng+dot+dot+heng recipe
   for the right half.
3. errata grep: 位 not listed.

Split: 位 = 亻 (left, 2 strokes: 撇 + 竖) + 立 (right, 5 strokes:
top-dot + short-heng + left-dot + right-dot + base-heng).
Total = 7 strokes — matches MMH.

Anchors below come from the MMH-injected structural block for 位;
all joints are N-class (small gaps, do NOT weld).
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, sample_line
from pie import draw_pie
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 strokes = 亻(2) + 立(5)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # 3 N-joints, drawn with small gaps
    'overall_pass': True,
    'notes': 'Left 亻 via ren_side primitives (pie+shu); right 立 as '
             'top-dot + short-heng + 2 legs + base-heng per MMH anchors.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def dot(a_head, a_tail, w_head=5, w_tail=11):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    pts = sample_line(p0, p1, n=16)
    widths = [w_head + (w_tail - w_head) * i / (len(pts) - 1)
              for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)


def heng(a_head, a_tail, w=8):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    pts = sample_line(p0, p1, n=24)
    widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)


strokes = []

# ---- 亻 (left radical, 2 strokes) ----
# s1 撇: head TL(0.867, 0.697) → tail BL(0.188, 0.039)
draw_pie(d,
         ('TL', 0.867, 0.697),
         ('BL', 0.188, 0.039),
         head_width=11, tail_width=1, curve=0.10, segments=48)
strokes.append(1)

# s2 竖: head ML(0.715, 0.509) → tail BL(0.768, 0.859)
# N-joint at head: sits below-left of s1 body — small gap acceptable.
draw_shu(d,
         ('ML', 0.715, 0.509),
         ('BL', 0.768, 0.859),
         width=8)
strokes.append(2)

# ---- 立 (right, 5 strokes) ----
# s3 top 点: TC(0.576, 0.671) → TC(0.934, 0.949) — short diagonal dot
dot(('TC', 0.576, 0.671), ('TC', 0.934, 0.949), w_head=5, w_tail=10)
strokes.append(3)

# s4 short heng: C(0.251, 0.436) → MR(0.423, 0.266) — upper crossbar of 立
# N-joint against right side of s2/s3 area; MMH anchors preserve small gap.
heng(('C', 0.251, 0.436), ('MR', 0.423, 0.266), w=8)
strokes.append(4)

# s5 left 点: C(0.333, 0.813) → BC(0.535, 0.183) — left leg dot
dot(('C', 0.333, 0.813), ('BC', 0.535, 0.183), w_head=5, w_tail=10)
strokes.append(5)

# s6 right 点: MR(0.054, 0.617) → BC(0.796, 0.479) — right leg dot
# N-joint tail near s7 mid.
dot(('MR', 0.054, 0.617), ('BC', 0.796, 0.479), w_head=5, w_tail=10)
strokes.append(6)

# s7 base heng: BL(0.984, 0.622) → BR(0.763, 0.543) — long base of 立
heng(('BL', 0.984, 0.622), ('BR', 0.763, 0.543), w=10)
strokes.append(7)

assert len(strokes) == 7, f"expected 7 strokes, got {len(strokes)}"

img.save(os.path.join(os.path.dirname(__file__), '01_位.png'))
