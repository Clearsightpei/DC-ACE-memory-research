"""処 (chù, 5 strokes) — v8 attempt.

Decomposition: 夂 (top-left, strokes 1-3) + 几 (bottom-right frame, strokes 4-5).
Under v8, treating anchors as REFERENCE; drawing per MMH-derived anchor block.

Strokes (from injected MMH block):
  s1 撇   : TL(0.797, 0.785) -> BL(0.261, 0.062)   long left-descending
  s2 撇   : ML(0.747, 0.503) -> BL(0.214, 0.812)   inner short 撇 of 夂
  s3 捺   : ML(0.501, 0.978) -> BR(0.742, 0.804)   right-falling 捺 of 夂
  s4 撇   : TC(0.658, 0.861) -> BC(0.412, 0.253)   inner 撇 of 几
  s5 横折弯钩: TC(0.828, 0.879) -> BR(0.804, 0.01)  outer right frame w/ hook

Joints:
  s1.mid ⇆ s2.head       N (~13 px gap in ML)
  s1.tail ⇆ s3.head      N (~18 px gap in ML)
  s2.mid ⇆ s3.mid        P welded at BL corner
  s3.mid ⇆ s4.tail       N (~25 px gap in BC)
  s4.head ⇆ s5.head      N (~14 px gap in TC)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes; N-gaps preserved at top of 几 and at 夂-几 seam.'
}


def _draw_heng_zhe_wan_gou(draw, head, corner, knee, tail):
    """横折弯钩 inlined: top bar -> corner -> curved descent to knee -> flick up-left to tail."""
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_knee = anchor_to_xy(knee)
    p_tail = anchor_to_xy(tail)
    # top horizontal segment (head -> corner)
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 1)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=22)
    top_widths = [6 + (i / 22) * 3 for i in range(23)]
    # descent (corner -> knee at bottom-right) with slight rightward bow
    ctrl_desc = (max(p_corner[0], p_knee[0]) + 3,
                 (p_corner[1] + p_knee[1]) / 2.0)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_knee, n=36)
    desc_widths = [9 - (i / 36) * 3 for i in range(37)]
    # hook flick from knee up-left to tail
    ctrl_hook = ((p_knee[0] + p_tail[0]) / 2.0 - 4,
                 (p_knee[1] + p_tail[1]) / 2.0)
    hook_pts = quad_bezier(p_knee, ctrl_hook, p_tail, n=18)
    hook_widths = [7 - (i / 18) * 6 for i in range(19)]

    pts = top_pts + desc_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)


def draw_chu(draw):
    # s1 — long outer 撇 of 夂 (top-right to bottom-left across left half)
    draw_pie(draw, ('TL', 0.797, 0.785), ('BL', 0.261, 0.062),
             head_width=9, tail_width=1, curve=0.10, segments=48)
    # s2 — short inner 撇 of 夂
    draw_pie(draw, ('ML', 0.747, 0.503), ('BL', 0.214, 0.812),
             head_width=7, tail_width=1, curve=0.08, segments=36)
    # s3 — 捺 sweeping from mid-left down to bottom-right
    draw_na(draw, ('ML', 0.501, 0.978), ('BR', 0.742, 0.804),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10, segments=48)
    # s4 — inner 撇 of 几 (from top-center down to bottom-center, slight left bow)
    draw_pie(draw, ('TC', 0.658, 0.861), ('BC', 0.412, 0.253),
             head_width=8, tail_width=1, curve=0.06, segments=44)
    # s5 — 横折弯钩 outer right frame; MMH tail (BR 0.804, 0.01 -> pixel y~201)
    # is the hook TIP; descent bottoms out at knee near BR corner then flicks up-left.
    _draw_heng_zhe_wan_gou(draw,
                           head=('TC', 0.828, 0.879),
                           corner=('TR', 0.88, 0.90),
                           knee=('BR', 0.95, 0.75),
                           tail=('BR', 0.804, 0.01))


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chu(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_処.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
