"""
所 = 户 (left) + 斤 (right).
Left 户 (4 strokes): 点 (top), 横折 (upper shoulder), 横 (middle), 撇 (long sweep down-left).
Right 斤 (4 strokes): 短撇 (top-left slant), 横 (top cross), 竖撇 (down-left), 长竖 (long vertical, extending below baseline).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

def curve(pts, w=6, steps=40):
    # quadratic bezier through 3 pts
    (x0, y0), (x1, y1), (x2, y2) = pts
    prev = (x0, y0)
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        d.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)

# ---------- LEFT 户 ----------
# 1) 点 - short slanted dot at top (small, above shoulder, centered-ish)
curve([(88, 45), (95, 55), (105, 68)], w=7)

# 2) 横折 (shoulder) - horizontal then sharp turn down
line([(60, 88), (140, 82)], w=6)
line([(140, 82), (144, 105)], w=6)

# 3) 横 - middle horizontal inside 户 (just below shoulder area)
line([(72, 128), (135, 125)], w=6)

# 4) 长撇 - long left sweep starting near top-left of shoulder, going down-left
curve([(78, 90), (68, 175), (32, 275)], w=7)

# ---------- RIGHT 斤 ----------
# 5) 短撇 - short slanting stroke at top-left of 斤
curve([(180, 55), (172, 72), (162, 90)], w=7)

# 6) 横 - top horizontal of 斤 (slightly rising to right)
line([(162, 90), (260, 80)], w=6)

# 7) 竖撇 - starts near left side of 斤, curves down-left
curve([(180, 100), (172, 180), (152, 270)], w=7)

# 8) 长竖 - long vertical extending well below from mid-top area
line([(228, 100), (228, 285)], w=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0371_所/01_所.png")
