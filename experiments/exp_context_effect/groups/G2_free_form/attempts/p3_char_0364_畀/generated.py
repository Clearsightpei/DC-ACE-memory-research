"""
G2 attempt for 畀 (p3_char_0364_畀).

Structure: 田 (top) + long 一 (middle) + two legs 丌-style (bottom).
- Top: small 田 rectangle with inner cross, centered upper half.
- Middle: long horizontal bar (wider than top田), the "shoulder" that
  makes 畀 recognizable and separates top from legs.
- Bottom: two verticals descending from the shoulder; left leg is a
  straight 竖, right leg is 竖 (in GT slightly leans, but keep upright).
No hooks in 畀.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=8):
    d.line(pts, fill=BLACK, width=width, joint="curve")


# --- 田 on top: rectangle from (95,45) to (205,150) with inner cross ---
# Outer rectangle: 4 strokes drawn as one continuous shape.
# Left vertical of 田
stroke([(95, 45), (95, 150)], width=8)
# Top horizontal + right shoulder (横折)
stroke([(95, 45), (205, 45), (205, 150)], width=8)
# Bottom horizontal (closes 田 base)
stroke([(95, 150), (205, 150)], width=8)
# Inner vertical of 田
stroke([(150, 45), (150, 150)], width=7)
# Inner horizontal of 田
stroke([(95, 98), (205, 98)], width=7)

# --- Long shoulder 一 (the widest horizontal, well below 田) ---
# Positioned a bit below 田's bottom, extending outward past 田's width.
stroke([(35, 195), (270, 195)], width=10)

# --- Two legs descending from the shoulder ---
# Left leg: straight 竖, from just inside left of shoulder down to bottom.
stroke([(90, 195), (75, 285)], width=9)
# Right leg: straight 竖, mirroring, from near right of shoulder.
stroke([(210, 195), (225, 285)], width=9)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0364_畀/01_畀.png"
)
print("saved 01_畀.png")
