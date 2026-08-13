# BANK_DEVIATION
# skipped: ren_pang.py (turtle-based); no bank entry for 長
# reason: 倀 is 亻 + 長; 長 has no bank entry and needs 8 strokes inlined,
#   so cleaner to render whole char in PIL rather than mix turtle+PIL.
# fresh_component: chang_long_for_LR (right-side 長 sized for L-R composition)

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5


def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)


def poly(pts, w=LW):
    d.line(pts, fill="black", width=w, joint="curve")


# ------------- LEFT: 亻 (compressed narrow) -------------
# pie: gentle curve from upper-right down to lower-left
poly([(78, 55), (72, 85), (60, 130), (42, 200)], w=LW)
# shu: short vertical starting on pie's mid-shaft
line((72, 115), (72, 245), w=LW)

# ------------- RIGHT: 長 -------------
# Right block: x in [110, 275], vertical shaft near x=180

# heng 1 (top short)
line((135, 68), (240, 66), w=LW)
# small down-tick on right end of heng 1
line((240, 66), (243, 88), w=LW)

# heng 2 (slightly longer)
line((130, 100), (245, 98), w=LW)

# heng 3 (long horizontal — the base of the top block)
line((115, 135), (255, 133), w=LW)

# Central vertical shaft (from heng 1 down to bottom crotch)
line((180, 68), (180, 210), w=LW)

# Middle short heng crossing shaft (between heng3 and bottom)
line((140, 170), (220, 168), w=LW)

# Bottom-left 撇 — sweeps down-left from lower shaft
poly([(180, 208), (160, 228), (135, 250), (110, 270)], w=LW)

# Bottom-right 捺 with hook — from mid shaft area, curves down-right
# starts as a short horizontal, then swoops down-right with slight curve
poly([(155, 200), (185, 218), (215, 240), (245, 260), (270, 262)], w=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_倀.png"))
