"""
p3_char_0132_内 — retry 1

# SIGNATURE CHECK (from sibling_signature_checklist, 亾 row):
# 冂 outer frame + 人 INSIDE the enclose (not stacked separately).
# 内 = 冂 (top-left 竖 + top 横折钩) + 人 interior (撇 from top-mid, 捺 from mid).

Prior attempt fail: interior 人 too small/stubby, 撇 didn't reach base.
Fix: make 撇 sweep from just below top-横 down to bottom-left, and
捺 sweep from mid of 撇 out to bottom-right. Fill the interior.
Also ensure top 横折钩's terminal hook flicks UP-and-LEFT (~-110°).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def line(p1, p2, w=7):
    d.line([p1, p2], fill=INK, width=w)

def polyline(pts, w=7):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i+1], w=w)

# ==== 冂 frame ====
# Stroke 1: 竖 (left vertical), slightly leaning inward at top
line((70, 70), (68, 265), w=8)

# Stroke 2: 横折钩 — top horizontal from left-top across to right-top, then
# down as right vertical, terminating with a small up-and-left hook.
# Start at (72, 70), horizontal to (238, 62) (slight rise for calligraphy),
# turn down to (232, 260), then hook up-left.
polyline([(72, 66), (238, 60), (232, 262)], w=8)
# hook flick: from (232, 262) up-and-left ~ 22 px at -115°
import math
ang = math.radians(-115)  # in screen coords: -115° means up-left
hx = 232 + 22 * math.cos(ang)
hy = 262 + 22 * math.sin(ang)
line((232, 262), (hx, hy), w=8)

# ==== 人 interior ====
# Stroke 3: 撇 — starts near top-center (just under the top 横), sweeps down-left
# to bottom-left area of interior.
polyline([(150, 100), (135, 145), (110, 195), (88, 240)], w=8)

# Stroke 4: 捺 — starts near upper part of 撇 (around y=130), sweeps down-right
# with a widening tail.
polyline([(150, 130), (170, 165), (195, 205), (215, 235)], w=7)
# Slight thicker tail at end
line((205, 225), (222, 240), w=10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0132_内__retry_1/01_内.png")
print("saved")
