from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=BLACK, width=w)

# 所 = 户 (left) + 斤 (right)

# ---- LEFT: 户 ----
# stroke 1: top dot / short slant of 户
curve([(75, 50), (95, 55), (105, 65)])

# stroke 2: 横折 — top horizontal that bends down
curve([(50, 85), (115, 80), (118, 100)])

# stroke 3: middle horizontal of 户 (short, on the left column area)
line((55, 130), (115, 128))

# stroke 4: long 撇 — sweeping down-left from top through middle
curve([(105, 70), (95, 120), (75, 175), (55, 225), (35, 270)])

# ---- RIGHT: 斤 ----
# stroke 1: top-left short 撇 of 斤
curve([(150, 60), (140, 80), (135, 95)])

# stroke 2: top horizontal of 斤 (long)
curve([(145, 100), (210, 95), (250, 98)])

# stroke 3: left short 撇 of 斤 going down-left from upper area
curve([(175, 105), (160, 155), (145, 200)])

# stroke 4: short horizontal in middle of 斤
line((160, 160), (215, 158))

# stroke 5: long vertical of 斤 (rightmost)
line((215, 105), (215, 280))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0371_所/01_所.png")
