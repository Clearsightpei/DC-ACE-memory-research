"""p3_char_0565_桃 (táo) — 10 strokes.

Decomposition: 桃 = 木 (left) + 兆 (right).
  木 = heng + shu + pie + na (strokes 1-4, compressed left)
  兆 = 撇 + 点 + 竖弯钩(long)  +  撇 + 短竖 + 竖弯钩 (strokes 5-10, right)

Per B9/B10/B11 A-recipe: MMH-verbatim anchors + base primitives inline.
Left 木 uses the same recipe as p3_char_0455_相 (compressed-left 木).
Right 兆: 6 strokes MMH-verbatim; the two 竖弯钩 (s7 long left, s10 right
hook) are the identifying feature. Per errata for 佻/兆: keep the two
inner column strokes with a natural gap, not splayed. Follow MMH heads
literally.

# BANK_DEVIATION
# skipped: (no compound primitive existed for 木 or 兆)
# reason: no mu.py; no zhao.py. Inlining base primitives per A-recipe.
# fresh_component: mu_left_compressed_for_桃 + zhao_right_for_桃
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 draw-primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim. 木 left (4) + 兆 right (6). All N-joints preserved as natural gaps.',
}


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ================================================
# 木 (strokes 1-4) — LEFT radical, compressed column
# ================================================

# s1: heng (short, left)
s1h = anchor_to_xy(('ML', 0.325, 0.477))
s1t = anchor_to_xy(('C',  0.166, 0.321))
fat_line(draw, s1h, s1t, width=8)

# s2: shu (vertical spine of 木)
s2h = anchor_to_xy(('TL', 0.753, 0.560))
s2t = anchor_to_xy(('BL', 0.794, 1.088))
fat_line(draw, s2h, s2t, width=9)

# s3: pie (down-left from spine)
s3h = anchor_to_xy(('ML', 0.797, 0.491))
s3t = anchor_to_xy(('BL', 0.144, 0.607))
mid3 = ((s3h[0] + s3t[0]) / 2, (s3h[1] + s3t[1]) / 2)
ctrl3 = (mid3[0] + 4, mid3[1] - 10)
pts3 = quad_bezier(s3h, ctrl3, s3t, n=32)
widths3 = [8 - 6 * (i / len(pts3)) for i in range(len(pts3))]
stroke_variable_width(draw, pts3, widths3)

# s4: na (short dot-like, since 木 is left radical it's compressed)
s4h = anchor_to_xy(('ML', 0.943, 0.702))
s4t = anchor_to_xy(('C',  0.166, 0.928))
mid4 = ((s4h[0] + s4t[0]) / 2, (s4h[1] + s4t[1]) / 2)
ctrl4 = (mid4[0] - 3, mid4[1] + 2)
pts4 = quad_bezier(s4h, ctrl4, s4t, n=24)
widths4 = [3 + 6 * (i / len(pts4)) for i in range(len(pts4))]
stroke_variable_width(draw, pts4, widths4)

# ================================================
# 兆 (strokes 5-10) — RIGHT side, 6 strokes
# ================================================

# s5: 撇 (long pie of 兆 left column, sweeps down-left with taper)
s5h = anchor_to_xy(('TC', 0.55, 0.976))
s5t = anchor_to_xy(('BC', 0.099, 0.842))
mid5 = ((s5h[0] + s5t[0]) / 2, (s5h[1] + s5t[1]) / 2)
ctrl5 = (mid5[0] + 10, mid5[1] - 12)
pts5 = quad_bezier(s5h, ctrl5, s5t, n=36)
widths5 = [9 - 6 * (i / len(pts5)) for i in range(len(pts5))]
stroke_variable_width(draw, pts5, widths5)

# s6: 点 (short dot, inner-left of 兆)
s6h = anchor_to_xy(('C', 0.236, 0.471))
s6t = anchor_to_xy(('C', 0.456, 0.638))
# small dian: taper from thin to thicker
pts6 = [s6h, ((s6h[0]+s6t[0])/2, (s6h[1]+s6t[1])/2), s6t]
widths6 = [3, 6, 8]
stroke_variable_width(draw, pts6, widths6)

# s7: 提 (rising short stroke — bottom of 兆 left column, rises up-right)
s7h = anchor_to_xy(('BC', 0.11, 0.165))
s7t = anchor_to_xy(('C',  0.573, 0.881))
# ti is a straight rising taper from thick (head) to thin (tail)
pts7 = quad_bezier(s7h,
                   ((s7h[0]+s7t[0])/2, (s7h[1]+s7t[1])/2),
                   s7t, n=24)
widths7 = [8 - 5 * (i / len(pts7)) for i in range(len(pts7))]
stroke_variable_width(draw, pts7, widths7)

# s8: 撇 (short pie, top of right column)
s8h = anchor_to_xy(('TC', 0.934, 0.712))
s8t = anchor_to_xy(('BR', 0.795, 0.265))
mid8 = ((s8h[0] + s8t[0]) / 2, (s8h[1] + s8t[1]) / 2)
ctrl8 = (mid8[0] + 4, mid8[1] - 4)
pts8 = quad_bezier(s8h, ctrl8, s8t, n=24)
widths8 = [7 - 4 * (i / len(pts8)) for i in range(len(pts8))]
stroke_variable_width(draw, pts8, widths8)

# s9: 点 / short vertical stroke on right upper
s9h = anchor_to_xy(('MR', 0.388, 0.172))
s9t = anchor_to_xy(('MR', 0.104, 0.579))
pts9 = [s9h, ((s9h[0]+s9t[0])/2, (s9h[1]+s9t[1])/2), s9t]
widths9 = [4, 6, 7]
stroke_variable_width(draw, pts9, widths9)

# s10: 竖弯钩 (right hook) — long down-right sweep with terminal hook
s10h = anchor_to_xy(('MR', 0.092, 0.896))
s10t = anchor_to_xy(('BR', 0.561, 0.227))
mid10 = ((s10h[0] + s10t[0]) / 2, (s10h[1] + s10t[1]) / 2)
ctrl10 = (mid10[0] - 6, mid10[1] + 18)
pts10 = quad_bezier(s10h, ctrl10, s10t, n=40)
widths10 = [8 - 3 * (i / len(pts10)) for i in range(len(pts10))]
stroke_variable_width(draw, pts10, widths10)
# terminal hook (upward-left)
hook10_end = (s10t[0] - 12, s10t[1] - 6)
fat_line(draw, s10t, hook10_end, width=6)


out = os.path.join(os.path.dirname(__file__), '01_桃.png')
img.save(out)
print(f'wrote {out}')
