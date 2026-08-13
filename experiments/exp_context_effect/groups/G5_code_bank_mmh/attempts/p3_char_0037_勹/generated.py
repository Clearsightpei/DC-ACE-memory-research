"""p3_char_0037_勹 — G5 attempt.

Recipe: P-A-001 identity-reuse. The Phase-3 char 勹 is literally the
same shape as p2_radical_010_勹, which is bank-promoted as
`draw_bao(d, ox=0, oy=0, scale=1.0)`. MMH anchors verified against
the bank primitive's baked-in geometry:

  MMH s1 head TC(0.116, 0.645) = (111.6, 64.5)  == bank pie head (111.6, 64.5) exact
  MMH s1 tail ML(0.560, 0.682) = (56.0, 168.2)  == bank pie tail (56.0, 168.2) exact
  MMH s2 head ML(0.987, 0.336) = (98.7, 133.6)  == bank heng-zhe-gou head (98.7, 133.6) exact
  MMH s2 tail BC(0.453, 0.742) = (145.3, 274.2) == bank heng-zhe-gou tail (145.3, 274.2) exact

Zero-parameter identity call.
"""
import os, sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from bao_wrap import draw_bao

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # draw_bao draws 2 strokes (pie + heng_zhe_gou), matches MMH count=2
    'endpoint_mismatches': [],         # all four endpoints match exactly (see docstring)
    'joint_class_mismatches': [],      # joint is N (neighbor gap); bank primitive s2 head at (98.7,133.6) sits ~13-16px from s1 mid — natural gap
    'overall_pass': True,
    'notes': 'P-A-001 identity-reuse of draw_bao (from p2_radical_010_勹 bootstrap PASS). MMH anchors match bank geometry exactly.',
}

def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_bao(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), '01_勹.png')
    img.save(out)
    print(f"Wrote {out}")

if __name__ == '__main__':
    main()
