# BANK_DEVIATION
# skipped: (no 言 bank entry exists; ren_pang bank entry uses turtle primitives)
# reason: 信 = 亻 + 言; no 言 primitive in bank and inline PIL is cleaner
#         at 300x300 than composing turtle bank funcs for a fresh 言.
# fresh_component: yan_speech_inline (亠 + 二-hengs + 口 stack for right side)
#
# 信 (xin, "letter/trust"): left 亻 + right 言 (dot + heng + heng + heng + 口).
# Total ~9 strokes. Uniform thin lines per P12 (MMH GT style).

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4


def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)


# --- LEFT: 亻 (person radical), tall on left side --------------------
# pie: from top ~(100, 50) sweeping down-left with more curve to ~(50, 205)
d.line([(100, 50), (92, 95)], fill="black", width=LW)
d.line([(92, 95), (78, 140)], fill="black", width=LW)
d.line([(78, 140), (62, 175)], fill="black", width=LW)
d.line([(62, 175), (50, 210)], fill="black", width=LW)
# shu: vertical dropping from pie upper-mid to bottom
line((100, 100), (100, 270))

# --- RIGHT: 言 (speech), stacked components on right half -------------
# right side spans x ~ 135..270

# 1) top dot (slanted 点 stroke above the top heng, centered-ish)
d.line([(190, 40), (208, 65)], fill="black", width=LW + 2)

# 2) top heng (longest, spans across the right side)
line((135, 85), (265, 85))

# 3) middle heng #1 (shorter, inside)
line((155, 125), (245, 125))

# 4) middle heng #2 (shorter, inside)
line((155, 160), (245, 160))

# 5-7) 口 (mouth) at bottom of 言
# left shu
line((160, 195), (160, 260))
# top heng-zhe: heng across top + right shu down (drawn as 2 segments)
line((160, 195), (245, 195))
line((245, 195), (245, 260))
# bottom heng closing the 口
line((160, 260), (245, 260))

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_信.png"))
print("saved 01_信.png")
