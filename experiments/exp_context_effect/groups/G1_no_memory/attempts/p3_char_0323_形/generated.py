"""Render 形 (xíng) as 300x300 PNG. Left: 开, Right: 彡."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 6

def line(p0, p1, width=TH):
    d.line([p0, p1], fill=INK, width=width)

def curve(points, width=TH):
    # polyline
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=INK, width=width)

# ---------- LEFT: 开 (occupies roughly x=30..165) ----------
# Top horizontal (short, upper): a slight arc
curve([(40, 80), (90, 72), (160, 80)])

# Second horizontal (main, longer, crossing both verticals)
curve([(20, 145), (95, 138), (175, 145)])

# Left vertical (short pie-like slanting down-left from the middle bar)
curve([(60, 90), (55, 145), (40, 240)])

# Right vertical (straight, from top bar down)
line((130, 90), (130, 260))
# little hook or straight ending — keep straight

# ---------- RIGHT: 彡 (three slanted strokes) occupying x=180..280 ----------
# Stroke 1 (top pie): from upper-left going down-right small then curving
curve([(210, 70), (230, 90), (250, 115)])

# Stroke 2 (middle pie): starts lower-left, ends lower-right
curve([(190, 130), (215, 155), (245, 180)])

# Stroke 3 (bottom pie, longest): sweeping
curve([(175, 195), (215, 235), (270, 275)], width=TH)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_形.png")
img.save(out_path)
print(f"wrote {out_path}")
