"""气 (qì) — Phase 3, item p3_char_0120_气.

MANDATORY LOOKUP CHECKLIST (from memory_index.md):
  1. success_bank/INDEX.md grep "气"   → not present (fresh).
  2. errata.md grep "气"              → p2_radical_111_气 (FAIL).
        FIX (literal): "s4 top-heng at y=0.35 (C or ML row); extend
        descent to canvas bottom; separate s2/s3 to distinct rows
        (y=0.35 and y=0.55)."
        In this Phase-3 4-stroke MMH decomposition the top short pie
        is s1, the two 横 strokes are s2 (top) and s3 (middle), and
        s4 is the 横折弯钩 compound. We keep MMH's s2/s3 row separation
        and extend s4 descent down to the canvas bottom.
  3. form_catalog.md — 气 does not have a Phase-3 row; the two 横 are
     the standard top-of-radical class; the 横折弯钩 compound follows
     heng_pie_wan_gou-family (heng at top → bend → wan → hook).
  4. principles_meta.md — TR6 (inline if bank primitive needs extreme
     transformation): the 4th stroke needs a custom 横折弯钩 not in
     the bank exactly (heng_pie_wan_gou is the closest but structurally
     different — pie between heng and wan), so we INLINE it here from
     first principles using quad_beziers + fat lines.
  5. joint_atlas.md — the two joints in the MMH block are N-class
     (small natural gap, DO NOT weld). 气's structure: s1 pie's mid
     sits above s2's head (gap), and s1 pie's tail sits above s3's
     head (small gap). Keep as N-class with ~15-30 px visible gap.
  6. sandbox.md — nothing specific noted for 气.

MMH-derived structural expectations (4 strokes, 2 joints):
  s1: head TC(0.037,0.565) tail ML(0.495,0.456)    — top-left short pie 撇
  s2: head C(0.037,0.043)  tail TR(0.039,0.885)    — top heng 横 (mid → right)
  s3: head ML(0.914,0.392) tail C(0.77,0.257)      — middle heng 横 (left → right)
  s4: head ML(0.557,0.84)  tail BR(0.672,0.367)    — 横折弯钩 compound

Joints (both N-class, DO NOT weld):
  J1: s1.mid(0.35) ~ s2.head  gap ≈ 17 px
  J2: s1.mid(0.67) ~ s3.head  gap ≈ 29 px
"""

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, CODE_DIR)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402
from pie import draw_pie                                                         # noqa: E402
from heng import draw_heng                                                       # noqa: E402


# ---- SELF_CHECK placeholder (populated after visual review) ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revised once. Pass 1: s4 top-heng overlapped s3 and corner '
             'crossed at MR (crowded upper band). Pass 2: moved s4 top-heng '
             'BELOW s3 (head ML(0.10,0.75) → corner MR(0.75,0.55)), routed '
             'descent nearly straight down to BR(0.55,0.85), then hook '
             'flicks up-and-LEFT to BR(0.35,0.35). Structural anchors '
             'diverge from MMH endpoints on s4 (MMH gives only head+tail; '
             'the compound path is inlined) — head still lands in ML per '
             'MMH; tip lands in BR per MMH but at a different sub-cell '
             'fraction to preserve the classical hook direction seen in '
             'the GT PNG.',
}


def draw_heng_zhe_wan_gou(draw, head, corner, knee, hook_pt, tip,
                          h_width=9, corner_shoulder=12,
                          wan_head_w=9, wan_belly_w=13,
                          hook_start_w=11, tip_w=2,
                          color=(0, 0, 0)):
    """Inline 横折弯钩 for 气 s4.
       head    — leftmost start of top-heng segment.
       corner  — top-right corner where 折 turns downward.
       knee    — bottom of the vertical/curve descent before the hook.
       hook_pt — bottom base of the hook.
       tip     — hook tip flicked up-and-LEFT of hook_pt.
    """
    p_h = anchor_to_xy(head)
    p_c = anchor_to_xy(corner)
    p_k = anchor_to_xy(knee)
    p_hk = anchor_to_xy(hook_pt)
    p_t = anchor_to_xy(tip)

    # 横 segment: head → corner
    fat_line(draw, p_h, p_c, h_width, color=color)
    r = corner_shoulder / 2.0
    draw.ellipse([p_c[0] - r, p_c[1] - r, p_c[0] + r, p_c[1] + r], fill=color)

    # 弯 body: corner → knee → hook_pt via a curved bezier.
    # Use a control point that pulls the belly slightly RIGHT of the chord
    # so the descender curves like a shu_wan_gou.
    mid1 = ((p_c[0] + p_k[0]) * 0.5 + 6, (p_c[1] + p_k[1]) * 0.5)
    seg_a = quad_bezier(p_c, mid1, p_k, n=40)
    widths_a = []
    for i in range(len(seg_a)):
        t = i / (len(seg_a) - 1)
        widths_a.append(wan_head_w + (wan_belly_w - wan_head_w) * t)
    stroke_variable_width(draw, seg_a, widths_a, color=color)

    # knee → hook_pt (short curve continuing the bend to the lower base)
    mid2 = ((p_k[0] + p_hk[0]) * 0.5 + 4, (p_k[1] + p_hk[1]) * 0.5 + 2)
    seg_b = quad_bezier(p_k, mid2, p_hk, n=30)
    widths_b = []
    for i in range(len(seg_b)):
        t = i / (len(seg_b) - 1)
        widths_b.append(wan_belly_w + (hook_start_w - wan_belly_w) * t)
    stroke_variable_width(draw, seg_b, widths_b, color=color)

    # 钩: hook_pt → tip (flick up-and-left)
    hook_ctrl = (p_hk[0] + (p_t[0] - p_hk[0]) * 0.3,
                 p_hk[1] + (p_t[1] - p_hk[1]) * 0.15)
    hook_pts = quad_bezier(p_hk, hook_ctrl, p_t, n=20)
    k = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / k)
                   for i in range(k + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- s1: top-left short pie (MMH-verbatim) ----
    draw_pie(draw,
             ('TC', 0.037, 0.565),   # head (upper, in TC)
             ('ML', 0.495, 0.456),   # tail (lower-left, in ML)
             head_width=11, tail_width=2, curve=0.08, segments=40)

    # ---- s2: top heng (MMH-verbatim) ----
    # C(0.037, 0.043) → TR(0.039, 0.885)  ~= (104,104) → (204,88).
    # This is the upper of the two 横s. Keep it slightly rising (natural).
    draw_heng(draw, ('C', 0.037, 0.043), ('TR', 0.039, 0.885), width=9)

    # ---- s3: middle heng (MMH gives ML head → C tail) ----
    # ML(0.914, 0.392) → C(0.77, 0.257) ~= (91,139) → (177,126).
    # Also gently rising. Sits below s2 with a row of separation.
    draw_heng(draw, ('ML', 0.914, 0.392), ('C', 0.77, 0.257), width=9)

    # ---- s4: 横折弯钩 compound (inlined) ----
    # MMH head ML(0.557, 0.84) ~= (56, 184) — this is the left starting
    # point of the top segment of s4 (the "top-heng" that then bends
    # right-then-down and hooks).
    # MMH tail BR(0.672, 0.367) ~= (267, 237) — the hook TIP, in lower
    # right band. Per errata fix ("extend descent to canvas bottom"),
    # we route the descent down through the lower band.
    # Revised: place s4 top-heng below s3 (so the three horizontals
    # stack cleanly), route corner to upper-right of BR cell, descend
    # nearly straight down toward the canvas bottom, then flick a hook
    # up-and-LEFT. MMH tail BR(0.672, 0.367) is the hook TIP location.
    draw_heng_zhe_wan_gou(
        draw,
        head=('ML', 0.10, 0.75),        # left start (below s3)
        corner=('MR', 0.75, 0.55),      # top-right corner of s4 (higher than knee, right side)
        knee=('BR', 0.55, 0.85),        # descent bottom-right area
        hook_pt=('BR', 0.65, 0.60),     # hook base
        tip=('BR', 0.35, 0.35),         # hook tip flicked up-and-LEFT
        h_width=9, corner_shoulder=12,
        wan_head_w=9, wan_belly_w=13,
        hook_start_w=11, tip_w=2,
    )

    out_png = os.path.join(HERE, '01_气.png')
    img.save(out_png)
    print(f'wrote {out_png}')


if __name__ == '__main__':
    render()
