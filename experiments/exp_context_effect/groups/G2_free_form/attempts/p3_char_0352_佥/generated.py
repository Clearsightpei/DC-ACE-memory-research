"""
Item: p3_char_0352_佥
Character 佥 structure:
  - Top: 人 (large roof: 撇 from top-center diagonal down-left, 捺 top-center down-right)
  - Small dot under the peak (short tick)
  - Middle horizontal 一 (short)
  - Two small strokes below middle (a small 丿 left, a small 丶 right)
  - Bottom long horizontal 一

Render with PIL at 300x300.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, width=6):
    d.line([p0, p1], fill="black", width=width)

def tapered_line(p0, p1, w_start=8, w_end=4, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        wa = w_start + (w_end - w_start) * ((t0 + t1) / 2)
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        d.line([(xa, ya), (xb, yb)], fill="black", width=max(2, int(wa)))

# --- Top: 人 (roof) ---
# Peak near top-center
peak = (150, 55)
# 撇 (left diagonal, thick to thin, sweeps down-left)
tapered_line(peak, (60, 175), w_start=8, w_end=4, steps=30)
# 捺 (right diagonal, thin to thicker sweep)
tapered_line(peak, (245, 170), w_start=5, w_end=8, steps=30)

# small hook/tick just below peak (like a small nose)
d.line([(155, 75), (162, 88)], fill="black", width=4)

# --- Middle: horizontal under the roof, spans between roof lines ---
line((85, 148), (225, 150), width=5)
# small tick on right end of middle horizontal
d.line([(225, 150), (232, 158)], fill="black", width=4)

# --- Below middle: 从-like pair (small 撇+捺 on left, small 撇+捺 on right) ---
# left pair
tapered_line((115, 170), (100, 210), w_start=5, w_end=3, steps=15)  # 丿
tapered_line((115, 175), (128, 210), w_start=3, w_end=5, steps=15)  # 捺
# right pair
tapered_line((175, 170), (162, 210), w_start=5, w_end=3, steps=15)  # 丿
tapered_line((175, 175), (195, 215), w_start=3, w_end=6, steps=15)  # 捺

# --- Bottom: long horizontal 一 ---
line((50, 245), (255, 242), width=6)
# small starting tick on the left of bottom horizontal
d.line([(50, 245), (58, 250)], fill="black", width=5)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0352_佥/01_佥.png"
img.save(out)
print("wrote", out)
