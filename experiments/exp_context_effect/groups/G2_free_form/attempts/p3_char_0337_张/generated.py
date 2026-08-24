"""
张 = 弓 (left, compressed) + 长 (right). 7 strokes.
Revision 1: fix 长 topology — vertical extends up above 横, short 撇
crosses at top; 捺 starts from near crossing and sweeps to bottom-right.
Fix 弓 bottom hook to flick UP-LEFT (per TIER-0 B).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

def bezier(p0, p1, p2, steps=40, width=6):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    line(pts, width=width)

# ==== 弓 (left, compressed) ====
# Stroke 1: 横折 (top)
line([(50, 90), (115, 88), (113, 130)], width=6)
# Stroke 2: 横 (middle)
line([(55, 128), (110, 130)], width=6)
# Stroke 3: 竖折折钩 — from top-right going down, jog, then bottom horizontal,
# then hook flick UP-LEFT into interior
line([(110, 130), (110, 170), (55, 170), (55, 215), (110, 213)], width=6)
# hook flick UP-LEFT
line([(110, 213), (85, 195)], width=6)

# ==== 长 (right) ====
# Stroke 1: short 撇 at top-left of component (small diagonal)
bezier((170, 85), (162, 100), (145, 120), width=6)

# Stroke 2: 横 - horizontal crossing (through middle-upper)
line([(155, 130), (250, 130)], width=6)

# Stroke 3: 竖提 - vertical starting above 横, going down, then flick up-right
line([(195, 95), (195, 220)], width=6)
# 提 flick up-right
line([(195, 220), (235, 205)], width=6)

# Stroke 4: 捺 - long sweeping diagonal from near crossing down to lower-right
bezier((200, 135), (240, 190), (285, 240), width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0337_张/01_张.png")
print("saved")
