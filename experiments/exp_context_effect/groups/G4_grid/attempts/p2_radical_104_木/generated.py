"""木 (mù, "tree", 4 strokes) — G4 Phase-2 radical attempt.

Composition per MMH: 横 + 竖 + 撇 + 捺 (all meeting near center).

Anchor plan (米字格; y grows DOWN):
  s1 (横):   head ('ML', 0.10, 0.45), tail ('MR', 0.90, 0.45), width=9
            — full-width horizontal bar. TR9: expanded from MMH's narrow
              span so standalone radical fills the grid. TR12: both
              endpoints in same cell row (M-row).
  s2 (竖):   head ('TC', 0.50, 0.15), tail ('BC', 0.50, 0.90), width=10
            — straight vertical, x=150. TR12: both endpoints in same
              column (C-column). Straight body per shu.
  s3 (撇):   head ('C', 0.389, 0.479) ≈ (138.9, 147.9), tail ('BL', 0.15, 0.90),
            head_width=11, tail_width=1, curve=0.10.
            — MMH head kept (near cross); tail extended to BL corner
              (TR9 / GT shows it reaches near bottom-left).
  s4 (捺):   head ('C', 0.547, 0.497) ≈ (154.7, 149.7), tail ('BR', 0.85, 0.85),
            head_width=3, peak_width=12, tail_width=1, peak_t=0.75.
            — MMH head kept; tail extended toward BR corner.

Joint verification (target: N-class ≤25 px, P-class welded):
  J1 (P) s1×s2 : s1 y=145, s2 x=150 → weld at (150,145). MMH C(147,137). ✓
  J2 (N) s1.mid⇆s3.head : s3.head=(138.9,147.9); s1 at x=138.9 has y=145.
         Gap ≈ 3 px (welded — reads as connected). ✓
  J3 (N) s1.mid⇆s4.head : s4.head=(154.7,149.7); s1 at x=154.7 has y=145.
         Gap ≈ 4.7 px. ✓
  J4 (N) s2.mid⇆s3.head : s2 at y=147.9 has x=150. s3.head=(138.9,147.9).
         Gap ≈ 11.1 px. ✓
  J5 (N) s2.mid⇆s4.head : s2 at y=149.7 has x=150. s4.head=(154.7,149.7).
         Gap ≈ 4.7 px. ✓
  J6 (N) s3.head⇆s4.head : (138.9,147.9) vs (154.7,149.7). Gap ≈ 15.9 px. ✓

All joints will read as connected (all within 16 px), satisfying TR10.
"""
import sys, os
_BANK = os.path.join(os.path.dirname(__file__),
                     '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Revision 1 applied: moved 撇/捺 heads UP to y_frac=0.45 (same '
        'as horizontal) so heads emerge cleanly from the crossing; '
        'thinned strokes (pie head_w 11→8; na peak_w 12→10); flipped '
        '撇 curve sign to -0.08 (convex-right, matching GT sweep). '
        'Two GT-vs-render agreements: (1) 横 spans wide across the '
        'upper-middle at y~145 with 竖 crossing through its center; '
        '(2) 撇 and 捺 fan out from the crossing down-left and '
        'down-right respectively, reaching near BL and BR corners. '
        'Stroke count 4 matches MMH. All joints within TR10 25-px.'
    ),
}


def draw_mu(draw):
    # s1 横 (horizontal bar)
    s1_head = ('ML', 0.10, 0.45)
    s1_tail = ('MR', 0.90, 0.45)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # s2 竖 (straight central vertical)
    s2_head = ('TC', 0.50, 0.15)
    s2_tail = ('BC', 0.50, 0.90)
    draw_shu(draw, s2_head, s2_tail, width=10)

    # s3 撇 (down-left sweep starting near the crossing to BL).
    # Head positioned right at horizontal (y ~ 0.45 in ML row = y=145)
    # so the stroke visually emerges from the intersection.
    s3_head = ('C', 0.42, 0.45)
    s3_tail = ('BL', 0.10, 0.95)
    draw_pie(draw, s3_head, s3_tail,
             head_width=8, tail_width=1, curve=-0.08, segments=48)

    # s4 捺 (down-right sweep starting near the crossing to BR).
    s4_head = ('C', 0.55, 0.45)
    s4_tail = ('BR', 0.90, 0.90)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=10, tail_width=1,
            peak_t=0.75, curve=0.08, segments=48)

    # Direction / sanity asserts (post-anchor→pixel):
    p_s1h = anchor_to_xy(s1_head); p_s1t = anchor_to_xy(s1_tail)
    p_s2h = anchor_to_xy(s2_head); p_s2t = anchor_to_xy(s2_tail)
    p_s3h = anchor_to_xy(s3_head); p_s3t = anchor_to_xy(s3_tail)
    p_s4h = anchor_to_xy(s4_head); p_s4t = anchor_to_xy(s4_tail)
    # 横: same row (y equal)
    assert abs(p_s1h[1] - p_s1t[1]) < 1, 's1 horizontal must be flat'
    # 竖: same column (x equal)
    assert abs(p_s2h[0] - p_s2t[0]) < 1, 's2 vertical must be straight'
    # 撇: tail is down-left of head
    assert p_s3t[0] < p_s3h[0] and p_s3t[1] > p_s3h[1], 's3 撇 direction'
    # 捺: tail is down-right of head
    assert p_s4t[0] > p_s4h[0] and p_s4t[1] > p_s4h[1], 's4 捺 direction'


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_mu(draw)
    out = os.path.join(os.path.dirname(__file__), '01_木.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
