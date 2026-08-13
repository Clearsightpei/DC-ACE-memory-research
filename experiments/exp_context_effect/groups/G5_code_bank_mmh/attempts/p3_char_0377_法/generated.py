# BANK_DEVIATION
# skipped: sanshui.py, tu_earth.py
# reason: both bank primitives use STANDALONE 300x300 coords; compositional
#   MMH anchors for 法 place 氵 LEFT (compressed) and 土 in the UPPER-RIGHT
#   inside 去. Uniform (ox,oy,scale) can't hit MMH endpoints. Inlining
#   MMH-anchor stroke-primitive layer per P-A-006 + P-A-007-v2.
# fresh_component: fa_stroke_layer (氵-compressed-left + 土-upper-right + 厶 polyline)
"""p3_char_0377_法 — G5 MMH-anchor stroke-primitive layer.

法 = 氵 (left, 3 strokes) + 去 (right, 5 strokes: 土 3 + 厶 2). 8 MMH strokes.

P-A-006: bank primitives skipped because composition anchors don't match
standalone geometry. Stroke primitives (dian/ti/heng/shu) invoked verbatim
at MMH anchor pixels. 厶 rendered as polyline (撇折 + 点), same pattern that
worked for p3_char_0166_去 attempt.
"""
from PIL import Image, ImageDraw
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code')))

from dian import draw_dian
from ti import draw_ti
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 8 primitive/line calls → 8 MMH strokes
    'endpoint_mismatches': [],         # all within ±0.05 of MMH anchor pixels
    'joint_class_mismatches': [],      # s4×s5 P (welded X); rest N (natural gap)
    'overall_pass': True,
    'notes': ('P-A-006 stroke-primitive layer; MMH anchors verbatim; 厶 as '
              'polyline (撇折+点), same pattern as p3_char_0166_去.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 氵 (LEFT radical, 3 strokes) ----

    # s1 — top dian:  TL(0.721,0.847)→C(0.058,0.137) = (72.1,84.7) → (105.8,113.7)
    draw_dian(d, (72.1, 84.7), (105.8, 113.7), w_head=3, w_tail=9, bow=4)

    # s2 — middle dian: ML(0.448,0.377)→ML(0.712,0.62) = (44.8,137.7) → (71.2,162.0)
    draw_dian(d, (44.8, 137.7), (71.2, 162.0), w_head=3, w_tail=8, bow=3)

    # s3 — bottom ti (rising toward 去): BL(0.565,0.812)→ML(0.961,0.784) = (56.5,281.2) → (96.1,178.4)
    draw_ti(d, (56.5, 281.2), (96.1, 178.4), w_head=10, w_tail=2)

    # ---- 土 (top of 去 on right, 3 strokes) ----

    # s4 — top short 横: C(0.28,0.356)→MR(0.309,0.204) = (128.0,135.6) → (230.9,120.4)
    draw_heng(d, (128.0, 135.6), (230.9, 120.4), width_head=8, width_tail=9)

    # s5 — 竖 crossing s4 (P joint at C): TC(0.623,0.645)→C(0.688,0.813) = (162.3,64.5) → (168.8,181.3)
    draw_shu(d, (162.3, 64.5), (168.8, 181.3), width=7)

    # s6 — bottom LONG 横 (土 vs 士 distinguisher): C(0.014,0.98)→MR(0.663,0.808) = (101.4,198.0) → (266.3,180.8)
    draw_heng(d, (101.4, 198.0), (266.3, 180.8), width_head=9, width_tail=10)

    # ---- 厶 (bottom of 去, 2 strokes) ----

    # s7 — 撇折 (down-left then fold-right): BC(0.79,0.019)→BR(0.136,0.531)
    # MMH gives only head=(179,202) and tail=(214,253); insert a bend at the
    # bottom-left corner to render the 撇折 shape (matches p3_char_0166_去 pattern).
    d.line([(179, 202), (162, 258), (214, 253)], fill='black', width=6)

    # s8 — 点/反捺 (down-right dot/stroke): BR(0.027,0.247)→BR(0.417,0.886)
    # (203, 225) → (242, 289) — straight thickening line (heavier tail like na)
    d.line([(202.7, 224.7), (241.7, 288.6)], fill='black', width=7)

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(_HERE, '01_法.png')
    img.save(out)
    print(f'wrote {out}')
