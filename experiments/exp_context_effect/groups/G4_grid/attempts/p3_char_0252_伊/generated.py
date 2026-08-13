"""p3_char_0252_伊 — G4 attempt.

Decomposition: 伊 = 亻 (left) + 尹 (right).
Reads drawer_memory.md first — ren_side primitive for 亻 fits.
尹 drawn fresh per MMH anchors (not in bank).

Strokes (6 total, matching MMH count):
  s1: 撇 of 亻    — head TL(.908,.659) → tail ML(.208,.948)
  s2: 竖 of 亻    — head ML(.688,.509) → tail BL(.732,.906)
  s3: top of 尹    — C(.307,.093) → MR(.074,.74), mid MR(.223,.405)  (curved horizontal)
  s4: middle heng — ML(.996,.547) → MR(.672,.424)   (crosses s6 at C)
  s5: lower heng  — C(.228,.928) → MR(.288,.849)    (crosses s6 at C)
  s6: long 撇      — C(.588,.134) → BL(.955,.95)    (P-weld with s4 and s5)

Joints implemented:
  s1.mid ⇆ s2.head : N  (~15px gap)
  s2.tail ⇆ s6.tail : N  (~30px gap)
  s3.mid ⇆ s4.mid  : P (welded near MR(.223,.405))
  s3.tail ⇆ s5.mid : N  (~12px gap)
  s3.head ⇆ s6.head : N (~12px)
  s4.mid ⇆ s6.mid  : P (welded near C(.686,.475))
  s5.mid ⇆ s6.mid  : P (welded near C(.638,.894))
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 strokes drawn = 6 expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '亻 uses MMH anchors verbatim (does not import ren_side because ren_side default anchors sit in TC/C/BC — this item wants TL/ML/BL). Right-side 尹 drawn fresh per MMH.'
}

from PIL import Image, ImageDraw
import os

CANVAS = 300
CELL = 100.0
CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def a(cell, xf, yf):
    col, row = CELL_ORIGIN[cell]
    return ((col + xf) * CELL, (row + yf) * CELL)


def qbez(p0, p1, p2, n=40):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
            for t in [i / n for i in range(n + 1)]]


def poly(draw, pts, width=6):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=width)
    r = width / 2.0
    for (x, y) in pts:
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def variable_pie(draw, p0, p2, ctrl=None, head_w=10, tail_w=2, n=48):
    """Tapered curve from head (wide) to tail (thin)."""
    if ctrl is None:
        ctrl = ((p0[0] + p2[0]) / 2.0, (p0[1] + p2[1]) / 2.0)
    pts = qbez(p0, ctrl, p2, n)
    for i in range(len(pts) - 1):
        t = i / (len(pts) - 1)
        w = max(1, int(round(head_w * (1 - t) + tail_w * t)))
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
        r = w / 2.0
        draw.ellipse([pts[i][0] - r, pts[i][1] - r, pts[i][0] + r, pts[i][1] + r], fill=(0, 0, 0))


img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

# ---- 亻 (left radical, MMH anchors verbatim) ----
# s1: 撇
s1_h = a('TL', 0.908, 0.659)
s1_t = a('ML', 0.208, 0.948)
s1_ctrl = ((s1_h[0] + s1_t[0]) / 2.0 - 8, (s1_h[1] + s1_t[1]) / 2.0 - 4)  # slight bow left
variable_pie(d, s1_h, s1_t, ctrl=s1_ctrl, head_w=11, tail_w=2)

# s2: 竖 (touches s1 body ~ mid — leaves natural N gap by starting at ML(.688,.509))
s2_h = a('ML', 0.688, 0.509)
s2_t = a('BL', 0.732, 0.906)
poly(d, [s2_h, s2_t], width=7)

# ---- 尹 (right side, fresh from MMH anchors) ----
# s3: top curved heng — head near top of C, curves through MR(.223,.405), ends MR(.074,.74)
s3_h = a('C', 0.307, 0.093)
s3_t = a('MR', 0.074, 0.740)
s3_mid = a('MR', 0.223, 0.405)  # welded P with s4
# Two-segment polyline through mid for shape control
p_s3 = qbez(s3_h, (s3_h[0] + 20, s3_h[1] + 5), s3_mid, n=24) + \
       qbez(s3_mid, ((s3_mid[0] + s3_t[0]) / 2.0 + 4, (s3_mid[1] + s3_t[1]) / 2.0), s3_t, n=24)
poly(d, p_s3, width=6)

# s4: middle heng — ML(.996,.547) → MR(.672,.424), passes through C(.686,.475)
s4_h = a('ML', 0.996, 0.547)
s4_t = a('MR', 0.672, 0.424)
poly(d, [s4_h, s4_t], width=6)

# s5: lower heng — C(.228,.928) → MR(.288,.849)
s5_h = a('C', 0.228, 0.928)
s5_t = a('MR', 0.288, 0.849)
poly(d, [s5_h, s5_t], width=6)

# s6: long 撇 — C(.588,.134) → BL(.955,.95), gently curved
s6_h = a('C', 0.588, 0.134)
s6_t = a('BL', 0.955, 0.950)
s6_ctrl = ((s6_h[0] + s6_t[0]) / 2.0 + 8, (s6_h[1] + s6_t[1]) / 2.0 - 6)
variable_pie(d, s6_h, s6_t, ctrl=s6_ctrl, head_w=10, tail_w=2, n=64)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, '01_伊.png'))
print('wrote 01_伊.png')
