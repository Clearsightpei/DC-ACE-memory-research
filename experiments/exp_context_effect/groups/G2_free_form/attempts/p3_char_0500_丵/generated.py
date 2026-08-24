"""
p3_char_0500_丵
Structure (from GT):
  - Top: 3 pairs of short slanted flicks (like 業 crown, denser than 丷).
    Left three dots slant \\ then / then \\ (leftmost group).
    Center pair and right group similar — total ~6 short strokes.
  - Horizontal 1: wide 横 spanning most width, just under the flicks.
  - Middle body: a 干/羊-like frame — three shorter horizontals stacked
    with a central 竖 running through them and extending well below.
Applies calligraphic-4 moves: tapered short strokes, shoulder dabs at
horizontal endings, thicker central 竖 with slight taper.
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def stroke(pts, widths):
    """Draw a variable-width stroke by sampling ellipses along polyline."""
    if len(widths) == 2:
        w0, w1 = widths
        widths = [w0 + (w1 - w0) * i / (len(pts) - 1) for i in range(len(pts))]
    # Interpolate finely between successive points
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        r0 = widths[i] / 2
        r1 = widths[i + 1] / 2
        steps = max(2, int(math.hypot(x1 - x0, y1 - y0) / 1.2))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = r0 + (r1 - r0) * t
            dab(x, y, r)


def hline(x1, y, x2, w=6):
    stroke([(x1, y), (x2, y)], (w, w))


def flick(x1, y1, x2, y2, w_start=7, w_end=2):
    stroke([(x1, y1), (x2, y2)], (w_start, w_end))


# --- Top crown: 3 groups of paired flicks (like 業 top, ∧∧∧ pattern) ---
# Each group forms a ∧: left flick starts low-left, ends high (like a 撇),
# right flick starts high, ends low-right (like a 捺/点).
crown_top = 32   # y at top (thin end)
crown_bot = 72   # y at bottom (thick end)

def pair(cx, spread=20):
    # Left half (like 撇): thick at bottom-left, thin at top toward peak
    flick(cx - spread, crown_bot, cx - 3, crown_top, 8, 2)
    # Right half (like 点): thin at top near peak, thick at bottom-right
    flick(cx + 3, crown_top, cx + spread, crown_bot, 2, 8)

pair(70, spread=22)   # left group
pair(150, spread=22)  # middle group
pair(230, spread=22)  # right group

# --- Wide horizontal under crown ---
hline(35, 100, 265, w=7)

# --- Middle body (羊-like frame): 3 horizontals + central 竖 ---
# Central vertical 竖
stroke([(150, 100), (150, 270)], (9, 7))

# Three horizontals across middle & bottom
hline(70, 145, 230, w=6)   # upper mid horizontal
hline(60, 195, 240, w=6)   # long horizontal (widest of the three)
hline(80, 235, 220, w=6)   # bottom horizontal (shorter)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0500_丵/01_丵.png"
img.save(out)
print("saved", out)
