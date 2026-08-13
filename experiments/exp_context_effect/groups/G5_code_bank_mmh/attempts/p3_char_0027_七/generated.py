# BANK_DEVIATION
# skipped: shu_wan_gou.py
# reason: MMH tail anchor for stroke 2 is at (~230, 267) — near canvas bottom, not
#   the "upper-right after hook" that shu_wan_gou is parameterized for. Feeding
#   this tail into the bank fn would push the bottom of the curve off-canvas
#   (bottom_extra pushes bottom_y to 327). The 七 second stroke bends into the
#   tail rather than hooking up above it.
# fresh_component: pie_wan_for_qi  (vertical-ish descent → bend right ending
#   near BR, tiny terminal upflick)
"""Draw 七 (qi, seven) — 2 strokes: rising heng + curving pie-wan.

MMH structural expectations:
  stroke 1: BL(0.296,0.004) → MR(0.584,0.649)  # rising heng
  stroke 2: TC(0.066,0.803) → BR(0.297,0.672)  # descend + bend right
  joint  1: P at C  (s1 mid ≈ s2 mid)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)
from heng import draw_heng  # noqa: E402


# ---------- 米字格 anchor helper ----------------------------------------------
CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


# ---------- stroke 2 (inline: pie_wan_for_qi) --------------------------------
def _bezier3(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        pts.append((
            b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0],
            b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1],
        ))
    return pts


def draw_pie_wan_for_qi(d, head, tail, width=7):
    hx, hy = head
    tx, ty = tail
    # Descend nearly-vertical from head with slight left lean, bend at the
    # bottom, sweep right along a low shoulder to tail. Terminal upflick is
    # continuous with the body (single polyline, no separate segment).
    c1 = (hx + 4, hy + 100)                     # keep upper body near hx
    knee = (hx + 25, ty + 8)                    # low shoulder before sweep-right
    c2 = ((knee[0] + tx) / 2, ty + 30)          # under-swing gives calligraphic wan
    body = _bezier3(head, c1, knee, tail, n=80)
    # continuous small upflick: extend past tail with a short bezier segment
    up_tip = (tx + 6, ty - 14)
    flick_c = (tx + 3, ty - 3)
    flick = _bezier3(tail, flick_c, ((tx + up_tip[0]) / 2, (ty + up_tip[1]) / 2),
                     up_tip, n=20)
    pts = body + flick[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    d.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')
    _ = c2


# ---------- render ------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

s1_head = anchor('BL', 0.296, 0.004)   # (29.6, 200.4)
s1_tail = anchor('MR', 0.584, 0.649)   # (258.4, 164.9)
s2_head = anchor('TC', 0.066, 0.803)   # (106.6, 80.3)
s2_tail = anchor('BR', 0.297, 0.672)   # (229.7, 267.2)

draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=11)
draw_pie_wan_for_qi(d, s2_head, s2_tail, width=8)

out = pathlib.Path(__file__).parent / '01_七.png'
img.save(out)


# ---------- SELF_CHECK --------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 primitives (draw_heng + draw_pie_wan_for_qi)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # P: s2 bezier passes through (~120, 185) area
    'overall_pass': True,
    'notes': 'BANK_DEVIATION for stroke 2: shu_wan_gou would push bottom off canvas '
             'because MMH tail is at y=267. Inlined pie_wan_for_qi.',
}
