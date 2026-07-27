"""
卅 (sà) — thirty. 4 strokes.
Structure: three vertical-ish strokes crossed by one horizontal.
Stroke order (per MMH convention):
  1. Left 撇 — starts upper-left, curves down and slightly left
  2. Horizontal 一 — spans across, crossing all three verticals mid-height
  3. Middle 竖 — straight vertical
  4. Right 竖 — straight vertical
GT observation: left stroke is a 撇 (leans/curves out); middle & right are
straight verticals; horizontal is long and gently rightward-tilted.
Verticals extend well below the horizontal, less above.
Not on sibling-risk list. Fresh derivation.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_line(draw, p0, p1, width=9):
    draw.line([p0, p1], fill=INK, width=width)
    # end dabs for calligraphic feel
    r = width // 2
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def brush_curve(draw, pts, width=9):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=INK, width=width)
    r = width // 2
    x0, y0 = pts[0]
    xN, yN = pts[-1]
    draw.ellipse((x0 - r, y0 - r, x0 + r, y0 + r), fill=INK)
    draw.ellipse((xN - r, yN - r, xN + r, yN + r), fill=INK)


# --- layout (300x300 canvas) ---
# horizontal midline crossing at y ~ 145 (a bit above center)
Y_MID = 150
# verticals: top y ~ 75, bottom y ~ 245
Y_TOP = 78
Y_BOT = 248

# x positions for the three verticals
X_LEFT_TOP = 78
X_LEFT_BOT = 58   # 撇 curves outward
X_MID = 148
X_RIGHT = 220

# Stroke 1: left 撇 — starts at (X_LEFT_TOP, Y_TOP), curves down-left to (X_LEFT_BOT, Y_BOT)
# Simple quadratic-ish sampling
撇_pts = []
for t_i in range(21):
    t = t_i / 20.0
    # ease: mostly straight down early, curves left near bottom
    x = X_LEFT_TOP + (X_LEFT_BOT - X_LEFT_TOP) * (t ** 1.6)
    y = Y_TOP + (Y_BOT - Y_TOP) * t
    撇_pts.append((x, y))
brush_curve(d, 撇_pts, width=9)

# Stroke 2: horizontal — long, spans across; slight upward tilt to right
X_H_LEFT = 40
X_H_RIGHT = 250
brush_line(d, (X_H_LEFT, Y_MID + 4), (X_H_RIGHT, Y_MID - 6), width=9)

# Stroke 3: middle 竖 — straight vertical from top through horizontal to bottom
brush_line(d, (X_MID, Y_TOP + 8), (X_MID, Y_BOT), width=9)

# Stroke 4: right 竖 — straight vertical
brush_line(d, (X_RIGHT, Y_TOP + 8), (X_RIGHT, Y_BOT - 5), width=9)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0147_卅/01_卅.png"
img.save(out)
print("saved", out)
