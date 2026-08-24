"""
王 (wang) — Phase-2 radical, 4 strokes.
Structure: three horizontal 横 stacked, with a central vertical 竖
passing through all three.
Length rule (王): bottom 横 is LONGEST (base). Top 横 is MEDIUM.
Middle 横 is SHORTEST. This is the "王" length signature; getting
the ordering wrong could slide it toward 三 + 丨 or a generic grid.
The 竖 is a through-going axis (form_catalog: 竖 as through-going
axis) — straight, no hook, extending slightly above the top 横 and
slightly below the bottom 横, uniform width, 顿 dab at start.

Silhouette family (radical_position_rules): square-ish, centered,
canvas fill x~65%, y~65%.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_line(p0, p1, width_start, width_end, steps=40):
    """Draw a tapered line by dabbing circles from p0 to p1."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = width_start + (width_end - width_start) * t
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def heng(x_start, x_end, y, w_start=7, w_end=6, tilt=0):
    """Horizontal stroke with tiny up-tilt (calligraphic).
    tilt = pixels the right end rises above the left."""
    p0 = (x_start, y)
    p1 = (x_end, y - tilt)
    # thicker terminal dabs (顿) at both ends
    draw.ellipse((p0[0] - 5, p0[1] - 5, p0[0] + 5, p0[1] + 5), fill=INK)
    brush_line(p0, p1, w_start, w_end, steps=60)
    draw.ellipse((p1[0] - 5, p1[1] - 5, p1[0] + 5, p1[1] + 5), fill=INK)


def shu(x, y_top, y_bot, w_top=8, w_bot=7):
    """Vertical through-axis stroke, uniform width, blunt terminal."""
    # 顿 dab at start (top)
    draw.ellipse((x - 6, y_top - 6, x + 6, y_top + 6), fill=INK)
    brush_line((x, y_top), (x, y_bot), w_top, w_bot, steps=60)
    # blunt terminal at bottom
    draw.ellipse((x - 5, y_bot - 5, x + 5, y_bot + 5), fill=INK)


# --- Layout ---
# Centered square silhouette. Central vertical axis around x=150.
CX = 150

# Y-positions of the three horizontals
Y_TOP = 100
Y_MID = 165
Y_BOT = 230

# Half-widths (from center) for each 横
# BOT longest, TOP medium, MID shortest.
HALF_TOP = 60   # top 横 width ~120
HALF_MID = 40   # middle 横 width ~80 (shortest)
HALF_BOT = 82   # bottom 横 width ~164 (longest, base)

# --- Stroke 1: top 横 ---
heng(CX - HALF_TOP, CX + HALF_TOP, Y_TOP, w_start=7, w_end=6, tilt=3)

# --- Stroke 2: middle 横 (shortest) ---
# Slightly left-shifted in the GT so it sits near the 竖 axis, not
# hugging the exact middle.
heng(CX - HALF_MID + 5, CX + HALF_MID + 5, Y_MID, w_start=6, w_end=5, tilt=2)

# --- Stroke 3: 竖 through-axis ---
# Extends ~10 px above top 横 and ~10 px below bottom 横.
shu(CX - 5, Y_TOP - 8, Y_BOT + 8, w_top=8, w_bot=7)

# --- Stroke 4: bottom 横 (longest — the base) ---
heng(CX - HALF_BOT, CX + HALF_BOT, Y_BOT, w_start=7, w_end=7, tilt=3)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_122_王/01_王.png"
)
print("Wrote 01_王.png")
