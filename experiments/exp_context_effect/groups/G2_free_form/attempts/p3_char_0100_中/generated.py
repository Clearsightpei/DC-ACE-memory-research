"""
p3_char_0100_中 — G2 free-form

Structure: 口-like box + through-going central 竖 (hanging-drop signature).
Consulted memory:
- form_catalog "竖 as central hanging drop (巾, 中, 甲)":
    LONG vertical (~180 px), starts well ABOVE the box top,
    passes through the middle, extends WELL BELOW the box base.
- form_catalog "囗/口 as pure box": 3-stroke box, corners meet cleanly.
- GT observation: box is somewhat wider than tall, sits centered
  around canvas mid. Vertical clearly protrudes both ends.

Stroke order (4 strokes):
  1. left 竖 of box
  2. 横折 (top + right wall)
  3. bottom 一 of box
  4. central 竖 through the box (long, hanging)
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 8  # line width

# Box geometry — a bit wider than tall, centered
box_left   = 90
box_right  = 210
box_top    = 110
box_bottom = 195
box_cx     = (box_left + box_right) // 2  # 150

# Central 竖 — protrudes well above and well below (hanging-drop)
axis_top    = 55    # ~55 px above box_top
axis_bottom = 275   # ~80 px below box_bottom

# ---- Stroke 1: left 竖 of box ----
draw.line([(box_left, box_top), (box_left, box_bottom)], fill=INK, width=LW)

# ---- Stroke 2: 横折 (top horizontal then right wall down) ----
# top horizontal
draw.line([(box_left, box_top), (box_right, box_top)], fill=INK, width=LW)
# shoulder + right wall
draw.line([(box_right, box_top), (box_right, box_bottom)], fill=INK, width=LW)

# ---- Stroke 3: bottom 一 ----
draw.line([(box_left, box_bottom), (box_right, box_bottom)], fill=INK, width=LW)

# ---- Stroke 4: central through-going 竖 (hanging axis) ----
draw.line([(box_cx, axis_top), (box_cx, axis_bottom)], fill=INK, width=LW)

# Small terminal 顿 dabs (blunt ends) for the axis
r = LW // 2 + 1
draw.ellipse([(box_cx - r, axis_top - r), (box_cx + r, axis_top + r)], fill=INK)
draw.ellipse([(box_cx - r, axis_bottom - r), (box_cx + r, axis_bottom + r)], fill=INK)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0100_中/01_中.png"
img.save(out)
print(f"wrote {out}")
