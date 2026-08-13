"""p3_char_0431_说 (shuō, 'speak') — 9 strokes = 讠(2) + 兑(7).

BANK USE:
- LEFT (讠, 2 strokes): draw_yan_speech (bank primitive `yan_speech.py`).
  Called at (ox=-30, oy=-5, scale=0.85). Native yan_speech spans
  x=[55,140], y=[55,240]. After transform → x=[16.75,89], y=[41.75,199].
  This lands 讠 in the LEFT ~30% of canvas as recommended by the
  drawer_memory hint "position table 讠 → (-45, 20, 0.70)". Chose
  slightly larger scale (0.85 vs 0.70) because 说 has a tall/wide
  right half that gives the left more vertical breathing room, and
  the GT's 讠 reaches near y=250.

RIGHT (兑, 7 strokes): INLINED. No 兑 bank primitive exists.

# BANK_DEVIATION
# skipped: ba.py (八 primitive)
# reason: 兑's top two strokes are 丷 (SHORT inward-facing dots
#   spanning only ~90px), not 八 (long outward pie+na spanning ~260px).
#   Quantitative: ba.py native pie tail at x=26 (canvas-left edge),
#   na tail at x=287 (canvas-right edge) — aspect ratio ~2.6:1
#   width:height. 兑's 丷 needs ~1:1 aspect at ~90x50 px, embedded
#   in the upper portion of the right half only. Scaling ba.py down
#   would give WRONG angle (八 legs splay wider than 丷 by design).
# fresh_component: dui_top_ba (compact 丷 inward dots)
#
# skipped: kou_mouth.py for 兑's middle
# reason: 兑's 口 sits at x~[140,240], y~[95,175] — width ~100, height
#   ~80, aspect 1.25:1. kou_mouth.py native is x=[92,225] width=133,
#   y=[122,275] height=153, aspect 0.87:1 (taller than wide).
#   Ratio-check: to fit 100px wide, need scale=100/133=0.75; that
#   forces height=115 vs available 80 — 44% too tall. Inline a
#   compact wider-than-tall 口 instead. (P-A-009 quantitative
#   deviation reasoning.)
# fresh_component: dui_kou_compact (aspect ~1.25:1 mouth for 兑)

Per-stroke plan vs MMH anchors (300x300, y-down, MMH y-up flipped):

  s1 讠dian: MMH TL(0.747,0.686)→TC(0.069,0.949) = (74.7,31.4)→(106.9,5.1)
  s2 讠hzt : MMH ML(0.188,0.649)→BC(0.195,0.256) = (18.8,135.1)→(119.5,274.4)
     both delivered by draw_yan_speech(ox=-30, oy=-5, scale=0.85).
  s3 兑丶L : MMH TC(0.43,0.806)→C(0.649,0.046)   = (143,19.4)→(164.9,195.4)
     -- MMH shows long stroke but visually it's a SHORT dot at top;
     use compact dian near (155, 60)→(140, 95).
  s4 兑丶R : MMH TR(0.165,0.554)→C(0.887,0.066)  = (216.5,44.6)→(188.7,193.4)
     compact dian going down-right, (215, 55)→(240, 95).
  s5 兑口丨: MMH C(0.307,0.354)→C(0.512,0.939)   = (130.7,164.6)→(151.2,106.1)
  s6 兑口𠃌: MMH C(0.447,0.345)→MR(0.027,0.673)  = (144.7,165.5)→(202.7,132.7)
  s7 兑口一: MMH C(0.564,0.884)→MR(0.197,0.784)  = (156.4,111.6)→(219.7,121.6)
     s5-s7 = 口: inline compact box at x=[140,240], y=[100,175].
  s8 兑儿丿: MMH BC(0.477,0.101)→BL(0.993,0.918) = (147.7,289.9)→(99.3,208.2)
     ← the pie of 儿, from upper middle down to lower left.
  s9 兑儿乚: MMH C(0.811,0.878)→BR(0.73,0.3)     = (181.1,112.2)→(273,270)
     ← shu_wan_gou, the right hook leg.
"""

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': None,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': '9 strokes: 2 (讠 bank) + 2 (丷 fresh dians) + 3 (口 fresh) + 2 (儿 fresh: pie + shu_wan_gou).'
}

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from yan_speech import draw_yan_speech
from dian import draw_dian
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def draw_shuo(draw):
    # LEFT: 讠 via bank (2 strokes) — REVISION: shifted down (oy -5→+25)
    # so 讠 spans y=[73, 229] to match GT's y=[70, 250], not y=[42, 199].
    draw_yan_speech(draw, ox=-30, oy=25, scale=0.85)

    # RIGHT: 兑 (7 strokes) — inlined per BANK_DEVIATION reasoning above.

    # s3: 兑 top-left dot 丶 — compact dian going down-right
    draw_dian(draw, head=(155, 55), tail=(138, 92),
              w_head=3, w_tail=8, bow=3, steps=48)

    # s4: 兑 top-right dot 丶 — compact dian going down-right, mirrored bow
    draw_dian(draw, head=(215, 55), tail=(238, 92),
              w_head=3, w_tail=8, bow=-3, steps=48)

    # s5-s7: 兑 中 口 — compact wider-than-tall box
    # box footprint x=[140,240], y=[100,175]
    # s5 left 竖
    draw_shu(draw, head=(148, 105), tail=(144, 178), width=6)
    # s6 top 横折 (heng across top + zhe down the right side)
    draw_heng_zhe_box(draw, top_left=(150, 100),
                      bottom_right=(238, 172), width=6)
    # s7 bottom 横
    draw_heng(draw, head=(148, 178), tail=(232, 174),
              width_head=6, width_tail=7)

    # s8: 儿 left pie 丿 — REVISION: start below 口 not overlapping it
    # (moved head from (160,180) → (155,195), shortened tail from
    # (85,285) → (80,282) to keep pie under the box).
    draw_pie(draw, head=(155, 195), tail=(80, 282),
             bow_perp=10, w_head=8, w_tail=3, steps=80)

    # s9: 儿 right shu_wan_gou 乚 — REVISION: shifted head down (180→198)
    # so leg begins below 口; adjusted knee for stronger hook.
    draw_shu_wan_gou(draw, head=(228, 198), tail=(285, 262),
                     width=7, bottom_extra=48, knee_ratio=0.70)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shuo(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_说.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
