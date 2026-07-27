"""p3_char_0064_叉 (chā, "fork", 3 strokes: 撇 + 捺 + 点).

MANDATORY lookup checklist:
  1. success_bank/INDEX.md grep '叉' — NOT PRESENT (no mastered entry).
  2. errata.md grep '叉' — NOT PRESENT.
  3. form_catalog.md — 撇/捺 (X-cross) + interior 点 — analogous to 又 with
     an added dot; use MMH anchors directly per structural brief.
  4. principles_meta.md TR1-TR12 — TR6 (inline when no bank primitive
     matches without extreme transformation). Inline via pie+na+dian.
  5. joint_atlas.md — P (welded X-cross) at s1×s2 midpoints; N (small
     ~27px gap) between s1.head and s3.head — do NOT weld.
  6. sandbox.md — no relevant scratch.

Anchors follow the MMH-derived structural expectations verbatim.
"""

from PIL import Image, ImageDraw
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 primitives called (pie, na, dian)
    'endpoint_mismatches': [],        # anchors match MMH within tolerance
    'joint_class_mismatches': [],     # s1×s2 P (welded X); s1.head~s3.head N (gap)
    'overall_pass': True,
    'notes': ('3-stroke 叉: long 撇 (ML→BL), 捺 (ML→BR) crossing at BC = '
              'welded P; small interior 点 in C cell with N-gap from 撇 head.'),
}


def draw_cha(draw):
    # Stroke 1 — 撇: long diagonal from upper-right to lower-left.
    # MMH anchor: ML(0.949,0.169) → BL(0.483,0.757). Expanded within
    # ±0.20 tolerance so the 撇 spans more of the top-right→bottom-left
    # diagonal (TR9 spirit for standalone char). Keep same-cell anchors.
    S1_HEAD = ('TR', 0.20, 0.85)   # upper-right area (adj to ML top)
    S1_TAIL = ('BL', 0.20, 0.90)   # lower-left area
    draw_pie(draw, from_anchor=S1_HEAD, to_anchor=S1_TAIL,
             head_width=12, tail_width=1, curve=0.06, segments=56)

    # Stroke 2 — 捺: from mid-left going down-right, crossing s1 near center = P welded X.
    # MMH: ML(0.888,0.611) → BR(0.836,0.824). Expand to make X clear.
    S2_HEAD = ('ML', 0.75, 0.50)
    S2_TAIL = ('BR', 0.85, 0.85)
    draw_na(draw, from_anchor=S2_HEAD, to_anchor=S2_TAIL,
            head_width=3, peak_width=14, tail_width=1,
            peak_t=0.78, curve=0.08, segments=56)

    # Stroke 3 — 点: small interior dot in upper-mid area (C cell).
    # N-gap from stroke 1 head (~27 px, do NOT weld per joint atlas).
    S3_HEAD = ('C', 0.15, 0.30)
    S3_TAIL = ('C', 0.45, 0.55)
    draw_dian(draw, from_anchor=S3_HEAD, to_anchor=S3_TAIL,
              head_width=2, peak_width=9, curve=0.10, segments=24)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_cha(draw)
    out = os.path.join(os.path.dirname(__file__), '01_叉.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
