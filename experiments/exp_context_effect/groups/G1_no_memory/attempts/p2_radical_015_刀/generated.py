"""G1 render of radical 刀 (2 strokes)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
T = 5  # ink thickness

def stroke(pts, width=T):
    draw.line(pts, fill=INK, width=width, joint="curve")

# Stroke 1: 横折钩 (horizontal-fold-hook)
# Entry dip on the left, go right (slight rise), turn down, curve into a hook at bottom-right.
s1 = [
    (92, 122),   # small entry dip
    (100, 115),
    (135, 108),
    (172, 105),
    (200, 107),  # end of horizontal segment
    (211, 114),  # fold corner
    (213, 150),
    (211, 190),
    (206, 220),  # bottom of vertical
    (198, 235),  # curve into hook
    (185, 240),  # hook tip (points left)
]
stroke(s1)

# Stroke 2: 撇 (left-falling), starts inside the top of stroke 1, sweeps down-left with curve.
s2 = [
    (155, 115),
    (145, 155),
    (130, 200),
    (110, 240),
    (85, 270),
]
stroke(s2)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_015_刀/01_刀.png"
img.save(out)
print(out)
