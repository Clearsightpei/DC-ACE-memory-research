"""
Render 伲 (yi/ni) to 300x300 PNG.
伲 = 亻 (left, 2 strokes) + 尼 (right, 5 strokes) — 7 strokes total.

# SIGNATURE CHECK (per TIER-0.D compound-component rule):
# 伲 contains 匕 as a sub-component of 尼.
# 匕 row: top stroke is a 撇 (upper-right→lower-left);
#         terminal 竖弯钩 flicks UP-and-LEFT (not down).

Revision notes (pass 2): first pass hid the 匕 inside the 尸 body so
the right half read as 亢. Fix: shorten the middle 横 so it doesn't
form a lid; place the 匕 clearly (短撇 crossing the 竖弯钩 vertical);
raise the 匕 slightly so its hook sits inside the 尸 belly.

Layout (left-right compound, 亻 narrow):
  亻 x 55..135, y 55..258.
  尸 outline: top 横折 (155→232, drop to y=118),
              long 撇 from (158,85) sweeping to (150,255).
  Middle short 横: (158..190, y=140) — only spans the top-left cavity.
  匕 inside 尸's lower cavity:
    短撇 from (215,150) → (185,180) — crosses the 竖弯钩 vertical.
    竖弯钩: down from (208,140), curve at y=225, sweep right to x=260, hook UP-LEFT.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        dx, dy = x1 - x0, y1 - y0
        seg = max(abs(dx), abs(dy))
        steps = max(int(seg) * 2, 8)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = w0 * (1 - t) + w1 * t
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# =========== 亻 (left radical) ===========
pie_L = [
    (128, 58),
    (120, 90),
    (108, 125),
    (92, 160),
    (75, 195),
]
pie_L_w = [5.0, 4.7, 4.2, 3.4, 1.8]
brush_stroke(pie_L, pie_L_w)

shu_L = [
    (116, 115),
    (116, 165),
    (116, 215),
    (116, 258),
]
shu_L_w = [5.0, 5.0, 5.0, 4.5]
brush_stroke(shu_L, shu_L_w)


# =========== 尼 (right side) ===========

# --- 1. 横折 (top of 尸) ---
top_h = [(158, 82), (200, 80), (232, 80)]
top_h_w = [4.5, 4.5, 4.8]
brush_stroke(top_h, top_h_w)
fold = [(232, 80), (232, 100), (232, 120)]
fold_w = [4.8, 4.3, 4.0]
brush_stroke(fold, fold_w)

# --- 2. 横 (middle short horizontal inside 尸, only spans left half) ---
mid_h = [(158, 140), (180, 138), (200, 138)]
mid_h_w = [4.0, 4.0, 4.0]
brush_stroke(mid_h, mid_h_w)

# --- 3. 长撇 (尸's tail sweep) ---
long_pie = [
    (158, 85),
    (152, 118),
    (147, 155),
    (143, 195),
    (145, 230),
    (152, 258),
]
long_pie_w = [4.5, 4.5, 4.3, 4.0, 3.4, 2.2]
brush_stroke(long_pie, long_pie_w)


# --- 4. 匕 短撇 (crosses the 竖弯钩 vertical, upper-right→lower-left) ---
duan_pie = [
    (218, 148),
    (208, 162),
    (195, 175),
    (182, 185),
]
duan_pie_w = [3.8, 3.6, 3.0, 1.8]
brush_stroke(duan_pie, duan_pie_w)

# --- 5. 竖弯钩 ---
# down segment (starts a bit right of the 短撇's crossing)
down_seg = [
    (212, 140),
    (211, 175),
    (211, 210),
    (214, 232),
]
down_w = [4.0, 4.0, 4.0, 4.0]
brush_stroke(down_seg, down_w)
# curve to horizontal
curve_seg = [
    (214, 232),
    (225, 246),
    (245, 251),
    (262, 249),
]
curve_w = [4.0, 4.2, 4.2, 3.8]
brush_stroke(curve_seg, curve_w)
# hook flick UP-and-LEFT
hook = [
    (262, 249),
    (259, 238),
    (254, 228),
]
hook_w = [3.8, 2.8, 1.3]
brush_stroke(hook, hook_w)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0312_伲/01_伲.png"
)
