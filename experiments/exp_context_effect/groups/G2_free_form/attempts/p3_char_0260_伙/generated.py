"""
p3_char_0260_伙 — G2 attempt
伙 = 亻 (left, ~35% width) + 火 (right, ~55% width)
火 = 丶 (left dot) + 丿 (upper-mid short pie) + 撇 (long left pie from top) + 捺 (long right sweep)
Simple brush-dab PIL render.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush(pts, widths):
    """Draw a series of dabs along pts with per-point width."""
    for (x, y), w in zip(pts, widths):
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def stroke(p0, p1, w0, w1, n=60, curve=None):
    """Bezier-ish stroke. curve = control point (cx, cy) or None for straight."""
    pts, ws = [], []
    for i in range(n + 1):
        t = i / n
        if curve is None:
            x = p0[0] + (p1[0] - p0[0]) * t
            y = p0[1] + (p1[1] - p0[1]) * t
        else:
            cx, cy = curve
            x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * cx + t ** 2 * p1[0]
            y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * cy + t ** 2 * p1[1]
        pts.append((x, y))
        ws.append(w0 + (w1 - w0) * t)
    brush(pts, ws)

# ---------- 亻 (person radical, left side) ----------
# 撇 (falling-left pie): from upper-right of radical, sweeps down-left
stroke((110, 70), (60, 210), 10, 6, curve=(95, 140))
# 竖 (long vertical): from where the 撇 meets, straight down
stroke((100, 130), (100, 260), 9, 8)

# ---------- 火 (fire, right side) ----------
# 丶 (left tick of 火 top): a short down-left flick above the body
stroke((175, 85), (160, 120), 5, 9, curve=(165, 105))
# 丿 (right tick of 火 top): a short down-right flick, mirror of 丶
stroke((230, 85), (245, 120), 5, 9, curve=(240, 105))
# 撇 (long left pie of 火 body): starts high-center, sweeps down-left long
stroke((215, 115), (150, 270), 12, 5, curve=(175, 210))
# 横 base of body: a short horizontal crossing at mid where pie meets sweep
# (skip — 火 doesn't have a horizontal; the 撇 and 捺 cross visually)
# 捺 (long right sweep): starts near the pie's upper section, sweeps down-right with flare
stroke((200, 140), (285, 265), 6, 15, curve=(225, 205))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0260_伙/01_伙.png")
