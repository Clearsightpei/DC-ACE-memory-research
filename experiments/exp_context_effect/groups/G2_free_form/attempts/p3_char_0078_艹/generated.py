"""
p3_char_0078_艹 — grass radical (cao zi tou)
Structure: one long horizontal spanning the width, crossed by two
short verticals that slant slightly (left vertical tilts a bit right at
top, right vertical tilts a bit right at top, both hanging below the bar).

Simple 3-stroke composition. Drawing with PIL brush-dabs for a hand-
inked feel per drawer_memory technique notes.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def brush_line(p0, p1, width=10, steps=None):
    """Anti-aliased tapered ink line using overlapping ellipses."""
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    dist = (dx * dx + dy * dy) ** 0.5
    if steps is None:
        steps = max(int(dist) * 2, 2)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        # slight taper at the ends
        edge = min(t, 1 - t) * 2  # 0..1..0
        w = width * (0.65 + 0.35 * edge)
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- Stroke 1: the long horizontal bar ---
# Runs roughly across the middle band, slightly rising to the right
# (typical calligraphic 横 with a slight up-tilt).
brush_line((45, 155), (255, 148), width=10)

# --- Stroke 2: left short vertical (crosses the bar) ---
# Slight slant: top a touch to the right of the bottom (i.e. leaning left
# as it descends). Passes through the bar.
brush_line((105, 120), (95, 200), width=10)

# --- Stroke 3: right short vertical (crosses the bar) ---
# Slight mirror slant: top a bit right of bottom too — looking at the GT
# both hang down-left slightly.
brush_line((195, 120), (185, 200), width=10)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0078_艹/01_艹.png"
)
print("saved")
