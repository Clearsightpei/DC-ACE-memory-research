from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
T = 5

def line(pts, w=T):
    d.line(pts, fill=INK, width=w, joint="curve")

# 也 — 3 strokes matching GT layout:
# GT shows:
#  - a long slanted stroke from upper-right down to lower-left (the 横折钩's long body)
#  - a short vertical near center-top (the 竖)
#  - a big U/cup shape: right vertical, bottom curve, left hook up (the 竖弯钩)
#  - a small inner curve on the right side (part of the 竖弯钩's turn area / a small stroke)

# Stroke 1: 横折 — very short top horizontal then long slanted down-left with a tiny hook up
# Start: (200, 65) → tiny right (215, 70) → down-left slash to (35, 210), hook up (48, 200)
line([(200, 65), (215, 72), (35, 205)], w=T)
line([(35, 205), (50, 195)], w=T)  # small hook

# Stroke 2: 竖 — center short vertical from ~top down to middle
line([(140, 55), (140, 155)], w=T)

# Stroke 3: 竖弯钩 — right vertical starting high-right, down, curving left along bottom, hook up at left end
# Right vertical from (220, 95) down to (225, 235), then bottom curve to (110, 250), hook up (110, 225)
line([(222, 95), (225, 235), (215, 250), (110, 252)], w=T)
line([(110, 252), (110, 225)], w=T)  # hook up at left end

# Small inner curve visible in GT (right-center): a tiny 撇 or curve
line([(180, 155), (172, 185), (188, 200)], w=T)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_也.png"))
print("Saved 01_也.png")
