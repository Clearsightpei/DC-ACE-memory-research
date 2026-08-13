"""
Render 疔 (dīng) — sickness radical 疒 (5 strokes) + 丁 (2 strokes) = 7 strokes.
Layout: 疒 forms L-frame at top-left. 丁 sits in the interior — its
horizontal is at mid-upper region and extends widely to the right, its
vertical drops with an UP-and-LEFT hook flick.

Revision notes (v2):
  - Moved 丁's 横 DOWN (~y=140) to match GT.
  - Connected 疒's 撇 to right end of 疒's 横 (no floating).
  - 疒's 横 kept short (top-of-frame only).
  - 丁 vertical extended to ~y=260 with clear UP-and-LEFT hook.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=6):
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        d.line([(x1, y1), (x2, y2)], fill=BLACK, width=width)
    for (x, y) in pts:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# --- 疒 radical (top-left) ---

# 1. 点 (top dot) — small slanted mark at very top
stroke([(115, 52), (128, 70)], width=7)

# 2. 横 (long horizontal — top of the 疒 frame, extends wide to the right)
stroke([(70, 88), (160, 84), (255, 90)], width=6)

# 3. 撇 (long left-descending, from RIGHT END of the 横, curving down-left to bottom)
stroke([(255, 90), (200, 145), (140, 210), (75, 265)], width=7)

# 4. 点 (small dot inside — upper-left interior of 疒)
stroke([(85, 130), (100, 145)], width=6)

# 5. 提 (small rising stroke lower-left interior, going up-right)
stroke([(70, 195), (110, 180)], width=6)

# --- 丁 (interior/right) ---

# 6. 横 (horizontal of 丁 — shorter, inside, at mid region)
stroke([(140, 155), (255, 155)], width=6)

# 7. 竖钩 (vertical drops from right-of-middle of 横, hook flicks UP-and-LEFT)
stroke([(205, 155), (203, 265), (188, 253)], width=7)

img.save("01_疔.png")
print("saved 01_疔.png")
