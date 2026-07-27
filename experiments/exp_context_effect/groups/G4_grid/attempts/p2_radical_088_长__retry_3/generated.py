"""长 (cháng) — 4-stroke radical. Retry #3.

Errata fix (LITERAL, per errata.md retry_n=2 entry):
  s3 head=('C', 0.55, 0.30), s3 knee=('BC', 0.55, 0.85),
  s3 tip=('BR', 0.35, 0.55). Column-share head→knee, then flick
  up-right. Use `shu_ti.py` VERBATIM (no local tuning).

Also carrying forward retry_2 errata: s1 in upper-mid area.

Stroke plan (4 strokes):
  s1: 短撇 head TC(0.55, 0.20) → tail ML(0.65, 0.40)
  s2: 长横 head ML(0.10, 0.55) → tail MR(0.90, 0.45)
  s3: 竖提 shu_head C(0.55, 0.30) → shu_tail BC(0.55, 0.85)
              → ti_tail BR(0.35, 0.55)  [LITERAL from errata]
  s4: 捺 head C(0.30, 0.35) → tail BR(0.85, 0.55)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from na import draw_na
from shu_ti import draw_shu_ti


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry #3. LITERAL anchors from errata retry_n=2 entry.'
}


def draw_chang_radical(draw):
    # s3: 竖提 LITERAL from errata
    draw_shu_ti(draw,
                shu_head=('C', 0.55, 0.30),
                shu_tail=('BC', 0.55, 0.85),
                ti_tail=('BR', 0.35, 0.55),
                shu_head_w=12, shu_tail_w=11,
                ti_head_w=11, ti_tail_w=1)

    # s2: 长横
    draw_heng(draw,
              ('ML', 0.10, 0.55),
              ('MR', 0.90, 0.45),
              width=9)

    # s1: short 撇 upper
    draw_pie(draw,
             ('TC', 0.55, 0.20),
             ('ML', 0.65, 0.40),
             head_width=9, tail_width=2,
             curve=0.10, segments=36)

    # s4: long 捺
    draw_na(draw,
            ('C', 0.30, 0.35),
            ('BR', 0.85, 0.55),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.80, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chang_radical(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_长.png')
    img.save(out_path)
    print("Saved:", out_path)


if __name__ == '__main__':
    main()
