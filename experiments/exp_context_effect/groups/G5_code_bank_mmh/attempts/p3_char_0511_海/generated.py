"""p3_char_0511_海 — 10 strokes = 氵 (left, 3) + 每 (right, 7).

STRATEGY (P-A-006 + P-A-007-v2):
- LEFT 氵: reuse the proven `fa_law.py` 氵-side coords verbatim (very-high
  reuse water radical; drawn from a passing 氵+X composition template).
- RIGHT 每: inline from stroke primitives (no whole-radical mei_ bank
  entry exists). 每 = 丿+一 (top hat, 2 strokes) + 母 (mother, 5 strokes:
  竖折 + 横折钩 + 一 crossbar + 2 dots inside).

BANK_DEVIATION: none (氵 from fa_law is direct verbatim reuse; 每 has no
bank primitive so it is legitimately inlined — not a skip).

MMH anchor cross-check (approx — 300x300 canvas):
  s1 (top pie of 每): head near TL(top-right of char) → tail down-left.
  s2 (top heng of 每): short horizontal at ~y=100.
  s3 (母 top heng/竖折 start).
  s4 (母 竖折 vertical part) etc.
"""
from PIL import Image, ImageDraw
import os, sys

_here = os.path.dirname(os.path.abspath(__file__))
_bank = os.path.abspath(os.path.join(_here, "..", "..", "success_bank", "code"))
sys.path.insert(0, _bank)

from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from ti import draw_ti
from shu_zhe import draw_shu_zhe
from heng_gou import draw_heng_gou


def render(path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ============ 氵 (left) — from fa_law.py verbatim ============
    draw_dian(d, (72.1, 84.7), (105.8, 113.7), w_head=3, w_tail=9, bow=4)
    draw_dian(d, (44.8, 137.7), (71.2, 162.0), w_head=3, w_tail=8, bow=3)
    draw_ti(d, (56.5, 281.2), (96.1, 178.4), w_head=10, w_tail=2)

    # ============ 每 (right) — 7 strokes inlined ============
    # s4 — 丿 (top pie): starts upper-right of 每, sweeps down-left
    draw_pie(d, (215.0, 55.0), (145.0, 120.0), bow_perp=10, w_head=8, w_tail=3)
    # s5 — 一 (top heng under the pie, spans across upper 每)
    draw_heng(d, (160.0, 95.0), (285.0, 90.0), width_head=6, width_tail=7)

    # 母 (mother) block — 5 strokes; tighten y-range for calligraphic proportion
    # s6 — 母's 竖折 (left vertical + short horizontal bottom, ends before right wall)
    draw_shu_zhe(d, (155.0, 135.0), (155.0, 265.0), (270.0, 265.0), width=6)
    # s7 — 母's 横折钩 (top heng, right vertical, hook back-left at bottom)
    draw_heng_gou(d, (155.0, 135.0), (275.0, 130.0), (255.0, 270.0),
                  w_start=4.0, w_corner=6.0, w_tip=3.0)
    # s8 — 母 middle 横 crossbar (extends slightly outside the box on both sides)
    draw_heng(d, (135.0, 200.0), (290.0, 195.0), width_head=7, width_tail=8)
    # s9 — upper dot inside 母
    draw_dian(d, (195.0, 155.0), (215.0, 178.0), w_head=2, w_tail=6, bow=1)
    # s10 — lower dot inside 母
    draw_dian(d, (195.0, 215.0), (220.0, 240.0), w_head=2, w_tail=6, bow=1)

    img.save(path)


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 3 (氵) + 2 (top of 每) + 5 (母) = 10 ✓
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': '氵 from fa_law verbatim; 每 inlined from primitives.'
}


if __name__ == "__main__":
    out = os.path.join(_here, "01_海.png")
    render(out)
    print(out)
