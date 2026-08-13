"""G1 render for 步 (p3_char_0351)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def line(pts, width=4):
    d.line(pts, fill=BLACK, width=width, joint="curve")


def curve(pts, width=4, steps=60):
    (x0, y0), (cx, cy), (x1, y1) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1
        d.line([prev, (x, y)], fill=BLACK, width=width)
        prev = (x, y)


# --- Top: 止 (upper portion) ---
# 1. Left vertical of 止 (the main center-left vertical)
line([(115, 70), (115, 145)], width=4)
# 2. Small horizontal tick top-right of 止
line([(155, 90), (195, 88)], width=4)
# 3. Short vertical dropping from that tick
line([(192, 88), (192, 145)], width=4)
# 4. Long baseline horizontal of 止 — extends wide (this is the wide horizontal in GT)
line([(55, 148), (240, 138)], width=4)

# --- Bottom: 少-without-dot part ---
# 5. Long 丿 (left-descending curve) — from around the middle-top going down and left,
#    passing through the baseline, sweeping all the way to bottom-left corner
curve([(135, 115), (95, 200), (65, 285)], width=5)
# 6. Right piegou / curve — from the right of the bottom half, curving down-right
curve([(200, 160), (208, 215), (218, 265)], width=4)

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_步.png"))
print("saved 01_步.png")
