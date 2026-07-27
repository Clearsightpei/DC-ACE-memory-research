"""
队 (duì) — 4 strokes total
Left: 阝 (left ear) = 横撇弯钩 (ear-lobe D-shape) + 竖
Right: 人 = 撇 + 捺

Revision: rounder D-shaped ear-lobe; splay 人 more widely with a
proper diagonal 撇 and a broader 捺 sweeping to bottom-right.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def polyline(points, width=6):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill="black", width=width)
    for p in points:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# --- 阝 (left ear) ---
# Stroke 1: 横撇弯钩 — a D-shaped lobe. Start upper-left, small 横
# to the right, then curve down-right (belly), curve back left-down,
# close near the 竖 line with a small hook.
lobe = [
    (55, 85),   # start (top of lobe)
    (85, 82),   # small 横 to right
    (100, 95),  # 折 down-right, belly point
    (100, 120), # belly
    (90, 145),  # curve back left-down
    (70, 155),  # arrive near 竖 line
    (78, 148),  # small hook up-left
]
polyline(lobe, width=6)

# Stroke 2: 竖 — starts at top-left (around 55, 80) and drops long
shu = [(55, 80), (55, 275)]
polyline(shu, width=8)

# --- 人 (right side) ---
# In GT: apex mid-upper, 撇 shorter down-left, 捺 very long down-right
# Apex around (185, 75)
# Stroke 3: 撇 — apex (185, 75) sweeps down-left, curving slightly
pie = [(185, 75), (170, 115), (150, 160), (130, 205), (115, 245)]
polyline(pie, width=6)

# Stroke 4: 捺 — starts near apex (183, 78), sweeps down-right
# with widening foot toward bottom-right corner
na_segments = [
    ((183, 78), (200, 115), 4),
    ((200, 115), (225, 160), 5),
    ((225, 160), (250, 215), 7),
    ((250, 215), (285, 275), 10),
]
for (p1, p2, w) in na_segments:
    d.line([p1, p2], fill="black", width=w)
# Broaden the 捺 foot
d.line([(275, 260), (290, 278)], fill="black", width=12)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0146_队/01_队.png")
print("saved")
