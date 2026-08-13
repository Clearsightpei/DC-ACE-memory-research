"""G5 · p3_char_0331_更 · 7 strokes.

MMH decomposition (image-y down convention):
  s1 top 一       (94.6, 83.8)  → (207.4, 69.1)         — heng
  s2 left 撇      (73.8, 127.1) → (103.7, 203.9)        — pie (slight bow)
  s3 横折 (top+right of 曰 box)  (91.4, 130.4) → (193.4, 201.9) — heng_zhe_box
  s4 middle 一   (113.1, 162.6) → (176.7, 154.4)        — heng
  s5 bottom 一   (109.0, 192.5) → (183.1, 184.3)        — heng
  s6 long 撇     (129.5, 92.9)  → (40.1, 294.7)         — pie
  s7 long 捺     (67.1, 215.0)  → (275.1, 299.7)        — na

Bank usage: heng, pie, heng_zhe_box, na — all matched at MMH anchors.
No BANK_DEVIATION.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from heng import draw_heng                    # noqa: E402
from pie import draw_pie                      # noqa: E402
from na import draw_na                        # noqa: E402
from heng_zhe_box import draw_heng_zhe_box    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 7 primitive calls, one per MMH stroke
    'endpoint_mismatches': [],   # anchors used verbatim from MMH block
    'joint_class_mismatches': [], # P joints from natural stroke crossings; N joints from small MMH gaps preserved
    'overall_pass': True,
    'notes': '更 · heng + pie + heng_zhe_box + heng + heng + pie + na. '
             'Pie s6 and na s7 both cross s3 (right vert), s4 (mid heng), s5 (bot heng) '
             'inside center cell → P welds emerge naturally from line overlap. '
             's1-s6 head kept as N (~19 px gap) — s6 head just below s1.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top heng
    draw_heng(d, (94.6, 83.8), (207.4, 69.1),
              width_head=9, width_tail=10)

    # s2 — left 撇 of 曰 box (slight rightward drift as it descends)
    draw_pie(d, (73.8, 127.1), (103.7, 203.9),
             bow_perp=4, w_head=8, w_tail=6)

    # s3 — 横折: top of box (heng segment) + right vertical drop
    draw_heng_zhe_box(d, (91.4, 130.4), (193.4, 201.9), width=8)

    # s4 — middle heng inside 曰
    draw_heng(d, (113.1, 162.6), (176.7, 154.4),
              width_head=6, width_tail=7)

    # s5 — bottom heng closing 曰
    draw_heng(d, (109.0, 192.5), (183.1, 184.3),
              width_head=8, width_tail=9)

    # s6 — long 撇 leg (from top-center swooping down to bottom-left)
    draw_pie(d, (129.5, 92.9), (40.1, 294.7),
             bow_perp=18, w_head=8, w_tail=3)

    # s7 — long 捺 leg (from bottom-left area extending to bottom-right)
    draw_na(d, (67.1, 215.0), (275.1, 299.7),
            bow_perp=14, w_head=4, w_tail=11)

    out = os.path.join(os.path.dirname(__file__), '01_更.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
