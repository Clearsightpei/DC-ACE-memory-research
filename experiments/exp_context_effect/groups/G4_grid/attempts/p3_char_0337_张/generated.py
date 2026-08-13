# BANK_DEVIATION
# skipped: chronic/gong_bow.py
# reason: chronic gong_bow uses hardcoded full-canvas anchors (弓 fills 300x300).
#         In 张, 弓 is compressed to the LEFT column (x∈[50,115]) — calling
#         the chronic default would spill across the whole canvas and clash
#         with 长. MMH places 弓 stroke endpoints entirely in TL/ML/BL cells,
#         so inline base primitives with MMH-verbatim anchors per B9 A-recipe.
# fresh_component: gong_bow_left_col_for_zhang
"""张 (zhāng) — 7 strokes.
Decomposition: 张 = 弓 (left, s1-s3) + 长 (right, s4-s7).
  弓: s1 横折 top / s2 短横 mid / s3 竖折折钩 bottom bowl+hook.
  长: s4 短撇 top-right / s5 长横 crossing / s6 slanted 竖 / s7 长捺 sweep.

Anchors are MMH-verbatim per dispatcher-injected block.
Chronic gong_bow.py skipped: full-canvas defaults incompatible with
left-column compression; see BANK_DEVIATION note above.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 7 stroke primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('7 strokes MMH-verbatim. s1 heng_zhe with interpolated '
              'corner. s3 竖折折钩 inlined as descent+bowl+hook via '
              'fat_line segments (one logical stroke). s5-s6 welded (P). '
              'All other joints N gaps preserved.'),
}


def _draw_bowl_hook(draw, head, corner1, corner2, hook_pt, tip, width=9):
    """Custom 竖折折钩 for 弓's bottom tier — one logical stroke.
    Direct primitive draws: descent, bottom sweep, up-tick, hook flick.
    """
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)
    fat_line(draw, p_head, p_c1, width)       # 竖 descent
    fat_line(draw, p_c1, p_c2, width)         # 横 bottom
    fat_line(draw, p_c2, p_hook, width)       # short up-tick
    # Hook flick: tapered curve from hook_pt toward tip.
    ctrl = ((p_hook[0] + p_tip[0]) * 0.5,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.3)
    pts = quad_bezier(p_hook, ctrl, p_tip, n=24)
    m = len(pts) - 1
    widths = [width + (2 - width) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_zhang(draw):
    # ----- 弓 (left, strokes 1-3) — left column x∈[50,115] -----
    # s1: 横折 top tier. MMH head=(TL,0.62,0.97), tail=(ML,0.98,0.34).
    # Interpolated corner at (TL,0.98,0.97) to give the L bend.
    draw_heng_zhe(draw,
                  ('TL', 0.62, 0.97),
                  ('TL', 0.98, 0.97),
                  ('ML', 0.98, 0.34),
                  h_width=9, v_width=9, shoulder=11)

    # s2: 短横 middle tier. MMH head=(ML,0.72,0.53), tail=(C,0.15,0.42).
    draw_heng(draw, ('ML', 0.72, 0.53), ('C', 0.15, 0.42), width=9)

    # s3: 竖折折钩 bottom tier bowl + hook.
    # MMH head=(ML,0.54,0.40), tail=(BL,0.50,0.70). Interpolated corners
    # to form a clean 弓 belly ending at MMH tail (bottom-left flick).
    _draw_bowl_hook(draw,
                    ('ML', 0.54, 0.40),    # head — start descent
                    ('BL', 0.54, 0.45),    # corner1 — bottom of descent (y=245)
                    ('BL', 1.00, 0.45),    # corner2 — sweep right end (x=100, y=245)
                    ('BL', 0.90, 0.65),    # hook_pt — bowl bottom (x=90, y=265)
                    ('BL', 0.50, 0.70),    # tip — MMH tail flick (x=50, y=270)
                    width=9)

    # ----- 长 (right, strokes 4-7) -----
    # s4: 短撇 top-right. MMH head=(TR,0.156,0.946), tail=(C,0.772,0.488).
    draw_pie(draw,
             ('TR', 0.156, 0.946),
             ('C',  0.772, 0.488),
             head_width=9, tail_width=2, curve=0.06, segments=32)

    # s5: 长横 crossing. MMH head=(C,0.271,0.816), tail=(MR,0.581,0.69).
    draw_heng(draw, ('C', 0.271, 0.816), ('MR', 0.581, 0.69), width=9)

    # s6: slanted 竖 crossing s5 (P weld). MMH head=(TC,0.494,0.776),
    # tail=(BR,0.016,0.514). Straight fat_line — MMH gives no midpoints.
    fat_line(draw,
             anchor_to_xy(('TC', 0.494, 0.776)),
             anchor_to_xy(('BR', 0.016, 0.514)),
             width=10)

    # s7: 长捺 down-right sweep. MMH head=(C,0.717,0.846), tail=(BR,0.783,0.578).
    draw_na(draw,
            ('C',  0.717, 0.846),
            ('BR', 0.783, 0.578),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.78, curve=0.08, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_zhang(d)
    out = os.path.join(os.path.dirname(__file__), '01_张.png')
    img.save(out)
    print('Saved:', out)


if __name__ == '__main__':
    main()
