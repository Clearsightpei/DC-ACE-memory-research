"""p3_char_0166_去 (qù, "go/leave", 5 strokes)

Composition:
  Top:    土 (3 strokes) = short 横 + 竖 + long 横 — reuse tu.py idea.
  Bottom: 厶 (2 strokes) = 撇折 (compound as line) + 点 (as line/pie).

MMH-derived stroke anchors (from injected brief):
  s1 heng     ML(0.923,0.356)  →  MR(0.062,0.23)     (short top heng)
  s2 shu      TC(0.356,0.612)  →  C(0.421,0.86)      (spine)
  s3 heng     BL(0.243,0.036)  →  MR(0.748,0.89)     (long bottom heng)
  s4 pie-arc  C(0.33,0.998)    →  BC(0.937,0.643)    (厶 first arm)
  s5 na-arc   BC(0.793,0.329)  →  BR(0.191,0.974)    (厶 second arm/点)

Joints (all in C or BC region, mostly N):
  s1 × s2 @ C : P (welded cross, 十 crossing)
  s2.tail ⇆ s3.mid : N (small gap)
  s2.tail ⇆ s4.head : N
  s3.mid ⇆ s4.head : N
  s4.tail ⇆ s5.mid : N
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '土 top uses heng+shu+heng (P at C). 厶 bottom uses two tapered segments with N-gap between them and small N gaps to bottom heng.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng import draw_heng
from shu import draw_shu


def _tapered_curve(draw, p0, p2, w0, w1, curve=0.06, segments=32,
                   color=(0, 0, 0)):
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [w0 + (w1 - w0) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_qu(draw):
    # ---- Top: 土 ----
    # s1: short 横 top of 土 (near mid-band, upper)
    s1_head = ('ML', 0.923, 0.356)
    s1_tail = ('MR', 0.062, 0.23)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # s2: 竖 spine — crosses s1 at C (P joint)
    s2_head = ('TC', 0.356, 0.612)
    s2_tail = ('C', 0.421, 0.86)
    draw_shu(draw, s2_head, s2_tail, width=10)

    # s3: long 横 bottom of 土 / top of 厶 — spans BL to MR
    s3_head = ('BL', 0.243, 0.036)
    s3_tail = ('MR', 0.748, 0.89)
    draw_heng(draw, s3_head, s3_tail, width=10)

    # ---- Bottom: 厶 ----
    # In GT, 厶 opens like a wide ㄥ under the long heng. MMH endpoints
    # are compressed; render classic 厶 anchored near those points but
    # spanning a visible triangle shape.
    #
    # s4: 撇 that starts near the middle of the long heng (below it)
    #     and curves DOWN-LEFT to the lower-left corner of BC.
    #     Then the tail heads back RIGHT (folded into one long piece).
    # Using MMH-provided anchors literally + a mild leftward bow so
    # the segment reads as a curved 撇折 arm.
    s4_head = ('C', 0.33, 0.998)
    s4_tail = ('BC', 0.937, 0.643)
    p4a = anchor_to_xy(s4_head)
    p4b = anchor_to_xy(s4_tail)
    # Custom bow: pull DOWN so the arm dips into a shallow bowl.
    dx, dy = p4b[0]-p4a[0], p4b[1]-p4a[1]
    length = max(1.0, (dx*dx+dy*dy)**0.5)
    ctrl = ((p4a[0]+p4b[0])*0.5 + 0, (p4a[1]+p4b[1])*0.5 + 18)
    pts4 = quad_bezier(p4a, ctrl, p4b, n=32)
    widths4 = [9 - (9-6)*(i/32) for i in range(33)]
    stroke_variable_width(draw, pts4, widths4)

    # s5: right arm of 厶 sweeping from upper-BC down-right to lower-BR.
    # This is the na-like tail.  Give it a curve that bows down.
    s5_head = ('BC', 0.793, 0.329)
    s5_tail = ('BR', 0.191, 0.974)
    p5a = anchor_to_xy(s5_head)
    p5b = anchor_to_xy(s5_tail)
    ctrl5 = ((p5a[0]+p5b[0])*0.5 - 4, (p5a[1]+p5b[1])*0.5 + 10)
    pts5 = quad_bezier(p5a, ctrl5, p5b, n=32)
    widths5 = [5 + (11-5)*(i/32) for i in range(33)]
    stroke_variable_width(draw, pts5, widths5)
    cap = 11 / 2.0
    draw.ellipse([p5b[0]-cap, p5b[1]-cap, p5b[0]+cap, p5b[1]+cap], fill=(0,0,0))


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_qu(draw)
    out = os.path.join(os.path.dirname(__file__), '01_去.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
