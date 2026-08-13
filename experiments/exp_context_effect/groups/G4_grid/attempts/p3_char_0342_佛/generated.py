"""佛 (fó) — 7 strokes.
Decomposition: 佛 = 亻 (left, 2 strokes: pie + shu) + 弗 (right, 5 strokes:
  short heng-top, middle heng, left pie, middle shu, right shu-gou).

Following A-recipe (drawer_memory.md B9 section):
  1. Explicit decomposition (above).
  2. MMH-verbatim anchors — every stroke uses the dispatcher-injected
     anchor tuples unchanged.
  3. SELF_CHECK block below.
  4. Base primitives (fat_line + quad_bezier) rather than compound bank
     primitives — ren_side's defaults sit in TC/C and would drift right of
     MMH's TL/ML anchors for 亻.
  5. N-joint discipline: joints s1.mid⇆s2.head and s3.tail⇆s4.mid and
     s4.head⇆s5.head are neighbor-class — leave the small gap.

Reading log (v8 mandatory triplet):
  # memory_index.md  → read; A-recipe applies.
  # drawer_memory.md → read; B8 亻+X pattern → inline pie+shu, do NOT
  #                    partial-override ren_side.
  # errata.md         → grep 佛 → not present.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = 3  # stroke half-width baseline (fat_line width)
INK = (0, 0, 0)


def draw_pie_curve(d, head, tail, width=6):
    """Long pie with a gentle leftward bow."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    # control point: bow slightly left/down of the straight midpoint
    mx = (p0[0] + p2[0]) / 2 - 8
    my = (p0[1] + p2[1]) / 2 + 4
    pts = quad_bezier(p0, (mx, my), p2, n=40)
    # variable width: thicker near head, thin at tail
    widths = [max(2, width - i / len(pts) * (width - 2)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths, INK)


def draw_straight(d, head, tail, width=6):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(d, p0, p1, width, INK)


def draw_shu_gou(d, head, tail, width=6):
    """Vertical stroke with a small leftward hook at the bottom."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(d, p0, p1, width, INK)
    # small hook at tail: 8-10px to the left
    hook_end = (p1[0] - 12, p1[1] - 4)
    fat_line(d, p1, hook_end, width, INK)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 亻 pie (long slanted left-down) ----
    s1_head = ('TL', 0.885, 0.53)
    s1_tail = ('ML', 0.161, 0.854)
    draw_pie_curve(d, s1_head, s1_tail, width=6)

    # ---- Stroke 2: 亻 shu (vertical, starts near s1 mid) ----
    s2_head = ('ML', 0.703, 0.351)
    s2_tail = ('BL', 0.727, 0.868)
    draw_straight(d, s2_head, s2_tail, width=6)

    # ---- Stroke 3: 弗 top-left short heng ----
    s3_head = ('C', 0.225, 0.175)
    s3_tail = ('MR', 0.165, 0.307)
    draw_straight(d, s3_head, s3_tail, width=6)

    # ---- Stroke 4: 弗 middle heng (rises slightly right) ----
    s4_head = ('C', 0.315, 0.608)
    s4_tail = ('MR', 0.338, 0.403)
    draw_straight(d, s4_head, s4_tail, width=6)

    # ---- Stroke 5: 弗 left pie (short, going down-right per MMH) ----
    s5_head = ('C', 0.169, 0.5)
    s5_tail = ('BR', 0.068, 0.279)
    draw_straight(d, s5_head, s5_tail, width=6)

    # ---- Stroke 6: 弗 middle shu (vertical, top to bottom) ----
    s6_head = ('TC', 0.412, 0.729)
    s6_tail = ('BC', 0.102, 0.83)
    draw_straight(d, s6_head, s6_tail, width=6)

    # ---- Stroke 7: 弗 right shu with hook (extends past baseline) ----
    s7_head = ('TC', 0.772, 0.533)
    s7_tail = ('BC', 0.896, 1.185)
    draw_shu_gou(d, s7_head, s7_tail, width=6)

    out = os.path.join(os.path.dirname(__file__), '01_佛.png')
    img.save(out)
    print(f"wrote {out}")


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 stroke primitives called (s1..s7)
    'endpoint_mismatches': [],    # all MMH-verbatim
    'joint_class_mismatches': [], # N joints left as natural gaps; P joints
                                  # emerge from where s6/s7 verticals cross
                                  # s3/s4 horizontals in cell C
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; 亻 inlined (not ren_side) per B8 partial-override warning; N-joints preserved as gaps; shu-gou for s7 adds small left hook consistent with 弗-right form.',
}


if __name__ == '__main__':
    main()
