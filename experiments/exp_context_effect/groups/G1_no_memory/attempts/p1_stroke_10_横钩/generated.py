"""
G1 no-memory attempt: 横钩 (heng gou) — horizontal stroke ending with a small hook down-left.
Renders a 300x300 white PNG with black ink using PIL (turtle-free for reliability).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 横 (horizontal): a mostly-flat stroke going left-to-right, slight rise at the right end.
# Then 钩 (hook): a short tick pointing down-left.
#
# Coordinates in PIL image space (y grows DOWN).
# Start point on the left, end point on the right where the hook begins.
x_start, y_start = 50, 150
x_end,   y_end   = 245, 140   # slight upward tilt to the right, typical of 横

# Main horizontal body — draw as a thick line, then thicken the right end (顿笔) with an ellipse.
body_width = 14
draw.line([(x_start, y_start), (x_end, y_end)], fill="black", width=body_width)

# Left cap: soft round start
r_left = body_width // 2
draw.ellipse([x_start - r_left, y_start - r_left,
              x_start + r_left, y_start + r_left], fill="black")

# Right 顿笔 (pause/press) — a stronger blob just before the hook launches
dun_r = 11
draw.ellipse([x_end - dun_r, y_end - dun_r,
              x_end + dun_r + 4, y_end + dun_r + 4], fill="black")

# 钩 (hook): a short tapered stroke going down-and-left from the 顿笔 point.
# Approximate taper by drawing several progressively thinner lines from the hook root
# toward its sharp tip.
hook_root = (x_end + 2, y_end + 4)
hook_tip  = (x_end - 22, y_end + 34)   # down-left

steps = 10
for i in range(steps):
    t0 = i / steps
    t1 = (i + 1) / steps
    x0 = hook_root[0] + (hook_tip[0] - hook_root[0]) * t0
    y0 = hook_root[1] + (hook_tip[1] - hook_root[1]) * t0
    x1 = hook_root[0] + (hook_tip[0] - hook_root[0]) * t1
    y1 = hook_root[1] + (hook_tip[1] - hook_root[1]) * t1
    w = max(1, int(round(12 * (1 - t1))))
    draw.line([(x0, y0), (x1, y1)], fill="black", width=w)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_10_横钩/01_横钩.png"
img.save(out)
print(f"saved {out}")
