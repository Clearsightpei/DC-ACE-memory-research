"""p3_char_0096_为 — revised (rev 1).

4 strokes:
  1. Top short pie: small diagonal near top-center
  2. Inner small pie/dian: short diagonal below the top pie
  3. Long 撇 (pie): big sweeping curve from upper-right down to bottom-left
  4. 横折折折钩 envelope on the right: heng across, drops, small step, drops,
     ends in leftward hook

Uniform thin ~5px lines (MMH GT style).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5


def polyline(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)


# --- Stroke 1: top short pie (upper-center small diagonal) ---
polyline([(120, 55), (100, 100)])

# --- Stroke 2: inner short pie (middle small diagonal, inside the envelope) ---
polyline([(160, 155), (140, 190)])

# --- Stroke 3: long 撇 — big sweeping diagonal from upper-right to bottom-left ---
pie_pts = [
    (195, 55),
    (180, 100),
    (155, 155),
    (115, 220),
    (70, 275),
]
polyline(pie_pts)

# --- Stroke 4: 横折折折钩 right envelope ---
# heng across, then drops to bottom, ending in small leftward hook
env_pts = [
    (85, 145),       # left start (crosses pie)
    (220, 135),      # heng across, slight upward slope
    (230, 275),      # long shu down along right
    (200, 265),      # hook back to left
]
polyline(env_pts)

img.save("01_为.png")
print("saved 01_为.png")
