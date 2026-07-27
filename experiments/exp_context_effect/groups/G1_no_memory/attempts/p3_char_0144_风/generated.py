"""Render 风 (wind) as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4  # stroke thickness

def line(pts, width=T):
    d.line(pts, fill=INK, width=width, joint="curve")

# 风 structure: outer 几-like frame + interior 乂
# Outer frame:
# 1) Top horizontal 横 (with slight tilt down-right like GT)
line([(80, 88), (225, 82)], width=T)

# 2) Small 撇 tick coming off top-left going down-left (short)
line([(85, 88), (72, 100)], width=T)

# 3) Left 撇 — long sweeping descent from just below top to bottom-left
line([(88, 100), (75, 170), (55, 240), (45, 275)], width=T)

# 4) Right 横折弯钩 — from top-right, down, curve, hook
# vertical descent
line([(225, 82), (232, 210)], width=T)
# curve to bottom
line([(232, 210), (225, 245), (200, 268)], width=T)
# hook up (钩)
line([(200, 268), (188, 252)], width=T)

# Interior 乂 (two crossing strokes), positioned centered-lower in frame
# 撇 (top-right to bottom-left)
line([(170, 150), (110, 225)], width=T)
# 捺 (top-left to bottom-right) with tail
line([(115, 155), (175, 220), (190, 228)], width=T)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0144_风/01_风.png")
print("saved")
