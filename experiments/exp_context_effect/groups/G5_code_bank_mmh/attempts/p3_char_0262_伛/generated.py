"""p3_char_0262_伛 (yǔ, 亻+区 L-R, 6 strokes).

Recipe: P-A-006 — MMH-anchor verbatim + stroke-primitive layer.
亻 (left) = pie + shu, mirroring qian_person's 亻 anchors.
区 (right) = heng + pie + na (乂 crossing at C, P-joint) + shu_zhe (匚 outer L).

SELF_CHECK plan:
 stroke count = 6 (matches MMH).
 s1 pie head TL(0.89,0.62)=(89,62), tail BL(0.16,0.03)=(16,203).
 s2 shu head ML(0.68,0.53)=(68,153), tail BL(0.72,0.97)=(72,297).
 s3 heng head C(0.40,0.00)=(140,100), tail TR(0.40,0.87)=(240,87).
 s4 pie head MR(0.12,0.23)=(212,123), tail BC(0.48,0.39)=(148,239).
 s5 na  head C(0.59,0.51)=(159,151),  tail BR(0.37,0.38)=(237,238).
 s6 shu_zhe head TC(0.20,0.92)=(120,92), corner=(120,269), tail BR(0.65,0.69)=(265,269).
 Joint s4.mid ⇆ s5.mid @ C = P (welded X-cross, MMH dist=0).
 All other joints = N (natural gaps).
"""
import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na
from shu_zhe import draw_shu_zhe


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 recipe: 亻 pattern from qian_person; 区 inline via MMH pixels.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical) ----
    # s1: pie (long TL→BL sweep, gentle bow)
    draw_pie(d, (89, 62), (16, 203),
             bow_perp=13, w_head=9, w_tail=3, steps=90)
    # s2: shu (vertical descender)
    draw_shu(d, (68, 153), (72, 297), width=7)

    # ---- 区 (right radical: 匚 outer + 乂 inner) ----
    # s3: top heng of 匚 (slight upward slant TL→TR)
    draw_heng(d, (140, 100), (240, 87), width_head=8, width_tail=9)

    # s4: 乂 pie (down-left)
    draw_pie(d, (212, 123), (148, 239),
             bow_perp=6, w_head=8, w_tail=3, steps=70)

    # s5: 乂 na (down-right, crosses s4 at cell C — P joint welded)
    draw_na(d, (159, 151), (237, 238),
            bow_perp=10, w_head=4, w_tail=10, steps=70)

    # s6: 竖折 outer L of 匚 (top-left down to bottom-left, then across)
    draw_shu_zhe(d, (120, 92), (120, 269), (265, 269), width=7)

    out = os.path.join(os.path.dirname(__file__), '01_伛.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
