"""
p3_char_0092_廾 (nòng, "twenty-hands" / 弄 base)
3 strokes:
  1. 撇 (piě) — left vertical descending, curves outward left near bottom
  2. 竖 (shù) — right vertical, straight down (slight lean if any)
  3. 横 (héng) — long horizontal crossing both verticals at upper portion

Wait: standard stroke order for 廾 is:
  1. 横 (long horizontal, top)
  2. 撇 (left leg — starts high on horizontal, curves down-left)
  3. 竖 (right leg — descends straight from horizontal)

Actually the canonical order for 廾 is: 一 丿 丨 (heng, pie, shu).
Looking at GT: horizontal is at the vertical midpoint, both legs
extend above and below it (legs are through-going).

Structure per GT:
  - 撇: left leg, top around (~90, ~110), curves down and left to (~70, ~230)
  - 竖: right leg, straight from (~200, ~110) to (~205, ~240)
  - 横: horizontal, from (~55, ~150) to (~245, ~145), long, slight lift right
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke_line(pts, width=8):
    """Draw a polyline with rounded joints/caps by dabbing circles."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        r = width // 2
        draw.ellipse((p[0]-r, p[1]-r, p[0]+r, p[1]+r), fill="black")

# Stroke 1: 横 (horizontal top-bar) — long, spans nearly full width, slight right lift
heng_pts = [(48, 152), (120, 148), (200, 145), (252, 142)]
stroke_line(heng_pts, width=9)

# Stroke 2: 撇 (left leg) — starts above horizontal at ~x=100,
# descends nearly vertical then curves outward to lower-left
pie_pts = [
    (102, 108),
    (100, 150),
    (96, 190),
    (88, 225),
    (72, 250),
    (58, 262),
]
stroke_line(pie_pts, width=9)

# Stroke 3: 竖 (right leg) — starts above horizontal at ~x=200,
# descends straight down with a mild lean, extends below GT range
shu_pts = [
    (200, 108),
    (202, 160),
    (204, 210),
    (206, 258),
]
stroke_line(shu_pts, width=9)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0092_廾/01_廾.png"
img.save(out)
print(f"Wrote {out}  size={img.size}")
