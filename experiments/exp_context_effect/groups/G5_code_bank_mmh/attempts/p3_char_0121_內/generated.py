"""p3_char_0121_內 — G5 attempt.

4 strokes:
  1. 竖 (shu — left vertical)
  2. 横折钩 (heng_zhe_gou — top + right + hook, forming outer 冂)
  3. 撇 (pie — inner slant from top-center down to touch left vertical)
  4. 捺 (na — inner slant from center down-right, forming inner 入-like)

Uses bank primitives shu / heng_zhe_gou / pie / na. No BANK_DEVIATION.
Anchors derived from injected MMH block, adjusted for a slightly larger
box that visually matches the GT and keeps the hook well inside the canvas.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

# Import bank primitives.
BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from shu import draw_shu  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,      # 4 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'Bank primitives shu / heng_zhe_gou / pie / na. '
             'Inner pie ends tangent to left vertical near s1.mid(0.65). '
             'Inner na starts from mid of pie (natural for 入-like inner).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 竖 (left vertical) --------------------------------
    # MMH: ML(0.665,0.239) -> BL(0.665,0.83) = (66.5,123.9) -> (66.5,283)
    s1_head = (72, 78)
    s1_tail = (68, 280)
    draw_shu(d, s1_head, s1_tail, width=7)

    # ---- Stroke 2: 横折钩 (top + right + hook) -----------------------
    # MMH s2 head near ML(84,129), tail near BC(188,276). Inferred:
    #   heng_head just right of s1 head (so heads touch → N joint)
    #   corner at top-right of the box
    #   gou_tail near bottom-right, tail extends a bit past
    #   hook_tip up-and-left from gou_tail (standard 钩)
    s2_heng_head = (78, 82)
    s2_corner = (222, 82)
    s2_gou_tail = (212, 250)
    s2_hook_tip = (192, 232)
    draw_heng_zhe_gou(d, s2_heng_head, s2_corner, s2_gou_tail, s2_hook_tip)

    # ---- Stroke 3: 撇 (inner) --------------------------------------
    # MMH: head TC(133,58) -> tail BL(89,227). Tail near s1.mid(0.65).
    # Shorten the head slightly so pie starts just inside the top edge.
    s3_head = (152, 108)
    s3_tail = (75, 218)
    draw_pie(d, s3_head, s3_tail, bow_perp=10, w_head=7, w_tail=2)

    # ---- Stroke 4: 捺 (inner) --------------------------------------
    # MMH: head C(149,165) -> tail BC(194,212). Head near mid of pie.
    s4_head = (140, 165)
    s4_tail = (205, 235)
    draw_na(d, s4_head, s4_tail, bow_perp=6, w_head=3, w_tail=9)

    out = pathlib.Path(__file__).parent / '01_內.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
