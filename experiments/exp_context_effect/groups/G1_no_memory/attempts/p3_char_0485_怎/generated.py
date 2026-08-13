"""G1 render of 怎 (top: 乍, bottom: 心)."""
from PIL import Image, ImageDraw
import os, math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def stroke(points, w=LW):
    d.line(points, fill=BLACK, width=w, joint="curve")

# --- Top: 乍 (about y=35..165) ---
# stroke 1: 撇 - slant left from upper (150, 38) down to (95, 95)
stroke([(150, 38), (135, 55), (118, 75), (100, 95)])

# stroke 2: 横 - top horizontal from (115, 70) to (220, 60), slight upward
stroke([(115, 72), (155, 68), (195, 63), (222, 60)])

# stroke 3: 竖 - short vertical drop from (215, 60) to (215, 100)
stroke([(215, 62), (215, 100)])

# stroke 4: 横 middle - horizontal from (115, 108) to (215, 108)
stroke([(115, 108), (165, 108), (215, 108)])

# stroke 5: 竖 left - vertical from (140, 78) to (140, 165)
stroke([(140, 78), (140, 130), (140, 165)])

# stroke 6: 横 bottom - horizontal from (140, 160) to (225, 158)
stroke([(140, 160), (185, 159), (225, 158)])

# --- Bottom: 心 (about y=185..270) ---
# stroke 1: left dot 点 (short slash going down-right)
stroke([(78, 195), (85, 220), (92, 240)])

# stroke 2: 卧钩 - bowl curve with hook at end
pts = []
for i in range(25):
    t = i / 24.0
    x = 100 + t * 130
    y = 210 + 55 * math.sin(math.pi * t)
    pts.append((x, y))
# hook up at the end
pts.append((232, 215))
pts.append((228, 200))
stroke(pts)

# stroke 3: middle dot (short vertical)
stroke([(158, 210), (162, 232)], w=6)

# stroke 4: right dot (short slash)
stroke([(210, 200), (222, 218)], w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_怎.png"))
print("wrote 01_怎.png")
