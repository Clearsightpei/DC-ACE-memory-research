"""Render 来 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
from pathlib import Path

OUT = Path(__file__).parent / "01_来.png"

img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

W = 6  # stroke width

def line(p1, p2, w=W):
    draw.line([p1, p2], fill="black", width=w)

# 来 has 7 strokes:
# 1) top horizontal (一)
# 2) small left slanting stroke (top-left)
# 3) small right slanting stroke (top-right)
# 4) middle horizontal (longer)
# 5) vertical (through center, from top to bottom)
# 6) left falling (撇) from center down-left
# 7) right pressing (捺) from center down-right

# 1) top horizontal
line((80, 90), (215, 85))

# 2) small left slanting stroke (dot-like, down-left from top area)
line((110, 100), (95, 125))

# 3) small right slanting stroke (down-right from top area)
line((175, 100), (200, 125))

# 4) middle horizontal (longest)
line((50, 170), (255, 165))

# 5) central vertical (from top down through middle to bottom)
line((150, 70), (150, 265))

# 6) left falling (撇) from center-ish down to lower-left
line((150, 175), (70, 265))

# 7) right pressing (捺) from center-ish down to lower-right
line((150, 175), (245, 265))

img.save(OUT)
print(f"Saved {OUT}")
