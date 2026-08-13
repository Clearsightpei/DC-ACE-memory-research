"""G1 render of 里 (character p3_char_0299)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 7

def line(p1, p2, w=W):
    d.line([p1, p2], fill="black", width=w)

# 里 = 日 (top rectangle w/ one middle bar) + vertical continuing down + short 横 + long 横
# Central vertical is CONTINUOUS from top to just above the bottom horizontal.

# Box: x 95..205, y 60..170
BX0, BX1, BY0, BY1 = 95, 205, 60, 170
CX = 150

# 1. Top of box (横 across the top; also serves as the "横折" start)
line((BX0, BY0 + 2), (BX1, BY0))

# 2. Right side of box (from top-right corner down): part of 横折
line((BX1, BY0), (BX1 + 2, BY1))

# 3. Left side of box
line((BX0, BY0 + 2), (BX0 - 2, BY1))

# 4. Middle horizontal inside box (the bar of 日)
mid_y = (BY0 + BY1) // 2 + 2
line((BX0 + 2, mid_y), (BX1 - 2, mid_y))

# 5. Bottom of box
line((BX0 - 2, BY1), (BX1 + 2, BY1))

# 6. Central vertical: continuous from just above box down into 土 region
line((CX, 50), (CX, 235))

# 7. Short horizontal (middle bar of 土 part): between box-bottom and base
line((115, 210), (200, 210))

# 8. Long bottom horizontal (base — 土's base, extends wider)
line((55, 250), (255, 248), w=W + 1)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_里.png"))
print("saved", os.path.join(out_dir, "01_里.png"))
