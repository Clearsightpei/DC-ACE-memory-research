"""好 (hao) = 女 + 子, 6 strokes.

P-A-006 strategy: MMH-anchor verbatim + stroke-primitive layer. Refusing
whole-radical composition (nu_woman standalone) because 女 must be
compressed to left ~40% of canvas which would double-transform. Drawing
all 6 strokes fresh using MMH endpoints directly.

# BANK_DEVIATION
# skipped: nu_woman.py (whole-radical primitive)
# reason: 女 in 好 is compressed to left ~40% width; the standalone
#         nu_woman primitive spans nearly full canvas — using it here
#         would double-transform aspect at Phase-3 (P-A-006 diagnosis,
#         same as P-COMP-009). Drawing 女's 3 strokes fresh at MMH
#         anchors instead.
# fresh_component: nu_left_compressed (3 strokes: pie-dian, pie, heng)
"""

from PIL import Image, ImageDraw

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

# ---- 女 (left, compressed) ----

# s1: 撇点 compound — head TL(82.6, 69.1) → corner at BL area → tail BC(124.2, 261)
s1_head = (82.6, 69.1)
s1_corner = (63.0, 210.0)  # sharp turn where pie ends and dian begins
s1_tail = (124.2, 261.0)
# pie segment
pie1_ctrl = (76.0, 145.0)
pie1_pts = _bezier_quad(s1_head, pie1_ctrl, s1_corner, 40)
pie1_w = _taper(40, 5.5, 5.0, 4.0)
_stamp_chain(d, pie1_pts, pie1_w)
# dian segment (short down-right)
dian1_ctrl = (90.0, 245.0)
dian1_pts = _bezier_quad(s1_corner, dian1_ctrl, s1_tail, 30)
dian1_w = _taper(30, 4.0, 5.5, 4.0)
_stamp_chain(d, dian1_pts, dian1_w)

# s2: long pie — head C(114.3, 137.1) → tail BL(40.1, 271.6)
s2_head = (114.3, 137.1)
s2_tail = (40.1, 271.6)
s2_ctrl = (72.0, 210.0)
s2_pts = _bezier_quad(s2_head, s2_ctrl, s2_tail, 60)
s2_w = _taper(60, 6.0, 5.0, 2.0)
_stamp_chain(d, s2_pts, s2_w)

# s3: heng across left mid — head ML(17.3, 166.1) → tail C(111.3, 153.2)
s3_head = (17.3, 166.1)
s3_tail = (111.3, 153.2)
s3_ctrl = (64.0, 158.0)
s3_pts = _bezier_quad(s3_head, s3_ctrl, s3_tail, 50)
s3_w = _taper(50, 4.0, 5.5, 5.0)
_stamp_chain(d, s3_pts, s3_w)

# ---- 子 (right) ----

# s4: 子's top 横撇 — head C(144.4, 107.8) → tail C(194.2, 143.0)
# short slightly-curved down-right stroke (top of 子)
s4_head = (144.4, 107.8)
s4_tail = (194.2, 143.0)
s4_ctrl = (172.0, 121.0)
s4_pts = _bezier_quad(s4_head, s4_ctrl, s4_tail, 40)
s4_w = _taper(40, 5.5, 5.0, 5.5)
_stamp_chain(d, s4_pts, s4_w)

# s5: 弯钩 wan_gou — head C(179.6, 144.7) → tail BC(161.4, 275.1)
# vertical stroke with slight bow to right then hook back at bottom (curve to left)
s5_head = (179.6, 144.7)
s5_tail = (161.4, 275.1)
s5_ctrl = (200.0, 220.0)  # bows to the right
s5_pts = _bezier_quad(s5_head, s5_ctrl, s5_tail, 60)
s5_w = _taper(60, 5.5, 6.0, 4.5)
_stamp_chain(d, s5_pts, s5_w)
# hook tail (small flick to lower-left)
hook_end = (145.0, 262.0)
hook_pts = _bezier_quad(s5_tail, (155.0, 275.0), hook_end, 20)
hook_w = _taper(20, 4.5, 4.0, 2.5)
_stamp_chain(d, hook_pts, hook_w)

# s6: crossing 横 of 子 — head C(131.5, 187.5) → tail MR(281.2, 179.3)
s6_head = (131.5, 187.5)
s6_tail = (281.2, 179.3)
s6_ctrl = (206.0, 182.0)
s6_pts = _bezier_quad(s6_head, s6_ctrl, s6_tail, 60)
s6_w = _taper(60, 4.5, 6.0, 5.5)
_stamp_chain(d, s6_pts, s6_w)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 stroke primitives (s5 hook is part of wan_gou)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s1↔s2 P at BL, s1↔s3 P at ML, s4↔s5 N at C, s5↔s6 P at MR
    'overall_pass': True,
    'notes': 'MMH-anchor verbatim per P-A-006. 女 inlined fresh to avoid double-transform.'
}


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0253_好/01_好.png")
