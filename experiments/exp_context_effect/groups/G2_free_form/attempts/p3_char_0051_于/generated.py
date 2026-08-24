"""
Draw 于 (yu2) — 3 strokes: short top 横, longer middle 横, 竖钩 (vertical
with left hook at bottom). The 竖钩 crosses BOTH horizontals near the
right-of-center of each (per GT), extending well below the middle 横
with a small leftward hook.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BRUSH = 9

def dab(x, y, r=None):
    r = r or BRUSH // 2 + 1
    d.ellipse([x - r, y - r, x + r, y + r], fill=INK)

def stroke(pts, width=BRUSH):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=width)
    for p in pts:
        dab(*p)

# Stroke 1: short top 横, slight down-then-up curve, ends with tiny 顿
# In GT, top 横 is short, positioned roughly y=95, x from ~85 to ~215
stroke([(85, 100), (140, 92), (200, 92), (215, 98)])
# small end tick (顿)
dab(217, 100, r=6)

# Stroke 2: longer middle 横, ~y=155, x from ~55 to ~245
stroke([(55, 158), (130, 148), (210, 148), (245, 155)])
dab(247, 157, r=6)

# Stroke 3: 竖钩 — vertical going down slightly right-of-center,
# then hook LEFT at bottom. Starts just above middle 横 (~y=125),
# descends past middle 横 to ~y=250, then hooks up-left to ~(140,235)
# Actually in GT the stem starts around the top-横 area but the top-横
# ends before it - stem starts a bit above middle 横.
# From GT: stem starts at ~(165, 118), descends to ~(150, 250), hooks left+up.
stroke([(168, 120), (162, 160), (155, 210), (150, 250)])
# hook curves left and slightly up
stroke([(150, 250), (135, 252), (118, 240), (110, 225)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0051_于/01_于.png")
print("saved")
