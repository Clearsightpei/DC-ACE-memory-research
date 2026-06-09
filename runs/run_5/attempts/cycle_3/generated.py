"""Cycle 3 (run_5) — 十 / 上 / 下.

Reuses success_bank/code/heng.py for every 横.
Defines a new draw_shu(...) primitive (垂露 variant).

Convention (matches heng.py): canvas 800x600, math-convention coords with
origin at canvas center. to_px translates math -> PIL pixel.
"""

import os
import sys

from PIL import Image, ImageDraw

# --- Success Bank shim ---------------------------------------------------
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from heng import draw_heng, brushed_bezier, to_px, CANVAS_W, CANVAS_H  # noqa: E402


# --- New primitive: 竖 (shu) — 垂露 variant ------------------------------

def w_profile_shu(s):
    """entry-press 16 (top) -> shaft 11 -> bottom-press 18 (rounded 垂露).
       Same flooring contract as heng (caller applies max(3, w)).
    """
    if s <= 0.10:
        return 16.0
    elif s <= 0.20:
        t = (s - 0.10) / 0.10
        return 16.0 + (11.0 - 16.0) * t
    elif s <= 0.80:
        return 11.0
    elif s <= 0.95:
        t = (s - 0.80) / 0.15
        return 11.0 + (18.0 - 11.0) * t
    else:
        return 18.0


def draw_top_hook_shu(draw, ox, oy_top, scale=1.0):
    """Small top entry hook for 竖 — slants down-left from the top, like a
       calligraphic 起笔. Drawn at the entry-press width (16).
       (Matches the small leftward kink visible in the GTs.)
    """
    flen = 12.0 * scale
    P0 = (ox - flen * 0.55, oy_top + flen * 0.40)
    P1 = (ox - flen * 0.35, oy_top + flen * 0.25)
    P2 = (ox - flen * 0.15, oy_top + flen * 0.10)
    P3 = (ox, oy_top)
    brushed_bezier(draw, P0, P1, P2, P3, lambda s: 16.0, samples=80)


def draw_shu(draw, ox, oy_top, length, scale=1.0):
    """Draw a 楷书 垂露 竖 from (ox, oy_top) downward by `length` px.

    - small top hook at entry-press width 16
    - body Bezier, near-vertical with a very slight rightward bow
    - rounded bottom-press 18 (no exposed point)
    """
    oy_bot = oy_top - length
    # Tiny rightward curvature so the shaft is alive, not a ruler line.
    bow = 2.0 * scale
    P0 = (ox, oy_top)
    P1 = (ox + bow * 0.5, oy_top - length * 0.30)
    P2 = (ox + bow, oy_top - length * 0.70)
    P3 = (ox, oy_bot)

    draw_top_hook_shu(draw, ox, oy_top, scale)
    brushed_bezier(draw, P0, P1, P2, P3, w_profile_shu, samples=220)
    # Rounded 垂露: an extra disk at the bottom guarantees a fully round end.
    bx, by = to_px(ox, oy_bot)
    r = 18.0 / 2.0
    draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


# --- New primitive: 点 (dot, small brushed disk for 下) ------------------

def draw_dian(draw, ox, oy, scale=1.0):
    """A short 点 stroke — diagonal teardrop from upper-left to lower-right.
       Used as the right-side 点 in 下.
    """
    flen = 36.0 * scale
    # Start narrow at top-left, swell to a heavy bottom-right.
    P0 = (ox - flen * 0.45, oy + flen * 0.35)
    P1 = (ox - flen * 0.20, oy + flen * 0.15)
    P2 = (ox + flen * 0.15, oy - flen * 0.10)
    P3 = (ox + flen * 0.45, oy - flen * 0.35)

    def w(s):
        # taper-in then heavy press at the end (collected 点)
        if s <= 0.20:
            return 6.0 + (12.0 - 6.0) * (s / 0.20)
        elif s <= 0.85:
            return 12.0 + (18.0 - 12.0) * ((s - 0.20) / 0.65)
        else:
            return 18.0

    brushed_bezier(draw, P0, P1, P2, P3, w, samples=160)
    # Rounded bottom-right press.
    bx, by = to_px(P3[0], P3[1])
    r = 18.0 / 2.0
    draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


# --- Helpers -------------------------------------------------------------

def new_canvas():
    img = Image.new('RGB', (CANVAS_W, CANVAS_H), (255, 255, 255))
    return img, ImageDraw.Draw(img)


# --- Characters ----------------------------------------------------------

def draw_shi(path):
    """十: long 横 across middle, long 竖 crossing it (vertical extends a
       bit above the heng and significantly below it).
       From GT: heng is near the canvas vertical center, slightly above.
       The 竖 top is ~80px above heng; bottom is ~190px below heng.
    """
    img, d = new_canvas()
    heng_y = 0
    heng_len = 320
    draw_heng(d, ox=0, oy=heng_y, length=heng_len, scale=1.0)
    # 竖 crosses the heng. Top above, longer below per GT proportions.
    shu_top_y = heng_y + 90
    shu_len = 280
    draw_shu(d, ox=0, oy_top=shu_top_y, length=shu_len, scale=1.0)
    img.save(path)


def draw_shang(path):
    """上: short 竖 (upper), short 横 to its right (mid), long 横 across bottom.

       From GT:
         - long bottom 横 around oy=-110, length ~320
         - 竖 stands on the bottom 横, going up about 200px from it
         - short 横 sits to the right of the 竖 at mid-height (~oy=-30),
           length ~130
    """
    img, d = new_canvas()
    # Bottom long 横
    bot_y = -110
    draw_heng(d, ox=0, oy=bot_y, length=320, scale=1.0)
    # 竖 — stands ON the bottom 横; its bottom-press should sit right at bot_y.
    shu_top_y = bot_y + 210   # 200px tall + extra so press sits at heng line
    shu_len = 210
    shu_ox = -20  # slightly left of center, per GT
    draw_shu(d, ox=shu_ox, oy_top=shu_top_y, length=shu_len, scale=1.0)
    # Short 横 to the right of the 竖, mid-height
    short_y = -30
    draw_heng(d, ox=shu_ox + 90, oy=short_y, length=130, scale=0.7)
    img.save(path)


def draw_xia(path):
    """下: long 横 on top, long 竖 below it centered, short 点 right of 竖.

       From GT:
         - top 横 around oy=+80, length ~330
         - 竖 starts a touch above the 横 (small top-hook overlaps), goes
           down ~270px below the heng
         - 点 sits to the right of the 竖, between the heng and the
           middle of the 竖 (~oy=+10..+30, ox= +50..+80)
    """
    img, d = new_canvas()
    heng_y = 80
    draw_heng(d, ox=0, oy=heng_y, length=330, scale=1.0)
    # 竖 — crosses the heng slightly (top-hook slightly above heng), shaft goes
    # well below.
    shu_top_y = heng_y + 25
    shu_len = 290
    draw_shu(d, ox=0, oy_top=shu_top_y, length=shu_len, scale=1.0)
    # 点 to the right of the 竖, sitting below the heng.
    draw_dian(d, ox=55, oy=heng_y - 60, scale=1.0)
    img.save(path)


# --- Entry point ---------------------------------------------------------

def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    draw_shi(os.path.join(out_dir, '01_十.png'))
    draw_shang(os.path.join(out_dir, '02_上.png'))
    draw_xia(os.path.join(out_dir, '03_下.png'))


if __name__ == '__main__':
    main()
