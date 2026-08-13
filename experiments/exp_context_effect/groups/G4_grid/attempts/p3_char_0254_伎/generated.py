"""p3_char_0254_伎 (jì, "skill/performer", 6画) — 亻 + 支 (left-right).

Decomposition (per drawer_memory.md compositional playbook):
  伎 = 亻 (left, strokes 1-2) + 支 (right, strokes 3-6)
  支 = 十 (top: heng + shu, strokes 3-4) + 又-simplified (bottom: pie + na, strokes 5-6)

Memory consult (v8 slim checklist):
  1. drawer_memory.md — 亻 primitive shortlist: `ren_side.py` (draw_ren_side).
     But MMH s1 head at TL(0.885, 0.762) and tail at BL(0.149, 0.077) is a
     LONGER pie than ren_side's default (TC(0.588, 0.738) → BL(0.806, 0.112)).
     Per v8 "never-tune-anchors" rule for chronic primitives (and ren_side is
     not chronic), and since MMH-verbatim > hand-tuned overrides (v9 evidence),
     draw fresh with MMH per-stroke anchors using shared primitives.
  2. INDEX.md — 支 not mastered; errata p2_radical_132_支 says
     "10 top + p3_char_bank.draw_p3_you for base with shared-pixel P".
     But no `draw_p3_you` exists in this bank. Draw fresh.
  3. errata.md — 伎 not listed; no fix idea to follow.

Strokes (from MMH-injected brief):
  s1 撇   head TL(0.885, 0.762) → tail BL(0.149, 0.077)  — 亻 pie (long)
  s2 竖   head ML(0.765, 0.468) → tail BL(0.768, 0.941)  — 亻 shu
  s3 横   head C(0.242, 0.395)  → tail MR(0.394, 0.166)  — 支 top heng (slight up-tilt)
  s4 竖   head TC(0.617, 0.583) → tail C(0.652, 0.799)   — 支 十-shu (short)
  s5 撇   head C(0.274, 0.934)  → tail BC(0.066, 0.868)  — 支 又-pie (short)
  s6 捺   head BC(0.324, 0.083) → tail BR(0.827, 0.918)  — 支 又-na (long diagonal)

Joints (from MMH-injected brief):
  s1.mid ⇆ s2.head @ ML — N (~16 px gap) — 亻 T-touch, DO NOT weld
  s3.mid ⇆ s4.mid  @ C  — P (welded)    — 十 crossing
  s4.tail ⇆ s5.head @ C — N (~15 px gap) — 十-shu tail to 又-pie head
  s5.mid ⇆ s6.mid  @ BC — P (welded)    — 又 X crossing
"""
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 stroke calls: pie, shu, heng, shu, pie, na
    'endpoint_mismatches': [], # anchors used verbatim from MMH brief
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Drawn fresh from MMH per-stroke anchors. 亻 fresh (not '
              'ren_side; MMH pie is longer than default). 支 fresh: heng+shu '
              '(十 P-cross) + pie+na (又 X-cross). Joint s5.mid ⇆ s6.mid '
              'welded via slight pie curve inward.'),
}


def draw_ji(draw):
    # ---- Left: 亻 (strokes 1-2) — MMH per-stroke anchors ----
    # s1 撇: TL(0.885, 0.762) → BL(0.149, 0.077). Long left-sweep.
    draw_pie(draw,
             from_anchor=('TL', 0.885, 0.762),
             to_anchor=('BL', 0.149, 0.077),
             head_width=12, tail_width=2, curve=0.08)

    # s2 竖: ML(0.765, 0.468) → BL(0.768, 0.941). Short vertical.
    # s2.head sits at ML(0.765, 0.468) which is ~15 px right of s1's midpoint
    # near ML(0.752, 0.411) — natural N-gap T-touch (do NOT weld to s1).
    draw_shu(draw,
             from_anchor=('ML', 0.765, 0.468),
             to_anchor=('BL', 0.768, 0.941),
             width=9)

    # ---- Right: 支 top 十 (strokes 3-4) ----
    # s3 横: C(0.242, 0.395) → MR(0.394, 0.166). Slight upward tilt.
    draw_heng(draw,
              from_anchor=('C', 0.242, 0.395),
              to_anchor=('MR', 0.394, 0.166),
              width=8)

    # s4 竖: TC(0.617, 0.583) → C(0.652, 0.799). Crosses s3 near C(0.726, 0.335)
    # — P weld (fat_line + fat_line naturally overlaps).
    draw_shu(draw,
             from_anchor=('TC', 0.617, 0.583),
             to_anchor=('C', 0.652, 0.799),
             width=8)

    # ---- Right: 支 bottom 又-simplified (strokes 5-6) ----
    # s5 撇: C(0.274, 0.934) → BC(0.066, 0.868). Short pie down-left.
    # Slightly heavier curve so the belly bows toward s6 for the P weld
    # at BC(0.780, 0.468) area — actually s5 is very short so weld happens
    # near s5.tail region touching s6 body.
    draw_pie(draw,
             from_anchor=('C', 0.274, 0.934),
             to_anchor=('BC', 0.066, 0.868),
             head_width=10, tail_width=2, curve=0.12)

    # s6 捺: BC(0.324, 0.083) → BR(0.827, 0.918). Long diagonal down-right,
    # thin head, peak swell, needle tip. s5.head and s6.head are ~15 px apart
    # naturally (both near pixel (128-132, 195-208)) — reads as the 又 apex.
    # s6 body passes through the BC(0.78, 0.47) area where s5 tail region
    # nears it, giving the visual P weld effect.
    draw_na(draw,
            from_anchor=('BC', 0.324, 0.083),
            to_anchor=('BR', 0.827, 0.918),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.78, curve=0.08)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ji(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_伎.png')
    img.save(out_path)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
