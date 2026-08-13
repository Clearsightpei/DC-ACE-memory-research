"""Render 兇 to 01_兇.png at 300x300, white bg, black ink.
Structure:
  Top half: 凶-like frame (乂 crossing inside, two side verticals).
  Bottom half: 儿 (left slash + right vertical-hook), wrapping wide.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)

# --- Top: 乂 (X crossing) ---
# left-falling (丿): upper-right to lower-left
line((175, 55), (95, 165))
# right-falling (乀): upper-left to lower-right
line((115, 65), (200, 175))

# --- Frame side walls (two vertical short strokes flanking the 乂) ---
# left wall
line((85, 105), (95, 180))
# right wall
line((215, 100), (225, 185))

# --- Bottom: 儿 ---
# left stroke 丿: from around top-center of bottom half, sweeping down-left
poly([(120, 155), (100, 200), (70, 250), (50, 280)])
# right stroke 乚 (vertical then hook right at bottom)
poly([(190, 145), (200, 220), (215, 265), (245, 278), (265, 270)])

out = os.path.join(os.path.dirname(__file__), "01_兇.png")
img.save(out)
print("saved", out)
