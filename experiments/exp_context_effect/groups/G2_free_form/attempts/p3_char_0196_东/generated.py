"""
东 (dōng) — 5 strokes
Order:
 1. 横 (short top horizontal)
 2. 撇 (short slant down-left from right side of top horizontal — the "折" tick)
 3. 横 (long middle horizontal)
 4. 竖钩 (vertical hook through center)
 5. 撇 (bottom-left dot/slant)
 6. 捺 (bottom-right dot/slant)

Note: MMH standard is 5 strokes; the top 横+撇 unit is one 横撇 (横 + 撇) but here
we render as two visible segments for clarity, in line with GT appearance.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
BRUSH = 6

def stroke(pts, width=BRUSH):
    d.line(pts, fill=INK, width=width, joint="curve")
    # round the endpoints
    r = width // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# 1. Top short 横 (a bit tilted up-right)
stroke([(110, 78), (185, 70)])

# 2. Small 撇 tick coming off the right end of the top 横, going down-left
stroke([(175, 68), (150, 105)])

# 3. Long middle 横 (slight upward slant, brush-broken feel by two segments)
stroke([(55, 145), (255, 132)])

# 4. 竖钩 — vertical through center, ending with UP-and-LEFT hook flick
stroke([(155, 55), (150, 240)])
# hook flick (UP-and-slightly-LEFT ~ -105°)
stroke([(150, 240), (135, 228)])

# 5. Bottom-left 撇 (dot-like short slant down-left)
stroke([(105, 220), (75, 260)])

# 6. Bottom-right 捺 (short slant down-right)
stroke([(195, 220), (240, 258)])

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0196_东/01_东.png"
img.save(out)
print("saved", out)
