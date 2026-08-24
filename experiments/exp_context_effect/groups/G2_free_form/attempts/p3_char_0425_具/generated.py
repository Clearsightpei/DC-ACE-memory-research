"""
Render 具 (jù) at 300x300, white bg, black ink.

Structure (8 strokes, per standard order):
1. 竖 — left vertical of the top rectangle (目-like)
2. 横折 — top horizontal + right vertical (top-right corner shape)
3. 横 — inner horizontal 1
4. 横 — inner horizontal 2
5. 横 — bottom horizontal of the rectangle
6. 长横 — long horizontal beneath the rectangle (extends past both sides)
7. 撇 — short left leg flicking down-left
8. 点 — right dot flicking down-right

The GT shows a squarish top block ~45% width, with the long 横 clearly
protruding wider on both sides, and two small feet at the bottom.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
STROKE = 6

# --- Top rectangle (目-like) ---
# Center it horizontally, place near top
rect_left = 105
rect_right = 195
rect_top = 55
rect_bottom = 175

# 1. 竖 — left vertical
d.line([(rect_left, rect_top), (rect_left, rect_bottom)], fill=BLACK, width=STROKE)

# 2. 横折 — top horizontal + right vertical (as one continuous shape)
d.line([(rect_left, rect_top), (rect_right, rect_top)], fill=BLACK, width=STROKE)
d.line([(rect_right, rect_top), (rect_right, rect_bottom)], fill=BLACK, width=STROKE)

# Compute even spacing for 3 inner horizontal bars + bottom
# Rectangle is 120 tall, divide into 4 rows
h_span = rect_bottom - rect_top
row_h = h_span / 4
y1 = rect_top + row_h
y2 = rect_top + 2 * row_h
y3 = rect_top + 3 * row_h
y_bottom = rect_bottom

# 3. inner 横 1
d.line([(rect_left + 3, y1), (rect_right - 3, y1)], fill=BLACK, width=STROKE - 1)

# 4. inner 横 2
d.line([(rect_left + 3, y2), (rect_right - 3, y2)], fill=BLACK, width=STROKE - 1)

# 5. inner 横 3 (three inner bars total inside the 目-like top)
d.line([(rect_left + 3, y3), (rect_right - 3, y3)], fill=BLACK, width=STROKE - 1)

# 6a. bottom 横 of rectangle (part of the stroke that closes the block)
d.line([(rect_left, y_bottom), (rect_right, y_bottom)], fill=BLACK, width=STROKE)

# 6. 长横 — long horizontal below, extends past both sides
long_y = 205
d.line([(50, long_y), (250, long_y)], fill=BLACK, width=STROKE + 1)

# 7. 撇 — left short leg, slanting down-left from around center-left below long_y
# Start from just under long_y (slightly left of center), sweep to lower-left
d.line([(125, 215), (95, 265)], fill=BLACK, width=STROKE)

# 8. 点 — right dot, slanting down-right from just under long_y (right of center)
# Draw as a short thick tapered line (approximate with a few dabs)
def dot_stroke(draw, p0, p1, w_start=4, w_end=9, steps=10):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w_start + (w_end - w_start) * t
        r = w / 2
        draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=BLACK)

dot_stroke(d, (180, 215), (210, 260), w_start=4, w_end=9)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0425_具/01_具.png")
print("saved")
