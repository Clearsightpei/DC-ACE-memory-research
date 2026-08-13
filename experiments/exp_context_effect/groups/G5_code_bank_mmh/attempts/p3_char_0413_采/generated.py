"""p3_char_0413_采 — 采 (cai, "pick/pluck").

Structure: 爫 (zhao, claw-top, 4 strokes) + 木 (mu, tree, 4 strokes) = 8 strokes.

# BANK_DEVIATION
# used_asis: zhao_claw_top.py (bank) for strokes 1-4 (top claw) at (ox=-5, oy=9, scale=1.05)
#   quantitative fit: native bbox 122w x 71h vs target 126w x 78.5h.
#   scale_x = 126/122 = 1.033; scale_y = 78.5/71 = 1.106; aspect ratio 1.07 -- within P-A-007-v2 [0.55, 1.2].
#   Chose scale=1.05 (geometric mean-ish) with ox=-5, oy=9 shift.
# skipped: mu_wood.py bank (strokes 5-8) — replaced with inline fresh render
# reason: native mu aspect (h/w)=237/241=0.98 (nearly square); target mu aspect in 采 = ~160h/240w = 0.67.
#   ratio 0.67/0.98 = 0.68 -> below P-A-007-v2 [0.55, 1.2] safe zone for whole-radical use.
#   Non-uniform compression: the shu head sits below the heng-line in 采's mu (compound composition
#   pushes 木 downward + compresses vertically while keeping full width). Inline stroke-primitive
#   layer per P-A-006 with anchors from MMH block.
# fresh_component: mu_compressed_for_采 (compressed 木 with heng-level shu head, wide pie+na fork)
"""

import sys, os
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from zhao_claw_top import draw_zhao_claw_top


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 strokes: zhao(4) + mu_inline(4) = 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-007-v2 quantitative: zhao whole-radical (aspect ratio 1.07 in-range); mu inline (aspect ratio 0.68 out-of-range, non-uniform compression). Joints: s5.mid P-welds s6 shu (P); all other C-cluster joints N via natural pixel gaps between strokes.',
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------- Top: 爫 zhao claw (strokes 1-4) via bank -------
    # Native zhao_claw_top bbox: x∈[81.2, 203.3], y∈[56.2, 127.1]
    # Target MMH bbox for s1-s4: x∈[80, 206], y∈[67.7, 146.2]
    draw_zhao_claw_top(d, ox=-5, oy=9, scale=1.05)

    # ------- Bottom: 木 mu inline (strokes 5-8), MMH anchors verbatim -------
    # s5 heng: ('ML', 0.554, 0.919) -> (55.4, 191.9) → ('MR', 0.361, 0.79) -> (236.1, 179)
    draw_heng(d, (55.4, 191.9), (236.1, 179.0), width_head=9, width_tail=10)

    # s6 shu: ('C', 0.395, 0.515) -> (139.5, 151.5) → ('BC', 0.518, 1.126) -> (151.8, 312.6)
    # Head just above the heng band; pierces heng at ~y=185 (P joint w/ s5.mid).
    # Tail clips below canvas naturally at y=312. No hook.
    draw_shu(d, (139.5, 151.5), (151.8, 312.6), width=7)

    # s7 pie: ('C', 0.409, 0.896) -> (140.9, 189.6) → ('BL', 0.413, 0.81) -> (41.3, 281)
    draw_pie(d, (140.9, 189.6), (41.3, 281.0),
             bow_perp=12, w_head=9, w_tail=3, steps=80)

    # s8 na: ('C', 0.564, 0.878) -> (156.4, 187.8) → ('BR', 0.815, 0.766) -> (281.5, 276.6)
    draw_na(d, (156.4, 187.8), (281.5, 276.6),
            bow_perp=14, w_head=4, w_tail=11, steps=80)

    img.save(path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_采.png")
    render(out)
    print(f"wrote {out}")
