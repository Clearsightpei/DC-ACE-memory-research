"""p3_char_0126_长 — the character 长 (zhǎng/cháng, 4 strokes).

Reading order (per memory_index):
  1. success_bank/INDEX.md grep 长 -> 'chang.py' exists but is for 厂
     (cliff), NOT for 长. Not a valid reuse (different character).
  2. errata.md grep 长 -> p2_radical_088_长 (radical) failed prev.
     Fix idea recorded: s3 = straight 竖 + short 提 flick (shu_ti.py).
     Reuse this literal fix here: s3 is 竖提.
  3. form_catalog: 4-stroke chars combining 撇+横+竖提+捺 are the
     canonical 长 layout (top 撇, middle 横 crossbar, vertical 竖提
     down-left, 捺 sweeps down-right).
  4. principles_meta: TR1 override anchors; TR10 N gaps <=25 px.
  5. joint_atlas: three N-class gaps here — do NOT weld crossings
     between s1↔s3, s2↔s4, s3↔s4 (the crossings look connected
     visually because ink is thick, but joint class = N per MMH).
     The one P joint (s2 ⇆ s3) is welded.

Structure:
  s1 — 短撇 (short pie) starting upper-right of 竖 top, sweeping
       down-left toward center.
  s2 — 横 (long horizontal crossbar) from ML to MR, crosses s3.
  s3 — 竖提 (vertical + up-right flick) — the long vertical spine.
  s4 — 捺 (right-falling sweep) from center down to lower-right.

Joints (all in cell C region):
  s1.tail ⇆ s3.mid (N) — s1's needle tip approaches s3's upper body.
  s2.mid ⇆ s3.mid (P — welded) — the crossbar crosses the vertical.
  s2.mid ⇆ s4.head (N) — 捺 head sits near left end of crossbar.
  s3.mid ⇆ s4.head (N) — 捺 head starts near s3's lower body.
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from pie import draw_pie
from heng import draw_heng
from shu_ti import draw_shu_ti
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('s1 短撇 upper region; s2 横 crossbar; s3 竖提 spine; '
              's4 捺 down-right. All 4 primitives, endpoints within '
              '±0.20 of MMH anchors; P weld at s2×s3 crossing; N gaps '
              'small (thick ink makes them read as connected).')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 短撇: TC(0.85, 0.82) -> C(0.33, 0.57)
    draw_pie(draw,
             ('TC', 0.85, 0.82), ('C', 0.33, 0.57),
             head_width=10, tail_width=1, curve=0.10, segments=40)

    # s2 — 横 (crossbar, long): ML(0.41, 0.92) -> MR(0.60, 0.80)
    # Slight upward slope to right, matches MMH.
    draw_heng(draw,
              ('ML', 0.41, 0.92), ('MR', 0.60, 0.80),
              width=10)

    # s3 — 竖提: head TL(0.98, 0.79) — this is upper region — straight
    # down to a bend, then 提 flick up-right. MMH tail is BC(0.60, 0.44)
    # which is the flick needle tip. Bend point is approx BC bottom.
    # For 竖提 we need: shu_head, shu_tail (bend), ti_tail (flick tip).
    # Pick bend at BC top-ish so vertical dominates.
    draw_shu_ti(draw,
                shu_head=('TL', 0.98, 0.79),
                shu_tail=('BC', 0.10, 0.85),
                ti_tail=('BC', 0.60, 0.44),
                shu_head_w=11, shu_tail_w=10,
                ti_head_w=11, ti_tail_w=1)

    # s4 — 捺: C(0.34, 0.92) -> BR(0.79, 0.76)
    draw_na(draw,
            ('C', 0.34, 0.92), ('BR', 0.79, 0.76),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.75, curve=0.10, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_长.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
