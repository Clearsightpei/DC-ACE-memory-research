"""Render 疽 (jū) - illness radical 疒 + 且 inside.
300x300 white bg, black ink, PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)

def poly(pts, w=4):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# === 疒 radical ===
# 1. Top dian (short falling stroke, upper-left area)
poly([(95, 55), (115, 75)], w=5)

# 2. Horizontal stroke (with slight downward tilt to right, ends with tiny tick)
poly([(75, 100), (215, 92)], w=5)
# small tick at right end
poly([(215, 92), (222, 100)], w=4)

# 3. Long left-falling pie (from horizontal down-left)
poly([(155, 65), (140, 105), (115, 155), (90, 200), (65, 245)], w=5)

# 4. Two small strokes on the left inside 疒
poly([(100, 145), (118, 160)], w=4)
poly([(88, 185), (108, 200)], w=4)

# === 且 component (inside/right) ===
# Top horizontal with hook at right end
poly([(140, 130), (232, 128)], w=5)
poly([(232, 128), (228, 138)], w=4)  # tiny hook down
# Left vertical
poly([(142, 130), (142, 240)], w=5)
# Right vertical
poly([(230, 130), (228, 240)], w=5)
# Two inner horizontals
poly([(148, 165), (225, 163)], w=4)
poly([(148, 200), (225, 198)], w=4)
# Bottom horizontal of 且 (short, connecting)
poly([(142, 240), (232, 238)], w=5)

# Bottom long horizontal (base stroke extending across)
poly([(55, 265), (265, 260)], w=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0528_疽/01_疽.png")
print("saved")
