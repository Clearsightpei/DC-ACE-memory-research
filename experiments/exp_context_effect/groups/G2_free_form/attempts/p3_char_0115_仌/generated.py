"""
仌 (bīng) — two 人 stacked vertically (an old form of 冰).
4 strokes: top 人 (撇+捺), bottom 人 (撇+捺), bottom larger.

# SIGNATURE CHECK (per sibling_signature_checklist.md):
#   target = 人 (applied twice, stacked)
#   bit = "apex SHARED at same y; both strokes throw outward; 捺 has thick foot"
#   Both 人s share apex; 捺 does NOT overhang (that would be 入).

From GT:
- Top 人: apex around (140, 55), 撇 sweeps down-left, 捺 sweeps down-right.
- Bottom 人: apex around (135, 155), larger; 撇 goes to ~(55, 285), 捺 to ~(240, 285).
- The two 人s are stacked; top is smaller, bottom is broader.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width_start=5, width_end=5, steps=40):
    """Draw a variable-width smooth stroke by dabbing circles along a polyline."""
    # Interpolate along the polyline
    total_len = 0
    segs = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        dx, dy = x2 - x1, y2 - y1
        L = (dx * dx + dy * dy) ** 0.5
        segs.append((x1, y1, x2, y2, L))
        total_len += L
    # Sample
    for s in range(steps + 1):
        t = s / steps
        target = t * total_len
        acc = 0
        for x1, y1, x2, y2, L in segs:
            if acc + L >= target:
                lt = (target - acc) / L if L > 0 else 0
                x = x1 + (x2 - x1) * lt
                y = y1 + (y2 - y1) * lt
                w = width_start + (width_end - width_start) * t
                r = w / 2
                d.ellipse([x - r, y - r, x + r, y + r], fill="black")
                break
            acc += L

# --- Top 人 ---
# 撇: from apex (140, 55) sweeping down-left, curving, ending ~(85, 165)
top_pie = [(142, 55), (130, 85), (115, 120), (95, 155), (78, 170)]
stroke(top_pie, width_start=6, width_end=3, steps=50)

# 捺: from near apex (145, 60) sweeping down-right, thickening, ending ~(200, 155)
top_na = [(145, 60), (160, 90), (180, 120), (200, 145), (215, 158)]
stroke(top_na, width_start=3, width_end=8, steps=50)

# --- Bottom 人 (broader; ~2/3 of canvas) ---
# 撇: apex (140, 155) sweeping down-left with slight curve, ending ~(35, 290)
bot_pie = [(142, 155), (115, 190), (85, 230), (55, 270), (35, 290)]
stroke(bot_pie, width_start=7, width_end=3, steps=60)

# 捺: from apex (145, 158) sweeping down-right, thickening toward foot ~(265, 288)
bot_na = [(145, 158), (175, 195), (205, 230), (235, 265), (265, 288)]
stroke(bot_na, width_start=3, width_end=10, steps=60)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0115_仌/01_仌.png")
