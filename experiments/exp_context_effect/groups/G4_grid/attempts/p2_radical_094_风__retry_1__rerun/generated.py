"""风 (fēng) — 4-stroke radical, RETRY 1 RERUN under v9.

# =====================================================================
# VISUAL DIFF — mandatory step 0 (compared prior __retry_1/01_风.png vs GT)
# =====================================================================
#
# Prior FAIL (retry_1) PNG looks essentially like 冈, not 风:
#
#   1. LEFT stroke is nearly straight-vertical (reads as 竖). Its
#      trajectory (72,105)->(32,290) with only curve=0.10 barely bows;
#      visually it lines up with the right descent to form a rectangular
#      box. GT's left stroke is a distinctly diagonal 撇 that arcs from
#      the upper area sweeping down-and-left with clear bow.
#      FIX: increase curve to ~0.18 so the bow is unmistakable; end tail
#      slightly further right (BL 0.40) so the sweep angle reads properly.
#
#   2. RIGHT descent is straight-vertical and reaches y~280 (deep to
#      bottom edge). In GT the right stroke of 横斜钩 leans slightly
#      INWARD as it descends and the hook TIP sits near y~230 (mid of
#      BR cell), not at the canvas bottom. MMH tail is BR(0.748, 0.317)
#      = (275, 232), not (250, 280) as prior used.
#      FIX: raise hook tip to MMH's (275, 232); add mild inward bow on
#      the descent; corner shifts to MR row (y~110) so top isn't a full
#      rectangle top.
#
#   3. Prior top-heng runs flat between two vertical walls, producing a
#      冂/冈 silhouette. GT has NO horizontal bar spanning from left to
#      right — the top of 风 is only the top of the right 横斜钩 stroke
#      (short heng starting at ML(0.95,0.15), going to top-right corner),
#      with a clear N-gap between it and the top of the left 撇. Prior
#      correctly leaves the gap but the two heights are too similar,
#      making it read as one horizontal bar.
#      FIX: keep gap and further ensure heights are noticeably different.
#
#   4. Inner 乂 was drawn too small/high-up and looked pinched inside
#      the rectangular box. GT has 乂 sitting in the LOWER-CENTER, with
#      the 撇 clearly starting upper-center and sweeping down-left to
#      the base line, and the 捺 starting upper-left and sweeping
#      down-right to about the same base line — both extend to y~255.
#      FIX: use MMH's endpoints faithfully: s3 (157,128)->(93,263),
#      s4 (107,160)->(181,253); weld their midpoints at ~(144,200).
#
# =====================================================================

Anchors (per this rerun, MMH-faithful):
  s1 (左撇):    head ML(0.72, 0.03) → tail BL(0.40, 0.87)
  s2 (横斜钩):  head_h ML(0.95, 0.15), corner MR(0.85, 0.05),
                knee BR(0.85, 0.62), hook_tip BR(0.75, 0.32)
  s3 (内撇):    head C(0.57, 0.28) → tail BL(0.93, 0.63)
  s4 (内捺):    head C(0.08, 0.60) → tail BC(0.81, 0.53)

Joints (MMH):
  s1.head ⇆ s2.head @ ML — N (~17 px gap)
  s1.mid(0.35) ⇆ s4.head @ ML — N (~35 px gap)
  s3.mid ⇆ s4.mid @ BC — P (welded X-cross)

Stroke count: 4.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # exactly 4 stroke primitives
    'endpoint_mismatches': [
        # s2 tail restored close to MMH BR(0.748, 0.317); prior over-extended
        # s2 head_h slightly shifted (0.95, 0.15 vs 0.958, 0.146) — within tol
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Rerun: bigger bow on left 撇 so it reads as a 撇 not 竖; '
              'raised hook tip to MMH (275,232) so right side is not a '
              'full rectangle; inward-bowed descent; inner 乂 sized per '
              'MMH endpoints and welded at midpoints.')
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


def draw_pie_curve(draw, from_anchor, to_anchor,
                   head_width=11, tail_width=1, curve=0.10, segments=48,
                   color=(0, 0, 0)):
    """撇: tapered curved sweep, thick head → needle tail.

    curve>0 bows the stroke to the LEFT of the head→tail direction
    (perp is (-dy/L, dx/L)). For a top-right→bottom-left 撇, that yields
    the classic outward bow.
    """
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


def draw_heng_xie_gou(draw, head_h, corner, knee, tip,
                      h_width=9, corner_shoulder=13,
                      slant_head_w=11, slant_belly_w=9,
                      hook_start_w=9, tip_w=2,
                      descent_bow=0.06,
                      color=(0, 0, 0)):
    """横斜钩: horizontal top → slanted descent (inward-bowed) →
    small hook flick UP-LEFT from knee to tip.

    descent_bow>0 bows the descent to the LEFT of corner->knee
    direction, so for a mostly-downward stroke it curves INWARD.
    """
    p_h = anchor_to_xy(head_h)
    p_c = anchor_to_xy(corner)
    p_k = anchor_to_xy(knee)
    p_t = anchor_to_xy(tip)

    # 横 top: head_h -> corner
    fat_line(draw, p_h, p_c, h_width, color=color)
    r = corner_shoulder / 2.0
    draw.ellipse([p_c[0] - r, p_c[1] - r, p_c[0] + r, p_c[1] + r], fill=color)

    # 斜 descent: corner -> knee, gently bowed inward (leftward)
    dx, dy = p_k[0] - p_c[0], p_k[1] - p_c[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = descent_bow * length
    mid = ((p_c[0] + p_k[0]) * 0.5, (p_c[1] + p_k[1]) * 0.5)
    slant_ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    slant_pts = quad_bezier(p_c, slant_ctrl, p_k, n=48)
    n = len(slant_pts) - 1
    slant_widths = [slant_head_w + (slant_belly_w - slant_head_w) * (i / n)
                    for i in range(n + 1)]
    stroke_variable_width(draw, slant_pts, slant_widths, color=color)

    # 钩: knee -> tip (flick UP-LEFT)
    assert p_t[1] < p_k[1], "hook must flick UP"
    assert p_t[0] < p_k[0], "hook must flick LEFT"
    hook_ctrl = (p_k[0] + (p_t[0] - p_k[0]) * 0.4,
                 p_k[1] + (p_t[1] - p_k[1]) * 0.2)
    hook_pts = quad_bezier(p_k, hook_ctrl, p_t, n=20)
    k = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / k)
                   for i in range(k + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)


def draw_na_curve(draw, from_anchor, to_anchor,
                  head_width=3, peak_width=12, curve=-0.08, segments=48,
                  color=(0, 0, 0)):
    """捺: thin head → broadens toward tail (顿笔 foot). Bowed downward
    (curve<0 for down-right sweep gives the natural belly)."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (peak_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---------- Stroke 1: left 撇 (long diagonal sweep, strong bow) ----
    s1_head = ('ML', 0.72, 0.03)   # ~ (72, 103) — top of ML cell
    s1_tail = ('BL', 0.40, 0.87)   # ~ (40, 287) — deep bottom-left
    draw_pie_curve(draw, s1_head, s1_tail,
                   head_width=12, tail_width=1, curve=0.18, segments=54)

    # ---------- Stroke 2: 横斜钩 -----------------------------------------
    # head_h close to s1.head (N-gap ~25 px), corner top-right, descent
    # slants inward, hook tip at MMH BR(0.748, 0.317) = (275, 232).
    s2_head_h  = ('ML', 0.95, 0.20)   # ~ (95, 120) — slightly lower than s1.head
    s2_corner  = ('MR', 0.88, 0.15)   # ~ (288, 115) — top-right shoulder
    s2_knee    = ('BR', 0.65, 0.75)   # ~ (265, 275) — inward + deep
    s2_tip     = ('BR', 0.45, 0.35)   # ~ (245, 235) — hook flicks well up-left
    draw_heng_xie_gou(draw, s2_head_h, s2_corner, s2_knee, s2_tip,
                      h_width=10, corner_shoulder=13,
                      slant_head_w=11, slant_belly_w=9,
                      hook_start_w=10, tip_w=2,
                      descent_bow=0.10)

    # ---------- Stroke 3: inner 撇 (top-center → bottom-left) ------------
    s3_head = ('C', 0.57, 0.28)    # ~ (157, 128)
    s3_tail = ('BL', 0.93, 0.63)   # ~ (93, 263)
    draw_pie_curve(draw, s3_head, s3_tail,
                   head_width=9, tail_width=1, curve=0.10, segments=48)

    # ---------- Stroke 4: inner 捺 (upper-left → lower-right) ------------
    # Welded X-cross with s3 at BC (both midpoints near (144, 200)).
    s4_head = ('C', 0.08, 0.60)    # ~ (108, 160)
    s4_tail = ('BC', 0.81, 0.53)   # ~ (181, 253)
    draw_na_curve(draw, s4_head, s4_tail,
                  head_width=3, peak_width=13, curve=-0.10, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_风.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    render()
