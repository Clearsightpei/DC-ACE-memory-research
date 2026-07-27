"""乔 (qiao) — 6 strokes.
Structure: 撇 (short top slant) + 横 (upper) + 撇 (long down-left) + 横 (lower)
           + 丿 (left leg) + 亅 (right hooked vertical).
G3 v8: inline PIL, thin uniform widths matching MMH GT.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
WID = 5  # thin like GT

def line(p0, p1, w=WID):
    d.line([p0, p1], fill="black", width=w)

def curve(pts, w=WID):
    # polyline for smooth-ish curve
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# 1. Short 撇 at top (small slant, ~35-degree, high up)
curve([(150, 60), (140, 68), (128, 82)])

# 2. Upper 横 (short-ish horizontal just under the top pie)
line((100, 100), (200, 92))

# 3. Long 撇 going down-left from around the upper horizontal
curve([(155, 95), (140, 130), (115, 165), (85, 200), (60, 230)])

# 4. Lower 横 (wider horizontal, midway)
line((70, 155), (240, 148))

# 5. Left leg — 丿 (short curving pie from lower horizontal down-left slightly)
curve([(140, 155), (135, 190), (125, 225), (115, 255)])

# 6. Right leg — 亅 vertical with hook at bottom
curve([(170, 155), (170, 190), (172, 225), (170, 255), (162, 258)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0226_乔/01_乔.png")
