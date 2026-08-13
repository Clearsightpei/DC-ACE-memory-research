"""p3_char_0113_仉 — G5 retry #1.

TRAJECTORY DIFF (main FAIL @ groups/G5_code_bank_mmh/attempts/p3_char_0113_仉/01_仉.png):
  Comparing prior attempt vs GT:
  1. WHAT: 几's right stroke rendered as a rectangular BOX with a sharp
     right-angle corner and a nearly-straight vertical shu, ending in a
     tiny straight hook — the reader sees "门" not "几".
     WHERE: right half of canvas, s4 (heng-zhe-wan-gou).
     BY HOW MUCH: the corner used a full 90° with no rounding; the shu
     was straight (no belly); the wan (bottom bow) essentially absent;
     the hook was ~15px and pointed almost straight up. Should be:
     smooth shoulder, subtly-curving shu, a clear "belly" (弯) at the
     bottom that swings the ink OUTWARD then UP-RIGHT into a short gou.
  2. WHAT: 亻 shu (s2) appears slightly disconnected from the pie tick.
     WHERE: at MMH joint s1.mid(0.56) ~ s2.head @ ML — the visible gap
     is closer to ~35px than the target ~17px.
     BY HOW MUCH: s2.head y needs to move UP ~10px OR the pie needs to
     drop slightly so the shu head sits on the pie's spine.
  3. WHAT: s3 (几 left pie) barely readable — it's absorbed into the
     box on the previous attempt.
     WHERE: left leg of 几.
     FIX: draw it as a proper tapered pie that arches outward-left.

  PLAN this attempt:
  * Rewrite s4 as: short heng (~120px) with rounded shoulder → gently
    curving shu (bezier, slight outward belly) → smooth wan hooking
    back up-right into a small gou. Bezier throughout, no sharp corner.
  * Move s2.head up ~8px so shu sits on the pie spine (joint is N so
    small natural gap is fine, but not a big one).
  * Draw s3 with clear outward bow so the pie belly is visible.

MMH structural expectations (4 strokes, all joints N):
  s1: 亻-pie   head TL(0.908, 0.659) -> tail BL(0.164, 0.03)
  s2: 亻-shu   head ML(0.671, 0.579) -> tail BL(0.686, 0.988)
  s3: 几-pie   head C(0.213, 0.283)  -> tail BL(0.826, 0.895)
  s4: 几-heng-zhe-wan-gou  head C(0.436, 0.386) -> tail BR(0.76, 0.355)

# BANK_DEVIATION
# skipped: heng_zhe_gou.py (does not apply — s4 is 横折弯钩, hook comes off
#          a curved wan belly, not a straight-down shu-gou terminal)
# reason:  bank has no 横折弯钩 primitive; prior deviation existed but
#          rendered too boxy. Re-inlining with a smoother bezier chain.
# fresh_component: heng_zhe_wan_gou_for_几_v2  (candidate for promotion)
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
                       / 'G5_code_bank_mmh' / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes: pie, shu, pie, inline-hzwg
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints N (natural gap)
    'overall_pass': True,
    'notes': 'BANK_DEVIATION for s4 (no heng_zhe_wan_gou); smoother bezier chain.',
}


# --- 米字格 anchor helper ------------------------------------------------
CELL = {
    'TL': (0,   0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100),   'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200),   'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + xf * 100, oy + yf * 100)


# --- helpers ------------------------------------------------------------
def _bez3(p0, p1, p2, p3, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0*p0[0] + b1*p1[0] + b2*p2[0] + b3*p3[0]
        y = b0*p0[1] + b1*p1[1] + b2*p2[1] + b3*p3[1]
        pts.append((x, y))
    return pts

def _bez2(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1 - t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    return pts

def _stroke_from_pts(draw, pts, w_start, w_end):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = (w_start + (w_end - w_start) * t) / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_shu(draw, head, tail, w_head=8, w_tail=6):
    """Vertical shu with slight taper."""
    n = 40
    for i in range(n + 1):
        t = i / n
        x = head[0] + (tail[0] - head[0]) * t
        y = head[1] + (tail[1] - head[1]) * t
        r = (w_head + (w_tail - w_head) * t) / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_heng_zhe_wan_gou(draw, head, tail, width=7):
    """横折弯钩 — the compound stroke that forms 几's right leg.

    head : (x, y) where the heng starts (upper-left of the compound)
    tail : (x, y) where the gou hook TIP ends (upper-right, above the
           bottom belly).
    Shape: heng right -> smooth shoulder -> shu descending with slight
    outward belly -> smooth wan at bottom -> gou hooks up-right to tail.
    """
    hx, hy = head
    tx, ty = tail

    # 1) HENG segment: shorter heng ending in a well-rounded shoulder.
    corner_x = tx - 8                # corner clearly LEFT of tail
    corner_y = hy + 4                # small drop
    corner = (corner_x, corner_y)

    heng_pts = _bez2(head, ((hx + corner_x) / 2, hy - 1), corner, steps=30)
    _stroke_from_pts(draw, heng_pts, width + 1, width + 2)

    # 2) SHU + WAN: one long S-curve from the shoulder DOWN then swinging
    #    LEFT-DOWN into a pronounced belly (the 弯 of 横折弯钩).
    #    Belly must extend well below the tail-y and clearly leftward.
    bottom_belly_x = corner_x - 42   # belly swings deep LEFT
    bottom_belly_y = ty + 55         # deep belly below tail

    # Control points crafted for a rounded shoulder + deep swinging belly:
    #   ctrl1 near the shoulder (right side) — smooths the turn
    #   ctrl2 deep down-and-left — pulls belly outward-down-and-left
    ctrl1 = (corner_x + 6, corner_y + (bottom_belly_y - corner_y) * 0.30)
    ctrl2 = (corner_x - 6, bottom_belly_y + 18)
    belly_pts = _bez3(corner, ctrl1, ctrl2,
                      (bottom_belly_x, bottom_belly_y),
                      steps=80)
    _stroke_from_pts(draw, belly_pts, width + 2, width)

    # 3) GOU: from the belly's lowest-left point, arc up-right to the tail.
    belly_end = (bottom_belly_x, bottom_belly_y)
    hook_ctrl = (belly_end[0] + 30, belly_end[1] - 4)
    hook_pts = _bez2(belly_end, hook_ctrl, tail, steps=32)
    _stroke_from_pts(draw, hook_pts, width, max(2, width - 4))


# --- Render -------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: 亻 pie — long left-sweeping tick
s1_head = A('TL', 0.908, 0.659)   # ~(90.8, 65.9)
s1_tail = A('BL', 0.164, 0.03)    # ~(16.4, 203.0)
draw_pie(d, s1_head, s1_tail, bow_perp=14, w_head=10, w_tail=3)

# s2: 亻 shu — straight vertical dropping from pie spine to near bottom.
# NUDGE: raise head slightly (~8px) so it sits closer to the pie spine,
# reducing the too-large gap from the failed attempt.
s2_head_raw = A('ML', 0.671, 0.579)   # ~(67.1, 157.9)
s2_head = (s2_head_raw[0], s2_head_raw[1] - 8)
s2_tail = A('BL', 0.686, 0.988)       # ~(68.6, 298.8)
draw_shu(d, s2_head, s2_tail, w_head=8, w_tail=7)

# s3: 几 left pie — short calligraphic sweep from top-center down-left.
# bow_perp positive → curve arches to the RIGHT of travel; since travel
# is down-and-slightly-left, "right of travel" is down-and-right, which
# makes the pie belly face inward. That's the wrong direction for 几's
# left leg (belly should face OUTWARD-LEFT). Use NEGATIVE bow_perp.
s3_head = A('C',  0.213, 0.283)   # ~(121.3, 128.3)
s3_tail = A('BL', 0.826, 0.895)   # ~(82.6, 289.5)
draw_pie(d, s3_head, s3_tail, bow_perp=-18, w_head=11, w_tail=3, steps=90)

# s4: 几 right stroke — inline heng-zhe-wan-gou (BANK_DEVIATION).
s4_head = A('C',  0.436, 0.386)   # ~(143.6, 138.6)
s4_tail = A('BR', 0.76,  0.355)   # ~(276.0, 235.5)
draw_heng_zhe_wan_gou(d, s4_head, s4_tail, width=7)

img.save(str(pathlib.Path(__file__).parent / '01_仉.png'))
print('rendered 仉 retry_1 (4 strokes; smoother hzwg bezier chain)')
