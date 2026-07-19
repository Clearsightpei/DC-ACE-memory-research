"""G1 render for p2_radical_092_厄. PIL, 300x300, black ink on white."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 5  # base stroke thickness


def line(p0, p1, w=TH):
    d.line([p0, p1], fill=INK, width=w)


def polyline(pts, w=TH):
    d.line(pts, fill=INK, width=w, joint="curve")


# --- 厂 (outer): stroke 1 = top horizontal, stroke 2 = left-falling 撇 ---
# Stroke 1: top horizontal, spans most of the character width
polyline([(70, 90), (230, 96)], w=5)

# Stroke 2: 撇 — left-falling curve from top-left corner down to lower-left
polyline([
    (72, 92),
    (68, 130),
    (60, 175),
    (50, 220),
    (42, 258),
], w=6)

# --- 㔾 (inner, 2 strokes) — sits in the upper-right, compact ---
# Stroke 3: 横折 — short horizontal then turns down (forms top and right of inner)
polyline([
    (120, 130),
    (195, 128),
    (198, 160),
    (196, 195),
], w=5)

# Stroke 4: 竖弯钩 — left vertical, curving right along bottom, small hook up
polyline([
    (125, 160),
    (125, 200),
    (135, 220),
    (170, 226),
    (200, 222),
], w=5)
# small hook at the end (up-right tick)
polyline([(200, 222), (205, 212)], w=5)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_厄.png")
img.save(out_path)
print(f"wrote {out_path} size={img.size}")
