"""p3_char_0393_实__retry_1 — 实 (shí, "real") — 8 strokes = 宀 + 头.

# TRAJECTORY DIFF (from Reading GT + prior FAILED main attempt PNG)
# GT visual: 宀 top clean with dian + short pie + heng-with-tiny-hook;
#   center has two small right-slanting ticks (upper 头 marks);
#   bottom is a 大-like shape: wide heng crossing pie near its lower
#   half, na starting near heng-midline and sweeping down-right.
#   Everything fits within canvas; the 大 heng is horizontally wide
#   and around y~200; pie tail stops near y~285; na tail near y~290.
#
# main FAIL got wrong (visual gaps):
#   1. Bottom heng was RAW-MMH-low (y~232, MMH BL 0.329) — visually
#      too low; GT has it around y=200. Off by ~30 px.
#   2. Pie head was placed at raw-MMH y=131 (inside 宀 area) and
#      tail extended off canvas to y=306 (raw MMH tail y=1.064). The
#      pie should visibly start ~y=140-150 and end AT/BEFORE y=290.
#   3. Na was too short (177->227 x, only 50 px horizontal) — GT na
#      spans ~150→245 with visible thick belly. Failed na barely
#      swept.
#   4. Top 宀 corner-hook of heng_zhe_short was rendered but the
#      middle 头-marks (s4, s5) sat too close together and both hidden
#      under the roof; GT shows two ticks visibly BELOW the roof.
#
# Fixes this retry (per errata cluster D + P-A-010 kind-b/c):
#   a. Use ding_fix's proven 宀 anchors (which PASSED in B10) verbatim
#      for the top — those matched 实's very similar 宀 aspect.
#   b. Shift bottom heng UP from y=232 → y~200 so it sits at visible
#      GT position; adjust s6 endpoints while keeping ~same length.
#   c. Clip pie tail to y≤285 (draw within canvas) — head at (155,145),
#      tail at (60, 285); belly bows left slightly (bow_perp negative
#      for da-style crossing per P-A-005).
#   d. Widen na horizontal sweep to ~150 → 245.
#   e. Shift s4, s5 down slightly so they sit visibly below roof at
#      y~155-190 (inside 宀 but visible as ticks).

# BANK_DEVIATION
# skipped: mian_roof.py
# reason: 实's 宀 aspect (W/H ~1.45) is JUST below mian_roof's native
#   aspect (2.43) ratio 0.60 (below P-A-007-v2 lower 0.55). BUT the
#   B10 PASSED ding_fix used inline 宀 at essentially the same
#   anchors as 实 needs. Following the B12 errata recommendation
#   (kind-b: correct primitive mistuned → use ding_fix's proven
#   inline template) rather than trying to squeeze mian_roof.
# fresh_component: mian_for_实 (copy of ding_fix's proven inline 宀)
"""

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,      # 8 explicit stroke-primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'ding_fix 宀 template + retuned 大-bottom to fit canvas.',
}

import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from dian import draw_dian
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short
from na import draw_na
from pie import draw_pie


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 宀 top (3 strokes) — copied from ding_fix (B10 PASS) ----
    # s1: TC dian
    draw_dian(d, (127.7, 53.0), (159.1, 79.4),
              w_head=3, w_tail=8, bow=3, steps=48)
    # s2: left pie
    draw_pie(d, (67.1, 105.8), (57.1, 164.4),
             bow_perp=4, w_head=6, w_tail=3, steps=60)
    # s3: heng_zhe_short (top bar + hook down-right)
    draw_heng_zhe_short(d, (79.7, 123.6), (203.3, 155.0),
                        corner_offset=(-6, -4))

    # ---- 头 top ticks (2 strokes) — visible below roof ----
    # s4: small dian upper-inside (left tick)
    draw_dian(d, (100.0, 145.0), (125.0, 168.0),
              w_head=2, w_tail=5, bow=2, steps=40)
    # s5: another dian (right tick, slightly lower)
    draw_dian(d, (90.0, 175.0), (120.0, 200.0),
              w_head=2, w_tail=6, bow=3, steps=48)

    # ---- 大-shape bottom (3 strokes) ----
    # s6: long heng crossing full width around y~200
    draw_heng(d, (45.0, 205.0), (255.0, 195.0),
              width_head=8, width_tail=8)
    # s7: 大's 丿 — piercing pie from center-upper down-left
    draw_pie(d, (155.0, 145.0), (55.0, 285.0),
             bow_perp=-18, w_head=8, w_tail=3, steps=100)
    # s8: 大's 捺 — from just below heng-center sweeping down-right
    draw_na(d, (150.0, 210.0), (250.0, 285.0),
            bow_perp=14, w_head=4, w_tail=11, steps=100)

    img.save(out_path)
    return out_path


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_实.png')
    render(out)
    print('wrote', out)
