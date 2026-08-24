"""
p3_char_0317_员  (member/personnel)

Structure: 口 (top, small) + 贝 (bottom, larger).

# SIGNATURE CHECK (from sibling_signature_checklist.md, applied to 贝 sub-glyph):
#   贝 | 冂 + TWO internal 横 stacked in LOWER 2/3 of box + legs (撇 + 点)
#   NOT 见 (which has ONE 横 + 撇+竖弯钩 legs).
# So the bottom must have: box frame, TWO internal horizontal bars, and 撇+点 legs.

Strokes (7 total):
  口: 1) 竖 (left)  2) 横折 (top+right)  3) 横 (bottom)          -- top small
  贝: 4) 竖 (left)  5) 横折 (top+right)  6) 横 lower inside      -- box
      7) 横 above bottom (2nd inner bar)                          -- (this is the "TWO horizontals")
      8) 撇 (left leg)   9) 点 (right leg)
NOTE: Standard 贝 stroke count is 4 for the box+lines then legs; total 员 = 7 strokes.
Standard MMH decomposition for 贝: 竖, 横折, 横, 横, 撇, 点 = 6 strokes.
So 员 = 3 (口) + 6 (贝) = wait, standard 员 is 7 strokes.
Standard 员 = 口(3) + 贝(4)? Actually 贝 simplified = 4 strokes: 竖, 横折,
撇, 点 with 2 horizontals hidden? No — 贝 simplified is 4 strokes:
  1) 竖 (left of box)
  2) 横折 (top+right of box, ending inside)
  3) — combined horizontal
Actually 员 = 7 strokes: 3 for 口 + 4 for 贝. The two "inner" bars
plus bottom of 贝's box are collapsed. Let's match the GT (which
clearly shows the box with two internal horizontals + 撇+点 legs).
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_line(p0, p1, w0=6, w1=6, steps=None):
    """Line drawn as a series of filled circles ("brush dabs")."""
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(6, int(dist))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = (w0 * (1 - t) + w1 * t) / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def bezier(p0, p1, p2, p3, w0=6, w1=6, steps=80):
    """Cubic Bezier drawn with brush dabs of interpolated width."""
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt**3 * p0[0] + 3 * omt**2 * t * p1[0] + 3 * omt * t**2 * p2[0] + t**3 * p3[0]
        y = omt**3 * p0[1] + 3 * omt**2 * t * p1[1] + 3 * omt * t**2 * p2[1] + t**3 * p3[1]
        r = (w0 * (1 - t) + w1 * t) / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# ---------------- TOP: 口 (small square) ----------------
# Position: top-center. GT shows 口 at ~y=30..95, x=105..190.
kx0, kx1 = 108, 192
ky0, ky1 = 32, 96

# 1. 竖 (left vertical of 口)
brush_line((kx0, ky0 + 2), (kx0, ky1), w0=6, w1=6)
# 2. 横折 (top horizontal + right vertical, one stroke)
brush_line((kx0 - 2, ky0), (kx1, ky0), w0=6, w1=6)  # top horizontal
brush_line((kx1, ky0), (kx1 + 1, ky1 - 2), w0=6, w1=5)  # right vertical (slight inward hook)
# 3. 横 (bottom of 口)
brush_line((kx0 - 1, ky1), (kx1 + 2, ky1 + 1), w0=6, w1=6)


# ---------------- BOTTOM: 贝 (larger box + 2 inner 横 + 撇+点 legs) ----------------
# Box occupies roughly x=70..230, y=110..215
bx0, bx1 = 72, 228
by0, by1 = 110, 215

# 4. 竖 (left of 贝 box)
brush_line((bx0, by0 + 2), (bx0, by1), w0=7, w1=7)

# 5. 横折 (top + right vertical, one continuous)
brush_line((bx0 - 2, by0), (bx1, by0), w0=7, w1=7)  # top horizontal
brush_line((bx1, by0), (bx1 - 1, by1 - 1), w0=7, w1=6)  # right vertical

# 6. inner 横 #1 (upper interior bar) — sits in upper-third of box
in_y1 = by0 + 32
brush_line((bx0 + 6, in_y1), (bx1 - 6, in_y1), w0=5, w1=5)

# 7. inner 横 #2 (lower interior bar) — sits in mid/lower of box
in_y2 = by0 + 68
brush_line((bx0 + 6, in_y2), (bx1 - 6, in_y2), w0=5, w1=5)

# 8. bottom closing horizontal of the 贝 box (bottom of frame)
brush_line((bx0 - 1, by1), (bx1 + 1, by1), w0=6, w1=6)

# 8. 撇 (left leg) — starts near center of box bottom, curves down-left with taper
# Start: (150, 214), end: (72, 288). Curved sweep.
bezier((152, 213), (135, 240), (110, 265), (68, 288), w0=8, w1=3)

# 9. 点 (right leg / 捺 form) — starts near center, sweeps down-right, thickens then tapers
# Start (152, 213) -> end (232, 285) with a slight arc; use a short 捺 shape.
bezier((152, 213), (175, 232), (200, 258), (234, 286), w0=4, w1=8)
# Add a small terminal taper flick at end of 捺
brush_line((234, 286), (242, 282), w0=8, w1=2)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0317_员/01_员.png")
print("wrote 01_员.png")
