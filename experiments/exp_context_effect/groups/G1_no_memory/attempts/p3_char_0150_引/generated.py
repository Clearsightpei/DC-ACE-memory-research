"""Render 引 (yǐn) — 弓 (3 strokes) + 丨 (1 stroke) = 4 strokes total."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# 弓 on the left (occupies roughly x=55..160, y=75..250)
# Stroke 1: 横折 — top: short horizontal then a short down-tick
d.line([(70, 95), (155, 90)], fill=INK, width=LW)         # top horizontal
d.line([(155, 90), (150, 115)], fill=INK, width=LW)       # short down turn

# Stroke 2: 横折 — middle: horizontal (slightly shorter) then a short down-tick
d.line([(75, 130), (150, 128)], fill=INK, width=LW)       # middle horizontal
d.line([(150, 128), (140, 158)], fill=INK, width=LW)      # short down turn

# Stroke 3: 横折折钩 — bottom horizontal, then curve down-left to a hook
d.line([(65, 172), (145, 170)], fill=INK, width=LW)       # bottom horizontal
# down and to the left to form the sweeping bottom of 弓
d.line([(145, 170), (130, 210)], fill=INK, width=LW)      # down-left segment
d.line([(130, 210), (55, 250)], fill=INK, width=LW)       # long sweep to bottom-left
# hook up-right at the end
d.line([(55, 250), (85, 240)], fill=INK, width=LW)        # small hook

# Stroke 4: 丨 vertical on the right (a bit taller than 弓)
d.line([(220, 70), (220, 270)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_引.png")
img.save(out)
print(f"Saved {out}")
