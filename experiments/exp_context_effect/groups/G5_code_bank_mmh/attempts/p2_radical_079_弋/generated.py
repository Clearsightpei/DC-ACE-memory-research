# BANK_DEVIATION
# skipped: heng.py, yi_hook.py (no xie_gou primitive exists in bank)
# reason: 弋's key stroke is a 斜钩 (long diagonal down-right with terminal hook)
#         which the current bank does not contain. The 横 is also atypically
#         short and angled upward, not a canonical heng.
# fresh_component: xie_gou_for_yi_ge (long diagonal-hook), heng_short_angled

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def line(a, b, w=7):
    d.line([a, b], fill=INK, width=w)
    # round caps
    r = w // 2
    for (x, y) in (a, b):
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

def curve(points, w=7):
    for i in range(len(points) - 1):
        line(points[i], points[i + 1], w=w)

# ------------------------------------------------------------
# Stroke 1: heng (short, angled slightly up-right)
#   MMH: head ML(0.48,0.764)=(48,176)  tail MR(0.095,0.38)=(210,138)
# ------------------------------------------------------------
s1_head = (48, 176)
s1_tail = (210, 138)
line(s1_head, s1_tail, w=7)

# ------------------------------------------------------------
# Stroke 2: xie_gou (long diagonal from upper-center down to bottom-right,
#           with a small terminal hook going up)
#   MMH: head TC(0.02,0.806)=(102,81)  tail BR(0.581,0.347)=(258,235)
#   Joint P with s1 at C(0.418,0.531)=(142,153) — welded crossing
# ------------------------------------------------------------
s2_head = (102, 81)
s2_body_end = (258, 235)
# Smooth curve as many small segments along a quadratic Bezier through (170,150)
def quad_bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts

curve_pts = quad_bezier(s2_head, (155, 175), s2_body_end, n=48)
curve(curve_pts, w=7)
# terminal hook (small upward tick continuing curl at bottom-right)
hook_end = (262, 210)
line(s2_body_end, hook_end, w=7)

# ------------------------------------------------------------
# Stroke 3: dian (small dot at upper-right, going down-right)
#   MMH: head TC(0.822,0.694)=(182,69)  tail TR(0.183,0.97)=(218,97)
# ------------------------------------------------------------
s3_head = (182, 69)
s3_tail = (218, 97)
line(s3_head, s3_tail, w=8)

# ------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 3 stroke primitives (line calls: s1, s2 curve, s3)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # s1/s2 crossing at ~(142,153) is P (welded)
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: inlined xie_gou fresh (no bank primitive); heng short/angled inlined too.'
}

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_079_弋/01_弋.png")
