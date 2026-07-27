"""G1 render of radical 爫 (zhǎo, claw/paw top) — revision 2.

Layout from GT: 4 strokes, all in upper ~40% of frame.
Structure (standard 爫 stroke order):
  1. left piě (short, top-left)
  2. left-center vertical/short piě (hanging below the héng)
  3. top héng-zhé (horizontal then turn down) — the roof
  4. inner piě going down-left (rightmost, angled)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 4


def poly(points, width=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=INK, width=width)


# Stroke 1: left piě — short slanted down-left, starts under the roof's left end
poly([(95, 105), (85, 125), (78, 140)])

# Stroke 2: middle-left piě — hangs under the roof center-left
poly([(130, 108), (122, 128), (115, 145)])

# Stroke 3: top héng-zhé (roof): a gentle arc going right then turning down
# horizontal-ish top with slight curve
poly([(95, 100), (130, 92), (170, 90), (200, 93), (215, 100)])
# turn down on the right end (zhé)
poly([(215, 100), (212, 115), (205, 135)])

# Stroke 4: inner piě — short slanted down-left, positioned in the middle-lower area
poly([(170, 118), (155, 138), (142, 155)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_131_爫/01_爫.png")
