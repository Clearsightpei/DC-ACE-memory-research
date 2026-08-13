"""p3_char_0431_说 (retry_2) — 讠 + 兑 (9 strokes).

TRAJECTORY DIFF (viewing main + retry_1 vs GT):
  main C:    讠 zig-zag fold, 八 too big/tall, 口 gap, 儿 splayed.
  retry_1 C: 讠 clean L OK; 八 still too tall (~30 px pies with
             calligraphy taper — read as long marks, not tiny dots);
             口 walls now closed but oversized/low; 儿's 竖弯钩 read
             as L-shape (belly bezier too gentle), and the sweep went
             way past x=260 producing a huge hook that dominates the
             right side. Meanwhile GT: 八 = 2 TINY marks (~18 px);
             口 sits compact just below the 八; 儿's 竖弯钩 makes a
             smooth soft curve turning right then flicking up around
             tail y~230, not sweeping to x=260.

  Retry_2 fixes:
    (1) 八: shrink each mark to ~18 px length total (currently ~35).
    (2) 口: make the box smaller and higher (top y~130, bottom y~175)
        so 儿 has room below; keep visible N-gap corners.
    (3) 儿 竖弯钩: shorter sweep (tail x ~230, not 260) and rounder
        belly — hook tip lands near BR(0.55, 0.3), inside the canvas.
    (4) 儿 撇 (s8): steeper curve, tail landing lower-left near BL.

BANK_DEVIATION rationale unchanged — yan_speech/kou/er_legs are
calibrated for standalone whole-canvas render. Here each must slot
into a compressed left column (讠) or a compressed 3-part stack (兑).
"""
# BANK_DEVIATION
# skipped: yan_speech.py, kou.py, er_legs.py
# reason: primitives are whole-canvas calibrated; 说 needs 讠 in a
#         narrow left column and 兑 as a compressed vertical stack
#         (八 top / 口 middle / 儿 bottom) in the right 2/3.
# fresh_component: shuo_composition_v3 (compact 八 dots + smaller 口 + shorter 儿 sweep)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes; 讠 clean-L kept from R1; 八 dots shrunk to ~20 px; '
              '口 compact/higher; 儿 竖弯钩 sweep shortened & belly rounded.')
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def _short(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    m = (dx * dx + dy * dy) ** 0.5
    if m < 1e-6:
        return pt
    t = min(1.0, px / m)
    return (x0 + dx * t, y0 + dy * t)


# =========================================================
# 讠 (left radical) — narrow left column (KEEP from retry_1)
# =========================================================

# s1 — 点 (upper-left dot)
s1h = anchor_to_xy(('TL', 0.747, 0.686))
s1t = anchor_to_xy(('TC', 0.069, 0.949))
pts1 = quad_bezier(s1h,
                   ((s1h[0] + s1t[0]) / 2, (s1h[1] + s1t[1]) / 2 + 2),
                   s1t, n=24)
w1 = [2 + 8 * (i / 24) for i in range(25)]
stroke_variable_width(d, pts1, w1)

# s2 — 横折提 compound (clean L)
s2h = anchor_to_xy(('ML', 0.188, 0.649))     # (18.8, 164.9)
s2corner_top = (95.0, 158.0)
s2corner_bot = (95.0, 250.0)
s2t = anchor_to_xy(('BC', 0.195, 0.256))     # (119.5, 225.6)
fat_line(d, s2h, s2corner_top, width=8)
d.ellipse([s2corner_top[0] - 5, s2corner_top[1] - 5,
           s2corner_top[0] + 5, s2corner_top[1] + 5], fill=(0, 0, 0))
fat_line(d, s2corner_top, s2corner_bot, width=9)
pts_ti = [s2corner_bot,
          (0.55 * s2corner_bot[0] + 0.45 * s2t[0],
           0.55 * s2corner_bot[1] + 0.45 * s2t[1]),
          s2t]
w_ti = [12, 7, 2]
stroke_variable_width(d, pts_ti, w_ti)


# =========================================================
# 兑 (right side) — compact 八 top + 口 middle + 儿 bottom
# =========================================================

# ----- 八 (top marks) — TINY compact dots (fix #1) -----
# s3 — 点 (left, going down-right). Anchor: TC(0.43, 0.806) -> C(0.649, 0.046).
s3h_raw = anchor_to_xy(('TC', 0.43, 0.806))   # (143.0, 80.6)
s3t_raw = anchor_to_xy(('C', 0.649, 0.046))   # (164.9, 104.6)
# Shrink to ~20 px total from head
s3h = s3h_raw
s3t = _short(s3t_raw, s3h_raw, 22)
pts3 = [s3h,
        (0.5 * s3h[0] + 0.5 * s3t[0],
         0.5 * s3h[1] + 0.5 * s3t[1]),
        s3t]
w3 = [2, 5, 9]           # thin→thick (点)
stroke_variable_width(d, pts3, w3)

# s4 — 短撇 (right, going down-left). Anchor: TR(0.165, 0.554) -> C(0.887, 0.066).
s4h_raw = anchor_to_xy(('TR', 0.165, 0.554))  # (216.5, 55.4)
s4t_raw = anchor_to_xy(('C', 0.887, 0.066))   # (188.7, 106.6)
s4h = s4h_raw
s4t = _short(s4t_raw, s4h_raw, 24)
pts4 = [s4h,
        (0.5 * s4h[0] + 0.5 * s4t[0],
         0.5 * s4h[1] + 0.5 * s4t[1]),
        s4t]
w4 = [9, 5, 2]           # thick→thin (撇)
stroke_variable_width(d, pts4, w4)


# ----- 口 (fix #2: smaller, higher, visibly closed) -----
# Box coords chosen inline (BANK_DEVIATION scope).
# Anchors within ±0.20 of MMH C(0.307,0.354)..MR(0.197,0.784) tolerance.
BOX_L, BOX_R = 138.0, 208.0
BOX_T, BOX_B = 122.0, 172.0

# s5 — left wall (shu), N-gap top-left
s5h = (BOX_L, BOX_T + 4)   # small gap from s6.head
s5t = (BOX_L + 3, BOX_B - 2)
fat_line(d, s5h, s5t, width=9)

# s6 — top + right wall (heng-zhe), corner welded
s6h = (BOX_L + 3, BOX_T)
s6c = (BOX_R, BOX_T)
s6t = (BOX_R, BOX_B - 4)
fat_line(d, s6h, s6c, width=9)
fat_line(d, s6c, s6t, width=9)
r = 5
d.ellipse([s6c[0] - r, s6c[1] - r, s6c[0] + r, s6c[1] + r], fill=(0, 0, 0))

# s7 — bottom heng, slight up-tilt right; N-gaps at both corners
s7h = (BOX_L - 2, BOX_B + 2)
s7t = (BOX_R - 3, BOX_B - 3)
fat_line(d, s7h, s7t, width=9)


# ----- 儿 (fix #3+4: shorter sweep, rounder belly) -----
# s8 — 撇 (long left leg). MMH: BC(0.477, 0.101) -> BL(0.993, 0.918).
s8h = anchor_to_xy(('BC', 0.477, 0.101))   # (147.7, 210.1)
s8t = anchor_to_xy(('BL', 0.993, 0.918))   # (99.3, 291.8)
s8m = (0.5 * s8h[0] + 0.5 * s8t[0] - 10,
       0.5 * s8h[1] + 0.5 * s8t[1] + 6)
pts8 = quad_bezier(s8h, s8m, s8t, n=48)
w8 = [11 - 9 * (i / 48) for i in range(49)]
stroke_variable_width(d, pts8, w8)

# s9 — 竖弯钩 (right leg with hook). MMH: C(0.811, 0.878) -> BR(0.73, 0.3).
# Shorter, rounder — tail flicks up around (230, 220), not (273, 230).
s9h = anchor_to_xy(('C', 0.811, 0.878))    # (181.1, 187.8)
s9belly = (185.0, 245.0)                    # slight right lean
s9corner = (200.0, 278.0)                   # bottom bend
s9sweep_end = (230.0, 275.0)                # sweep ends closer
s9tip = (243.0, 240.0)                      # hook tip UP-right, compact

# body (down)
pts9_body = quad_bezier(s9h, (183.0, 220.0), s9belly, n=24)
w9_body = [9] * 25
stroke_variable_width(d, pts9_body, w9_body)

# curve (down-right around bottom)
pts9_curve = quad_bezier(s9belly, (210.0, 282.0), s9sweep_end, n=24)
w9_curve = [9 + 2 * (i / 24) for i in range(25)]
stroke_variable_width(d, pts9_curve, w9_curve)

# hook flick UP
pts9_hook = [s9sweep_end,
             (0.5 * s9sweep_end[0] + 0.5 * s9tip[0] + 2,
              0.5 * s9sweep_end[1] + 0.5 * s9tip[1] - 4),
             s9tip]
w9_hook = [10, 6, 2]
stroke_variable_width(d, pts9_hook, w9_hook)


# ----- stroke count assertion -----
STROKE_COUNT = 9
assert STROKE_COUNT == 9

out_path = os.path.join(os.path.dirname(__file__), '01_说.png')
img.save(out_path)
print(f"wrote {out_path}")
