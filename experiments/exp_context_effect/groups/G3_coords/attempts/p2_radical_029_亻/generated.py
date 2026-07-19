"""亻 (人字旁) — left-radical form of 人.

Composition: pie (top, longer, sweeping down-left) + shu (short vertical
on the right, head touching the pie's mid-section).

TR-compliant placements below with explicit target-pixel derivations.
"""
import os
import sys
from PIL import Image, ImageDraw

# Make bank primitives importable.
BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from pie import draw_pie
from shu import draw_shu

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # --- TR6 explicit derivations ---
    #
    # Canvas 300x300, math coords (center origin, +y up).
    # In PIL pixels: center is (150, 150).
    #
    # 亻 shape from GT:
    #   撇 (pie): head at ~PIL (175, 55) i.e. math (+25, +95),
    #             tail at ~PIL (95, 205) i.e. math (-55, -55).
    #   竖 (shu): head at ~PIL (170, 135) i.e. math (+20, +15),
    #             tail at ~PIL (170, 245) i.e. math (+20, -95).
    #             Length ~110 px (short compared to standalone 200px shu).
    #
    # ---- 撇 (pie) placement ----
    # pie primitive default: head at math (+65, +90), tail at math (-45, -85).
    # Bank pie is a diagonal slash; for 亻 we want a shorter, more vertical
    # sweep. Scale down to 0.80 to compress it.
    # Head target ~PIL (170, 55) i.e. math (+20, +95). Tail ~PIL (100, 200)
    # i.e. math (-50, -50). Chord center: math (-15, +22).
    # Default chord center at scale 0.8 ~ math (+8, +2). ox = -23, oy = +20.
    draw_pie(t, ox=-23, oy=20, scale=0.80)

    # ---- 竖 (shu) placement ----
    # shu primitive default: length 200 px, centered at math origin (0,0).
    # Target: short shu, length ~100 px → scale = 0.50.
    # Head should touch pie's mid-shaft. At scale 0.80, pie at u=0.5:
    #   bx_local = 0.25*52 + 0.5*(-4) + 0.25*(-36) = 13 - 2 - 9 = +2
    #   by_local = 0.25*72 + 0.5*(+6) + 0.25*(-68) = 18 + 3 - 17 = +4
    # With ox=-23, oy=20 → pie mid at math (-21, +24) → PIL (129, 126).
    # But the shu should be on the RIGHT of the radical. In the GT the shu
    # sits at x_PIL≈170, and its head appears to touch the pie shaft slightly
    # BELOW the pie's midpoint, where the pie is at x_PIL≈140.
    # Compromise: place shu at math x=+20 (PIL 170); shu head at PIL 140
    # (math y=+10), tail at PIL 240 (math y=-90). Center math (+20, -40).
    # Half-length = 100*0.50 = 50. Top math y = -40+50 = +10 ✓.
    draw_shu(t, ox=20, oy=-40, scale=0.50)

    out_path = os.path.join(os.path.dirname(__file__), "01_亻.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
