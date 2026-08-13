"""Render 佟 (tong) — person radical 亻 + 冬 (winter)."""
from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

def curve(pts, width=4, steps=50):
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        d.line([prev, (x, y)], fill="black", width=width)
        prev = (x, y)

# === LEFT: 亻 (person radical) ===
# 撇 (slash): top down to lower-left
curve([(90, 70), (75, 140), (50, 215)], width=5)
# 竖 (vertical): from upper mid, straight down
line([(92, 130), (92, 250)], width=5)

# === RIGHT: 冬 ===
# Top = 夂 (three strokes forming an inverted-V-with-slash)
# Stroke A: 撇 — short slash from upper-mid going down-left
curve([(195, 65), (170, 105), (140, 170)], width=5)
# Stroke B: 横撇 — horizontal into slash starting near stroke A top
line([(195, 75), (245, 75)], width=5)
curve([(245, 75), (235, 110), (200, 175)], width=5)
# Stroke C: 捺 — from mid-upper going down-right (crosses A)
curve([(170, 120), (210, 165), (250, 210)], width=5)

# Bottom of 冬: 冫 two small dots/ticks
# left dot: small slash
line([(170, 220), (180, 240)], width=5)
# right dot: small tick
line([(220, 225), (210, 245)], width=5)

out_dir = Path(__file__).parent
img.save(out_dir / "01_佟.png")
print("saved", out_dir / "01_佟.png")
