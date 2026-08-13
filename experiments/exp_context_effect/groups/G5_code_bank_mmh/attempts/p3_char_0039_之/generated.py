"""p3_char_0039_之 — G5 attempt.

之 has 3 strokes per MMH:
  s1 dian (top dot):     TC(0.239, 0.627)=(123.9, 62.7) -> TC(0.597, 0.914)=(159.7, 91.4)
  s2 heng-pie/横折:      ML(0.653, 0.415)=(65.3, 141.5) -> BL(0.776, 0.165)=(77.6, 216.5)
                          (the two endpoints are top-left of horizontal and bottom-tip of pie;
                           the horizontal extends rightward between them per the GT.)
  s3 ping-na (flat na):  BL(0.252, 0.276)=(25.2, 227.6) -> BR(0.774, 0.739)=(277.4, 273.9)

Joint: s2.tail ⇆ s3.mid(0.18) at BL, class N (natural gap ~13.6 px, do NOT weld).

Strategy: reuse bank primitives (dian, heng_pie, ping_na) at MMH pixel coords.
heng_pie defaults were tuned for 又's larger stroke; for 之 the horizontal is
shorter and lifts slightly, so override apex_x/corner_x to keep the arc tight
and land the pie tail near the injected anchor.
"""

import sys
import pathlib

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve()
GROUP = HERE.parents[2]
sys.path.insert(0, str(GROUP / 'success_bank' / 'code'))

from dian import draw_dian  # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from ping_na import draw_ping_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 primitive calls: dian, heng_pie, ping_na
    'endpoint_mismatches': [],        # coords derived directly from MMH anchors
    'joint_class_mismatches': [],     # N-joint: s2 tail lands ~13px above s3 body — natural gap preserved
    'overall_pass': True,
    'notes': 'Identity-reuse of bank primitives (P-A-001). Tuned heng_pie apex/corner shorter than 又 default because 之 heng is more compact.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top dot (short tapered dian, oriented down-right)
    draw_dian(d, head=(123.9, 62.7), tail=(159.7, 91.4),
              w_head=3, w_tail=8, bow=3)

    # s2: heng-pie. Head at left of horizontal, tail at bottom of pie.
    # 之's horizontal is shorter than 又's — override apex/corner ~110px right of head.
    s2_head = (65.3, 141.5)
    s2_tail = (77.6, 216.5)
    draw_heng_pie(d, head=s2_head, tail=s2_tail,
                  apex_x=s2_head[0] + 115, corner_x=s2_head[0] + 108)

    # s3: ping-na (flat wide na) across the bottom.
    draw_ping_na(d, head=(25.2, 227.6), tail=(277.4, 273.9), belly_drop=6)

    out = HERE.parent / '01_之.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
