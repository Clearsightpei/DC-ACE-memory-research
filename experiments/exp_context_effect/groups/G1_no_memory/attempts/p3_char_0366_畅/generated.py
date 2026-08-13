"""G1 render of 畅 = 申 (left) + 昜-simplified (right)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w)

# ===== LEFT: 申 (occupies x ~ 40..130) =====
box_l, box_r = 55, 125
box_t, box_b = 105, 175
line([(box_l, box_t), (box_r, box_t)], 4)             # top
line([(box_l, box_b), (box_r, box_b)], 4)             # bottom
line([(box_l, box_t), (box_l, box_b)], 4)             # left
line([(box_r, box_t), (box_r, box_b)], 4)             # right
line([(box_l, (box_t+box_b)//2), (box_r, (box_t+box_b)//2)], 4)  # middle H
line([((box_l+box_r)//2, 50), ((box_l+box_r)//2, 255)], 5)        # vertical through

# ===== RIGHT: 昜-simplified (occupies x ~ 155..275) =====
# Top small 日/box
tb_l, tb_r = 175, 245
tb_t, tb_b = 60, 110
line([(tb_l, tb_t), (tb_r, tb_t)], 4)
line([(tb_l, tb_t), (tb_l, tb_b)], 4)
line([(tb_r, tb_t), (tb_r, tb_b)], 4)
line([(tb_l, tb_b), (tb_r, tb_b)], 4)
line([(tb_l, (tb_t+tb_b)//2 + 3), (tb_r, (tb_t+tb_b)//2 + 3)], 3)

# Short horizontal just under the box (一)
line([(170, 130), (250, 130)], 4)

# Left downward stroke — long 撇 from ~ (215, 130) sweeping lower-left
line([(215, 130), (200, 175), (170, 235), (150, 275)], 5)

# Right hook — 横折折折钩 style: dive right, down, curve left, hook
# Start where 一 ends on right, go down-right forming the right cheek then hook.
line([(250, 130), (270, 155), (255, 200), (225, 245), (185, 240)], 5)

# Two inner 撇 strokes (like 勿's inner slashes)
line([(210, 175), (185, 220)], 4)
line([(235, 180), (210, 225)], 4)

out = os.path.join(os.path.dirname(__file__), "01_畅.png")
img.save(out)
print("wrote", out)
