"""
Render 畦 (qi2) at 300x300, black ink on white.

Composition: 田 (left) + 圭 (right).
  田: compact rectangle with cross inside — 竖(left) + 横折(top-right corner)
      + inner 竖 + inner 横 + bottom 一 closing the box. 5 strokes.
  圭: two 土 stacked (top 土 + bottom 土). Each 土 = 横 + 竖 + 横.
      6 strokes total: 横, 竖, 横, 横, 竖, 横.

TIER-0 checks:
  - No hooks in this character (no 钩 flick concerns).
  - Not a sibling-risk target itself; 土 appears as a component
    (sibling-risk row applies): 土 has short top 横, long bottom 横,
    竖 shorter than the width of bottom 横. Repeat for stacked 土.
  - H rule: components must touch — 田 right edge and 圭 left edge
    should be close (~5-10 px gap, no huge whitespace).
  - Calligraphic 4-move: variable-width strokes, shoulder dabs at
    折 joints, bezier for curved lines.

Layout:
  田 on left, x 30..135, y 95..215 (~40% width).
  圭 on right, x 160..280, spans vertically from y 65..270.
    Top 土 (smaller): y 70..155
    Bottom 土 (larger, wider bottom 横): y 155..265
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts

def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# =========== 田 (left) ===========
# Box bounds: x 30..135, y 95..215
LX, RX, TY, BY = 30, 135, 95, 215
MX = (LX + RX) / 2
MY = (TY + BY) / 2

# Stroke 1: 竖 (left side)
stroke(bez((LX, TY), (LX, TY+40), (LX, TY+80), (LX, BY), n=40), (7, 6))

# Stroke 2: 横折 (top + right side)
stroke(bez((LX, TY), (LX+30, TY-1), (LX+70, TY-1), (RX, TY), n=40), (6, 7))
dab(RX, TY, 5)  # shoulder at top-right corner
stroke(bez((RX, TY), (RX, TY+40), (RX, TY+80), (RX, BY), n=40), (7, 6))

# Stroke 3: inner 竖
stroke(bez((MX, TY), (MX, TY+40), (MX, TY+80), (MX, BY), n=40), (6, 6))

# Stroke 4: inner 横
stroke(bez((LX, MY), (LX+30, MY), (LX+70, MY), (RX, MY), n=40), (5, 6))

# Stroke 5: bottom 一
stroke(bez((LX, BY), (LX+30, BY), (LX+70, BY), (RX, BY), n=40), (6, 7))

# =========== 圭 (right) — two 土 stacked ===========
# Right region x 160..285.
# --- Top 土 ---
# short top 横 at y=75 (clearly shorter than middle 横)
stroke(bez((190, 75), (205, 74), (222, 74), (238, 75), n=40), (6, 7))
# 竖 through top 土 — pokes above the short 横, extends down to middle 横
stroke(bez((214, 62), (214, 95), (214, 128), (214, 152), n=40), (7, 7))
# middle 横 (base of top 土, longer than top 横)
stroke(bez((165, 152), (200, 151), (235, 151), (265, 152), n=40), (6, 7))

# --- Bottom 土 ---
# top 横 of bottom 土 (short; sits at y ~ 195)
stroke(bez((190, 195), (205, 194), (222, 194), (238, 195), n=40), (6, 7))
# 竖 through bottom 土 (continues from middle 横 down to bottom 横)
stroke(bez((214, 155), (214, 190), (214, 225), (214, 258), n=40), (7, 7))
# bottom 一 of 圭 (the longest 横, base of character)
stroke(bez((155, 258), (200, 257), (240, 257), (283, 258), n=40), (6, 8))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0570_畦/01_畦.png")
