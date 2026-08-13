"""p3_char_0411_受 — G5 attempt.

Decomposition (from GT + MMH anchors, 8 strokes total):
  - Top 4 strokes: 爫 (zhao_claw_top)  → BANK primitive draw_zhao_claw_top
  - Middle 2 strokes: 冖 (mi_cover)     → BANK primitive draw_mi_cover
  - Bottom 2 strokes: 又 (heng_pie + na) → BANK_DEVIATION, inline (aspect mismatch)

Per-sub-component reasoning trace (P-A-008):

  [1] 爫 top: bank draw_zhao_claw_top native footprint W=122 H=71 AR=1.72.
      Target footprint from MMH anchors: W=114 H=73 AR=1.56.
      AR ratio 1.56/1.72 = 0.91 (within P-A-007-v2 [0.55, 1.2] range).
      Scale 0.93 (=114/122) → use whole-radical BANK (aspect close, natural fit).

  [2] 冖 middle: bank draw_mi_cover native W=159 H=56 AR=2.84.
      Target W=165 H=58 AR=2.84 → IDENTICAL aspect. Scale ~1.03.
      Use whole-radical BANK.

  [3] 又 bottom: bank draw_you native W=243 H=163 AR=1.49.
      Target W=206 H=103 AR=2.00.
      AR ratio 2.00/1.49 = 1.34 > 1.2 → P-A-007-v2 hard-check FAILS.
      In 受 the 又 is squashed vertically (only ~103 px tall vs bank 163).
      BANK_DEVIATION: inline s7 (heng_pie) + s8 (na) at exact MMH endpoints.
"""

# BANK_DEVIATION
# skipped: you_again.py (draw_you)
# reason: target 又 AR=2.00 vs bank native AR=1.49; ratio 1.34 exceeds
#         P-A-007-v2 [0.55, 1.2] band. In 受 the 又 is significantly
#         flatter/wider than the standalone radical. Whole-radical scale
#         would either overshoot height (162*0.85=138 vs target 103) or
#         squeeze width — no single (ox,oy,scale) triple fits.
# fresh_component: inline heng_pie + na at MMH-anchor endpoints
# quantitative: native (W243, H163) → target (W206, H103):
#   width_scale = 206/243 = 0.848
#   height_scale = 103/163 = 0.632
#   ratio 0.848/0.632 = 1.34 → aspect distortion beyond tolerance.

import os
import sys
from PIL import Image, ImageDraw

# Success bank on path
BANK_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK_DIR))

from zhao_claw_top import draw_zhao_claw_top  # noqa: E402
from mi_cover import draw_mi_cover              # noqa: E402
from heng_pie import draw_heng_pie              # noqa: E402
from na import draw_na                          # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 (爫) + 2 (冖) + 2 (又) = 8 ✓
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all N-gaps preserved by bank spacing;
                                  # s7/s8 cross naturally at ~(120,230) → P
    'overall_pass': True,
    'notes': (
        'Top 爫 via bank scale~0.93 ox~14 oy~14; '
        'Middle 冖 via bank scale=1.0 ox=-3 oy=60; '
        'Bottom 又 inline (BANK_DEVIATION, AR mismatch 2.00 vs 1.49).'
    ),
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # --- Top: 爫 (strokes 1-4) --------------------------------------------
    # Target region: x=[91,205], y=[66,139]. Bank native: x=[81,203] y=[56,127].
    draw_zhao_claw_top(d, ox=14.7, oy=14.8, scale=0.93)

    # --- Middle: 冖 (strokes 5-6) -----------------------------------------
    # Target region: x=[51,216], y=[152,210]. Bank native: x=[54,213] y=[92,148].
    draw_mi_cover(d, ox=-3, oy=60, scale=1.0)

    # --- Bottom: 又 (strokes 7-8) — inline ---------------------------------
    # s7 heng_pie: MMH head (104.3, 197.8), tail (67.4, 295.9).
    # Override apex_x / corner_x so the horizontal segment is short (in 受
    # the bottom 又 is squashed; the horizontal wing doesn't extend far right).
    s7_head = (104, 198)
    s7_tail = (67, 296)
    draw_heng_pie(d, s7_head, s7_tail,
                  apex_x=s7_head[0] + 40,
                  corner_x=s7_head[0] + 35)

    # s8 na: MMH head (96.7, 219.1), tail (273.3, 300.9).
    # The 撇 (s7) and 捺 (s8) cross at ~(120, 230) — P-joint welded implicitly.
    draw_na(d, (97, 219), (273, 301),
            bow_perp=13, w_head=4, w_tail=12, steps=90)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_受.png",
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
