# p2_radical_023_卩 — coord-format G3 attempt.
#
# 卩 = 2画 radical: 横折钩 (top-right, small, D-shape) + 竖 (long vertical, center-left).
#
# GT analysis (300x300, math-coord, center origin +y up):
#   - The 竖 dominates: a long vertical descending from mid-height (y≈+80)
#     down past bottom (y≈-130), positioned slightly left of center (x≈-15).
#   - The 横折钩 sits in the upper-right: a short horizontal head starts
#     near the 竖's top and turns down into a short vertical with a small
#     hook flicking up-left at its base. Compact D-shape.
#
# Bank usage (TR1-TR7 compliant):
#   - draw_shu(ox=-15, oy=-25, scale=1.05): center at (-15,-25), half_len=105.
#     Top at y=+80, bottom at y=-130. Scales up ~5% (standalone half_len=100
#     -> 105). scale is within P4's uniform-width range.
#   - draw_heng_zhe_gou at scale=0.38: primitive is TOO big at default
#     (spans ~170 wide, 130 tall). Radical needs ~50 wide, 65 tall.
#     scale 0.38 -> ~65 wide x ~50 tall, close to target.
#     BUT TR5 warns scale<0.4 breaks brushwork. So INLINE the 横折钩
#     recipe scaled to fit rather than call the primitive.
#
# Composition math (math-coord):
#   竖 top pixel: math (-15, +80). PIL (135, 70).
#   竖 bottom pixel: math (-15, -130). PIL (135, 280).
#   横折钩 head start: math (-10, +75). PIL (140, 75).
#   横折钩 corner: math (+40, +75). PIL (190, 75).
#   横折钩 vertical bottom: math (+40, +20). PIL (190, 130).
#   hook flick tip: math (+22, +30). PIL (172, 120).
#
# Sanity check (TR7):
#   - 竖 top (y=+80) is 2px above 横折钩 head (y=+75): shu extends slightly
#     higher, which matches GT (shu head visible above the 横折钩 head).
#   - Horizontal head at y=+75 starts near shu's shaft (x=-10) and extends
#     right to x=+40. The horizontal actually TOUCHES the shu's left edge
#     so the D-shape's top-left corner meets the shu. Good.
#   - vertical portion of 横折钩 descends from y=+75 to y=+20, sitting to
#     the RIGHT of shu. Compact D-shape, correct orientation.
#   - hook at bottom of vertical flicks up-and-left (P1). OK.
#   - All content within 300x300 with >15px margin. OK.

from PIL import Image, ImageDraw
import sys, os

CANVAS = 300
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from shu import draw_shu  # noqa: E402


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_segment(draw, p0, p1, w0, w1, steps=20, ox=0, oy=0):
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


def draw_heng_zhe_gou_small(draw, ox=0, oy=0):
    """Inlined small 横折钩 for the top-right of 卩.
    GT shows a rounded D-shape (curved outer edge), not a sharp right angle.
    So the vertical is drawn as a bezier bowing outward to the right."""
    # horizontal head from (-10, +75) to (+40, +75) — short and flat
    p_h_start = (-10, 75)
    p_corner = (40, 75)
    p_v_end = (30, 20)

    # horizontal head
    _tapered_segment(draw, p_h_start, p_corner, 8, 10, steps=18, ox=ox, oy=oy)

    # corner blob (顿笔) at the turn — P6
    cx, cy = _to_pixel(ox + p_corner[0], oy + p_corner[1])
    r = 5
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # vertical as a bezier bowing slightly rightward (rounded D-shape)
    # Bezier: P0=corner, P1=(52, 50) control, P2=v_end
    def bezier_pt(u, p0, p1, p2):
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        return (x, y)

    ctrl = (52, 50)
    steps = 24
    prev = p_corner
    for i in range(1, steps + 1):
        u = i / steps
        curr = bezier_pt(u, p_corner, ctrl, p_v_end)
        w = int(10 - 1.5 * u)
        w = max(1, w)
        _tapered_segment(draw, prev, curr, w, w, steps=2, ox=ox, oy=oy)
        prev = curr

    # hook up-and-left (P1) from vertical end
    h_base = (p_v_end[0] + 1, p_v_end[1] + 2)
    h_tip = (p_v_end[0] - 14, p_v_end[1] + 14)
    _tapered_segment(draw, h_base, h_tip, 9, 2, steps=12, ox=ox, oy=oy)

    # small base blob
    bx, by = _to_pixel(ox + p_v_end[0], oy + p_v_end[1])
    br = 5
    draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 竖 (long vertical) — center at (-15, -25), half_len=105 (scale 1.05).
    # Head at math y=+80, tail at math y=-130.
    draw_shu(draw, ox=-15, oy=-25, scale=1.05)

    # 横折钩 inlined (small, top-right of 卩)
    draw_heng_zhe_gou_small(draw, ox=0, oy=0)

    out_path = os.path.join(os.path.dirname(__file__), "01_卩.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
