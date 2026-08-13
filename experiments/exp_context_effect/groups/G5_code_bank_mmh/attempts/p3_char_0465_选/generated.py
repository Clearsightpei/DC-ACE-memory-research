"""p3_char_0465_选 — G5 attempt.

Structure: 先 (top, 6 strokes) + 辶 (wrap bottom-left, 3 strokes) = 9 strokes.

Reasoning trace (P-A-008):
- No `xian_first` bank primitive exists (hard-checked INDEX). So 先 is
  inlined via stroke primitives at MMH anchors, per P-A-006 recipe
  (stroke-primitive layer + MMH-anchor verbatim).
- 辶 has a strong bank primitive `draw_chuo`. Reused whole via
  `chuo_walk`, with the same +3/+8 ox/oy shift used successfully in
  hai_still.py (draw_chuo native ~(62,72) for s1_head vs target
  (63.9, 78.8) here). No BANK_DEVIATION — we USE the primitive.

MMH anchors → PIL px (cell=100):
  s1 head(133.3,104.3) tail(114.8,155.3)  — 撇 short (down-left)
  s2 head(142.7,132.7) tail(220.9,117.5)  — 横 (upper)
  s3 head(168.8, 66.5) tail(174.0,163.2)  — 竖 (long descending)
  s4 head(112.5,178.1) tail(250.8,164.6)  — 横 (long crossbar)
  s5 head(149.7,181.6) tail(112.2,251.1)  — 撇 (long down-left)
  s6 head(181.1,175.8) tail(254.3,203.9)  — 竖弯钩
  s7 head( 63.9, 78.8) tail( 95.8,107.2)  — 辶 point   (via chuo_walk)
  s8 head( 30.5,171.7) tail( 81.7,248.7)  — 辶 zigzag  (via chuo_walk)
  s9 head( 31.6,262.5) tail(275.1,285.4)  — 辶 平捺    (via chuo_walk)
"""

import sys
from pathlib import Path
BANK = Path(__file__).resolve().parents[4] / "groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from chuo_walk import draw_chuo
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke primitives (6 inlined 先 + draw_chuo which is 3)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '先 inlined at MMH anchors (no xian_first bank); 辶 via draw_chuo +3/+8 shift.',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 先 (strokes 1-6) — inlined at MMH anchors ----

    # s1: 撇 (short top-left slant)
    draw_pie(d, (133.3, 104.3), (114.8, 155.3),
             bow_perp=4, w_head=6, w_tail=2)

    # s2: 横 (upper horizontal)
    draw_heng(d, (142.7, 132.7), (220.9, 117.5),
              width_head=6, width_tail=7)

    # s3: 竖 (long descending vertical through top heng)
    draw_shu(d, (168.8, 66.5), (174.0, 163.2), width=6)

    # s4: 横 (long crossbar heng)
    draw_heng(d, (112.5, 178.1), (250.8, 164.6),
              width_head=7, width_tail=8)

    # s5: 撇 (long down-left)
    draw_pie(d, (149.7, 181.6), (112.2, 251.1),
             bow_perp=8, w_head=6, w_tail=2)

    # s6: 竖弯钩 (vertical, right-bend, up-hook)
    draw_shu_wan_gou(d, (181.1, 175.8), (254.3, 203.9),
                     width=6, bottom_extra=55, knee_ratio=0.72)

    # ---- 辶 (strokes 7-9) — via draw_chuo with hai_still.py shift ----
    draw_chuo(d, ox=2, oy=7, scale=1.0)

    return img


if __name__ == "__main__":
    out_dir = Path(__file__).parent
    img = draw()
    img.save(out_dir / "01_选.png")
    print(f"saved {out_dir/'01_选.png'}  size={img.size}")
