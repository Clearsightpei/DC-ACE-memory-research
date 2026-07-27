# 乡 (xiang) — 3 strokes. Structurally similar to 纟 (si_zi_pang):
# two 撇折 hooks stacked, then a long curved 撇 sweep at bottom
# (rather than 纟's horizontal 提). Adapting si_zi_pang's hook helper
# and replacing the final 提 with a downward-sweeping curved 撇.

from PIL import Image, ImageDraw

CANVAS = 300


def _to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                         fill=(0, 0, 0))
        prev = pt


def _draw_pie_zhe_hook(draw, cx, cy, size, ink=7):
    # 撇 stroke: diagonal down-left ending at (cx, cy)
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    # 折 stroke: right-and-slightly-down from the turn point
    h0 = (cx, cy)
    h2 = (cx + size * 1.7, cy + size * 0.55)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.1)
    _tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5,
                    n=40, head_ramp=0.05)
    r = ink * 0.75
    px, py = _to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def _draw_long_pie(draw, x_start, y_start, x_end, y_end, ink=8):
    """Long curved 撇 sweeping down-left, tapered."""
    p0 = (x_start, y_start)
    p2 = (x_end, y_end)
    # Bow the curve slightly rightward (concave to the right)
    mid_x = (p0[0] + p2[0]) / 2 + 15
    mid_y = (p0[1] + p2[1]) / 2 + 5
    p1 = (mid_x, mid_y)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=1.5, n=60, head_ramp=0.08)


def _draw_pie_zhe_with_sweep(draw, cx, cy, size, sweep_len_x, sweep_len_y, ink=8):
    """撇折 where the second (折→撇) stroke sweeps down-left in a long curve
    (used for bottom stroke of 乡)."""
    # 撇 stroke: diagonal down-left to (cx, cy)
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    # Long curved sweep starting at turn: goes right briefly then down-left
    h0 = (cx, cy)
    h2 = (cx + sweep_len_x, cy + sweep_len_y)
    # Control point bows the sweep — first go right/down, then curl left/down
    h1 = (cx + size * 1.2, cy - size * 0.1)
    _tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5,
                    n=60, head_ramp=0.05)
    r = ink * 0.75
    px, py = _to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_xiang(t, ox=0.0, oy=0.0, scale=1.0):
    """乡 (3 strokes). Three 撇折 stacked vertically; the bottom has a
    long curved sweep instead of a short horizontal turn."""
    # Top hook — smallest, upper region
    _draw_pie_zhe_hook(t, cx=ox + 5 * scale, cy=oy + 75 * scale,
                       size=18 * scale, ink=5)
    # Middle hook — slightly larger, shifted left-down
    _draw_pie_zhe_hook(t, cx=ox + -8 * scale, cy=oy + 20 * scale,
                       size=22 * scale, ink=6)
    # Bottom 撇折 with long down-left sweep
    _draw_pie_zhe_with_sweep(t,
                             cx=ox + -22 * scale, cy=oy + -35 * scale,
                             size=24 * scale,
                             sweep_len_x=-50 * scale,
                             sweep_len_y=-75 * scale,
                             ink=7)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_xiang(draw)
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_乡.png")
    img.save(out)
    print(f"Saved {out}")
