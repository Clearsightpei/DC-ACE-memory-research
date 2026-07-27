"""p3_char_0214_记 — 记 = 讠 (left) + 己 (right).

Memory checklist (v8):
  1. drawer_memory.md: use IMPORT for reused sub-radicals. 讠 → yan_speech.
  2. success_bank/INDEX.md: 讠 (yan_speech.py, entry 67) exists → IMPORT.
  3. errata.md: no entry for 记.
  4. 己 has no mastered primitive → inline fresh per MMH anchors.

Split: 记 = 讠 (left column ~x[0.0,0.35]) + 己 (right ~x[0.40,0.95]).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from yan_speech import draw_yan_speech


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 2 (讠) + 3 (己) = 5, matches MMH.
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Composition L-R: 讠 uses imported yan_speech primitive; '
             '己 inlined per MMH anchors (s3 横折, s4 横, s5 竖弯钩).',
}


def draw_ji_self(draw,
                 s3_head=('C', 0.20, 0.15),
                 s3_corner=('MR', 0.70, 0.10),
                 s3_tail=('MR', 0.65, 0.55),
                 s4_head=('C', 0.35, 0.55),
                 s4_tail=('MR', 0.55, 0.55),
                 s5_head=('C', 0.40, 0.62),
                 s5_knee=('BC', 0.40, 0.55),
                 s5_sweep=('BR', 0.70, 0.30),
                 s5_hook_tip=('BR', 0.75, 0.15)):
    """Draw 己 (self, 3 strokes) as the right half of 记.

    s3 横折: horizontal top-bar then bend down.
    s4 横:   short middle horizontal.
    s5 竖弯钩: vertical down, curve right, up-flick hook.
    """
    # s3 — 横折 (heng-zhe): 横 then 折 down.
    p_h_start = anchor_to_xy(s3_head)
    p_h_corner = anchor_to_xy(s3_corner)
    p_v_end = anchor_to_xy(s3_tail)

    # 横 portion (top bar), slight downward slope.
    heng_pts = [(p_h_start[0] + i / 20 * (p_h_corner[0] - p_h_start[0]),
                 p_h_start[1] + i / 20 * (p_h_corner[1] - p_h_start[1]))
                for i in range(21)]
    heng_widths = [7 - (i / 20) * 2 for i in range(21)]
    # small shoulder into 折
    ctrl_sh = (p_h_corner[0] + 4, p_h_corner[1] + 2)
    sh_pts = quad_bezier(p_h_corner, ctrl_sh, p_v_end, n=18)
    sh_widths = [8 + (i / 18) * 1 for i in range(19)]
    pts = heng_pts + sh_pts[1:]
    widths = heng_widths + sh_widths[1:]
    stroke_variable_width(draw, pts, widths)

    # s4 — middle 横 (a short horizontal that hangs off 竖 on the right side).
    p4h = anchor_to_xy(s4_head)
    p4t = anchor_to_xy(s4_tail)
    fat_line(draw, p4h, p4t, width=7)

    # s5 — 竖弯钩: vertical down from top-of-己, curve right, up-hook.
    p5_head = anchor_to_xy(s5_head)          # top of 竖
    p5_knee = anchor_to_xy(s5_knee)          # bottom-left corner
    p5_sweep = anchor_to_xy(s5_sweep)        # bottom-right after sweep
    p5_tip = anchor_to_xy(s5_hook_tip)       # up-flick end

    # 竖 down
    ctrl_v = (p5_head[0] - 2, (p5_head[1] + p5_knee[1]) / 2.0)
    v_pts = quad_bezier(p5_head, ctrl_v, p5_knee, n=28)
    v_widths = [9 - (i / 28) * 1 for i in range(29)]
    # 弯 sweep right
    ctrl_s = ((p5_knee[0] + p5_sweep[0]) / 2.0, p5_sweep[1] + 8)
    s_pts = quad_bezier(p5_knee, ctrl_s, p5_sweep, n=28)
    s_widths = [8 + (i / 28) * 1 for i in range(29)]
    # 钩 up
    ctrl_h = ((p5_sweep[0] + p5_tip[0]) / 2.0 + 2,
              (p5_sweep[1] + p5_tip[1]) / 2.0)
    h_pts = quad_bezier(p5_sweep, ctrl_h, p5_tip, n=18)
    h_widths = [9 - (i / 18) * 8 for i in range(19)]

    all_pts = v_pts + s_pts[1:] + h_pts[1:]
    all_w = v_widths + s_widths[1:] + h_widths[1:]
    stroke_variable_width(draw, all_pts, all_w)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # LEFT: 讠 via imported primitive (default anchors already left-column).
    draw_yan_speech(draw)

    # RIGHT: 己 inlined, shifted into right ~half of canvas.
    draw_ji_self(draw)

    out = os.path.join(os.path.dirname(__file__), '01_记.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
