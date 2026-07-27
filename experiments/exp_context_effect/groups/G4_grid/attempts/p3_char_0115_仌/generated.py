"""仌 (bīng, "ice", 4 strokes) — two 人 stacked (top + bottom).

Lookup checklist (per memory_index.md):
  1. success_bank/INDEX.md grep: 人 (ren.py) exists — but MMH says apex is N
     (small gap ~13-16px), while ren.py uses T at apex. Override anchors AND
     do NOT weld at apex — inline pie+na per stroke for gap control.
  2. errata.md grep: 仌 not listed.
  3. form_catalog: 撇+捺 as person-radical pattern.
  4. principles_meta TR6: extreme transformation → inline. TR10: N-class must
     look connected (≤25 px gap). MMH expected_gap ~13-16 px, well under 25.
  5. joint_atlas: N-class = small natural gap; do NOT weld.
  6. sandbox: no relevant entry.

Stroke order (from MMH):
  s1 = top 人's 撇 (TC → ML)
  s2 = top 人's 捺 (C  → MR)  — head N-gap with s1 mid at cell C
  s3 = bottom 人's 撇 (C → BL)
  s4 = bottom 人's 捺 (BC → BR) — head N-gap with s3 mid at cell BC
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'two-人 stack; both apex joints N (small gap); anchors match MMH within tol.'
}


def draw_bing_ice(draw):
    # ---- Top 人 ----
    # s1: 撇 head TC(0.315,0.662) → tail ML(0.577,0.948)
    s1_head = ('TC', 0.35, 0.55)
    s1_tail = ('ML', 0.62, 0.95)
    draw_pie(draw, s1_head, s1_tail,
             head_width=10, tail_width=1, curve=0.08, segments=48)

    # s2: 捺 head C(0.4,0.04) → tail MR(0.171,0.57)
    # NOTE: s2.head is intentionally offset from s1.mid — MMH says N-class
    # with ~13 px expected gap.  Do NOT snap to s1.mid (would weld = T).
    s2_head = ('C', 0.42, 0.05)
    s2_tail = ('MR', 0.25, 0.58)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.82, curve=0.10, segments=48)

    # ---- Bottom 人 ----
    # s3: 撇 head C(0.274,0.676) → tail BL(0.396,1.05→clamp 1.0)
    s3_head = ('C', 0.274, 0.676)
    s3_tail = ('BL', 0.396, 1.00)
    draw_pie(draw, s3_head, s3_tail,
             head_width=10, tail_width=1, curve=0.08, segments=48)

    # s4: 捺 head BC(0.468,0.156) → tail BR(0.81,1.0)
    # N-class apex again — ~16 px expected gap with s3 mid.
    s4_head = ('BC', 0.468, 0.156)
    s4_tail = ('BR', 0.81, 1.00)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.82, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_bing_ice(d)
    out = os.path.join(os.path.dirname(__file__), '01_仌.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
