"""Render 升 (rise) — 4 strokes.

Structure (from GT observation):
  1. 短撇 (short slash) — small top-left flick above the horizontal
  2. 撇 (long left vertical-into-curve) — starts high on left side,
     drops nearly vertically then curves out to lower-left
  3. 横 (horizontal) — mid-height, crosses full width
  4. 竖 (long vertical) — right side, from just above the horizontal
     down through the bottom

Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def dab_line(pts, width=6):
    """Draw a polyline with rounded joints (brush-dab style)."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=INK, width=width)
    r = width // 2
    for x, y in pts:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# Stroke 1: 短撇 — short flick, top region, goes from upper-right down to lower-left
# Around x=110..85, y=70..110
s1 = [(115, 68), (108, 82), (98, 98), (86, 112)]
dab_line(s1, width=6)

# Stroke 2: 撇 — long left stroke. Starts near top-left (below stroke 1's start),
# drops nearly vertically, then curves out to bottom-left.
# Uses a smooth polyline approximating a J-mirror shape.
s2 = [
    (128, 85),
    (125, 115),
    (122, 145),
    (118, 175),
    (112, 205),
    (100, 230),
    (82, 250),
    (58, 262),
]
dab_line(s2, width=7)

# Stroke 3: 横 — horizontal, mid-height, crossing full width
# Slight upward slope typical of 横
s3 = [(48, 158), (120, 154), (200, 150), (258, 148)]
dab_line(s3, width=7)

# Stroke 4: 竖 — long vertical on the right, from just above the 横 down to bottom
s4 = [(198, 108), (198, 155), (198, 210), (198, 275)]
dab_line(s4, width=7)

img.save("01_升.png")
print("Wrote 01_升.png")
