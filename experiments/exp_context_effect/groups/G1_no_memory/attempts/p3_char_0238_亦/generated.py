"""Render 亦 at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

# Stroke 1: top dot (short slanted stroke, upper center)
d.line([(148, 55), (158, 75)], fill=BLACK, width=LW)

# Stroke 2: long horizontal (with slight rise on right end, per GT)
# main horizontal
d.line([(55, 115), (245, 108)], fill=BLACK, width=LW)

# Stroke 3: left short stroke (piě - short downward slant left)
d.line([(105, 130), (85, 165)], fill=BLACK, width=LW)

# Stroke 4: left long piě (curving down and left from below the horizontal)
# starts around center-left, curves down-left ending as a tail
pts = []
for i in range(21):
    t = i / 20
    # bezier-like curve
    x = (1-t)**2 * 130 + 2*(1-t)*t*115 + t**2 * 95
    y = (1-t)**2 * 135 + 2*(1-t)*t*200 + t**2 * 250
    pts.append((x, y))
for i in range(len(pts)-1):
    d.line([pts[i], pts[i+1]], fill=BLACK, width=LW)

# Stroke 5: right vertical-ish (short) — the small vertical near center-right
d.line([(178, 135), (178, 195)], fill=BLACK, width=LW)

# Stroke 6: right diagonal piě (down-right stroke)
pts2 = []
for i in range(21):
    t = i / 20
    x = (1-t)**2 * 190 + 2*(1-t)*t*215 + t**2 * 240
    y = (1-t)**2 * 140 + 2*(1-t)*t*200 + t**2 * 250
    pts2.append((x, y))
for i in range(len(pts2)-1):
    d.line([pts2[i], pts2[i+1]], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0238_亦/01_亦.png")
print("saved")
