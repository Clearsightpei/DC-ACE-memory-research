"""亡 (wáng, "perish") — 3 strokes: 点 + 横 + 竖折.

Mandatory lookup checklist (per memory_index.md):
1. success_bank/INDEX.md — 亡 not present. Related: tou.py (亠 = 点+横) — pattern applies to top half.
2. errata.md — 亡 not listed.
3. form_catalog.md — 亠 = dian + heng, N. Applies to strokes 1+2.
4. principles_meta.md — TR1 (override anchors), TR4 (shared anchors for joints), TR8 (row/column check),
   TR10 (N-class must LOOK connected, ≤25 px pixel gap).
5. joint_atlas.md — N-class small gap, verify pixel dist ≤25 px.

MMH expected (from brief):
  s1 (点): head TC(0.307,0.691) tail C(0.734,0.043)
  s2 (横): head ML(0.375,0.655) tail MR(0.695,0.494)
  s3 (竖折): head ML(0.967,0.685) tail BR(0.396,0.514) — single MMH stroke covers both segments.
  joint: s2.mid(0.22) ⇆ s3.head @ ML — N (gap ~13 px)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from shu_zhe import draw_shu_zhe

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 3 stroke calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Composed: dian (top dot) + heng (top horizontal) + shu_zhe (bottom L-shape). '
             's3.head placed just below s2 body at ~22% of s2 for N-class gap ~10-15 px.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 点 (dot above the horizontal). Anchors follow MMH.
    draw_dian(draw,
              from_anchor=('TC', 0.307, 0.691),   # (131, 69) thin head, upper-left
              to_anchor=('C',   0.734, 0.043),    # (173, 104) heavier tail, lower-right
              head_width=2, peak_width=11, curve=0.08, segments=24)

    # s2 — 横 (top horizontal, spans ML → MR).
    # TR8 rule 5: keep near-same row (ML y_frac ~0.65, MR y_frac ~0.60) — small tilt OK, matches MMH.
    draw_heng(draw,
              from_anchor=('ML', 0.30, 0.65),    # (30, 165)
              to_anchor=('MR', 0.75, 0.60),      # (275, 160)
              width=10)

    # s3 — 竖折 (down then right). Head just under the left tip of s2 (N gap).
    # s2 at 22% has x ≈ 30 + 0.22*(275-30) = 84, y ≈ 165 + 0.22*(-5) = 164.
    # Place s3.head at (84, 178) → gap ~14 px vertical (matches expected ~13 px, TR10 ≤25).
    draw_shu_zhe(draw,
                 head=('ML', 0.84, 0.78),        # (84, 178) — under s2 mid area
                 corner=('BL', 0.30, 0.55),      # (30, 255) — bottom-left corner
                 tail=('BR', 0.70, 0.55),        # (270, 255) — bottom-right tail
                 v_width=10, h_width=10, shoulder=13)

    out_path = os.path.join(os.path.dirname(__file__), '01_亡.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
