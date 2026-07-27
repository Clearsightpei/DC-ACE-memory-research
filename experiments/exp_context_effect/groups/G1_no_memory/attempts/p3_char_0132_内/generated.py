"""G1 render of 内 (nei) — 4 strokes."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def polyline(pts, width=LW):
    d.line(pts, fill=INK, width=width)

# Center the glyph better. GT frame spans roughly x=60..240, y=60..250.
# Stroke 1: 竖 — left vertical, slight lean
polyline([(70, 70), (66, 250)], width=LW)

# Stroke 2: 横折钩 — top horizontal, right vertical, small hook up-left at bottom
polyline([(70, 70), (232, 78), (238, 250), (222, 238)], width=LW)

# Inner 人 sits inside the frame, roughly centered.
# Stroke 3: 撇 (left-falling) — starts near top-center of interior, curves down-left
polyline([(150, 105), (135, 140), (105, 200), (90, 225)], width=LW)

# Stroke 4: 捺 (right-falling) — starts a bit below the 撇 start, sweeps down-right
polyline([(150, 130), (175, 170), (200, 210), (215, 225)], width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_内.png")
img.save(out_path)
print(f"wrote {out_path}")
