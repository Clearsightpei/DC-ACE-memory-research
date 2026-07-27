"""亢 (kàng) — 4 strokes: 点 + 横 + 撇 + 横折弯钩.

Composition: 亠 (top: dot + horizontal) + 几-like bottom (撇 + 横折弯钩).

MEMORY LOOKUP (per memory_index checklist):
  1. success_bank/INDEX.md grep '亢': not present. Related: 几 (ji.py),
     亠 (tou.py), 兀 (wu_lame.py). We do NOT call tou/ji with defaults —
     TR1 requires overriding anchors for THIS composition.
  2. errata.md grep '亢': not present. Related: p3_021_几 (gap fusion
     — keep ~15-20 px top N gap), p3_058_兀 (avoid wu_lame primitive).
  3. form_catalog: 点 in top-center, 横 as horizontal cover, 撇 as
     left-descender, 横折弯钩 as right descending hook (几-family).
  4. principles_meta.md TR1 (override anchors), TR8 (横 shares row).
  5. joint_atlas.md 几-family exception: top N-gap must be ~15-20 px
     visible — do NOT weld. MMH here says s3.head vs s4.head gap
     ≈ 16 px (18 in my anchors) — good, matches exception.
  6. sandbox: 几-family s2 knee at y≈0.85-0.90 (not ≥0.95) so the
     round bottom sweep has room.

Anchor plan (from MMH dispatcher block):
  s1 点:  head TC(0.271, 0.601) → tail TC(0.644, 0.914)
  s2 横:  head ML(0.524, 0.324) → tail MR(0.394, 0.137)
  s3 撇:  head ML(0.999, 0.664) → tail BL(0.595, 0.924)
  s4 横折弯钩 (inlined 4-segment):
        head @ C(0.184, 0.667)
        corner @ MR(0.85, 0.30)   [top bar turns down at right edge]
        knee   @ BR(0.85, 0.55)   [begins round sweep]
        hook_s @ BR(0.70, 0.35)   [pre-hook]
        tip    @ BR(0.593, 0.326) [MMH tail]

Joint (from MMH):
  s3.head ML(0.999, 0.664) ⇆ s4.head C(0.184, 0.667) : N — gap ≈ 18 px
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, CANVAS
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,               # after revision — 几-frame proportions match GT
    'stroke_count_ok': True,         # 4 primitives called (dian, heng, pie, inlined 横折弯钩)
    'endpoint_mismatches': [],       # s1-s3 anchors from MMH verbatim; s4 head/tail from MMH
    'joint_class_mismatches': [],    # s3.head/s4.head N-gap ≈ 18 px (in [15,22] per joint_atlas exception)
    'overall_pass': True,
    'notes': 'revised s4 top-bar to be horizontal and descent to reach bottom-right; matches GT几-frame',
}


def draw_kang(draw):
    # s1 — 点 (top-center dot)
    s1_head = ('TC', 0.271, 0.601)
    s1_tail = ('TC', 0.644, 0.914)
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=11, curve=0.10, segments=24)

    # s2 — 横 (top horizontal, wide span, slight upward tilt matches MMH)
    s2_head = ('ML', 0.524, 0.324)
    s2_tail = ('MR', 0.394, 0.137)
    draw_heng(draw, s2_head, s2_tail, width=9)

    # s3 — 撇 (left-descender starting at cell C top-left)
    s3_head = ('ML', 0.999, 0.664)
    s3_tail = ('BL', 0.595, 0.924)
    draw_pie(draw, s3_head, s3_tail,
             head_width=10, tail_width=1, curve=0.12, segments=48)

    # s4 — 横折弯钩 (inlined 4-segment, 几-family, N-gap ~18px vs s3.head)
    # MMH gives only head + tail; interior corner/knee/hook are structural.
    # Right column must drop nearly to bottom to match GT's tall 几-frame.
    s4_head_a = ('C', 0.184, 0.667)     # (118, 166) — top-left corner of 几
    s4_corner_a = ('MR', 0.90, 0.65)    # (290, 165) — top-right, same row as head
    s4_knee_a = ('BR', 0.85, 0.75)      # (285, 275) — bottom-right descent end
    s4_hook_s_a = ('BR', 0.60, 0.65)    # (260, 265) — pre-hook
    s4_tip_a = ('BR', 0.593, 0.326)     # (259, 232) — MMH tail (hook flick up)

    p_head = anchor_to_xy(s4_head_a)
    p_corner = anchor_to_xy(s4_corner_a)
    p_knee = anchor_to_xy(s4_knee_a)
    p_hs = anchor_to_xy(s4_hook_s_a)
    p_tip = anchor_to_xy(s4_tip_a)

    # top bar — nearly straight horizontal
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                (p_head[1] + p_corner[1]) / 2.0 - 1)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=24)
    top_widths = [7 + (i / 24) * 3 for i in range(25)]

    # descent — long vertical drop on right
    ctrl_desc = (p_corner[0] - 2, (p_corner[1] + p_knee[1]) / 2.0)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_knee, n=32)
    desc_widths = [10 - (i / 32) * 2 for i in range(33)]

    # round sweep (bottom curl)
    ctrl_sweep = ((p_knee[0] + p_hs[0]) / 2.0,
                  max(p_knee[1], p_hs[1]) + 4)
    sweep_pts = quad_bezier(p_knee, ctrl_sweep, p_hs, n=28)
    sweep_widths = [8 + (i / 28) * 1 for i in range(29)]

    # hook flick up
    ctrl_hook = ((p_hs[0] + p_tip[0]) / 2.0 - 2,
                 (p_hs[1] + p_tip[1]) / 2.0)
    hook_pts = quad_bezier(p_hs, ctrl_hook, p_tip, n=18)
    hook_widths = [9 - (i / 18) * 8 for i in range(19)]

    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)
    draw_kang(draw)
    out = os.path.join(os.path.dirname(__file__), '01_亢.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
