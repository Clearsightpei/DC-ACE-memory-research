"""Render 亠 (p3_char_0020) at 300x300.

亠 is a wide-flat, top-heavy 2-stroke radical/character:
  Stroke 1: a small "dot-撇" (点) sitting above and slightly left of center.
  Stroke 2: a long 横 top-lid spanning wide, slight up-tilt, below the dot.

Per form_catalog:
  - 撇 as top-lid: VERY SHORT (~35-50 px), starts ~x=140 y=50 ends ~x=110 y=80
    (but scaled to observed GT position — GT has dot much lower than y=50).
  - 横 as top-lid: MEDIUM (~140-160 px), slight up-tilt (~3°), 顿 dabs.

Adjusted from GT observation: horizontal sits roughly middle of canvas
(y ~ 175), spans widely; the dot sits above it around (150, 130-155).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(draw, pts, widths):
    """Draw a variable-width polyline using dabs (thick→thin taper).

    pts: list of (x, y) sample points along the stroke.
    widths: list of radii, same length as pts.
    """
    # dabs at every point
    for (x, y), w in zip(pts, widths):
        draw.ellipse([x - w, y - w, x + w, y + w], fill=BLACK)
    # segment lines to fill gaps
    for (x1, y1), (x2, y2), w1, w2 in zip(pts[:-1], pts[1:], widths[:-1], widths[1:]):
        wm = max(1, int((w1 + w2) / 2))
        draw.line([(x1, y1), (x2, y2)], fill=BLACK, width=wm * 2)


# ---- Stroke 1: the top 点 (dot-撇) ----
# REVISION: shifted UP ~40 px to match GT composition.
# GT dot sits around (145,92) -> (162,125), thin->thick teardrop
p_start = (146, 90)
p_end = (164, 128)
# sample 6 points along
import math
N = 8
pts = []
widths = []
for i in range(N):
    t = i / (N - 1)
    x = p_start[0] + (p_end[0] - p_start[0]) * t
    y = p_start[1] + (p_end[1] - p_start[1]) * t
    # thin -> thick taper (点 opens downward)
    w = 1.5 + 3.5 * t  # radius from ~1.5 to ~5
    pts.append((x, y))
    widths.append(w)
brush_line(draw, pts, widths)

# ---- Stroke 2: the long 横 top-lid ----
# REVISION: shifted UP ~30 px, thinner, subtler dabs, slight downward bow
# GT: starts ~x=45 y=170 ends ~x=260 y=160 approx (wide, mildly up-tilted)
h_start = (46, 172)
h_end = (258, 158)
# 顿 dab at start (modest)
draw.ellipse([h_start[0] - 5, h_start[1] - 4, h_start[0] + 3, h_start[1] + 5], fill=BLACK)
# main horizontal body — thinner, slight downward mid-bow (calligraphic)
N = 50
hpts = []
hwidths = []
for i in range(N):
    t = i / (N - 1)
    x = h_start[0] + (h_end[0] - h_start[0]) * t
    # add mild downward bow ~3 px at center
    bow = 3.0 * math.sin(math.pi * t)
    y = h_start[1] + (h_end[1] - h_start[1]) * t + bow
    # thinner middle, small dabs at ends
    if t < 0.04 or t > 0.96:
        w = 3.8
    else:
        w = 2.6
    hpts.append((x, y))
    hwidths.append(w)
brush_line(draw, hpts, hwidths)
# 顿 dab at end (slight down-press)
draw.ellipse([h_end[0] - 4, h_end[1] - 3, h_end[0] + 5, h_end[1] + 5], fill=BLACK)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0020_亠/01_亠.png"
img.save(out_path)
print(f"wrote {out_path}")
