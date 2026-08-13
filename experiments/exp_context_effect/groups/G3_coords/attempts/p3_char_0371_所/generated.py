# p3_char_0371_所 (suǒ) — 户 (left) + 斤 (right)
#
# Composition:
#   Left ~ 40% width: 户 built from bank shi_radical (尸) shifted left/down-scaled
#          plus a top-left dot (户 = 尸 + top dot).
#   Right ~ 50% width: 斤 inlined (short pie + long pie + heng + shu),
#          since 斤 is unsolved in errata (p2_radical_101_斤 FAIL).
#          Thin ~4-5px per P12 (MMH GT is thin uniform).
#
# No BANK_DEVIATION: shi_radical is used as-is (with position/scale knobs).

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
    ),
)
from shi_radical import draw_shi_radical  # noqa: E402


CANVAS = 300


def _to_px(bx, by, ox=0.0, oy=0.0, scale=1.0):
    """Math convention: y grows up. Origin at canvas center."""
    px = CANVAS / 2 + ox + bx * scale
    py = CANVAS / 2 - (oy + by * scale)
    return px, py


def _stroke(draw, pts, w=4):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    r = w / 2
    for pt in pts:
        draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def _bezier_taper(draw, p0, p1, p2, n=50, w_head=6, w_tail=2):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_hu_component(t, ox=-70, oy=15, scale=0.75):
    """户 = 尸 (via shi_radical) + top dot."""
    # Base 尸 (heng-zhe + middle heng + long pie).
    draw_shi_radical(t, ox=ox, oy=oy, scale=scale)

    # Top-left dot (户's distinguishing tick).
    # shi_radical top-left of 尸 is around local (-55, 90); we want the dot
    # slightly above that area, sloping down-right.
    dot_head = _to_px(-55, 118, ox=ox, oy=oy, scale=scale)
    dot_tail = _to_px(-32, 100, ox=ox, oy=oy, scale=scale)
    _bezier_taper(
        t,
        dot_head,
        ((dot_head[0] + dot_tail[0]) / 2, (dot_head[1] + dot_tail[1]) / 2 - 2),
        dot_tail,
        n=25,
        w_head=3,
        w_tail=7,
    )


def draw_jin_component(t, ox=55, oy=15, scale=0.9):
    """斤 inline: short pie + long pie + heng + long shu.

    Local coord cell about 110 wide, 220 tall.
    """
    # Stroke 1: short 撇 at top-left (a tick).
    p0 = _to_px(-5, 95, ox=ox, oy=oy, scale=scale)
    p1 = _to_px(-18, 82, ox=ox, oy=oy, scale=scale)
    p2 = _to_px(-30, 70, ox=ox, oy=oy, scale=scale)
    _bezier_taper(t, p0, p1, p2, n=30, w_head=5, w_tail=2)

    # Stroke 2: long 撇, from top area sweeping down-left.
    q0 = _to_px(-8, 65, ox=ox, oy=oy, scale=scale)
    q_mid = _to_px(-30, -20, ox=ox, oy=oy, scale=scale)
    q1 = _to_px(-60, -110, ox=ox, oy=oy, scale=scale)
    _bezier_taper(t, q0, q_mid, q1, n=60, w_head=7, w_tail=2)

    # Stroke 3: 横 (middle horizontal). Slightly below the long-pie head level.
    h_a = _to_px(-25, 20, ox=ox, oy=oy, scale=scale)
    h_b = _to_px(50, 25, ox=ox, oy=oy, scale=scale)
    _stroke(t, [h_a, h_b], w=5)

    # Stroke 4: 竖 (long vertical). Right side, from heng right-end going down.
    s_a = _to_px(45, 60, ox=ox, oy=oy, scale=scale)
    s_b = _to_px(45, -125, ox=ox, oy=oy, scale=scale)
    _stroke(t, [s_a, s_b], w=5)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    draw_hu_component(t, ox=-72, oy=10, scale=0.72)
    draw_jin_component(t, ox=55, oy=10, scale=0.88)

    out_path = os.path.join(os.path.dirname(__file__), "01_所.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
