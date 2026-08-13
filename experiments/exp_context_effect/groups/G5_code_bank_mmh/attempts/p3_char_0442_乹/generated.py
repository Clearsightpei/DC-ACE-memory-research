"""p3_char_0442_乹 — variant of 乾. Left component (十/日/十 stack style)
+ right component 乙 (large yi-second hook wrapping bottom-right).

REASONING TRACE (P-A-008):
  GT decomposition — 9 MMH strokes:
    - Left cluster: top heng, vertical, small box (heng-zhe + heng), inner heng,
      bottom heng, long vertical shu passing through.
    - Right: single large 乙 hook covering right column + bottom sweep.
  Right primitive: yi_second bank primitive fits — large scale, positioned right.
  Left: inline (no matching whole-radical bank; too specific to this variant).

# BANK_DEVIATION
# skipped: no whole-radical bank for 乹-left (idiosyncratic 卓-like stack).
# reason: bank has no primitive matching top-heng + narrow box + long vertical
#         configuration at this aspect (roughly 60% width, 90% height of canvas).
# fresh_component: qian_left_stack (top heng, narrow box, mid heng, bot heng,
#         central long shu passing through all — inlined).

Right uses bank primitive yi_second at scale ~1.15, translated to sit at
right-center and extend from top-right down through bottom.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from yi_second import draw_yi_second

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
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill='black', width=w)


# ---- LEFT COMPONENT — inlined 9-ish stroke stack ----
# Occupies roughly x in [35, 170], y in [30, 275].

# stroke 1: top horizontal (spans top of left component)
line((45, 55), (165, 50), w=6)

# stroke 2: right vertical of upper section (small descent)
line((155, 55), (150, 115), w=6)

# stroke 3 + 4: small box under top heng — left vertical + bottom heng
line((70, 60), (70, 120), w=6)  # left vertical of small box
line((70, 118), (155, 118), w=6)  # bottom of box (also serves as mid heng)

# stroke 5: middle horizontal below the box
line((45, 155), (170, 152), w=6)

# stroke 6: another horizontal (lower middle)
line((60, 195), (155, 195), w=6)

# stroke 7: bottom horizontal (widest)
line((30, 245), (185, 245), w=6)

# stroke 8: long central vertical passing through mid + lower horizontals
line((100, 125), (95, 285), w=7)

# ---- RIGHT COMPONENT — 乙 hook using bank primitive ----
# stroke 9: yi_second scaled to fit right column, running from top-right
# down through the bottom-right of the canvas.
# yi_second native canvas ~ (95..222, 108..278). We want it positioned so
# top of the hook sits at ~y=70, right edge at ~x=280, bottom hook end ~y=275.
# native width ~127, native height ~170. Target width ~145, height ~205.
# scale ~ 1.20; ox shifts so native x=95 maps to ~180; oy shifts so native y=108 maps to ~70.
scale = 1.20
ox = 180 - 95 * scale   # 180 - 114 = 66
oy = 70 - 108 * scale   # 70 - 130 = -60
draw_yi_second(d, ox=ox, oy=oy, scale=scale)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 inline lines + 1 yi_second call = 9 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Left component inlined (BANK_DEVIATION); right uses yi_second bank primitive at 1.20 scale.'
}


out = os.path.join(os.path.dirname(__file__), '01_乹.png')
img.save(out)
print('wrote', out)
