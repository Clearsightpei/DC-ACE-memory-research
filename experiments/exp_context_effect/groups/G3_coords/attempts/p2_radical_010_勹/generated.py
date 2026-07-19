# p2_radical_010_勹 (2 strokes: 撇 + 横折钩)
# G3 coord-format render.
#
# Composition analysis vs GT:
# - 撇: short tapered slash upper-left. Head ~(180, 100 PIL), tail ~(115, 155 PIL).
# - 横折钩: horizontal at PIL y=115 x=95->200, then vertical down x=200 y=115->245,
#   then hook flicks up-left ending near (175, 220 PIL).
#
# Bank options:
#   * pie primitive (default head (215,60)->(105,235)) is too long for a small
#     radical-slot 撇. Applied scale=0.42 with a small offset works dimensionally.
#   * heng_zhe_gou has aspect (170w x 130h) but 勹 needs (~105w x 130h). Uniform
#     scale would force a compromise (per TR5, inline the recipe instead of
#     stretching), so 横折钩 is INLINED here to hit the target dimensions.

from PIL import Image, ImageDraw
import sys, os

# Import the pie primitive from the success bank for the 撇 stroke.
_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, _BANK)
from pie import draw_pie  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_segment(d, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        pa = _to_pixel(xa, ya)
        pb = _to_pixel(xb, yb)
        d.line([pa, pb], fill=(0, 0, 0), width=w)


def _tapered_bezier(d, p0, pc, p1, w0, w1, steps=40):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        px, py = _to_pixel(bx, by)
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


# =============================================================================
# STROKE 1: 撇 — short upper slash (revised)
# =============================================================================
# TR6 record (REVISION 1):
# Pass-1 placed 撇 head at PIL (177, 108) - too far right, crossing the horizontal.
# In GT, 撇's head sits ABOVE the horizontal's left third at ~PIL (150, 80) and
# sweeps down-left ending near ~PIL (105, 130).
#   Target head math: (0, 70). Target tail math: (-45, 20).
# pie primitive default: head (65, 90) -> tail (-45, -85). scale=0.35 gives
# head (22.75, 31.5) -> tail (-15.75, -29.75). To hit target head (0, 70):
#   ox = 0 - 22.75 = -23,  oy = 70 - 31.5 = +38
# Sanity: scaled tail lands at (-15.75 - 23, -29.75 + 38) = (-38.75, 8.25) math
#   -> PIL (111, 142). GT tail ~PIL (105, 130). Close enough.
draw_pie(draw, ox=-23, oy=38, scale=0.35)

# =============================================================================
# STROKE 2: 横折钩 — INLINED (aspect mismatch with bank primitive)
# =============================================================================
# TR6 record: inlined per TR5. Target endpoints in math coords:
#   horizontal start: PIL (95, 115)  -> math (-55,  35)
#   corner:           PIL (200, 115) -> math ( 50,  35)
#   vertical end:     PIL (200, 245) -> math ( 50, -95)
#   hook tip:         PIL (177, 220) -> math ( 27, -70)

p_h_start = (-55, 35)
p_corner = (50, 35)
p_v_end = (50, -95)

# Horizontal segment (slight thickening left->right, like 横).
_tapered_segment(draw, p_h_start, p_corner, w0=8, w1=11, steps=28)

# 顿笔 blob at the corner (P6).
cx_p, cy_p = _to_pixel(*p_corner)
r_corner = 7
draw.ellipse([cx_p - r_corner, cy_p - r_corner, cx_p + r_corner, cy_p + r_corner], fill=(0, 0, 0))

# Vertical segment — very slight inward curve (bow left) to give 勹's rounded feel.
# Use a bezier control point pulled slightly left of the corner->end chord midpoint.
mid_control = ((p_corner[0] + p_v_end[0]) / 2 - 6, (p_corner[1] + p_v_end[1]) / 2)
_tapered_bezier(draw, p_corner, mid_control, p_v_end, w0=12, w1=10, steps=32)

# Base blob at the vertical's terminus (顿笔 before hook).
bx_p, by_p = _to_pixel(*p_v_end)
r_base = 6
draw.ellipse([bx_p - r_base, by_p - r_base, bx_p + r_base, by_p + r_base], fill=(0, 0, 0))

# Hook: flick up-and-left from base. P1/P9: hook shares pixels with shaft tail.
h_base = (p_v_end[0] + 1, p_v_end[1] + 2)
h_tip = (p_v_end[0] - 23, p_v_end[1] + 25)
_tapered_segment(draw, h_base, h_tip, w0=10, w1=2, steps=18)

# Save.
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_010_勹/01_勹.png"
img.save(out_path)
print(f"Wrote {out_path}")
