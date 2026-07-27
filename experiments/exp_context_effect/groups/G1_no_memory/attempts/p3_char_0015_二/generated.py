"""Render 二 (two) as a 300x300 PNG.

二 = two horizontal strokes:
  - Upper stroke: shorter
  - Lower stroke: longer
Both roughly centered horizontally with visible vertical gap.
"""
from PIL import Image, ImageDraw

SIZE = 300
OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0015_二/01_二.png"

img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

# Upper horizontal (shorter) — slight downward slant at end typical of 横
# start ~ (85, 105), end ~ (200, 100). Length ~115.
d.line([(85, 108), (205, 102)], fill="black", width=10)

# Lower horizontal (longer) — the base 横; slightly heavier feel
# start ~ (55, 205), end ~ (245, 200)
d.line([(55, 208), (250, 200)], fill="black", width=12)

# Optional subtle 顿笔 (right end of lower stroke): tiny thickening dot
d.ellipse([(244, 194), (255, 208)], fill="black")
# Small 顿 at right end of upper stroke
d.ellipse([(200, 97), (210, 108)], fill="black")

img.save(OUT)
print(f"Saved {OUT}")
