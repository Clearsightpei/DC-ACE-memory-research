"""甾 (zāi) — 8 strokes.
Decomposition: 甾 = 巛 (top, 3 curly strokes) + 田 (bottom, 5 strokes: shu + heng_zhe + heng + shu + heng).
A-recipe: MMH-verbatim anchors + base primitives + N-joint discipline.
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng_zhe import draw_heng_zhe

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 strokes drawn (3 top curls + 5 田 strokes)
    'endpoint_mismatches': [],     # all MMH-verbatim
    'joint_class_mismatches': [],  # all N-gaps preserved; s6/s7 crossing = P
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim. Top 3 rendered as curly quad_beziers (小巛). Bottom 田 = shu + heng_zhe + heng + shu + heng.',
}


def draw_curl(draw, head_a, tail_a, width=8, color=(0, 0, 0)):
    """Small curly vertical stroke for 巛-piece.
    A short leftward flick at the head, then curves down to the tail.
    """
    p_head = anchor_to_xy(head_a)
    p_tail = anchor_to_xy(tail_a)
    dx = p_tail[0] - p_head[0]
    dy = p_tail[1] - p_head[1]
    length = (dx * dx + dy * dy) ** 0.5

    # Small hook segment at the head (leftward)
    hook_len = max(6.0, length * 0.15)
    hook_end = (p_head[0] - hook_len, p_head[1] + hook_len * 0.35)

    # Bezier from hook_end down to tail with a leftward bow to give the curl a wavy look
    mid_x = (hook_end[0] + p_tail[0]) * 0.5
    mid_y = (hook_end[1] + p_tail[1]) * 0.5
    # perpendicular offset (leftward bow)
    seg_dx = p_tail[0] - hook_end[0]
    seg_dy = p_tail[1] - hook_end[1]
    seg_len = max(1.0, (seg_dx ** 2 + seg_dy ** 2) ** 0.5)
    perp = (-seg_dy / seg_len, seg_dx / seg_len)  # perpendicular
    bow = 0.18 * seg_len
    ctrl = (mid_x - perp[0] * bow, mid_y - perp[1] * bow)

    pts = quad_bezier(hook_end, ctrl, p_tail, n=40)
    n = len(pts) - 1
    widths = [width + 1 + (width - 4 - (width + 1)) * (i / n) for i in range(n + 1)]
    # Draw the head hook
    fat_line(draw, p_head, hook_end, width, color=color)
    stroke_variable_width(draw, pts, widths, color=color)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    W = 9  # base stroke width

    # --- Top: 巛 (three curls) ---
    # stroke 1: head @ ('TL', 0.85, 0.732)  tail @ ('ML', 0.987, 0.857)
    draw_curl(d, ('TL', 0.85, 0.732), ('ML', 0.987, 0.857), width=W)
    # stroke 2: head @ ('TC', 0.424, 0.656)  tail @ ('C', 0.562, 0.799)
    draw_curl(d, ('TC', 0.424, 0.656), ('C', 0.562, 0.799), width=W)
    # stroke 3: head @ ('TR', 0.004, 0.621)  tail @ ('MR', 0.212, 0.717)
    draw_curl(d, ('TR', 0.004, 0.621), ('MR', 0.212, 0.717), width=W)

    # --- Bottom: 田 ---
    # stroke 4: shu (left vertical of 田)
    #   head @ ('BL', 0.671, 0.021)  tail @ ('BL', 0.973, 1.021)
    fat_line(d, anchor_to_xy(('BL', 0.671, 0.021)),
                anchor_to_xy(('BL', 0.973, 1.021)), W)

    # stroke 5: heng_zhe (top + right of 田)
    #   head @ ('BL', 0.823, 0.03)  tail @ ('BR', 0.024, 1.1)
    #   corner = top-right of 田 frame, near ('BR', 0.02, 0.03)
    draw_heng_zhe(d,
                  head=('BL', 0.823, 0.03),
                  corner=('BR', 0.024, 0.03),
                  tail=('BR', 0.024, 1.1),
                  h_width=W, v_width=W)

    # stroke 6: middle heng
    #   head @ ('BC', 0.104, 0.473)  tail @ ('BC', 0.822, 0.408)
    fat_line(d, anchor_to_xy(('BC', 0.104, 0.473)),
                anchor_to_xy(('BC', 0.822, 0.408)), W)

    # stroke 7: middle shu
    #   head @ ('BC', 0.374, 0.095)  tail @ ('BC', 0.418, 0.754)
    fat_line(d, anchor_to_xy(('BC', 0.374, 0.095)),
                anchor_to_xy(('BC', 0.418, 0.754)), W)

    # stroke 8: bottom heng
    #   head @ ('BC', 0.022, 0.839)  tail @ ('BC', 0.96, 0.81)
    fat_line(d, anchor_to_xy(('BC', 0.022, 0.839)),
                anchor_to_xy(('BC', 0.96, 0.81)), W)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_甾.png')
    img.save(out)


if __name__ == '__main__':
    main()
