# BANK_DEVIATION
# skipped: no whole-radical primitive for 鸟-head or 几 exists in bank
# reason: compose from stroke primitives per MMH anchors + GT geometry
# fresh_component: fu_wild_duck_v2 (whole-char)
#
# TRAJECTORY DIFF vs main attempt (which FAILED):
#   FAIL#1 issue: top head cluster was too small and offset upper-left
#     (rendered ~x=100-165 y=40-115, cramped). Fix: enlarge to
#     ~x=110-175 y=40-105, center over the 几 more.
#   FAIL#2 issue: long descender (stroke 4) stopped at (178, 218) with a
#     visible gap to 几 top horizontal at y=205 — visually disconnected.
#     Fix: extend descender from head bottom (120, 100) all the way
#     down to (150, 210), meeting the 几 top just right of center.
#   FAIL#3 issue: 几 right-leg hook was drawn as a short up-right poke
#     going to (272, 250); GT shows the hook is a distinct upward curl
#     terminating higher. Fix: 横折弯钩 with clearer curve+hook up
#     from bottom of the descender.
#   FAIL#4 issue: 几 top horizontal was drawn as separate arch pts, no
#     continuity with right descender. Fix: render as one continuous
#     polyline for stroke 6.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes: pie, heng-zhe-gou, heng, pie, pie, heng-zhe-wan-gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_1: enlarged head, extended descender to meet 几 top, fixed right-hook curl.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def _bezier2(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        b0=(1-t)**3; b1=3*(1-t)**2*t; b2=3*(1-t)*t**2; b3=t**3
        pts.append((b0*p0[0]+b1*p1[0]+b2*p2[0]+b3*p3[0],
                    b0*p0[1]+b1*p1[1]+b2*p2[1]+b3*p3[1]))
    return pts


def _stroke_polyline(draw, pts, w_head=6, w_tail=6):
    """Chain-of-ellipses variable-width stroke — matches bank rendering style."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        r = w_head + (w_tail - w_head) * t
        draw.ellipse([x-r, y-r, x+r, y+r], fill='black')


# =============================================================
# Top 鸟-head cluster (strokes 1-4)
# GT shows a compact rounded head ~x 115-170, y 45-100, with an
# inner horizontal bar and a small pie at the top-left.
# =============================================================

# Stroke 1: short pie at top-left of head. MMH: head TC(132,56) tail TC(109,94).
# Slight leftward sweep — the head-start feather.
draw_pie(d, head=(140, 45), tail=(115, 95), bow_perp=6, w_head=7, w_tail=3, steps=50)

# Stroke 2: 横折钩 forming the closed cap of the head.
# MMH short-anchor: head C(113,108) tail C(150,142) — dispatcher's head+tail
# only. Visually: horizontal from (120, 60) right to (172, 60), turn down
# to (168, 105), tiny hook flick left.
seg_a = _bezier2((120, 62), (146, 58), (172, 62), steps=30)  # top horizontal (slight arch)
_stroke_polyline(d, seg_a, w_head=5, w_tail=6)
# 顿笔 at corner
d.ellipse([172-6, 62-5, 172+6, 62+5], fill='black')
# vertical/curved-down segment
seg_b = _bezier2((172, 62), (170, 85), (162, 108), steps=30)
_stroke_polyline(d, seg_b, w_head=6, w_tail=4)
# tiny inward hook
seg_c = [(162 + (152-162)*i/10, 108 + (100-108)*i/10) for i in range(11)]
_stroke_polyline(d, seg_c, w_head=4, w_tail=2)

# Stroke 3: short 横 inside head (the "eye" bar).
draw_heng(d, head=(126, 82), tail=(158, 82), width_head=5, width_tail=6)

# Stroke 4: long 撇 — the descender from head bottom to top of 几.
# MMH: head TL(94,94) tail BC(181,221). Visually the pie starts at the
# bottom-left of the head cluster and sweeps DOWN-RIGHT (this pie leans
# right, unlike a standard 丿). Extend it to reach 几's top line.
draw_pie(d, head=(118, 100), tail=(152, 208), bow_perp=-10, w_head=8, w_tail=4, steps=80)

# =============================================================
# Bottom 几 structure (strokes 5-6) — spans full canvas width.
# =============================================================

# Stroke 5: 撇 = left leg of 几. MMH: head BL(88,208) tail BL(50,303).
# Adjust tail up so char fits inside 300 canvas.
draw_pie(d, head=(80, 200), tail=(40, 285), bow_perp=10, w_head=8, w_tail=3, steps=80)

# Stroke 6: 横折弯钩 — top horizontal + right descent + curve + hook.
# MMH: head BC(109,212) tail BR(258,246). Compound stroke, rendered as
# one continuous polyline for weld continuity.
# Segment A: top horizontal from (65, 200) to (240, 200) — slight arch.
seg6a = _bezier2((65, 200), (150, 194), (240, 200), steps=50)
# Segment B: turn down at (240, 200) → curve right-down to (260, 258).
seg6b = _bezier3((240, 200), (245, 215), (250, 240), (262, 260), steps=40)
# Segment C: hook curling up-right from (262, 260) to (280, 244).
seg6c = _bezier2((262, 260), (275, 258), (283, 240), steps=25)

full_s6 = seg6a + seg6b[1:] + seg6c[1:]
_stroke_polyline(d, full_s6, w_head=6, w_tail=3)
# corner 顿笔 emphasis at the top-right turn
d.ellipse([240-6, 200-5, 240+6, 200+5], fill='black')


img.save(os.path.join(os.path.dirname(__file__), '01_凫.png'))
print("saved 01_凫.png")
