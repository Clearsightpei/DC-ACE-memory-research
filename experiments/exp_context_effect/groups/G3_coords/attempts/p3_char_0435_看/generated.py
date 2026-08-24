# BANK_DEVIATION
# skipped: (no primitive for 手-top-form of 看; no 目 primitive in bank)
# reason: 看 = 手 (slanted top form: long pie + 3 stacked hengs) over 目 (rectangular
#         eye with 2 inner hengs). Bank has no 手/目 or close template; inline fresh.
# fresh_component: kan_hand_top (slanted 3-heng + long pie) + kan_mu_bottom (tall 目 lower-right)

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=4):
    d.line([p0, p1], fill="black", width=w)

def tapered(p0, p1, w0=6, w1=3, steps=24):
    x0, y0 = p0; x1, y1 = p1
    for i in range(steps):
        t0 = i / steps; t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0; ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1; yb = y0 + (y1 - y0) * t1
        w = int(round(w0 + (w1 - w0) * (t0 + t1) / 2))
        d.line([(xa, ya), (xb, yb)], fill="black", width=max(1, w))

def curve(pts, w=4):
    # polyline of pts, drawn segment by segment
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=w)

# ---- 手 top (3 hengs + long slanted pie) ----
# Stroke 1: short pie (top-left tiny slash) — very short slanted, upper region
tapered((110, 55), (95, 68), w0=4, w1=3)

# Stroke 2: top heng (long-ish) — slightly slanted up-right
tapered((85, 78), (245, 62), w0=4, w1=5)

# Stroke 3: middle heng — shorter, below top heng
tapered((105, 108), (220, 100), w0=4, w1=5)

# Stroke 4: long pie — starts upper-right, curves down-left to bottom-left
# Use a bezier-like polyline
pie_pts = [
    (200, 55),
    (188, 90),
    (170, 130),
    (145, 175),
    (110, 215),
    (75, 250),
    (55, 275),
]
# taper the pie
for i in range(len(pie_pts) - 1):
    ww = 5 if i < 3 else (4 if i < 5 else 3)
    d.line([pie_pts[i], pie_pts[i + 1]], fill="black", width=ww)

# Stroke 5: long heng (the third heng of 手, longest, extends far right)
# This heng passes through the pie
tapered((90, 148), (285, 138), w0=5, w1=6)

# ---- 目 bottom-right (rectangular eye with inner hengs) ----
# 目 box roughly: x from 150 to 235, y from 165 to 285
X0, X1 = 150, 235
Y0, Y1 = 165, 285

# Stroke 6: 竖 (left vertical of 目)
tapered((X0, Y0), (X0, Y1), w0=5, w1=5)

# Stroke 7: 横折 — top heng + right shu
tapered((X0, Y0), (X1, Y0 + 3), w0=5, w1=5)
tapered((X1, Y0 + 3), (X1 - 3, Y1), w0=5, w1=5)

# Stroke 8: inner heng #1
tapered((X0 + 4, Y0 + 38), (X1 - 6, Y0 + 38), w0=4, w1=4)

# Stroke 9: inner heng #2
tapered((X0 + 4, Y0 + 78), (X1 - 6, Y0 + 78), w0=4, w1=4)

# Stroke 10: bottom heng (closes 目)
tapered((X0, Y1), (X1 - 3, Y1), w0=5, w1=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0435_看/01_看.png")
print("saved")
