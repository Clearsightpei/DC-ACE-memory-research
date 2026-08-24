"""G1 render of 此 (this). Left: 止 (4 strokes). Right: 匕 (2 strokes)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(p0, p1, w=LW):
    d.line([p0, p1], fill="black", width=w)

# ============ LEFT: 止 ============
# stroke 1: short vertical (upper-left, the "丨" of 止)
line((70, 100), (75, 210))
# stroke 2: bottom horizontal (long baseline)
line((45, 245), (155, 250))
# stroke 3: short horizontal tick from left vertical going right
line((75, 175), (120, 170))
# stroke 4: middle vertical (taller, from upper area down to baseline)
line((120, 130), (125, 245))

# ============ RIGHT: 匕 ============
# stroke 1: short 撇 (slanting down-left) starting mid-upper
line((215, 100), (185, 180))
# stroke 2: the horizontal + vertical + curved hook (竖弯钩)
# horizontal top piece
line((190, 145), (245, 140))
# vertical dropping down
line((245, 140), (240, 230))
# curve bottom to right
d.arc([200, 200, 285, 275], start=270, end=360, fill="black", width=LW)
# hook tail going up
line((285, 240), (280, 190))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0255_此/01_此.png")
print("saved")
