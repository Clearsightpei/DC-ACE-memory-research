"""
Render 看 (kan4, "to look") at 300x300, black ink on white.

Structural read from GT:
  Top: 龵 (top-form of 手) = long 撇 sweeping from upper-right to
       lower-left, plus three short horizontals stacked at top-right.
  Bottom-right: 目 (5 strokes) — 竖, 横折, and 3 internal/bottom 横.

Recipe (per memory_index TIER-0 F, calligraphic-weight 4-move):
  - Teardrop taper on 撇 (thick→thin)
  - Shoulder dab at 折 joint of 目
  - Bezier for the curved 撇 sweep
  - No hooks in this glyph (龵 top loses 手's 亅)
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


def shoulder_dab(cx, cy, r=5.5):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# --- 1. Long 撇 sweeping from upper-right to lower-left ---
pie = bez((200, 35), (175, 95), (120, 180), (35, 280), n=100)
stroke(pie, (11, 4))

# --- 2. Top short 横 (uppermost bar of 龵) ---
h1 = bez((155, 55), (200, 53), (245, 53), (280, 58), n=40)
stroke(h1, (5, 5))

# --- 3. Middle long 横 (main crossbar spanning almost full width) ---
h2 = bez((60, 108), (130, 105), (210, 105), (285, 112), n=50)
stroke(h2, (6, 6))

# --- 4. Third short 横 (of 龵) ---
h3 = bez((115, 158), (155, 156), (200, 156), (240, 160), n=40)
stroke(h3, (5, 5))

# --- 目 (bottom-right box, 5 strokes) ---
# 目 occupies roughly x=[130, 265], y=[190, 285]
x0, x1 = 130, 265
y0, y1 = 190, 285

# 5. 竖 (left vertical of 目)
v_left = bez((x0, y0), (x0, y0 + 30), (x0, y0 + 65), (x0, y1), n=50)
stroke(v_left, (7, 7))

# 6. 横折 (top horizontal + right vertical, one stroke with shoulder)
top = bez((x0, y0), (x0 + 45, y0 - 1), (x1 - 45, y0 - 1), (x1, y0), n=40)
stroke(top, (5, 5))
shoulder_dab(x1, y0, r=4.5)
right = bez((x1, y0), (x1, y0 + 30), (x1, y0 + 65), (x1, y1), n=50)
stroke(right, (5, 5))

# 7. First internal 横
h_in1 = bez((x0 + 3, y0 + 32), (x0 + 45, y0 + 32),
            (x1 - 45, y0 + 32), (x1 - 3, y0 + 32), n=40)
stroke(h_in1, (4, 4))

# 8. Second internal 横
h_in2 = bez((x0 + 3, y0 + 64), (x0 + 45, y0 + 64),
            (x1 - 45, y0 + 64), (x1 - 3, y0 + 64), n=40)
stroke(h_in2, (4, 4))

# 9. Bottom 横 of 目
h_bot = bez((x0, y1), (x0 + 45, y1), (x1 - 45, y1), (x1, y1), n=40)
stroke(h_bot, (5, 5))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0435_看/01_看.png")
