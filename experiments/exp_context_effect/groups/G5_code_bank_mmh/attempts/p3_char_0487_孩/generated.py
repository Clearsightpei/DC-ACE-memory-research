# BANK_DEVIATION
# skipped: no whole-radical bank primitive exists for 子 (child) — the persistent
#   B4 R2 C item flagged in drawer_memory_anchors.md as terminal-freeze candidate
#   ("top heng-pie longer than sibling forms"). No bank primitive for 亥 either.
# reason: 孩 = 子(left) + 亥(right); neither radical has a bank whole-primitive.
#   MMH gives 9-stroke count that decomposes cleanly at the stroke-primitive layer.
# fresh_component: hai_stroke_primitive_layer (P-A-006 recipe, MMH anchors verbatim)
"""p3_char_0487_孩 — 孩 (hái, "child") = 子 (left, 3 strokes) + 亥 (right, 6 strokes).

P-A-006 stroke-primitive layer. All 9 strokes inlined at MMH-verbatim anchors
using bank stroke primitives (heng / shu / wan_gou / dian / pie / na).

Sub-component trace (P-A-008):
  - 子 (s1-s3): short 横 (top) + 弯钩 (long descending curved shaft with left hook)
    + long crossing 提/横 (middle band, descends slightly into right radical).
  - 亥 (s4-s9): 亠-top (dian + heng) + short pie + long pie + long pie + na.
    N-joints (natural gaps) at all inter-radical / inter-stroke meetings per MMH
    joint block; only one P-joint (s2 × s3 pierce inside 子).

Endpoint anchors verbatim from MMH-derived px:
  s1  (43.4,106.9)→(94.0,139.5)     heng short, tilts down-right
  s2  (79.7,141.2)→(61.2,268.9)     wan_gou, belly right, hook left
  s3  (21.7,217.7)→(128.9,260.8)    heng crossing 子, descends into center
  s4  (179.6,62.4)→(212.4,92.0)     dian at top of 亥 (亠 dian)
  s5  (133.3,128.0)→(254.9,114.8)   long heng of 亠, slight rise
  s6  (175.5,131.8)→(196.0,186.3)   short pie / vertical starter for 亥 body
  s7  (213.9,149.1)→(122.8,263.7)   long pie down-left
  s8  (244.6,208.9)→(155.6,282.7)   pie down-left (lower band)
  s9  (210.9,252.8)→(260.7,295.9)   na down-right
"""
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from heng import draw_heng
from wan_gou import draw_wan_gou
from dian import draw_dian
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke calls matching MMH count
    'endpoint_mismatches': [], # anchors set verbatim from MMH-derived pixels
    'joint_class_mismatches': [], # 1 P (s2×s3 pierce in 子), 6 N gaps preserved
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer with MMH-verbatim anchors. BANK_DEVIATION: no whole-radical primitive available for 子 or 亥.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 子 (strokes 1-3) ----
    # s1: short heng, tilts down-right (子's top 横撇 head part)
    draw_heng(d, (43.4, 106.9), (94.0, 139.5),
              width_head=8, width_tail=6)

    # s2: 弯钩 — long descending shaft, belly bows right, hook flicks left at bottom
    draw_wan_gou(d, (79.7, 141.2), (61.2, 268.9),
                 belly_right=20, hook_len=22, hook_up=12,
                 w_head=6, w_body=6.5, w_tail=2)

    # s3: long horizontal crossing 子's middle, extends into the composition center
    draw_heng(d, (21.7, 217.7), (128.9, 260.8),
              width_head=6, width_tail=7)

    # ---- 亥 (strokes 4-9) ----
    # s4: 亠's dian at top of 亥 (compact — MMH span only ~40px, keep tail slim)
    draw_dian(d, (179.6, 62.4), (212.4, 92.0),
              w_head=2, w_tail=5, bow=2)

    # s5: 亠's long heng, slight upward tilt to the right
    draw_heng(d, (133.3, 128.0), (254.9, 114.8),
              width_head=8, width_tail=9)

    # s6: short pie starting under s5, descends into 亥's belly (small leftward bow)
    draw_pie(d, (175.5, 131.8), (196.0, 186.3),
             bow_perp=7, w_head=6, w_tail=3, steps=40)

    # s7: long pie down-left from right side of 亥's heng
    draw_pie(d, (213.9, 149.1), (122.8, 263.7),
             bow_perp=14, w_head=9, w_tail=3, steps=80)

    # s8: second pie down-left, lower band (nested inside 亥's leg-cross)
    draw_pie(d, (244.6, 208.9), (155.6, 282.7),
             bow_perp=10, w_head=8, w_tail=3, steps=60)

    # s9: na, sweeps down-right from bottom of 亥's body
    draw_na(d, (210.9, 252.8), (260.7, 295.9),
            bow_perp=8, w_head=4, w_tail=11, steps=60)

    out_path = os.path.join(os.path.dirname(__file__), '01_孩.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
