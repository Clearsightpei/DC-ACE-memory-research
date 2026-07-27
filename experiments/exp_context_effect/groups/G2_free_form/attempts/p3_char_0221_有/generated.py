"""
有 (yǒu) — 6 strokes: 横, 撇, 横折钩 (outer 月), 竖 (left of 月), 横, 横
Layout: top ナ-like (横+撇), then 月 body hanging below-right from the 横.
Revised once: tightened margins, thinner strokes, moved 撇 origin left.
Hook on 横折钩 flicks UP-LEFT.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

def bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
        y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
        pts.append((x, y))
    return pts

# Stroke 1: 横 (top horizontal), slight rise right
stroke([(50, 100), (250, 88)], width=6)

# Stroke 2: 撇 — starts left-of-center on 横, curves down to lower-left
stroke(bezier((130, 65), (95, 165), (45, 275)), width=6)

# 月 body — sits to the right, hanging from 横
# Stroke 3: 横折钩 — top horizontal + right vertical + hook up-left
top_left = (128, 135)
top_right = (238, 135)
bot_right = (222, 268)
stroke([top_left, top_right, (240, 200), bot_right], width=6)
# Hook flick up-left
hx, hy = bot_right
stroke([(hx, hy), (hx - 16, hy - 12)], width=6)

# Stroke 4: 竖 — left side of 月 (short vertical)
stroke([(132, 148), (132, 262)], width=6)

# Stroke 5: 横 inside (upper)
stroke([(146, 178), (222, 178)], width=5)

# Stroke 6: 横 inside (lower)
stroke([(146, 220), (222, 220)], width=5)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0221_有/01_有.png"
img.save(out)
print(f"Saved {out}")
