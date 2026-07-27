"""p2_radical_077_忄 — heart-side radical (3 strokes). RETRY 1.

Errata fix (from errata.md): "Mirrored dot pair; the mirrored right
dot didn't match left dot's weight. Fix: use `variant_dian` for BOTH
dots with same w_head/w_tail, swap head/tail positions for the mirror."

GT re-inspection:
- Left stroke: slanting 点 — thin head at UPPER-LEFT, heavy tail at
  LOWER-RIGHT (classic diagonal dian).
- Right stroke: vertical 竖点 — thin head at UPPER-LEFT (near-vertical),
  heavy tail at LOWER-RIGHT — actually a nearly-vertical short thick
  stroke sitting to the right of the shaft, slightly higher than the
  left dot. It reads as more upright than the left dot.
- Center: long tapered 竖 with a slight leftward brush entry at top
  (no bottom hook — 忄 uses shu, not shu_gou, per most fonts). GT
  shows the shaft with a small curl at top and straight body.

Prior attempt failure mode: dots had different visual weights
(right dot appeared lighter/thinner than left). Retry recipe: SAME
width profile for both, only geometry differs. Both go through the
same `variant_dian` helper with identical w_head=3, w_tail=12.

Approach: use `variant_dian` from _shared_helpers.py for both dots
(per errata fix + form_catalog.md note on mirrored dot pairs).
Inline the central shu (has brush curl top, not a bank primitive fit).

Coord convention (P5): math coords, center origin (150, 150), +y up.
"""

import sys
import os
sys.path.insert(
    0,
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code",
)
from _shared_helpers import variant_dian, to_px  # noqa: E402

from PIL import Image, ImageDraw  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def draw_central_shu(t, top_math, bot_math, top_w=10.0, bot_w=11.0,
                     hook_len=14.0):
    """Long tapered central vertical with a small leftward brush-entry
    curl at the very top. No bottom hook."""
    # Brush-entry curl: small bezier from upper-left curling down-right
    # into the shaft top.
    hx0, hy0 = top_math[0] - hook_len, top_math[1] + 10
    hx1, hy1 = top_math[0], top_math[1]
    hmx = (hx0 + hx1) / 2.0 + 5.0
    hmy = (hy0 + hy1) / 2.0 + 3.0
    prev_pt = None
    n_hook = 24
    for i in range(n_hook + 1):
        u = i / n_hook
        bx = (1 - u) ** 2 * hx0 + 2 * (1 - u) * u * hmx + u ** 2 * hx1
        by = (1 - u) ** 2 * hy0 + 2 * (1 - u) * u * hmy + u ** 2 * hy1
        px, py = _to_pixel(bx, by)
        if prev_pt is not None:
            w = 2.5 * (1 - u) + top_w * u
            w_int = max(1, int(round(w)))
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)

    # Main shaft: straight tapered vertical.
    x0, y0 = top_math
    x1, y1 = bot_math
    prev_pt = None
    n = 60
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        px, py = _to_pixel(bx, by)
        if prev_pt is not None:
            w = top_w * (1 - u) + bot_w * u
            w_int = max(1, int(round(w)))
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # STROKE 3: Central 竖 (long vertical) — slightly right of center,
    # extends from upper-canvas top to near bottom. Small leftward
    # brush-entry curl at top. No bottom hook (per GT).
    shu_top = (8.0, 105.0)
    shu_bot = (8.0, -130.0)
    draw_central_shu(t, shu_top, shu_bot, top_w=10.5, bot_w=11.5, hook_len=15)

    # SHARED width profile for both dots (errata fix): same w_head, w_tail.
    W_HEAD = 3.0
    W_TAIL = 12.0

    # STROKE 1: LEFT 点 — thin head at UPPER-LEFT, heavy tail toward
    # LOWER-RIGHT (moving in toward shaft). Classic diagonal dian.
    variant_dian(
        t,
        head=(-52.0, 60.0),
        tail=(-22.0, 30.0),
        w_head=W_HEAD,
        w_tail=W_TAIL,
        bow_perp=-3.0,
    )

    # STROKE 2: RIGHT 点 — MIRRORED. In 忄 the right dot is more
    # vertical/upright (竖点): thin head at UPPER position, heavy tail
    # DOWNWARD, with a slight rightward lean. Positioned slightly higher
    # than the left dot per GT. Same width profile — SWAP head/tail
    # geometry for the mirror (per errata fix + form_catalog note).
    variant_dian(
        t,
        head=(32.0, 75.0),        # thin head upper (near shaft)
        tail=(48.0, 30.0),        # heavy tail lower-right
        w_head=W_HEAD,
        w_tail=W_TAIL,
        bow_perp=+3.0,            # mirror the bow direction
    )

    out = (
        "/Users/peilinwu/Documents/AI memory research/experiments/"
        "exp_context_effect/groups/G3_coords/attempts/"
        "p2_radical_077_忄__retry_1/01_忄.png"
    )
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
