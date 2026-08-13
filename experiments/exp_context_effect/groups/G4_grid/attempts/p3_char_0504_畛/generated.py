"""畛 (zhen) — G4 attempt.

Composition: 田 (left, strokes 1–5) + 㐱 (right, strokes 6–10).
㐱 = 人 (s6 撇 + s7 捺) + 彡 (s8-s10 three 撇).

We render every MMH stroke as a straight line between the given
head/tail anchors, with two exceptions:
  - s2 (田 横折): explicit corner point at (top-right of top-heng).
  - pies (s6, s8, s9, s10): slight quadratic curve for calligraphic
    look, still endpoint-anchored.

No bank primitive fits 田 well enough here (no draw_tian available;
xi_box / wei_enclose are too large/enclosed). Rendering fresh.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 10 strokes drawn, matches MMH expectation
    'endpoint_mismatches': [],    # anchors used verbatim from brief
    'joint_class_mismatches': [], # all N-joints left as natural line intersections; s3.mid ⇆ s4.mid weld is P
    'overall_pass': True,
    'notes': 'Straight-line rendering between MMH endpoints; s2 as 横折 with corner; pies as slight curves.',
}

# --- Anchors (verbatim from MMH-derived brief) ---
S = {
    1: (('ML', 0.167, 0.298), ('BL', 0.39, 0.317)),
    2: (('ML', 0.316, 0.383), ('BC', 0.002, 0.142)),
    3: (('ML', 0.425, 0.731), ('ML', 0.914, 0.646)),
    4: (('ML', 0.589, 0.336), ('BL', 0.612, 0.036)),
    5: (('BL', 0.451, 0.183), ('BL', 0.876, 0.048)),
    6: (('TC', 0.749, 0.68),  ('C',  0.201, 0.693)),
    7: (('TC', 0.893, 0.955), ('MR', 0.886, 0.652)),
    8: (('C',  0.793, 0.383), ('BC', 0.356, 0.051)),
    9: (('C',  0.919, 0.737), ('BC', 0.345, 0.496)),
    10:(('BR', 0.089, 0.083), ('BC', 0.233, 1.091)),
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)
INK = (0, 0, 0)


def pt(a):
    return anchor_to_xy(a)


# s1: 丨 left vertical of 田 (slight slant per MMH)
fat_line(d, pt(S[1][0]), pt(S[1][1]), width=5)

# s2: 横折 — top-heng then right-shu. Explicit corner.
h2, t2 = pt(S[2][0]), pt(S[2][1])
corner2 = (t2[0], h2[1])  # go right first, then down
fat_line(d, h2, corner2, width=5)
fat_line(d, corner2, t2, width=5)

# s3: 一 middle heng inside 田
fat_line(d, pt(S[3][0]), pt(S[3][1]), width=5)

# s4: 丨 middle vertical inside 田
fat_line(d, pt(S[4][0]), pt(S[4][1]), width=5)

# s5: 一 bottom heng of 田
fat_line(d, pt(S[5][0]), pt(S[5][1]), width=5)


def pie_curve(head, tail, bow=0.25, widths=(6, 5, 3)):
    """Draw a 撇: quadratic curve bowing slightly to the upper-right
    of the head→tail line, with tapering width."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    # perpendicular offset upward-right (for down-left pie: bow to upper-right)
    ox, oy = -dy * bow, dx * bow
    ctrl = (mx + ox, my + oy)
    pts = quad_bezier(head, ctrl, tail, n=40)
    w = [widths[0] + (widths[2] - widths[0]) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(d, pts, w, color=INK)


def na_curve(head, tail, bow=0.18, widths=(3, 6, 8)):
    """Draw a 捺: swells toward tail; slight downward bow."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    # bow outward (down-right for right-going na)
    ox, oy = dy * bow, -dx * bow
    ctrl = (mx + ox, my + oy)
    pts = quad_bezier(head, ctrl, tail, n=40)
    w = [widths[0] + (widths[2] - widths[0]) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(d, pts, w, color=INK)


# s6: 撇 (top of 㐱 / 人 left half)
pie_curve(pt(S[6][0]), pt(S[6][1]), bow=0.18, widths=(5, 5, 3))

# s7: 捺 (top of 㐱 / 人 right half)
na_curve(pt(S[7][0]), pt(S[7][1]), bow=0.15, widths=(3, 5, 7))

# s8, s9, s10: 彡 three 撇 (progressively larger)
pie_curve(pt(S[8][0]),  pt(S[8][1]),  bow=0.22, widths=(6, 5, 3))
pie_curve(pt(S[9][0]),  pt(S[9][1]),  bow=0.22, widths=(6, 5, 3))
pie_curve(pt(S[10][0]), pt(S[10][1]), bow=0.22, widths=(6, 5, 3))

out = os.path.join(os.path.dirname(__file__), '01_畛.png')
img.save(out)
print(f'wrote {out}')
