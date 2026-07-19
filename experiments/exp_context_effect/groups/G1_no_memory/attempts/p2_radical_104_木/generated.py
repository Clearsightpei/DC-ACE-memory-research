"""G1 render for radical 木 (4 strokes)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
STROKE = 6

# Stroke 1: horizontal 一 (heng) — roughly middle, slight upward tilt
# From GT: horizontal crosses at ~y=140, from x≈55 to x≈235
d.line([(55, 145), (235, 138)], fill=INK, width=STROKE)

# Stroke 2: vertical 丨 (shu) — center vertical, slight top overshoot above heng
# From GT: vertical top at ~y=70, bottom at y=280, x≈150
# Top hook / small tail above heng
d.line([(150, 70), (150, 280)], fill=INK, width=STROKE)
# Small upper-right tick (顿笔) at top of vertical — like GT shows a small hook
d.line([(150, 70), (172, 92)], fill=INK, width=STROKE)

# Stroke 3: left-falling 丿 (pie) — curved sweep from crossing down-left
# Approximate curve with polyline
pie_pts = [(148, 142), (135, 170), (115, 200), (90, 230), (60, 265)]
for i in range(len(pie_pts) - 1):
    d.line([pie_pts[i], pie_pts[i + 1]], fill=INK, width=STROKE)

# Stroke 4: right-falling 乀 (na) — curved sweep from crossing down-right
na_pts = [(152, 142), (170, 165), (195, 195), (220, 225), (248, 258)]
for i in range(len(na_pts) - 1):
    d.line([na_pts[i], na_pts[i + 1]], fill=INK, width=STROKE)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_木.png")
img.save(out_path)
print(f"wrote {out_path}")
