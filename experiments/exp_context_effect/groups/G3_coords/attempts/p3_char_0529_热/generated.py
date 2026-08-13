# p3_char_0529_热 — top: 执 (扌 + 丸); bottom: 灬
# G3: uses bank shou_pang + bank huo_bottom; inlines 丸 fresh (no bank entry).
# No BANK_DEVIATION: bank primitives fit their slots as-is.

import os
import sys
import math

from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from shou_pang import draw_shou_pang  # noqa: E402
from huo_bottom import draw_huo_bottom  # noqa: E402


CANVAS = 300


def to_px(mx, my):
    return (CANVAS / 2 + mx, CANVAS / 2 - my)


def tap_line(t, p0, p1, w0, w1, n=20):
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        a = (p0[0] + u0 * (p1[0] - p0[0]), p0[1] + u0 * (p1[1] - p0[1]))
        b = (p0[0] + u1 * (p1[0] - p0[0]), p0[1] + u1 * (p1[1] - p0[1]))
        w = max(1, int(round(w0 * (1 - (u0 + u1) / 2) + w1 * ((u0 + u1) / 2))))
        t.line([a, b], fill=(0, 0, 0), width=w)


def tap_bez(t, p0, p1, p2, w0, w1, n=30):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w0 * (1 - u) + w1 * u
        if prev is not None:
            wi = max(1, int(round(w)))
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
        prev = (bx, by)


def draw_wan(t, ox=0.0, oy=0.0, scale=1.0):
    """Inline 丸 (wan, "ball"). 3 strokes: 撇 + 竖弯钩 + 丶."""
    s = scale

    # Stroke 1: short 撇 at top going down-left, tapered
    p_head = to_px(ox + 32 * s, oy + 60 * s)
    p_tail = to_px(ox - 8 * s, oy + 20 * s)
    tap_line(t, p_head, p_tail, 5, 8, n=24)

    # Stroke 2: 竖弯钩 — shaft down, arc right, tail right, hook up
    thick = max(1, int(round(8 * s)))
    shaft_top = to_px(ox + 22 * s, oy + 55 * s)
    shaft_bot = to_px(ox + 20 * s, oy - 20 * s)
    t.line([shaft_top, shaft_bot], fill=(0, 0, 0), width=thick)

    # Arc — quarter circle center (ox + 55, oy - 20), radius 35
    arc_cx = ox + 55 * s
    arc_cy = oy - 20 * s
    r = 35 * s
    prev = None
    for i in range(15):
        u = i / 14
        ang = math.pi + u * math.pi / 2  # 180° -> 270°
        px = arc_cx + r * math.cos(ang)
        py = arc_cy + r * math.sin(ang)
        curr = to_px(px, py)
        if prev is not None:
            t.line([prev, curr], fill=(0, 0, 0), width=thick)
        prev = curr

    # Tail horizontal right
    tail_s = to_px(ox + 55 * s, oy - 55 * s)
    tail_e = to_px(ox + 82 * s, oy - 55 * s)
    t.line([tail_s, tail_e], fill=(0, 0, 0), width=thick)

    # Hook up (tapered)
    hook_base = to_px(ox + 82 * s, oy - 55 * s)
    hook_tip = to_px(ox + 76 * s, oy - 32 * s)
    tap_line(t, hook_base, hook_tip, 8, 2, n=12)

    # Stroke 3: 丶 dot inside the belly
    dh = to_px(ox + 40 * s, oy + 15 * s)
    dt = to_px(ox + 55 * s, oy - 5 * s)
    dc = to_px(ox + 48 * s, oy + 5 * s)
    tap_bez(t, dh, dt, dc, 3, 9, n=25)


def draw_re(t):
    """热 — 执 top (扌 left + 丸 right) + 灬 bottom."""
    # 扌 top-left, compressed for L-R slot in top half
    draw_shou_pang(t, ox=-60, oy=42, scale=0.70)
    # 丸 top-right
    draw_wan(t, ox=20, oy=20, scale=1.0)
    # 灬 four dots bottom (bank primitive at its native px placement)
    draw_huo_bottom(t, ox=0, oy=0, scale=1.0)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_re(t)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_热.png")
    img.save(out)
    print(f"wrote {out}")
