"""
G1 render for radical 戈 (4 strokes).
Strokes:
  1) 横 (heng) — short horizontal, upper-middle
  2) 斜钩 (xie gou) — long curve from upper area down to lower-right with small hook
  3) 撇 (pie) — slanted stroke from horizontal down-left through the base
  4) 点 (dian) — small dot upper-right
Output: 300x300 white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=8):
    # draw a smooth-ish polyline of variable thickness by joining segments
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill="black", width=width)
    # end caps
    for p in points:
        r = width // 2
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill="black")

# 1) 横 — horizontal, from left-mid to right-mid, slight rise
stroke([(65, 148), (110, 143), (160, 140), (205, 138)], width=8)

# 2) 斜钩 — starts on the horizontal near left-of-center-top area,
#    sweeps in a long gentle curve down-right, then tiny hook up
xg = [
    (135, 90),
    (150, 120),
    (165, 150),
    (185, 185),
    (210, 220),
    (240, 250),
    (248, 240),   # hook up
    (252, 230),
]
stroke(xg, width=8)

# 3) 撇 — starts from the horizontal around x~150, sweeps down-left
pie = [
    (160, 145),
    (135, 175),
    (110, 205),
    (85, 235),
    (65, 260),
]
stroke(pie, width=8)

# 4) 点 — small slanted dot upper-right around (215, 95)
dot = [(210, 88), (220, 98), (228, 108)]
stroke(dot, width=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_096_戈/01_戈.png")
print("saved")
