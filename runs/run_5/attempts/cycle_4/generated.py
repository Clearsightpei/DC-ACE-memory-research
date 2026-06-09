"""Cycle 4 — Drawer attempts: 下, 干, 工.

Reuses 横 and 竖 primitives from the Success Bank (run_5 c2/c3).
Defines an inline `draw_dian` (small brushed teardrop) for 下's 点
since 点 is not yet in the Success Bank.

Renders three PNGs into attempts/cycle_4/.
"""

import sys
import os

SB = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from PIL import Image, ImageDraw  # noqa: E402

from heng import draw_heng, to_px, bezier_point, brushed_bezier  # noqa: E402
from shu import draw_shu  # noqa: E402

CANVAS_W, CANVAS_H = 800, 600
WHITE = (255, 255, 255)


def new_canvas():
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), WHITE)
    return img, ImageDraw.Draw(img)


# ---------------------------------------------------------------------------
# Inline 点 (small brushed diagonal teardrop, top-left → bottom-right).
# Tapered tip on the upper-left (light entry), heavy press at the lower-right
# (收笔). Width floor max(3, w) per principle §1.0.
# ---------------------------------------------------------------------------
def w_profile_dian(s):
    """Light entry (5) → grows → heavy press at the bottom-right (18)."""
    if s <= 0.20:
        # taper from 5 -> 10
        t = s / 0.20
        return 5.0 + (10.0 - 5.0) * t
    elif s <= 0.80:
        # grow 10 -> 16
        t = (s - 0.20) / 0.60
        return 10.0 + (16.0 - 10.0) * t
    else:
        # final press 16 -> 18
        t = (s - 0.80) / 0.20
        return 16.0 + (18.0 - 16.0) * t


def draw_dian(pil_draw, ox, oy, length=36.0, scale=1.0):
    """Diagonal teardrop 点. Anchored such that the heavy tail lands near (ox, oy).
       Stroke runs from upper-left (light tip) to (ox, oy) (heavy press).
    """
    L = length * scale
    P0 = (ox - L * 0.85, oy + L * 0.85)   # upper-left tip
    P1 = (ox - L * 0.55, oy + L * 0.55)
    P2 = (ox - L * 0.25, oy + L * 0.25)
    P3 = (ox, oy)                          # heavy press anchor (bottom-right)
    brushed_bezier(pil_draw, P0, P1, P2, P3, w_profile_dian, samples=160)


# ---------------------------------------------------------------------------
# 下 — top long 横, 竖 hanging FROM the heng (no pierce above), 点 right of 竖.
# ---------------------------------------------------------------------------
def draw_xia(pil_draw, ox=0, oy=0, scale=1.0):
    # Top heng — long, sits as the cap of the character.
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 80, length=330 * scale, scale=1.0 * scale)
    # 竖 — top sits 10 BELOW the heng centerline (so it hangs without piercing).
    draw_shu(pil_draw, ox=ox + 0, oy_top=oy + 70, length=240 * scale, scale=1.0 * scale)
    # 点 — small diagonal teardrop to the right of the 竖, upper region.
    draw_dian(pil_draw, ox=ox + 60, oy=oy + 20, length=42.0, scale=1.0 * scale)


# ---------------------------------------------------------------------------
# 干 — short heng top, long heng middle, 竖 pierces THROUGH the long heng.
# ---------------------------------------------------------------------------
def draw_gan(pil_draw, ox=0, oy=0, scale=1.0):
    # Top short heng.
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 110, length=200 * scale, scale=0.85 * scale)
    # Middle long heng.
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 10, length=330 * scale, scale=1.0 * scale)
    # 竖 — pierces THROUGH the long middle heng (starts above it).
    # oy_top sits ~70 above the long heng centerline (between the two hengs),
    # length carries it down well below the long heng.
    draw_shu(pil_draw, ox=ox + 0, oy_top=oy + 80, length=270 * scale, scale=1.0 * scale)


# ---------------------------------------------------------------------------
# 工 — top short heng, 竖 spans between the two hengs, bottom long heng.
# ---------------------------------------------------------------------------
def draw_gong(pil_draw, ox=0, oy=0, scale=1.0):
    top_y = oy + 90
    bot_y = oy - 110
    # Top heng (shorter).
    draw_heng(pil_draw, ox=ox + 0, oy=top_y, length=200 * scale, scale=0.85 * scale)
    # Bottom heng (longer).
    draw_heng(pil_draw, ox=ox + 0, oy=bot_y, length=310 * scale, scale=1.0 * scale)
    # 竖 — spans BETWEEN the two hengs.
    # oy_top at the top heng's y; length = vertical gap.
    gap = top_y - bot_y
    draw_shu(pil_draw, ox=ox + 0, oy_top=top_y, length=gap, scale=1.0 * scale)


def render(fn, path):
    img, d = new_canvas()
    fn(d)
    img.save(path)
    print(f"wrote {path}")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    render(draw_xia, os.path.join(here, "01_下.png"))
    render(draw_gan, os.path.join(here, "02_干.png"))
    render(draw_gong, os.path.join(here, "03_工.png"))
