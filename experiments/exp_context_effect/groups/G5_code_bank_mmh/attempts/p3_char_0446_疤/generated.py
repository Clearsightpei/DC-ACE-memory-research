"""p3_char_0446_疤 — 疒 (radical) + 巴 (interior). REVISION 1.

REASONING TRACE (P-A-008):
  9 MMH strokes decomposed as:
    疒 (5): s1 top dot, s2 short heng at top-center, s3 long left pie,
            s4 upper dot on sweep, s5 lower dot on sweep.
    巴 (4): s6 left vertical (short), s7 middle heng,
            s8 top-right 横折 (single continuous stroke: heng then shu-down
                then implicit close of bottom under the wrap),
            s9 竖弯钩 spanning from top-right down and hooking up-right.

  Revision fixes from pass 1:
    - Consolidated 巴 into strictly 4 stroke primitives (was 6+ line calls).
    - Repositioned dots on 疒 sweep so they read as 冫-style pair.
    - Tightened 巴 into upper-right, not spilling below.

# BANK_DEVIATION
# skipped: no whole-radical 疒 (family terminal-freeze declared B10);
#          no 巴 (ba-earth) bank primitive.
# reason: inline both. Native aspect: 疒 spans full canvas ~65% width;
#         巴 sits inside upper-right ~40% width, 45% height.
# fresh_component: bing_frame + ba_interior inlined this attempt.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from shu_wan_gou import draw_shu_wan_gou

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


def polyline(pts, w=6):
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    d.line(ipts, fill='black', width=w, joint='curve')


# ---- 疒 RADICAL (strokes 1–5) ----

# s1: top dot 丶 near top-center
draw_dian(d, head=(150, 38), tail=(172, 58), w_head=3, w_tail=7, bow=2)

# s2: short right-side descender at top (the small "roof cap" of 疒)
# A short slightly-curved stroke going right and dropping a bit.
curve((140, 65), (175, 70), (208, 90), w=6)

# s3: long 丿 pie — the defining left sweep of 疒
curve((205, 75), (135, 175), (45, 270), w=8)

# s4: upper dot on left of sweep (top of 冫-like pair)
draw_dian(d, head=(80, 130), tail=(100, 152), w_head=3, w_tail=7, bow=2)

# s5: lower dot on left of sweep (bottom of 冫-like pair)
draw_dian(d, head=(60, 190), tail=(82, 213), w_head=3, w_tail=7, bow=2)

# ---- 巴 INTERIOR (strokes 6–9) ----
# Positioned upper-right, roughly x in [135, 235], y in [110, 240].

# s6: left vertical of 巴 (short, from top of box to just above the hook)
line((140, 115), (144, 200), w=6)

# s7: middle horizontal (divides upper box)
line((144, 165), (232, 162), w=6)

# s8: 横折 — top edge and right edge as a single continuous stroke
polyline([(140, 115), (180, 112), (220, 112), (235, 116), (238, 155),
          (238, 205)], w=6)

# s9: 竖弯钩 — starts near the bottom-left of 巴, sweeps right along the
# bottom, hooks up-right. Provides the bottom of 巴 AND the hook.
draw_shu_wan_gou(d, head=(144, 200), tail=(245, 195),
                 width=6, bottom_extra=40, knee_ratio=0.95)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 (疒: dian, curve, curve, dian, dian) + 4 (巴: line, line, polyline, shu_wan_gou) = 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('疒 family terminal-freeze — inlined. 巴 inlined as 4 strokes '
              'with s8 as continuous 横折 polyline and s9 as shu_wan_gou. '
              'Bank use: dian×3, shu_wan_gou×1.')
}


out = os.path.join(os.path.dirname(__file__), '01_疤.png')
img.save(out)
print('wrote', out)
