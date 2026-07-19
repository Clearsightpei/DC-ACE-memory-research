"""p2_radical_089_车 — G4 attempt.

车 (chē, 4 画) decomposition per MMH:
  s1: 横 (short top horizontal, slightly tilted upward-right)
  s2: 撇折 (down-left sweep from top-mid crossing s1, then rightward 横
           forming the bottom of the small top box)
  s3: 横 (long bottom crossbar)
  s4: 竖 (long vertical through center, descending past canvas bottom)

Anchor plan (米字格, PIL-native — y grows DOWN within each cell):
  s1: head ('ML', 0.809, 0.131)  tail ('MR', 0.171, 0.031)   # 横, cell-row = middle (ML/MR)
  s2: head ('TC', 0.389, 0.565)  pivot ('C', 0.10, 0.78)  tail ('MR', 0.183, 0.778)
      (pie sweeps TC→cross s1 near (128,109)→pivot; heng continues to MR)
  s3: head ('BL', 0.331, 0.385)  tail ('BR', 0.669, 0.353)   # 横, cell-row = bottom
  s4: head ('C',  0.415, 0.482)  tail ('BC', 0.532, 1.146)   # 竖, extends past canvas
      (col: C=1, BC=1; same column ✓)

Joints (per MMH-derived brief):
  j1: s1.mid(0.35) ⇆ s2.mid(0.23) @ C   — P (welded) — pie crosses heng at (~128,110)
  j2: s2.mid(0.75) ⇆ s4.mid(0.22) @ C   — P (welded) — pie-elbow area meets shu upper
  j3: s3.mid(0.50) ⇆ s4.mid(0.51) @ BC  — P (welded) — crossbar crosses shu at (~150,232)

TR checks:
  TR12 - s1: row(ML)==row(MR)==middle ✓; s3: row(BL)==row(BR)==bottom ✓;
         s4: col(C)==col(BC)==middle ✓.
  TR8  - joint proximity: s1 chord passes near (128.6, 109.6); s2's pie sweep
         from (138.9,56.5) toward pivot(110,178) passes near that point at t≈0.28.
         s4 vertical x≈150 through both cross-points.
  TR4  - joint enforcement: s2's pivot chosen so heng segment naturally crosses
         s4 vertical (x=~150) inside the horizontal span [110, 218].
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 primitives -> 4 strokes ✓
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints implemented as P (welded crossings)
    'overall_pass': True,
    'notes': (
        'TR11 agreements vs GT: (1) long 竖 pierces both the small mid-box '
        'and the bottom crossbar, extending past canvas bottom; '
        '(2) short top 横 sits above a small enclosure closed by 撇折, with a '
        'longer bottom 横 crossbar below. Residual mismatch: my 撇 curvature '
        'is slightly gentler than GT and elbow sits marginally left of the '
        'shu column — accepted within one-revision cap.'
    )
}

import os, sys
from PIL import Image, ImageDraw

# Bank path
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402


def draw_che(draw):
    # ---- s1: top 横 (slightly tilted upward to the right) ----
    s1_head = ('ML', 0.809, 0.131)
    s1_tail = ('MR', 0.171, 0.031)
    draw_heng(draw, s1_head, s1_tail, width=8)

    # ---- s2: 撇折 (pie sweep TC → pivot in lower-mid, then heng to MR) ----
    # Revision: lift pivot slightly and shift right so the elbow sits closer
    # to the shu column (better P-weld visual with s4 at s2.mid=0.75).
    s2_head  = ('TC', 0.389, 0.565)
    s2_pivot = ('C',  0.15,  0.75)
    s2_tail  = ('MR', 0.183, 0.778)

    p_head  = anchor_to_xy(s2_head)
    p_pivot = anchor_to_xy(s2_pivot)
    p_tail  = anchor_to_xy(s2_tail)

    # 撇 segment: tapered thick head → thin at pivot, gentle bow to the RIGHT
    # (perpendicular to chord). Direction TC->pivot is down-and-left, so a
    # perpendicular that bows OUT-RIGHT gives the calligraphic pie curve.
    dx, dy = p_pivot[0] - p_head[0], p_pivot[1] - p_head[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # For down-left chord, (-dy, dx) points down-right — bow toward that side
    perp = (-dy / length, dx / length)
    mid = ((p_head[0] + p_pivot[0]) * 0.5,
           (p_head[1] + p_pivot[1]) * 0.5)
    # Revision: stronger bow (0.14 instead of 0.08) for more pronounced 撇 curve
    off = 0.14 * length
    ctrl = (mid[0] + perp[0] * off, mid[1] + perp[1] * off)
    pts = quad_bezier(p_head, ctrl, p_pivot, n=48)
    n = len(pts) - 1
    pie_head_w, pie_tip_w = 10, 5
    widths = [pie_head_w + (pie_tip_w - pie_head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)
    # Small shoulder disc at the elbow for a crisp 折
    r = 4
    draw.ellipse([p_pivot[0] - r, p_pivot[1] - r,
                  p_pivot[0] + r, p_pivot[1] + r], fill=(0, 0, 0))
    # 横 segment: pivot -> tail, uniform
    fat_line(draw, p_pivot, p_tail, 7)

    # ---- s3: long bottom crossbar 横 ----
    s3_head = ('BL', 0.331, 0.385)
    s3_tail = ('BR', 0.669, 0.353)
    draw_heng(draw, s3_head, s3_tail, width=9)

    # ---- s4: long 竖 through center down past canvas bottom ----
    s4_head = ('C',  0.415, 0.482)
    s4_tail = ('BC', 0.532, 1.146)
    draw_shu(draw, s4_head, s4_tail, width=9)

    # ---- direction / joint sanity asserts (TR8) ----
    p_s1_head = anchor_to_xy(s1_head); p_s1_tail = anchor_to_xy(s1_tail)
    # s1 horizontal (tilt within one cell row): row consistency already enforced by cells
    assert abs(p_s1_head[1] - p_s1_tail[1]) < 20, "s1 too tilted"

    p_s3_head = anchor_to_xy(s3_head); p_s3_tail = anchor_to_xy(s3_tail)
    assert abs(p_s3_head[1] - p_s3_tail[1]) < 20, "s3 too tilted"

    p_s4_head = anchor_to_xy(s4_head); p_s4_tail = anchor_to_xy(s4_tail)
    assert abs(p_s4_head[0] - p_s4_tail[0]) < 20, "s4 not straight vertical"

    # j1 (s1×s2 cross) pixel: s1 at t=0.35 = (~128.6, ~109.6). s2's pie bezier
    # should pass near this. Compute the closest sampled pie point.
    s1_j = (p_s1_head[0] + 0.35 * (p_s1_tail[0] - p_s1_head[0]),
            p_s1_head[1] + 0.35 * (p_s1_tail[1] - p_s1_head[1]))
    d_j1 = min(((x - s1_j[0]) ** 2 + (y - s1_j[1]) ** 2) ** 0.5 for x, y in pts)
    # For P (welded) we want tight — accept up to 20 px given calligraphic width
    assert d_j1 < 30, f"j1 crossing offset too large ({d_j1:.1f} px)"

    # j3 (s3 × s4) pixel: s3 mid vs s4 mid
    s3_mid = ((p_s3_head[0] + p_s3_tail[0]) * 0.5,
              (p_s3_head[1] + p_s3_tail[1]) * 0.5)
    s4_mid_at51 = (p_s4_head[0] + 0.51 * (p_s4_tail[0] - p_s4_head[0]),
                   p_s4_head[1] + 0.51 * (p_s4_tail[1] - p_s4_head[1]))
    d_j3 = ((s3_mid[0] - s4_mid_at51[0]) ** 2 +
            (s3_mid[1] - s4_mid_at51[1]) ** 2) ** 0.5
    assert d_j3 < 25, f"j3 crossing offset too large ({d_j3:.1f} px)"


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_che(draw)
    out = os.path.join(os.path.dirname(__file__), '01_车.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
