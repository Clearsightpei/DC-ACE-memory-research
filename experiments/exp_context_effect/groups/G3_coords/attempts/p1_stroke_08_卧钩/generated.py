# p1_stroke_08_卧钩 — G3 coord-bank Drawer attempt
# 卧钩 (wo-gou, "lying hook"): a shallow lying curve that dips down and
# right, then flicks up-left as a hook. Found in 心, 必, 志, 忘, 忙.
#
# Shape recipe (all coordinates in a 300x300 canvas, origin top-left,
# turtle math-coords with y grows UP, screen center = (0,0)):
#   - Start upper-left around (-70, +5)
#   - Sweep in a shallow downward arc to the lower-right (+70, -35)
#   - At the right end, thicken (顿笔) then flick a short hook up-left
#     ending near (+55, -5)
#   - Ink is black, canvas is white, size 300x300.

from PIL import Image, ImageDraw

W, H = 300, 300
cx, cy = W / 2, H / 2  # screen center in image coords

def M(x, y):
    """math-coord (x,y) -> image-coord (px,py). y grows UP in math coords."""
    return (cx + x, cy - y)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# --- Main lying-hook body: a shallow downward arc traced left -> right
# Sample points along the arc, math-coords. Thickness swells then tapers.
arc_pts = [
    (-72,  10),   # start (light entry, top-left)
    (-55,   0),
    (-35,  -8),
    (-15, -18),
    (  5, -26),
    ( 25, -32),
    ( 45, -36),
    ( 60, -37),   # bottom-most, just before the hook base
    ( 68, -35),   # 顿笔 (pause / thickening at the hook base)
]

# Draw the body as a chain of thickening line segments.
# Start thin, swell in the middle-right, then thickest at the 顿笔.
widths_body = [3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in range(len(arc_pts) - 1):
    p1 = M(*arc_pts[i])
    p2 = M(*arc_pts[i + 1])
    w = widths_body[i]
    d.line([p1, p2], fill="black", width=w)
    # smooth joints with a filled circle
    d.ellipse([p2[0] - w/2, p2[1] - w/2, p2[0] + w/2, p2[1] + w/2], fill="black")

# --- Hook flick: from the 顿笔 point up-and-left, tapering
hook_pts = [
    ( 68, -35),   # base of hook (thick)
    ( 62, -22),   # rising up-left
    ( 55, -10),   # tip of hook (tapered)
]
widths_hook = [10, 7, 3]
for i in range(len(hook_pts) - 1):
    p1 = M(*hook_pts[i])
    p2 = M(*hook_pts[i + 1])
    w = widths_hook[i]
    d.line([p1, p2], fill="black", width=w)
    d.ellipse([p2[0] - w/2, p2[1] - w/2, p2[0] + w/2, p2[1] + w/2], fill="black")

# Soft round cap at the start (light entry)
sx, sy = M(*arc_pts[0])
d.ellipse([sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5], fill="black")

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_08_卧钩/01_卧钩.png"
img.save(out)
print("saved:", out, img.size)
