# p3_char_0148_书 — 书 (shū, "book"), 4-5 strokes.
# Fresh derivation matched to GT visual: a tall central vertical shaft
# dominating the character, a short 横折 at upper-left (heng bending
# down into a short shu that meets the top of the shaft), a wide middle
# 横 crossing the shaft, a right-side 竖折折钩-ish curve at bottom right,
# and a small dot on the upper right.
# Widths thin ~5 px MMH-style. Character occupies roughly y in [-110, +90],
# horizontally x in [-70, +70].
import math
from PIL import Image, ImageDraw


CANVAS_SIZE = 300


def _to_pixel(mx, my):
    return 150 + mx, 150 - my


def _line(t, x0, y0, x1, y1, width):
    a, b = _to_pixel(x0, y0)
    c, d = _to_pixel(x1, y1)
    t.line([(a, b), (c, d)], fill=(0, 0, 0), width=width)


def _shu(t, xc, yc, half_len, thickness):
    _line(t, xc, yc + half_len, xc, yc - half_len, thickness)


def _heng(t, xc, yc, half_len, thickness):
    _line(t, xc - half_len, yc, xc + half_len, yc, thickness)


def _bezier(t, x0, y0, mx, my, x1, y1, w_head, w_tail, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _dian(t, x0, y0, x1, y1, w_head, w_tail):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    bow_perp = -2.0
    mx = (x0 + x1) / 2.0 + perp_x * bow_perp
    my = (y0 + y1) / 2.0 + perp_y * bow_perp
    _bezier(t, x0, y0, mx, my, x1, y1, w_head, w_tail, n=30)


def draw_shu_char(t, ox=0.0, oy=0.0, scale=1.0):
    """书 — matched to GT visual: tall central shaft + short 横折 top-left
    + wide middle heng + right-side curve + dot upper-right. Thin ~5 px."""

    # Stroke 1: 横折 at upper-left — short horizontal bending down into a
    # short vertical that meets the top region of the central shaft.
    _heng(t, ox + (-38) * scale, oy + 55 * scale, 25 * scale, thickness=5)
    _shu(t, ox + (-13) * scale, oy + 30 * scale, 25 * scale, thickness=5)

    # Stroke 2: Central 竖 with hook at bottom — the tall dominant vertical
    # of 书. Runs from top (~y=+80) down to (~y=-110), long shaft.
    _shu(t, ox + (-5) * scale, oy + (-15) * scale, 95 * scale, thickness=5)
    # Small left-curling hook at very bottom
    _bezier(t,
            ox + (-5) * scale, oy + (-110) * scale,
            ox + (-8) * scale, oy + (-108) * scale,
            ox + (-15) * scale, oy + (-100) * scale,
            w_head=5.0, w_tail=2.0, n=15)

    # Stroke 3: Middle 横 — wide horizontal bar crossing the shaft.
    _heng(t, ox + 5 * scale, oy + (-15) * scale, 70 * scale, thickness=5)

    # Stroke 4: Right side 竖折折钩 — vertical starting from the middle heng
    # level going down, then curving right, then up with a hook.
    # Segment A: short vertical down from crossing point on right side
    _shu(t, ox + 35 * scale, oy + (-35) * scale, 20 * scale, thickness=5)
    # Segment B: curve bottom — comes down further and curls right
    _bezier(t,
            ox + 35 * scale, oy + (-55) * scale,
            ox + 40 * scale, oy + (-85) * scale,
            ox + 60 * scale, oy + (-85) * scale,
            w_head=5.0, w_tail=5.0, n=30)
    # Segment C: upward hook at end
    _bezier(t,
            ox + 60 * scale, oy + (-85) * scale,
            ox + 60 * scale, oy + (-70) * scale,
            ox + 50 * scale, oy + (-60) * scale,
            w_head=5.0, w_tail=2.0, n=15)

    # Stroke 5: 点 (dian) on upper right, slanting down-right
    _dian(t,
          ox + 30 * scale, oy + 55 * scale,
          ox + 50 * scale, oy + 30 * scale,
          w_head=3.0 * scale, w_tail=8.0 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_shu_char(draw, ox=0, oy=0, scale=1.0)
    out_path = ("/Users/peilinwu/Documents/AI memory research/experiments/"
                "exp_context_effect/groups/G3_coords/attempts/"
                "p3_char_0148_书/01_书.png")
    img.save(out_path)
    print(f"Saved: {out_path}")
