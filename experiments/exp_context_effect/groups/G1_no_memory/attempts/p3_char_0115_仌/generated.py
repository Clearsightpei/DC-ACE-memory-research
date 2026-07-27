"""Render 仌 (two 人 stacked vertically) at 300x300, black ink on white.
Revision 1: match GT — top 人 smaller and shifted slightly right,
bottom 人 larger with捺 sweeping further, gentle curves."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

WIDTH = 5

def stroke(points, width=WIDTH):
    d.line(points, fill="black", width=width, joint="curve")
    r = width // 2
    for x, y in [points[0], points[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Top 人 — apex around (160, 50), moderately sized
# 撇 (left-falling): starts at apex, curves down-left
stroke([(158, 48), (150, 70), (130, 105), (108, 140), (95, 160)])
# 捺 (right-falling): starts just below apex, sweeps down-right
stroke([(162, 68), (180, 100), (200, 130), (218, 155)])

# Bottom 人 — apex around (140, 155), larger
# 撇 (left-falling): long sweeping curve down-left
stroke([(140, 155), (128, 180), (108, 215), (85, 250), (70, 268)])
# 捺 (right-falling): long sweeping curve down-right, extending further
stroke([(146, 178), (170, 210), (200, 240), (235, 262), (255, 268)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0115_仌/01_仌.png")
