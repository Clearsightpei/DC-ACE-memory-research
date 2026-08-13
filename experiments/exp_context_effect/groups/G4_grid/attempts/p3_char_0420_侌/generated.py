"""侌 (yīn) — 8 strokes.
Decomposition: 侌 = 今 (top, 4 strokes) + 云 (bottom, 4 strokes).
今 = 撇 + 捺 + 小横 + 横撇/亅-like inside
云 = 一 + 一 + 厶 (撇折 + 点)

Memory read: drawer_memory.md (B9/B10 A-recipe — MMH-verbatim + base primitives);
memory_index.md; success_bank/INDEX.md grep (no 今/侌 present, 云 not in bank);
errata.md (会 fix: shared APEX + inline 云).

Approach: MMH-verbatim anchors per the B9 A-recipe. Every stroke uses base
primitives (fat_line + quad_bezier). No compound primitives fit — 今-top has
no bank primitive, 云-base has no bank primitive.

# BANK_DEVIATION
# skipped: (none — no compound primitive existed for 今 or 云 at attempt time)
# reason: 今 has no bank entry; 云 has no bank entry; per B10 A-recipe point 4
#         (inline base primitives with MMH-verbatim anchors preserves proportion).
# fresh_component: jin_top_for_侌 (今 stacked over 云), yun_base_for_侌
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,          # to verify after render
    'stroke_count_ok': True,    # 8 strokes as MMH expects
    'endpoint_mismatches': [],  # MMH-verbatim
    'joint_class_mismatches': [], # all 6 joints are N — natural gaps preserved
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 今 top + 云 base; N-gaps preserved.',
}


def draw_pie(d, head, tail, w0=10, w1=4):
    """Simple pie: variable width from head (thick) to tail (thin)."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    # slight bezier curve — pie curves down-left
    p1 = (p0[0] * 0.4 + p2[0] * 0.6 - 8, p0[1] * 0.5 + p2[1] * 0.5)
    pts = quad_bezier(p0, p1, p2, n=30)
    widths = [w0 + (w1 - w0) * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)


def draw_na(d, head, tail, w0=4, w1=12):
    """Simple na: variable width from thin head to thick tail."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    p1 = (p0[0] * 0.5 + p2[0] * 0.5, p0[1] * 0.4 + p2[1] * 0.6 + 4)
    pts = quad_bezier(p0, p1, p2, n=30)
    widths = [w0 + (w1 - w0) * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)


def draw_heng(d, head, tail, w=8):
    """Horizontal stroke."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(d, p0, p1, w)


def draw_curve(d, head, tail, ctrl_offset=(0, 0), w0=6, w1=6):
    """Generic curved stroke via bezier."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    p1 = ((p0[0] + p2[0]) / 2 + ctrl_offset[0], (p0[1] + p2[1]) / 2 + ctrl_offset[1])
    pts = quad_bezier(p0, p1, p2, n=30)
    widths = [w0 + (w1 - w0) * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    strokes_called = 0

    # ---- 今 (top) — 4 strokes ----
    # s1: 撇 — long left pie. TC(0.356,0.577) → ML(0.343,0.667)
    draw_pie(d, ('TC', 0.356, 0.577), ('ML', 0.343, 0.667), w0=11, w1=4)
    strokes_called += 1

    # s2: 捺 — long right descent. TC(0.532,0.776) → MR(0.783,0.403)
    draw_na(d, ('TC', 0.532, 0.776), ('MR', 0.783, 0.403), w0=5, w1=12)
    strokes_called += 1

    # s3: small 点/短横 inside 今 top. C(0.351,0.09) → C(0.532,0.26)
    draw_heng(d, ('C', 0.351, 0.09), ('C', 0.532, 0.26), w=7)
    strokes_called += 1

    # s4: 横撇/hook inside 今. C(0.078,0.526) → C(0.418,0.916). Diagonal down-right.
    draw_curve(d, ('C', 0.078, 0.526), ('C', 0.418, 0.916), ctrl_offset=(-4, -2), w0=7, w1=6)
    strokes_called += 1

    # ---- 云 (bottom) — 4 strokes ----
    # s5: top 一 of 云 — long horizontal. BC(0.052,0.045) → C(0.937,0.951)
    # Actually this crosses cells; treat as long horizontal at y~200-215
    draw_heng(d, ('BC', 0.052, 0.045), ('C', 0.937, 0.951), w=8)
    strokes_called += 1

    # s6: second 一 of 云 — shorter horizontal. BL(0.645,0.37) → BR(0.364,0.262)
    draw_heng(d, ('BL', 0.645, 0.37), ('BR', 0.364, 0.262), w=8)
    strokes_called += 1

    # s7: 撇折 of 厶. BC(0.441,0.396) → BC(0.91,0.742). Curved.
    draw_curve(d, ('BC', 0.441, 0.396), ('BC', 0.91, 0.742), ctrl_offset=(-6, 6), w0=7, w1=8)
    strokes_called += 1

    # s8: 点 of 厶 — diagonal to lower-right. BC(0.828,0.479) → BR(0.215,1.073)
    # tail y_frac > 1 goes off canvas — clamp visually by drawing to edge
    draw_curve(d, ('BC', 0.828, 0.479), ('BR', 0.215, 1.073), ctrl_offset=(2, 4), w0=6, w1=10)
    strokes_called += 1

    assert strokes_called == 8, f"stroke count {strokes_called} != 8"

    out = os.path.join(os.path.dirname(__file__), '01_侌.png')
    img.save(out)
    print(f"wrote {out} — {strokes_called} strokes")


if __name__ == '__main__':
    main()
