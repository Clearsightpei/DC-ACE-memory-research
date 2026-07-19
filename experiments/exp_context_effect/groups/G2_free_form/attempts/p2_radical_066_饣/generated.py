"""
饣 (food radical, shortened, 3 strokes) — G2 free-form drawer. REVISED.

GT observation (round 2): the GT is a THIN, delicate, handwritten-style
rendering, not a bold seal-script look. My round-1 render was too thick
and the bottom read as an angular 竖提 shoulder instead of the smooth
弯钩-like curve visible in the GT.

Revised interpretation of the 3 strokes:
  1) 撇 (pie): top diagonal, upper-mid → lower-left, thin taper, gentle bow.
  2) 横钩 (heng gou): small horizontal-with-hook near the top-right,
     hooking down-left. Kept small and thin.
  3) 竖弯钩-ish tail (rendered here as smooth arc + upward flick):
     starts high, drops down, curves smoothly rightward like the KEY
     PRIMITIVE tangent-continuous arc, then flicks up-and-left as a hook.
     (This is the standalone-radical form of the 饣 body-and-tail.)

Renderer: PIL brush-dabs. Thin strokes (r ~ 3–4), sharp taper tips.
Canvas 300x300 white.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        L = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(L * 4))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(P0, P1, P2, r0, r1, steps=260):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ============================================================
# STROKE 1 — 撇 (pie)
# Top starts around (140,70), sweeps down-and-left to (~90,215).
# Gentle rightward bow. Thin.
# ============================================================
P0_1 = (145, 70)
P2_1 = (92, 210)
P1_1 = (128, 118)
dab(P0_1[0], P0_1[1], 4.5)   # subtle 顿 (standalone-scale: keep small)
bezier_taper(P0_1, P1_1, P2_1, r0=3.8, r1=0.9, steps=300)


# ============================================================
# STROKE 2 — 横钩 (short heng gou)
# Sits high near top-center-right. Very short.
# horizontal from (140,92) → (188,86), then small hook down-left.
# ============================================================
H_START = (140, 92)
H_END = (188, 84)
dab(H_START[0], H_START[1], 3.5)
line_taper(H_START[0], H_START[1], H_END[0], H_END[1], r0=3.2, r1=3.2, steps=170)
# small shoulder
dab(H_END[0], H_END[1], 4.2)
# hook flick: down-and-left
HK_END = (H_END[0] - 14, H_END[1] + 16)
line_taper(H_END[0], H_END[1], HK_END[0], HK_END[1], r0=3.5, r1=0.9, steps=100)


# ============================================================
# STROKE 3 — body-tail: 竖-arc-flick (弯钩-like)
# Start high just below/right of 撇 body, drop straight down,
# curve smoothly rightward via the tangent-continuous arc primitive,
# short rightward extension, then hook up-and-left.
# ============================================================
# Straight 竖 segment:
V_START = (150, 100)
V_MID = (150, 210)  # bottom of vertical, before the arc
dab(V_START[0], V_START[1], 3.5)
line_taper(V_START[0], V_START[1], V_MID[0], V_MID[1], r0=3.5, r1=3.5, steps=260)

# Tangent-continuous quarter arc (vertical → rightward horizontal)
# starting at (V_MID) with radius R.
R = 22
x0, y0 = V_MID
steps = 90
last = V_MID
for i in range(steps + 1):
    t = i / steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 3.4)
    last = (x, y)
# arc ends at (x0 + R, y0 + R) = (172, 232). Chain from that.
ARC_END = (x0 + R, y0 + R)

# Short rightward horizontal continuation
CONT_END = (ARC_END[0] + 22, ARC_END[1] - 2)
line_taper(ARC_END[0], ARC_END[1], CONT_END[0], CONT_END[1], r0=3.4, r1=3.6, steps=80)

# Hook flick UP-and-LEFT (~ -115° in image coords: dx<0, dy<0 large)
# Give it length ~30 to read as a swept flick.
flick_len = 30
ang_deg = -115  # from +x axis, image coords (y down); so flick goes up-left
HOOK_END = (CONT_END[0] + flick_len * math.cos(math.radians(ang_deg)),
            CONT_END[1] + flick_len * math.sin(math.radians(ang_deg)))
line_taper(CONT_END[0], CONT_END[1], HOOK_END[0], HOOK_END[1], r0=4.0, r1=0.9, steps=140)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_066_饣/01_饣.png")
print("saved")
