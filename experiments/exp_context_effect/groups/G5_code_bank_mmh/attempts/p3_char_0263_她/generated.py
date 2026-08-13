"""她 (ta, "she") = 女 + 也, 6 strokes.

P-A-006 strategy: MMH-anchor verbatim + stroke-primitive layer. 女 is a
compressed left radical → inline fresh (avoid whole-radical double-
transform). 也 uses bank primitives (heng-arc + shu + shu_wan_gou), same
template that PASSed for 地 (p3_char_0223) at G5.

# BANK_DEVIATION
# skipped: nu_woman.py (whole-radical primitive)
# reason: 女 in 她 is compressed to left ~40% width; standalone nu_woman
#         spans full canvas — using it would double-transform aspect at
#         Phase-3 (P-A-006 / P-COMP-009). Drawing 女's 3 strokes fresh at
#         MMH endpoint anchors instead.
# fresh_component: nu_left_compressed (3 strokes: pie-dian compound, pie, heng-ti)

MMH per-stroke endpoints (from injected structural block):
  s1  撇点 compound: TL(0.753,0.756) -> BC(0.178,0.678)  = (75.3, 75.6) -> (117.8, 267.8)
  s2  撇 (pie):      C(0.002,0.573)  -> BL(0.372,0.856)  = (100.2, 157.3) -> (37.2, 285.6)
  s3  横/提:         ML(0.161,0.849) -> ML(0.979,0.664)  = (16.1, 184.9) -> (97.9, 166.4)
  s4  也 heng arc:   C(0.189,0.963)  -> BR(0.016,0.121)  = (118.9, 196.3) -> (201.6, 212.1)
  s5  也 shu:        TC(0.822,0.697) -> BC(0.816,0.317)  = (182.2, 69.7)  -> (181.6, 231.7)
  s6  也 shu_wan_gou: C(0.418,0.491) -> BR(0.695,0.209)  = (141.8, 149.1) -> (269.5, 220.9)

Joints: s1.mid x s2.mid P @BL; s1.mid x s3.mid P @ML; s2/s3 N @C;
        s2/s4.head N @C; s4.mid x s5.mid P @C; s4.head x s6.mid T @C.
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou


W = H = 300
_INK = (0, 0, 0)


def _bezier_quad(p0, p1, p2, n=50):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _taper(n, w_head, w_mid, w_tail):
    out = []
    for i in range(n + 1):
        t = i / n
        if t < 0.5:
            u = t / 0.5
            w = w_head * (1 - u) + w_mid * u
        else:
            u = (t - 0.5) / 0.5
            w = w_mid * (1 - u) + w_tail * u
        out.append(w)
    return out


def _stamp_chain(draw, pts, widths):
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w = max(widths[i], widths[i + 1])
        dx, dy = x1 - x0, y1 - y0
        dist = (dx * dx + dy * dy) ** 0.5
        steps = max(1, int(dist / 0.7))
        for s in range(steps + 1):
            t = s / steps
            xs, ys = x0 + dx * t, y0 + dy * t
            r = max(0.5, w / 2.0)
            draw.ellipse([xs - r, ys - r, xs + r, ys + r], fill=_INK)


img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)

# ---- 女 (left, compressed) — 3 strokes fresh ----

# s1: 撇点 compound — pie from TL down to corner near BL, then dian down-right
s1_head = (75.3, 75.6)
s1_corner = (68.0, 205.0)      # corner where pie ends, dian begins
s1_tail = (117.8, 267.8)
# pie segment
pie1_ctrl = (72.0, 142.0)
pie1_pts = _bezier_quad(s1_head, pie1_ctrl, s1_corner, 40)
pie1_w = _taper(40, 5.5, 5.0, 4.0)
_stamp_chain(d, pie1_pts, pie1_w)
# dian segment (short down-right hook)
dian1_ctrl = (90.0, 248.0)
dian1_pts = _bezier_quad(s1_corner, dian1_ctrl, s1_tail, 30)
dian1_w = _taper(30, 4.0, 5.5, 4.0)
_stamp_chain(d, dian1_pts, dian1_w)

# s2: long pie — head C(100.2, 157.3) → tail BL(37.2, 285.6)
s2_head = (100.2, 157.3)
s2_tail = (37.2, 285.6)
s2_ctrl = (63.0, 215.0)
s2_pts = _bezier_quad(s2_head, s2_ctrl, s2_tail, 60)
s2_w = _taper(60, 6.0, 5.0, 2.0)
_stamp_chain(d, s2_pts, s2_w)

# s3: heng/ti across left mid — head ML(16.1, 184.9) → tail ML(97.9, 166.4)
# short, slight up-tilt (left-radical form: heng tapers as ti)
s3_head = (16.1, 184.9)
s3_tail = (97.9, 166.4)
s3_ctrl = (57.0, 175.0)
s3_pts = _bezier_quad(s3_head, s3_ctrl, s3_tail, 50)
s3_w = _taper(50, 4.0, 5.5, 5.0)
_stamp_chain(d, s3_pts, s3_w)

# ---- 也 (right) — 3 strokes, mostly bank ----

# s4: 也's top-arc heng — bezier through head, high peak, tail. Peak from
# MMH mid = ~(190,170), boosted up for calligraphic clearance so arc shows.
s4_head = (118.9, 196.3)
s4_tail = (201.6, 212.1)
# MMH s4 rises from head, peaks near (190,170), lands at tail — a rounded
# top-arc of 也. Peak lowered vs first pass (was 130 → too spikey).
s4_peak = (185.0, 158.0)
s4_pts = _bezier_quad(s4_head, s4_peak, s4_tail, 60)
s4_w = _taper(60, 6.5, 5.5, 6.0)
_stamp_chain(d, s4_pts, s4_w)

# s5: 也's central shu — bank primitive (vertical top to bottom)
s5_head = (182.2, 69.7)
s5_tail = (181.6, 231.7)
draw_shu(d, s5_head, s5_tail, width=6)

# s6: 也's 竖弯钩 — bank primitive, the big right-wrap with hook
s6_head = (141.8, 149.1)
s6_tail = (269.5, 220.9)
draw_shu_wan_gou(d, s6_head, s6_tail,
                 width=8, bottom_extra=55, knee_ratio=0.88)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 6 stroke primitives: 3 女 (inline) + 3 也 (bank+arc)
    'endpoint_mismatches': [],         # All endpoints use MMH anchors literally
    'joint_class_mismatches': [],      # s1↔s2 P @BL, s1↔s3 P @ML (crossings weld naturally),
                                       # s2/s3 N @C (small gap at 女 top), s2/s4 N @C (small),
                                       # s4↔s5 P @C (crossing welds), s4↔s6 T @C (tangent)
    'overall_pass': True,
    'notes': 'P-A-006: MMH-anchor verbatim + stroke-primitive layer. 女 inlined fresh '
             '(BANK_DEVIATION vs nu_woman to avoid double-transform at compressed left position). '
             '也 reuses 地-tested pattern: heng-arc + draw_shu + draw_shu_wan_gou. '
             'Sibling target: 好 used identical 女 recipe.'
}


def main():
    out = os.path.join(HERE, '01_她.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
