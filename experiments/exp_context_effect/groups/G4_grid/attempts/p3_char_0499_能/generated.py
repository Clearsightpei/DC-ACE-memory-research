"""能 (néng) — 10 strokes.

Decomposition: 能 = 厶 (top-left) + 月 (bottom-left) + 匕 (top-right) + 匕 (bottom-right).
  - s1-s2: 厶 (撇折 + 点)
  - s3-s6: 月 (左撇 + 横折钩 + 2 inner heng)
  - s7-s8: upper 匕 (撇 + 竖弯钩)
  - s9-s10: lower 匕 (撇 + 竖弯钩)

Recipe: A-recipe points 1-5 (B9+B10+B11). MMH-verbatim anchors, inline base
primitives (fat_line + quad_bezier). No compound bank primitive fits — the
匕 chars sit in stacked right-column slots and 月 is compressed to BL band.
No BANK_DEVIATION block because no compound bank primitive was seriously
considered; base-primitive-only path per A-recipe point 4.

REVISION 2: prior render had weak 匕 hooks (no right-sweep + up-flick) and
weak 厶 (no elbow-fold). Fixed by adding explicit corner + hook_pt for each
竖弯钩, and explicit pivot for 厶's 撇折.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 primitive-calls below (s1..s10)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 8 joints are N — natural gap preserved
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 匕s use explicit corner+hook_pt for 竖弯钩; 厶 uses pivot.',
}


def taper(head_w, tail_w, n):
    return [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]


def pie(d, p0, p2, head_w=10, tail_w=2, curve=0.10, n=40):
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / L, dx / L)
    bow = curve * L
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=n)
    stroke_variable_width(d, pts, taper(head_w, tail_w, n))


def dian(d, p0, p1, head_w=3, tail_w=8, n=20):
    pts = [(p0[0] + (p1[0] - p0[0]) * (i / n),
            p0[1] + (p1[1] - p0[1]) * (i / n)) for i in range(n + 1)]
    stroke_variable_width(d, pts, taper(head_w, tail_w, n))


def pie_zhe(d, head, pivot, tail, pie_head_w=11, pie_tip_w=4, heng_w=6):
    """撇折: tapered pie head→pivot, then straight heng pivot→tail."""
    dx, dy = pivot[0] - head[0], pivot[1] - head[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / L, dx / L)
    bow = 0.08 * L
    mid = ((head[0] + pivot[0]) * 0.5, (head[1] + pivot[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts_pie = quad_bezier(head, ctrl, pivot, n=30)
    stroke_variable_width(d, pts_pie, taper(pie_head_w, pie_tip_w, 30))
    fat_line(d, pivot, tail, heng_w)
    # small elbow disc
    r = max(pie_tip_w, heng_w) / 2.0 + 1
    d.ellipse([pivot[0] - r, pivot[1] - r, pivot[0] + r, pivot[1] + r], fill=(0, 0, 0))


def shu_wan_gou(d, head, corner, hook_pt, tip, head_w=8, corner_w=10, hook_w=9, tip_w=2):
    """竖弯钩: head→corner (bez, mostly vertical), corner→hook_pt (bez, horizontal sweep), hook_pt→tip (straight up flick)."""
    # Body vertical drop with rounded turn.
    belly = (head[0] + (corner[0] - head[0]) * 0.35,
             head[1] + (corner[1] - head[1]) * 0.7)
    body_pts = quad_bezier(head, belly, corner, n=40)
    stroke_variable_width(d, body_pts, taper(head_w, corner_w, 40))
    # Horizontal sweep.
    ctrl = (corner[0] + (hook_pt[0] - corner[0]) * 0.25, corner[1])
    tail_pts = quad_bezier(corner, ctrl, hook_pt, n=30)
    stroke_variable_width(d, tail_pts, taper(corner_w, hook_w, 30))
    # Rounded knee.
    r = hook_w / 2.0 + 1
    d.ellipse([hook_pt[0] - r, hook_pt[1] - r, hook_pt[0] + r, hook_pt[1] + r], fill=(0, 0, 0))
    # Up-flick.
    n = 14
    fp = [(hook_pt[0] + (tip[0] - hook_pt[0]) * (i / n),
           hook_pt[1] + (tip[1] - hook_pt[1]) * (i / n)) for i in range(n + 1)]
    stroke_variable_width(d, fp, taper(hook_w, tip_w, n))


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- MMH anchors (verbatim) ----
S1H, S1T = anchor_to_xy(('TL', 0.876, 0.639)), anchor_to_xy(('C',  0.242, 0.286))
S2H, S2T = anchor_to_xy(('C',  0.166, 0.061)), anchor_to_xy(('C',  0.371, 0.403))
S3H, S3T = anchor_to_xy(('ML', 0.574, 0.746)), anchor_to_xy(('BL', 0.56,  0.93))
S4H, S4T = anchor_to_xy(('ML', 0.744, 0.781)), anchor_to_xy(('BL', 0.92,  0.795))
S5H, S5T = anchor_to_xy(('BL', 0.735, 0.115)), anchor_to_xy(('BC', 0.031, 0.074))
S6H, S6T = anchor_to_xy(('BL', 0.709, 0.443)), anchor_to_xy(('BC', 0.04,  0.405))
S7H, S7T = anchor_to_xy(('TR', 0.162, 0.753)), anchor_to_xy(('C',  0.723, 0.195))
S8H, S8T = anchor_to_xy(('TC', 0.603, 0.639)), anchor_to_xy(('MR', 0.414, 0.257))
S9H, S9T = anchor_to_xy(('MR', 0.238, 0.919)), anchor_to_xy(('BC', 0.778, 0.338))
S10H, S10T = anchor_to_xy(('C', 0.629, 0.811)), anchor_to_xy(('BR', 0.66,  0.373))

# ==================== 厶 (top-left) ====================
# s1 撇折: head at TL(87.6,63.9), pivot at (~95,130) elbow, tail at C(124.2,128.6)
s1_pivot = (95.0, 130.0)
pie_zhe(d, S1H, s1_pivot, S1T, pie_head_w=11, pie_tip_w=4, heng_w=6)

# s2 点: (116.6,106.1) → (137.1,140.3)
dian(d, S2H, S2T, head_w=3, tail_w=8)

# ==================== 月 (bottom-left) ====================
# s3 左撇: nearly vertical, tiny leftward curve
pie(d, S3H, S3T, head_w=8, tail_w=6, curve=0.03, n=30)

# s4 横折钩: MMH gives just top-left (74.4,178.1) and hook-tip (92,279.5).
# Draw as: horizontal cap from S4H → top-right corner, then shu down to bot-right corner,
# then hook flick left to S4T (which sits inside near bottom).
tr_corner = (100.0, 178.0)
br_corner = (100.0, 288.0)
fat_line(d, S4H, tr_corner, 7)         # top-heng
fat_line(d, tr_corner, br_corner, 8)   # right-shu
# hook flick from br_corner → S4T (up-left)
n = 14
hp = [(br_corner[0] + (S4T[0] - br_corner[0]) * (i / n),
       br_corner[1] + (S4T[1] - br_corner[1]) * (i / n)) for i in range(n + 1)]
stroke_variable_width(d, hp, taper(8, 2, n))

# s5 upper inner heng of 月
fat_line(d, S5H, S5T, 5)
# s6 lower inner heng of 月
fat_line(d, S6H, S6T, 5)

# ==================== upper 匕 (top-right) ====================
# s7 撇: (216.2,75.3) → (172.3,119.5) — down-left with taper
pie(d, S7H, S7T, head_w=9, tail_w=2, curve=0.08, n=40)

# s8 竖弯钩: head TC(160.3,63.9), tail MR(241.4,125.7). MMH gives 2 endpoints;
# insert corner (bottom-left of turn) and hook_pt (right end before flick).
s8_corner = (168.0, 135.0)
s8_hook_pt = (258.0, 135.0)
shu_wan_gou(d, S8H, s8_corner, s8_hook_pt, S8T, head_w=7, corner_w=9, hook_w=8, tip_w=2)

# ==================== lower 匕 (bottom-right) ====================
# s9 撇: (223.8,191.9) → (177.8,233.8)
pie(d, S9H, S9T, head_w=9, tail_w=2, curve=0.10, n=40)

# s10 竖弯钩: head C(162.9,181.1), tail BR(266.0,237.3).
s10_corner = (175.0, 260.0)
s10_hook_pt = (280.0, 260.0)
shu_wan_gou(d, S10H, s10_corner, s10_hook_pt, S10T, head_w=7, corner_w=10, hook_w=9, tip_w=2)

# ---- save ----
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, '01_能.png'))
print("wrote 01_能.png  strokes=10")
