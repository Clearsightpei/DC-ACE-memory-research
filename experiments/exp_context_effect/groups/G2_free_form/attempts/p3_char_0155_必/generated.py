"""
必 — 5 strokes
Stroke order:
  1. 卧钩 (lying hook)   — shallow smile-arc across the bottom, hook flicks up-left from right end
  2. 点 (dot) middle-top — inside the bowl
  3. 撇 (diagonal down-left) — long, sweeping through the character from upper-right to lower-left
  4. 点 (dot) left       — outside the bowl on the far left
  5. 点 (dot) right      — outside the bowl on the far right (short rightward flick)

Consulted memory:
  - form_catalog.md 卧钩-as-心-bowl-base: shallow concave-up bowl at bottom-middle;
    hook flicks up-and-left (~145°) from right end; do NOT close into oval.
  - sibling_signature_checklist TIER-0.B: 卧钩 flick UP-and-LEFT (~-145°).
  - form_catalog notes 必 shares the 卧钩 with 心 but has a long 撇 slashing through it.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_stroke(points, width_start=6, width_end=6):
    """Draw a variable-width stroke by dabbing circles along a polyline."""
    if len(points) < 2:
        return
    # accumulate length
    seg_lens = []
    total = 0.0
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        L = math.hypot(dx, dy)
        seg_lens.append(L)
        total += L
    step = 0.9
    dist = 0.0
    for i in range(len(points) - 1):
        L = seg_lens[i]
        if L == 0:
            continue
        n = max(1, int(L / step))
        for k in range(n + 1):
            t_local = k / n
            x = points[i][0] + (points[i + 1][0] - points[i][0]) * t_local
            y = points[i][1] + (points[i + 1][1] - points[i][1]) * t_local
            t_global = (dist + L * t_local) / total
            r = (width_start * (1 - t_global) + width_end * t_global) / 2.0
            d.ellipse([x - r, y - r, x + r, y + r], fill=INK)
        dist += L


def bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


# ---- Stroke 1: 卧钩 (lying hook) — shallow smile-arc at bottom, hook flicks up-left ----
# Bowl: wider, shallow, sitting lower on canvas
bowl = bezier((80, 210), (150, 275), (230, 210), n=60)
brush_stroke(bowl, width_start=5, width_end=9)
# Hook flick up-and-left from right end (~-145°) — clear, distinct
flick = [(230, 210), (218, 195), (210, 188)]
brush_stroke(flick, width_start=9, width_end=2)

# ---- Stroke 2: 点 middle-top (inside the bowl, well above belly, offset from 撇 path) ----
dot_mid = bezier((170, 120), (178, 138), (184, 158), n=25)
brush_stroke(dot_mid, width_start=3, width_end=9)

# ---- Stroke 3: 撇 — long sweeping diagonal from upper-right down through center to lower-left ----
# Start further right so it doesn't overlap dot_mid; end at lower-left below the bowl
pie = bezier((220, 55), (150, 175), (60, 275), n=70)
brush_stroke(pie, width_start=8, width_end=2)

# ---- Stroke 4: 点 far-left (outside the bowl, mid-left height) ----
dot_left = bezier((45, 160), (38, 185), (34, 215), n=25)
brush_stroke(dot_left, width_start=3, width_end=8)

# ---- Stroke 5: 点 far-right (short rightward flick, upper right area) ----
dot_right = bezier((235, 145), (255, 158), (275, 172), n=25)
brush_stroke(dot_right, width_start=3, width_end=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0155_必/01_必.png")
print("wrote 01_必.png")
