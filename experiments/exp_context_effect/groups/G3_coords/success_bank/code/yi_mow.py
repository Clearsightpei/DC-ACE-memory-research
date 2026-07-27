# p3_char_0137_刈 (yì, "to mow") — 4 strokes.
# Left half: 乂 (X-cross: 撇 + 捺). Right half: 刂 (short 竖 + 竖钩).
#
# Reuse plan (G3 coord-bank):
# - 乂 shape: use variant_pie + variant_na from _shared_helpers (same as
#   yi_cross.py and gang.py inside 冂). Draw shifted to the LEFT half in
#   math coords.
# - 刂 shape: inline PIL-pixel recipe (tapered lines) on the RIGHT half,
#   modeled on gang.py's frame right-vertical + hook.
# Widths chosen to match GT (uniform ~4-6px thin lines per GT).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import variant_pie, variant_na  # noqa: E402


def _tapered_line_px(draw, p0, p1, w0, w1, steps=32):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_yi_char(draw):
    """Render 刈 into the given PIL ImageDraw at fixed 300px canvas."""

    # --- Left half: 乂 (X-cross) ---
    # Math coords (center 150,150; +y up). Shift the 乂 leftward by ~55px.
    # Original yi_cross endpoints centered:
    #   撇 head (45,65) tail (-105,-110)
    #   捺 head (-45,40) tail (100,-110)
    # Left-shift by dx = -55 to place 乂 in left half.
    dx = -50
    # 撇 — from upper-right down-and-left, thinner tail with a bit of curve.
    variant_pie(draw,
                head=(40 + dx, 55),
                tail=(-90 + dx, -95),
                bow_perp=-8.0, w_head=4.0, w_tail=1.2, n=60)
    # 捺 — from upper-left down-and-right, thinner overall (GT thin lines).
    variant_na(draw,
               head=(-40 + dx, 30),
               tail=(90 + dx, -95),
               bow_perp=6.0, w_head=1.5,
               w_belly=5.0, w_tail=1.5, belly_u=0.65, n=70)

    # --- Right half: 刂 (short 竖 + 竖钩) ---
    # GT: short shu sits at upper right, hook at very bottom, long shu extends
    # nearly full height on the right.
    # Short 竖 — small vertical stroke at upper right
    short_top = (210, 70)
    short_bot = (212, 155)
    _tapered_line_px(draw, short_top, short_bot, w0=3, w1=4, steps=28)

    # Long 竖钩 — right side, tall, with a small hook flicking lower-left
    long_top = (255, 55)
    long_bot = (248, 255)
    _tapered_line_px(draw, long_top, long_bot, w0=3, w1=4, steps=40)
    # Hook — modest flick to lower-left from the bottom
    hook_end = (long_bot[0] - 22, long_bot[1] - 8)
    _tapered_line_px(draw, long_bot, hook_end, w0=4, w1=1, steps=14)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_yi_char(draw)
    out_path = os.path.join(_HERE, "01_刈.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
