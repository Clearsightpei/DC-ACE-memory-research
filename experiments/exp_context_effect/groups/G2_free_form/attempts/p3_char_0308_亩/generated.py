"""Render 亩 (p3_char_0308) at 300x300.

亩 = 亠 (top: dot + long horizontal lid) + 田 (grid box below).
Composition: top-heavy 亠 lid wider than the 田 box; 田 sits centered below.

Precedents (own group PASSes):
- 亠 (attempts/p3_char_0020_亠/01_亠.png): dot near (145,90)-(165,128),
  long 横 at y~165 spanning x=46..258.
- 由 / 田-like (attempts/p3_char_0204_由/01_由.png): 8-px straight lines,
  square box left=90 right=210 top=130 bot=250.

For 亩 we compress vertically: 亠 lid occupies top ~third, 田 box below.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def brush_line(draw, pts, widths):
    for (x, y), w in zip(pts, widths):
        draw.ellipse([x - w, y - w, x + w, y + w], fill=BLACK)
    for (x1, y1), (x2, y2), w1, w2 in zip(pts[:-1], pts[1:], widths[:-1], widths[1:]):
        wm = max(1, int((w1 + w2) / 2))
        draw.line([(x1, y1), (x2, y2)], fill=BLACK, width=wm * 2)


# ---- Top 亠 ----
# Stroke 1: 点 (dot), thin->thick, tilted down-right, sits above the lid
p_start = (160, 45)
p_end = (180, 82)
N = 8
pts, widths = [], []
for i in range(N):
    t = i / (N - 1)
    x = p_start[0] + (p_end[0] - p_start[0]) * t
    y = p_start[1] + (p_end[1] - p_start[1]) * t
    w = 1.5 + 3.5 * t
    pts.append((x, y))
    widths.append(w)
brush_line(draw, pts, widths)

# Stroke 2: long 横 lid (widest stroke of the char), slight up-tilt, gentle mid-bow down
h_start = (35, 130)
h_end = (265, 122)
N = 50
hpts, hwidths = [], []
for i in range(N):
    t = i / (N - 1)
    x = h_start[0] + (h_end[0] - h_start[0]) * t
    bow = 3.0 * math.sin(math.pi * t)
    y = h_start[1] + (h_end[1] - h_start[1]) * t + bow
    w = 3.8 if (t < 0.04 or t > 0.96) else 2.6
    hpts.append((x, y))
    hwidths.append(w)
brush_line(draw, hpts, hwidths)
# 顿 dabs at ends
draw.ellipse([h_start[0] - 5, h_start[1] - 4, h_start[0] + 3, h_start[1] + 5], fill=BLACK)
draw.ellipse([h_end[0] - 4, h_end[1] - 3, h_end[0] + 5, h_end[1] + 5], fill=BLACK)

# ---- Bottom 田 (centered under lid, narrower than lid) ----
BW = 8
left, right = 85, 215
top, bot = 155, 275
cx = (left + right) // 2  # 150
cy = (top + bot) // 2     # 207

# Stroke: left vertical of box
draw.line([(left, top), (left, bot)], fill=BLACK, width=BW)

# 横折: top horizontal + right vertical (slight extension of top past corner is common)
draw.line([(left, top), (right, top)], fill=BLACK, width=BW)
draw.line([(right, top), (right, bot)], fill=BLACK, width=BW)

# Inner cross: vertical through center
draw.line([(cx, top), (cx, bot)], fill=BLACK, width=BW)
# Inner cross: horizontal through center
draw.line([(left, cy), (right, cy)], fill=BLACK, width=BW)

# Bottom horizontal (close box)
draw.line([(left, bot), (right, bot)], fill=BLACK, width=BW)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0308_亩/01_亩.png"
img.save(out_path)
print(f"wrote {out_path}")
