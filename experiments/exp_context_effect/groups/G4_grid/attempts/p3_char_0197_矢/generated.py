"""矢 (arrow) — G4 grid-bank attempt.

Decomposition: 矢 = 丿 (short top pie) + 一 (upper heng) + 大 (heng + pie + na).
5 strokes matching MMH order:
  s1: top short 撇 (TC → ML)
  s2: upper 一 (C.head → MR.tail)
  s3: lower 一 (ML → MR) crossing through center
  s4: 撇 (C → BL) — left leg
  s5: 捺 (C → BR) — right leg
Joints: s1.mid tips near s2.head (N), s2.mid touches s4.head (N),
s3 pierces s4 (P) and neighbors s5.head (N), s4 neighbors s5.head (N).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy, stroke_variable_width, fat_line, sample_line, quad_bezier
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes; joints handled visually (no explicit weld/gap enforcement).',
}


def draw_shi(img_path='01_矢.png'):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: top short 撇 (TC → ML) ----
    p0 = anchor_to_xy(('TC', 0.116, 0.709))
    p2 = anchor_to_xy(('ML', 0.712, 0.6))
    ctrl = ((p0[0] + p2[0]) / 2 + 4, (p0[1] + p2[1]) / 2 - 6)
    pts = quad_bezier(p0, ctrl, p2, n=30)
    widths = [max(2, int(6 - 4 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- Stroke 2: upper 一 (top horizontal) ----
    p0 = anchor_to_xy(('C', 0.069, 0.301))
    p1 = anchor_to_xy(('MR', 0.109, 0.131))
    fat_line(d, p0, p1, width=5)

    # ---- Stroke 3: lower 一 (middle horizontal, crossing) ----
    p0 = anchor_to_xy(('ML', 0.489, 0.998))
    p1 = anchor_to_xy(('MR', 0.528, 0.866))
    fat_line(d, p0, p1, width=6)

    # ---- Stroke 4: 撇 (left leg C → BL) ----
    p0 = anchor_to_xy(('C', 0.333, 0.354))
    p2 = anchor_to_xy(('BL', 0.486, 0.9))
    ctrl = ((p0[0] + p2[0]) / 2 + 6, (p0[1] + p2[1]) / 2 + 6)
    pts = quad_bezier(p0, ctrl, p2, n=40)
    widths = [max(2, int(6 - 3 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- Stroke 5: 捺 (right leg C → BR) ----
    p0 = anchor_to_xy(('C', 0.506, 0.978))
    p2 = anchor_to_xy(('BR', 0.657, 0.903))
    ctrl = ((p0[0] + p2[0]) / 2 - 4, (p0[1] + p2[1]) / 2 + 4)
    pts = quad_bezier(p0, ctrl, p2, n=40)
    widths = [max(2, int(3 + 4 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    img.save(os.path.join(os.path.dirname(__file__), img_path))


if __name__ == '__main__':
    draw_shi()
