"""
Render 爪 (zhǎo) — 4-画 radical.

Revised (v2) after comparing v1 to GT:
  - GT's left leg has a distinct hook-in-then-curve-out shape at top,
    then arcs down to the lower-left. In v1 the left leg started too
    high and was too straight.
  - GT's right leg (捺) starts near the top junction, not from a
    middle-竖.
  - GT's top has three small marks near center: a small top-left flick
    (撇), a short horizontal reaching right (which is actually the
    starting portion of stroke 2/3), and a short down-stub (竖).

Standard 4 strokes of 爪 (from top-down stroke order):
  1. 撇 short — top-left flick
  2. 撇 long — starts near center-top, arcs briefly right then curves
     down-left to lower-LEFT corner
  3. 竖 — short vertical stub near center (the "middle drop")
  4. 捺 long — sweeps from center-top down-right to lower-right

Canvas 300x300, PIL, white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke_bezier(pts, widths, samples=140):
    """Variable-width brush-dab along a Bezier of arbitrary degree."""
    for i in range(samples + 1):
        t = i / samples
        cps = list(pts)
        while len(cps) > 1:
            cps = [((1 - t) * a[0] + t * b[0], (1 - t) * a[1] + t * b[1])
                   for a, b in zip(cps, cps[1:])]
        x, y = cps[0]
        wt = t * (len(widths) - 1)
        wi = int(wt)
        wf = wt - wi
        if wi >= len(widths) - 1:
            w = widths[-1]
        else:
            w = widths[wi] * (1 - wf) + widths[wi + 1] * wf
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- Stroke 1: short 撇 top-left flick ---
# Small dash starting near (140, 75) flicking down-left to (108, 108).
stroke_bezier(
    [(142, 72), (128, 88), (108, 110)],
    widths=[7, 6, 3],
    samples=50,
)

# --- Stroke 2: long 撇 (left leg) ---
# GT shows this stroke starting near the top center at ~(148, 75),
# going briefly rightward/downward with a small hook-like turn near the
# top (~(160, 82)), then curving down and sweeping to the lower-left.
# End near (100, 275).
stroke_bezier(
    [(148, 74), (162, 82), (155, 100), (135, 160), (115, 220), (100, 278)],
    widths=[8, 8, 9, 9, 8, 5],
    samples=180,
)

# --- Stroke 3: short 竖 (middle stub) ---
# Small vertical near center starting from ~(158, 90) descending to
# ~(160, 145). Visible below the shoulder of stroke 2.
stroke_bezier(
    [(158, 92), (160, 118), (162, 148)],
    widths=[7, 7, 7],
    samples=40,
)

# --- Stroke 4: long 捺 (right leg) ---
# Starts near the top junction ~(158, 82), sweeps rightward and downward
# with progressive thickening, ending broad at ~(255, 240).
stroke_bezier(
    [(158, 82), (185, 120), (215, 165), (255, 238)],
    widths=[5, 8, 11, 14],
    samples=180,
)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_134_爪/01_爪.png")
