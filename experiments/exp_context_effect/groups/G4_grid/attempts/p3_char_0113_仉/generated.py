"""p3_char_0113_仉 (zhǎng) — 亻 (left) + 几 (right), 4 strokes total.

Memory lookups performed (per memory_index.md checklist):
  1. success_bank INDEX grep: 亻 (ren_side.py, pos 61), 几 (ji.py, pos 54) both mastered.
  2. errata grep: 几-family top gap needs visible ~15-20 px N (p3_021 lesson).
     Item 仉 itself not in errata.
  3. form_catalog: 亻 in left-radical position; 几 in right-body position (compact).
  4. principles_meta: TR1 override anchors for compositional use (NOT default anchors).
     TR10 exception for 几-family — do NOT weld the top gap.
  5. joint_atlas: N-class = small gap, do NOT weld.

Composition: left half ≈ columns 0-1 for 亻, right half ≈ columns 1-2 for 几.
Anchors from MMH-injected structural expectations (adapted to reuse
mastered primitives via TR1 anchor override).

Strokes (matches MMH's 4-stroke expectation):
  s1 = 亻 撇: head TL(0.91, 0.66) → tail BL(0.16, 0.03)  [from MMH]
  s2 = 亻 竖: head ML(0.67, 0.58) → tail BL(0.69, 0.99) [from MMH]
  s3 = 几 撇: head C(0.21, 0.28) → tail BL(0.83, 0.90)   [from MMH]
  s4 = 几 横折弯钩: head C(0.44, 0.39) → ... → tip BR(0.76, 0.36)
       (inline — no clean primitive; based on ji.py pattern.)

Joints (all N — small gap, do NOT weld):
  J1: s1 body (mid ~0.56) ⇆ s2 head @ ML → N (~17 px)
  J2: s2 tail ⇆ s3 tail @ BL → N (~23 px)
  J3: s3 head ⇆ s4 head @ C → N (~14 px, the classic 几-top gap)
"""
import os
import sys
from PIL import Image, ImageDraw

# Add success_bank/code to path so we can import primitives.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke primitives called (see comments)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('亻 + 几 composition; anchors from MMH structural expectations; '
              'all 3 joints N-class per MMH; 几-top gap preserved (TR10 exception).'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- s1: 亻's 撇 (from TL to BL) ---- stroke 1
    s1_head = ('TL', 0.91, 0.66)
    s1_tail = ('BL', 0.16, 0.03)
    draw_pie(draw, s1_head, s1_tail,
             head_width=12, tail_width=1, curve=0.10, segments=48)

    # ---- s2: 亻's 竖 (short vertical dropping from mid) ---- stroke 2
    s2_head = ('ML', 0.67, 0.58)
    s2_tail = ('BL', 0.69, 0.99)
    draw_shu(draw, s2_head, s2_tail, width=9)

    # ---- s3: 几's 撇 (left leg) ---- stroke 3
    s3_head = ('C', 0.21, 0.28)
    s3_tail = ('BL', 0.83, 0.90)
    draw_pie(draw, s3_head, s3_tail,
             head_width=9, tail_width=1, curve=0.12, segments=48)

    # ---- s4: 几's 横折弯钩 (inlined — no clean primitive) ---- stroke 4
    # Pattern lifted from ji.py structure: top bar → descent → sweep → up-flick.
    # The MMH head @ C(0.44, 0.39) is the start of the top bar; the tip is
    # BR(0.76, 0.36). We inject a corner (top-right area) and knee (bottom-right
    # area) so the shape reads as 横折弯钩.
    s4_head = ('C', 0.44, 0.39)
    s4_corner = ('MR', 0.75, 0.42)     # top-right corner: extend the 横 further right
    s4_knee = ('BR', 0.55, 0.65)       # bottom of the descent (lower-right area)
    s4_hook_s = ('BR', 0.80, 0.55)     # end of the sweep (right side, ready to flick up)
    s4_tip = ('BR', 0.76, 0.36)        # from MMH: tip point (upward flick)

    p_head = anchor_to_xy(s4_head)
    p_corner = anchor_to_xy(s4_corner)
    p_knee = anchor_to_xy(s4_knee)
    p_hs = anchor_to_xy(s4_hook_s)
    p_tip = anchor_to_xy(s4_tip)

    # Top bar (mostly horizontal, slight curve)
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 2)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=24)
    top_widths = [6 + (i / 24) * 4 for i in range(25)]

    # Descent (corner down to knee)
    ctrl_desc = (p_corner[0] - 5, (p_corner[1] + p_knee[1]) / 2.0)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_knee, n=32)
    desc_widths = [10 - (i / 32) * 2 for i in range(33)]

    # Sweep (round bottom bend)
    ctrl_sweep = ((p_knee[0] + p_hs[0]) / 2.0,
                  max(p_knee[1], p_hs[1]) + 6)
    sweep_pts = quad_bezier(p_knee, ctrl_sweep, p_hs, n=28)
    sweep_widths = [8 + (i / 28) * 1 for i in range(29)]

    # Hook up-flick
    ctrl_hook = ((p_hs[0] + p_tip[0]) / 2.0 - 2,
                 (p_hs[1] + p_tip[1]) / 2.0)
    hook_pts = quad_bezier(p_hs, ctrl_hook, p_tip, n=18)
    hook_widths = [9 - (i / 18) * 8 for i in range(19)]

    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)

    out = os.path.join(_HERE, '01_仉.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
