"""p3_char_0082_尢 — G5 attempt.

尢 (yóu) — 3 strokes:
  s1: 横 (rising heng)          head ML(0.571,0.482)=(57,148) → tail MR(0.273,0.295)=(227,130)
  s2: 撇 (long pie)             head TC(0.225,0.691)=(122,69) → tail BL(0.275,0.915)=(28,291)
  s3: 竖弯钩 (shu-wan-gou)      head C(0.465,0.652)=(146,165) → tail BR(0.657,0.259)=(266,226)

Joints:
  s1.mid × s2.mid : P (welded crossing) at C ~ (91,123)  [natural crossing]
  s2.mid × s3.head: N (small gap, don't weld) at C

Prior C-verdicts noted 'proportions off, tighter x-spread' — nudged the
outer x-values inward a hair while keeping MMH-derived anchor structure.

Uses bank primitives (heng, pie, shu_wan_gou). No BANK_DEVIATION.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

# add success_bank/code to path
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 primitives called for 3 MMH strokes
    'endpoint_mismatches': [],   # anchors match MMH within tolerance
    'joint_class_mismatches': [], # s1×s2 crosses (P); s3.head sits away from s2 (N)
    'overall_pass': True,
    'notes': '3-stroke 尢. Heng rises slightly (ML→MR). Long pie sweeps top-center to bottom-left. Shu_wan_gou drops from mid, sweeps right, hooks up to BR. Pie & heng cross near C for the P-joint.'
}


def draw(img):
    d = ImageDraw.Draw(img)

    # s1 — 横 (rising: tail is 18px higher than head)
    #  slight x-compression from MMH (57,148)/(227,130) to reduce spread
    draw_heng(d, head=(60, 148), tail=(222, 130),
              width_head=9, width_tail=10)

    # s2 — 撇 (long leftward sweep from top-center to bottom-left)
    #  strong bow_perp so the curve is pronounced
    draw_pie(d, head=(122, 70), tail=(30, 289),
             bow_perp=16, w_head=9, w_tail=3, steps=90)

    # s3 — 竖弯钩 (drops from mid, curves right, hooks up-right to BR)
    #  head at ~C(146,165); tail at BR(266,226); N-joint w/ s2 (no weld)
    draw_shu_wan_gou(d, head=(148, 168), tail=(263, 226),
                     width=8, bottom_extra=52, knee_ratio=0.78)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    draw(img)
    out = pathlib.Path(__file__).parent / '01_尢.png'
    img.save(out)
    print(f'wrote {out}')
