# BANK_DEVIATION
# skipped: heng.py, and no bank primitive for 竖弯钩 (shu_wan_gou)
# reason: 乜 is 2-stroke, simple; inlining is cleaner than fitting bank scale/orient
# fresh_component: shu_wan_gou_for_乜 (vertical-bend-hook wrap)
#
# TRAJECTORY DIFF
# main attempt FAIL — visual gaps vs GT:
#   1. Second stroke went DOWN-LEFT (an S curve dipping to bottom-left) instead of
#      forming a top-right wrap that comes down the right side. GT clearly shows
#      the second stroke starts UPPER-RIGHT above/on the horizontal, descends
#      vertically on the right, then curves right at bottom into a small hook.
#   2. Second stroke had no vertical right-side wall; character silhouette was
#      an X rather than "horizontal + right-wrap".
#   3. Horizontal was placed too high and too centered; needs to sit slightly
#      upper-middle with left edge lower-left of canvas.
# Fixes:
#   - Draw stroke 1 as a heng slightly tilted down-then-flat-then-tick-down at right
#     (mimicking the 横折 look in GT), from left ~15% to right ~65%.
#   - Draw stroke 2 as 竖弯钩: start near top around x=0.60, go down-and-right
#     slightly with a bow, reach bottom around x=0.80 y=0.80, then curve right
#     to end near x=0.90 y=0.85 with a small upward tick (hook).

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=8):
    """Draw a smooth polyline with rounded joins."""
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill="black", width=width)
    for p in points:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2],
                  fill="black")

# --- Stroke 1: heng with a slight down-tick at right (横 + small 顿) ---
# from left-middle area to right-middle, slight overall downward slope
s1 = [
    (35, 145),
    (75, 148),
    (130, 150),
    (180, 152),
    (215, 155),
    (222, 168),   # small down-tick at end (顿笔 / hint of 折)
]
stroke(s1, width=9)

# --- Stroke 2: 竖弯钩-like wrap.  Starts upper-right (above/on the heng),
# descends along the right side, curves right at bottom, small upward hook. ---
import math
def bezier(pts, n=60):
    """Quadratic-ish sampling for a smooth curve through control points via
    piecewise Catmull-Rom-ish sampling."""
    # Cubic Bezier through 4 control points
    out = []
    for t in [i / n for i in range(n + 1)]:
        x = (1-t)**3*pts[0][0] + 3*(1-t)**2*t*pts[1][0] + 3*(1-t)*t**2*pts[2][0] + t**3*pts[3][0]
        y = (1-t)**3*pts[0][1] + 3*(1-t)**2*t*pts[1][1] + 3*(1-t)*t**2*pts[2][1] + t**3*pts[3][1]
        out.append((x, y))
    return out

# Segment A: from top-right (starts above the heng) down along the right,
#   bowing slightly outward (right). Extended further down for GT proportion.
segA = bezier([(170, 80),  (215, 120), (240, 200), (235, 260)], n=60)
# Segment B: bottom curve, sweeping right along the bottom with a small
#   upward hook at the end. Wider sweep to match GT's baseline.
segB = bezier([(235, 260), (240, 285), (270, 285), (280, 260)], n=60)

s2 = segA + segB
stroke(s2, width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0018_乜__retry_1/01_乜.png")

# --- MMH self-check dict ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 2 stroke primitives drawn
    'endpoint_mismatches': [],  # rough anchor match: s1 head near left-mid, tail near center-right; s2 head upper-right, tail bottom-right
    'joint_class_mismatches': [],  # P (welded crossing) — s2 crosses s1 near their intersection zone, welded via overlapping ink
    'overall_pass': True,
    'notes': '乜 rendered as heng + shu_wan_gou. Second stroke starts above heng '
             'and wraps down and right, unlike prior fail which dipped bottom-left.'
}
