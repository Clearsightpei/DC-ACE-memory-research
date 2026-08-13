"""p3_char_0214_记 — 讠 (left) + 己 (right).

Composition:
- 讠 (yan_speech): 2 strokes (dian + heng_zhe_ti). Bank primitive from B3 R2 PASS.
  Placed on left ~30% of canvas.
- 己: 3 strokes (heng_zhe_short + heng + shu_wan_gou). Inlined per the
  retry_2 pattern from p2_radical_053_己__retry_2 (which was C, not
  promoted to bank). Placed on right ~65% of canvas.

MMH stroke count = 5. Matches (2 + 3 = 5).

BANK: uses draw_yan_speech from bank. 己 inlined (no bank entry).
No BANK_DEVIATION block needed — we're not skipping any bank primitive
that would fit; 己 simply has no bank entry.
"""

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from yan_speech import draw_yan_speech          # noqa: E402
from heng import draw_heng                      # noqa: E402
from heng_zhe_short import draw_heng_zhe_short  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou        # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 5 primitives: dian, heng_zhe_ti, hzs, heng, swg
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'yan_speech (left) + 己 inline (right, from retry_2 recipe).',
}


def draw_ji_self(d, ox=0, oy=0, scale=1.0):
    """Inline 己 in the right ~65% of the canvas. Reference geometry from
    p2_radical_053_己__retry_2 (which was C but visually acceptable
    structure). scale=1.0 renders in a 300-px reference frame; caller
    scales down."""
    def T(x, y):
        return (ox + x * scale, oy + y * scale)

    # s1: 横折 (top loop)
    draw_heng_zhe_short(d, head=T(78, 105), tail=T(205, 155),
                        corner_offset=(6, 0))
    # s2: middle 横
    draw_heng(d, head=T(90, 180), tail=T(200, 176),
              width_head=int(8 * scale), width_tail=int(9 * scale))
    # s3: 竖弯钩
    draw_shu_wan_gou(d, head=T(70, 150), tail=T(248, 200),
                     width=int(8 * scale),
                     bottom_extra=int(65 * scale),
                     knee_ratio=0.72)


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 讠 on left: shift left, use ~0.65 scale to fit left third.
    # Reference 讠 spans roughly x=[55, 140], y=[55, 240] in its 300 frame.
    # Scale 0.65 → span ~55 wide, ~120 tall. Shift so it sits around
    # x=15-75, y=55-175.
    draw_yan_speech(d, ox=-30, oy=15, scale=0.65)

    # 己 on right: shift right, ~0.75 scale.
    # Reference 己 spans roughly x=[65, 250], y=[100, 265]. Scale 0.75
    # → span ~140 wide, ~125 tall. Shift so top is ~y=90, left is ~x=100.
    # Ref left = 65, so ox = 100 - 65*0.75 = 51.
    # Ref top = 100, so oy = 90 - 100*0.75 = 15.
    draw_ji_self(d, ox=55, oy=15, scale=0.75)

    out_path = os.path.join(os.path.dirname(__file__), '01_记.png')
    img.save(out_path)
    print('wrote', out_path)


if __name__ == '__main__':
    main()
