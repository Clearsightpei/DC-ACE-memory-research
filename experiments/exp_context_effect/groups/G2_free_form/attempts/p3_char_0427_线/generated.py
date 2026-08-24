"""
Render 线 (line/thread) — 8 strokes.
Left: 纟 (silk radical) - 3 strokes stacked, narrow left column.
Right: 戋 - 5 strokes: two short horizontals + long 斜钩 + 撇 + 点.
Revision 2: tighten 纟 top loops, angle horizontals slightly upward,
improve 斜钩 curvature so it reads as identity of 线.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

def bezier(pts, steps=50, width=6):
    p0, p1, p2 = pts
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        d.line([prev, (x, y)], fill="black", width=width)
        prev = (x, y)

# ============ 纟 (silk radical, left column, ~x in [40,120]) ============
# 撇折 #1 (top): small down-left curve, turn right (a compact zig)
bezier([(88, 60), (70, 78), (95, 88)], width=6)
# 撇折 #2 (middle): larger loop below, ending with a rightward tail
bezier([(78, 100), (55, 130), (100, 145)], width=6)
# 提 (rising bottom stroke)
line([(50, 200), (125, 175)], width=7)

# ============ 戋 (right side, ~x in [130,260]) ============
# top horizontal 一 (short, upper)
line([(160, 85), (230, 82)], width=6)

# second horizontal 一 (longer, middle)
line([(140, 140), (245, 133)], width=6)

# 斜钩 (long slanting hook) — from upper-right, sweeps down-left, hook up-left
bezier([(220, 65), (220, 180), (185, 265)], width=7)
# hook flick UP-and-LEFT at end
line([(185, 265), (165, 250)], width=6)

# 撇 — crosses the middle horizontal going down-left
bezier([(200, 145), (170, 205), (125, 255)], width=6)

# 点 — small tick in upper-right, above the 斜钩 start
bezier([(248, 70), (258, 82), (250, 92)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0427_线/01_线.png")
print("saved")
