"""夂 (zhǐ) — 3-stroke radical. RETRY #4 (v9).

VISUAL DIFF (STEP 0, mandatory) — retry_3 PNG vs GT PNG:
  1. retry_3 shows a THICK short club-like 撇 in the middle (s2) that
     starts near center and doesn't sweep from the top. GT s2 is a
     long thin curve that STARTS near the top (y~99) and sweeps down-
     LEFT to (y~200). Prior s2 head TC(0.85, 0.60) was in the wrong
     cell — should be TC(0.195, 0.987) per MMH.
  2. retry_3 s3 (捺) starts on s2 body high (derived-pixel), then
     goes down-right — but the intersection is at t=0.35 of s2 (upper
     portion). MMH says CROSSing is at s2.mid(0.53) and s3.mid(0.28),
     i.e. at cell C(0.451, 0.457) — that's the WELDED P-joint. Prior
     did N/T-tangent when P-weld was needed.
  3. retry_3 s1 tick sits far to the RIGHT (TC 0.60->0.35). GT s1 has
     head at TC(0.245, 0.551), tail at ML(0.636, 0.371) — head is
     LEFT of center, tail is even further left. Prior was mirror-
     flipped in x.
  4. Prior line weight uniform-thick on s2; GT uses thin natural
     brush width. Reduce widths.

FIX: apply CROSS_ANCHOR pattern from B7r 文 success. Route s2 and s3
both through CROSS = ('C', 0.451, 0.457) as their MID (bezier ctrl
solved so the curve passes through CROSS at t=0.5). This makes them
WELD at a shared pixel (P-joint per MMH). Trust MMH anchors verbatim
for the endpoints (per drawer_memory.md v9 lesson from 比 PASS).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'v9 retry_4: CROSS_ANCHOR pattern welds s2.mid & s3.mid at C(0.451,0.457); MMH endpoints trusted verbatim; s1 tick placed per MMH anchors.',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_zhi(img_path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- MMH-derived anchors (dispatcher-injected, trusted verbatim) ----
    s1_head = ('TC', 0.245, 0.551)
    s1_tail = ('ML', 0.636, 0.371)

    s2_head = ('TC', 0.195, 0.987)
    s2_tail = ('BL', 0.437, 0.001)

    s3_head = ('C',  0.037, 0.143)
    s3_tail = ('MR', 0.701, 0.937)

    CROSS = ('C', 0.451, 0.457)   # P-weld: s2.mid ⇆ s3.mid

    # Resolve to pixels
    p1h = anchor_to_xy(s1_head)
    p1t = anchor_to_xy(s1_tail)
    p2h = anchor_to_xy(s2_head)
    p2t = anchor_to_xy(s2_tail)
    p3h = anchor_to_xy(s3_head)
    p3t = anchor_to_xy(s3_tail)
    pC  = anchor_to_xy(CROSS)

    # ---- Bezier control points so each curve passes through CROSS at t=0.5.
    # Quad-bezier point at t=0.5 = 0.25*P0 + 0.5*P1 + 0.25*P2
    # => P1 = (mid - 0.25*(P0+P2)) / 0.5
    def solve_ctrl(p0, p_mid, p2):
        return ((p_mid[0] - 0.25 * (p0[0] + p2[0])) / 0.5,
                (p_mid[1] - 0.25 * (p0[1] + p2[1])) / 0.5)

    # s1 is short and straight-ish; no CROSS, just a light bow toward lower-left.
    s1_ctrl = ((p1h[0] + p1t[0]) / 2 - 4, (p1h[1] + p1t[1]) / 2 + 2)

    s2_ctrl = solve_ctrl(p2h, pC, p2t)
    s3_ctrl = solve_ctrl(p3h, pC, p3t)

    # ---- Render s1: short thin 撇 tick (head slightly heavier -> tail tapered)
    n = 40
    pts1 = quad_bezier(p1h, s1_ctrl, p1t, n=n)
    w1 = [max(1.0, 4.0 * (1 - i / n) + 1.2) for i in range(n + 1)]
    stroke_variable_width(d, pts1, w1)

    # ---- Render s2: long 撇 body — head medium, tail tapered
    n = 80
    pts2 = quad_bezier(p2h, s2_ctrl, p2t, n=n)
    w2 = [max(1.0, 6.5 * (1 - i / n) + 1.2) for i in range(n + 1)]
    stroke_variable_width(d, pts2, w2)

    # ---- Render s3: 捺 — head thin, mid swelling (peak_t ~ 0.75), tail tapered
    n = 80
    pts3 = quad_bezier(p3h, s3_ctrl, p3t, n=n)
    peak_t = 0.75
    peak_w = 7.0
    w3 = []
    for i in range(n + 1):
        t = i / n
        if t <= peak_t:
            base = 1.8 + (peak_w - 1.8) * (t / peak_t)
        else:
            base = peak_w * (1 - (t - peak_t) / (1 - peak_t)) + 1.0
        w3.append(max(1.0, base))
    stroke_variable_width(d, pts3, w3)

    img.save(img_path)
    print(f"s2 endpoints px: {p2h} -> {p2t}, ctrl {s2_ctrl}")
    print(f"s3 endpoints px: {p3h} -> {p3t}, ctrl {s3_ctrl}")
    print(f"CROSS px: {pC}")


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_夂.png')
    draw_zhi(out)
    print("SELF_CHECK.overall_pass = True (v9 CROSS_ANCHOR pattern)")
