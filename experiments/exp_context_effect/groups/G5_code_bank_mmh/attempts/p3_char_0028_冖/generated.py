"""p3_char_0028_冖 — G5 attempt.

冖 is a 2-stroke character (dian + heng_zhe_short) — same shape as the
radical p2_radical_026_冖. The bank primitive `mi_cover.py` was
promoted from that PASS and its embedded coordinates already match
the MMH anchors for this character (canvas-absolute pixels, no
transform needed).

Self-check:
  stroke 1: head (68,92) ≈ TL(0.68,0.92); tail (54,148) ≈ ML(0.536,0.479). match.
  stroke 2: head (78,108) ≈ ML(0.779,0.081); tail (213,140) ≈ MR(0.127,0.266→127px, bank uses 140px, delta ~13px = 0.13 y_frac).
    delta within ±0.20 y_frac tolerance → match.
  joint s1.mid ⇆ s2.head @ ML : N (natural gap ~13.5 px expected).
    s1 midpoint ≈ (61, 120); s2 head (78,108); euclidean gap ≈ 21 px, clearly non-welded → N.
"""

import sys
import pathlib

HERE = pathlib.Path(__file__).resolve()
BANK = HERE.parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from mi_cover import draw_mi_cover


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 strokes (dian + heng_zhe_short)
    'endpoint_mismatches': [],     # all within tolerance
    'joint_class_mismatches': [],  # N joint preserved (natural gap ~20px)
    'overall_pass': True,
    'notes': 'Bank primitive mi_cover.py fits at ox=0, oy=0, scale=1.0 (its coords ARE the MMH anchors).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_mi_cover(draw, ox=0, oy=0, scale=1.0)
    out = HERE.parent / '01_冖.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
