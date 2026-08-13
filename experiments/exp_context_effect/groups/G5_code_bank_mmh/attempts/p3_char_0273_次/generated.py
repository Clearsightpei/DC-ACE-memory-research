"""p3_char_0273_次 (ci — "next"). 6 strokes: 冫 (left, 2 strokes) + 欠 (right, 4 strokes).

# BANK_DEVIATION
# skipped: bing_ice.py (draw_bing) and qian_owe.py (draw_qian)
# reason: P-A-006 5-6 stroke A-recipe — MMH-anchor verbatim + stroke-primitive layer
#         beats whole-radical composition (which double-transforms at Phase-3 aspect).
#         Also: bing_ice's second stroke is a downward dian, but 次's 冫 second stroke
#         is a rising 提 pointing toward 欠, which the whole-radical primitive doesn't
#         parameterize.
# fresh_component: 次 stroke-by-stroke inline via dian/ti/pie/heng_gou/na primitives
#                  with head/tail placed at MMH-derived pixel anchors.

MMH anchors (300x300 canvas, cell 100px, y grows DOWN):
  s1 (冫 upper dian)  head ML(0.574,0.128)=(57.4,112.8)  tail ML(0.896,0.45)=(89.6,145)
  s2 (冫 rising ti)   head BL(0.346,0.332)=(34.6,233.2)  tail ML(0.99,0.772)=(99,177.2)
  s3 (欠 short pie)   head TC(0.521,0.636)=(152.1,63.6)  tail C(0.163,0.72)=(116.3,172)
  s4 (欠 heng-gou)    head C(0.532,0.362)=(153.2,136.2)  tail MR(0.027,0.649)=(202.7,164.9)
  s5 (欠 long pie)    head C(0.488,0.717)=(148.8,171.7)  tail BL(0.771,0.842)=(77.1,284.2)
  s6 (欠 na)          head BC(0.676,0.045)=(167.6,204.5) tail BR(0.748,0.865)=(274.8,286.5)

All 3 joints are class N (natural gap) — do NOT weld.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] /
                       'success_bank' / 'code'))

from dian import draw_dian           # noqa: E402
from ti import draw_ti               # noqa: E402
from pie import draw_pie             # noqa: E402
from na import draw_na               # noqa: E402
from heng_gou import draw_heng_gou   # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints are class N (natural gap preserved)
    'overall_pass': True,
    'notes': ('P-A-006 stroke-primitive route: 冫 as dian+ti, 欠 as '
              'pie+heng_gou+pie+na. MMH anchors verbatim. N gaps '
              'preserved at s3.mid<->s4.head, s3.mid<->s5.head, '
              's5.mid<->s6.head — no welds.')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 冫 upper 点 (short down-right dian)
    draw_dian(d, head=(57.4, 112.8), tail=(89.6, 145.0),
              w_head=3, w_tail=8, bow=4)

    # s2 — 冫 rising 提 (bottom-left to middle, thick to thin)
    draw_ti(d, head=(34.6, 233.2), tail=(99.0, 177.2),
            w_head=9, w_tail=2)

    # s3 — 欠 short 撇 (top-center down-left)
    draw_pie(d, head=(152.1, 63.6), tail=(116.3, 172.0),
             bow_perp=8, w_head=6, w_tail=2)

    # s4 — 欠 横钩 (small horizontal with downward hook)
    # MMH tail treated as corner; hook_tip descends down-left.
    draw_heng_gou(d, head=(153.2, 136.2),
                  corner=(202.7, 164.9),
                  hook_tip=(192.0, 195.0),
                  w_start=3, w_corner=5, w_tip=1.5)

    # s5 — 欠 long 撇 (main body, center-mid down to bottom-left)
    draw_pie(d, head=(148.8, 171.7), tail=(77.1, 284.2),
             bow_perp=18, w_head=7, w_tail=2)

    # s6 — 欠 捺 (from mid-bottom start down-right to bottom-right)
    draw_na(d, head=(167.6, 204.5), tail=(274.8, 286.5),
            bow_perp=12, w_head=3, w_tail=10)

    out = pathlib.Path(__file__).with_name('01_次.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
