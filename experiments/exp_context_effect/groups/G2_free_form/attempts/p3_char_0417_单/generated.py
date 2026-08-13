"""
G2 render of 单 (dan / single).

Structure (top→bottom):
  1. 丷 — two short slanted dots at the very top (left-leans-in, right-leans-in)
  2. 日 — rectangular box with horizontal mid-bar (口 with 一 through middle)
  3. 一 — long horizontal below the box
  4. 丨 — long vertical spanning the whole character (center axis),
          with subtle hook flick on 竖钩? 单's 竖 does NOT hook (it's straight).

Cross-refs:
  - form_catalog: "竖 as through-going axis" — center vertical extends
    from just above the box top to bottom of canvas.
  - Two dots 丷 at top: left dot leans DOWN-LEFT to RIGHT, right dot
    leans DOWN-RIGHT to LEFT (mirror pair).
  - Long horizontal below 日 is the widest stroke; extends past 日's width.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 8  # main stroke width

# ---- 1. Top two dots 丷 ----
# Left dot: from upper-right to lower-left (short 撇 style)
d.line([(128, 35), (115, 60)], fill=INK, width=6)
# Right dot: from upper-left to lower-right (short 捺/点 style)
d.line([(172, 35), (185, 60)], fill=INK, width=6)

# ---- 2. 日 (rectangular box with mid-bar) ----
# Box coords
box_left, box_right = 95, 205
box_top, box_bottom = 70, 165
mid_y = 118

# Top horizontal (roof)
d.line([(box_left, box_top), (box_right, box_top)], fill=INK, width=LW)
# Left vertical
d.line([(box_left, box_top), (box_left, box_bottom)], fill=INK, width=LW)
# Right vertical (with slight bend at top — 横折)
d.line([(box_right, box_top), (box_right, box_bottom)], fill=INK, width=LW)
# Bottom horizontal
d.line([(box_left, box_bottom), (box_right, box_bottom)], fill=INK, width=LW)
# Middle horizontal
d.line([(box_left, mid_y), (box_right, mid_y)], fill=INK, width=LW)

# ---- 3. Long horizontal 一 below the box ----
# This is the widest stroke; extends beyond the box on both sides.
h_y = 210
d.line([(35, h_y), (265, h_y)], fill=INK, width=LW + 1)

# ---- 4. Center vertical 丨 (straight, no hook for 单) ----
# Extends from top of the box down through the long horizontal to near bottom.
cx = 150
d.line([(cx, box_top - 5), (cx, 285)], fill=INK, width=LW + 1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0417_单/01_单.png")
print("wrote 01_单.png", img.size)
