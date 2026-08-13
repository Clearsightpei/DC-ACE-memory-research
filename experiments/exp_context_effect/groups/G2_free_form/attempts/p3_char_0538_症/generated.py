"""
Render 症 (zhèng) — sickness radical 疒 (5 strokes) + 正 (5 strokes) = 10 strokes.

Frozen cohort 疒 rules applied (TIER-0 G / frozen_cohort.md):
  - 5-stroke 疒 decomposition: 点 / 横 / 长撇 / 内点 / 提
  - Inner 点 + 提 nested INSIDE the canopy triangle (wedge between
    横 above and 撇 to the left), not dangling on the 撇 stem
  - Body 正 tucked fully under the 撇's belly (shifted right, shrunk)
  - Component-touch rule (TIER-0 H): 正's top 一 overlaps beneath 撇
Calligraphic 4-move (TIER-0 F):
  - Teardrop taper via stroke helper (thin→thick per point widths)
  - Shoulder dabs at 折 joints (none needed here; 正 uses simple joins)
  - Bezier for 撇's bowed sweep
  - Hook flick — 正 has no hook; 疒 has no hook either
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, widths=None, width=6):
    """Draw a polyline with per-point width (taper). widths is a list
    matching pts, or None for uniform width."""
    n = len(pts)
    if widths is None:
        widths = [width] * n
    # segments
    for i in range(n - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        # sample line via ellipses for smoothness at width variation
        steps = max(2, int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5))
        for s in range(steps + 1):
            t = s / steps
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            r = (widths[i] + (widths[i + 1] - widths[i]) * t) / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def bez(p0, p1, p2, p3, n=50):
    """Cubic Bezier point list."""
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        pts.append((x, y))
    return pts


# --- 疒 canopy (top-left, forms L-frame) ---

# 1. 点 (small slanted dot at very top, on the横 line)
stroke([(112, 48), (128, 68)], widths=[3.0, 7.0])

# 2. 横 (top of frame — moderate length; must NOT bleed into 正's area)
stroke([(72, 88), (140, 84), (210, 90)], widths=[5.5, 6.0, 5.5])

# 3. 长撇 (long left-descending from RIGHT END of 横 down-left to bottom)
pie = bez((210, 90), (180, 150), (130, 215), (55, 270), n=60)
stroke(pie, widths=[7.5] * 20 + [7.0] * 20 + [5.0] * 15 + [2.0] * 6)

# 4. 内点 (inner dot — sits inside the canopy triangle, upper-left interior)
stroke([(95, 128), (112, 144)], widths=[3.0, 7.0])

# 5. 提 (small rising stroke lower-left interior, going up-right)
stroke([(82, 195), (125, 178)], widths=[7.0, 3.0])

# --- 正 (interior body, tucked fully under 撇's belly, right of inner ticks) ---
# 正 = 5 strokes: 横 (top), 竖 (short left), 横 (mid), 竖 (long center down), 横 (bottom long)
# Shrunk ~20% and shifted right so it packs under the canopy.

# 6. 横 (top short bar of 正 — clearly BELOW canopy 横)
stroke([(158, 145), (245, 145)], widths=[5.0, 6.0, 5.5])

# 7. 竖 (short vertical dropping from left of top bar)
stroke([(172, 145), (172, 188)], widths=[6.5, 5.5])

# 8. 横 (middle bar, shorter, starts from left 竖)
stroke([(172, 188), (225, 188)], widths=[5.0, 5.0])

# 9. 竖 (long central vertical — main axis of 正)
stroke([(200, 145), (200, 262)], widths=[7.0, 6.5])

# 10. 横 (bottom long bar — extends widest to close the character)
stroke([(150, 262), (200, 262), (270, 262)], widths=[5.5, 6.5, 5.5])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0538_症/01_症.png")
print("saved 01_症.png")
