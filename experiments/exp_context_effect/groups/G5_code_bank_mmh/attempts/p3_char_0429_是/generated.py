# BANK_DEVIATION
# skipped: ri_sun.py  (bank primitive for 日)
# reason: native 日 aspect w:h = 118:189 = 0.62 (tall). 是's top 日 needs
#         w:h ~ 90:80 = 1.13 (flat/squat). ratio 1.13/0.62 = 1.82x wider
#         than native, well outside P-A-007-v2 [0.55, 1.2] whole-radical band.
#         Inline the 4 strokes at target proportions instead.
# fresh_component: ri_flat_for_shi (squat 日 top for 是-family: 是/题/提/堤)
#
# skipped: zheng_correct.py (bottom half is 疋, not 正 — different stroke set)
# reason: 疋 = 5 strokes (heng, shu, short-heng, pie, na); 正 = 5 strokes
#         (heng, shu, short-heng, short-shu, long-heng). Structure diverges
#         on strokes 4-5 (pie+na vs shu+heng). Bank has no zheng-family
#         primitive that models pie+na tail. Inline fresh.
# fresh_component: pi_bottom_for_shi (疋-style bottom: heng+shu+shortheng+pie+na)
#
# P-A-008 per-sub-component trace:
#   sub 1 = 日 (top, 4 strokes) → bank-aspect-mismatch → inline squashed
#   sub 2 = 一 (middle long heng, 1 stroke) → primitive draw_heng
#   sub 3 = 龰-remainder (bottom, 4 strokes: shu+shortheng+pie+na) → primitive strokes
#
# P-A-009 quantitative reasoning:
#   日 native aspect 0.62 vs target 1.13 → 1.82x deviation → SKIP whole-radical
#   heng primitive: uniform stroke → USE
#   pie/na primitives: MMH endpoint bow tuning → USE

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, BANK)

from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from na import draw_na
from pie import draw_pie
from shu import draw_shu

img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# --- Top 日 (strokes 1-4) — squashed inline ---
# s1: left shu
draw_shu(d, (108, 50), (110, 132), width=5)
# s2: heng-zhe-box (top-right corner)
draw_heng_zhe_box(d, (112, 52), (198, 132), width=5)
# s3: middle horizontal inside 日
draw_heng(d, (114, 90), (190, 88), width_head=4, width_tail=5)
# s4: bottom horizontal closing 日
draw_heng(d, (108, 128), (198, 126), width_head=5, width_tail=6)

# --- Middle heng under 日 (stroke 5) — spans wider than 日 ---
draw_heng(d, (48, 172), (254, 165), width_head=6, width_tail=8)

# --- Bottom 龰-part (strokes 6-9) ---
# s6: small shu drops from just below the middle heng, slightly right of center
draw_shu(d, (145, 176), (155, 225), width=5)
# s7: short heng branching right from the shu bottom (small ⊥ shape)
draw_heng(d, (152, 218), (210, 213), width_head=5, width_tail=6)
# s8: long pie sweeping down-left from crossing region
draw_pie(d, (155, 220), (50, 278), bow_perp=18, w_head=9, w_tail=3)
# s9: long na sweeping down-right (final closing diagonal, flat foot)
draw_na(d, (135, 225), (270, 282), bow_perp=14, w_head=4, w_tail=13)

out = os.path.join(os.path.dirname(__file__), "01_是.png")
img.save(out)
print("wrote", out)

# ------ SELF-CHECK ------
SELF_CHECK = {
    "visual_ok": None,          # filled after first render inspection
    "stroke_count_ok": True,    # 9 primitive calls (shu, hzbox, heng, heng, heng, shu, heng, pie, na)
    "endpoint_mismatches": [],  # visual placement approximates MMH cells
    "joint_class_mismatches": [],  # all joints implemented as N (gaps preserved by not welding)
    "overall_pass": None,
    "notes": (
        "9 strokes: s1 shu, s2 heng_zhe_box, s3 inner heng, s4 bottom heng, "
        "s5 long middle heng, s6 shu drop, s7 short heng, s8 pie, s9 na. "
        "BANK_DEVIATION for ri_sun (aspect mismatch) and zheng_correct (疋 not 正)."
    ),
}
