"""p3_char_0177_仗 — G5 attempt.

Composition: 亻 (left, ren_left bank) + 丈 (right; inline heng + pie + na).
Stroke count: 2 (ren_left) + 3 (丈: heng, pie, na) = 5 (matches MMH).

MMH anchors (PIL px, y-down):
  s1 head (99.6, 66.8) → tail (25.8, 200.7)   撇 of 亻
  s2 head (75.3, 155.9) → tail (77.9, 291.8)  竖 of 亻
  s3 head (129.2, 153.8) → tail (248.7, 133.3) heng (一) of 丈
  s4 head (177.0, 61.8) → tail (104.3, 277.4)  long pie (丿) of 丈
  s5 head (120.4, 178.7) → tail (281.0, 287.7) na (捺) of 丈

Joints:
  s1.mid ⇆ s2.head N  (inherent to 亻)
  s3.mid ⇆ s4.mid  P  (heng crosses pie at C — emerges from MMH anchors)
  s4.mid ⇆ s5.mid  P  (pie crosses na at BC — emerges from MMH anchors)

For 亻 we call the ren_left bank primitive shifted left (ox=-63, oy=0,
scale=1.0). This lands the anchors within tolerance of the MMH targets
(all deltas < 12px).
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from ren_left import draw_ren_left
from heng import draw_heng
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 2 (亻) + 3 (丈) = 5
    'endpoint_mismatches': [],    # all within ±20 px tolerance
    'joint_class_mismatches': [], # 亻 N inherent; 丈 P/P emerge from anchor crossings
    'overall_pass': True,
    'notes': 'ren_left translated ox=-63 to squeeze 亻 into left column; 丈 inline via MMH anchors.',
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 on the LEFT (2 strokes, N-joint inherent) ----
    draw_ren_left(d, ox=-63, oy=0, scale=1.0)

    # ---- 丈 inline on the RIGHT (3 strokes) ----
    # s3 一 (heng, slight upward tilt)
    draw_heng(d, (129.2, 153.8), (248.7, 133.3),
              width_head=8, width_tail=9)

    # s4 丿 (long pie sweeping top-center → bottom-left)
    draw_pie(d, (177.0, 61.8), (104.3, 277.4),
             bow_perp=14, w_head=8, w_tail=3, steps=80)

    # s5 捺 (na sweeping center → bottom-right)
    draw_na(d, (120.4, 178.7), (281.0, 287.7),
            bow_perp=14, w_head=4, w_tail=11, steps=80)

    out = os.path.join(os.path.dirname(__file__), "01_仗.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
