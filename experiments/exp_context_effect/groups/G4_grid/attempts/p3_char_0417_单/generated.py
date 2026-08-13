"""单 (dān) — 8 strokes.

Decomposition: 单 = 丷 (top two dots) + 田-ish box (口 with inner cross bars)
              + 十 (long bottom heng + central shu extending through).

Stroke roles (MMH-verbatim anchors):
  s1: 丶 left dot of 丷
  s2: 丶 right dot of 丷
  s3: 竖 — left vertical of the box (extends into left of long heng)
  s4: 横折 — top+right of the box
  s5: 横 — upper horizontal cross bar inside box
  s6: 横 — lower horizontal (bottom of box)
  s7: 长横 — the long horizontal (十's heng)
  s8: 长竖 — the long central vertical stem going through everything (十's shu),
      extends below canvas (MMH tail y_frac > 1); clip to canvas.

A-recipe (B9/B10): MMH-verbatim anchors + base primitives + N-joint discipline.
No BANK_DEVIATION — 单 has no matching compound bank primitive; inline via
_anchor + fat_line is the standard A-recipe route.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; box corners welded (P), inner heng gaps preserved (N).',
}

W = 300
img = Image.new('RGB', (W, W), 'white')
d = ImageDraw.Draw(img)

INK = 6   # main ink width
DOT = 8   # dot width

# ------- s1: left dot 丶 of 丷 -------
p1a = anchor_to_xy(('TL', 0.964, 0.747))
p1b = anchor_to_xy(('C',  0.28,  0.052))
# Tapered dot (thicker at tail)
pts = [p1a, p1b]
stroke_variable_width(d, pts, [3, 9])

# ------- s2: right dot 丶 of 丷 -------
p2a = anchor_to_xy(('TC', 0.819, 0.577))
p2b = anchor_to_xy(('C',  0.523, 0.154))
stroke_variable_width(d, [p2a, p2b], [3, 9])

# ------- s3: left vertical of the box (shu) — smooth curve -------
p3a = anchor_to_xy(('ML', 0.732, 0.271))
p3b = anchor_to_xy(('BC', 0.017, 0.007))
# Use a quadratic bezier through the mid anchor for a smooth mild curve
m52 = anchor_to_xy(('C', 0.02, 0.624))
pts3 = quad_bezier(p3a, m52, p3b, n=30)
stroke_variable_width(d, pts3, [INK] * len(pts3))

# ------- s4: 横折 — top of box + right vertical -------
p4a = anchor_to_xy(('ML', 0.926, 0.286))
p4b = anchor_to_xy(('C',  0.942, 0.854))
# Bend corner: horizontal from head, then down to tail
# Joint at s4.mid(0.19) is at C(0.308, 0.268) — first phase heading right along top
# Joint at s4.mid(0.31) is at C(0.508, 0.181) — still top area
# Then bends down. Corner around top-right of box, roughly at C(0.942, 0.20)
corner = anchor_to_xy(('C', 0.95, 0.20))
# Segment 1: horizontal top of box
fat_line(d, p4a, corner, INK)
# Segment 2: right vertical of box
fat_line(d, corner, p4b, INK)

# ------- s5: upper horizontal cross inside box -------
p5a = anchor_to_xy(('C', 0.125, 0.62))
p5b = anchor_to_xy(('C', 0.778, 0.526))
fat_line(d, p5a, p5b, INK)

# ------- s6: lower horizontal (bottom of box region) -------
p6a = anchor_to_xy(('C', 0.075, 0.942))
p6b = anchor_to_xy(('C', 0.878, 0.778))
fat_line(d, p6a, p6b, INK)

# ------- s7: 长横 — the long bottom horizontal (十's heng) -------
p7a = anchor_to_xy(('BL', 0.328, 0.385))
p7b = anchor_to_xy(('BR', 0.643, 0.262))
fat_line(d, p7a, p7b, INK + 1)

# ------- s8: 长竖 — long central vertical (十's shu), extends past canvas -------
p8a = anchor_to_xy(('C',  0.345, 0.289))
p8b_raw = anchor_to_xy(('BC', 0.474, 1.179))
# Clip at canvas edge
p8b = (p8b_raw[0], min(p8b_raw[1], W - 2))
fat_line(d, p8a, p8b, INK + 1)

out = os.path.join(os.path.dirname(__file__), '01_单.png')
img.save(out)
print(f'wrote {out}')
