"""
北 — 5 strokes, side-by-side composition (left half + right 匕).

# SIGNATURE CHECK (from sibling_signature_checklist row for 匕):
#   匕 | top stroke is a 撇 (upper-right→lower-left); terminal hook
#       flicks UP-and-LEFT
# The right half of 北 IS a 匕 — enforce its two signature bits:
#   (1) top stroke: 撇 going upper-right → lower-left
#   (2) terminal 竖弯钩 flicks UP-and-LEFT (never down/right)

Strokes:
  Left half (a rotated/mirrored 匕-like piece):
    1. 竖 — a slightly leftward-slanted vertical near left-center
    2. 横 — short horizontal near top, crossing the vertical
    3. 提 — short rising stroke from bottom of vertical up-right
  Right half (匕):
    4. 撇 — long stroke from upper-right area falling to lower-left,
            crossing near the middle
    5. 竖弯钩 — vertical, bends right, flicks UP-and-LEFT
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=10):
    d.line(pts, fill=INK, width=width, joint="curve")
    # dab endpoints so strokes look weighted
    for (x, y) in (pts[0], pts[-1]):
        r = width // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# ---------- LEFT HALF ----------
# 1) 竖 — vertical (slight lean), left-center
stroke([(90, 75), (90, 245)], width=11)

# 2) 横 — short horizontal at top-left, meeting the vertical at its top
#    (in 北 this 横 goes to the LEFT of the vertical, not crossing it)
stroke([(45, 108), (95, 108)], width=10)

# 3) 提 — short rising stroke from bottom of vertical up-right
stroke([(90, 215), (150, 178)], width=10)

# ---------- RIGHT HALF (匕) ----------
# 4) 撇 — from upper-right area falls to lower-left, signature stroke
#         upper-right → lower-left, crosses roughly through middle
stroke([(230, 75), (155, 240)], width=11)

# 5) 竖弯钩 — starts on the 撇 midway, vertical then bends right,
#    terminal hook flicks UP-and-LEFT (signature bit)
vertical = [(200, 135), (200, 240)]
bend = [(200, 240), (218, 258), (245, 260), (262, 250)]  # curve right/down
hook = [(262, 250), (256, 228)]  # flick UP-and-LEFT
stroke(vertical, width=11)
stroke(bend, width=11)
stroke(hook, width=11)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0208_北/01_北.png"
)
