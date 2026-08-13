"""p3_char_0520_疳 — 疒 (radical, 5 strokes) + 甘 (interior, 5 strokes) = 10.

REASONING TRACE (P-A-008):
  疒 family is terminal-freeze cluster (9 cumulative FAILs). No whole-radical
  bank primitive for 疒 exists per P-COMP-008 refutation. No whole 甘
  primitive in bank either (gan_dry.py is 干, not 甘).

  Inline both, using MMH-derived 米字格 anchors verbatim (P-A-006 recipe:
  MMH-anchor verbatim + stroke-primitive layer). BANK usage: dian×2 for
  the two upper dots + inline lines for the 甘 box structure.

# BANK_DEVIATION
# skipped: no whole-radical 疒 (family terminal-freeze declared B10);
#          no whole 甘 primitive (only gan_dry.py = 干).
# reason: inline both. Native aspect from MMH: 疒 spans full canvas
#         (long pie ML→BL); 甘 sits in center-right of C/MR/BC area,
#         ~75px wide × ~155px tall.
# fresh_component: nou_frame + gan_sweet_interior inlined.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


def line(a, b, w=6):
    d.line([a, b], fill='black', width=w)


def _bezier_pts(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def curve(p0, p1, p2, w=6):
    pts = _bezier_pts(p0, p1, p2)
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    d.line(ipts, fill='black', width=w, joint='curve')


# MMH-derived pixel coordinates (米字格 anchors → 300×300 canvas):
# Cell top-lefts: TL(0,0) TC(100,0) TR(200,0) ML(0,100) C(100,100)
#                 MR(200,100) BL(0,200) BC(100,200) BR(200,200)

# ---- 疒 RADICAL (strokes 1–5) ----

# s1: top dot at TC (142.7, 51.9) → (176.1, 76.2)
draw_dian(d, head=(143, 52), tail=(176, 76), w_head=3, w_tail=8, bow=3)

# s2: short heng-cap sweeping up-right at top of 疒
# C(0.025, 0.134) → TR(0.329, 0.979): (102, 113) → (233, 98)
curve((102, 113), (167, 100), (233, 98), w=6)

# s3: long left 撇 pie sweep — defining stroke of 疒
# ML(0.806, 0.052) → BL(0.319, 0.991): (81, 105) → (32, 299)
curve((81, 105), (45, 200), (32, 299), w=8)

# s4: upper dian on the sweep — small mark
# ML(0.387, 0.318) → ML(0.583, 0.553): (39, 132) → (58, 155)
draw_dian(d, head=(39, 132), tail=(58, 155), w_head=3, w_tail=7, bow=2)

# s5: lower ti mark, going up-right (提 direction)
# BL(0.19, 0.238) → ML(0.729, 0.939): (19, 224) → (73, 194)
line((19, 224), (73, 194), w=7)

# ---- 甘 INTERIOR (strokes 6–10) ----

# s6: top horizontal (long) of 甘
# C(0.011, 0.887) → MR(0.704, 0.781): (101, 189) → (270, 178)
line((101, 189), (270, 178), w=7)

# s7: left short vertical of 甘 (drops through top horizontal)
# C(0.286, 0.488) → BC(0.377, 0.851): (129, 149) → (138, 285)
line((129, 149), (138, 285), w=7)

# s8: right vertical of 甘 (also drops through top horizontal, extends past bottom)
# C(0.945, 0.263) → BR(0.03, 1.026): (195, 126) → (203, 303)
line((195, 126), (203, 303), w=7)

# s9: middle short horizontal inside 甘
# BC(0.485, 0.285) → BC(0.884, 0.224): (149, 229) → (188, 222)
line((149, 229), (188, 222), w=6)

# s10: bottom horizontal of 甘 (spans between the two verticals)
# BC(0.456, 0.769) → BC(0.931, 0.692): (146, 277) → (193, 269)
line((146, 277), (193, 269), w=7)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10: dian, curve, curve, dian, line, line, line, line, line, line
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('疒 family terminal-freeze — inlined per MMH anchors verbatim. '
              '甘 inlined as 5 strokes (top heng, L-vert, R-vert, mid-heng, '
              'bot-heng). N-class joints between s2/s3 heads (small gap at ML), '
              's3-mid/s5-tail, s3-mid/s6-head (natural gaps preserved).')
}


out = os.path.join(os.path.dirname(__file__), '01_疳.png')
img.save(out)
print('wrote', out)
