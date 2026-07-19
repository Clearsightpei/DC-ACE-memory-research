"""p2_radical_011_匕 — G3 coord-bank render.

匕 has 2 strokes:
  1) 撇 (pie): slants down-left from upper-mid, moderate length.
     GT: starts ~(150, 90) ends ~(110, 200) in PIL pixels.
     In math coords (center 150,150; +y up): start (0, +60), end (-40, -50).
     Default pie primitive runs (+65, +90) → (-45, -85) — a much longer,
     steeper diagonal than 匕's opening 撇. Scale ~0.6 gives ~
     start (+39, +54) end (-27, -51) i.e. length ~115 → we want ~110.
     Center of default pie is ((65-45)/2, (90-85)/2) = (10, 2.5).
     Target center = ((0-40)/2, (60-50)/2) = (-20, +5).
     ox = -20 - (10 * 0.6) = -26; oy = +5 - (2.5 * 0.6) = +3.5 → round to (-26, +4).
     TR-compliant: pie primitive at (ox=-26, oy=+4, scale=0.6).

  2) 竖弯钩 (shu wan gou): shaft down from ~(150, 130) to (150, 210),
     curves right to (210, 240), then upward hook to ~(210, 210) PIL px.
     In math coords: shaft top (0, +20), shaft bottom (0, -60), tail end (+60, -90),
     hook tip (+60, -60).
     Default shu_wan_gou: shaft (0, +70)→(0, -30), arc center (+40, -30) r=40,
     tail end (+80, -70), hook tip (+75, -48). Total span ox=[0..80] oy=[+70..-70].
     Default center ~= (40, 0). Target center ~= (30, -35).
     scale 0.75: default extents scaled span (0..60, +52..-52). Better ratio.
       Default at s=0.75: shaft top (0,52.5), bot (0,-22.5), arc c (30,-22.5)
       r=30, tail end (60,-52.5), hook tip (56.25,-36).
       Default center = (30, 0).
     Target center = (30, -35), so ox = 30-30 = 0, oy = -35 - 0 = -35.
     Result: shaft top (0, +17.5), bot (0, -57.5), tail end (60, -87.5),
             hook tip (56, -71). Very close to the GT reading.
     TR-compliant: shu_wan_gou primitive at (ox=0, oy=-35, scale=0.75).

  TR4 joint check: the 撇 ends around math (-27, -51) i.e. pixel (123, 201).
  The 竖弯钩 shaft top is at math (0, +17.5) i.e. pixel (150, 132.5).
  In the GT the 撇 crosses the 竖弯钩's shaft midway — the shaft top sits
  well ABOVE the pie's tail, and the pie crosses the shaft near y_pixel~170
  where shaft x=150 vs pie x at y=170 crossing ≈ interpolation of
  (150,138.5)→(123,201) at y=170 → t=(170-138.5)/(201-138.5)=0.504,
  x ≈ 150 - 0.504*27 ≈ 136. So they cross at ~(136, 170). GT shows
  the crossing point clearly. This matches; no adjustment needed.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


CANVAS_SIZE = 300
OUT = Path(__file__).parent / "01_匕.png"


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # REVISION 1 (self-check vs GT — see notes below):
    #   - First attempt's 撇 was entirely left of the shaft and didn't cross it.
    #     GT shows 撇 clearly crossing the shaft near its top. Fix: scale pie
    #     up to 0.7 and shift right so its (0, y) crossing sits ~18 px below
    #     the shaft top.
    #     Default pie start (45.5, 63) end (-31.5, -59.5) at s=0.7; center (7, 1.75).
    #     Target center math (-15, +2.5) → ox = -15-7 = -22, oy ≈ +1.
    #     Result start math (23.5, 64) PIL (173.5, 86); end math (-53.5, -58.5)
    #     PIL (96.5, 208.5). Crosses shaft x=0 at PIL y≈123 (~18 px below shaft top).
    #   - First attempt's 竖弯钩 was too small; GT spans further. Scale up to 0.9
    #     and lift slightly.
    #     At s=0.9: shaft top math y = 63+oy, bot = -27+oy. With oy=-25 → shaft
    #     top PIL 112, bot PIL 202. Arc c (30, -52) r=36; tail end PIL (216, 238);
    #     hook tip PIL (211.5, 218.2). ox = -6 (default center 36, target 30).
    draw_pie(d, ox=-22, oy=+1, scale=0.7)
    draw_shu_wan_gou(d, ox=-6, oy=-25, scale=0.9)

    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
