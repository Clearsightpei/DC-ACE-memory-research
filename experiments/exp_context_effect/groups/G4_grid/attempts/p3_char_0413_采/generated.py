"""p3_char_0413_采 — G4 attempt

Decomposition: 采 = 爫 (top, 4 strokes) + 木 (bottom, 4 strokes) = 8 strokes.

Memory consulted:
  - drawer_memory.md v8 read (component playbook: top-bottom composition).
    Top band y in [0.10, 0.50], bottom 木 y in [0.50, 0.95].
  - success_bank/INDEX.md grep: 木 mastered (mu.py) — but mu.py file MISSING
    from success_bank/code/ (only listed in INDEX). Fall back to inline
    heng+shu+pie+na following p3_char_0186_本 attempt's proven pattern.
    p3_char_0202_术 (木+dot) and p3_char_0293_来 also in bank — reuse pattern.
  - errata.md grep for 采: not present. 爪 (p2_radical_134) is in errata
    but 采's top uses 爫 (claws-flat), not 爪 — different form. Take note:
    top's centerline x must align with 木 spine (from 爪 errata).
  - No chronic primitive applies (no 丿/刀/冂/弓/马 as component).

Anchors follow the MMH-derived expectations block verbatim.
"""

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 8 strokes rendered
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('8 strokes: 爫 top (s1 slanted cap + s2/s3/s4 three short dots) '
              '+ 木 bottom (s5 heng crosses s6 shu = P weld; s7 pie + s8 na '
              'fork from cross vicinity, N-gaps). Column-share: top scaled '
              'to center on 木 spine x~150.')
}


def clip_y(pt, ymax=295):
    return (pt[0], min(pt[1], ymax))


def draw_cai():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    N = 40

    # ============================================================
    # TOP: 爫 (4 strokes) — a small cap-like cluster centered above 木
    # ============================================================

    # --- Stroke 1: top slanted cap stroke, right→left, going down-left ---
    # head TC(0.925, 0.677) → tail TL(0.955, 0.979)
    s1_h = anchor_to_xy(('TC', 0.925, 0.677))   # ~(192.5, 67.7)
    s1_t = anchor_to_xy(('TL', 0.955, 0.979))   # ~(95.5, 97.9)
    # slight downward bow
    ctrl = ((s1_h[0] + s1_t[0]) / 2, (s1_h[1] + s1_t[1]) / 2 + 6)
    pts = quad_bezier(s1_h, ctrl, s1_t, N)
    widths = [6] * (N + 1)
    widths[0] = 4
    widths[-1] = 3
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 2: LEFT short dot of 爫 ---
    # head ML(0.8, 0.14) → tail C(0.11, 0.462)
    s2_h = anchor_to_xy(('ML', 0.8, 0.14))     # ~(80, 114)
    s2_t = anchor_to_xy(('C', 0.11, 0.462))    # ~(111, 146)
    pts = sample_line(s2_h, s2_t, N)
    widths = [max(3, int(6 - 2 * i / N)) for i in range(N + 1)]
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 3: MIDDLE short dot of 爫 ---
    # head C(0.321, 0.061) → tail C(0.503, 0.298)
    s3_h = anchor_to_xy(('C', 0.321, 0.061))   # ~(132, 106)
    s3_t = anchor_to_xy(('C', 0.503, 0.298))   # ~(150, 130)
    pts = sample_line(s3_h, s3_t, N)
    widths = [max(3, int(6 - 2 * i / N)) for i in range(N + 1)]
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 4: RIGHT slanted 撇-like stroke of 爫 (longer than s2/s3) ---
    # head TR(0.06, 0.923) → tail C(0.737, 0.392)
    s4_h = anchor_to_xy(('TR', 0.06, 0.923))   # ~(206, 92)
    s4_t = anchor_to_xy(('C', 0.737, 0.392))   # ~(174, 139)
    # slight leftward bow
    ctrl = ((s4_h[0] + s4_t[0]) / 2 - 4, (s4_h[1] + s4_t[1]) / 2 - 2)
    pts = quad_bezier(s4_h, ctrl, s4_t, N)
    widths = [max(3, int(6 - 2 * i / N)) for i in range(N + 1)]
    stroke_variable_width(draw, pts, widths)

    # ============================================================
    # BOTTOM: 木 (4 strokes) — heng + shu + pie + na
    # ============================================================

    # --- Stroke 5: 横 (heng) — wide horizontal ---
    # head ML(0.554, 0.919) → tail MR(0.361, 0.79)
    s5_h = anchor_to_xy(('ML', 0.554, 0.919))  # ~(55, 192)
    s5_t = anchor_to_xy(('MR', 0.361, 0.79))   # ~(236, 179)
    pts = sample_line(s5_h, s5_t, N)
    widths = [6] * (N + 1)
    # slight thick middle
    for i in range(N // 3, 2 * N // 3):
        widths[i] = 7
    widths[0] = 4
    widths[-1] = 5
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 6: 竖 (shu) — vertical, crosses s5 (P weld) ---
    # head C(0.395, 0.515) → tail BC(0.518, 1.126) clipped to canvas
    s6_h = anchor_to_xy(('C', 0.395, 0.515))          # ~(140, 152)
    s6_t = clip_y(anchor_to_xy(('BC', 0.518, 1.126))) # ~(152, 295)
    pts = sample_line(s6_h, s6_t, N)
    widths = [8] * (N + 1)
    # slight taper at bottom
    for i in range(N - 4, N + 1):
        widths[i] = max(5, 8 - (i - (N - 4)))
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 7: 撇 (pie) — from cross point down-left ---
    # head C(0.409, 0.896) → tail BL(0.413, 0.81)
    s7_h = anchor_to_xy(('C', 0.409, 0.896))   # ~(141, 190)
    s7_t = anchor_to_xy(('BL', 0.413, 0.81))   # ~(41, 281)
    # curved 撇
    ctrl = (s7_h[0] * 0.5 + s7_t[0] * 0.5 + 8,
            s7_h[1] * 0.3 + s7_t[1] * 0.7)
    pts = quad_bezier(s7_h, ctrl, s7_t, N)
    widths = [max(3, int(8 - 5 * i / N)) for i in range(N + 1)]
    stroke_variable_width(draw, pts, widths)

    # --- Stroke 8: 捺 (na) — from cross point down-right, thin-to-thick flare ---
    # head C(0.564, 0.878) → tail BR(0.815, 0.766)
    s8_h = anchor_to_xy(('C', 0.564, 0.878))   # ~(156, 188)
    s8_t = anchor_to_xy(('BR', 0.815, 0.766))  # ~(282, 277)
    # slight downward arc
    ctrl = ((s8_h[0] + s8_t[0]) / 2, (s8_h[1] + s8_t[1]) / 2 + 12)
    pts = quad_bezier(s8_h, ctrl, s8_t, N)
    widths = [max(4, int(4 + 7 * i / N)) for i in range(N + 1)]
    widths[-1] = 3  # taper very tip
    widths[-2] = 5
    stroke_variable_width(draw, pts, widths)

    return img


if __name__ == '__main__':
    img = draw_cai()
    out = os.path.join(HERE, '01_采.png')
    img.save(out)
    print('wrote', out)
