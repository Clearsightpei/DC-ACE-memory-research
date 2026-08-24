"""G1 render of 乘 (chéng) — revision 1."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4

def poly(pts, w=T):
    d.line(pts, fill=INK, width=w, joint="curve")

# 1) Top short piě (top-left slanted little stroke)
poly([(155, 40), (135, 55)], w=T)

# 2) Top horizontal — the 一 across the top
poly([(70, 78), (230, 78)], w=T)

# 3) Central vertical — long, going from top down to bottom
poly([(150, 55), (150, 250)], w=T)

# 4) Left short piě-like stroke inside upper block (angled)
poly([(95, 108), (135, 108)], w=T)
# vertical drop on left inner
poly([(95, 108), (95, 175)], w=T)
# left inner horizontal (middle)
poly([(95, 140), (135, 140)], w=T)
# closing horizontal at bottom of left inner box
poly([(80, 175), (140, 175)], w=T)

# 5) Right inner block (mirrored 匕-like shape with hook)
# top-right descending small piě
poly([(170, 108), (215, 108)], w=T)
# right vertical going down
poly([(215, 108), (215, 155)], w=T)
# a small hook down-right at end
poly([(215, 155), (225, 168)], w=T)
# middle horizontal joining central vertical to right side
poly([(150, 140), (200, 140)], w=T)
# lower right slanted stroke (like the 乙 tail)
poly([(160, 165), (230, 175), (240, 195)], w=T)

# 6) Big 撇 (left downward sweep from mid-vertical)
poly([(150, 155), (60, 265)], w=T)

# 7) Big 捺 (right downward sweep from mid-vertical)
poly([(150, 175), (250, 265)], w=T)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0514_乘/01_乘.png")
