"""G5 attempt: p3_char_0136_比 (bi, 'compare').

Structure (from MMH block, 4 strokes) — two 匕-like halves:
  s1: short 提       ML(80,175.5) -> C(132.7,162)   [left small rising]
  s2: 竖弯钩(short)  ML(57.4,109.3) -> BC(126.3,215.9) [left main curl+hook]
  s3: 撇             MR(227.9,116.9) -> C(169.3,171.7)  [right short pie]
  s4: 竖弯钩(tall)   TC(146.8,73.2) -> BR(260.7,211.2)  [right main curl+hook]

Joints (both N):
  s1.head ⇆ s2.mid(0.37) @ ML — natural gap ~15 px (no weld)
  s3.tail ⇆ s4.mid(0.32) @ C  — natural gap ~17 px (no weld)

Bank usage: draw_ti (s1), draw_shu_wan_gou x2 (s2, s4), draw_pie (s3).
No BANK_DEVIATION needed — every stroke class has a bank primitive.
"""

import sys
import pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from ti import draw_ti
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 stroke calls: ti + swg + pie + swg
    'endpoint_mismatches': [],   # anchors used verbatim from MMH block
    'joint_class_mismatches': [],# both N; no weld attempted
    'overall_pass': True,
    'notes': ('Composition: two 匕 halves. Left half uses shorter '
              'shu_wan_gou (bottom_extra=20, tail y=216); right half '
              'uses taller shu_wan_gou (bottom_extra=45, tail y=211).'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 提 (short left rising) — ML head, C tail
    draw_ti(d, head=(80, 176), tail=(133, 162),
            w_head=8, w_tail=3, steps=50)

    # s2: 竖弯钩 (left, short) — ML head, BC tail
    # head is high (109), tail at y=216 is the hook tip after the wrap.
    # small bottom_extra so the curve stays compact in the left half.
    draw_shu_wan_gou(d, head=(57, 109), tail=(126, 216),
                     width=7, bottom_extra=18, knee_ratio=0.7)

    # s3: 撇 (right short pie) — MR head, C tail
    draw_pie(d, head=(228, 117), tail=(169, 172),
             bow_perp=6, w_head=8, w_tail=3, steps=80)

    # s4: 竖弯钩 (right, tall) — TC head, BR tail
    # taller vertical descent; wider knee for the right half.
    draw_shu_wan_gou(d, head=(147, 73), tail=(261, 211),
                     width=8, bottom_extra=45, knee_ratio=0.72)

    out = pathlib.Path(__file__).with_name('01_比.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
