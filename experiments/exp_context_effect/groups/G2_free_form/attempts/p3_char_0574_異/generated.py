"""異 — top: 田-like box with internal grid; middle: horizontal;
bottom: 共-like base (two verticals + splayed 撇/捺 legs).
Applies calligraphic taper on 撇/捺. Components touch.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, widths):
    if isinstance(widths, (int, float)):
        widths = [widths] * len(pts)
    if len(widths) != len(pts):
        n = len(pts)
        w0, w1 = widths[0], widths[-1]
        widths = [w0 + (w1 - w0) * i / max(1, n - 1) for i in range(n)]
    dense_pts = []
    dense_w = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        steps = max(2, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5 / 2))
        for s in range(steps):
            t = s / steps
            dense_pts.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
            dense_w.append(w0 + (w1 - w0) * t)
    dense_pts.append(pts[-1])
    dense_w.append(widths[-1])
    for (x, y), w in zip(dense_pts, dense_w):
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- TOP: 田 box ---
box_l, box_r, box_t, box_b = 100, 200, 40, 125
# left vertical
stroke([(box_l, box_t), (box_l, box_b)], widths=[6, 6])
# top horizontal
stroke([(box_l - 2, box_t), (box_r + 2, box_t)], widths=[6, 6])
# right vertical
stroke([(box_r, box_t), (box_r, box_b)], widths=[6, 6])
# bottom horizontal
stroke([(box_l - 3, box_b), (box_r + 3, box_b)], widths=[6, 6])
# internal cross
mx = (box_l + box_r) // 2
my = (box_t + box_b) // 2
stroke([(mx, box_t + 3), (mx, box_b - 3)], widths=[5, 5])
stroke([(box_l + 3, my), (box_r - 3, my)], widths=[5, 5])

# --- BOTTOM BODY (共-like): starts immediately under the box ---
# The two verticals extend from just below the top-box down past the middle 一
# Left upright
stroke([(118, 128), (110, 210)], widths=[6, 7])
# Right upright
stroke([(185, 128), (195, 210)], widths=[7, 6])
# Small horizontal cross-bar between uprights (upper bar of 共 base)
stroke([(120, 148), (188, 148)], widths=[5, 5])

# --- LONG MIDDLE HORIZONTAL (the wide 一 spanning the char) ---
stroke([(50, 178), (250, 178)], widths=[7, 7])

# --- BOTTOM LEGS: 撇 (left, thick→thin) and 捺 (right, thin→thick) ---
# Legs anchor from just above the middle horizontal on the uprights
# Left 撇 — starts from left upright base, sweeps out-and-down
stroke([(115, 200), (85, 240), (60, 268)], widths=[7.0, 4.5, 1.8])
# Right 捺 — starts from right upright base, sweeps out-and-down
stroke([(190, 200), (222, 240), (245, 268)], widths=[2.0, 5.0, 7.5])

img.save("01_異.png")
print("wrote 01_異.png")
