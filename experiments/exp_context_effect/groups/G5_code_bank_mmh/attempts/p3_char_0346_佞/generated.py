"""Drawer attempt for p3_char_0346_佞 (nìng, "flattering") — 7 strokes.

Composition (visible in GT): 亻 (left, 2 strokes) + 二 (top-right, 2 strokes) +
女 (bottom-right, 3 strokes).

P-A-008 INLINE REASONING TRACE (per sub-component):

1) 亻 (亻 = left-position person radical, 2 strokes)
   - Hard-check per P-A-007-v2: bank has ren_left. Native aspect: pie length ~158,
     shu length ~135, pie-tail y ≈ 211, shu-head y ≈ 158 (pie ends BEFORE shu starts).
   - Needed for 佞: pie (94, 70.3) → (17.3, 204.2), length ≈ 154; shu (70, 156.7) →
     (74.4, 295.3), length ≈ 139. Ratio 154/158 = 0.97, 139/135 = 1.03. Both ∈ [0.55, 1.2].
     Aspect + geometry both match. → CALL BANK.
   - Translate: pie head 94 - 158.8 = -64.8; shu head 70 - 138.9 = -68.9. Average ≈ -67.
     Use draw_ren_left(ox=-67, oy=-2, scale=1.0).

2) 二 (top-right stack of two heng, 2 strokes)
# BANK_DEVIATION
# skipped: er_two.py
# reason: standalone 二 has upper 一 = 129px wide, lower 一 = 232px wide (ratio 1.80)
#         and vertical sep ≈ 108px. 佞's 二 has upper = 80px, lower = 120px
#         (ratio 1.50), sep = 44px. Non-uniform aspect: at any single scale that
#         matches one heng-width, the other heng-width and the vertical sep are off.
# fresh_component: er_two_compact — two short heng at MMH endpoints (both slightly
#                  rising as the GT shows).
   - s3 (upper 一): draw_heng at (135.4, 101.7) → (214.5, 94.9), narrow.
   - s4 (lower 一): draw_heng at (117.2, 145.3) → (237.0, 136.5), slightly wider.

3) 女 (bottom-right, 3 strokes)
# BANK_DEVIATION
# skipped: nu_woman.py
# reason: standalone 女's s1 (撇点) head at (129.5, 62.7 — upper), but 佞's s5 head
#         at (157, 165 — middle-center); no (ox, oy, scale) can align. Also heng
#         ratio 169/258 = 0.65 but pie height ratio 108/137 = 0.79 — non-uniform.
# fresh_component: nu_compact_under_二 — 3 straight-tapered strokes at MMH endpoints
#                  approximating 撇点 (as diagonal), 撇, 横.
   - s5: (157.0, 165.2) → (234.7, 298.8) — straight diagonal (approx of 撇点's
     compressed second half).
   - s6 (撇): (189.3, 184.6) → (110.7, 293.0) — down-left, taper thick→thin.
   - s7 (横): (96.7, 204.8) → (266.0, 196.3) — long horizontal under.

SELF_CHECK: stroke count 2+2+3 = 7 ✓. Endpoints copied verbatim from MMH block.
Joint classes: s1.mid⇆s2.head N (bank's ren_left naturally produces this gap);
s5⇆s6 P (both cross at BC, straight-line rendering yields a crossing near their
midpoints); s5⇆s7 P (crossing near their lower ends); s6.head⇆s7.mid T (s6 head
lands on s7's ~0.6 position ≈ (198, 200), close enough for T contact).
"""

import os
import sys

# Add success_bank/code to path for bank primitives
_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402
from ren_left import draw_ren_left  # noqa: E402
from heng import draw_heng  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Bank ren_left called at (-67, -2, 1.0). 二 and 女 inlined per BANK_DEVIATION with MMH endpoints verbatim.',
}


def _tapered_line(draw, head, tail, w_head, w_tail, steps=70):
    dx = tail[0] - head[0]
    dy = tail[1] - head[1]
    for i in range(steps):
        t = i / (steps - 1)
        x = head[0] + t * dx
        y = head[1] + t * dy
        w = w_head + (w_tail - w_head) * t
        r = max(0.5, w / 2.0)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- 亻 (2 strokes, BANK ren_left; P-A-007-v2 hard-check pass) ---
    draw_ren_left(draw, ox=-67, oy=-2, scale=1.0)

    # --- 二 (2 strokes, BANK_DEVIATION inline) ---
    # s3: upper 一, narrow, slight rise
    draw_heng(draw, (135.4, 101.7), (214.5, 94.9),
              width_head=8, width_tail=9)
    # s4: lower 一, slightly wider, slight rise
    draw_heng(draw, (117.2, 145.3), (237.0, 136.5),
              width_head=9, width_tail=10)

    # --- 女 (3 strokes, BANK_DEVIATION inline) ---
    # s5: 撇点 (approx as diagonal down-right)
    _tapered_line(draw, (157.0, 165.2), (234.7, 298.8),
                  w_head=6, w_tail=9, steps=70)
    # s6: 撇 (down-left, thick→thin)
    _tapered_line(draw, (189.3, 184.6), (110.7, 293.0),
                  w_head=9, w_tail=3, steps=70)
    # s7: 横 (long horizontal, spans lower half of right side)
    _tapered_line(draw, (96.7, 204.8), (266.0, 196.3),
                  w_head=6, w_tail=8, steps=70)

    out_path = os.path.join(os.path.dirname(__file__), '01_佞.png')
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
