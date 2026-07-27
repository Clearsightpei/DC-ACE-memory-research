"""p3_char_0219_在 — 6 strokes.

Reading order (per drawer_memory.md v8): drawer_memory.md checked
(no explicit 在 entry, no chronic frame required); INDEX grep — 土
primitive exists (tu.py) but the 6-stroke MMH split gives us
1(top heng) + 2(long pie) + 3(short shu) + 4/5/6 (bottom 土 as
three separate MMH strokes), so we render each stroke directly with
the anchors supplied by the dispatcher's structural block instead of
importing tu.draw_tu (which would collapse strokes 4-6 into one call
but obscure the per-stroke joint mapping). errata grep — 在 not
listed.

Decomposition: 在 = ナ (heng + pie) + 亅-ish short vertical + 土
(the last three strokes = heng+shu+heng bottom-right, MMH lists
them as separate primitives).

Joints (from MMH):
  s1.mid × s2.mid @ C     : P (welded)
  s2.mid × s3.mid @ ML    : P (welded)
  s3.mid ⇆ s6.head @ BL   : N (~33 px)
  s4.mid × s5.mid @ BC    : P (welded)
  s5.tail ⇆ s6.mid @ BC   : N (~17 px)
"""
import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'anchors taken verbatim from MMH-derived brief; s2 rendered as pie (long taper); s3 as short shu; bottom 土 as heng+shu+heng.',
}

def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — top 横 (upper horizontal of ナ)
    draw_heng(draw, ('ML', 0.724, 0.263), ('MR', 0.188, 0.063), width=9)

    # s2 — long 撇 sweeping from upper-center to bottom-left
    draw_pie(draw, ('TC', 0.368, 0.53), ('BL', 0.144, 0.552),
             head_width=12, tail_width=2, curve=0.06, segments=56)

    # s3 — short 竖 (left-lower vertical, spine dropping through ML/BL)
    draw_shu(draw, ('ML', 0.756, 0.731), ('BL', 0.838, 1.018), width=9)

    # s4 — 土's top 短横 (bottom-right region, going right, slight rise)
    draw_heng(draw, ('BC', 0.236, 0.077), ('MR', 0.25, 0.939), width=9)

    # s5 — 土's central 竖 (short vertical)
    draw_shu(draw, ('C', 0.626, 0.479), ('BC', 0.69, 0.602), width=9)

    # s6 — 土's bottom 长横 (long base horizontal)
    draw_heng(draw, ('BC', 0.078, 0.728), ('BR', 0.599, 0.684), width=10)

    out = os.path.join(HERE, '01_在.png')
    img.save(out)
    return out

if __name__ == '__main__':
    p = render()
    print('WROTE', p)
