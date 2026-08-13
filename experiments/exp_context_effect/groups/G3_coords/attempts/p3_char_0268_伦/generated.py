# p3_char_0268_伦 — 伦 (lún), 6 strokes.
# Composition: 亻 (left) + 仑 (right).
#   仑 = 人-roof (top) + 匕 (bottom).
#
# Recipe from drawer_memory L-R table: 亻 at ox=-45, scale=0.55;
# right at ox=+40, scale=0.55.  We inline both halves in PIL so we
# can control widths (P12 thin), avoiding the ren_pang turtle detour.
#
# Right side geometry lifted from p3_char_0117_仑 attempt but scaled
# and re-anchored for the +40/0.55 slot.

import os
from PIL import Image, ImageDraw
import sys

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, kiss_apex, tapered_line, tapered_bezier,
)


W, H = 300, 300


# Helpers below expect MATH coords (center origin, +y up); they call
# to_px internally. So P returns raw math coords, not pixels.


# ---------- LEFT 亻 (person radical) ----------
def draw_ren_pang_inline(draw, ox=0, oy=0, scale=1.0):
    """亻: pie + short shu; shu head touches pie mid-shaft."""
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # 撇: long sweep from upper-right down-left.
    variant_pie(draw, head=P(+5, +70), tail=P(-45, -60),
                bow_perp=-6.0, w_head=4.0, w_tail=2.0)
    # 竖 (short): starts on pie's mid-shaft, drops straight down.
    tapered_line(draw, P(-8, +15), P(-8, -80), w0=3.5, w1=3.0, n=24)


# ---------- RIGHT 仑 ----------
def draw_lun_inline(draw, ox=0, oy=0, scale=1.0):
    """仑: 人-roof + 匕 below."""
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # --- TOP 人-roof ---
    pie_head = P(0, +95)
    pie_tail = P(-70, -10)
    na_tail = P(+70, -15)
    pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                            u_pie=0.0, bow_pie=-6.0)
    variant_pie(draw, head=pie_h, tail=pie_tail,
                bow_perp=-6.0, w_head=3.5, w_tail=2.0)
    variant_na(draw, head=na_h, tail=na_tail,
               bow_perp=+6.0, w_head=2.5, w_belly=3.5,
               w_tail=2.0, belly_u=0.75)

    # --- BOTTOM 匕 ---
    # 撇 of 匕: shorter than the roof pie, sits under the apex.
    variant_pie(draw, head=P(+5, +25), tail=P(-40, -55),
                bow_perp=-4.0, w_head=3.0, w_tail=2.0)

    # 竖弯钩: vertical drop, then rounded bend to horizontal, tiny
    # upturn hook at end.
    tapered_line(draw, P(-15, -10), P(-15, -60), w0=3.0, w1=3.0, n=20)
    tapered_bezier(draw,
                   P(-15, -60),
                   P(-15, -78),
                   P(+10, -78),
                   w_head=3.0, w_tail=3.0, n=24)
    tapered_line(draw, P(+10, -78), P(+35, -76), w0=3.0, w1=3.0, n=14)
    # small upturn hook:
    tapered_line(draw, P(+35, -76), P(+38, -66), w0=3.0, w1=2.0, n=6)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # Left 亻: ox=-45, scale=0.55 (drawer_memory recipe).
    draw_ren_pang_inline(draw, ox=-55, oy=0, scale=0.60)
    # Right 仑: ox=+40, scale=0.55.
    draw_lun_inline(draw, ox=+40, oy=0, scale=0.55)

    out = os.path.join(os.path.dirname(__file__), "01_伦.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
