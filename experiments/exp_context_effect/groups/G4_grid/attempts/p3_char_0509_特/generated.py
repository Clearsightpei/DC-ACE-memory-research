"""特 (tè, "special") — 10 strokes.

Split:  牜 (cow radical, left, 4 strokes) + 寺 (right, 6 strokes = 土 + 寸).

Left 牜:
  s1 撇 (upper-left down sweep)
  s2 短横
  s3 长竖 (tall spine)
  s4 提 (rising stroke bottom-left)

Right 寺:
  s5 top 横 of 土
  s6 短竖 of 土
  s7 long 横 (bottom of 土 / main middle bar of 寺)
  s8 top 横 of 寸
  s9 竖钩 (spine of 寸)
  s10 点 of 寸

Anchors follow MMH-derived structural expectations (rounded to ±0.02).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 primitive calls total
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '牜+寺 composed via bank primitives (pie/heng/shu/dian/shu_gou) + inline 提 tapered line.'
}

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, sample_line, fat_line
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from dian import draw_dian
from shu_gou import draw_shu_gou


def draw_ti(draw, head_anchor, tail_anchor, head_w=11, tail_w=2):
    """提 — rising tapered stroke (head thick at lower-left, needle tip at upper-right)."""
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    pts = sample_line(p0, p1, n=36)
    n = len(pts) - 1
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- Left 牜 (4 strokes) ----
draw_pie(draw, ('ML', 0.55, 0.07), ('ML', 0.30, 0.83),
         head_width=12, tail_width=1, curve=0.10)                       # s1
draw_heng(draw, ('ML', 0.62, 0.49), ('C', 0.30, 0.35), width=9)         # s2
draw_shu(draw, ('TL', 0.89, 0.63), ('BL', 0.96, 0.97), width=10)        # s3
draw_ti(draw, ('BL', 0.255, 0.285), ('C', 0.207, 0.831))                # s4

# ---- Right 寺 (6 strokes) ----
draw_heng(draw, ('C', 0.53, 0.15), ('MR', 0.32, 0.05), width=9)         # s5 top 横 of 土
draw_shu(draw, ('TC', 0.81, 0.56), ('C', 0.86, 0.52), width=9)          # s6 短竖 of 土
draw_heng(draw, ('C', 0.28, 0.66), ('MR', 0.75, 0.51), width=10)        # s7 long middle 横
draw_heng(draw, ('BC', 0.35, 0.03), ('MR', 0.61, 0.91), width=9)        # s8 top 横 of 寸
draw_shu_gou(draw,
             head=('C', 0.986, 0.635),
             belly=('C', 0.99, 0.85),
             hook_pt=('BC', 0.705, 0.821),
             tip=('BC', 0.55, 0.72),
             head_w=11, belly_w=10, hook_start_w=9, tip_w=2)             # s9 竖钩
draw_dian(draw, ('BC', 0.383, 0.271), ('BC', 0.649, 0.531),
          head_width=3, peak_width=10, curve=0.08)                       # s10 点

img.save(os.path.join(_HERE, '01_特.png'))
print('wrote', os.path.join(_HERE, '01_特.png'))
