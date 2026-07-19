# p1_stroke_31_竖折折钩 — 竖折折钩 (shu zhe zhe gou)
# Structure: vertical DOWN -> horizontal RIGHT (折) -> vertical DOWN (折)
#            -> hook up-and-left at the bottom.
# Used in characters like 马, 与, 号. Four segments joined at three corners
# plus a terminal flick. Coord math convention (center origin, +y up).

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _tapered_segment(t, p0_math, p1_math, w0, w1, steps=20, ox=0, oy=0):
    """Draw a straight tapered line in math coords."""
    x0, y0 = p0_math
    x1, y1 = p1_math
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        pa = _to_pixel(ox + xa, oy + ya)
        pb = _to_pixel(ox + xb, oy + yb)
        t.line([pa, pb], fill=(0, 0, 0), width=w)


def _blob(t, p_math, r_px, ox=0, oy=0):
    px, py = _to_pixel(ox + p_math[0], oy + p_math[1])
    t.ellipse([px - r_px, py - r_px, px + r_px, py + r_px], fill=(0, 0, 0))


def draw_shu_zhe_zhe_gou(t, ox=0, oy=0, scale=1.0):
    """竖折折钩 = ▏ + ▁ + ▕ + hook flick up-left.

    Layout (math coords, canvas center 0,0):
      A  (-60,  90)  top of first vertical
      B  (-60, -10)  bottom of first vertical / left of horizontal
      C  ( 60, -10)  right of horizontal / top of second vertical
      D  ( 60, -70)  bottom of second vertical (base for hook)
      hook tip ( 20, -50)  up and left of D
    """
    A = (-60 * scale,  90 * scale)
    B = (-60 * scale, -10 * scale)
    C = ( 60 * scale, -10 * scale)
    D = ( 60 * scale, -70 * scale)

    ink = 12
    # First vertical (shu) — uniform width.
    _tapered_segment(t, A, B, ink, ink, steps=22, ox=ox, oy=oy)
    # Horizontal (heng) — uniform width, slight thicken to right end for 折 turn.
    _tapered_segment(t, B, C, ink, ink + 1, steps=22, ox=ox, oy=oy)
    # Second vertical — uniform ink.
    _tapered_segment(t, C, D, ink, ink, steps=18, ox=ox, oy=oy)

    # 顿笔 corner blobs at B, C, D to hide miters and give brush turns.
    r_corner = int(round((ink / 2 + 1) * scale))
    _blob(t, B, r_corner, ox=ox, oy=oy)
    _blob(t, C, r_corner, ox=ox, oy=oy)
    _blob(t, D, r_corner + 1, ox=ox, oy=oy)

    # Hook: up-and-left flick from D. Tapered wide->needle.
    hook_base = (D[0] + 2 * scale, D[1] - 2 * scale)  # slight overshoot below corner
    hook_tip  = (D[0] - 26 * scale, D[1] + 22 * scale)  # up-left in math coords
    hsteps = 14
    for i in range(hsteps):
        u0 = i / hsteps
        u1 = (i + 1) / hsteps
        xa = hook_base[0] + (hook_tip[0] - hook_base[0]) * u0
        ya = hook_base[1] + (hook_tip[1] - hook_base[1]) * u0
        xb = hook_base[0] + (hook_tip[0] - hook_base[0]) * u1
        yb = hook_base[1] + (hook_tip[1] - hook_base[1]) * u1
        w = max(1, int(round((11 - 9 * u0) * scale)))
        pa = _to_pixel(ox + xa, oy + ya)
        pb = _to_pixel(ox + xb, oy + yb)
        t.line([pa, pb], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_shu_zhe_zhe_gou(draw, ox=0, oy=0, scale=1.0)
    out_path = __file__.rsplit("/", 1)[0] + "/01_竖折折钩.png"
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
