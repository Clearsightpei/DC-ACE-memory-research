"""大 (dà) — p3_char_0041.

Structure (X-crossing family, per form_catalog.md):
- 横 (top crossbar) — sits at upper-mid, spans wide, slightly rising.
- 撇 (left descender) — starts on the heng crossbar, sweeps to lower-left.
- 捺 (right descender) — starts on the heng crossbar, sweeps to lower-right.

Per form_catalog X-crossing recipe: 大 uses u_pie=0.5 (crossing at pie
midpoint, apex on heng crossbar). Both pie head and na head sit on the
heng bar. We compute pie's midpoint and place the heng across it, then
use kiss_apex to weld na to pie at that midpoint.

GT observation (300x300): heng centered roughly at y ~ +35 math, spans
x ~ [-70, +65]. Pie sweeps from (~+20, +80) down to (~-95, -100).
Na sweeps from (~+15, +75) down to (~+100, -105). Crossing at heng level.
"""
import os
import sys
from PIL import Image, ImageDraw

# Import shared helpers.
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, kiss_apex, to_px,
)


def draw_da(draw, ox=0, oy=0, scale=1.0):
    # --- 大 geometry (from GT observation):
    # The 撇 starts at the top as a small nub, sweeps down through the
    # heng crossbar, and continues to lower-left.
    # The 捺 starts at the SAME top apex, sweeps down through the heng,
    # continues to lower-right.
    # The 横 is a separate crossbar BELOW the apex, crossing both
    # descenders roughly at their upper third.
    #
    # So this is a 人-style kiss (u_pie=0.0) at the TOP, with a heng
    # painted across the descenders below the apex.
    from _shared_helpers import tapered_line  # noqa: E402

    # Apex at top of character (both pie and na start here).
    apex = (ox + 5 * scale, oy + 85 * scale)
    pie_tail = (ox - 100 * scale, oy - 108 * scale)
    na_tail = (ox + 100 * scale, oy - 108 * scale)

    # Kiss at apex (both heads at same pixel — 人-style).
    pie_h, na_h = kiss_apex(apex, pie_tail, na_tail,
                            u_pie=0.0, bow_pie=-6.0)

    # --- 撇 (left descender) from apex to lower-left.
    variant_pie(draw, head=pie_h, tail=pie_tail,
                bow_perp=-8.0, w_head=8, w_tail=1)

    # --- 捺 (right descender) from same apex to lower-right.
    variant_na(draw, head=na_h, tail=na_tail,
               bow_perp=+7.0, w_head=2, w_belly=11, w_tail=3,
               belly_u=0.72)

    # --- 横 (crossbar). Sits BELOW the apex, crossing both descenders
    # at roughly upper-third of their length. Slight upward tilt.
    # Apex y = +85; tails y = -108. Heng at y ≈ +30 crosses well.
    heng_y = oy + 30 * scale
    heng_left = (ox - 85 * scale, heng_y - 3 * scale)
    heng_right = (ox + 80 * scale, heng_y + 5 * scale)  # slight rise
    tapered_line(draw, heng_left, heng_right, w0=7, w1=8, n=40)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_da(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(HERE, "01_大.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    main()
