"""受 (shòu) — 8 strokes: 爫 (4) + 冖-like (2) + 又 (2).

Bank primitives used: pie, na, heng_pie, heng_gou, _anchor helpers.
Anchors follow the MMH-derived structural expectations from brief.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line
from pie import draw_pie
from na import draw_na
from heng_pie import draw_heng_pie
from heng_gou import draw_heng_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('8 strokes: s1 top pie of 爫; s2/s3/s4 three dot-like '
              'strokes of 爫; s5 short pie left-side of cover; '
              's6 horizontal cover; s7 横撇 of 又 (with corner for '
              'joint mid to land in BC); s8 捺 of 又 crossing s7 (P).')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 爫 (top, 4 strokes) ----
    # s1: top pie sweeping down-left across the top
    draw_pie(d, ('TC', 0.907, 0.668), ('TL', 0.999, 0.943),
             head_width=9, tail_width=2, curve=0.04)

    # s2: leftmost small dian (down-right)
    draw_pie(d, ('ML', 0.911, 0.099), ('C', 0.128, 0.389),
             head_width=8, tail_width=2, curve=-0.10)

    # s3: middle small dian (down-right)
    draw_pie(d, ('C', 0.362, 0.002), ('C', 0.535, 0.219),
             head_width=3, tail_width=9, curve=-0.05)

    # s4: rightmost dian pie (down-left)
    draw_pie(d, ('TR', 0.045, 0.867), ('C', 0.743, 0.307),
             head_width=8, tail_width=2, curve=0.05)

    # ---- 冖-cover (2 strokes: 短撇 + 横) ----
    # s5: short 撇 at left side of cover
    draw_pie(d, ('ML', 0.598, 0.529), ('BL', 0.51, 0.101),
             head_width=9, tail_width=2, curve=0.04)

    # s6: horizontal cover body, thick and gently down-slanting
    p_head = anchor_to_xy(('ML', 0.724, 0.638))
    p_tail = anchor_to_xy(('MR', 0.162, 0.825))
    heng_pts = sample_line(p_head, p_tail, n=40)
    heng_ws = [7 + (10 - 7) * (i / 40) for i in range(41)]
    stroke_variable_width(d, heng_pts, heng_ws)
    # Small down-left tick at right end (subtle hook, calligraphic)
    tip_end = (p_tail[0] - 4, p_tail[1] + 10)
    hook_pts = quad_bezier(p_tail, ((p_tail[0]+tip_end[0])/2 + 2,
                                    (p_tail[1]+tip_end[1])/2), tip_end, n=10)
    hook_ws = [10 + (2 - 10) * (i / 10) for i in range(11)]
    stroke_variable_width(d, hook_pts, hook_ws)

    # ---- 又 (bottom, 2 strokes) ----
    # s7: 横撇 — corner pulled in to sit right above BC joint point.
    # Head slightly higher/left so the horizontal reads clean; corner at
    # upper-right of C cell; tip at BL bottom-left as MMH tail specifies.
    draw_heng_pie(d,
                  head=('ML', 0.95, 0.85),
                  corner=('C', 0.75, 0.70),
                  tip=('BL', 0.674, 0.959),
                  head_w=6, corner_w=12, tip_w=2)

    # s8: 捺 sweeping down-right, crosses s7 (P joint near BC).
    draw_na(d, from_anchor=('BL', 0.967, 0.191),
               to_anchor=('BR', 0.733, 1.009),
               head_width=3, peak_width=14, tail_width=1,
               peak_t=0.78, curve=0.09, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_受.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
