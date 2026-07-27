"""G1 render for 刅 (character p3_char_0135) — revised."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

# 刅 has the 刀 radical on the left with an extra 丶 (dot / short stroke) inside,
# and per the GT PNG there's also a nà-like stroke to the right.
# GT placement: character centered vertically, slightly left of center.

# --- Stroke 1: 横折 (top horizontal then turn down) of 刀 ---
# horizontal segment
d.line([(95, 115), (185, 108)], fill=BLACK, width=LW)
# short down-turn (the 折 part)
d.line([(185, 108), (188, 132)], fill=BLACK, width=LW)

# --- Stroke 2: 撇 (long left-curving sweep from top-right down to bottom-left) ---
pts = []
for i in range(40):
    t = i / 39.0
    # start near end of 横折, end lower-left
    x0, y0 = 188, 130
    x1, y1 = 85, 225
    x = x0 * (1 - t) + x1 * t
    y = y0 * (1 - t) + y1 * t
    # gentle bulge to the right (character-standard 撇 shape)
    bulge = 12 * (1 - (2*t - 1)**2)
    x += bulge * 0.4
    pts.append((x, y))
for i in range(len(pts) - 1):
    d.line([pts[i], pts[i+1]], fill=BLACK, width=LW)

# --- Stroke 3: interior short 丶 / 撇 inside the 刀 (the mark that makes 刅) ---
# A short diagonal inside the enclosure
pts3 = []
for i in range(15):
    t = i / 14.0
    x = 135 * (1 - t) + 115 * t
    y = 160 * (1 - t) + 190 * t
    pts3.append((x, y))
for i in range(len(pts3) - 1):
    d.line([pts3[i], pts3[i+1]], fill=BLACK, width=LW)

# --- Stroke 4: right 捺 (nà) — descending stroke to the right ---
pts2 = []
for i in range(30):
    t = i / 29.0
    x = 200 * (1 - t) + 248 * t
    y = 150 * (1 - t) + 220 * t
    # slight downward bulge to give a nà shape
    bulge = 5 * (1 - (2*t - 1)**2)
    y += bulge
    pts2.append((x, y))
for i in range(len(pts2) - 1):
    d.line([pts2[i], pts2[i+1]], fill=BLACK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_刅.png")
img.save(out_path)
print(f"Saved {out_path}")
