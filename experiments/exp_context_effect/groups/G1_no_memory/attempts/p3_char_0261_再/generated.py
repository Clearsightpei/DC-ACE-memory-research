"""G1 render for 再 (p3_char_0261)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

# 再 — 6 strokes
# 1. Top horizontal (short, slight rise to right)
line(90, 60, 215, 55)

# 2. Long horizontal across middle-upper (the wide 一 crossing)
line(55, 140, 260, 130)

# 3. Left vertical of the inner box (going down from top-h into bottom)
line(105, 62, 100, 250)

# 4. Right vertical (top of inner-right down through, forms right side of 冂-like frame)
line(215, 55, 220, 245)
# small hook at bottom-right? keep straight

# 5. Inner short horizontal (middle bar inside the box, between top-h and long-h... actually
# 再 has: top short 一, then 冂 frame, then two inner horizontals crossed by center vertical.
# Redo more faithfully:

# Clear and redo
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Stroke 1: top short horizontal (upper 一)
d.line([(95, 60), (215, 55)], fill=INK, width=LW)

# Stroke 2: left downward stroke (丿-ish, nearly vertical) from top-left
d.line([(95, 60), (75, 250)], fill=INK, width=LW)

# Stroke 3: long horizontal 一 crossing wide (the big middle bar)
d.line([(40, 155), (270, 148)], fill=INK, width=LW)

# Stroke 4: right vertical of inner frame (from top-right corner down)
d.line([(215, 55), (218, 250)], fill=INK, width=LW)
# small hook
d.line([(218, 250), (205, 258)], fill=INK, width=LW)

# Stroke 5: inner short horizontal (between long-h and bottom), inside frame
d.line([(105, 205), (218, 202)], fill=INK, width=LW)

# Stroke 6: center vertical (from middle-h down through inner-h to bottom)
d.line([(150, 148), (150, 258)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_再.png")
img.save(out)
print(f"wrote {out}")
