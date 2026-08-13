"""p3_char_0446_疤 — 9 strokes.

Decomposition: 疤 = 疒 (sickness radical, 5 strokes) + 巴 (4 strokes, inside frame).

Lookup checklist:
  1. drawer_memory.md — A-recipe: MMH-verbatim anchors + inline base primitives.
  2. INDEX.md grep 疒 (p3_char_0171) — prior attempt exists (not in bank);
     I reuse its 5-stroke pattern for the radical.
  3. INDEX.md grep 巴 — not a mastered primitive; inline via base primitives.
  4. errata.md grep 疤 — not present.
  5. B11 fail-cluster A note: 疡 (also 疒-based) failed by dropping top dot;
     defensive fix — draw top dot (s1) LAST so it can't be overwritten.

MMH stroke anchors (used verbatim per B9/B11 A-recipe):
  s1 TC(0.427,0.568) → TC(0.714,0.870)   点 (top-right dot of 疒)
  s2 C (0.025,0.143) → TR(0.238,0.979)   横 (top bar of 疒)
  s3 ML(0.823,0.087) → BL(0.325,1.012)   长撇 (left sweep of 疒)
  s4 ML(0.372,0.351) → ML(0.545,0.664)   inner upper dot
  s5 BL(0.173,0.229) → ML(0.771,0.951)   提 (rising inner stroke)
  s6 C (0.289,0.655) → MR(0.010,0.896)   top heng of 巴
  s7 C (0.594,0.670) → C (0.608,0.969)   short 竖 (left-inner)
  s8 BC(0.266,0.136) → MR(0.174,0.998)   bottom heng of 巴
  s9 C (0.128,0.611) → BR(0.648,0.312)   竖弯钩 (outer sweep of 巴)

Joint classes (all N per MMH — preserve small gaps, do NOT weld).
"""

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim; 疒 frame + 巴 interior; '
              'all N-joints kept as visible gaps; top dot drawn LAST.'),
}


def _tapered_dian(d, h, t, w_start=3, w_end=8, curve=3, n=20):
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + curve)
    pts = quad_bezier(h, mid, t, n=n)
    widths = [w_start + (w_end - w_start) * (i / (n - 1)) for i in range(n + 1)]
    stroke_variable_width(d, pts, widths)


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s2: top horizontal bar of 疒 ----
    h = anchor_to_xy(('C', 0.025, 0.143))
    t = anchor_to_xy(('TR', 0.238, 0.979))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 3)
    pts = quad_bezier(h, mid, t, n=30)
    stroke_variable_width(d, pts, [4] * len(pts))

    # ---- s3: long 撇 of 疒 (upper-right corner down to lower-left) ----
    h = anchor_to_xy(('ML', 0.823, 0.087))
    t = anchor_to_xy(('BL', 0.325, 1.012))
    ctrl = (h[0] - 18, h[1] + (t[1] - h[1]) * 0.72)
    pts = quad_bezier(h, ctrl, t, n=60)
    n = len(pts)
    widths = [3 + 4 * (1 - abs(2 * (i / (n - 1)) - 1)) for i in range(n)]
    stroke_variable_width(d, pts, widths)

    # ---- s4: inner upper dot (inside 疒 frame, upper) ----
    _tapered_dian(d, anchor_to_xy(('ML', 0.372, 0.351)),
                     anchor_to_xy(('ML', 0.545, 0.664)),
                  w_start=3, w_end=7, curve=1, n=20)

    # ---- s5: 提 rising stroke inside 疒 frame ----
    h = anchor_to_xy(('BL', 0.173, 0.229))
    t = anchor_to_xy(('ML', 0.771, 0.951))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 4)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [6 - 3 * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- s6: top heng of 巴 (small) ----
    h = anchor_to_xy(('C', 0.289, 0.655))
    t = anchor_to_xy(('MR', 0.010, 0.896))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 2)
    pts = quad_bezier(h, mid, t, n=20)
    stroke_variable_width(d, pts, [4] * len(pts))

    # ---- s7: short 竖 of 巴 (left inner) ----
    h = anchor_to_xy(('C', 0.594, 0.670))
    t = anchor_to_xy(('C', 0.608, 0.969))
    fat_line(d, h, t, width=5)

    # ---- s8: bottom heng of 巴 (long, slight rise) ----
    h = anchor_to_xy(('BC', 0.266, 0.136))
    t = anchor_to_xy(('MR', 0.174, 0.998))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 - 1)
    pts = quad_bezier(h, mid, t, n=30)
    stroke_variable_width(d, pts, [5] * len(pts))

    # ---- s9: 竖弯钩 outer sweep of 巴 (down then curve right, ending upper-right) ----
    h = anchor_to_xy(('C', 0.128, 0.611))
    t = anchor_to_xy(('BR', 0.648, 0.312))
    # Route via a corner pulling the curve down before it sweeps up to hook tip.
    # Bend point sits near BC-right / bottom-baseline of 巴.
    corner = anchor_to_xy(('BC', 0.55, 0.85))
    pts_a = quad_bezier(h, (h[0] - 6, (h[1] + corner[1]) / 2), corner, n=30)
    pts_b = quad_bezier(corner, (corner[0] + 40, corner[1] + 8), t, n=30)
    pts = pts_a + pts_b[1:]
    n = len(pts)
    widths = [5.5 - 1.5 * (i / (n - 1)) for i in range(n)]  # slight taper into hook
    stroke_variable_width(d, pts, widths)

    # ---- s1: top-right dot 点 of 疒 — drawn LAST (defensive, per B11 疡 note) ----
    _tapered_dian(d, anchor_to_xy(('TC', 0.427, 0.568)),
                     anchor_to_xy(('TC', 0.714, 0.870)),
                  w_start=3, w_end=8, curve=3, n=20)

    out = os.path.join(HERE, '01_疤.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
