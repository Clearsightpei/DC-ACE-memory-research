"""
p1_stroke_30_横折折折  (heng-zhe-zhe-zhe)

Four-beat compound stroke: 横 → 折 down → 折 right → 折 down.
A zigzag: horizontal, corner down, corner right, corner down.

Using established brush-dab technique (per drawer_memory.md):
- Uniform primary segments r~5
- 顿-dab (r+2) at each 折 shoulder to visualize the press
- Blunt terminal press at final end (no hook flick)
- 横 segments tilt up ~3-5deg; 竖 segments drop straight

Image coords: y grows DOWN. Canvas 300x300 white, black ink.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

R = 5           # base stroke radius
R_DUN = R + 2   # 顿-dab / shoulder press radius


def dab(x, y, r=R):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def segment(x0, y0, x1, y1, r_start=R, r_end=R, steps=None):
    """Stack brush-dabs along a straight segment."""
    if steps is None:
        length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        steps = max(int(length * 2.5), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --------- Path anchors ---------
# Beat 1: 横 (top horizontal), slight up-tilt
p0 = (55, 90)
p1 = (215, 82)

# Beat 2: 竖 short, straight down from p1
p2 = (207, 140)

# Beat 3: 横 rightward from p2, slight up-tilt
p3 = (265, 132)

# Beat 4: 竖 straight down from p3, longer final descent
p4 = (257, 235)

# --------- Draw ---------

# 顿-dab at the very start of the top 横
dab(p0[0], p0[1], R_DUN)

# Beat 1: 横 (uniform)
segment(*p0, *p1, r_start=R, r_end=R)

# Shoulder-dab at corner 1
dab(p1[0], p1[1], R_DUN)

# Beat 2: short 竖 down
segment(*p1, *p2, r_start=R, r_end=R)

# Shoulder-dab at corner 2
dab(p2[0], p2[1], R_DUN)

# Beat 3: 横 rightward
segment(*p2, *p3, r_start=R, r_end=R)

# Shoulder-dab at corner 3
dab(p3[0], p3[1], R_DUN)

# Beat 4: final 竖 down
segment(*p3, *p4, r_start=R, r_end=R)

# Terminal blunt press (no hook flick — 折折折 ends blunt)
dab(p4[0], p4[1], R_DUN)

out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_30_横折折折/01_横折折折.png"
)
img.save(out_path)
print(f"Saved {out_path}")
