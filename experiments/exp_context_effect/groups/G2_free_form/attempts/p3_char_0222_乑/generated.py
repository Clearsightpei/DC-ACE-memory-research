"""
乑 — three 人 stacked (top-center + two below), with a central vertical
descending through the middle. GT shows: small top 人, long central 竖
running down through the character, and two flanking 人 in the lower half
with 撇+捺 fanning out.

Rendered at 300x300 with PIL brush-dabs (width ~7-9) for calligraphic feel.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(p0, p1, width=8):
    d.line([p0, p1], fill="black", width=width)
    # end caps
    r = width // 2
    for p in (p0, p1):
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill="black")

def brush_curve(pts, width=8):
    for i in range(len(pts)-1):
        brush_line(pts[i], pts[i+1], width=width)

# ---- top 人 (small, centered near top) ----
# 撇 from center-top going down-left
brush_curve([(150, 60), (140, 75), (128, 92), (118, 110)], width=8)
# 捺 from same start going down-right
brush_curve([(150, 60), (162, 75), (175, 90), (188, 105)], width=8)

# ---- central long 竖 (the defining spine of 乑) ----
# goes from just below the top 人 straight down to bottom
brush_line((152, 95), (152, 275), width=9)

# ---- lower-left 人 ----
# 撇
brush_curve([(95, 135), (85, 160), (75, 190), (67, 220)], width=8)
# 捺 (short, angling right)
brush_curve([(95, 145), (105, 165), (117, 185)], width=7)

# ---- lower-right 人 ----
# 撇
brush_curve([(200, 135), (192, 155), (185, 175)], width=7)
# 捺 (long sweeping down-right)
brush_curve([(200, 145), (218, 175), (240, 210), (265, 235)], width=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0222_乑/01_乑.png")
print("saved")
