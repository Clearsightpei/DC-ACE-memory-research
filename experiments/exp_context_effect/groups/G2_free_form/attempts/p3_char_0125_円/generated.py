"""
p3_char_0125_円 — Japanese yen character, 4 strokes.

Structure (from GT):
- Left wall: 撇/竖 slightly slanted, descends from upper-left area.
- Top+right: 横折钩 spanning across top then down right wall, with a small
  hook flick at bottom-right.
- Two internal 横 bars stacked (upper divider around 40%, lower base near bottom).

Layout notes (from form_catalog):
- 冂-family: shared corners. Top-lid connects to right vertical at TOP-RIGHT.
- Internal cross-bars span wall-to-wall.

PIL rendering at 300x300.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=8):
    """Draw a polyline with rounded joints via overlapping segments + end caps."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    # circle caps at every vertex to smooth
    r = width // 2
    for (x, y) in pts:
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# Box bounds — 円 has an OPEN bottom (冂 style with legs extending
# past the last internal 横). The two internal 横 sit in the UPPER
# portion; the legs continue well below the lowest horizontal.
LEFT   = 70
RIGHT  = 232
TOP    = 80
LEG_BOTTOM = 270  # where the legs terminate (open bottom)

# --- Stroke 1: left 撇/竖 — starts up-left, slants slightly, descends
# past the bottom internal bar down to LEG_BOTTOM. Slight leftward curve. ---
stroke([(LEFT + 10, TOP - 8),
        (LEFT + 4, TOP + 40),
        (LEFT - 2, TOP + 110),
        (LEFT - 6, TOP + 170),
        (LEFT - 10, LEG_BOTTOM)], width=8)

# --- Stroke 2: 横折钩 — top 横 across, corner at top-right, right 竖
# descends to LEG_BOTTOM, small hook flick left at base. ---
stroke([(LEFT + 6, TOP - 2),
        (LEFT + 70, TOP - 4),
        (LEFT + 140, TOP - 3),
        (RIGHT, TOP + 3),
        (RIGHT + 3, TOP + 60),
        (RIGHT + 2, TOP + 120),
        (RIGHT, TOP + 175),
        (RIGHT - 2, LEG_BOTTOM),
        (RIGHT - 20, LEG_BOTTOM - 8)],  # hook flick up-left
       width=8)

# --- Stroke 3: upper internal 横 (wall-to-wall, in upper third) ---
Y_UP = TOP + 55
stroke([(LEFT + 2, Y_UP),
        (LEFT + 70, Y_UP - 2),
        (RIGHT - 4, Y_UP)], width=8)

# --- Stroke 4: lower internal 横 (wall-to-wall, middle-ish, well ABOVE
# the leg terminus — legs continue past it) ---
Y_LOW = TOP + 120
stroke([(LEFT - 2, Y_LOW + 2),
        (LEFT + 70, Y_LOW),
        (RIGHT - 4, Y_LOW + 2)], width=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0125_円/01_円.png")
print("Saved 01_円.png")
