"""气 (qì) — retry_1. 4-stroke radical.

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Errata entry: "横撇 + inner 乙-like sweep. Complex curl." Skipped
#   in prior priority list ("no clear new lever"). Prior attempt used
#   calligraphic tapered widths 7-9 and hook flicked up-LEFT. Fix:
#   apply P12 (thin uniform ~3-4 px, MMH-style), correct 横斜钩
#   geometry (starts left, flat right, then curls DOWN and RIGHT into
#   deep bowl, tiny hook flicking up-LEFT at bottom-right end), and
#   make strokes 2 & 3 short/thin uniform hengs matching the MMH GT.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   - "横 | 亼 base (thin uniform, MMH-style)" (w=3 uniform) — for the
#     two upper hengs.
#   - "撇 | 丿-char thin uniform (MMH-style)" (w_head 4, w_tail 2,
#     bow_perp -10) — for the top-left pie.
#   - No direct row for 横斜钩; inline as tapered polyline per P12.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - Not X-crossing/apex-kiss (no shared pixel).
#   - Not mirror-dot pair.
#   - Per-stroke form applies (variant_pie thin) — use variant_pie for
#     stroke 1. For heng use inline draw (thin uniform, no primitive
#     matches the thin width — bank draw_heng is calligraphic-thick).
#   - Uniform thin lines (MMH GT): YES → P12 discipline throughout.
#   Import: variant_pie from _shared_helpers.
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from _shared_helpers import variant_pie, tapered_bezier, tapered_line  # noqa: E402


CANVAS = 300


def _to_px(ox, oy):
    """math coords (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _thin_heng(draw, x0, x1, y, width=4):
    """Uniform-thin horizontal heng, math coords."""
    p0 = _to_px(x0, y)
    p1 = _to_px(x1, y)
    draw.line([p0, p1], fill=(0, 0, 0), width=width)
    # rounded caps
    r = width / 2.0
    draw.ellipse([p0[0] - r, p0[1] - r, p0[0] + r, p0[1] + r], fill=(0, 0, 0))
    draw.ellipse([p1[0] - r, p1[1] - r, p1[0] + r, p1[1] + r], fill=(0, 0, 0))


def draw_qi_radical(draw):
    # --- Stroke 1: 撇 (top-left, thin uniform, MMH-style) ---
    # Head near (-20, +90) with small 起笔 blob; tail near (-70, +5).
    # Slightly longer than v1.
    variant_pie(draw, head=(-20, 90), tail=(-72, 0),
                bow_perp=-5.0, w_head=4.0, w_tail=2.0, n=48)
    hx, hy = _to_px(-20, 90)
    r = 3
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))

    # --- Stroke 2: upper short 横 ---
    _thin_heng(draw, x0=-5, x1=55, y=65, width=4)

    # --- Stroke 3: middle longer 横 --- extended right per GT
    _thin_heng(draw, x0=-30, x1=68, y=25, width=4)

    # --- Stroke 4: 横斜钩 ---
    # Longer flat opening, deeper drop, hook flicking up-left.
    ink_w = 4

    # A. longer flat opening (rises very slightly)
    a0 = _to_px(-78, -30)
    a1 = _to_px(-15, -22)
    draw.line([a0, a1], fill=(0, 0, 0), width=ink_w)
    r = ink_w / 2.0
    draw.ellipse([a0[0] - r, a0[1] - r, a0[0] + r, a0[1] + r], fill=(0, 0, 0))

    # B. long curved sweep — deeper drop, gentler early curve
    b0 = (-15, -22)
    b1 = (72, -115)
    bc = (60, -25)
    tapered_bezier(draw, b0, bc, b1, w_head=ink_w, w_tail=ink_w, n=60)

    # C. small hook flicking UP-LEFT at stroke end
    h0 = _to_px(72, -115)
    h1 = _to_px(54, -95)
    draw.line([h0, h1], fill=(0, 0, 0), width=ink_w)
    r = ink_w / 2.0
    draw.ellipse([h1[0] - r, h1[1] - r, h1[0] + r, h1[1] + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_qi_radical(draw)
    out = Path(__file__).parent / "01_气.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
