"""
p3_char_0135_刅 — G2 attempt

刅 = 刀 (horizontal-fold-hook + body-crossing 撇) + two 丶 dots
     (one on the upper-left of 刀, one on the right of 刀).

4 strokes total (per stroke count position in curriculum).

GT observation: 刀 sits center-left. A short 撇-dot on the upper-left of 刀's
opening; a longer 丶 dot on the right side of 刀. Whole glyph slightly
compact / italic-feeling, occupying the middle band.

Uses form_catalog:
- 撇 body-crossing diagonal for the 刀's main 撇
- 横折钩: hook flicks UP-and-LEFT into the body (TIER-0.B)
- Two dots rendered with the PIL brush-dab technique.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(pts, width=8, color=(0, 0, 0)):
    """Polyline with round-cap joints (draw circles at each vertex)."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=color, width=width)
    for p in pts:
        d.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2], fill=color)

def bezier(p0, p1, p2, steps=40):
    return [
        (
            (1-t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0],
            (1-t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1],
        )
        for t in [i/steps for i in range(steps+1)]
    ]

def dab_dot(cx, cy, angle_deg, length=22, thick=10, color=(0,0,0)):
    """A calligraphic 丶 dot: short teardrop that fattens toward its end."""
    a = math.radians(angle_deg)
    # start (thin) -> end (thick). Use 3-stop ellipses along the axis.
    steps = 12
    for i in range(steps+1):
        t = i / steps
        x = cx + t * length * math.cos(a)
        y = cy + t * length * math.sin(a)
        r = thick * (0.35 + 0.65 * t)  # grows from thin to thick
        d.ellipse([x-r/2, y-r/2, x+r/2, y+r/2], fill=color)

# ---------------------------------------------------------------
# Stroke 1: 刀's 横折钩 — top horizontal then fold down with hook
# ---------------------------------------------------------------
# Top horizontal: goes from ~ (110, 110) to (180, 108) — slight upward tilt
brush_line([(112, 112), (140, 110), (172, 108)], width=8)
# Fold-down 竖: from (172, 108) curving down-left to (150, 175)
fold_curve = bezier((172, 108), (178, 140), (152, 178), steps=24)
brush_line([(int(x), int(y)) for x, y in fold_curve], width=8)
# Hook: flicks UP-and-LEFT from (152, 178) — per TIER-0.B: ~-105° to -120°
hook_end_x = 152 + 14 * math.cos(math.radians(-115))
hook_end_y = 178 + 14 * math.sin(math.radians(-115))
brush_line([(152, 178), (int(hook_end_x), int(hook_end_y))], width=7)

# ---------------------------------------------------------------
# Stroke 2: 刀's body-crossing 撇 — LONG, must cross the top 横
# Starts ABOVE the top-横 at ~(150, 90), sweeps down-left to (95, 210)
# ---------------------------------------------------------------
pie_pts = bezier((150, 90), (135, 140), (95, 210), steps=30)
brush_line([(int(x), int(y)) for x, y in pie_pts], width=8)

# ---------------------------------------------------------------
# Stroke 3: left-inside 丶 dot (short 撇-flick INSIDE the 刀 opening)
# GT shows this as a short down-left flick near the middle-left,
# nestled inside the 刀 bowl area.
# ---------------------------------------------------------------
dab_dot(108, 158, angle_deg=215, length=24, thick=10)

# ---------------------------------------------------------------
# Stroke 4: right-side 丶 dot (upper-right of 刀, sweeping down-right)
# GT shows this as a longer flick from about (195, 130) down-right.
# ---------------------------------------------------------------
dab_dot(190, 130, angle_deg=30, length=32, thick=11)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0135_刅/01_刅.png")
print("saved 01_刅.png")
