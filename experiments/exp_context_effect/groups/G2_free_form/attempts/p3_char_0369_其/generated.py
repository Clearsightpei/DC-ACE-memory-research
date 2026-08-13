"""Render 其 (qi) — 8 strokes.
Stroke order:
  1. 横 top horizontal (medium width)
  2. 撇 left leg (slightly slanted vertical, gentle out-left curve at bottom)
  3. 竖 right leg (slightly slanted vertical)
  4. 横 inner short horizontal 1
  5. 横 inner short horizontal 2
  6. 横 long bottom horizontal (widest — extends beyond legs)
  7. 撇 bottom-left small foot (curve down-left)
  8. 点 bottom-right dot
Composition note: two vertical legs form a slight A-frame (wider at top? actually
  wider at BOTTOM slightly — GT shows tops slightly wider); bottom horizontal is
  the widest stroke; feet 撇 and 点 hang below bottom horizontal.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def line(pts, width=8):
    d.line(pts, fill="black", width=width, joint="curve")


def stroke_taper(pts, w0=8, w1=8, steps=None):
    # simple polyline (uniform width). tapering approximated by short segments.
    steps = steps or len(pts) - 1
    for i in range(len(pts) - 1):
        t = i / max(1, len(pts) - 2)
        w = int(round(w0 * (1 - t) + w1 * t))
        d.line([pts[i], pts[i + 1]], fill="black", width=w)
        d.ellipse(
            (pts[i][0] - w / 2, pts[i][1] - w / 2, pts[i][0] + w / 2, pts[i][1] + w / 2),
            fill="black",
        )
    # end cap
    px, py = pts[-1]
    d.ellipse((px - w1 / 2, py - w1 / 2, px + w1 / 2, py + w1 / 2), fill="black")


# 1. Top horizontal — extends BEYOND leg tops (GT shows overhang both sides)
stroke_taper([(55, 72), (245, 62)], w0=7, w1=9)

# 2. Left leg — splays outward: starts inside top (x~95), ends outside (x~72)
stroke_taper([(98, 70), (92, 130), (82, 180), (72, 218)], w0=9, w1=8)

# 3. Right leg — splays outward: starts inside top (x~205), ends outside (x~232)
stroke_taper([(205, 68), (213, 130), (222, 180), (232, 218)], w0=9, w1=8)

# 4. Inner horizontal 1 — short, around y=118, x 100..205
stroke_taper([(102, 118), (205, 115)], w0=7, w1=8)

# 5. Inner horizontal 2 — short, around y=163, x 98..208
stroke_taper([(100, 165), (208, 162)], w0=7, w1=8)

# 6. Long bottom horizontal — widest, y ~ 215, x 45..258
stroke_taper([(45, 218), (150, 213), (258, 216)], w0=8, w1=10)

# 7. 撇 bottom-left foot — closer to center, from ~(135, 225) down to (95, 278)
stroke_taper([(135, 225), (120, 245), (108, 262), (95, 280)], w0=9, w1=4)

# 8. 点 bottom-right dot — closer to center, teardrop (185, 232) → (215, 272)
stroke_taper([(185, 232), (198, 250), (215, 272)], w0=6, w1=11)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0369_其/01_其.png"
)
