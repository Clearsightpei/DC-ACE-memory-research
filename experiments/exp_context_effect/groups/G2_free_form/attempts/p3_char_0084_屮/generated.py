"""Render 屮 (chè, "sprout") — 3 strokes.

Structure (from GT):
- Central 竖: long vertical, top ~y=70 down to ~y=270, running through
  the middle of the canvas.
- Horizontal crossbar (横) around y=175, spanning ~x=80..220, crossing
  the central 竖.
- Left branch: a short curved/angled stroke going from the crossbar
  down-left then upward (like a hook rising from the left endpoint of
  the bar up to about y=130).
- Right branch: a short diagonal/curve going from the crossbar up-right
  (from the right endpoint of the bar up to about y=140).

Canvas: 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
WIDTH = 6

# 1) Central 竖 (vertical descender) — runs top~65 to bottom~280
cx = 155
draw.line([(cx, 65), (cx, 285)], fill=INK, width=WIDTH)

# 2) Left branch — 竖折 style: starts high (up around y=110), comes
#    down and to the right along the crossbar. In GT the left arm
#    rises to about the same height as the top of the central 竖.
#    Model as two segments: vertical-ish drop + horizontal to center.
draw.line([(88, 110), (78, 195)], fill=INK, width=WIDTH)   # left vertical of the "cup"
draw.line([(78, 195), (155, 180)], fill=INK, width=WIDTH)  # left half of crossbar

# 3) Right branch — mirror: crossbar-right + rising tick
draw.line([(155, 180), (230, 185)], fill=INK, width=WIDTH) # right half of crossbar
draw.line([(230, 185), (222, 120)], fill=INK, width=WIDTH) # right rising tick

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0084_屮/01_屮.png")
