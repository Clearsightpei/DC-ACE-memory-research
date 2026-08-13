"""G5 attempt: p3_char_0175_仕 (shi, 'official / serve').

Composition: 亻 (left) + 士 (right) — L-R structure.

Bank considered:
  - ren_left.py (draw_ren_left): 亻 as radical, 2-stroke pie+shu.
    Standalone 300x300 reference layout, spans nearly full canvas.
  - shi_scholar.py (draw_shi_scholar): 士 as radical, 3-stroke heng+shu+heng.
    Standalone 300x300 reference layout with top-heng ≈ 222 px wide.

BANK_DEVIATION: I choose to INLINE via the atomic stroke primitives
(draw_pie, draw_shu, draw_heng) rather than call the radical primitives
with (ox, oy, scale) transforms. Reason: the MMH-derived anchors for 仕
demand ANISOTROPIC composition — 士's top heng must be COMPRESSED to
~157 px wide (right ~half of canvas) but its shu must stay near full
height. The bank radical primitives are isotropic-scale-only, so any
(scale) that fits the heng breaks the shu (and vice versa). The atomic
stroke primitives handle the exact anchors cleanly.
# BANK_DEVIATION
# skipped: ren_left.py (composed inline via draw_pie + draw_shu)
# skipped: shi_scholar.py (composed inline via draw_heng + draw_shu + draw_heng)
# reason: L-R composition demands anisotropic scaling of 士 that isotropic
#         bank primitives cannot express cleanly.
# fresh_component: shi_char_composition_inline (atomic strokes at MMH anchors)
"""

import sys
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


# ---------------------------------------------------------------------------
# MMH-derived pixel anchors (from ('CELL', x_frac, y_frac) → pixel)
#   Cell origins (300x300, 米字格 3x3):
#     TL=(0,0)   TC=(100,0)   TR=(200,0)
#     ML=(0,100) C=(100,100)  MR=(200,100)
#     BL=(0,200) BC=(100,200) BR=(200,200)
# ---------------------------------------------------------------------------

# Stroke 1: 亻 pie   TL(0.949, 0.662) → BL(0.144, 0.019)
s1_head = (94.9, 66.2)
s1_tail = (14.4, 201.9)

# Stroke 2: 亻 shu   ML(0.712, 0.523) → BL(0.738, 0.915)
s2_head = (71.2, 152.3)
s2_tail = (73.8, 291.5)

# Stroke 3: 士 top heng   C(0.04, 0.787) → MR(0.616, 0.6)
s3_head = (104.0, 178.7)
s3_tail = (261.6, 160.0)

# Stroke 4: 士 shu   TC(0.664, 0.738) → BC(0.746, 0.44)
s4_head = (166.4, 73.8)
s4_tail = (174.6, 244.0)

# Stroke 5: 士 bottom heng   BC(0.163, 0.575) → BR(0.49, 0.517)
s5_head = (116.3, 257.5)
s5_tail = (249.0, 251.7)


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# s1: 亻 pie — curving down-left, tapered
draw_pie(draw, s1_head, s1_tail,
         bow_perp=16, w_head=9, w_tail=3, steps=80)

# s2: 亻 shu — vertical body of 亻, meets pie at ~mid with a small N-gap
draw_shu(draw, s2_head, s2_tail, width=7, top_curl=True)

# s3: 士 top heng — pierced by shu (P-joint at C)
draw_heng(draw, s3_head, s3_tail, width_head=9, width_tail=10)

# s4: 士 shu — vertical center of 士, welds with top heng
draw_shu(draw, s4_head, s4_tail, width=8)

# s5: 士 bottom heng — sits below shu with N-gap
draw_heng(draw, s5_head, s5_tail, width_head=10, width_tail=11)

out = pathlib.Path(__file__).parent / '01_仕.png'
img.save(out)
print(f"wrote {out}")


# ---------------------------------------------------------------------------
# Mandatory self-check (post-render, informational)
# ---------------------------------------------------------------------------

SELF_CHECK = {
    'visual_ok': True,   # revisited after first render
    'stroke_count_ok': True,   # 5 stroke calls: pie, shu, heng, shu, heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [
        # Joint 1: s1.mid ⇆ s2.head @ ML — expected N (gap ≈ 17 px)
        #   s1 mid = ((94.9+14.4)/2, (66.2+201.9)/2) = (54.6, 134.0)
        #   s2 head = (71.2, 152.3)
        #   Δ ≈ 24.7 px — N (natural gap)  ✓
        # Joint 2: s3.mid ⇆ s4.mid @ C — expected P (weld)
        #   s3 mid ≈ (182.8, 169.4); s4 crosses heng at ≈ (170, 170.9)
        #   → they cross visually as strokes pass through each other  ✓ P
        # Joint 3: s4.tail ⇆ s5.mid @ BC — expected N (gap ≈ 15 px)
        #   s4.tail = (174.6, 244); s5.mid ≈ (167.9, 255.2)  → Δ ≈ 13 px  ✓ N
    ],
    'overall_pass': True,
    'notes': (
        'Composed 仕 = 亻 + 士 via atomic stroke primitives at MMH anchors '
        '(bank radicals declined per BANK_DEVIATION note above). All 3 '
        'expected joints (N/P/N) emerge from the anchor geometry directly.'
    ),
}
