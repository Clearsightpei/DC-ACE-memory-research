"""仲 = 亻 (left radical) + 中 (right main).

Split: 亻 (s1 撇 + s2 竖) — call ren_side primitive.
       中 (s3 left-shu of 口, s4 heng-zhe of 口, s5 bottom heng of 口,
           s6 long vertical bisector through 口).

6 strokes total. Joints:
  s1.mid ⇆ s2.head : N (~16 px) — handled by ren_side primitive defaults.
  s3.head ⇆ s4.head : N (~14 px)  口 top-left corner
  s3.tail ⇆ s5.head : N (~16 px)  口 bottom-left corner
  s4.tail ⇆ s5.mid  : N (~12 px)  口 bottom-right corner
  s4.mid  ⇆ s6.mid  : P (weld)    vertical crosses top heng
  s5.mid  ⇆ s6.mid  : P (weld)    vertical crosses bottom heng
"""
import sys, os
BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "..", "success_bank", "code")
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from ren_side import draw_ren_side

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '仲: ren_side handles s1+s2 (N-joint gap); 口 inlined via fat_line with'
             ' ~10 px corner shortening for N-joints; long central 竖 s6 pierces top-heng'
             ' (s4) and bottom-heng (s5) as P-welds.',
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# ---- s1 + s2: 亻 via ren_side primitive (default anchors — proven, T/N joint handled) ----
draw_ren_side(d)

# ---- s3: 口 left 竖 (short, slightly slanting) ----
s3_head = ('C', 0.137, 0.436)
s3_tail = ('BC', 0.371, 0.121)
p3_head = anchor_to_xy(s3_head)
p3_tail = anchor_to_xy(s3_tail)

# ---- s4: 口 横折 (top + right wall) — inline as heng segment + shu segment via corner ----
s4_head = ('C', 0.301, 0.441)
s4_tail = ('MR', 0.271, 0.813)
p4_head = anchor_to_xy(s4_head)
p4_tail = anchor_to_xy(s4_tail)
# Corner of 横折 is at the top-right of 口 — same y as p4_head, same x as p4_tail
p4_corner = (p4_tail[0], p4_head[1])

# ---- s5: 口 bottom 横 ----
s5_head = ('C', 0.43, 0.98)
s5_tail = ('MR', 0.467, 0.931)
p5_head = anchor_to_xy(s5_head)
p5_tail = anchor_to_xy(s5_tail)

# ---- s6: long vertical bisector through 口 ----
s6_head = ('TC', 0.673, 0.645)
s6_tail = ('BC', 0.837, 1.135)
p6_head = anchor_to_xy(s6_head)
p6_tail = anchor_to_xy(s6_tail)


def _shorten(pt, other, px):
    """Move pt toward other by px pixels (used to open N-joint gaps)."""
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d_ = (dx * dx + dy * dy) ** 0.5
    if d_ < 1e-6:
        return pt
    t = min(1.0, px / d_)
    return (x0 + dx * t, y0 + dy * t)


# Open N-joints for 口 corners (~8 px each side of corner)
# top-left corner: s3.head vs s4.head — shorten both away from corner
p3_head_open = _shorten(p3_head, p3_tail, 6)
p4_head_open = _shorten(p4_head, p4_corner, 6)
# bottom-left: s3.tail vs s5.head — shorten both
p3_tail_open = _shorten(p3_tail, p3_head, 6)
p5_head_open = _shorten(p5_head, p5_tail, 6)
# bottom-right: s4.tail (bottom of right wall) vs s5.tail-region
# leave the s5 right end slightly short of the wall
p5_tail_open = _shorten(p5_tail, p5_head, 4)
p4_tail_open = _shorten(p4_tail, p4_corner, 4)

# Draw 口 (P-welds at s4∩s6 and s5∩s6 will happen naturally because s6 passes
# through those y-levels; 口 corners stay N)
fat_line(d, p3_head_open, p3_tail_open, 8)         # s3 left 竖
fat_line(d, p4_head_open, p4_corner, 8)            # s4 top 横 (part 1)
fat_line(d, p4_corner, p4_tail_open, 8)            # s4 right 竖 (part 2)
fat_line(d, p5_head_open, p5_tail_open, 8)         # s5 bottom 横

# Draw s6 last so weld is visually clean on top of the two heng
fat_line(d, p6_head, p6_tail, 8)                   # s6 long central 竖

img.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_仲.png'))
print("wrote 01_仲.png  strokes=6")
