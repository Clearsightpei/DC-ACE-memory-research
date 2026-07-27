"""办 (bàn) — 4-stroke character.

Composition (from GT):
- Central 力 = 横折钩 (top 横 + shoulder + hooked 竖) + body-crossing 撇.
- Two flanking dots: LEFT is a short 撇 (down-left); RIGHT is a 点 (down-right).

Layout (image coords, 300x300, y grows DOWN):
- 力 sits center. The 横折钩's top 横 spans roughly x=120..205 at y~118.
  The hooked 竖 descends from the right shoulder (x=205,y=118) to
  x~180,y=245, then flicks UP-and-LEFT (~-115°) to the terminal.
- Body-crossing 撇: starts ~x=175,y=90 (visibly ABOVE the top 横),
  ends ~x=95,y=270 (lower-left). Passes through/over the 横.
- LEFT flanking 撇-dot: short down-left flick at ~x=75..40, y=145..195.
- RIGHT 点 dot: short down-right flick at ~x=225..265, y=145..185.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r0, r1, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_bezier(p0, p1, p2, r0, r1, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- Stroke 1: 横折钩 (top 横 + shoulder + hooked 竖 + hook flick) ----
# top 横: x=118..205 at y=118, with a small 顿 press at right shoulder
dab_line((118, 118), (205, 118), r0=3.5, r1=4.5, steps=300)
# shoulder press
draw.ellipse((205 - 6, 118 - 6, 205 + 6, 118 + 6), fill="black")
# hooked 竖 descending with a very slight rightward-then-back curve
dab_bezier((205, 120), (198, 180), (180, 246), r0=4.2, r1=3.5, steps=400)
# hook flick UP-and-LEFT (~-115°), ~24 px
import math
hx, hy = 180, 246
ang = math.radians(-115)  # image coords: -y is up
flick_len = 26
tx = hx + flick_len * math.cos(ang)
ty = hy + flick_len * math.sin(ang)
dab_line((hx, hy), (tx, ty), r0=4.5, r1=1.2, steps=200)

# ---- Stroke 2: body-crossing 撇 through the top 横 ----
# Starts above the 横 at (175, 90) -- visible ABOVE the crossing line.
# Ends lower-left at (95, 270). Gentle rightward bow (control pulled right).
dab_bezier((175, 88), (165, 175), (95, 270), r0=5.5, r1=1.5, steps=500)

# ---- Stroke 3: LEFT flanking 撇 (short down-left flick, closer to body) ----
dab_bezier((95, 168), (78, 195), (58, 222), r0=4.8, r1=1.3, steps=250)

# ---- Stroke 4: RIGHT flanking 点 (down-right teardrop, closer to body) ----
dab_bezier((218, 158), (235, 175), (250, 195), r0=2.0, r1=5.5, steps=250)
# small terminal press for the 捺-like foot
draw.ellipse((250 - 5, 195 - 5, 250 + 5, 195 + 5), fill="black")


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0141_办/01_办.png"
)
print("wrote 01_办.png")
