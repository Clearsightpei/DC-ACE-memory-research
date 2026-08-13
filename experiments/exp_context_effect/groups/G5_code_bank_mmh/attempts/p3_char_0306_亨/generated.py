"""G5 attempt for p3_char_0306_亨 (7 strokes).

Decomposition:
  1) dian — top dot (of 亠)
  2) heng — long top horizontal (of 亠)
  3) shu — left vertical of small 口
  4) heng_zhe_box — top+right of small 口
  5) heng — bottom sealing of small 口
  6) heng — wide horizontal above the last hook (top of the 了-like tail)
  7) wan_gou — 弯钩 (curved-shaft with left-flick hook), same class as 了 s2

Bank primitives (all reference-only, TR-compliant):
  dian, heng, shu, heng_zhe_box, wan_gou (last one is the exact class
  promoted from 了 — perfect fit for the 亨 tail).
No BANK_DEVIATION needed — all primitives sit at natural scale.

Self-check block per G4/G5 mandatory pre-submit rules.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)

from dian import draw_dian            # noqa: E402
from heng import draw_heng            # noqa: E402
from shu import draw_shu              # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402
from wan_gou import draw_wan_gou      # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 stroke calls: dian, heng, shu, heng_zhe_box, heng, heng, wan_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 6 joints are N (natural gaps preserved)
    'overall_pass': True,
    'notes': 'kou box is intentionally small (upper-middle), wan_gou is the 了 tail primitive.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 1) top dot (小 丶)
    draw_dian(d, (148, 30), (170, 58), w_head=3, w_tail=7, bow=4, steps=48)

    # 2) long top heng of 亠
    draw_heng(d, (35, 85), (268, 88), width_head=8, width_tail=10)

    # 3) small 口 — left 竖  (slightly wider box, shorter)
    draw_shu(d, (108, 112), (106, 148), width=6)

    # 4) small 口 — 横折 (top+right)
    draw_heng_zhe_box(d, (106, 110), (196, 150), width=6)

    # 5) small 口 — bottom sealing 横
    draw_heng(d, (106, 150), (196, 148), width_head=6, width_tail=7)

    # 6) wide horizontal (top of 了 tail)
    draw_heng(d, (48, 185), (255, 187), width_head=8, width_tail=10)

    # 7) 弯钩 — curved-shaft with left-flick hook (same class as 了 s2)
    #    Head sits under the middle-right of stroke 6; tail curls to
    #    bottom-left with the terminal upward-left flick.
    draw_wan_gou(d, head=(178, 192), tail=(92, 260),
                 belly_right=20, hook_len=32, hook_up=16,
                 w_head=6, w_body=6, w_tail=2)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_亨.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
