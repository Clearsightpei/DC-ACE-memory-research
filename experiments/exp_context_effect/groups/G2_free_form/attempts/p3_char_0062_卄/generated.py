"""Render 卄 (p3_char_0062) to a 300x300 PNG.

卄 = two verticals crossed by one horizontal bar. 4 strokes total?
Looking at the GT: 2 near-vertical strokes (slight inward lean at top
for the right one, straighter for the left), plus one long horizontal
bar crossing them in the upper-middle region. Total 3 visible strokes.
(卄 is the ancient form; MMH renders it as three strokes.)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
WIDTH = 7

# Left vertical: from upper-left down to lower-left
# From GT: starts around (90, 105), ends around (95, 265)
d.line([(90, 105), (95, 265)], fill=INK, width=WIDTH)

# Right vertical: from upper-right down to lower-right, slight inward top
# From GT: starts around (210, 100), ends around (200, 265)
d.line([(210, 100), (200, 265)], fill=INK, width=WIDTH)

# Horizontal cross-bar: long, slightly wavy, crosses both verticals
# From GT: from about (55, 165) to (245, 160)
d.line([(55, 165), (245, 158)], fill=INK, width=WIDTH)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0062_卄/01_卄.png")
