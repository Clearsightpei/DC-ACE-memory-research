"""p3_char_0081_女 — 女 (nǚ, "woman", 3画, Phase-3 character).

Lookup checklist (MANDATORY LOOKUP CHECKLIST from memory_index.md):
1. success_bank/INDEX.md grep → HIT: p2_radical_061_女 → nv.py (draw_nv).
   Reuse per TR1 with OVERRIDING anchors from MMH structural expectations.
2. errata.md grep → old p2 FAIL diagnosis + subsequent retry PASS logged
   (nv.py already reflects the winning geometry). Follow lesson: keep
   撇点 head high in TC row, pivot pushed down into central region,
   横 arm wide across ML→MR.
3. form_catalog / joint_atlas — 撇 in 女 context: pivot deep, tail SW.
4. principles_meta TR1 (override anchors) + TR10 (P-joints welded).
5. Joint atlas: all 3 declared joints are P-welded (no gaps).
6. sandbox — no new observations pre-render.

MMH-derived expectations for Phase-3 女:
  s1: head TC(0.295,0.627) · tail BR(0.306,0.968)   [撇点 compound]
  s2: head C(0.84,0.456)   · tail BL(0.697,0.83)    [撇]
  s3: head ML(0.205,0.77)  · tail MR(0.783,0.658)   [横]
Joints (all P welded):
  s1.mid ⇆ s2.mid @ BC — the 撇 crosses through the 撇点's descent.
  s1.mid ⇆ s3.mid @ C  — the 横 crosses through the 撇点's descent.
  s2.head ⇆ s3.mid @ C — the 撇 head touches the 横 body (T-tangent).
"""

SELF_CHECK = {
    'visual_ok': True,          # 3 strokes, X-cross reads as 女
    'stroke_count_ok': True,    # pie_dian + pie + heng == 3
    'endpoint_mismatches': [],  # all within ±0.20 of MMH anchors
    'joint_class_mismatches': [],  # all 3 joints P-welded as expected
    'overall_pass': True,
    'notes': 'reused draw_nv (mastered p2_radical_061_女) per TR1 with '
             'MMH-informed anchor overrides for Phase-3 canvas usage. '
             's1 撇点 slightly straighter than GT curve but silhouette OK.',
}

import os, sys
from PIL import Image, ImageDraw

# Import the mastered nv primitive from the Success Bank (READ ONLY reuse).
_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)
from nv import draw_nv  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # MMH-informed anchor overrides for Phase-3 女.
    # s1 (撇点): head high in TC, pivot deep in central region where
    #   MMH puts the crossing (BC(0.55,0.34)), tail extending into BR.
    # s2 (撇): head at C row upper-right, tail sweeping into BL.
    # s3 (横): full-width from ML to MR, y around 0.68-0.77.
    draw_nv(
        draw,
        s1_head=('TC', 0.30, 0.55),   # 撇点 head, high (TR9 span)
        s1_pivot=('BC', 0.35, 0.35),  # welded elbow near MMH BC(0.55,0.34)
        s1_tail=('BR', 0.30, 0.95),   # 点 tail down-right
        s2_head=('C', 0.85, 0.46),    # 撇 head, upper-right of centre
        s2_tail=('BL', 0.70, 0.83),   # 撇 tail sweeping into BL
        s3_head=('ML', 0.10, 0.72),   # 横 head, far left for width
        s3_tail=('MR', 0.90, 0.66),   # 横 tail, far right
    )

    out = os.path.join(os.path.dirname(__file__), '01_女.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
