"""
丽 (li) — 7 strokes, structure:
  1) 一 long horizontal across the top
  2) two mirrored 冂-like frames side by side beneath
     each frame: outer 丨 (or 撇-like) + top-hook curving down as 竖
     inner: a small 丶 or 丨 mark inside each compartment
Layout:
  一 spans wide across top (~y=70).
  Two frames sit below, occupying roughly left half and right half.
  Left compartment: outer left vertical ~x=50, inner vertical ~x=100,
   top of frame connects them ~y=110.
  Right compartment: outer left vertical ~x=175, inner vertical ~x=225,
   top of frame connects.
  Inside each compartment: a small vertical dot-stroke.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, w=8):
    """Draw a polyline with rounded joints (brush-dab style)."""
    d.line(pts, fill=INK, width=w, joint="curve")
    r = w // 2
    for (x, y) in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# 1) 一 top horizontal — slight rise then flat, ends with tiny 顿笔
stroke([(35, 78), (90, 72), (180, 68), (255, 74), (262, 80)], w=8)

# 2) LEFT frame — outer 丨 (short vertical / mild 撇 flare down-left)
stroke([(70, 110), (60, 200), (52, 275)], w=9)

# 3) LEFT frame — top横折 (horizontal turn into a vertical) with tiny hook at bottom
stroke([(70, 110), (135, 112), (140, 118)], w=8)   # top horizontal shoulder
stroke([(140, 118), (135, 200), (130, 268), (120, 262)], w=8)  # right side vertical + tiny hook

# 4) LEFT inner mark — small vertical dot inside
stroke([(100, 165), (100, 210)], w=7)

# 5) RIGHT frame — outer 丨
stroke([(170, 110), (162, 200), (155, 275)], w=9)

# 6) RIGHT frame — top横折 + vertical with tiny hook
stroke([(170, 110), (245, 112), (250, 118)], w=8)
stroke([(250, 118), (245, 200), (240, 268), (230, 262)], w=8)

# 7) RIGHT inner mark
stroke([(205, 165), (205, 210)], w=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0298_丽/01_丽.png")
