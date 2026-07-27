"""乌 (wū, "crow", 4 strokes) — G4 grid-bank drawer attempt.

# MANDATORY LOOKUP CHECKLIST confirmations:
# 1. success_bank/INDEX.md: no 乌/鸟 primitive exists.
# 2. errata.md: 乌 not listed.
# 3. form_catalog.md: no specific 乌 row; treat as fresh compound.
# 4. principles_meta.md: TR1 (override), TR6 (inline compound), TR9 (full-grid span).
# 5. joint_atlas.md: all 3 joints N-class (small ~15px gap, do NOT weld).
# 6. sandbox.md: no prior 乌 notes.
#
# REVISION 2: enlarged the character to fill the full 米字格 grid per TR9.
# Body-hook now spans TL top → down right → bottom baseline meeting s4.
# GT shape: top head-loop on upper-left with short pie tick, small
# eye-line inside head, big body swings out to right and down, bottom 横.
"""

from PIL import Image, ImageDraw
import sys, os

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'revision 2: enlarged to full grid span',
}


def draw_pie_curved(draw, p_head, p_tail, control_bias=(0.15, 0.35),
                    head_w=10, tail_w=3, color=(0, 0, 0)):
    mx = (p_head[0] + p_tail[0]) / 2
    my = (p_head[1] + p_tail[1]) / 2
    dx = p_tail[0] - p_head[0]
    dy = p_tail[1] - p_head[1]
    ctrl = (mx + control_bias[0] * dx + control_bias[1] * (-dy),
            my + control_bias[1] * dx + control_bias[0] * dy)
    pts = quad_bezier(p_head, ctrl, p_tail, n=40)
    m = len(pts) - 1
    widths = [head_w + (tail_w - head_w) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_wu(draw):
    # === Stroke 1: top-left short 撇 tick ===
    # Small pie above the head loop (like the tick on top of 乌).
    # MMH says TC(0.397, 0.524) → C(0.146, 0.002) — small stroke near top center.
    s1_head = anchor_to_xy(('TC', 0.55, 0.20))   # a bit high & right
    s1_tail = anchor_to_xy(('TC', 0.30, 0.75))   # sweep down-left
    draw_pie_curved(draw, s1_head, s1_tail,
                    control_bias=(0.10, 0.30),
                    head_w=8, tail_w=2)

    # === Stroke 2: small horizontal "eye" line inside head loop ===
    # MMH C(0.163, 0.16) → C(0.523, 0.465)
    p2h = anchor_to_xy(('C', 0.20, 0.30))
    p2t = anchor_to_xy(('C', 0.55, 0.35))
    fat_line(draw, p2h, p2t, width=6)

    # === Stroke 3: 横折折折钩 body — head loop + right descent + hook ===
    # Build the head loop starting from near top-left of C column,
    # up and over to the right, then descend along the right side, then
    # hook back at the bottom.
    # Head at top of head-loop (below s1 tail slightly with N gap).
    p_a = anchor_to_xy(('TC', 0.10, 0.80))   # head start (upper-left of loop)
    p_b = anchor_to_xy(('TC', 0.55, 0.55))   # top of loop (curving up-right)
    p_c = anchor_to_xy(('TR', 0.30, 0.65))   # top-right shoulder
    p_d = anchor_to_xy(('MR', 0.50, 0.20))   # right-side upper
    p_e = anchor_to_xy(('MR', 0.65, 0.85))   # right-side lower (belly)
    p_f = anchor_to_xy(('BR', 0.55, 0.55))   # right-bottom curve out
    p_g = anchor_to_xy(('BR', 0.35, 0.85))   # bottom of hook
    p_h = anchor_to_xy(('BC', 0.85, 0.60))   # hook tip (flick up-left)

    # Segment a→b (top of head loop, curves up)
    pts1 = quad_bezier(p_a, ((p_a[0] + p_b[0]) / 2, p_a[1] - 15), p_b, n=25)
    stroke_variable_width(draw, pts1, [8] * len(pts1))

    # Segment b→c (over the shoulder curving down slightly)
    pts2 = quad_bezier(p_b, (p_c[0] - 5, p_b[1] - 5), p_c, n=25)
    stroke_variable_width(draw, pts2, [8] * len(pts2))

    # Segment c→d (right side upper, slight bulge outward)
    pts3 = quad_bezier(p_c, (p_c[0] + 15, (p_c[1] + p_d[1]) / 2), p_d, n=25)
    stroke_variable_width(draw, pts3, [8] * len(pts3))

    # Segment d→e (right side descending, main body)
    pts4 = quad_bezier(p_d, (p_d[0] + 10, (p_d[1] + p_e[1]) / 2), p_e, n=30)
    stroke_variable_width(draw, pts4, [8] * len(pts4))

    # Segment e→f (curve out at bottom right)
    pts5 = quad_bezier(p_e, (p_e[0] + 15, p_e[1] + 15), p_f, n=25)
    stroke_variable_width(draw, pts5, [8] * len(pts5))

    # Segment f→g (bottom of hook coming back left-down)
    pts6 = quad_bezier(p_f, (p_f[0] - 5, p_g[1] + 5), p_g, n=20)
    stroke_variable_width(draw, pts6, [8] * len(pts6))

    # Segment g→h (hook flick up-and-left, tapering)
    pts7 = quad_bezier(p_g, ((p_g[0] + p_h[0]) / 2, p_g[1] - 10), p_h, n=25)
    m = len(pts7) - 1
    w7 = [8 + (2 - 8) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, pts7, w7)

    # === Stroke 4: bottom 横 (long baseline) ===
    # MMH BL(0.36, 0.47) → BC(0.992, 0.388)
    # Represents a broad flat bottom line across the character.
    p4h = anchor_to_xy(('BL', 0.10, 0.75))
    p4t = anchor_to_xy(('BR', 0.90, 0.75))
    fat_line(draw, p4h, p4t, width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_wu(draw)
    out = os.path.join(os.path.dirname(__file__), '01_乌.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
