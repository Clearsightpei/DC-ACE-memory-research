"""
Render 冖 (mì — 'cover' radical, MMH curriculum p3_char_0028).

Composition (from GT + form_catalog + radical_position_rules):
- Wide-flat family (x ~85%, y ~25%). Top-heavy. Sits in upper canvas.
- Stroke 1: 点 (dian) — small tilted teardrop at the top-left, flicks
  down-right, terminates at the LEFT-START of the lid horizontal.
- Stroke 2: 横折 with a light left-flicking foot (per GT):
  * 横 spans left-right across the upper canvas, VERY slight up-tilt.
  * Shoulder dab at TOP-RIGHT, then a SHORT 竖 descends (short — this
    is a lid radical, not a full box). The 竖 leans slightly inward.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_dab(x, y, r):
    """Small round ink dab, used for 顿 press points."""
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_line(p0, p1, w0, w1, steps=48):
    """
    Straight-line stroke that tapers from width w0 at p0 to w1 at p1.
    Emulated by stamping filled circles along the segment.
    """
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (w0 + (w1 - w0) * t) / 2.0
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---------------------------------------------------------------
# Geometry (all coords in PIL: y grows DOWN)
# ---------------------------------------------------------------
# Lid spans wide-flat: use ~85% x-extent. y sits in upper third.
LID_LEFT_X   = 75
LID_RIGHT_X  = 235
LID_Y_LEFT   = 130     # slight up-tilt to the right
LID_Y_RIGHT  = 118
SHOULDER_DAB_R = 5

# Stroke 1 — 点 sitting ABOVE-LEFT of the lid start as a DISTINCT
# stroke (not merged into the lid). Reads like a short 丿-flick:
# fatter at top-right, thin tapered tip at bottom-left. Small gap
# between its lower tip and where the lid begins.
dot_top    = (LID_LEFT_X + 4,  LID_Y_LEFT - 32)   # top-right (fat)
dot_bottom = (LID_LEFT_X - 14, LID_Y_LEFT + 6)    # bottom-left (thin), just below/left of lid start
taper_line(dot_top, dot_bottom, w0=10, w1=3, steps=32)
brush_dab(*dot_top, r=5)

# Stroke 2a — 横 (top lid), light left end (no heavy 顿 dab so it
# doesn't visually merge with the 点), stronger dab on the right
# corner. Slight up-tilt.
taper_line((LID_LEFT_X, LID_Y_LEFT),
           (LID_RIGHT_X, LID_Y_RIGHT),
           w0=7, w1=8, steps=64)
# shoulder press at top-right corner
brush_dab(LID_RIGHT_X, LID_Y_RIGHT, r=SHOULDER_DAB_R + 1)

# Stroke 2b — SHORT 竖 descending from the shoulder with a small
# leftward flick at the foot (matches GT). Length ~50 px.
FOOT_X = LID_RIGHT_X - 14   # leans inward-left
FOOT_Y = LID_Y_RIGHT + 55
taper_line((LID_RIGHT_X, LID_Y_RIGHT),
           (FOOT_X, FOOT_Y),
           w0=8, w1=5, steps=40)
# small leftward flick terminal (subtle 撇-tip visible in GT)
flick_end = (FOOT_X - 8, FOOT_Y - 4)
taper_line((FOOT_X, FOOT_Y), flick_end, w0=5, w1=2, steps=14)

# ---------------------------------------------------------------
img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0028_冖/01_冖.png"
)
