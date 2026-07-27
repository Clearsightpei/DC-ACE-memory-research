"""
夂 (zhi) — 3-stroke radical/character.
Structure per errata p2_radical_081_夂 + form_catalog 捺 right-leg:
  1. short 撇 top-left (~50 px)
  2. short 横撇 crossing the 撇 mid-height (short 横 shoulder + short 撇 tail)
  3. dominant 捺 sweeping down-right with broad terminal foot (~150 px)

Silhouette: compact "each" shape, 捺 dominates.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def brush_stroke(pts, r_start=5, r_end=5, steps=None):
    """Draw a tapered brush along polyline pts by dabbing circles."""
    if steps is None:
        steps = 60
    # sample along polyline by cumulative arc-length
    seg_lens = []
    total = 0.0
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        L = (dx * dx + dy * dy) ** 0.5
        seg_lens.append(L)
        total += L
    if total == 0:
        return
    for s in range(steps + 1):
        t = s / steps
        target = t * total
        acc = 0.0
        px, py = pts[0]
        for i, L in enumerate(seg_lens):
            if acc + L >= target:
                u = (target - acc) / L if L > 0 else 0
                px = pts[i][0] + u * (pts[i + 1][0] - pts[i][0])
                py = pts[i][1] + u * (pts[i + 1][1] - pts[i][1])
                break
            acc += L
        r = r_start + (r_end - r_start) * t
        draw.ellipse((px - r, py - r, px + r, py + r), fill="black")


# Stroke 1: short 撇 top-left. Starts upper-mid, sweeps down-left more diagonally.
# Length ~55 px. Thin start, slight taper to thin end.
brush_stroke(
    [(155, 72), (140, 88), (125, 105), (115, 118)],
    r_start=3.5, r_end=2.0, steps=40,
)

# Stroke 2: 横撇 — short 横 shoulder that turns into a 撇 tail crossing the body.
# 横 part: from left of stroke-1 tip, going right ~55 px.
# Then shoulder dab, then 撇 tail sweeping down-left through the character body.
# Shoulder at (~205, 108). Tail sweeps to (~95, 195) — crosses the coming 捺.
brush_stroke(
    [(148, 105), (175, 105), (200, 108)],  # 横 lid
    r_start=3.5, r_end=4.5, steps=30,
)
# shoulder emphasis
draw.ellipse((200 - 5, 108 - 5, 200 + 5, 108 + 5), fill="black")
# 撇 tail from shoulder down-left
brush_stroke(
    [(200, 110), (180, 135), (150, 165), (115, 195), (85, 220)],
    r_start=4.5, r_end=2.0, steps=55,
)

# Stroke 3: dominant 捺 sweeping down-right ending in a flat horizontal foot.
# Starts thin near the 横撇 shoulder area (~150, 128), curves down-right,
# then flattens into a nearly horizontal terminal (per GT: broad flat foot).
brush_stroke(
    [(150, 128), (175, 155), (200, 180), (225, 200), (245, 215)],
    r_start=2.5, r_end=6.5, steps=60,
)
# flat terminal foot — extends horizontally to the right
brush_stroke(
    [(245, 215), (260, 218), (275, 220), (285, 220)],
    r_start=6.5, r_end=3.0, steps=25,
)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0070_夂/01_夂.png"
img.save(out_path)
print(f"wrote {out_path}")
