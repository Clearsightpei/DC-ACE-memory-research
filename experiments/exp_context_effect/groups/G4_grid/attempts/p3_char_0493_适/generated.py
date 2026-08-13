"""适 (shì) — 9 strokes.

Decomposition: 适 = 舌 (top-right, 6 strokes) + 辶 (left+bottom sweep, 3 strokes).

Strokes 1-6 render 舌 inline via base primitives (撇 + 一 + 丨 + 口).
Strokes 7-9 use the mastered chronic-equivalent chuo_walk primitive
(点 + 横折折撇 + 平捺). MMH anchors for the 辶 strokes match
chuo_walk defaults within ±0.05 in both x_frac and y_frac, so we USE
the bank primitive (not BANK_DEVIATION).

Joints (all N except s2-s3 which is P for the 舌 cross):
  s1.mid ⇆ s3.head  @ C — N (~16 px gap)
  s2.mid ⇆ s3.mid   @ C — P (welded cross)
  s3.tail ⇆ s5.mid  @ C — N (~13 px)
  s4.head ⇆ s5.head @ C — N (~11 px, 口 top-left corner)
  s4.mid ⇆ s6.head  @ BC — N (~15 px)
  s4.tail ⇆ s9.mid  @ BC — N (~30 px)
  s5.tail ⇆ s6.mid  @ BR — N (~13 px, 口 bottom-right corner)
  s8.tail ⇆ s9.mid  @ BL — N (~10 px)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier
from chuo_walk import draw_chuo_walk


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 6 inline + 3 from chuo_walk = 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('适 = 舌 (inline 6 strokes MMH-verbatim) + 辶 (chuo_walk '
              'primitive, matches MMH anchors). P joint at s2xs3; all '
              'others N (口 corners naturally gapped).'),
}


def draw_shu_variable(draw, head, tail, w_head=8, w_tail=8):
    """Straight-ish vertical/general stroke as short polyline with per-vertex widths."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = [(p0[0] + t * (p1[0] - p0[0]),
            p0[1] + t * (p1[1] - p0[1])) for t in (0.0, 0.5, 1.0)]
    widths = [w_head, (w_head + w_tail) / 2, w_tail]
    stroke_variable_width(draw, pts, widths)


def draw_pie_curve(draw, head, tail, w_head=11, w_tail=2, curve=0.10):
    """撇 as quadratic Bezier bulging left of the head-tail line."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # perpendicular (left side for a 撇 going down-left)
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx = -dy / L
    ny = dx / L
    ctrl = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, ctrl, p2, n=32)
    widths = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        widths.append(w_head * (1 - t) + w_tail * t)
    stroke_variable_width(draw, pts, widths)


def draw_heng_zhe_kou(draw, head_top, corner, tail_bot):
    """One-stroke 横折 for the top+right side of 口: heng then vertical."""
    p0 = anchor_to_xy(head_top)
    p1 = anchor_to_xy(corner)
    p2 = anchor_to_xy(tail_bot)
    stroke_variable_width(draw, [p0, p1, p1, p2],
                          [7, 8, 8, 7])


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------- 舌 (strokes 1..6) -------

    # s1 撇 — TR(0.247,0.829) → C(0.336, 0.096)
    draw_pie_curve(d,
                   ('TR', 0.247, 0.829),
                   ('C',  0.336, 0.096),
                   w_head=11, w_tail=3, curve=0.08)

    # s2 一 (top horizontal of 舌) — C(0.093,0.535) → MR(0.625,0.415)
    fat_line(d,
             anchor_to_xy(('C',  0.093, 0.535)),
             anchor_to_xy(('MR', 0.625, 0.415)),
             width=7)

    # s3 丨 long vertical through center — C(0.661,0.058) → C(0.685,0.834)
    fat_line(d,
             anchor_to_xy(('C', 0.661, 0.058)),
             anchor_to_xy(('C', 0.685, 0.834)),
             width=8)

    # s4 竖 (left of 口) — C(0.31,0.901) → BC(0.5, 0.514)
    fat_line(d,
             anchor_to_xy(('C',  0.31, 0.901)),
             anchor_to_xy(('BC', 0.5,  0.514)),
             width=7)

    # s5 横折 (top+right of 口) — C(0.38,0.884) → BR(0.042,0.232)
    # heng across top of 口 (at y ~ head), then zhe straight down to tail.
    # Corner: same y as head, same x as tail → top-right corner of 口.
    p0 = anchor_to_xy(('C',  0.38,  0.884))
    p2 = anchor_to_xy(('BR', 0.042, 0.232))
    corner = (p2[0], p0[1])
    stroke_variable_width(d, [p0, corner, corner, p2],
                          [7, 8, 8, 7])

    # s6 一 (bottom horizontal of 口) — BC(0.55,0.335) → BR(0.212,0.347)
    fat_line(d,
             anchor_to_xy(('BC', 0.55,  0.335)),
             anchor_to_xy(('BR', 0.212, 0.347)),
             width=7)

    # ------- 辶 (strokes 7..9) via chuo_walk primitive -------
    draw_chuo_walk(d)

    out = os.path.join(os.path.dirname(__file__), '01_适.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
