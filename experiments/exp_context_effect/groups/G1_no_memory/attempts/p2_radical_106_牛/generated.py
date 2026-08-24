"""Render 牛 (radical, 4 strokes) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def stroke(p0, p1, width=6):
    # Solid line with rounded caps via end circles.
    d.line([p0, p1], fill=INK, width=width)
    r = width / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# 牛 layout (approx from GT):
# Stroke 1: 撇 (short left-falling) top-left of the cross
# Stroke 2: short upper horizontal (slight rise)
# Stroke 3: long middle horizontal (slight rise)
# Stroke 4: long vertical spine through both horizontals

# Stroke 1: 撇
stroke((160, 65), (108, 118), width=6)

# Stroke 2: short upper horizontal (slight upward tilt)
stroke((138, 100), (208, 85), width=6)

# Stroke 4: vertical spine
stroke((172, 55), (172, 278), width=6)

# Stroke 3: long middle horizontal, slight upward tilt to the right
stroke((70, 165), (250, 150), width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_106_牛/01_牛.png")
print("saved")
