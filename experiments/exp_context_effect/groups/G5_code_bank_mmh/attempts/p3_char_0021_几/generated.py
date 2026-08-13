# BANK_DEVIATION
# skipped: shu_wan_gou.py (bare-vertical form doesn't fit 几's s2 which
#          starts HORIZONTAL — 横折弯钩, not 竖弯钩)
# reason: 几 s2 = heng segment (top) + wan (curve down-right, bulging out) +
#         tiny upward hook. Bank has no heng_zhe_wan_gou primitive.
#         shu_wan_gou starts vertically from head, but MMH puts s2.head at
#         (119, 106) and needs a horizontal-then-turn shape.
# fresh_component: heng_zhe_wan_gou_for_几 (candidate future bank entry
#                  if 凡 / 风 / 见 / 儿 style compositions reappear)

SELF_CHECK = {
    'visual_ok': None,           # filled after render
    'stroke_count_ok': True,     # 2 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 's1 uses bank pie; s2 inlined heng_zhe_wan_gou (BANK_DEVIATION)'
}

import sys, pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from pie import draw_pie

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# --- Stroke 1: 撇 (pie) ---
# MMH: head ('TL', 0.952, 0.94) = (95, 94), tail ('BL', 0.378, 0.877) = (38, 288)
s1_head = (95, 94)
s1_tail = (38, 288)
draw_pie(d, head=s1_head, tail=s1_tail, bow_perp=14, w_head=9, w_tail=3)

# --- Stroke 2: 横折弯钩 (inline; BANK_DEVIATION) ---
# MMH: head ('C', 0.192, 0.063) = (119, 106), tail ('BR', 0.78, 0.188) = (278, 219)
# Joint s1.head ⇆ s2.head @ C, N-class, expected gap ~15.6 px.
# Actual gap: |(119,106) - (95,94)| = sqrt(24^2 + 12^2) = ~26 px  → N (small natural gap, OK)
s2_head = (119, 106)
s2_tail = (278, 219)

def _bezier2(p0, p1, p2, n=30):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts

def _bezier3(p0, p1, p2, p3, n=60):
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

# Heng segment: from (119, 106) slightly right/down to just before corner
pre_corner = (225, 110)
heng_pts = []
for i in range(15):
    t = i / 14
    heng_pts.append((s2_head[0] + t * (pre_corner[0] - s2_head[0]),
                     s2_head[1] + t * (pre_corner[1] - s2_head[1])))

# Rounded corner transition (short bezier through the elbow)
corner_apex = (245, 118)
elbow_end = (250, 145)
corner_pts = _bezier3(pre_corner, corner_apex, (252, 130), elbow_end, n=25)

# Wan curve: gentle bulge outward, going down and slightly right to bottom
bottom = (280, 258)
c1 = (250, 195)
c2 = (285, 235)
wan_pts = _bezier3(elbow_end, c1, c2, bottom, n=60)

# Hook: strong tick going up-LEFT from bottom, ending at MMH tail (278, 219)
# Since tail is above and slightly left of bottom, use a curved hook that
# briefly extends right/down then curls up-left.
hook_ctrl1 = (288, 250)
hook_pts = _bezier3(bottom, hook_ctrl1, (285, 235), s2_tail, n=30)

all_pts = heng_pts + corner_pts[1:] + wan_pts[1:] + hook_pts[1:]
ipts = [(int(round(x)), int(round(y))) for x, y in all_pts]
d.line(ipts, fill='black', width=8, joint='curve')

# End caps
for (x, y) in (ipts[0], ipts[-1]):
    d.ellipse([x - 4, y - 4, x + 4, y + 4], fill='black')

out = pathlib.Path(__file__).parent / '01_几.png'
img.save(out)
print(f'wrote {out}')
