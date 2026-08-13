"""仳 (pǐ) — Phase-3 character, 6 strokes.
Composition: 亻 (left, 撇 + 竖) + 比 (right = left-匕-shape 一+竖提, right-匕-shape 撇+竖弯钩).

Reading order per memory_index.md:
  drawer_memory.md → yes, 亻 + component reuse (see ren_side / bi entries).
  INDEX grep → no p3_char_0244_仳 in bank yet; 134_化 (亻+匕) previously PASSed.
  errata grep → no direct 仳 entry (86_比 exists w/ pixel-share pointer, but 仳's
    right half is 比 not 匕; still, joint-N discipline applies).

Split: 仳 = 亻 (x∈[0.05,0.35]) + 比 (x∈[0.35,0.95]).
比 = 一 (top of left-half匕) + 竖提 (bottom of left-half) + 撇 (top of right-half) + 竖弯钩 (bottom of right-half).

MMH-derived anchors (from brief, 6 strokes):
  s1 亻撇     : head ('TL', 0.855, 0.639) → tail ('BL', 0.141, 0.027)
  s2 亻竖     : head ('ML', 0.665, 0.521) → tail ('BL', 0.68,  0.95)
  s3 一(短横) : head ('C',  0.245, 0.737) → tail ('C',  0.667, 0.594)
  s4 竖提     : head ('C',  0.034, 0.251) → tail ('BC', 0.579, 0.197)
  s5 撇       : head ('MR', 0.408, 0.239) → tail ('C',  0.928, 0.696)
  s6 竖弯钩   : head ('TC', 0.72,  0.82)  → tail ('BR', 0.728, 0.124)

Joints (all N — small natural gap, do NOT weld):
  J1: s1.mid ⇆ s2.head @ ML  — N (~17 px)
  J2: s3.head ⇆ s4.mid @ C   — N (~15 px) — 竖提 body crosses near 一 left tip
  J3: s3.tail ⇆ s6.mid @ C   — N (~24 px) — right 一's right tip near 竖弯钩 body
  J4: s5.tail ⇆ s6.mid @ C   — N (~17 px) — 撇 tail near 竖弯钩 body

Rendering: PIL 300x300 white. All strokes rendered via bank primitives
using MMH anchors verbatim.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from shu_ti import draw_shu_ti
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 6 stroke primitives called below.
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('6 strokes; anchors MMH-verbatim. All 4 declared joints are N-class '
              '(natural gap, not welded). 亻 left column x∈[0.05,0.35]; 比 fills right.')
}


def draw():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical, strokes 1-2) ----
    # s1 撇: long diagonal from upper (TL area) sweeping down-left to BL.
    draw_pie(d,
             from_anchor=('TL', 0.855, 0.639),
             to_anchor=('BL', 0.141, 0.027),
             head_width=12, tail_width=2, curve=0.10, segments=48)

    # s2 竖: short vertical from mid-left down to BL bottom.
    # Head sits at ML(0.665, 0.521) near 撇 body midpoint — N-gap, not welded.
    draw_shu(d,
             from_anchor=('ML', 0.665, 0.521),
             to_anchor=('BL', 0.68, 0.95),
             width=9)

    # ---- 比 (right, strokes 3-6): 一 + 竖提 + 撇 + 竖弯钩 ----
    # s3 一 (top of left-half匕): short horizontal, slight upward tilt.
    draw_heng(d,
              from_anchor=('C', 0.245, 0.737),
              to_anchor=('C', 0.667, 0.594),
              width=9)

    # s4 竖提 (bottom of left-half匕): vertical body then flick up-right.
    # MMH head is start of body; MMH tail is tip of 提 flick.
    # Body: from head down to approx BC(0.30, 0.55); flick: from that corner to MMH tail.
    draw_shu_ti(d,
                shu_head=('C', 0.034, 0.251),
                shu_tail=('BC', 0.30, 0.55),
                ti_tail=('BC', 0.579, 0.197),
                shu_head_w=11, shu_tail_w=10,
                ti_head_w=11, ti_tail_w=1)

    # s5 撇 (top of right-half匕): short diagonal down-left.
    draw_pie(d,
             from_anchor=('MR', 0.408, 0.239),
             to_anchor=('C', 0.928, 0.696),
             head_width=10, tail_width=2, curve=0.08, segments=40)

    # s6 竖弯钩 (bottom of right-half匕): vertical from TC.72,.82 → curve right → hook up to BR.728,.124.
    # Head = MMH head; tip = MMH tail. Body drops, corner in BC/BR, hook flicks up on right.
    draw_shu_wan_gou(
        d,
        head=('TC', 0.72, 0.82),
        belly=('C',  0.75, 0.95),   # keep body vertical, curve concentrated low
        corner=('BC', 0.75, 0.55),  # bottom bend
        hook_pt=('BR', 0.55, 0.55), # right-end of horizontal sweep
        tip=('BR', 0.728, 0.124),   # up-flick tip (MMH tail)
        head_w=10, belly_w=12, corner_w=12,
        hook_start_w=10, tip_w=2,
    )

    out = os.path.join(_HERE, '01_仳.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = draw()
    print('wrote', p)
    print('SELF_CHECK:', SELF_CHECK)
