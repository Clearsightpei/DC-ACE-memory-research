"""
设 (shè) — left 讠 (2 strokes: 点 + 横折提), right 殳 (top 几-like + bottom 又).
Total ~7 strokes. Left radical compressed to ~1/3 width.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    # smooth stroke via joined line + rounded caps (dab circles at each pt)
    d.line(pts, fill="black", width=width, joint="curve")
    r = width // 2
    for (x, y) in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---------- LEFT: 讠 (compressed to left ~30%) ----------
# 1) 点 (dot) at upper-left of the radical
stroke([(55, 70), (70, 90)], width=9)

# 2) 横折提 — short horizontal, turn down-left, then flick up-right
stroke([(45, 130), (95, 135)], width=7)          # horizontal top
stroke([(95, 135), (55, 195)], width=7)          # descending fold
stroke([(55, 195), (105, 175)], width=7)         # rising flick (提)

# ---------- RIGHT: 殳 ----------
# Top part: 几-like — short 撇 + 横折弯钩(简化为横折弯)
# short 撇 (top-left flick of the top box)
stroke([(155, 75), (140, 105)], width=8)

# 横折 top: horizontal then fold down to form the "几" top
stroke([(150, 90), (240, 90)], width=7)          # horizontal top
stroke([(240, 90), (225, 140)], width=7)         # fold down-left curve
# small inside dot/mark inside top (a horizontal short line inside)
stroke([(165, 120), (215, 120)], width=6)

# Bottom part: 又
# 横撇 — starts high-left, goes right-then-flicks down-left
stroke([(135, 165), (235, 165)], width=7)        # horizontal
stroke([(235, 165), (170, 235)], width=8)        # long 撇 down-left
# 捺 — starts near the crossing, sweeps down-right
stroke([(180, 195), (260, 265)], width=9)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0281_设/01_设.png")
print("done")
