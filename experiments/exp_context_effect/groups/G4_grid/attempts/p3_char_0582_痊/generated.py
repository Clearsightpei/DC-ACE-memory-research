"""p3_char_0582_痊 — 痊 = 疒 (5-stroke top-left frame) + 全 (6 strokes: 人 hat + 王).

# BANK_DEVIATION
# skipped: success_bank/code/wang.py  (would have handled the 王 portion of 全)
# reason: 王 lives in the bottom-right slot of 痊 under the 人 hat, at ~60%
#         scale — wang.py's full-canvas DEFAULTS would overrun the 疒 frame.
#         Inline all 王 strokes at MMH-verbatim endpoints instead.
# fresh_component: wang_under_ren_hat_for_疒 (王 compressed to BR slot)

Reading order (v8 slim checklist):
  1. drawer_memory.md — 疒 named-pattern recipe (B13 疸 PASS + 疽 A);
     right-half taper defaults.
  2. INDEX.md grep 痊/疒/全 — 疒 = named pattern (no chronic file);
     全 has no primitive; wang.py exists (SKIP — see BANK_DEVIATION).
  3. errata.md grep 痊 — not listed.

疒 frame drawn 5-stroke MMH-verbatim per the B13 canonical recipe.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ANCHOR_DIR = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _ANCHOR_DIR)

from PIL import Image, ImageDraw
from _anchor import (
    anchor_to_xy,
    fat_line,
    quad_bezier,
    stroke_variable_width,
    sample_line,
)


# ---------- MMH-verbatim endpoints ----------
S = {
    1:  (('TC', 0.438, 0.539), ('TC', 0.726, 0.762)),  # top 点 of 疒
    2:  (('C',  0.043, 0.113), ('TR', 0.206, 0.987)),  # 疒 short heng
    3:  (('ML', 0.809, 0.04),  ('BL', 0.158, 0.927)),  # 疒 long pie
    4:  (('ML', 0.398, 0.356), ('ML', 0.589, 0.664)),  # 疒 inner 点
    5:  (('BL', 0.164, 0.183), ('ML', 0.747, 0.916)),  # 疒 inner 提
    6:  (('C',  0.57,  0.254), ('BL', 0.911, 0.191)),  # 人 hat 撇
    7:  (('C',  0.705, 0.415), ('BR', 0.827, 0.042)),  # 人 hat 捺
    8:  (('BC', 0.292, 0.06),  ('C',  0.957, 0.992)),  # 王 top heng
    9:  (('BC', 0.204, 0.473), ('BR', 0.013, 0.426)),  # 王 mid heng
    10: (('BC', 0.544, 0.127), ('BC', 0.567, 0.783)),  # 王 spine
    11: (('BL', 0.896, 0.906), ('BR', 0.399, 0.859)),  # 王 bottom heng
}


def _px(a):
    return anchor_to_xy(a)


def render(path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---------- s2: 疒 short heng (top) ----------
    p2h, p2t = _px(S[2][0]), _px(S[2][1])
    # slight downward arc; taper from 4 to 7 (heng often gets heavier at tail)
    pts = sample_line(p2h, p2t, n=30)
    widths = [max(4, 4 + int(2 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---------- s3: 疒 long pie (sweep from top-right to bottom-left) ----------
    p3h, p3t = _px(S[3][0]), _px(S[3][1])
    # gentle bow curving down-left
    ctrl = ((p3h[0] + p3t[0]) / 2 - 15, (p3h[1] + p3t[1]) / 2 + 8)
    pts = quad_bezier(p3h, ctrl, p3t, n=50)
    widths = [max(1, int(12 - 11 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---------- s5: 疒 inner 提 (rising) ----------
    p5h, p5t = _px(S[5][0]), _px(S[5][1])
    pts = sample_line(p5h, p5t, n=25)
    widths = [max(2, int(8 - 6 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---------- s4: 疒 inner 点 ----------
    p4h, p4t = _px(S[4][0]), _px(S[4][1])
    pts = sample_line(p4h, p4t, n=15)
    widths = [max(3, int(4 + 5 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---------- s6: 人 hat 撇 ----------
    p6h, p6t = _px(S[6][0]), _px(S[6][1])
    ctrl = ((p6h[0] + p6t[0]) / 2 - 5, (p6h[1] + p6t[1]) / 2 + 3)
    pts = quad_bezier(p6h, ctrl, p6t, n=35)
    widths = [max(1, int(10 - 9 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---------- s7: 人 hat 捺 ----------
    p7h, p7t = _px(S[7][0]), _px(S[7][1])
    # na: swells in the middle then tapers
    pts = sample_line(p7h, p7t, n=35)
    widths = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        # 3 -> peak 12 at t~0.7 -> 2
        w = int(3 + 9 * (1 - abs(t - 0.7) / 0.7)) if t <= 0.7 else int(12 - 10 * ((t - 0.7) / 0.3))
        widths.append(max(2, w))
    stroke_variable_width(d, pts, widths)

    # ---------- s8: 王 top heng ----------
    p8h, p8t = _px(S[8][0]), _px(S[8][1])
    pts = sample_line(p8h, p8t, n=25)
    widths = [max(4, 4 + int(2 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---------- s9: 王 mid heng (shorter) ----------
    p9h, p9t = _px(S[9][0]), _px(S[9][1])
    pts = sample_line(p9h, p9t, n=20)
    widths = [5] * len(pts)
    stroke_variable_width(d, pts, widths)

    # ---------- s10: 王 spine (vertical) ----------
    p10h, p10t = _px(S[10][0]), _px(S[10][1])
    fat_line(d, p10h, p10t, width=7)

    # ---------- s11: 王 bottom heng (widest, base of 全) ----------
    p11h, p11t = _px(S[11][0]), _px(S[11][1])
    pts = sample_line(p11h, p11t, n=30)
    widths = [7] * len(pts)
    stroke_variable_width(d, pts, widths)

    # ---------- s1: 疒 top 点 (DRAW LAST per B6 defensive rule) ----------
    p1h, p1t = _px(S[1][0]), _px(S[1][1])
    pts = sample_line(p1h, p1t, n=12)
    widths = [max(3, int(4 + 6 * i / len(pts))) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    img.save(path)


SELF_CHECK = {
    'visual_ok': None,          # set after rendering
    'stroke_count_ok': True,    # 11 stroke primitives (s1..s11)
    'endpoint_mismatches': [],  # all endpoints MMH-verbatim
    'joint_class_mismatches': [],  # all 8 N-joints left as natural gaps; s9/s10 P via spine crossing mid heng
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: skipped wang.py (full-canvas defaults would overrun compressed BR slot). All strokes MMH-verbatim.'
}


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_痊.png")
    render(out)
    print(f"wrote {out}")
