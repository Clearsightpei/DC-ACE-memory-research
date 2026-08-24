"""G1 render of 和 (hé) — 8 strokes.
Left component 禾 (grain, 5 strokes): 撇 top + 横 + 竖 + 撇 + 捺.
Right component 口 (mouth, 3 strokes): 竖 + 横折 + 横.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=BLACK, width=w)

def curve(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# ---- Left: 禾 (occupies roughly x=35..165, y=55..265) ----

# Stroke 1 (禾-1): short 撇 on top — slanting from upper-right to lower-left
curve([(115, 55), (100, 70), (85, 85)], w=LW)

# Stroke 2 (禾-2): 横 (horizontal), slight upward tilt
line((55, 100), (160, 92))

# Stroke 3 (禾-3): 竖 (vertical) — long central stem
line((108, 100), (108, 265))

# Stroke 4 (禾-4): 撇 (left-falling) from the horizontal down through vertical toward lower-left
curve([(105, 108), (80, 165), (40, 230)], w=LW)

# Stroke 5 (禾-5): 捺 (right-falling) from the horizontal down toward lower-right
curve([(112, 108), (140, 165), (170, 230)], w=LW)

# ---- Right: 口 (occupies roughly x=200..270, y=135..225) ----

# Stroke 6 (口-1): left 竖 (vertical)
line((200, 135), (200, 225))

# Stroke 7 (口-2): 横折 — top horizontal turning down into right vertical
curve([(200, 135), (270, 135), (270, 225)], w=LW)

# Stroke 8 (口-3): bottom 横 (horizontal) closing the box
line((200, 225), (270, 225))

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0365_和/01_和.png"
img.save(out)
print("saved", out)
