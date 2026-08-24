# BANK_DEVIATION
# skipped: bu_char.py, min_dish.py
# reason: 盃 stacks 不 (top ~45%) over 皿 (bottom ~50%); both bank entries
#   are sized for solo full-canvas renders. Retry_1 fixes prior C: prior
#   皿 top-横折 started at x=105 leaving a gap above the left vertical —
#   here the top heng spans the full basin width (left-vertical top to
#   right-vertical top). Also strengthens 不's pie sweep to match GT.
# fresh_component: bu_top_for_stack_v2, min_bottom_for_stack_v2
#
# RETRY MEMORY CHECKLIST
# Q1 (errata): No dedicated 盃 errata entry; prior C was structural — 皿's
#   top gap and slightly off 不 proportions. Fix idea: close the top edge
#   of 皿 (heng from x=68 to x=232), widen 不 pie sweep, tighten shu.
# Q2 (form_catalog): Top-bottom-stack forms — top gets y=30..150,
#   bottom gets y=155..280. Base heng of 皿 extends beyond box.
# Q3 (helpers): No X-crossing / mirror-dot; per-stroke width is 皿-style
#   thin uniform (~6px) matching MMH GT thinness.
#
# TRAJECTORY DIFF
# Prior main (C):
#   - 皿 top-right 横折 started at x=105 → visible top-left gap above the
#     left vertical (should have closed the basin top).
#   - 不 dian started at x=180 y=80 — too close to shu; GT dian starts
#     further right (~x=185) and terminates lower-right around (230, 140).
#   - 不 pie ended at (60, 145) — reasonable but could sweep slightly
#     lower to match GT's tail.
# Fixes this retry:
#   - 皿 top: one continuous heng from x=68 to x=232 at y=170, then right
#     wall descends from x=232 to x=225 (slight inward slant).
#   - 不 dian: start (183, 82) → (228, 142), stronger tail.
#   - 不 pie: (150, 63) → (55, 148), slightly longer.

"""盃 (bēi, "cup") — 不 over 皿, 9 strokes total (4 + 5).
Retry #1 — fresh inline PIL, GT-aligned proportions.
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6


def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)


def bezier_taper(x0, y0, x1, y1, w_head, w_tail, bow_perp=-6.0, n=60):
    """Tapered quadratic bezier from (x0,y0) to (x1,y1) with perpendicular bow."""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = (x0 + x1) / 2.0 + perp_x * bow_perp
    my = (y0 + y1) / 2.0 + perp_y * bow_perp
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (bx, by)], fill=INK, width=wi)
            r = w / 2.0
            d.ellipse([bx - r, by - r, bx + r, by + r], fill=INK)
        prev = (bx, by)


# ============================================================
# TOP: 不 (y ~ 35..150)
# ============================================================

# Stroke 1: 横 (heng) — top horizontal, spans wide
line((48, 55), (252, 50), w=6)

# Stroke 2: 丿 (pie) — from just left of center down-left, tapered
bezier_taper(150, 58, 55, 148, w_head=7.5, w_tail=2.5, bow_perp=-7.0)

# Stroke 3: 丨 (shu) — short vertical from heng center downward
line((156, 58), (162, 140), w=6)

# Stroke 4: 丶 (dian) — right dot, sweeping down-right
bezier_taper(183, 82, 228, 142, w_head=3.0, w_tail=8.0, bow_perp=-4.0)


# ============================================================
# BOTTOM: 皿 (y ~ 170..278)
# ============================================================

# Stroke 1: left vertical (slight inward slant at bottom)
line((68, 172), (76, 258), w=6)

# Stroke 2: first inner short vertical
line((118, 178), (120, 258), w=6)

# Stroke 3: second inner short vertical
line((168, 178), (168, 258), w=6)

# Stroke 4: 横折 — top heng spans full basin (closing top-left gap),
# then right wall descends with slight inward slant.
line((72, 170), (232, 170), w=6)      # top heng
line((232, 170), (225, 258), w=6)     # right vertical

# Stroke 5: long bottom horizontal (extends beyond box)
line((32, 275), (272, 273), w=7)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G3_coords/attempts/p3_char_0466_盃__retry_1/01_盃.png"
)
print("saved")
