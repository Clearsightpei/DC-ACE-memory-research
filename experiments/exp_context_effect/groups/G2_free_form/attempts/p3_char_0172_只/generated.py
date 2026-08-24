"""只 (zhǐ) — 5 strokes.
Structure: 口 (top, 3 strokes) + 八 (bottom: 撇 left, 长点/捺 right).
GT observation:
- 口 sits upper-center, slightly wider than tall, ~ mid-upper canvas.
- 八 legs splay wide below, well below the 口 with a small gap.
- Left leg is a 撇 (starts near lower-left of 口, sweeps down-left).
- Right leg is a 长点/捺-like flick from lower-right of 口 down-right.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6  # main stroke width

def line(p0, p1, width=LW):
    d.line([p0, p1], fill=INK, width=width)

def polyline(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# --- 口 (top) ---
# box roughly x: 95..205, y: 70..145
L, R, T, B = 95, 205, 70, 145

# Stroke 1: 竖 (left vertical) — a slight left-lean
polyline([(L+4, T+4), (L, B)], width=LW)

# Stroke 2: 横折 — top horizontal then turn down (right side)
polyline([(L-2, T), (R, T-2), (R+2, B-4)], width=LW)

# Stroke 3: 横 (bottom close) — slight upward tilt on right
polyline([(L-4, B-2), (R+2, B-6)], width=LW)

# --- 八 (bottom two legs) ---
# gap below 口
# Stroke 4: 撇 (left leg) — from ~lower-left area, sweep down-left
# Start just under 口 slightly right of its left edge; curve to lower-left
pie_start = (118, 165)
pie_mid = (95, 210)
pie_end = (55, 260)
polyline([pie_start, pie_mid, pie_end], width=LW)

# Stroke 5: 长点/捺 (right leg) — from under 口 slightly left of right edge, down-right
na_start = (180, 165)
na_mid = (215, 215)
na_end = (255, 260)
polyline([na_start, na_mid, na_end], width=LW+1)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0172_只/01_只.png"
img.save(out)
print("wrote", out)
