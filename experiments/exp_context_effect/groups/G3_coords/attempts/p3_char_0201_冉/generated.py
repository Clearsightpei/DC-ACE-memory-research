"""冉 (rǎn) — 5 strokes.

Composition inferred from GT PNG (v8: trust GT, inline fresh):
  1. 竖 (left vertical) — leans slightly right at top, ends bottom-left.
  2. 横折钩 (top+right frame) — short horizontal → vertical → tiny hook.
  3. 横 (inner upper horizontal) — inside the box, does not protrude.
  4. 竖 (short inner vertical) — connects the two inner horizontals.
  5. 横 (through-horizontal) — the longest stroke, protrudes past the frame.

Written fresh under v8; no bank primitive is a good geometric fit for this
compound envelope. Draws with PIL directly.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
THIN = 4   # GT uses thin uniform strokes per P12

def line(p0, p1, w=THIN):
    d.line([p0, p1], fill=INK, width=w)

def poly(pts, w=THIN):
    d.line(pts, fill=INK, width=w, joint="curve")

# --- Frame ---
# Left vertical 竖 — slight lean (top slightly right of bottom).
# Top ~ (95, 70), bottom ~ (75, 265).
poly([(95, 70), (85, 170), (75, 265)], w=THIN)

# 横折钩 — top-right frame with hook.
# top horizontal from (95, 70) sweeping right and slightly up to (215, 55),
# then vertical down to about (225, 245), tiny hook left at bottom.
poly([(95, 70), (155, 60), (215, 55)], w=THIN)      # top 横
poly([(215, 55), (220, 150), (225, 240)], w=THIN)    # right 竖
poly([(225, 240), (215, 245), (210, 240)], w=THIN)   # small 钩 back-left

# --- Inner strokes ---
# Upper inner 横 — sits inside the frame near y~130, spans left-vert to right-vert.
line((90, 128), (222, 122), w=THIN)

# Short inner 竖 — connects the two inner horizontals along the mid axis,
# extends slightly past the through-horizontal per GT.
line((150, 128), (150, 215), w=THIN)

# Through 横 — the long horizontal that protrudes past both sides.
# From x~35 to x~265, at y~198, slight downward slope right-to-left.
line((35, 205), (270, 195), w=THIN)

# Save
out = os.path.join(os.path.dirname(__file__), "01_冉.png")
img.save(out)
print("wrote", out)
