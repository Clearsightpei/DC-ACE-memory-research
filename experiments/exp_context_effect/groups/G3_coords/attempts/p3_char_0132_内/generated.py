# p3_char_0132_内 — G3 coord attempt
# 内 = 竖 (left) + 横折钩 (top+right envelope with hook) + 撇 + 点 (人 inside)
# Composition uses bank primitives with deliberate (ox, oy, scale) per TR1-TR3.

import os
import sys
from PIL import Image, ImageDraw

# Locate success bank
BASE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(BASE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from shu import draw_shu  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402
from dian import draw_dian  # noqa: E402

CANVAS = 300


def draw_nei(t, ox=0.0, oy=0.0, scale=1.0):
    """内 = box (竖 left + 横折钩 top-right) + 人 inside (撇 + 点)."""
    # --- Envelope box ---
    # Left 竖: from y ~ +65 down to y ~ -100. Length ~165 -> scale ~0.83.
    # Canonical shu length = 200. We want ~165 -> scale = 0.83.
    # x offset: left wall at x = -60.
    draw_shu(t, ox=ox + (-60) * scale, oy=oy + (-17) * scale, scale=0.83 * scale)

    # Top+right 横折钩:
    # canonical h_start=(-90,60), corner=(80,60), v_end=(80,-70) at scale 1.
    # We want horizontal from x=-60 to x=+60 at y=+65; vertical to y=-95; hook.
    # Horizontal width needed: 120. Canonical h_start->corner span=170 -> scale_h=0.71.
    # Vertical drop needed: 160. Canonical corner->v_end span=130 -> scale_v=1.23.
    # Compromise: use scale=0.75 and translate. Actually use two calls awkward;
    # single call with scale 0.75 gives h-span=127, v-span=97 — v too short.
    # Better: use scale=0.75 but this envelope shape is uneven. Try scale=0.78.
    # At scale=0.78: h_start=(-70, 47), corner=(62, 47), v_end=(62, -55).
    # After translation (dx, dy): want corner ~ (+60, +65) and v_end ~ (+60, -95).
    # corner y: 47 + dy = 65 -> dy = 18. v_end y: -55 + 18 = -37. Too short (want -95).
    # The canonical vertical is only 130 units vs needed 160.
    # Solution: draw envelope manually with tapered helpers rather than force scale.
    # But per bank principle, we use the primitive with best fit and accept mild proportion mismatch.
    # OR: draw envelope inline with correct proportions.

    # INLINE ENVELOPE (matches character proportions):
    _draw_envelope(t, ox=ox, oy=oy, scale=scale)

    # --- Inner 人 ---
    # 撇: from top-center (~x=+5, y=+40) sweeping down-left to (~x=-50, y=-55).
    # Canonical pie head=(65,90) tail=(-45,-85). Scale 0.6:
    # head=(39,54) tail=(-27,-51). Translation to place head at (5, 40):
    # dx = 5-39 = -34; dy = 40-54 = -14.
    draw_pie(t, ox=ox + (-34) * scale, oy=oy + (-14) * scale, scale=0.60 * scale)

    # --- Inner right stroke (short 捺 / 点 for 人's right leg) ---
    # In 内, the right stroke starts near the 撇's middle and sweeps down-right.
    # Use an inline tapered segment for control.
    right_start = (-10 * scale, 5 * scale)
    right_end = (25 * scale, -50 * scale)
    _tapered_segment(t, right_start, right_end, 3 * scale, 10 * scale, steps=20, ox=ox, oy=oy)
    # Small tail bulb
    tr = int(5 * scale)
    tx, ty = _to_pixel(ox + right_end[0], oy + right_end[1])
    t.ellipse([tx - tr, ty - tr, tx + tr, ty + tr], fill=(0, 0, 0))


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


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _draw_envelope(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw the top-horizontal + right-vertical + hook of 内 in-line
    with the correct proportions (rectangle ~120 wide x ~160 tall)."""
    # Top horizontal: from (-60, +65) to (+60, +65)
    h_start = (-60 * scale, 65 * scale)
    h_corner = (60 * scale, 65 * scale)
    _tapered_segment(t, h_start, h_corner, 8 * scale, 10 * scale, steps=24, ox=ox, oy=oy)

    # Corner dot
    r = int(6 * scale)
    cx, cy = _to_pixel(ox + h_corner[0], oy + h_corner[1])
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # Right vertical: from (+60, +65) to (+60, -95)
    v_end = (60 * scale, -95 * scale)
    _tapered_segment(t, h_corner, v_end, 10 * scale, 9 * scale, steps=32, ox=ox, oy=oy)

    # Hook: from v_end up-and-left
    h_base = (v_end[0] + 1 * scale, v_end[1] + 2 * scale)
    h_tip = (v_end[0] - 20 * scale, v_end[1] + 18 * scale)
    _tapered_segment(t, h_base, h_tip, 9 * scale, 2 * scale, steps=16, ox=ox, oy=oy)

    # End-bulb
    br = int(5 * scale)
    bx, by = _to_pixel(ox + v_end[0], oy + v_end[1])
    t.ellipse([bx - br, by - br, bx + br, by + br], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_nei(d, ox=0, oy=-5, scale=1.0)
    out = os.path.join(BASE, "01_内.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
