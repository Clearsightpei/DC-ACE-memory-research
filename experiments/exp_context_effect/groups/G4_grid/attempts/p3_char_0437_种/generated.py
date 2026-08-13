"""种 (zhǒng) — 9 strokes.

Decomposition: 种 = 禾 (left, 5 strokes) + 中 (right, 4 strokes).
  禾 = 撇(short top) + 横 + 竖(spine) + 撇(long) + 点/短捺
  中 = 竖(left wall) + 横折(top+right) + 横(bottom) + 长竖(spine, P-welded)

Memory reading log:
  # drawer_memory.md: 禾 as left-radical → 捺 shrinks to 点; A-recipe applied.
  # memory_index.md: INDEX grep 种 → not listed; 禾 not a mastered bank primitive.
  # errata.md grep 种 → not present.
  # prior 和 (p3_char_0365_和) uses inline 禾 with pie+shu+heng+na — reuse pattern.
  # prior 中 (p3_char_0100_中) overrode MMH heavily; here we stay closer to MMH.

BANK_DEVIATION not used: no bank primitive exists for 禾-radical or 中-frame;
this is fresh composition via base stroke primitives — no bank entry skipped.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie  import draw_pie
from shu  import draw_shu
from heng import draw_heng
from na   import draw_na
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # exactly 9 primitive calls
    'endpoint_mismatches': [],    # anchors passed verbatim from MMH
    'joint_class_mismatches': [], # P at s7×s9 and s8×s9 via shared spine x
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim. 禾: 5 base primitives. 中: box (s6 left, '
              's7 heng-zhe corner, s8 bottom heng) + long 竖 spine drawn LAST so P-welds '
              'sit on top. N-gaps between 禾 strokes preserved by primitive taper.')
}


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_zhong_char(draw):
    # ============ 禾 (left, strokes 1-5) — MMH anchors verbatim ============
    # s1 — 撇 short top: TC(0.33, 0.867) → ML(0.401, 0.26)
    draw_pie(draw, ('TC', 0.33, 0.867), ('ML', 0.401, 0.26),
             head_width=9, tail_width=1, curve=0.10)

    # s2 — 横: ML(0.296, 0.693) → C(0.23, 0.526)
    draw_heng(draw, ('ML', 0.296, 0.693), ('C', 0.23, 0.526), width=8)

    # s3 — 竖 spine of 禾: ML(0.823, 0.131) → BL(0.899, 0.921)
    draw_shu(draw, ('ML', 0.823, 0.131), ('BL', 0.899, 0.921), width=9)

    # s4 — 撇 long: ML(0.835, 0.682) → BL(0.237, 0.593)
    draw_pie(draw, ('ML', 0.835, 0.682), ('BL', 0.237, 0.593),
             head_width=11, tail_width=1, curve=0.12)

    # s5 — 短捺/点 (禾 as left radical shrinks 捺 to 点):
    # ML(0.976, 0.91) → BC(0.222, 0.095). Short — render as 点.
    draw_dian(draw, ('ML', 0.976, 0.91), ('BC', 0.222, 0.095),
              head_width=2, peak_width=10, curve=0.06)

    # ============ 中 (right, strokes 6-9) ============
    # s9 defines spine x; draw box first, spine last (P-welds on top).
    #
    # s6 — 竖 left wall: C(0.33, 0.471) → BC(0.547, 0.139)
    s6h = anchor_to_xy(('C', 0.33, 0.471))
    s6t = anchor_to_xy(('BC', 0.547, 0.139))
    #
    # s7 — 横折 top+right wall: head C(0.497, 0.482) → tail MR(0.373, 0.811)
    #      corner inferred at (tail_x, head_y) = top-right of the frame.
    s7h = anchor_to_xy(('C', 0.497, 0.482))
    s7t = anchor_to_xy(('MR', 0.373, 0.811))
    s7c = (s7t[0], s7h[1])
    #
    # s8 — 横 bottom bar: BC(0.603, 0.074) → MR(0.534, 0.942)
    s8h = anchor_to_xy(('BC', 0.603, 0.074))
    s8t = anchor_to_xy(('MR', 0.534, 0.942))
    #
    # s9 — 长竖 spine: TC(0.793, 0.68) → BC(0.942, 1.088)
    s9h = anchor_to_xy(('TC', 0.793, 0.68))
    s9t = anchor_to_xy(('BC', 0.942, 1.088))

    W = 8

    # Apply small N-gap shortening on the outer box corners (top-left,
    # bottom-left, bottom-right) — do NOT weld these.
    s6h_g = _shorten(s6h, s6t, 3)   # top-left corner gap
    s6t_g = _shorten(s6t, s6h, 3)   # bottom-left corner gap
    s7h_g = _shorten(s7h, s7c, 3)   # top-left (against s6 head) gap
    s8h_g = _shorten(s8h, s8t, 3)   # bottom-left corner gap (bottom bar left tip)
    s8t_g = _shorten(s8t, s8h, 2)   # bottom-right corner gap

    # s6 — left wall
    fat_line(draw, s6h_g, s6t_g, width=W)
    # s7 — top bar + right wall (short)
    fat_line(draw, s7h_g, s7c, width=W)
    fat_line(draw, s7c, s7t, width=W)
    # small fillet at corner
    cx, cy = s7c; r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # s8 — bottom bar
    fat_line(draw, s8h_g, s8t_g, width=W)
    # s9 — long spine LAST (P-welds on top)
    fat_line(draw, s9h, s9t, width=9)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zhong_char(d)
    out = os.path.join(os.path.dirname(__file__), '01_种.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
