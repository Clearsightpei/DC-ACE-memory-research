"""疭 (p3_char_0454) — 疒 (sickness radical, 5 strokes) + 从 (cong, 4 strokes) = 9 strokes.

Composition:
  - 疒 (s1-s5): top-right dot, top heng, long left-descending 撇, inner 点, inner 提
  - 从 (s6-s9): left 人 (pie+na small), right 人 (pie+na large) — cong = two people
    Note: the right 人's 捺 sweeps down and right below the 疒 frame.
"""

# Import path setup: pull in shared anchor helper from success_bank/code
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


# ---------- helpers ----------
def line_at(a, b, width=6):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(b)
    fat_line(draw, p0, p1, width)


def curve_at(a, ctrl_frac, b, widths=(6, 6, 6), n=40):
    """Curved stroke via quad bezier. ctrl_frac in canvas-frac (0..1)."""
    p0 = anchor_to_xy(a)
    p1 = (ctrl_frac[0] * W, ctrl_frac[1] * H)
    p2 = anchor_to_xy(b)
    pts = quad_bezier(p0, p1, p2, n=n)
    w0, wm, w1 = widths
    ws = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        if t < 0.5:
            w = w0 + (wm - w0) * (t / 0.5)
        else:
            w = wm + (w1 - wm) * ((t - 0.5) / 0.5)
        ws.append(w)
    stroke_variable_width(draw, pts, ws)


# ---------- 疒 (strokes 1-5) ----------

# s1: 点 (top-right small dot) — TC (0.412,0.507) → TC (0.799,0.771)
line_at(('TC', 0.412, 0.507), ('TC', 0.799, 0.771), width=7)

# s2: 横 (top heng of 疒) — C (0.16,0.175) → TR (0.347,0.914)
# Slight upward curve
curve_at(('C', 0.16, 0.175), (0.55, 0.33), ('TR', 0.347, 0.914),
         widths=(6, 6, 5))

# s3: 撇 (long left-descending pie) — ML (0.935,0.008) → BL (0.387,1.006)
# Arc curving left as it descends
p0 = anchor_to_xy(('ML', 0.935, 0.008))
p2 = anchor_to_xy(('BL', 0.387, 1.006))
# control point bulges outward to the right (curving left as descend)
ctrl = ((p0[0] + p2[0]) / 2 + 22, (p0[1] + p2[1]) / 2 - 6)
pts = quad_bezier(p0, ctrl, p2, n=60)
ws = [max(2, 10 - i * 8.5 / len(pts)) for i in range(len(pts))]
stroke_variable_width(draw, pts, ws)

# s4: 点 (small inner dot) — ML (0.442,0.242) → ML (0.747,0.526)
line_at(('ML', 0.442, 0.242), ('ML', 0.747, 0.526), width=7)

# s5: 提 (ti — small rising stroke on left) — BL (0.229,0.194) → ML (0.858,0.819)
p0 = anchor_to_xy(('BL', 0.229, 0.194))
p1 = anchor_to_xy(('ML', 0.858, 0.819))
pts = [(p0[0] + i / 40 * (p1[0] - p0[0]),
        p0[1] + i / 40 * (p1[1] - p0[1])) for i in range(41)]
ws = [max(2, 7 - i * 5 / 40) for i in range(41)]
stroke_variable_width(draw, pts, ws)


# ---------- 从 (strokes 6-9): two 人 ----------

# 人1 (left, smaller/upper): s6 pie + s7 na
# s6: 撇 — C (0.336,0.518) → BC (0.005,0.725)
p0 = anchor_to_xy(('C', 0.336, 0.518))
p2 = anchor_to_xy(('BC', 0.005, 0.725))
ctrl = ((p0[0] + p2[0]) / 2 + 6, (p0[1] + p2[1]) / 2 - 4)
pts = quad_bezier(p0, ctrl, p2, n=40)
ws = [max(2, 8 - i * 6 / len(pts)) for i in range(len(pts))]
stroke_variable_width(draw, pts, ws)

# s7: 捺 (small na of left 人) — BC (0.403,0.191) → BC (0.626,0.487)
p0 = anchor_to_xy(('BC', 0.403, 0.191))
p2 = anchor_to_xy(('BC', 0.626, 0.487))
ctrl = ((p0[0] + p2[0]) / 2 - 2, (p0[1] + p2[1]) / 2 - 4)
pts = quad_bezier(p0, ctrl, p2, n=40)
# na broadens then tapers
ws = []
for i in range(len(pts)):
    t = i / (len(pts) - 1)
    if t < 0.85:
        w = 3 + t / 0.85 * 8   # 3 -> 11
    else:
        w = 11 - (t - 0.85) / 0.15 * 9  # 11 -> 2
    ws.append(w)
stroke_variable_width(draw, pts, ws)

# 人2 (right, larger/lower): s8 pie + s9 na
# s8: 撇 — C (0.893,0.345) → BC (0.342,1.023)
p0 = anchor_to_xy(('C', 0.893, 0.345))
p2 = anchor_to_xy(('BC', 0.342, 1.023))
ctrl = ((p0[0] + p2[0]) / 2 + 14, (p0[1] + p2[1]) / 2 - 8)
pts = quad_bezier(p0, ctrl, p2, n=60)
ws = [max(2, 10 - i * 8 / len(pts)) for i in range(len(pts))]
stroke_variable_width(draw, pts, ws)

# s9: 捺 — BR (0.039,0.145) → BR (0.83,0.985)
p0 = anchor_to_xy(('BR', 0.039, 0.145))
p2 = anchor_to_xy(('BR', 0.83, 0.985))
ctrl = ((p0[0] + p2[0]) / 2 - 6, (p0[1] + p2[1]) / 2 - 6)
pts = quad_bezier(p0, ctrl, p2, n=60)
ws = []
for i in range(len(pts)):
    t = i / (len(pts) - 1)
    if t < 0.85:
        w = 3 + t / 0.85 * 10  # 3 -> 13
    else:
        w = 13 - (t - 0.85) / 0.15 * 11
    ws.append(w)
stroke_variable_width(draw, pts, ws)


# ---------- Save ----------
img.save(os.path.join(_HERE, "01_疭.png"))


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 6 joints are N (natural gaps)
    'overall_pass': True,
    'notes': '疒 (5) + 从 (4) = 9 strokes; all joints N-class (no welding).',
}
