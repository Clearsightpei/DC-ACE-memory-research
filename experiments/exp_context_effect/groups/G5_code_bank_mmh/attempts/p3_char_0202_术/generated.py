"""p3_char_0202_术 — G5 attempt.

术 = 木 (4 strokes) + 丶 (dot on upper right, s5).

MMH stroke count: 5. Bank reuse:
- draw_mu(d, 0, 0, 1.0) covers s1-s4 (heng+shu+pie+na); anchors align
  within tolerance vs MMH injection (see SELF_CHECK below).
- draw_dian for s5 (upper-right dot).
"""
import sys
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from PIL import Image, ImageDraw

from mu_wood import draw_mu
from dian import draw_dian

# ---------- SELF_CHECK block (mandatory) ----------
# Expected stroke count: 5
# Expected anchors (from MMH injection):
#   s1: head ML(0.621,0.482)=(62.1,148.2)  tail MR(0.25,0.33)=(225,133)
#   s2: head TC(0.351,0.618)=(135.1,161.8) tail BC(0.436,1.038)=(143.6,303.8)
#       (note: for anchor pixels we use cell_origin + frac*100; TC cell origin
#        y=0, x=100; so TC(.351,.618)=(135.1,61.8); BC origin (100,200) →
#        BC(.436,1.038)=(143.6,303.8))
#   s3: head C(0.4,0.506)=(140,150.6)    tail BL(0.337,0.763)=(33.7,276.3)
#   s4: head C(0.576,0.506)=(157.6,150.6) tail BR(0.845,0.651)=(284.5,265.1)
#   s5: head TC(0.898,0.721)=(189.8,72.1) tail TR(0.235,0.993)=(223.5,99.3)
# draw_mu at ox=0,oy=0,scale=1.0 uses:
#   s1 (66.8,143.6)->(224.4,131.8)  delta ~(4.7,4.6) / (0.6,1.2)  OK
#   s2 (132.7,58.3)->(142.4,295.0)  delta ~(2.4,3.5) / (1.2,8.8)  OK
#   s3 (138.9,147.9)->(38.1,263.7)  delta ~(1.1,2.7) / (4.4,12.6) OK
#   s4 (154.7,149.7)->(278.6,253.4) delta ~(2.9,0.9) / (5.9,11.7) OK
# All endpoint deltas within adjacent-cell tolerance.
# Joints: s1 crosses s2 at C (P — welded via mu_wood natural overlap).
#         s1-s3, s1-s4, s2-s3, s2-s4, s3-s4 all N (small natural gap from
#         mu_wood's slight below-heng offsets and pie/na fork origin).
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 (mu) + 1 (dian) = 5
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'draw_mu identity-call + draw_dian for upper-right dot (术=木+丶).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1-s4: 木 body via bank identity call
    draw_mu(d, 0, 0, 1.0)

    # s5: upper-right 丶 (short tapered dot, head thin at upper-left,
    #     tail thick at lower-right)
    draw_dian(
        d,
        head=(189.8, 72.1),
        tail=(223.5, 99.3),
        w_head=2, w_tail=6, bow=3, steps=32,
    )

    out = pathlib.Path(__file__).with_name('01_术.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
