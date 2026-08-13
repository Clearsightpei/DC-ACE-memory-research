"""p3_char_0534_痃 — 疒 (strokes 1-5) + 玄 (strokes 6-10).

Bank lookup (v8 slim checklist):
  1. drawer_memory.md — canonical 疒 recipe from 疽 A / 疸 PASS:
     5-stroke top-left frame (dot + 亠 top + long 撇 + inner dot + inner 提).
     No `chronic/ne_sick.py` promoted yet — inline via MMH anchors.
     No bank primitive for 玄 — inline as 亠 (2 strokes) + 幺 (3 strokes).
  2. INDEX.md grep 痃/玄 — not present. bing.py is 冫 (not 疒).
     yao_small.py is 幺 but with different anchors; inline for consistency
     with MMH endpoints for THIS composition.
  3. errata.md grep 痃 — not present.

Composition: 疒 top-left frame occupies x∈[0.0,0.35], y∈[0.0,1.0];
  玄 bottom-right slot fills x∈[0.35,0.95], y∈[0.30,1.0].

Expected 10 strokes, all N-class joints (small gaps).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 frame from 疽/疸 pattern + 玄 inline (亠 + 幺). All 9 joints N-class, small gaps only.'
}

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


def _tapered(d, h, t, w_head, w_tail, ctrl_dx=0, ctrl_dy=0, n=30):
    mid = ((h[0] + t[0]) / 2 + ctrl_dx, (h[1] + t[1]) / 2 + ctrl_dy)
    pts = quad_bezier(h, mid, t, n=n)
    widths = [w_head + (w_tail - w_head) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============ 疒 FRAME (strokes 1-5) ============

    # s1 — top 点 (dot)
    h = anchor_to_xy(('TC', 0.459, 0.595))
    t = anchor_to_xy(('TC', 0.813, 0.817))
    _tapered(d, h, t, 3, 8, ctrl_dy=2, n=20)

    # s2 — top 横 (亠 top bar, slight rise to the right)
    h = anchor_to_xy(('C', 0.099, 0.075))
    t = anchor_to_xy(('TR', 0.341, 0.94))
    _tapered(d, h, t, 5, 5, ctrl_dy=-3, n=40)

    # s3 — long 撇 sweep down the left frame
    h = anchor_to_xy(('TL', 0.876, 0.996))
    t = anchor_to_xy(('BL', 0.413, 1.003))
    ctrl = (h[0] - 15, h[1] + (t[1] - h[1]) * 0.7)
    pts = quad_bezier(h, ctrl, t, n=60)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        widths.append(4 + 4 * (1 - abs(2 * u - 1)))  # bulge middle
    stroke_variable_width(d, pts, widths)

    # s4 — inner upper 点 (small dot inside frame)
    h = anchor_to_xy(('ML', 0.437, 0.339))
    t = anchor_to_xy(('ML', 0.688, 0.544))
    _tapered(d, h, t, 3, 7, ctrl_dx=-2, n=20)

    # s5 — inner lower 提 (rising ti, thick to thin)
    h = anchor_to_xy(('BL', 0.188, 0.206))
    t = anchor_to_xy(('ML', 0.814, 0.887))
    _tapered(d, h, t, 6, 2, ctrl_dy=3, n=30)

    # ============ 玄 INTERIOR (strokes 6-10) ============

    # s6 — top 点 of 亠 (small dot)
    h = anchor_to_xy(('C', 0.579, 0.228))
    t = anchor_to_xy(('C', 0.805, 0.406))
    _tapered(d, h, t, 3, 8, ctrl_dy=2, n=20)

    # s7 — 横 of 亠 (long horizontal, slight arc)
    h = anchor_to_xy(('C', 0.169, 0.649))
    t = anchor_to_xy(('MR', 0.429, 0.544))
    _tapered(d, h, t, 4, 5, ctrl_dy=-2, n=40)

    # s8 — upper 撇折 of 幺 (small top loop): head at top, bends leftward, tail right
    # MMH endpoints are just head/tail of the median — imply the loop via curve.
    h = anchor_to_xy(('C', 0.55, 0.729))
    t = anchor_to_xy(('BC', 0.772, 0.215))
    # Draw as two segments: down-left then right-down
    pivot = (h[0] - 12, (h[1] + t[1]) / 2 + 4)
    pts1 = quad_bezier(h, ((h[0] + pivot[0]) / 2, (h[1] + pivot[1]) / 2 + 2), pivot, n=15)
    pts2 = quad_bezier(pivot, ((pivot[0] + t[0]) / 2, (pivot[1] + t[1]) / 2 + 2), t, n=15)
    w1 = [5 - 2 * (i / len(pts1)) for i in range(len(pts1))]
    w2 = [3 + 3 * (i / len(pts2)) for i in range(len(pts2))]
    stroke_variable_width(d, pts1, w1)
    stroke_variable_width(d, pts2, w2)

    # s9 — lower 撇折 of 幺 (main loop): head upper-right, curves down-left then down-right
    h = anchor_to_xy(('MR', 0.007, 0.887))
    t = anchor_to_xy(('BR', 0.191, 0.684))
    pivot = (h[0] - 20, h[1] + 30)
    pts1 = quad_bezier(h, ((h[0] + pivot[0]) / 2, (h[1] + pivot[1]) / 2), pivot, n=18)
    pts2 = quad_bezier(pivot, ((pivot[0] + t[0]) / 2, (pivot[1] + t[1]) / 2 + 3), t, n=18)
    w1 = [6 - 2 * (i / len(pts1)) for i in range(len(pts1))]
    w2 = [3 + 3 * (i / len(pts2)) for i in range(len(pts2))]
    stroke_variable_width(d, pts1, w1)
    stroke_variable_width(d, pts2, w2)

    # s10 — final long 点 / na (bottom sweep of 幺 base)
    h = anchor_to_xy(('BR', 0.074, 0.376))
    t = anchor_to_xy(('BR', 0.405, 0.93))
    _tapered(d, h, t, 3, 9, ctrl_dx=3, ctrl_dy=3, n=30)

    out = os.path.join(HERE, '01_痃.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
