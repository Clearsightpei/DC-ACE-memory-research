"""
G2 attempt: 而 (ér) — 6 strokes.

Structure (from GT):
  1. short 一 at top center
  2. long 一 below (the main brow), extends wider
  3. left side: 丿 stroke curving down-and-slightly-left (from left end of brow)
  4. right side: 竖 with rightward-then-up hook at bottom (from right end of brow)
  5. inner left short vertical
  6. inner right short vertical
The two inner verticals hang from the underside of the brow, not touching the bottom.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
BW = 6  # base ink width


def stroke(points, width=BW):
    """Draw a polyline with rounded joints, brush-dab style."""
    d.line(points, fill=INK, width=width, joint="curve")
    # dab endpoints for a slightly calligraphic look
    for x, y in (points[0], points[-1]):
        r = width // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# Layout — center of character around (150, 155). Overall character
# occupies roughly x=55..245, y=70..250.

# Stroke 1: top short horizontal — slightly tilted, above the brow
stroke([(120, 82), (188, 78)], width=6)

# Stroke 2: long brow horizontal — wider, extends left and right
stroke([(60, 118), (240, 112)], width=7)

# Stroke 3: left 丿 — starts near left end of brow, curves down-left
# Actually GT shows this as a downward-going left leg that curves slightly
stroke([(70, 118), (62, 175), (58, 240)], width=7)

# Stroke 4: right 竖弯 with hook — vertical down, curves rightward-then-up
# From right end of brow down to bottom-right, then hooks up-left
stroke([(238, 118), (238, 200), (232, 245), (218, 250)], width=7)
# hook flick going back into the character (up-left)
stroke([(218, 250), (208, 238)], width=6)

# Stroke 5: inner left short vertical — hangs from underside of brow
stroke([(115, 130), (112, 218)], width=6)

# Stroke 6: inner right short vertical
stroke([(175, 130), (172, 218)], width=6)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0225_而/01_而.png"
img.save(out)
print(f"wrote {out}")
