"""
G1 no-memory attempt: 横折折折 (heng-zhe-zhe-zhe)
Compound stroke: horizontal, turn down, horizontal, turn down, horizontal.
Appears in characters like 凸, 马 (top portion), build a zig-zag going right/down/right/down/right.
Rendered with PIL to a 300x300 white canvas, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
THICK = 12  # brush thickness in px

# Sequence of joints for 横折折折 (5 segments, 4 turns).
# Coordinate system: PIL (0,0) top-left, y grows DOWN.
# Layout designed to look like the outer contour of 凸's top:
#   start upper-left → right (heng) → down (zhe) → right (heng) → down (zhe) → right (heng)
# We keep the character in a centered box roughly 60..240 in x and 80..220 in y.
points = [
    (60,  90),   # start (top-left of first heng)
    (140, 90),   # end of 1st heng (goes right)
    (140, 140),  # after 1st zhe (goes down)
    (180, 140),  # end of 2nd heng (right)
    (180, 200),  # after 2nd zhe (down)
    (250, 200),  # end of 3rd heng (right)
]

# Draw connected thick line with rounded joints.
def draw_thick_polyline(pts, thickness, color):
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill=color, width=thickness)
    # Round the joints (including endpoints) so the corners look inked, not squared.
    r = thickness // 2
    for (x, y) in pts:
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color)

# Slight 顿笔 (starting/ending press): thicker dots at start and each turn.
draw_thick_polyline(points, THICK, INK)

# Emphasize the horizontal starts a touch (顿笔 at the very start).
sx, sy = points[0]
draw.ellipse([sx - THICK // 2 - 1, sy - THICK // 2 - 1,
              sx + THICK // 2 + 1, sy + THICK // 2 + 1], fill=INK)

# Save.
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_30_横折折折/01_横折折折.png"
img.save(out)
print("Saved:", out, img.size)
