"""
p3_char_0251_当 — 6-stroke character.
Top: three short flicks (竖 left, 点/撇 middle-left, 撇 right).
Bottom: rectangular structure with 横折 (top+right side), two inner
horizontals, bottom-closing 横 (which is actually the bottom of the
横折 continuation — total 3 horizontals inside/bottom).

Layout: character occupies roughly center (60..240) x (40..270).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")

# --- TOP THREE FLICKS ---
# 1. left short 竖 (nearly vertical, slight lean)
stroke([(112, 70), (105, 118)], width=8)

# 2. middle-top short 竖 (a bit taller, dominant central mark)
stroke([(150, 55), (150, 115)], width=8)

# 3. right short 撇 (top-right flick, down-left)
stroke([(200, 65), (172, 118)], width=8)

# --- BOTTOM BOX-LIKE STRUCTURE ---
# 4. 横折: top horizontal from left to right, then turn down (right side)
stroke([(90, 138), (215, 138), (215, 260)], width=8)

# 5. inner middle 横 (left side to just before right wall)
stroke([(95, 178), (205, 178)], width=7)

# 6. bottom 横 (closes the box)
stroke([(88, 258), (215, 258)], width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0251_当/01_当.png")
print("done")
