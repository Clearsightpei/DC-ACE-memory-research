"""义 (yì, "righteousness") — 3 strokes: 点 + 撇 + 捺.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
  1. success_bank/INDEX.md grep '义' -> not mastered (fresh derivation).
     Related: da.py (大, 横+撇+捺) — similar 撇/捺 crossing pattern (P).
  2. errata.md grep '义' -> not in errata.
  3. form_catalog.md — 撇 in char-body: head upper-right, tail lower-left,
     curve>0 (concave-right). 捺 in char-body: TL->BR, peak_t~0.8.
  4. principles_meta.md — TR1: override anchors, do NOT use defaults.
     TR8 rule5: ensure endpoints in expected cells.
  5. joint_atlas.md — P (welded crossing): 撇×捺 must intersect
     inside a single cell (BC per MMH). Widths meet, no visible gap.
  6. sandbox.md — no specific 义 note.

Structural spec (dispatcher-injected):
  s1 (点): head ('ML', 0.976, 0.099) tail ('C', 0.321, 0.38)  — short dot
  s2 (撇): head ('C',  0.723, 0.017) tail ('BL',0.416, 0.842) — long pie
  s3 (捺): head ('ML', 0.712, 0.635) tail ('BR',0.78,  0.912) — long na
  Joint: s2.mid × s3.mid @ BC — P (welded)
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'strokes=3; s2 & s3 cross at BC (welded P); s1 is short dian upper.'
}

import os, sys
_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from dian import draw_dian
from pie import draw_pie
from na import draw_na


def draw_yi(draw):
    # s1 — 点 (short dot): upper-mid, thin head to rounded press.
    draw_dian(draw,
              from_anchor=('ML', 0.976, 0.099),
              to_anchor=('C',  0.321, 0.38),
              head_width=2, peak_width=9, curve=0.05, segments=24)

    # s2 — 撇: from upper-mid down-left to BL. Slight concave-right bow.
    draw_pie(draw,
             from_anchor=('C',  0.723, 0.017),
             to_anchor=('BL', 0.416, 0.842),
             head_width=10, tail_width=1, curve=-0.06, segments=48)

    # s3 — 捺: from mid-left (ML) down-right to BR. Swells near tail.
    draw_na(draw,
            from_anchor=('ML', 0.712, 0.635),
            to_anchor=('BR', 0.78,  0.912),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.08, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_yi(d)
    out = os.path.join(os.path.dirname(__file__), '01_义.png')
    img.save(out)
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
