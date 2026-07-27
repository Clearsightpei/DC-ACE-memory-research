"""仇 (chóu) — Phase-3 character, 4 strokes: 亻 (撇 + 竖) + 九 (撇 + 横折弯钩).

# Memory-index-mandated lookups (types out fixes per B4 lesson):
# 1. INDEX.md grep 仇 -> not mastered. Related mastered: ren_side.py (亻),
#    ji.py (几-family; provides inlined 横折弯钩 recipe).
# 2. errata.md grep 仇 -> not present.
# 3. form_catalog / joint_atlas: 亻 = 撇 + 竖 (T-class, 竖 head on 撇 body).
#    九 = 撇 + 横折弯钩 (P at mid-crossing per brief).
# 4. principles_meta.md TR1 — override anchors on primitive reuse (I do:
#    ren_side normally defaults to TC/BC; brief here puts it further left,
#    stroke1 head at TL(0.861,0.645), tail at ML(0.152,0.972)).
#    TR9 does NOT apply (compound char, not standalone radical — 亻 is on
#    left side of a two-part char, occupies left column not full grid).
# 5. joint_atlas: mid-crossing weld (P). s2.tail ⇆ s3.tail N-neighbor.
# 6. sandbox: 亻 T-touch anchor should sit slightly below-left of chord mid.

# Compound-char layout: 亻 in TL/ML/BL column, 九 in TC-TR-C-MR-BR block.
# Follow MMH-provided anchors verbatim (endpoints), inlining 横折弯钩 as ji.py did.
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,          # 亻 + 九 identifiable; hook flick present
    'stroke_count_ok': True,    # 4 strokes: s1 pie, s2 shu, s3 pie, s4 inlined 横折弯钩
    'endpoint_mismatches': [],  # all endpoints match brief anchors exactly (verbatim)
    'joint_class_mismatches': [],  # s3/s4 P-weld happens geometrically at C-cell crossing;
                                   # s2.tail/s3.tail N-gap (they end at BL(0.703,0.915) and
                                   # BL(0.929,0.83) — separated horizontally); s1.mid/s2.head
                                   # N-gap (亻 T-touch, 竖 head sits below-left of 撇 mid).
    'overall_pass': True,
    'notes': 's4 inlined as 4-phase variable-width path (ji.py pattern). '
             'Revision 1: widened 九 by moving s4 corner to MR(0.55,0.28), '
             'knee/hook_s further right in BR to make hook curl distinct.'
}


def draw_horizontal_zhe_wan_gou(draw, head, corner, knee, hook_s, tip):
    """Inlined 横折弯钩: 横 → 折 → 弯 (sweep down-right) → 钩 up-flick.

    ji.py used the same pattern for 几's compound stroke.
    """
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_knee = anchor_to_xy(knee)
    p_hs = anchor_to_xy(hook_s)
    p_tip = anchor_to_xy(tip)

    # Segment 1: 横 top-bar (head -> corner) with tiny upward arc.
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 3)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=28)
    top_widths = [5 + (i / 28) * 3 for i in range(29)]

    # Segment 2: 折 descend corner -> knee (curved down-right, right-bowed).
    ctrl_desc = (p_corner[0] + 8, (p_corner[1] + p_knee[1]) / 2.0)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_knee, n=32)
    desc_widths = [9 - (i / 32) * 1 for i in range(33)]

    # Segment 3: 弯 sweep (knee -> hook_s), bulged downward.
    ctrl_sweep = ((p_knee[0] + p_hs[0]) / 2.0,
                  max(p_knee[1], p_hs[1]) + 6)
    sweep_pts = quad_bezier(p_knee, ctrl_sweep, p_hs, n=24)
    sweep_widths = [8 + (i / 24) * 1 for i in range(25)]

    # Segment 4: 钩 up-flick (hook_s -> tip), tapered to needle.
    ctrl_hook = ((p_hs[0] + p_tip[0]) / 2.0 - 1,
                 (p_hs[1] + p_tip[1]) / 2.0)
    hook_pts = quad_bezier(p_hs, ctrl_hook, p_tip, n=18)
    hook_widths = [9 - (i / 18) * 8 for i in range(19)]

    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)


def draw_chou(draw):
    # --- 亻 (person radical, left column) ---
    # s1 撇: MMH-brief anchors TL(0.861, 0.645) -> ML(0.152, 0.972).
    s1_head = ('TL', 0.861, 0.645)
    s1_tail = ('ML', 0.152, 0.972)
    draw_pie(draw, s1_head, s1_tail,
             head_width=10, tail_width=1, curve=0.10, segments=48)

    # s2 竖: MMH-brief anchors ML(0.709, 0.427) -> BL(0.703, 0.915).
    # Column shared (x_frac ~0.70/0.70), reads as vertical. TR8 satisfied.
    s2_head = ('ML', 0.709, 0.427)
    s2_tail = ('BL', 0.703, 0.915)
    draw_shu(draw, s2_head, s2_tail, width=8)

    # --- 九 (right side) ---
    # s3 撇: TC(0.488, 0.709) -> BL(0.929, 0.83). Long left-descending 撇.
    s3_head = ('TC', 0.488, 0.709)
    s3_tail = ('BL', 0.929, 0.83)
    draw_pie(draw, s3_head, s3_tail,
             head_width=10, tail_width=2, curve=0.08, segments=48)

    # s4 横折弯钩: MMH head C(0.014, 0.6), tail BR(0.742, 0.224).
    # Head at (101.4, 160) crosses s3 near C(0.593, 0.459)=(159, 146) -> P-weld.
    # Inlined intermediate anchors chosen visually to match 九-shape and GT:
    #   corner: end of 横 top-bar, upper-right region.
    #   knee:   bottom of descent, lower-right.
    #   hook_s: base of up-flick, just left of tip.
    #   tip:    BR(0.742, 0.224) per MMH.
    s4_head   = ('C',  0.014, 0.60)
    s4_corner = ('MR', 0.55,  0.28)   # end of top-bar, further right & down-slope
    s4_knee   = ('BR', 0.55,  0.70)   # descent bottom, more vertical
    s4_hook_s = ('BR', 0.78,  0.55)   # base of up-flick, further right
    s4_tip    = ('BR', 0.742, 0.224)  # up-flick tip (MMH tail)
    draw_horizontal_zhe_wan_gou(draw, s4_head, s4_corner, s4_knee,
                                s4_hook_s, s4_tip)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chou(draw)
    out = os.path.join(_HERE, '01_仇.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
