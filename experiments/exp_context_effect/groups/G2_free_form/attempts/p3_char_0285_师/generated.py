"""
师 (shī) — 6 strokes.  Revision 1.

Structure (left-right, LEFT ~1/3 wide, RIGHT ~2/3 wide):

LEFT component (narrow column):
  1) 丿 short top slash
  2) 丨 long vertical stem below the slash, extending near bottom

RIGHT component (巾-like, taller):
  3) 一  top horizontal
  4) 丿  left descender from under the horizontal, sweeping down-left
  5) 冂  shoulder + right vertical (with tiny hook)
  6) 丨  middle vertical descending past the box to bottom

Fixes vs first pass:
- widened the right box (was too cramped)
- kept the top horizontal within the right column so it doesn't
  overlap the left component
- moved the left 丿 lower so it doesn't dominate
- lengthened left 丨 to sit at the same baseline as the right 丨
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BW = 6


def poly(points, w=BW):
    d.line(points, fill=INK, width=w, joint="curve")


# ============ LEFT COMPONENT (x ~ [30, 100]) ============
# 1) 丿 small slash near top
poly([(95, 75), (80, 105), (60, 140)], w=BW)

# 2) 丨 long vertical (starts near end of slash, descends to bottom)
poly([(70, 120), (55, 265)], w=BW)


# ============ RIGHT COMPONENT (x ~ [120, 270]) ============
# 3) 一 top horizontal
poly([(125, 80), (265, 78)], w=BW)

# 4) 丿 left descender: from just under the top horizontal, sweeping
#    down-left to lower-left of the right component
poly([(155, 82), (140, 160), (125, 260)], w=BW)

# 5) 冂 shoulder + right vertical with small hook (竖钩 flick up-left)
poly([(155, 120), (255, 120), (255, 250), (245, 240)], w=BW)

# 6) 丨 middle vertical, descending past the box
poly([(205, 120), (205, 285)], w=BW)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0285_师/01_师.png")
print("wrote 01_师.png")
