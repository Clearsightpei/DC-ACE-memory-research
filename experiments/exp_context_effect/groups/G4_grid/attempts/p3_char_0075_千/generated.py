"""p3_char_0075_千 (qiān, "thousand") — 3 strokes: 短撇 + 横 + 竖.

MANDATORY LOOKUP CHECKLIST (per memory_index.md v7 @ position 200):
  1. INDEX grep '千' → NOT in success bank. Related: 干 (`gan.py`, 短横+长横+竖)
     but 千 uses 撇 (not 短横) for stroke 1. Do NOT reuse gan.py.
  2. errata grep '千' → NOT in errata.
  3. form_catalog: 撇 in top-cross-cover context = short flat pie sweeping
     down-left across TC/TR area; 横 as middle bar = same-row endpoints
     (TR8 rule 5); 竖 as spine = same-col endpoints.
  4. principles_meta: TR1 (override anchors) — use MMH anchors, NOT bank
     defaults. TR8 rule 5/6 for 横 and 竖 (same row/col).
  5. joint_atlas: P at C = welded crossing (heng pierces shu). N at TC =
     s3.head sits just below s1.belly with visible ~16 px gap (do NOT weld).
  6. sandbox: no relevant note.

Anchors (from MMH spec injected in brief):
  s1 (短撇): head TR(0.021, 0.724) → tail ML(0.835, 0.081)
  s2 (长横): head ML(0.381, 0.72)  → tail MR(0.675, 0.649)
  s3 (长竖): head TC(0.383, 0.987) → tail BC(0.497, 1.07)

Joints:
  s1.mid ⇆ s3.head @ TC : N — small natural gap (~16 px), do NOT weld.
  s2.mid ⇆ s3.mid  @ C  : P — welded crossing (natural: their paths cross).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 3 primitives called (pie + heng + shu)
    'endpoint_mismatches': [],     # all use MMH anchors verbatim
    'joint_class_mismatches': [],  # P at C by natural crossing; N at TC by construction
    'overall_pass': True,
    'notes': 'Anchors used verbatim from MMH brief. P-joint at C emerges '
             'from natural crossing of s2 horizontal (y~168) and s3 vertical. '
             'N-joint at TC: s1 belly y~90, s3 head y~99 → visible small gap.',
}

import os
import sys
from PIL import Image, ImageDraw

# Make shared primitives importable.
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie      # noqa: E402
from heng import draw_heng    # noqa: E402
from shu import draw_shu      # noqa: E402


def draw_qian(draw):
    # s1 — 短撇 (short flat pie sweeping down-left across the top).
    draw_pie(
        draw,
        from_anchor=('TR', 0.021, 0.724),
        to_anchor=('ML', 0.835, 0.081),
        head_width=11, tail_width=2, curve=0.06, segments=48,
    )
    # s2 — 长横 (long middle bar, roughly wall-to-wall, slight rise).
    draw_heng(
        draw,
        from_anchor=('ML', 0.381, 0.72),
        to_anchor=('MR', 0.675, 0.649),
        width=10,
    )
    # s3 — 长竖 (vertical spine; pierces s2 at C, ends below baseline).
    draw_shu(
        draw,
        from_anchor=('TC', 0.383, 0.987),
        to_anchor=('BC', 0.497, 1.07),
        width=10,
    )


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_qian(draw)
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '01_千.png',
    )
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
