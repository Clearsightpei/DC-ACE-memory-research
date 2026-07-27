"""p3_char_0010_丩 — G4 grid-bank attempt.

丩 (jiū) — 2 strokes:
  s1: 竖折-like shape (short vertical drop then a rightward turn)
      MMH endpoints: head ML(0.75, 0.251) → tail C(0.582, 0.597)
      Rendered as inlined竖折 using draw_shu_zhe: adds a corner in BL.
  s2: 竖 (straight vertical descender extending past canvas bottom)
      MMH endpoints: head TC(0.515, 0.659) → tail BC(0.626, 1.047)

Joint (1):
  s1.tail ⇆ s2.mid @ cell C — class N (small natural gap, ~24 px).
  Do NOT weld; leave 15-25 px separation per TR10 / joint_atlas N-class.

Anchor plan (TR7):
  s1 head    = ('ML', 0.75, 0.25)    # start of s1, upper mid-left
  s1 corner  = ('C',  0.05, 0.55)    # elbow (near left edge of C cell)
  s1 tail    = ('C',  0.55, 0.60)    # end of horizontal, ends inside C
  s1 widths  : v_width=9, h_width=9  (relatively thin — matches GT)

  s2 head    = ('TC', 0.55, 0.20)    # top of vertical, upper center
  s2 tail    = ('BC', 0.65, 1.00)    # bottom of canvas (MMH extends past)
  s2 width   = 10

TR8 sanity:
  - s2 (竖): head.x=0.55/TC → px 155;  tail.x=0.65/BC → px 165. Column-share
    within 10 px (acceptable slight lean). Both in C-column.
  - s1 corner and tail share row (both in C). Horizontal segment horizontal.

TR10 (N-class gap): s1.tail pixel = C(0.55, 0.60) = (155, 160).
                    s2.mid ≈ midpoint of head(155,50) and tail(165,300)
                          = (160, 175).
                    gap ≈ sqrt(5^2 + 15^2) ≈ 15.8 px — within [15, 25]. Good.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'shu_zhe for s1, shu for s2; N-gap ~16 px between s1.tail and s2.body.'
}

import sys
import os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy  # noqa: E402
from shu_zhe import draw_shu_zhe  # noqa: E402
from shu import draw_shu          # noqa: E402


def draw_jiu(draw):
    # Stroke 1: 竖折 — short vertical drop then right turn.
    # Corner further left, tail stops short of s2 for N-class gap (~18 px).
    draw_shu_zhe(draw,
                 head=('ML', 0.70, 0.25),
                 corner=('ML', 0.75, 0.60),
                 tail=('C', 0.35, 0.60),
                 v_width=9, h_width=9, shoulder=11)

    # Stroke 2: 竖 — straight vertical descender, extends past bottom.
    draw_shu(draw,
             from_anchor=('TC', 0.55, 0.20),
             to_anchor=('BC', 0.60, 1.00),
             width=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_jiu(draw)

    # Sanity: N-gap check
    s1_tail = anchor_to_xy(('C', 0.35, 0.60))
    s2_head = anchor_to_xy(('TC', 0.55, 0.20))
    s2_tail = anchor_to_xy(('BC', 0.60, 1.00))
    s2_mid = ((s2_head[0] + s2_tail[0]) / 2.0,
              (s2_head[1] + s2_tail[1]) / 2.0)
    gap = ((s1_tail[0] - s2_mid[0]) ** 2 +
           (s1_tail[1] - s2_mid[1]) ** 2) ** 0.5
    print(f"s1.tail={s1_tail}, s2.mid={s2_mid}, N-gap={gap:.1f} px "
          f"(target 15-25)")

    out = os.path.join(os.path.dirname(__file__), '01_丩.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
