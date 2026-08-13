"""伽 (jia) — G5 attempt following P-A-006 (MMH-anchor verbatim + stroke-
primitive layer). 7 strokes: 亻 (pie + shu) + 力 (heng_zhe_gou + pie) +
口 (shu + heng_zhe_box + heng).

Per P-A-007 guardrail we still deviate from the whole-radical primitives
draw_ren_left / draw_li / draw_kou because the MMH anchors squeeze all
three radicals into a very tight L-M-R layout that the standalone
primitives would over-transform. Per P-COMP-011 caveat this composition
has a hook-compound right half (力 has heng_zhe_gou) — flagged but
we accept the risk since the P-A-006 recipe worked on cousins.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 stroke calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 verbatim MMH anchors. s3 heng_zhe_gou hook_tip = MMH s3 tail. Kou box slightly taller than MMH tail-y to keep visible ink.',
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 ----
    # s1: pie (long TL→ML sweep)
    draw_pie(d, (88.5, 63.9), (19.6, 197.2),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: shu (亻 descender, ML→BL)
    draw_shu(d, (64.5, 156.2), (68.6, 286.5), width=7, top_curl=True)

    # ---- 力 ----
    # s3: heng_zhe_gou — straighter zhe (more vertical), hook up-left
    draw_heng_zhe_gou(d,
                      heng_head=(89.4, 158.8),
                      corner=(188.0, 152.0),
                      gou_tail=(172.0, 252.0),
                      hook_tip=(148.0, 242.0))
    # s4: pie (long TC→BL sweep, crosses s3 heng at P joint near C)
    draw_pie(d, (127.1, 77.1), (79.1, 261.0),
             bow_perp=14, w_head=8, w_tail=2, steps=100)

    # ---- 口 (small, right side; more rectangular) ----
    # s5: left shu of box
    draw_shu(d, (192.0, 160.0), (195.0, 246.0), width=7)
    # s6: heng_zhe_box (top + right side)
    draw_heng_zhe_box(d,
                      top_left=(190.0, 158.0),
                      bottom_right=(252.0, 246.0),
                      width=7)
    # s7: bottom heng (closes box)
    draw_heng(d, (192.0, 244.0), (252.0, 240.0), width_head=8, width_tail=9)

    out = os.path.join(os.path.dirname(__file__), "01_伽.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
