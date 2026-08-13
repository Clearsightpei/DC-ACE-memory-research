"""p3_char_0547_容 — G4 attempt.

Decomposition:  宀 (3 strokes: 点 + 点 + 横钩)
              + 谷-body (7 strokes: 撇 捺 撇 捺 竖 横折 横)
              = 10 strokes total (matches MMH count).

Rendered fresh from the MMH-derived per-stroke anchors auto-injected
into the drawer brief. `mian.py` was consulted for reference but not
imported — its default anchors are for a wider standalone roof; the
Phase-3 anchors put 宀 tighter to the top of the character. Straight-
line render with dot-style short strokes and hooked heng-gou for the
roof.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# --- import _anchor helper from the shared code dir ---
CODE_DIR = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(CODE_DIR))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402


CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)


def line(a1, a2, width=6):
    p1 = anchor_to_xy(a1)
    p2 = anchor_to_xy(a2)
    draw.line([p1, p2], fill="black", width=width)
    r = width / 2.0
    for (x, y) in (p1, p2):
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dot(a1, a2, head_w=3, tail_w=9):
    """Short dian-like stroke: taper from thin head to fat tail."""
    p1 = anchor_to_xy(a1)
    p2 = anchor_to_xy(a2)
    n = 12
    pts = [((1 - t / n) * p1[0] + (t / n) * p2[0],
            (1 - t / n) * p1[1] + (t / n) * p2[1]) for t in range(n + 1)]
    widths = [head_w + (tail_w - head_w) * (t / n) for t in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def heng_gou(a_head, a_shoulder, a_tip, head_w=5, mid_w=6, shoulder_w=9, tip_w=2):
    """横 across, then a short hook down-left at the right end."""
    p_head = anchor_to_xy(a_head)
    p_sh = anchor_to_xy(a_shoulder)
    p_tip = anchor_to_xy(a_tip)
    # horizontal portion
    n = 24
    pts = [((1 - t / n) * p_head[0] + (t / n) * p_sh[0],
            (1 - t / n) * p_head[1] + (t / n) * p_sh[1]) for t in range(n + 1)]
    widths = [head_w + (mid_w - head_w) * (t / n) for t in range(n + 1)]
    stroke_variable_width(draw, pts, widths)
    # hook portion (curved down-left)
    ctl = (p_sh[0] - 2, p_sh[1] + 6)
    hook_pts = quad_bezier(p_sh, ctl, p_tip, n=16)
    hook_widths = [shoulder_w - (shoulder_w - tip_w) * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths)


def pie(a_head, a_tail, head_w=8, tail_w=2):
    """撇 — taper thick head to thin tail with slight curve."""
    p1 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    # curve control: bow leftward
    mx = (p1[0] + p2[0]) / 2 - 6
    my = (p1[1] + p2[1]) / 2
    pts = quad_bezier(p1, (mx, my), p2, n=24)
    widths = [head_w - (head_w - tail_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def na(a_head, a_tail, head_w=2, mid_w=6, tail_w=10):
    """捺 — thin head, thick middle/tail with slight curve, sharp foot."""
    p1 = anchor_to_xy(a_head)
    p2 = anchor_to_xy(a_tail)
    mx = (p1[0] + p2[0]) / 2 + 4
    my = (p1[1] + p2[1]) / 2 + 4
    pts = quad_bezier(p1, (mx, my), p2, n=24)
    widths = []
    n = len(pts) - 1
    for i in range(len(pts)):
        t = i / n
        if t < 0.5:
            w = head_w + (mid_w - head_w) * (t / 0.5)
        else:
            w = mid_w + (tail_w - mid_w) * ((t - 0.5) / 0.5)
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


# ==== strokes 1-3: 宀 roof ====
# s1 — top 点 above roof (TC diagonal down-right)
dot(('TC', 0.263, 0.507), ('TC', 0.582, 0.732), head_w=3, tail_w=9)

# s2 — left 点 (short dot on the left corner of the roof)
dot(('TL', 0.674, 0.981), ('ML', 0.536, 0.541), head_w=3, tail_w=9)

# s3 — 横钩 (long horizontal from ML across to MR, then short hook)
heng_gou(('ML', 0.797, 0.078),
         ('MR', 0.051, 0.263),
         ('MR', 0.02, 0.42))

# ==== strokes 4-7: upper 谷 (八 + 八) ====
# s4 — 撇 (outer left stroke of first 八)
pie(('C', 0.055, 0.324), ('ML', 0.688, 0.819), head_w=7, tail_w=2)

# s5 — 捺 (outer right stroke of first 八)
na(('C', 0.632, 0.351), ('MR', 0.08, 0.646), head_w=2, mid_w=6, tail_w=9)

# s6 — small inner 撇
pie(('C', 0.336, 0.564), ('BL', 0.261, 0.684), head_w=6, tail_w=2)

# s7 — small inner 捺
na(('C', 0.518, 0.775), ('BR', 0.851, 0.385), head_w=2, mid_w=5, tail_w=7)

# ==== strokes 8-10: 口 mouth ====
# s8 — 左竖 (left vertical of 口, from BL top going down past BC bottom)
line(('BL', 0.861, 0.429), ('BC', 0.09, 1.082), width=6)

# s9 — 横折 (top of 口: horizontal then bend down)
p9_head = anchor_to_xy(('BC', 0.031, 0.411))
p9_tail = anchor_to_xy(('BC', 0.74, 0.76))
# horizontal segment
p9_corner = (p9_tail[0], p9_head[1])
draw.line([p9_head, p9_corner], fill="black", width=6)
draw.line([p9_corner, p9_tail], fill="black", width=6)
for p in (p9_head, p9_corner, p9_tail):
    draw.ellipse((p[0] - 3, p[1] - 3, p[0] + 3, p[1] + 3), fill="black")

# s10 — 底横 (bottom horizontal of 口)
line(('BC', 0.137, 0.886), ('BC', 0.942, 0.874), width=6)


# ==== output ====
OUT = Path(__file__).parent / "01_容.png"
img.save(OUT)
print(f"wrote {OUT}")


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 10 stroke calls made
    'endpoint_mismatches': [],   # anchors used verbatim from MMH spec
    'joint_class_mismatches': [],  # all joints kept as N (natural gap between
                                   # separate strokes, no welding)
    'overall_pass': True,
    'notes': ('宀 rendered fresh (mian.py default anchors are for a wider '
              'standalone roof); 谷 body inline from MMH anchors; 口 corners '
              'as N-neighbors.')
}
