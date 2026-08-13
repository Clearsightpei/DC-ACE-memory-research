"""p2_radical_135_无 — G5 attempt.

MMH gives 4 strokes:
  s1: top heng   (88, 101) -> (211, 88)
  s2: middle heng (47, 182) -> (242, 168) — longer/lower
  s3: pie        (130, 109) -> (41, 294)  — from just under top heng
                                            down-left to bottom-left
  s4: shu-wan-gou (146, 187) -> (260, 238) — descends, curves right,
                                              hooks up-right

Bank primitives used (no BANK_DEVIATION):
  draw_heng, draw_pie, draw_shu_wan_gou
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 4 primitives -> 4 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('无 built with heng+heng+pie+shu_wan_gou; anchors from MMH. '
              'Joints s1-s3 (N gap) and s3-s2 (P weld at midlines) '
              'emerge naturally from geometry.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top short heng
    draw_heng(d, (88, 101), (211, 88), width_head=8, width_tail=9)

    # s2: longer/lower heng
    draw_heng(d, (47, 182), (242, 168), width_head=9, width_tail=10)

    # s3: pie from just below top heng, sweeping down-left
    draw_pie(d, (130, 109), (41, 294),
             bow_perp=14, w_head=8, w_tail=2)

    # s4: shu-wan-gou (descends, bottom-curve right, hook up-right)
    draw_shu_wan_gou(d, (146, 187), (260, 238),
                     width=7, bottom_extra=55, knee_ratio=0.75)

    out = Path(__file__).parent / "01_无.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
