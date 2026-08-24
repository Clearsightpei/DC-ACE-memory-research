"""
p3_char_0377_法 — G2 first render.

Composition: 氵 (left) + 去 (right).
去 = 士 (top) + 厶 (bottom-curl).

# SIGNATURE CHECK (from sibling_signature_checklist.md, applied to 士
# component of 去):
#   | 士 | TOP 横 LONGER than bottom (~1.5×) | (vs 土)
# Enforced below: top 横 span ~135 px, bottom 横 span ~85 px (1.6x).

Form guidance from form_catalog.md:
  - 氵 water-radical: three teardrops, top two thin→thick down-right
    flicks (~40 px, ~45°), bottom is a rising 提 pointing up-right.
    x-positions form a slight leftward curve; y ~ 90, 150, 215 scaled.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=8):
    """Draw a smooth stroke through a polyline of (x, y) with round joints."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill="black")


def teardrop(x0, y0, x1, y1, w0=3, w1=10):
    """Tapered stroke from (x0,y0) thin to (x1,y1) thick — brush-dab style."""
    n = 12
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill="black")


# ---- 氵 water radical (left column) ----
# Top dot: thin-to-thick down-right flick
teardrop(55, 75, 75, 105, w0=3, w1=11)
# Middle dot: same
teardrop(40, 125, 60, 160, w0=3, w1=11)
# Bottom 提: rising, thick-to-thin going up-right
teardrop(45, 215, 85, 190, w0=11, w1=3)

# ---- 去 (right side): 士 on top ----
# Top 横 (LONG — per sibling row for 士): span ~125 px
stroke([(120, 115), (245, 115)], width=8)
# Vertical 竖 (through both horizontals)
stroke([(180, 95), (180, 170)], width=8)
# Bottom 横 (SHORTER — ~80 px vs 125 px ≈ 1.55x)
stroke([(145, 170), (225, 170)], width=8)

# ---- 厶 bottom curl ----
# 撇 (down-left from just below 士's baseline)
stroke([(180, 185), (135, 245)], width=8)
# 横折 — horizontal running rightward across, slight down slope
stroke([(140, 245), (235, 243)], width=8)
# 点 — small dab tucked inside the curl (up-right)
teardrop(210, 215, 228, 240, w0=3, w1=10)


img.save("<REPO_ROOT>/experiments/exp_context_effect/"
         "groups/G2_free_form/attempts/p3_char_0377_法/01_法.png")
