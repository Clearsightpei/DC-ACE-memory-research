"""G1 render of radical 卩 (2 strokes)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
T = 5  # ink thickness

def stroke(pts, width=T):
    draw.line(pts, fill=INK, width=width, joint="curve")

# 卩: two strokes
#   1) 横折钩 forming a small "P"-head at the upper-right
#   2) long 竖 on the left going all the way down

# Stroke 1: 横折钩 (horizontal, fold down-right, curve back left as hook)
# Starts at top-left of the head, goes right along top, folds down,
# then curves back leftward at the bottom of the head.
s1 = [
    (135, 90),    # entry (top-left of head)
    (150, 85),
    (175, 82),
    (195, 84),    # top-right of head (end of horizontal)
    (205, 92),    # fold corner
    (208, 115),
    (206, 140),
    (198, 158),   # curve begins
    (180, 165),   # bottom of head curve
    (155, 163),   # hook returns leftward
    (140, 158),   # hook tip
]
stroke(s1)

# Stroke 2: long 竖 (vertical) starting from the top-left of the head,
# extending down well past the head into the lower area.
s2 = [
    (135, 88),    # top (meets stroke 1 entry)
    (135, 130),
    (135, 180),
    (134, 230),
    (133, 265),   # bottom
]
stroke(s2)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_023_卩/01_卩.png"
img.save(out)
print(out)
