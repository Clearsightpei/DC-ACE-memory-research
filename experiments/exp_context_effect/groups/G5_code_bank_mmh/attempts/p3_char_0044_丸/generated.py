# BANK_DEVIATION
# skipped: (none in bank match) — 丸's stroke 2 is 横斜钩/横折弯钩 family,
#          which is still not in the current bank (same missing class as 九).
# reason: no primitive covers the horizontal-then-curve-around-then-hook
#         morphology in one call.
# fresh_component: heng_zhe_wan_gou_for_丸
#
# Stroke 1 uses draw_pie from the bank (long left-sweeping pie).
# Stroke 2 is inlined with cubic bezier body + quadratic hook (learned
# from 九's earlier attempt, tightened per the drawer_memory B3 note).
# Stroke 3 uses draw_dian for the internal 丶.

"""p3_char_0044_丸 — G5 attempt.

MMH structural expectations (3 strokes):
  s1: pie  head TC(0.257,0.639)=(125.7, 63.9) tail BL(0.322,0.766)=(32.2, 276.6)
  s2: heng_zhe_wan_gou-like  head ML(0.542,0.477)=(54.2, 147.7)
                              tail BR(0.792,0.229)=(279.2, 222.9)
  s3: dian/short  head ML(0.835,0.893)=(83.5, 189.3)
                   tail BC(0.362,0.35) =(136.2, 235.0)

Joints (both P — welded):
  s1.mid(0.30) ⇆ s2.mid(0.19) @ C
  s1.mid(0.59) ⇆ s3.mid(0.42) @ BC
"""

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(_HERE, '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from pie import draw_pie          # noqa: E402
from dian import draw_dian        # noqa: E402


def _bezier2(p0, p1, p2, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, n=90):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def draw_heng_zhe_wan_gou(draw, heng_head, corner, bottom, hook_tip, width=7):
    """横折弯钩 inline: top-heng → corner → down-curve belly → up-hook."""
    body_top = _bezier2(
        heng_head,
        ((heng_head[0] + corner[0]) / 2, (heng_head[1] + corner[1]) / 2 - 2),
        corner, n=25,
    )
    shoulder = (hook_tip[0] - 4, hook_tip[1] + 40)
    c1 = (corner[0] - 15, bottom[1] + 18)
    c2 = (bottom[0] + 55, bottom[1] + 35)
    belly = _bezier3(corner, c1, c2, shoulder, n=80)
    hook_ctrl = (hook_tip[0] + 10, hook_tip[1] + 15)
    hook = _bezier2(shoulder, hook_ctrl, hook_tip, n=25)
    pts = body_top + belly[1:] + hook[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — 撇 (pie): long sweep from upper-center down to lower-left.
    draw_pie(d, head=(126, 64), tail=(38, 275),
             bow_perp=15, w_head=8, w_tail=3)

    # Stroke 2 — 横斜钩 / 横折弯钩 inline. Top-heng starts at MMH ML head
    # but shifted right (~x=100) toward the visible ink; corner at right of
    # top-heng; belly bowing down through bottom-center; hook tip at MMH
    # BR tail (~(275, 218)).
    draw_heng_zhe_wan_gou(
        d,
        heng_head=(95, 155),
        corner=(220, 148),
        bottom=(180, 268),
        hook_tip=(272, 220),
        width=7,
    )

    # Stroke 3 — the small internal 丶 that turns 九 into 丸.
    # MMH head (83.5, 189.3) → tail (136.2, 235.0). Shift head slightly
    # LEFT (to x=68) so the stroke clearly pierces the pie at ~y=195,
    # honoring the P-joint spec (s1.mid(0.59) ⇆ s3.mid(0.42) @ BC).
    draw_dian(d, head=(68, 188), tail=(140, 238),
              w_head=3, w_tail=9, bow=4, steps=44)

    out = os.path.join(_HERE, '01_丸.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 3 primitive calls: pie + inline HZWG + dian
    'endpoint_mismatches': [
        {'stroke': 2, 'field': 'head',
         'expected': (54, 148), 'actual': (95, 155),
         'delta_x_frac': 0.14,
         'reason': 'MMH underconstrained for compound zhe; shift right per '
                   'drawer_memory B3 lesson (力/艹/月-style calibration).'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Bank has no heng_zhe_wan_gou; inlined per BANK_DEVIATION. '
             '丸 = 九 + inner-dian; s3 rendered as compact dian.',
}


if __name__ == '__main__':
    print(render())
