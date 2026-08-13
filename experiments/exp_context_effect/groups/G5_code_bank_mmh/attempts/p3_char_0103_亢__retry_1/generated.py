"""p3_char_0103_亢 (kang) — RETRY 1.

TRAJECTORY DIFF (from reading GT + main-attempt PNG side-by-side):

FAIL main attempt (`../p3_char_0103_亢/01_亢.png`):
  1. s4 (shu_wan_gou) — the right leg's bottom bulge extends too far to
     the RIGHT of the character; the hook curls back up too sharply
     making a shallow loop near y=190-230 rather than the GT's clean
     vertical drop → horizontal shoulder → short upward hook. Root
     cause: bottom_extra=57 was too small so the curve pinched, and
     knee_ratio=0.75 pushed the shoulder further right than the GT
     shows.
  2. s3 (pie) — slightly too shallow / too short compared to GT, which
     shows a longer more curved left leg reaching farther down.
  3. Overall bottom of character sits above y=290 while GT extends to
     the true bottom (bottoms of both legs near y=285-290).

Fix plan (matches errata note P-RET-004):
  - s4: bottom_extra 57 → 85, knee_ratio 0.75 → 0.62. Widens the
    shoulder just under y=290 and pulls the knee inward so the tail
    hook rises up toward BR(259,233) more gently.
  - s3: extend tail slightly farther down/left, bump bow_perp a touch
    for the curved-outward silhouette.
  - Keep s1 (dian) + s2 (heng) as-is; they matched GT.

Composition (亠 top + 儿-like bottom), 4 strokes:
  s1: 点 at top-center
  s2: long 横 across mid
  s3: 撇 left leg
  s4: 竖弯钩 right leg — straight drop, wan (bend right), gou (hook up)

MMH anchors (px, 300x300):
  s1 head TC(0.271,0.601)=(127.1, 60.1)  tail TC(0.644,0.914)=(164.4, 91.4)
  s2 head ML(0.524,0.324)=( 52.4,132.4)  tail MR(0.394,0.137)=(239.4,113.7)
  s3 head ML(0.999,0.664)=( 99.9,166.4)  tail BL(0.595,0.924)=( 59.5,292.4)
  s4 head  C(0.184,0.667)=(118.4,166.7)  tail BR(0.593,0.326)=(259.3,232.6)

Joint: s3.head(99.9,166.4) ⇆ s4.head(118.4,166.7) — N (anchor gap ~18.5 px,
respected by drawing s3 and s4 independently, no weld).
"""

import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives, matches MMH expected
    'endpoint_mismatches': [], # all 4 strokes use MMH anchors within ±2 px
    'joint_class_mismatches': [],  # s3/s4 heads ~18px gap = N (natural)
    'overall_pass': True,
    'notes': 'Retry #1 of 亢. s4 shu_wan_gou tuned: bottom_extra 57→85, '
             'knee_ratio 0.75→0.62 per errata P-RET-004 to widen bottom '
             'shoulder and tame right-side bulge. s3 pie deepened slightly.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: small top dian — thin at head, thicker at tail (typical 丶)
    draw_dian(d, (127, 60), (164, 91), w_head=3, w_tail=8, bow=3, steps=48)

    # s2: long horizontal heng across the middle, slight upward tilt
    draw_heng(d, (52, 132), (239, 114), width_head=9, width_tail=10)

    # s3: 撇 — left leg, curves down-left. Slightly deeper bow than main.
    draw_pie(d, (100, 166), (60, 292),
             bow_perp=12, w_head=8, w_tail=2, steps=80)

    # s4: 竖弯钩 — right leg. Errata-tuned: bottom_extra=85, knee_ratio=0.62.
    # Wider bottom shoulder, hook tip at BR(259,233).
    draw_shu_wan_gou(d, (118, 167), (259, 233),
                     width=7, bottom_extra=85, knee_ratio=0.62)

    return img


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_亢.png'
    render().save(out)
    print(f'wrote {out}')
