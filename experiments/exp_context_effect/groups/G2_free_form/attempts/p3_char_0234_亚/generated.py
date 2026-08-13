"""
亚 (yà) — 6 strokes.
Structure:
  1. 一 top horizontal
  2. 丨 left inner short vertical
  3. 一 middle short horizontal (spans between the two inner verticals)
  4. 丶 short outer tick on left (angling down-right)  --> gives 亚 its ID
  5. 丶 short outer tick on right (angling down-left)
  6. 一 bottom long horizontal (widest stroke)

Bottom stroke widest, top stroke slightly narrower. The two outer
ticks distinguish 亚 from 亘/目/工 lookalikes.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BRUSH = 8


def stroke(pts, width=BRUSH):
    d.line(pts, fill=INK, width=width, joint="curve")
    r = width // 2
    for x, y in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# 1) Top horizontal (long, slight upward tilt on the right)
stroke([(70, 90), (230, 88)])

# 2) Left inner short vertical (slightly slanted like a mild 丿)
stroke([(115, 100), (108, 190)])

# 3) Middle short horizontal spanning between the two inner verticals
stroke([(115, 150), (185, 150)])

# 4) Right inner short vertical (straight down)
stroke([(185, 100), (192, 190)])

# 5) Outer left tick — small slash angling down-right (亚's outer wing)
stroke([(70, 175), (95, 205)])

# 6) Outer right tick — small slash angling down-left (亚's outer wing)
stroke([(230, 175), (205, 205)])

# 7) Bottom horizontal (widest stroke)
stroke([(45, 235), (255, 240)])

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0234_亚/01_亚.png"
)
print("wrote 01_亚.png")
