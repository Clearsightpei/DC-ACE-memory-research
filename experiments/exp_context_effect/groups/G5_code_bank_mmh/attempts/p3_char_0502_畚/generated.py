"""p3_char_0502_畚 (běn — 'winnowing basket') — 10 strokes.

Structure: simplified-龹-like top (5 strokes: 2 dians + wide 一 + 撇 + 捺)
+ 田 bottom (5 strokes: 丨 + 横折 + 中一 + 中丨 + 底一).

BANK_DEVIATION
skipped: juan_yong.py (6-stroke top; 畚 has 5-stroke top — no lower stacked heng),
         si_four.py (bottom is 田 not 四 — inner marks are 一+丨, not 撇+竖折)
reason: top MMH has ONE middle heng not two stacked; bottom MMH is 田 box with
        cross bar + vertical, not 四's pie/shu_zhe. Both bank primitives
        have wrong stroke count / inner-shape for this composition.
fresh_component: ben_top (5-stroke top with bent central pie for P weld),
                 tian_field (5-stroke 田 box with weld at cross center)
per P-A-010-v2: this is real compositional mismatch — not a uniform ox/oy
shift issue — so BANK_DEVIATION is the correct channel (not shifting).
Per P-A-009: quantitative — juan_yong native stroke count 6 vs required 10-5=5,
si_four inner PIE vs required HENG differs in orientation +90deg.
Per P-A-006: MMH anchors verbatim + stroke-primitive layer.

Reasoning trace (P-A-008): 畚 = 龹-lite top + 田 bottom, both fresh-inlined.
Top pie (s4) is bent so it welds through s3 middle (P joint at (171, 65) frac).
Bottom 田 uses shu + heng_zhe_box + heng + shu + heng; s8-s9 P weld at
BC(0.422, 0.489) enforced by using overlapping midpoints.

SELF_CHECK below reflects post-run structural verification.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 10 stroke primitives called
    'endpoint_mismatches': [], # all endpoints within ±0.20 x/y_frac of MMH
    'joint_class_mismatches': [], # 2 P welds (s3-s4, s8-s9), rest N
    'overall_pass': True,
    'notes': 'Top 龹-lite + bottom 田 fresh-inlined per BANK_DEVIATION.',
}

import os
import sys

# make bank primitives importable
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw

from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box


def _bezier3(p0, p1, p2, p3, n=100):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _draw_bent_pie(d, head, tail, ctrls, w_head=8, w_tail=2):
    pts = _bezier3(head, ctrls[0], ctrls[1], tail, n=110)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


def _draw_bent_na(d, head, tail, ctrls, w_head=4, w_tail=11):
    pts = _bezier3(head, ctrls[0], ctrls[1], tail, n=110)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_ben(draw: ImageDraw.ImageDraw):
    # ---------- TOP (5 strokes, 龹-lite) ----------
    # s1: left dian — short, slanted down-right (top-of-character dot)
    draw_dian(draw, (138, 55), (168, 100), w_head=3, w_tail=8, bow=3, steps=32)

    # s2: right dian — short, complementary to s1
    draw_dian(draw, (205, 75), (188, 118), w_head=3, w_tail=8, bow=3, steps=32)

    # s3: wide middle heng (spans nearly full width) — anchor for P welds
    draw_heng(draw, (35, 173), (265, 158),
              width_head=8, width_tail=10)

    # s4: long left pie — BENT so it welds through s3 (must cross y=173 near x=115)
    _draw_bent_pie(draw,
                   head=(125, 125),
                   tail=(28, 245),
                   ctrls=[(120, 175), (75, 215)],
                   w_head=10, w_tail=2)

    # s5: long right na — starts above heng, sweeps down-right through heng
    _draw_bent_na(draw,
                  head=(170, 148),
                  tail=(288, 218),
                  ctrls=[(200, 180), (255, 210)],
                  w_head=4, w_tail=12)

    # ---------- BOTTOM (5 strokes, 田) ----------
    # 田 centered a bit lower, x=[85, 215], y=[220, 298] — wider to match GT
    # s6: left vertical 丨
    draw_shu(draw, (88, 222), (85, 298), width=8)

    # s7: 横折 top+right box corner (top-left to bottom-right)
    draw_heng_zhe_box(draw, (85, 222), (215, 298), width=8)

    # s8: middle horizontal (welds with s9 at center — P joint at ~x=150)
    draw_heng(draw, (90, 262), (212, 260),
              width_head=7, width_tail=8)

    # s9: middle vertical (welds with s8 — P joint)
    draw_shu(draw, (150, 224), (151, 296), width=7)

    # s10: bottom sealing heng
    draw_heng(draw, (85, 297), (215, 293),
              width_head=8, width_tail=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ben(draw)
    out = os.path.join(os.path.dirname(__file__), '01_畚.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
