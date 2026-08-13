# 要 (yao) — 9 strokes
# Structure: top 覀 (flat 西 form) + bottom 女
#
# Bank note: no 覀 or 女 bank entry (女 remains in errata retry_n=3,
# never PASSed). Full fresh inline PIL render — no bank primitive to
# call, so no BANK_DEVIATION block required.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5  # uniform thin per P12 (MMH GT is uniform-thin)

def line(p, q, w=LW):
    d.line([p, q], fill=INK, width=w)

# ---- TOP: 覀 (flat form of 西) ----------------------------------------
# 1. top short 一 (crown)
line((85, 55), (215, 55))

# 2. left vertical of frame (short 竖)
line((90, 65), (90, 130))

# 3. inner-left vertical divider
line((135, 75), (135, 125))

# 4. inner-right vertical divider
line((178, 75), (178, 125))

# 5. right vertical of frame — 横折 form: goes down from top corner,
#    small hook inward at bottom-right? In 覀 it is a 横折 (top-right
#    corner + right shu). Render as a plain shu on the right frame.
line((220, 65), (220, 130))

# 6. bottom 一 of the frame — spans and slightly overhangs both sides
line((78, 130), (232, 130))

# ---- BOTTOM: 女 ------------------------------------------------------
# 7. 撇点 (V): starts upper-left, comes down-right (steep 撇),
#    then folds with a clear angle change into a shorter, flatter
#    down-right 点. The fold must read as a V, not a straight line.
line((105, 150), (140, 220))      # 撇 part — steep down-right
line((140, 220), (205, 258))      # 点 part — flatter, distinctly different angle

# 8. 撇 (long diagonal) — starts upper-right of 女 area, sweeps
#    down-left across the whole bottom.
line((210, 150), (60, 275))

# 9. 横 (long horizontal) — cuts across at the waist, extends past
#    both sides of the 撇 crossing.
line((55, 235), (270, 235))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0433_要/01_要.png")
