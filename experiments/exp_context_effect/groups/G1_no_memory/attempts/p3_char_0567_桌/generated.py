"""G1 render of 桌 (table). Structure: 卜 top, 日 middle, 一 divider, 木 bottom."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4  # stroke thickness

def line(x1, y1, x2, y2, w=T):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

# ---------- Top: 卜-like (short heng + shu + small dot) ----------
# short horizontal near top
line(140, 40, 175, 38)
# vertical downward
line(158, 38, 158, 80)
# small right slant (dot)
line(158, 55, 180, 68)

# ---------- Middle: 日 (rectangle with horizontal middle bar) ----------
# left vertical
line(115, 82, 115, 145)
# top horizontal
line(115, 82, 190, 82)
# right vertical (slight inward)
line(190, 82, 188, 145)
# middle horizontal
line(117, 113, 188, 113)
# bottom horizontal
line(115, 145, 188, 145)

# ---------- Divider: 一 (wide horizontal, spans width) ----------
line(50, 175, 250, 175)

# ---------- Bottom: 木 (tree) ----------
# vertical (long, down through)
line(150, 148, 150, 275)
# left sweep (piě) from crossing region
line(150, 195, 70, 275)
# right sweep (nà)
line(150, 195, 235, 275)

out = os.path.join(os.path.dirname(__file__), "01_桌.png")
img.save(out)
print(f"Saved: {out}")
