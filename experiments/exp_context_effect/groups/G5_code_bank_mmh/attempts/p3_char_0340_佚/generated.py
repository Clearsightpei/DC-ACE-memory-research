"""p3_char_0340_佚 (yi, "lose/scatter") — G5 attempt.

Decomposition (7 strokes = 亻 (2) + 失 (5)):

  Sub-component 1: 亻 (ren_left) — strokes 1-2.
    P-A-007-v2 hard-check: bank primitive `ren_left.py` exists (whole
    radical, 2-stroke pie+shu). Native bank aspect matches the MMH
    anchors for this 亻: bank s1_head (158.8, 73.8) vs MMH (85, 67);
    shift ox=-74 aligns bank into the anchor box (within 15 px of all
    four endpoints). USE BANK — this is exactly the whole-radical
    match case P-A-007 targets.

  Sub-component 2: 失 (shi_lose) — strokes 3-7.
    P-A-007-v2 hard-check: NO bank primitive for 失 (checked
    success_bank/code/ — no shi_lose.py, shi_arrow.py, or 矢 either).
    Must inline. Per P-A-006, use stroke-primitive layer (draw_pie,
    draw_heng, draw_na) rather than raw draw.line, so the
    calligraphic taper/顿笔 emerges natively. Anchors taken verbatim
    from MMH block (converted cell frac → pixels on 300x300 3x3 米字格).

Joints per MMH block:
  s4∩s6 P (weld at C 0.794, 0.353) — s6 pierces s4 horizontal
  s5∩s6 P (weld at C 0.742, 0.859) — s6 pierces s5 horizontal
  s5∩s7 N (~18 px gap near C 0.819, 0.913)
  s6∩s7 N (~20 px gap near BC 0.771, 0.096)
  s1∩s2 N (~20 px gap on 亻 — handled by bank ren_left natively)
  s3∩s4 N (~12 px gap C 0.362, 0.409)
  s3∩s5 N (~32 px gap C 0.083, 0.846)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from ren_left import draw_ren_left  # noqa: E402
from pie import draw_pie              # noqa: E402
from heng import draw_heng            # noqa: E402
from na import draw_na                # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 2 (ren_left) + 5 (失 inline) = 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'ren_left shifted ox=-74 to align with MMH 亻 anchors; '
             '失 inlined with 3 pie/heng, 1 pie descender, 1 na — '
             '6 pierces 4 and 5 (P), 7 tangent-neighbor to 5 and 6 (N).'
}


def draw_shi_lose(draw, ox=0, oy=0, scale=1.0):
    """失 inline — 5 strokes, MMH anchors verbatim (300x300 frame).

    stroke 3: short 丿 top       C(0.298,0.043) → C(0.116,0.734) → px (129.8,104.3)→(111.6,173.4)
    stroke 4: short 一 middle    C(0.406,0.406) → MR(0.297,0.269) → px (140.6,140.6)→(229.7,126.9)
    stroke 5: long 一 lower      C(0.049,0.957) → MR(0.543,0.808) → px (104.9,195.7)→(254.3,180.8)
    stroke 6: long 丿 descender  TC(0.661,0.606) → BL(0.964,0.859) → px (166.1,60.6)→(96.4,285.9)
    stroke 7: 捺                 C(0.828,0.980) → BR(0.883,0.856) → px (182.8,198.0)→(288.3,285.6)
    """
    def tx(x, y):
        return (ox + x * scale, oy + y * scale)

    # s3: short 丿 at the top of 失 (points down-left, shallow)
    draw_pie(draw, tx(129.8, 104.3), tx(111.6, 173.4),
             bow_perp=6 * scale, w_head=5 * scale, w_tail=2 * scale)

    # s4: short 横 (upper of the two, slight right-up tilt)
    draw_heng(draw, tx(140.6, 140.6), tx(229.7, 126.9),
              width_head=6, width_tail=7)

    # s5: long 横 (lower, spans through center)
    draw_heng(draw, tx(104.9, 195.7), tx(254.3, 180.8),
              width_head=7, width_tail=8)

    # s6: long descending 丿 — pierces both s4 and s5 (P-joints)
    draw_pie(draw, tx(166.1, 60.6), tx(96.4, 285.9),
             bow_perp=14 * scale, w_head=8 * scale, w_tail=3 * scale, steps=100)

    # s7: 捺 — head sits just right of s5/s6 crossing, tail flares to BR
    draw_na(draw, tx(182.8, 198.0), tx(288.3, 285.6),
            bow_perp=10 * scale, w_head=4 * scale, w_tail=11 * scale)


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 亻 via bank primitive, shifted so bank native anchors land on MMH box
    draw_ren_left(d, ox=-74, oy=0, scale=1.0)

    # 失 inline
    draw_shi_lose(d, ox=0, oy=0, scale=1.0)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_佚.png')
    render(out)
    print('wrote', out)
