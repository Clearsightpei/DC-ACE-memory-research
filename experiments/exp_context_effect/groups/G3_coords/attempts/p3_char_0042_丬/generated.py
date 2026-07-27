"""p3_char_0042_丬 (jiāng) — piece-left radical, 3 strokes.

Layout from GT:
- Upper-left short 撇 (going from upper-right to lower-left)
- Lower-left short 提/撇 (also going down-left, further down)
- Right long shu with tiny hook/curl at top (starts a bit above,
  curves in from left, then straight down)

Kept thin & uniform (MMH-style GT, per form_catalog P12 candidate).
Inline PIL — bank primitives are for calligraphic strokes; GT is thin.
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if SB not in sys.path:
    sys.path.insert(0, SB)

from _shared_helpers import variant_pie, tapered_bezier, to_px  # noqa: E402


def draw_jiang_char(draw):
    # GT re-read: the left two strokes are 提-like (rising from
    # lower-left to upper-right toward the shaft). Written thin and
    # uniform per MMH style. The right shu has a small leftward curl
    # at the top (兒 heng-corner) then descends straight down.

    # -- Stroke 1: upper short 提 (short, rises to upper-right)
    #    head at lower-left (~-70, +25), tail near shaft (~-20, +55)
    variant_pie(draw,
                head=(-70, +25),
                tail=(-20, +55),
                bow_perp=+2.5,   # slight upward bow
                w_head=3.5,
                w_tail=3.0)

    # -- Stroke 2: lower short 提 (further down + further left)
    #    head at lower-left (~-85, -55), tail near shaft (~-25, -35)
    variant_pie(draw,
                head=(-85, -55),
                tail=(-25, -35),
                bow_perp=+2.5,
                w_head=3.5,
                w_tail=3.0)

    # -- Stroke 3: long shu on right with small top curl
    # Top curls from ~(+10, +100) leftward briefly to ~(+30, +85),
    # then straight down to ~(+30, -125). Use a bezier for the curl,
    # then a straight vertical.
    head = (+7, +105)
    corner_ctrl = (+35, +105)
    corner_end = (+35, +90)
    tapered_bezier(draw, head, corner_ctrl, corner_end,
                   w_head=3.5, w_tail=4.0, n=32)
    top_px = to_px(*corner_end)
    bot_px = to_px(+35, -130)
    draw.line([top_px, bot_px], fill=(0, 0, 0), width=4)
    bx, by = bot_px
    r = 2.0
    draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_jiang_char(draw)
    out = os.path.join(HERE, "01_丬.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
