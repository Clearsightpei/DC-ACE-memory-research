from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

ink = "black"
stroke = 6

# 卞: 4 strokes — dot (top center-left), horizontal (long), vertical (from mid-horizontal down), dot (bottom right of vertical)

# 1) Top dot: short diagonal stroke going down-left (点)
draw.line([(150, 70), (128, 100)], fill=ink, width=stroke)

# 2) Long horizontal (横) — spans wide
draw.line([(55, 140), (245, 140)], fill=ink, width=stroke)

# 3) Vertical (竖) from horizontal center down
draw.line([(150, 140), (150, 260)], fill=ink, width=stroke)

# 4) Bottom-right dot (点) — diagonal short stroke
draw.line([(170, 180), (200, 215)], fill=ink, width=stroke)

out_path = os.path.join(os.path.dirname(__file__), "01_卞.png")
img.save(out_path)
print(f"Saved {out_path}")
