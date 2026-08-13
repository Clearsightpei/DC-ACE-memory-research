"""G1 render of 张 (zhang) at 300x300."""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

def poly(points, w=LW):
    d.line(points, fill=INK, width=w, joint="curve")

# Layout: 弓 on the left (~x 60-125), 长 on the right (~x 135-260)

# ===== Left component: 弓 =====
# stroke 1: top horizontal-fold-hook (top bar going right then down)
poly([(65, 105), (120, 100), (120, 130)], w=LW)
# stroke 2: middle horizontal fold (small bar then down)
poly([(70, 140), (120, 138), (115, 165)], w=LW)
# stroke 3: bottom hook — vertical then curve down-left with hook
poly([(75, 175), (110, 175), (110, 210), (85, 235), (65, 250)], w=LW)

# ===== Right component: 长 =====
# stroke 1: short horizontal-ish top-left stroke (short pie)
poly([(150, 115), (175, 120)], w=LW)
# stroke 2: long slanted vertical / left-falling stroke from upper-left going down
poly([(170, 90), (155, 260)], w=LW)
# stroke 3: horizontal to the right at middle
poly([(155, 175), (255, 165)], w=LW)
# stroke 4: right-falling stroke (na) from top-right down to bottom-right
poly([(215, 100), (225, 140), (250, 175), (275, 245)], w=LW)

out = Path(__file__).parent / "01_张.png"
img.save(out)
print(f"saved {out}")
