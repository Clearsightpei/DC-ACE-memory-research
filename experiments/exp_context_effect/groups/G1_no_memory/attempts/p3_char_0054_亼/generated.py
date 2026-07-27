from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# 亼 = 人 (top) over 一 (bottom)
# Top: left-falling stroke (撇) from apex down-left
# Top-right: right-falling stroke (捺) from apex down-right
# Bottom: horizontal (一)

apex = (150, 70)
left_end = (75, 200)
right_end = (225, 200)

# 撇 (left-falling) - slightly curved
def draw_curve(pts, width=6):
    # Draw a smooth curve as a series of line segments
    d.line(pts, fill="black", width=width, joint="curve")

# Left stroke: apex to lower-left, slight curve outward (bulging left)
left_stroke = [
    (152, 72),
    (135, 100),
    (115, 135),
    (95, 170),
    (75, 200),
]
draw_curve(left_stroke, width=6)

# Right stroke (捺): starts slightly lower than apex, extends down-right
right_stroke = [
    (155, 90),
    (175, 125),
    (195, 160),
    (215, 190),
    (230, 205),
]
draw_curve(right_stroke, width=6)

# Bottom horizontal (一)
bottom = [
    (70, 245),
    (110, 240),
    (170, 240),
    (220, 243),
    (235, 248),
]
draw_curve(bottom, width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_亼.png")
img.save(out_path)
print(f"Saved {out_path}")
