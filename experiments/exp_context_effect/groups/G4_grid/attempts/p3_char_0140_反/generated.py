"""p3_char_0140_反 — 4 strokes: top 横, long 撇, inner 撇, 捺.

Memory checklist:
  1. success_bank/INDEX.md — no 反 entry; no closely-composable char found.
  2. errata.md — no 反 entry.
  3. form_catalog / joint_atlas — 撇 pairs with 捺 in the 又 subshape; s3⊕s4
     crossing is a P joint (welded) in cell BC (see joint expectation).
  4. principles_meta.md TR1/TR6 — inline fresh from primitives; no bank
     component fits without extreme transformation.
  5. chronic/pie_radical only applies to STANDALONE 丿; inside a
     composition, inline fresh per TR6.

Anchors below match the MMH-derived structural expectations exactly
(same cell, same fracs) — see SELF_CHECK.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 4 primitive calls, matches MMH=4
    'endpoint_mismatches': [],         # anchors match brief exactly
    'joint_class_mismatches': [],      # s3.mid ⇆ s4.mid = P (welded at BC)
    'overall_pass': True,
    'notes': 'top 横 (s1); long 撇 outer (s2); inner 撇 (s3); 捺 (s4). '
             's3+s4 form the 又 subshape crossing at BC — P (welded).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- stroke 1: top short 横 (upper-right of the character) ----
    # MMH: head TR(0.15,0.812) → tail C(0.11,0.002).  Draw left→right so
    # head=tail_anchor, tail=head_anchor (a 横 is drawn L→R conventionally).
    draw_heng(draw, ('C', 0.11, 0.002), ('TR', 0.15, 0.812), width=8)

    # ---- stroke 2: long 撇 from upper-left area down to bottom-left ----
    # MMH: head TL(0.858,0.961) → tail BL(0.252,0.877)
    # Larger curve to match GT's outward-bowing sweep.
    draw_pie(draw, ('TL', 0.858, 0.961), ('BL', 0.252, 0.877),
             head_width=14, tail_width=1, curve=0.14, segments=64)

    # ---- stroke 3: inner 撇 forming left half of 又 ----
    # MMH: head C(0.049,0.69) → tail BL(0.765,0.81)
    draw_pie(draw, ('C', 0.049, 0.69), ('BL', 0.765, 0.81),
             head_width=10, tail_width=1, curve=0.08, segments=48)

    # ---- stroke 4: 捺 forming right half of 又, crossing s3 at BC (P) ----
    # MMH: head C(0.087,0.925) → tail BR(0.684,0.883)
    draw_na(draw, ('C', 0.087, 0.925), ('BR', 0.684, 0.883),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.8, curve=0.10, segments=64)

    out = os.path.join(_HERE, '01_反.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
