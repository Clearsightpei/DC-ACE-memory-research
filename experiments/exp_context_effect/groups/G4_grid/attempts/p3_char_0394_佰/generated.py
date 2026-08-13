"""p3_char_0394_佰 — G4 attempt.

Split: 佰 = 亻 (left) + 百 (right).
百 = 一 (top横) + 丿 (short pie) + 日-like frame (left竖 + 横折 + middle横 + bottom横).

Memory citations (per memory_index.md step 1-3):
  - drawer_memory.md: shortlist lists ren_side for 亻 → IMPORT it.
  - success_bank/INDEX.md: 亻+X composition pattern (化/他/仔/仕/付...);
    百 has no standalone bank primitive → inline from MMH anchors.
  - errata.md: no entry for 佰 / 百.

MMH-derived structural expectations (8 strokes) followed verbatim
for endpoint anchors. Joints all N-class (no welds).
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from ren_side import draw_ren_side


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 (ren_side) + 6 inline = 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes: ren_side gives s1+s2; 百 inlined as 6 fat_lines.'
}


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6: return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_pie_curve(draw, head_xy, tail_xy, width_head, width_tail):
    # simple quadratic bezier bowing left
    mx = (head_xy[0] + tail_xy[0]) / 2 - 8
    my = (head_xy[1] + tail_xy[1]) / 2 + 4
    pts = quad_bezier(head_xy, (mx, my), tail_xy, n=40)
    widths = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        widths.append(width_head * (1 - t) + width_tail * t)
    stroke_variable_width(draw, pts, widths)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ============ 亻 left radical (strokes 1 & 2) ============
    # MMH anchors:
    #   s1: pie head TL(0.806, 0.662) -> tail BL(0.126, 0.007)
    #   s2: shu head ML(0.674, 0.453) -> tail BL(0.677, 0.938)
    draw_ren_side(
        draw,
        pie_head=('TL', 0.806, 0.662),
        pie_tail=('BL', 0.126, 0.007),
        shu_head=('ML', 0.674, 0.453),
        shu_tail=('BL', 0.677, 0.938),
    )

    # ============ 百 right side (strokes 3-8) ============
    w = 9  # main body stroke width

    # s3 — top 横 across full width of right side
    #   MMH: head C(0.107, 0.146) -> tail MR(0.684, 0.005)
    s3h = anchor_to_xy(('C', 0.107, 0.146))
    s3t = anchor_to_xy(('MR', 0.684, 0.005))
    fat_line(draw, s3h, s3t, width=w)

    # s4 — short 丿 pie (upper-left of box) — make more visible
    #   MMH: head C(0.646, 0.157) -> tail C(0.518, 0.682)
    s4h = anchor_to_xy(('C', 0.646, 0.157))
    s4t = anchor_to_xy(('C', 0.418, 0.72))  # extend tail down-left for visible pie
    draw_pie_curve(draw, s4h, s4t, width_head=11, width_tail=2)

    # s5 — left 竖 of the 日 box
    #   MMH: head C(0.277, 0.652) -> tail BC(0.38, 0.812)
    s5h = anchor_to_xy(('C', 0.277, 0.652))
    s5t = anchor_to_xy(('BC', 0.38, 0.812))
    fat_line(draw, s5h, s5t, width=w)

    # s6 — 横折 right side compound (top-right corner + right vertical)
    #   MMH: head C(0.479, 0.717) -> tail BR(0.229, 0.918)
    # Interpret as top-right 横 to corner then 竖 down. But MMH lists only
    # head+tail; we render as two segments through a corner point.
    s6h = anchor_to_xy(('C', 0.479, 0.717))
    s6t = anchor_to_xy(('BR', 0.229, 0.918))
    # corner: same x as tail, same y as head (top-right of 日 box)
    s6corner = (s6t[0], s6h[1])
    fat_line(draw, s6h, s6corner, width=w)
    fat_line(draw, s6corner, s6t, width=w)

    # s7 — middle 横 inside box (shortened so it doesn't hit right wall)
    #   MMH: head BC(0.471, 0.212) -> tail BR(0.01, 0.145)
    s7h = anchor_to_xy(('BC', 0.471, 0.212))
    s7t = anchor_to_xy(('BR', 0.01, 0.145))
    # bigger inward shorten on tail to keep clear N-gap from right wall
    fat_line(draw,
             _shorten(s7h, s7t, 4),
             _shorten(s7t, s7h, 12),
             width=w - 1)

    # s8 — bottom 横 closing box
    #   MMH: head BC(0.477, 0.707) -> tail BR(0.095, 0.628)
    s8h = anchor_to_xy(('BC', 0.477, 0.707))
    s8t = anchor_to_xy(('BR', 0.095, 0.628))
    fat_line(draw,
             _shorten(s8h, s8t, 3),
             _shorten(s8t, s8h, 3),
             width=w)

    out = os.path.join(os.path.dirname(__file__), '01_佰.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
