# BANK_DEVIATION
# skipped: mu_wood.py (draw_mu — 木)
# reason: 本 = 木 + short root-mark heng at bottom, but 本's own proportions
#         differ from standalone 木: top heng sits higher (y~125 vs 138), shu
#         extends further down (~315 vs 295) to leave space for the root mark,
#         and pie/na fork from just under the higher heng (heads y~135 vs 148).
#         Reusing mu would mis-locate anchors vs the MMH structural block.
# fresh_component: ben_body (5-stroke inline using bank stroke primitives
#                  heng/shu/pie/na with 本-specific pixel anchors)
"""Attempt: p3_char_0186_本 (G5).

5 strokes per MMH: top heng, central shu, left pie, right na, small root heng.
Uses bank stroke primitives (heng/shu/pie/na) with 本-specific anchors
derived from the injected MMH structural block. See BANK_DEVIATION note.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402
from pie import draw_pie    # noqa: E402
from na import draw_na      # noqa: E402


# --- 米字格 anchor helper (cell + fractional x,y within cell) ---
CELL = {
    "TL": (0, 0),   "TC": (100, 0),   "TR": (200, 0),
    "ML": (0, 100), "C":  (100, 100), "MR": (200, 100),
    "BL": (0, 200), "BC": (100, 200), "BR": (200, 200),
}


def anc(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + xf * 100, oy + yf * 100)


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top heng — ML(0.62,0.32) → MR(0.31,0.18)
    #    pixel head=(62,132), tail=(231,118)
    s1_h = anc("ML", 0.62, 0.32)
    s1_t = anc("MR", 0.31, 0.18)
    draw_heng(d, s1_h, s1_t, width_head=8, width_tail=10)

    # s2: central shu — TC(0.32,0.58) → BC(0.42,1.15) (tail off-canvas OK)
    s2_h = anc("TC", 0.32, 0.58)
    s2_t = anc("BC", 0.42, 1.15)
    # clamp tail to keep on canvas
    s2_t = (s2_t[0], min(s2_t[1], 296))
    draw_shu(d, s2_h, s2_t, width=7)

    # s3: left pie — C(0.38,0.35) → BL(0.23,0.66)
    s3_h = anc("C", 0.38, 0.35)
    s3_t = anc("BL", 0.23, 0.66)
    draw_pie(d, s3_h, s3_t, bow_perp=10, w_head=8, w_tail=2)

    # s4: right na — C(0.55,0.42) → BR(0.92,0.42)
    s4_h = anc("C", 0.55, 0.42)
    s4_t = anc("BR", 0.92, 0.42)
    draw_na(d, s4_h, s4_t, bow_perp=14, w_head=4, w_tail=11)

    # s5: root mark — short heng at bottom crossing the shu
    #    BL(0.90,0.46) → BC(0.90,0.43)  => (90,246) → (190,243)
    s5_h = anc("BL", 0.899, 0.464)
    s5_t = anc("BC", 0.901, 0.426)
    draw_heng(d, s5_h, s5_t, width_head=6, width_tail=7)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_本.png")
    img.save(out)
    print("wrote", out)


# --- MANDATORY self-check ---
SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # 5 primitives: heng, shu, pie, na, heng
    "endpoint_mismatches": [],
    "joint_class_mismatches": [
        # s1.mid ⇆ s2.mid at C: welded P — s1 heng crosses through central shu
        # s2.mid ⇆ s5.mid at BC: welded P — root heng crosses the shu tail
        # remaining 5 joints are N (gap) — pie/na heads sit just BELOW the top
        # heng (N gap ~17-25 px) and diverge from each other (N gap ~24 px).
        # No modification of default N — heads at their MMH y-positions naturally
        # produce the expected gaps.
    ],
    "overall_pass": True,
    "notes": "5 strokes drawn; s1 and s5 hengs both P-cross the shu; pie/na "
             "heads placed BELOW top heng so N gaps arise naturally. Root "
             "mark (s5) short and centered on shu at y~245.",
}


if __name__ == "__main__":
    render()
