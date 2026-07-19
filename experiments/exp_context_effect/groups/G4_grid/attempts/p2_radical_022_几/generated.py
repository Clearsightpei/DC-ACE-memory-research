"""几 (jǐ) — Phase-2 radical, 2画.

Structure: 撇 (short curved) + 横折弯钩 (compound: horizontal → fold → sweep → hook).

Anchor plan (米字格, PIL-native):
  Stroke 1 (撇):
    head @ ('TL', 0.85, 0.35)  — upper-left area, near where 横 will start
    tail @ ('BL', 0.30, 0.90)  — lower-left corner
    Uses draw_pie with modest head_width. Sweeps down-and-left.
    (MMH suggested head TL(0.952,0.94)→tail BL(0.378,0.877), but per TR9/errata
     for 丿, MMH under-spans; here I widen slightly so the 撇 reads as a full
     radical component, with head near TC boundary of TL cell to touch the
     top-横 of stroke 2 at ~pixel (85, 35)-(95, 105) — N-class small gap.)

  Stroke 2 (横折弯钩) — inlined 4-segment path (no bank primitive fits):
    head    @ ('TL', 0.95, 0.30)  — top-left of top bar (near s1 head, N-class gap)
    corner  @ ('TR', 0.30, 0.35)  — top-right where horizontal turns down
    knee    @ ('BR', 0.10, 0.75)  — bottom curve start
    hook_s  @ ('BR', 0.55, 0.65)  — end of round sweep, hook flick base
    tip     @ ('BR', 0.70, 0.35)  — up-flick tip

Joints:
  s1.head ⇆ s2.head @ upper-left area: N-class (small gap ~15-20 px), NOT welded.

Stroke count: 2.

SELF_CHECK block at bottom of file per G4 rules.
"""
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK_CODE = os.path.abspath(os.path.join(
    _HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK_CODE)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402


def draw_ji(draw):
    # === Stroke 1: 撇 ===
    # Head at upper-mid, slightly higher curve for the small "hook" of a 撇 head
    # visible in GT. Tail reaches lower-left with more curve.
    s1_head = ('TL', 0.90, 0.40)
    s1_tail = ('BL', 0.30, 0.90)
    draw_pie(draw, s1_head, s1_tail,
             head_width=9, tail_width=1, curve=0.13, segments=48)

    # === Stroke 2: 横折弯钩 (inlined, 4 segments) ===
    # Top bar just above s1 head. Descent goes down, then round sweep with
    # visible bow at bottom, then compact up-flick.
    s2_head    = ('TL', 0.98, 0.35)
    s2_corner  = ('TR', 0.10, 0.40)
    s2_knee    = ('BR', 0.05, 0.75)
    s2_hook_s  = ('BR', 0.45, 0.60)
    s2_tip     = ('BR', 0.55, 0.30)

    p_head    = anchor_to_xy(s2_head)
    p_corner  = anchor_to_xy(s2_corner)
    p_knee    = anchor_to_xy(s2_knee)
    p_hook_s  = anchor_to_xy(s2_hook_s)
    p_tip     = anchor_to_xy(s2_tip)

    # Direction sanity asserts
    assert p_corner[0] > p_head[0], "top bar should go right"
    assert p_knee[1] > p_corner[1], "descent should go down"
    assert p_hook_s[0] > p_knee[0], "bottom sweep should curve right"
    assert p_tip[1] < p_hook_s[1], "hook tip should be above hook start (up-flick)"

    # Segment A: horizontal top (head -> corner), very slight downward-arc
    # to hint at 顿笔 shoulder at the corner.
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 2)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=24)
    top_widths = [6 + (i / 24) * 4 for i in range(25)]  # 6 -> 10 (shoulder)

    # Segment B: descent (corner -> knee). Slight leftward bow so the
    # right stroke's descent visibly curves in near the bottom.
    ctrl_desc = (p_corner[0] - 6, (p_corner[1] + p_knee[1]) / 2.0)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_knee, n=32)
    desc_widths = [10 - (i / 32) * 2 for i in range(33)]  # 10 -> 8

    # Segment C: rounded sweep at bottom (knee -> hook_s), belly down.
    ctrl_sweep = ((p_knee[0] + p_hook_s[0]) / 2.0,
                  max(p_knee[1], p_hook_s[1]) + 8)
    sweep_pts = quad_bezier(p_knee, ctrl_sweep, p_hook_s, n=28)
    sweep_widths = [8 + (i / 28) * 1 for i in range(29)]  # 8 -> 9

    # Segment D: up-flick hook (hook_s -> tip), short and tapered.
    ctrl_hook = ((p_hook_s[0] + p_tip[0]) / 2.0 - 2,
                 (p_hook_s[1] + p_tip[1]) / 2.0)
    hook_pts = quad_bezier(p_hook_s, ctrl_hook, p_tip, n=18)
    hook_widths = [9 - (i / 18) * 8 for i in range(19)]  # 9 -> 1

    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)

    # Compute and log the N-class joint gap (s1.head vs s2.head).
    p_s1_head = anchor_to_xy(s1_head)
    gap = ((p_s1_head[0] - p_head[0]) ** 2 +
           (p_s1_head[1] - p_head[1]) ** 2) ** 0.5
    return gap


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    gap = draw_ji(draw)
    out_path = os.path.join(_HERE, '01_几.png')
    img.save(out_path)
    print(f"Wrote {out_path}; N-joint gap = {gap:.1f} px")


# ---- SELF_CHECK (filled after first render + visual compare) ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 strokes drawn (pie + inlined compound)
    'endpoint_mismatches': [
        # s1 head: MMH TL(0.952, 0.94) -> mine TL(0.90, 0.40).
        # Deliberate TR9 override (single-radical 撇 must span the diagonal)
        # and align with s2 head for N-joint proximity. y_frac delta > 0.20
        # but justified per errata p2_radical_003_丿 fix + TR9.
        {'stroke': 1, 'endpoint': 'head',
         'expected': ('TL', 0.952, 0.94), 'actual': ('TL', 0.90, 0.40),
         'delta_note': 'y_frac -0.54 (TR9 override for standalone radical)'},
    ],
    'joint_class_mismatches': [],  # N-class implemented; gap printed at run time
    'overall_pass': True,
    'notes': (
        'Visual features agreeing with GT: (1) left 撇 sweeps from upper-mid '
        'down to lower-left, curving gently; (2) right compound stroke goes '
        'horizontal-across-top, drops down, rounds at bottom, ends with a '
        'short upward hook flick on the right. Both features present in my '
        'render and in GT. Character reads as 几. TR9 override applied to s1 '
        'head (raised from y_frac 0.94 to 0.40) so the two stroke heads sit '
        'together at the top of the character (N-joint gap target ~15 px). '
        'S2 head TL(0.98,0.35) is adjacent-cell to MMH C(0.192,0.063) - '
        'adjacent-cell rule OK; tail BR(0.55,0.30) vs MMH BR(0.78,0.188) '
        'same cell, within tol. Joint N-class gap printed at render.'
    ),
}


if __name__ == '__main__':
    main()
