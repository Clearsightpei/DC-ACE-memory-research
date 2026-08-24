"""
Render 金 (jīn, "gold/metal") at 300x300 PNG, black ink on white.

Structure (8 strokes):
1. 撇 — top-right down to lower-left, forming the left slope of the roof
2. 捺 — top down to lower-right, forming the right slope of the roof
3. 短横 — short horizontal under the roof
4. 左点 — small dot lower-left inside the roof
5. 右点 — small dot lower-right inside the roof
6. 横 — middle horizontal (王-part upper bar)
7. 竖 — vertical center of the 王-part
8. 横 — bottom horizontal, widest (base of the character)

Notes:
- Roof (人) forms a wide triangle covering top ~55% of glyph.
- 王-like body sits inside/under the triangle, base extends past.
- Hooks: none for 金.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=7):
    """Draw a smooth polyline with round joins/caps."""
    draw.line(pts, fill=BLACK, width=width, joint="curve")
    # cap the endpoints as circles for smoother terminals
    for x, y in (pts[0], pts[-1]):
        r = width / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def dot(cx, cy, rx=6, ry=8, angle_pts=None):
    """Small teardrop-ish dot."""
    draw.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=BLACK)


# ---- Roof (人 shape on top) ----
# Apex near top-center — both roof strokes share this exact origin
apex = (150, 45)

# 1. 撇 — from apex down-left to lower-left (long slope)
pie = [
    apex,
    (128, 75),
    (100, 110),
    (72, 145),
    (48, 180),
    (35, 205),
]
stroke(pie, width=7)

# 2. 捺 — from apex down-right, ending with a wider foot
na = [
    apex,
    (178, 80),
    (208, 115),
    (238, 150),
    (262, 185),
    (278, 205),
]
stroke(na, width=8)

# ---- Under-roof horizontal (short bar closing the triangle interior) ----
# 3. 短横 — short horizontal roughly middle-height inside the roof
stroke([(108, 160), (198, 160)], width=6)

# ---- Two small inner strokes (左点 / 右点) — tilted, teardrop-like ----
# 4. 左点 — tilts down-left
draw.polygon(
    [(122, 182), (114, 200), (109, 202), (117, 188)],
    fill=BLACK,
)
# 5. 右点 — tilts down-right
draw.polygon(
    [(188, 182), (196, 200), (201, 202), (193, 188)],
    fill=BLACK,
)

# ---- 王-like body ----
# 6. Middle horizontal (upper bar of 王 part)
stroke([(95, 225), (215, 225)], width=6)

# 7. Central vertical (竖) — passes through both horizontals
stroke([(153, 205), (153, 270)], width=7)

# 8. Bottom horizontal — widest, base of the character
stroke([(50, 272), (260, 272)], width=8)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0395_金/01_金.png"
img.save(out)
print("wrote", out)
