"""G1 render for 仉 (character). PIL, 300x300, white bg, black ink.
Revision 1: better proportions, softer 几 curve, cleaner 亻 attachment.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def stroke(pts, width=5):
    d.line(pts, fill=INK, width=width, joint="curve")

# --- Left component: 亻 (person radical) ---
# Piě: from upper area slanting down-left
stroke([(100, 80), (55, 215)], width=6)
# Vertical: starts on the piě around mid-height, descends straight
stroke([(88, 140), (88, 255)], width=6)

# --- Right component: 几 ---
# Short piě on top-left of 几
stroke([(160, 105), (140, 140)], width=6)
# Left vertical of 几
stroke([(155, 138), (155, 255)], width=6)
# Top horizontal into héng zhé wān gōu (right side): horizontal then curves down and out
stroke([(155, 138), (230, 138)], width=6)
# Right curved stroke: gently curves outward and down, with slight upward hook at end
curve_pts = [
    (230, 138),
    (235, 175),
    (240, 210),
    (248, 240),
    (258, 255),
    (268, 253),
    (272, 246),
]
stroke(curve_pts, width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0113_仉/01_仉.png")
print("saved")
