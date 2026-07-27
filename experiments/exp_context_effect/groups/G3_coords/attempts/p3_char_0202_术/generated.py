# p3_char_0202_术 — 术 (shù, art/technique), 5 strokes.
# Structure = 木 (heng + shu + pie + na crossing at (0,+25)) + a 点 dian in the upper-right.
# Reuse of bank primitive: mu.py (draw_mu, PASSed in B2 pos 136).
# Extra 点 rendered inline as a small tapered bezier, positioned upper-right of the vertical stem.

import os
import sys
import math
from PIL import Image, ImageDraw

# Import mu (木) from success bank
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BANK_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_DIR)
from mu import draw_mu  # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _inline_dian(t, x0, y0, x1, y1, w_head=3.0, w_tail=9.0):
    """Short tapered stroke growing from head to tail — a 点 that lands heavier at the tail."""
    n = 30
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    t = ImageDraw.Draw(img)

    # 木 body — reuse mu bank primitive at identity transform.
    draw_mu(t, ox=0.0, oy=0.0, scale=1.0)

    # 点 in the upper-right — starts near the top of the shu just to the right,
    # falls down-and-right (typical 右点 direction).
    # Anchored around x=+22..+38, y=+52..+35 (math coords, so upper region).
    _inline_dian(t, x0=22, y0=52, x1=40, y1=32, w_head=3.0, w_tail=8.5)

    out_path = os.path.join(SCRIPT_DIR, "01_术.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
