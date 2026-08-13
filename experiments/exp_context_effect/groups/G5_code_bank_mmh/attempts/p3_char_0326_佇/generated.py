"""p3_char_0326_佇 — G5 attempt.

佇 = 亻 (2 strokes) + 宁 (5 strokes) = 7 strokes.
Recipe: P-A-006 — MMH anchors verbatim + stroke-primitive layer.
亻 half taken from bank stroke primitives (pie + shu),
宁 half inlined via bank primitives at MMH-injected anchors:
  s3 top dot, s4 left drop, s5 top heng, s6 bottom heng of 丁, s7 shu-gou 亅.

Note: P-COMP-011 boundary — 佇's right half (宁) has a hook-compound
(shu-gou), which is outside the pure straight-stroke recipe. Using
per-stroke bank primitives (not a whole-radical primitive since no 宁
exists in bank) matches P-A-006 more than P-A-007.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from heng import draw_heng
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 stroke primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints are N (natural gap), preserved
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; 亻 pie+shu, 宀 dot+drop+heng, 丁 heng+shu-gou.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- 亻 (person radical, left position) ---
    # s1: 亻 pie (TL→ML sweep)
    draw_pie(draw, head=(93, 61), tail=(16, 195),
             bow_perp=15, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu (vertical descender)
    draw_shu(draw, head=(74, 141), tail=(76, 293), width=7)

    # --- 宀 (roof radical) ---
    # s3: top dot (small down-right tick just left of center-top)
    draw_dian(draw, head=(170, 52), tail=(201, 81),
              w_head=3, w_tail=7, bow=2, steps=32)
    # s4: left drop of roof (short down-slightly-left)
    draw_dian(draw, head=(125, 109), tail=(116, 161),
              w_head=3, w_tail=7, bow=2, steps=32)
    # s5: roof top heng (short horizontal C→MR)
    draw_heng(draw, head=(135, 125), tail=(238, 142),
              width_head=8, width_tail=9)

    # --- 丁 (bottom component) ---
    # s6: 一 of 丁 (horizontal spanning right half)
    draw_heng(draw, head=(125, 186), tail=(259, 176),
              width_head=9, width_tail=11)
    # s7: 亅 of 丁 (vertical then leftward hook)
    draw_shu_gou(draw, head=(185, 187), tail=(156, 280),
                 width=7, hook_start_offset=28)

    out = Path(__file__).with_name('01_佇.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    render()
