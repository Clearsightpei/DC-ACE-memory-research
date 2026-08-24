"""
VISUAL DIFF (retry_4 PNG vs GT PNG for 匕):

1. Prior 撇 is DISCONNECTED and too high/left — it floats above the body as
   its own slash. GT: the 撇 CROSSES the upper vertical of the 竖弯钩,
   entering from upper-left and exiting to upper-right, intersecting the
   vertical shaft at roughly its top third.
2. Prior body is a U/rounded bowl that curls back inward on the right
   (like a "G"). GT: the body is a 竖弯钩 — a straight vertical on the
   LEFT running most of the height, a smooth curve across the BOTTOM,
   then a short VERTICAL RISER on the far right (the hook) that goes
   straight up, not curling inward.
3. Prior body has no clear right-side vertical hook. GT: the right end
   is a distinct upward tick standing tall (~45px), roughly parallel to
   the left vertical.
4. Prior body sits too far right of the 撇; the 撇 does not touch it.
   GT: the 撇 and the vertical share the same x-range at the top.

Fix: draw one continuous polyline for 竖弯钩 (down-curve-up), then
draw the 撇 as a separate short stroke crossing the upper vertical.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 7  # line weight roughly matching GT

# --- Stroke 1: 竖弯钩 (main body) ---
# Left vertical from top-left area, curve across bottom, hook up on right.
# Path points, sampled to approximate GT silhouette.
sh_top     = (100, 80)
sh_bottom  = (100, 210)
# Curve across bottom (bezier-like samples)
curve_pts = [
    (100, 210),
    (105, 232),
    (120, 248),
    (150, 253),
    (185, 253),
    (210, 250),
    (218, 245),
]
# Hook rising on right end
hook_start = (218, 245)
hook_end   = (222, 195)

# Draw the shaft
d.line([sh_top, sh_bottom], fill=INK, width=LW)
# Draw the bottom curve
d.line(curve_pts, fill=INK, width=LW, joint="curve")
# Draw the hook (upward)
d.line([hook_start, hook_end], fill=INK, width=LW)

# --- Stroke 2: 撇 (crossing stroke in upper portion) ---
# Enters from upper-left of the shaft, crosses the vertical near its top,
# exits to upper-right. Slight downward slope overall.
pie_start = (75, 118)
pie_mid   = (120, 118)
pie_end   = (175, 130)
d.line([pie_start, pie_mid, pie_end], fill=INK, width=LW, joint="curve")

# Round the endpoints for calligraphic feel
for p in [sh_top, hook_end, pie_start, pie_end]:
    r = LW // 2
    d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=INK)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_011_匕__retry_5/01_匕.png")
