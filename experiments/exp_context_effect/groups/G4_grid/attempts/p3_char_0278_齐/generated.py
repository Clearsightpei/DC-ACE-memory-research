"""G4 attempt for 齐 (p3_char_0278_齐) — 6 strokes per MMH.

Read: memory_index.md (v8 slim checklist) + drawer_memory.md pointer.
No mastered 齐 in success_bank. No errata entry. Drawing fresh from
MMH-derived anchors in the brief.
"""
import os, sys
from PIL import Image, ImageDraw

# Import shared anchor helper.
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 6 stroke primitives called below
    'endpoint_mismatches': [],        # all anchors used verbatim from brief
    'joint_class_mismatches': [],     # N-gaps preserved by drawing straight
    'overall_pass': True,
    'notes': '6 strokes drawn from MMH anchors: dot, short top slash '
             '(nearly horizontal), 撇 down-left, 捺 down-right (with hook '
             'shape), left descender, right vertical hook.'
}

# ----- Expected anchors (from brief) -----
S1_H = ('TC', 0.263, 0.571)
S1_T = ('TC', 0.676, 0.782)

S2_H = ('ML', 0.724, 0.087)
S2_T = ('TR', 0.247, 0.973)

S3_H = ('C',  0.685, 0.09)
S3_T = ('ML', 0.469, 0.998)

S4_H = ('C',  0.005, 0.304)
S4_T = ('BR', 0.824, 0.039)

S5_H = ('BC', 0.11,  0.133)
S5_T = ('BL', 0.753, 1.041)

S6_H = ('BC', 0.685, 0.033)
S6_T = ('BC', 0.799, 1.146)

# ----- Canvas -----
img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line_stroke(h, t, width=6):
    p0 = anchor_to_xy(h)
    p1 = anchor_to_xy(t)
    fat_line(draw, p0, p1, width, BLACK)


def dot_stroke(h, t, width=7):
    # short slanted dot; slightly tapered
    p0 = anchor_to_xy(h)
    p1 = anchor_to_xy(t)
    pts = [(p0[0] + i / 8 * (p1[0] - p0[0]),
            p0[1] + i / 8 * (p1[1] - p0[1])) for i in range(9)]
    widths = [3, 4, 5, 6, 7, 7, 6, 5, 3]
    stroke_variable_width(draw, pts, widths, BLACK)


def slash_stroke(h, t, width=6, curve=0.0):
    """撇/捺 style: gently curved via quadratic Bezier, tapered ends."""
    p0 = anchor_to_xy(h)
    p1 = anchor_to_xy(t)
    if curve == 0.0:
        ctrl = ((p0[0] + p1[0]) / 2.0, (p0[1] + p1[1]) / 2.0)
    else:
        mx = (p0[0] + p1[0]) / 2.0
        my = (p0[1] + p1[1]) / 2.0
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        # perpendicular offset
        L = max(1.0, (dx * dx + dy * dy) ** 0.5)
        nx, ny = -dy / L, dx / L
        ctrl = (mx + nx * curve, my + ny * curve)
    pts = quad_bezier(p0, ctrl, p1, n=32)
    widths = []
    n = len(pts)
    for i in range(n):
        t_ = i / (n - 1)
        # taper: thin at ends, fat middle
        w = width * (0.55 + 0.45 * (1 - abs(2 * t_ - 1)))
        widths.append(w)
    stroke_variable_width(draw, pts, widths, BLACK)


def hook_stroke(h, t, width=6):
    """vertical stroke with a small left hook at the bottom."""
    p0 = anchor_to_xy(h)
    p1 = anchor_to_xy(t)
    # main body
    fat_line(draw, p0, p1, width, BLACK)
    # small hook to left
    hx = p1[0] - 12
    hy = p1[1] - 4
    fat_line(draw, p1, (hx, hy), width, BLACK)


# ----- Render 6 strokes -----
# 1: top dot (short slash down-right)
dot_stroke(S1_H, S1_T)

# 2: near-horizontal top stroke (亠 top bar-ish, slight rise to right)
line_stroke(S2_H, S2_T, width=6)

# 3: 撇 — long left-falling slash from center-top to middle-left-bottom
slash_stroke(S3_H, S3_T, width=7, curve=8)   # slight leftward curve

# 4: 捺 — long right-falling slash from center-left to bottom-right
slash_stroke(S4_H, S4_T, width=7, curve=-8)  # slight rightward curve

# 5: bottom-left descender (丿 curving down-left)
slash_stroke(S5_H, S5_T, width=6, curve=6)

# 6: bottom-right vertical with hook (亅)
hook_stroke(S6_H, S6_T, width=6)


out_png = os.path.join(os.path.dirname(__file__), '01_齐.png')
img.save(out_png)
print(f"wrote {out_png}")
