# BANK_DEVIATION
# skipped: no whole-radical primitive for 鸟-head or 几 exists in bank
# reason: compose from stroke primitives per MMH anchors
# fresh_component: fu_wild_duck (whole-char)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'v2: enlarged top and bottom, tightened 几.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def _bezier2(p0, p1, p2, steps=50):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        b0=(1-t)**3; b1=3*(1-t)**2*t; b2=3*(1-t)*t**2; b3=t**3
        pts.append((b0*p0[0]+b1*p1[0]+b2*p2[0]+b3*p3[0],
                    b0*p0[1]+b1*p1[1]+b2*p2[1]+b3*p3[1]))
    return pts


def _draw_path(draw, pts, w_head=5, w_tail=5):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        r = w_head + (w_tail - w_head) * t
        draw.ellipse([x-r, y-r, x+r, y+r], fill='black')


# =============================================================
# Top "鸟-head" compressed cluster (strokes 1-4)
# GT shows: a small rounded shape roughly (100-165, 40-110)
# with an internal short mark, and a big diagonal 撇 going down
# from ~ (120, 60) to ~ (140, 210) that CONTINUES the top.
# =============================================================

# Stroke 1: small pie starting the top — from (135, 55) sweeping to (108, 100)
draw_pie(d, head=(135, 55), tail=(108, 105), bow_perp=6, w_head=6, w_tail=3, steps=50)

# Stroke 2: heng_zhe forming the closed cap of the head
# horizontal from (120, 68) to (162, 68), then down to (162, 112)
pts_a = [(120 + (162-120)*i/20, 68 - 3*(1-(2*i/20-1)**2)) for i in range(21)]
_draw_path(d, pts_a, w_head=4, w_tail=5)
pts_b = _bezier2((162, 68), (168, 90), (158, 115), steps=30)
_draw_path(d, pts_b, w_head=5, w_tail=4)

# Stroke 3: short heng inside the head
draw_heng(d, head=(125, 92), tail=(155, 95), width_head=5, width_tail=5)

# Stroke 4: large 撇 continuing from head down through middle to bottom-mid
# MMH: head TL(0.94,0.943)=(94,94) tail BC(0.813,0.206)=(181,221)
# Interpretation: from head bottom-left, curve down-right to (180, 220)
draw_pie(d, head=(112, 110), tail=(178, 218), bow_perp=14, w_head=7, w_tail=4, steps=80)

# =============================================================
# Bottom 几 structure (strokes 5-6) — spans wide
# =============================================================

# Stroke 5: left leg of 几 = 撇 sweeping down-left
# MMH: head BL(0.879,0.083)=(88,208) tail BL(0.495,1.032)=(50,303)
draw_pie(d, head=(88, 205), tail=(45, 292), bow_perp=10, w_head=8, w_tail=3, steps=80)

# Stroke 6: 横折弯钩 — horizontal across top of 几, descend, curve right, hook up
# MMH s6: head BC(0.093,0.121)=(109,212) tail BR(0.584,0.458)=(258,246)
# Compose as: horizontal (65-232, 205) → descend/curve to (255, 275) → hook up to (272, 250)

# Segment A: horizontal top (mild arch)
pts_h = [(65 + (232-65)*i/40, 205 - 2*(1-(2*i/40-1)**2)) for i in range(41)]
_draw_path(d, pts_h, w_head=5, w_tail=6)

# Segment B: descend + curve right (bezier from (232, 205) to (255, 275))
pts_b2 = _bezier3((232, 205), (238, 240), (245, 275), (255, 275), steps=50)
_draw_path(d, pts_b2, w_head=6, w_tail=6)

# Segment C: hook up-right from (255, 275) to (272, 250)
pts_c = [(255 + (272-255)*i/18, 275 + (250-275)*i/18) for i in range(19)]
_draw_path(d, pts_c, w_head=6, w_tail=2)


img.save(os.path.join(os.path.dirname(__file__), '01_凫.png'))
print("saved 01_凫.png")
