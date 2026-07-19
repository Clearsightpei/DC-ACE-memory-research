# p2_radical_059_门 — G3 coord-bank attempt.
#
# 门 (mén) — 3-stroke radical:
#   Stroke 1: 点 (dot) at top-left, above the left vertical.
#   Stroke 2: 竖 (left vertical) — descends from below the dot to the bottom.
#   Stroke 3: 横折钩 — horizontal top spanning right portion, descending
#            to a hook up-left at the bottom-right.
#
# Composition plan (300x300 canvas, math coords, center = (150,150), +y up):
#   - Dot: small, top-left. Center around (-55, +75). Small scale ~0.5.
#     Uses inlined mini-dot recipe (bank dian is too heavy at scale 1.0).
#   - Left 竖: center around (-45, -10), scale ~0.85 (so span ~170 px).
#     Top around y=+75, bottom around y=-95. Deliberately does NOT
#     touch the dot (there's a small gap in the GT).
#   - Right 横折钩: horizontal top from x=-25 to x=+65 at y=+80, then
#     descending vertical to y=-95, then hook up-left.
#     Bank primitive default: h_start(-90, 60), corner(80, 60), v_end(80, -70).
#     For 门 we want a shorter horizontal (starts near center, not far left)
#     and taller vertical. TR5 says inline if primitive doesn't fit — the
#     bank primitive is symmetric around center, but we want the horizontal
#     to start well right of center. Inlining recipe with adjusted endpoints.
#
# All coord numbers below are deliberate placements (TR1-TR7).

from PIL import Image, ImageDraw
import os
import sys

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _tapered_segment(draw, p0, p1, w0, w1, steps=24, ox=0, oy=0):
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
        pa = _to_pixel(ox + xa, oy + ya)
        pb = _to_pixel(ox + xb, oy + yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


# Import bank primitive shu for the left vertical.
# TR6: record transform explicitly.
# shu's canonical unit: 200 px length at scale 1.0, thickness 12, from y=+100
# (top) to y=-100 (bottom) around center (ox, oy).
# For 门 left 竖: we want top around y=+75, bottom around y=-95.
# Center at oy = (+75 + -95)/2 = -10. Half-length = (75-(-95))/2 = 85.
# So scale = 85/100 = 0.85. ox = -45 (left column).
SUCCESS_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, SUCCESS_BANK)
from shu import draw_shu  # noqa: E402


def draw_dot_small(draw, ox, oy, scale=1.0):
    """Small 点 for 门's top-left dot.
    Inlined variant of bank dian — smaller, less tail-heavy, tilted more.
    Head thin at upper-right, tail heavy at lower-left (dot slants
    down-left in 门's GT: shape looks like a comma leaning left)."""
    # Actually looking at GT again: the dot is a short diagonal from
    # upper-right to lower-left area — a 短撇-like flick.
    # Head at upper-right (+8, +12), tail at lower-left (-10, -10).
    x0, y0 = 8.0 * scale, 12.0 * scale
    x1, y1 = -10.0 * scale, -10.0 * scale
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    n_segments = 24
    thickness_head = max(1, 3.0 * scale)
    thickness_tail = max(1, 9.0 * scale)
    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        if prev_pt is not None:
            w = thickness_head * (1 - u) + thickness_tail * u
            w_int = max(1, int(round(w)))
            draw.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_heng_zhe_gou_inline(draw, ox=0, oy=0):
    """Inlined 横折钩 for 门's right side.
    Horizontal top: from (-25, +80) to (+65, +80). Then corner blob.
    Vertical: from (+65, +80) to (+65, -95). Then hook up-left.
    (TR5 — bank primitive was tuned for symmetric standalone; 门 needs
    asymmetric placement, so inline the recipe.)"""
    p_h_start = (-25, 80)
    p_corner = (65, 80)
    p_v_end = (65, -95)

    # Horizontal top — moderate uniform-ish taper.
    _tapered_segment(draw, p_h_start, p_corner, 10, 11, steps=28, ox=ox, oy=oy)

    # Corner blob (顿笔)
    r_corner = 7
    cx, cy = _to_pixel(ox + p_corner[0], oy + p_corner[1])
    draw.ellipse([cx - r_corner, cy - r_corner, cx + r_corner, cy + r_corner], fill=(0, 0, 0))

    # Vertical descent
    _tapered_segment(draw, p_corner, p_v_end, 11, 10, steps=32, ox=ox, oy=oy)

    # Hook: up-and-left from vertical's base. Tapered to a needle tip
    # (P1: hook must be a tapered short line pointing UP-LEFT, not a
    # blob). Longer, thinner, no terminal blob so it doesn't read as
    # an arrowhead.
    h_base = (p_v_end[0] + 1, p_v_end[1] + 2)
    h_tip = (p_v_end[0] - 24, p_v_end[1] + 26)
    _tapered_segment(draw, h_base, h_tip, 10, 1, steps=20, ox=ox, oy=oy)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: 点 (dot), top-left, sits above/left of the 竖.
    # Center around (-50, +85) in math coords. Slightly larger scale
    # for visibility (GT dot is prominent).
    draw_dot_small(draw, ox=-50, oy=85, scale=1.25)

    # Stroke 2: 竖 (left vertical). shu default half_len=100.
    # Target: top y=+75, bottom y=-95, center y=-10, half_len=85 → scale=0.85.
    # ox=-45 (left column).
    draw_shu(draw, ox=-45, oy=-10, scale=0.85)

    # Stroke 3: 横折钩 (right side). Inlined for asymmetric placement.
    draw_heng_zhe_gou_inline(draw, ox=0, oy=0)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_门.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
