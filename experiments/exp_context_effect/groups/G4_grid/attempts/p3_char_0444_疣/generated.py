"""疣 (yóu) — 9 strokes.
Decomposition: 疣 = 疒 (left+top enclosing radical, 5 strokes) + 尤 (interior, 4 strokes).
  疒 = 点(s1) + 横(s2) + 长撇(s3) + 点(s4) + 提(s5)
  尤 = 短横(s6) + 撇(s7) + 竖弯钩(s8) + 点(s9)

Memory notes consulted:
- memory_index.md v8 slim checklist
- drawer_memory.md B9/B10/B11 A-recipe: MMH-verbatim anchors + inline base primitives
- errata.md 疒-family (疡): "疒 top dot LAST; interior stacked"
- INDEX.md: no 疣, no 尤 bank primitive. 疒 mastered (as 广+dots pattern) but per A-recipe
  point 4 (avoid partial-override of compound primitives), inline with MMH-verbatim anchors.

Strategy: pure MMH-verbatim per A-recipe. Draw top-dot LAST (per errata 疡 rule).
No compound bank primitive fits well (尤 not in bank; 疒 primitive default anchors
would clash with MMH placement). Inlining base primitives.
"""
# No BANK_DEVIATION block: we did not skip any specific bank primitive we would
# otherwise have used — no 尤 primitive exists; 疒 inlined per B9 point 4 (base
# primitives over compound bank when MMH placement dominates).

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '../../success_bank/code')))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 draw calls, matches MMH expected 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim. s6-s7 welded (P) at C(0.536,0.8). '
             'N-joints preserved as natural gaps. Top-dot s1 rendered last.',
}


def draw_ti(draw, from_anchor, to_anchor,
            head_width=10, tail_width=2, curve=0.05, segments=32,
            color=(0, 0, 0)):
    """提 (tí) — rising short stroke, thick head → needle tail."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ----- 疒 (strokes 1-5) — outer enclosing radical -----
    # s2: 横 (top horizontal of 疒)
    #   head @ C(0.049, 0.163) tail @ MR(0.209, 0.061)
    draw_heng(d, ('C', 0.049, 0.163), ('MR', 0.209, 0.061), width=8)

    # s3: 长撇 (long descending pie of 疒 — from top-right to bottom-left)
    #   head @ ML(0.873, 0.104) tail @ BL(0.331, 0.982)
    draw_pie(d, ('ML', 0.873, 0.104), ('BL', 0.331, 0.982),
             head_width=11, tail_width=2, curve=0.05, segments=56)

    # s4: 点 (interior dot of 疒, upper)
    #   head @ ML(0.396, 0.342) tail @ ML(0.627, 0.588)
    draw_dian(d, ('ML', 0.396, 0.342), ('ML', 0.627, 0.588),
              head_width=2, peak_width=9, curve=0.08, segments=20)

    # s5: 提 (interior rising stroke of 疒)
    #   head @ BL(0.223, 0.159) tail @ ML(0.773, 0.884)
    draw_ti(d, ('BL', 0.223, 0.159), ('ML', 0.773, 0.884),
            head_width=9, tail_width=2, curve=0.03, segments=28)

    # ----- 尤 (strokes 6-9) — interior right-side -----
    # s6: 短横 (small horizontal of 尤)
    #   head @ C(0.084, 0.846) tail @ MR(0.133, 0.723)
    draw_heng(d, ('C', 0.084, 0.846), ('MR', 0.133, 0.723), width=7)

    # s7: 撇 of 尤 — welds with s6 (P — cross) and near s8-head (N)
    #   head @ C(0.479, 0.389) tail @ BL(0.759, 0.865)
    draw_pie(d, ('C', 0.479, 0.389), ('BL', 0.759, 0.865),
             head_width=10, tail_width=2, curve=0.08, segments=48)

    # s8: 竖弯钩 of 尤. MMH endpoints are head=BC(0.69, 0.013)=(169,201) and
    # tail=BR(0.59, 0.379)=(259,237). These read as start-of-vertical and
    # hook-tip in MMH's terse median. Expand corner deeper for GT-matching
    # prominence (visual A-recipe adjustment — interior control points are
    # not MMH-specified, only head/tail).
    head_a = ('BC', 0.69, 0.013)         # start of vertical
    belly_a = ('BC', 0.72, 0.35)         # vertical body
    corner_a = ('BC', 0.82, 0.72)        # deep bend for prominent hook
    hook_pt_a = ('BR', 0.55, 0.72)       # end of horizontal sweep
    tip_a = ('BR', 0.59, 0.379)          # hook tip = MMH tail (upward flick)
    draw_shu_wan_gou(d, head_a, belly_a, corner_a, hook_pt_a, tip_a,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)

    # s9: 点 (top-right dot of 尤)
    #   head @ MR(0.048, 0.277) tail @ MR(0.323, 0.456)
    draw_dian(d, ('MR', 0.048, 0.277), ('MR', 0.323, 0.456),
              head_width=2, peak_width=10, curve=0.10, segments=20)

    # ----- s1: top 点 of 疒 (drawn LAST per errata 疡 rule) -----
    #   head @ TC(0.377, 0.574) tail @ TC(0.664, 0.809)
    draw_dian(d, ('TC', 0.377, 0.574), ('TC', 0.664, 0.809),
              head_width=2, peak_width=10, curve=0.06, segments=20)

    out = os.path.join(os.path.dirname(__file__), '01_疣.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
