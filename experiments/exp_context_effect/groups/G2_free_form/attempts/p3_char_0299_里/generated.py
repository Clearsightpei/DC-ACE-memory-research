"""里 (lǐ) — 7 strokes
Structure: 日 on top + 土 on bottom, sharing the middle vertical.
Stroke order:
 1. 竖 (left vertical of top 日)
 2. 横折 (top + right vertical of top 日)
 3. 横 (middle horizontal inside 日)
 4. 横 (bottom of 日 / above 土)
 5. 竖 (central long vertical, extends into 土)
 6. 横 (middle horizontal of lower 土)
 7. 横 (bottom horizontal — longest, widest of all)

# SIGNATURE CHECK (not in sibling list, but note): the LAST horizontal
# stroke is the WIDEST; the character body 日 is narrower than 土-bottom.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=10):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill=BLACK)

# Top 日: roughly cols 100..200, rows 40..150
LX, RX = 105, 195
T, MID, BOT_RI = 50, 100, 155   # top, middle-bar, bottom of 日

# 1. 竖: left vertical of 日
stroke([(LX, T+3), (LX, BOT_RI)], width=9)

# 2. 横折: top horizontal + right vertical
stroke([(LX-4, T), (RX, T+4), (RX, BOT_RI)], width=9)

# 3. 横: middle horizontal inside 日
stroke([(LX+3, MID), (RX-3, MID)], width=8)

# 4. 横: bottom of 日
stroke([(LX-2, BOT_RI), (RX+2, BOT_RI)], width=9)

# 5. 竖: central vertical, from top of 日 through to bottom of 土
CX = (LX + RX) // 2
stroke([(CX, T+15), (CX, 245)], width=10)

# 6. 横: middle horizontal of lower 土 (a bit wider than 日)
stroke([(85, 205), (215, 205)], width=9)

# 7. 横: bottom horizontal — the WIDEST stroke, slight rightward taper
stroke([(50, 260), (255, 258)], width=11)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0299_里/01_里.png")
print("saved")
