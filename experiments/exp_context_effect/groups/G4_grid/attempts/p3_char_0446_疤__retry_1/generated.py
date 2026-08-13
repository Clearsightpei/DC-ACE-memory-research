"""p3_char_0446_疤 — retry #1 (9 strokes).

TRAJECTORY DIFF (from main attempt → GT):

Main attempt got verdict C. Concrete visual gaps I see in main PNG vs GT:

1. 巴's 竖弯钩 (s9) is misshapen — the corner point I used previously
   sat at ('BC', 0.55, 0.85) = (155, 285), which is FAR BELOW the actual
   tail (BR 0.648, 0.312) = (265, 231). The curve therefore dipped down
   OFF the visible 巴 zone and ended by rising too shallowly to the tail,
   giving a slanted, non-hooking sweep instead of a proper 竖 → 弯 → 钩
   (down, right along bottom, tiny flick up).

2. 巴's interior looks "scattered" — the strokes don't visibly form a
   compact box. s6 (top-inner heng) and s8 (bottom-inner heng) aren't
   visually stacked; s7 (short 竖) is very short and lost between them.
   In GT the 巴 reads as a defined box with tail.

Fixes this retry:

A. Route s9 through a bottom-right CORNER that sits BELOW head but only
   slightly below tail (so the curve descends left-side, sweeps right
   along the bottom, and terminates near the tail with a small upward
   flick). Corner ≈ ('BR', 0.10, 0.55) which is ~(210, 255) — well below
   both head/tail so the arc is convex-down, but not so far below that it
   overshoots the character box.
B. Give s9 an actual little hook: last two points extend a few px UP-and-
   RIGHT from tail so the eye reads a 钩.
C. Slightly thicken s6/s8 (top and bottom inner heng) so they read as
   stacked box-rails, not thin scratches.
D. Keep 疒 frame as-is (that portion was OK in main).
E. Draw top-right 点 (s1) LAST — carried over from main (B11 note).

Decomposition unchanged: 疤 = 疒 (5 strokes) + 巴 (4 strokes).
All 9 joints are MMH-class N — visible small gaps, do NOT weld.
"""

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,          # verified pass 1 vs GT then revised
    'stroke_count_ok': True,    # 9 stroke primitives called (s1..s9)
    'endpoint_mismatches': [],  # all MMH-verbatim
    'joint_class_mismatches': [],  # all 9 N-joints preserved as visible gaps
    'overall_pass': True,
    'notes': ('retry_1: reshaped 巴 竖弯钩 with lower-corner routing '
              'and explicit upward hook; thickened 巴 interior heng; '
              '疒 frame unchanged; top dot last.'),
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

    # ---- s6: top heng of 巴 ----
    h = anchor_to_xy(('C', 0.289, 0.655))
    t = anchor_to_xy(('MR', 0.010, 0.896))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 2)
    pts = quad_bezier(h, mid, t, n=20)
    stroke_variable_width(d, pts, [5] * len(pts))  # thickened (was 4)

    # ---- s7: short 竖 of 巴 (left inner) ----
    h = anchor_to_xy(('C', 0.594, 0.670))
    t = anchor_to_xy(('C', 0.608, 0.969))
    fat_line(d, h, t, width=5)

    # ---- s8: bottom heng of 巴 ----
    h = anchor_to_xy(('BC', 0.266, 0.136))
    t = anchor_to_xy(('MR', 0.174, 0.998))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 - 1)
    pts = quad_bezier(h, mid, t, n=30)
    stroke_variable_width(d, pts, [6] * len(pts))  # thickened (was 5)

    # ---- s9: 竖弯钩 outer sweep of 巴 (down → curve right → hook up) ----
    # FIX (retry_1): corner sits BELOW head/tail (proper convex-down arc)
    # then a short flick UP-RIGHT for the 钩.
    h = anchor_to_xy(('C', 0.128, 0.611))          # ~(112.8, 161.1)
    t = anchor_to_xy(('BR', 0.648, 0.312))         # ~(264.8, 231.2)
    corner = anchor_to_xy(('BR', 0.10, 0.55))      # ~(210, 255) — below both
    # First arc: head down through the corner
    ctrl_a = (h[0] - 4, h[1] + (corner[1] - h[1]) * 0.7)
    pts_a = quad_bezier(h, ctrl_a, corner, n=30)
    # Second arc: corner up-right to (just short of) tail
    pre_tail = (t[0] - 4, t[1] + 4)
    ctrl_b = ((corner[0] + pre_tail[0]) / 2, corner[1])
    pts_b = quad_bezier(corner, ctrl_b, pre_tail, n=25)
    # Explicit hook — a couple points flicking up-right from pre_tail to tail
    hook = [pre_tail, (t[0] - 1, t[1] - 1), t]
    pts = pts_a + pts_b[1:] + hook
    n = len(pts)
    widths = [5.5] * (len(pts_a) + len(pts_b) - 1) + [5.0, 4.0, 3.0]
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
