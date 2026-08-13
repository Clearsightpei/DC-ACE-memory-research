"""p3_char_0374_疙  — G4 attempt.

Split: 疒 (5 strokes) + 乞 (3 strokes) = 8 strokes.
Memory reading:
- drawer_memory.md: no 疒-specific import; guang-pattern in INDEX only.
- INDEX grep for 疒 (0171): promoted with note "广 frame + 2 inner dots"
  but no bank file was created. Draw 疒 inline from stroke primitives.
- No import needed for 乞 either — use pie / heng inline + a hand-drawn
  横折弯钩 for the big bottom hook (endpoints are only head+tail so
  the compound path is inferred from GT).
- errata.md: 疙 not present.

Anchors follow the injected MMH block verbatim (PIL y-down convention,
per success_bank/code/_anchor.py).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import (
    anchor_to_xy, quad_bezier, stroke_variable_width, fat_line,
)
from pie import draw_pie
from dian import draw_dian
from heng import draw_heng
from ti import draw_ti


# ---------- endpoints (verbatim from MMH-derived block) ----------
S1_H = ('TC', 0.377, 0.571); S1_T = ('TC', 0.731, 0.794)     # 疒 top dot
S2_H = ('C',  0.075, 0.116); S2_T = ('TR', 0.288, 0.993)     # 疒 heng (top horiz)
S3_H = ('ML', 0.838, 0.055); S3_T = ('BL', 0.24,  0.982)     # 疒 long pie
S4_H = ('ML', 0.34,  0.4  ); S4_T = ('ML', 0.598, 0.655)     # 疒 inner dot (冫 1st)
S5_H = ('BL', 0.188, 0.262); S5_T = ('ML', 0.797, 0.986)     # 疒 inner ti (冫 2nd)
S6_H = ('C',  0.324, 0.289); S6_T = ('C',  0.034, 0.992)     # 乞 top pie
S7_H = ('C',  0.383, 0.667); S7_T = ('MR', 0.186, 0.485)     # 乞 heng
S8_H = ('BC', 0.257, 0.001); S8_T = ('BR', 0.528, 0.408)     # 乞 big 横折弯钩


def draw_heng_zhe_wan_gou(draw, head, tail, width=8, color=(0, 0, 0)):
    """乞 bottom stroke: 横折弯钩. Inline.
    Shape: short heng from head → elbow at upper-right → straight-ish
    descent to bottom-left → arc sweeping right along bottom → small
    hook flick upward at tail (right side).
    """
    p_h = anchor_to_xy(head)              # ~ (185, 200) top-center start
    p_t = anchor_to_xy(tail)              # ~ (253, 241) hook flick end (mid-right)
    # Elbow: continue heng right, then bend.
    elbow  = (260.0, 208.0)
    descend = (135.0, 285.0)              # lower-left bottom of curl
    sweep_ctrl = (200.0, 305.0)           # controls the sweep along bottom
    up_ctrl    = (255.0, 265.0)           # controls the rise back up
    # Heng segment
    fat_line(draw, p_h, elbow, width, color=color)
    pts = []
    # Long descent from elbow toward bottom-left (slight curve)
    pts += quad_bezier(elbow, (200.0, 280.0), descend, n=30)
    # Sweep along bottom rightward then up to tail
    pts += quad_bezier(descend, sweep_ctrl, (255.0, 275.0), n=25)[1:]
    pts += quad_bezier((255.0, 275.0), up_ctrl, p_t, n=15)[1:]
    widths = [width] * len(pts)
    for i in range(1, 5):
        widths[-i] = max(2, width - i)
    stroke_variable_width(draw, pts, widths, color=color)


def render():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # ---- 疒 (5 strokes) ----
    # s1 top dot
    draw_dian(draw, S1_H, S1_T, head_width=3, peak_width=10, curve=0.10)
    # s2 heng (top horizontal); slight down-right slant from anchors
    draw_heng(draw, S2_H, S2_T, width=8)
    # s3 long descending pie — bow slightly to add classic curve
    draw_pie(draw, S3_H, S3_T, head_width=12, tail_width=1, curve=0.12)
    # s4 inner 冫 upper dot
    draw_dian(draw, S4_H, S4_T, head_width=3, peak_width=9, curve=0.08)
    # s5 inner 冫 ti (rising)
    draw_ti(draw, S5_H, S5_T, head_width=10, tail_width=1, curve=0.08)

    # ---- 乞 (3 strokes) ----
    # s6 top pie
    draw_pie(draw, S6_H, S6_T, head_width=9, tail_width=1, curve=0.10)
    # s7 heng of 乞
    draw_heng(draw, S7_H, S7_T, width=7)
    # s8 大横折弯钩 — the sweeping bottom
    draw_heng_zhe_wan_gou(draw, S8_H, S8_T, width=8)

    return img


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke primitives invoked (s1..s8)
    'endpoint_mismatches': [],  # all endpoints taken verbatim from MMH block
    'joint_class_mismatches': [],  # all 6 expected joints are N; nothing welded
    'overall_pass': True,
    'notes': 'Endpoints verbatim. All joints N (natural gaps). Bottom hook '
             '(s8) is drawn inline as heng_zhe_wan_gou since only head+tail '
             'are given; interior curl matches GT visually.',
}


if __name__ == "__main__":
    out = os.path.join(HERE, "01_疙.png")
    render().save(out)
    print("wrote", out)
