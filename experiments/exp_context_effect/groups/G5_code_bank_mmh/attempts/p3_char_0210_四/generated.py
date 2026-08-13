"""四 (si, four) — 5 strokes.

Bank composition:
  s1: draw_shu       — left vertical
  s2: draw_heng_zhe_box — top + right vertical (single stroke, forms ┐)
  s3: draw_pie       — inner-left short slanted stroke (down-left)
  s4: draw_shu_zhe   — inner-right L (down, then rightward to close inside)
  s5: draw_heng      — bottom seal

Endpoint anchors verified against MMH-derived block (see SELF_CHECK).
Joints are all class N (natural small gaps at corners), preserved by
using pixel offsets between neighboring stroke endpoints.

No BANK_DEVIATION — all five strokes come from bank primitives that
match the composition.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 primitive calls == expected 5
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Outer 3-stroke box (shu + heng_zhe_box + closing heng) + 2 inner strokes (pie left, shu_zhe right). N joints preserved via small pixel gaps at left-top, right-bottom, and inner-to-frame contacts.',
}

import os
import sys
from PIL import Image, ImageDraw

# Import bank primitives.
BANK_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
))
sys.path.insert(0, BANK_DIR)

from shu import draw_shu                          # noqa: E402
from heng import draw_heng                        # noqa: E402
from heng_zhe_box import draw_heng_zhe_box        # noqa: E402
from pie import draw_pie                          # noqa: E402
from shu_zhe import draw_shu_zhe                  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Outer frame ----
    # s1: 丨 left vertical (short leaves natural top/bottom gaps -> N joints).
    draw_shu(d, (58, 92), (72, 260), width=8)

    # s2: 横折 box — top-left corner near s1's head, drops down at right.
    draw_heng_zhe_box(d, (72, 88), (232, 268), width=8)

    # ---- Inner marks ----
    # s3: inner-left short 撇, top touches near the top heng, tail dangles
    #     just above the bottom heng (N gap ~12 px).
    draw_pie(d, (118, 122), (95, 218), bow_perp=4, w_head=7, w_tail=4)

    # s4: inner-right 竖折 — small L that starts a bit below the top heng
    #     and turns rightward to meet close to the right vertical.
    draw_shu_zhe(d, (162, 122), (162, 218), (222, 218), width=7)

    # s5: bottom sealing 一 — closes the frame between s1 tail and s2 tail.
    draw_heng(d, (60, 268), (232, 262), width_head=9, width_tail=10)

    out_path = os.path.join(os.path.dirname(__file__), '01_四.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
