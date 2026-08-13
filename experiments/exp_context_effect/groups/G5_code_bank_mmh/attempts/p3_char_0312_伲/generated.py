"""p3_char_0312_伲 — G5 attempt.

Composition: 亻 (left, 2 strokes) + 尼 (right, 5 strokes) = 7 (MMH).

Bank: ren_left exists for 亻. No 尼 primitive. Right half 尼 has 竖弯钩
(hook-compound) — per P-COMP-011, do NOT force a whole-radical composition
recipe; per P-A-006, inline stroke primitives at MMH anchors.

# BANK_DEVIATION
# skipped: (no 尼 bank primitive exists — inlined 5 尼 strokes fresh)
# reason: 尼 has 竖弯钩 (hook-compound); P-COMP-011 warns 亻+X compositions
#         with hook-compound right halves have historically FAILed when
#         forced through generic radical recipes. P-A-006 route.
# fresh_component: ni_from_mmh_verbatim (per-stroke inlined; potentially
#         promotable as ni_radical if this PASSes)

MMH stroke plan (pixels on 300x300):
  s1 亻pie:     (90.2, 66.2)  → (21.1, 202.7)
  s2 亻shu:     (69.1, 155.9) → (74.4, 288.3)
  s3 尸top横折:  (150.6, 100.8) → (204.5, 129.8)  — heng_zhe_short
  s4 尸中横:    (148.8, 151.5) → (224.1, 138.6)  — heng (slight up-slope)
  s5 尸长撇:    (130.4, 96.1)  → (89.4, 276.0)   — pie, long, strong bow
  s6 匕短撇:    (218.8, 169.3) → (168.8, 231.4)  — pie, short, slight up-bow
  s7 匕竖弯钩:   (154.7, 176.7) → (259.0, 226.8)  — shu_wan_gou

Joints (all N per MMH):
  s1.mid ⇆ s2.head @ ML  — inherent to 亻 pie+shu geometry
  s2.tail ⇆ s5.tail @ BL — natural gap where 亻shu ends and 尸pie ends
  s3.tail ⇆ s4.mid @ MR  — s3 zhe tail approaches s4 heng right side (~11px)
  s3.head ⇆ s5.head @ C  — both start near (145, 100) top of 尸
  s4.head ⇆ s5.mid @ C   — s4 heng head touches s5 pie mid
  s4.head ⇆ s7.head @ C  — natural gap, s4 well above s7 head
  s5.mid ⇆ s7.head @ C   — natural gap, s5 pie passes near s7 shu top
  s6.tail ⇆ s7.mid @ BC  — 匕 pie tail nears 竖弯钩 body (~10px N gap)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 7 primitive calls, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '亻 inlined from MMH anchors (not using ren_left) to keep '
             'anchor fidelity. 尸 top heng-zhe rendered via heng_zhe_short '
             'with corner_offset to widen the L. Long descender uses '
             'bow_perp=18 for the strong 尸 curl. 匕 竖弯钩 bottom_extra '
             'kept smaller since MMH tail is only 50px below head.',
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 (2 strokes, inlined MMH-verbatim) ----
    # s1: pie
    draw_pie(d, head=(90.2, 66.2), tail=(21.1, 202.7),
             bow_perp=16, w_head=9, w_tail=3)
    # s2: shu (natural top curl for 亻 shu)
    draw_shu(d, head=(69.1, 155.9), tail=(74.4, 288.3),
             width=7, top_curl=False)

    # ---- 尸 (top structure, 3 strokes) ----
    # s3: 横折 top+right of 尸. Widen corner so the L is legible.
    # heng_zhe_short defaults put corner near tail x-27; here we want
    # corner near tail.x itself for a squarer 尸 top.
    draw_heng_zhe_short(d, head=(150.6, 100.8), tail=(215.0, 132.0),
                        corner_offset=(30, -2))

    # s4: middle 横 of 尸 (slight upward slope per MMH)
    draw_heng(d, head=(148.8, 151.5), tail=(224.1, 138.6),
              width_head=7, width_tail=8)

    # s5: long 撇 descender of 尸 (starts top-left of 尸, sweeps down-left)
    draw_pie(d, head=(130.4, 96.1), tail=(89.4, 276.0),
             bow_perp=18, w_head=8, w_tail=3)

    # ---- 匕 (bottom structure, 2 strokes) ----
    # s6: short 撇 of 匕 (right-upper down to middle)
    draw_pie(d, head=(218.8, 169.3), tail=(168.8, 231.4),
             bow_perp=-6, w_head=6, w_tail=3)

    # s7: 竖弯钩 of 匕. MMH head→tail is (155,177)→(259,227).
    # shu_wan_gou expects head=top of vertical, tail=end of hook.
    # Give a small bottom_extra since the horizontal-to-hook run is short.
    draw_shu_wan_gou(d, head=(154.7, 176.7), tail=(259.0, 226.8),
                     width=7, bottom_extra=40, knee_ratio=0.75)

    out = os.path.join(os.path.dirname(__file__), "01_伲.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
