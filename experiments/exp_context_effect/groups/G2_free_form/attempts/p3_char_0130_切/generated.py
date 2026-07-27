"""Render 切 (p3_char_0130_切) — 4 strokes: 七 (left) + 刀 (right).

# SIGNATURE CHECK (per sibling_signature_checklist.md):
#   target = 切 = 七 + 刀 (2 components)
#   bit (七 component) = "top stroke is a 横 (left→right)" — NOT a 撇.
#     Avoid 匕 confusion: horizontal top, not diagonal.
#   flick (竖弯钩 in 七)    = UP-and-LEFT after arc (~-110°)
#   flick (横折钩 in 刀)    = UP-and-LEFT at terminal   (~-110°)

Layout (300x300, left-right composition):
  Left 七 : occupies roughly x ∈ [40, 145], centered vertically.
  Right 刀: occupies roughly x ∈ [155, 265], centered vertically,
           its 横折钩 top starts a bit above the 七 top (刀's shoulder
           usually rides higher).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width=8):
    """Draw a stroke as a smooth polyline with rounded joins."""
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=INK, width=width)
    # round caps / joints
    r = width // 2
    for x, y in points:
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# ----- LEFT: 七 -----
# Stroke 1: 横 (top horizontal, slight rise to the right).
# Long horizontal, extends left of the vertical stem.
heng_left = [(28, 138), (60, 133), (95, 128), (125, 124), (150, 121)]
stroke(heng_left, width=8)

# Stroke 2: 竖弯钩 (vertical starts high above 横, comes down, curves right, hooks up-left)
shuwan = [
    (100, 78),   # start high, well above 横
    (98, 105),
    (97, 138),   # crosses the 横 (which is around y=124-130)
    (98, 170),
    (105, 200),  # begin arc
    (125, 218),  # sweeping right
    (150, 222),
    (168, 218),  # arc peak on the right
    # hook: flick up-and-left
    (168, 200),
    (155, 190),
]
stroke(shuwan, width=8)

# ----- RIGHT: 刀 -----
# Stroke 3: 横折钩
#   top 横 (left→right, slight rise), fold down at the shoulder, descend
#   with slight left-lean, terminal hook flicks up-and-left.
hzhg = [
    (182, 92),   # top-left start of 横
    (215, 88),
    (245, 84),   # end of 横 / shoulder
    (253, 95),   # shoulder fold begins
    (250, 125),  # descending
    (243, 160),
    (232, 195),  # curving in slightly
    (220, 220),  # bottom of the down-stroke
    # hook: up-and-left flick
    (218, 205),
    (200, 198),
]
stroke(hzhg, width=8)

# Stroke 4: 撇 (from the top-left of the 刀 shoulder area, sweeps down-left,
# crossing through the descending 竖钩 stroke, ending near bottom-left).
pie = [
    (232, 108),
    (218, 138),
    (202, 168),
    (185, 200),
    (168, 232),
    (152, 262),
]
stroke(pie, width=8)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0130_切/01_切.png"
img.save(out)
print(f"wrote {out}")
