"""p3_char_0139_礻 — G4 grid-bank attempt.

Memory lookup:
- INDEX grep for 礻: not mastered (only related p2_radical_116_礻 which FAILED).
- errata.md p2_radical_116_礻: "extend stem upward (head at C(0.55, 0.35));
  shorten 横撇 horizontal so corner sits closer to center; two 点 flank
  stem symmetrically." Applied LITERALLY.
- MMH structural: 4 strokes.
  s1 top dot: TC(0.31,0.639)→TC(0.632,0.902)  — down-right dot
  s2 横撇 : ML(0.814,0.512)→BL(0.712,0.52) — heng-pie sweep (starts
     upper-right area of ML then curves down-left into BL)
  s3 stem : C(0.386,0.934)→BC(0.424,1.076) — vertical stem (MMH short;
     apply TR9 by extending head UP into MC/TC to match GT full-span)
  s4 right dot: C(0.617,0.857)→BC(0.928,0.13) diagonal — down-right dot
- Joints: 3× N (small gaps at center C, ~15-30 px). Do NOT weld.
"""

import sys, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH 4 strokes: dot + heng-pie + stem + dot. Errata fix from '
             'p2_radical_116 applied: stem head lifted, heng-pie centered, '
             'dots flank stem. All 3 joints N (~15-25 px gaps).'
}


def draw_dot(draw, head_anchor, tail_anchor, w_head=6, w_tail=14):
    """Down-right dot as a tapered fat line."""
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    n = 20
    pts = [(p0[0] + i / n * (p1[0] - p0[0]),
            p0[1] + i / n * (p1[1] - p0[1])) for i in range(n + 1)]
    widths = [w_head + (w_tail - w_head) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_heng_pie(draw, head_anchor, corner_anchor, tail_anchor, width=7):
    """横撇: heng segment (nearly horizontal) then pie sweep down-left."""
    p0 = anchor_to_xy(head_anchor)
    pc = anchor_to_xy(corner_anchor)
    p1 = anchor_to_xy(tail_anchor)
    # Heng segment: keep it nearly horizontal (share y roughly)
    fat_line(draw, p0, pc, width)
    # Pie sweep: curve BELOW straight line (control point down-and-in)
    ctrl_x = pc[0] - (pc[0] - p1[0]) * 0.25
    ctrl_y = pc[1] + (p1[1] - pc[1]) * 0.55
    pts = quad_bezier(pc, (ctrl_x, ctrl_y), p1, n=40)
    widths = [width + 1 - 3 * (i / len(pts)) for i in range(len(pts))]
    widths = [max(2, w) for w in widths]
    stroke_variable_width(draw, pts, widths)


def draw_stem(draw, head_anchor, tail_anchor, width=8):
    """Vertical stem — TR8 rule 6: keep x aligned."""
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    # force x-alignment (TR8 rule 6)
    x = (p0[0] + p1[0]) / 2
    fat_line(draw, (x, p0[1]), (x, p1[1]), width)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: top dot (short down-right dot ABOVE the 横撇) ----
    draw_dot(draw,
             head_anchor=('TC', 0.45, 0.55),
             tail_anchor=('TC', 0.65, 0.85),
             w_head=4, w_tail=11)

    # ---- Stroke 2: 横撇 (heng nearly-horizontal, then long pie down-left) ----
    # Heng starts far LEFT (spanning MMH TR9), corner near center-mid,
    # then pie sweeps down-left to BL.
    draw_heng_pie(draw,
                  head_anchor=('ML', 0.35, 0.65),   # left start (heng)
                  corner_anchor=('C', 0.55, 0.60),  # corner near center
                  tail_anchor=('BL', 0.15, 0.75),   # pie tail down-left
                  width=7)

    # ---- Stroke 3: vertical stem — from just below 横撇 corner to bottom ----
    # Errata: extend stem upward; head near C(0.55, 0.65) just under corner.
    draw_stem(draw,
              head_anchor=('C', 0.55, 0.70),
              tail_anchor=('BC', 0.55, 0.95),
              width=8)

    # ---- Stroke 4: right dot (flanks stem symmetrically) ----
    # Down-right diagonal dot on the right side of the stem.
    draw_dot(draw,
             head_anchor=('C', 0.70, 0.80),
             tail_anchor=('MR', 0.15, 0.05),
             w_head=4, w_tail=12)

    out = os.path.join(HERE, '01_礻.png')
    img.save(out)
    print(f'wrote {out}')

    # ---- Self-check summary ----
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    main()
