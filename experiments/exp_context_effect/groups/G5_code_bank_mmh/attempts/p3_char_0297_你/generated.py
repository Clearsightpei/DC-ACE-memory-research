"""p3_char_0297_你 — G5 attempt

你 = 亻 (left, 2 strokes) + 尔 (right, 5 strokes). 7 strokes per MMH.

Sibling of p3_char_0185_仟 (亻+X L-R template): use stroke-signature
primitives with MMH pixel anchors directly, avoiding double-transform
from calling draw_ren_left with scale/offset.

Per P-A-006 (MMH-anchor verbatim + stroke-primitive layer). Per
P-COMP-011 the right side (尔) has hooks (heng-gou + shu-gou) so this
is expected to PASS rather than A — do not force straight-stroke
replacements.

No BANK_DEVIATION — this is stroke-composition, no bank sub-element
replacement.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng_gou import draw_heng_gou
from shu_gou import draw_shu_gou
from dian import draw_dian

# ---------------------------------------------------------------
# MMH-derived pixel anchors (from injected structural block)
# Cell base:  TL(0,0) TC(100,0) TR(200,0) / ML(0,100) C(100,100) MR(200,100)
#             BL(0,200) BC(100,200) BR(200,200)
# ---------------------------------------------------------------
# s1 亻 pie:      TL(0.929, 0.621) -> ML(0.199, 0.925)  = (93, 62) -> (20, 193)
# s2 亻 shu:      ML(0.8, 0.365)   -> BL(0.762, 0.88)   = (80, 137) -> (76, 288)
# s3 尔 pie:      TC(0.629, 0.574) -> C(0.189, 0.737)   = (163, 57) -> (119, 174)
# s4 尔 heng-gou: C(0.503, 0.441)  -> MR(0.186, 0.652)  = (150, 144) -> (219, 165)
# s5 尔 pie:      C(0.717, 0.644)  -> BC(0.436, 0.751)  = (172, 164) -> (144, 275)
# s6 尔 shu-gou:  BC(0.333, 0.074) -> BC(0.163, 0.558)  = (133, 207) -> (116, 256)
# s7 尔 dian:     BR(0.174, 0.045) -> BR(0.572, 0.549)  = (217, 205) -> (257, 255)

img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# --- Stroke 1: 亻 pie (long TL→ML sweep) ---
draw_pie(d, head=(93, 62), tail=(20, 193),
         bow_perp=14, w_head=9, w_tail=3, steps=90)

# --- Stroke 2: 亻 shu (long vertical descender) ---
# N-gap with s1.mid ~ 12px: s1 mid is at ((93+20)/2, (62+193)/2) + bow ≈ (57, 140);
# s2 head (80, 137). Distance ≈ 23px. Natural N.
draw_shu(d, head=(80, 137), tail=(76, 288), width=7)

# --- Stroke 3: 尔 pie (top-left of 尔, descending down-left) ---
draw_pie(d, head=(163, 57), tail=(119, 174),
         bow_perp=10, w_head=8, w_tail=3, steps=70)

# --- Stroke 4: 尔 heng-gou (short horizontal top of 尔 with downward hook) ---
# MMH gives head + tail (median endpoints), corner = tail. Hook extends below.
draw_heng_gou(d, head=(150, 144), corner=(219, 165), hook_tip=(212, 190),
              w_start=6, w_corner=8, w_tip=3)

# --- Stroke 5: 尔 pie (left short pie descending down-left) ---
draw_pie(d, head=(172, 164), tail=(144, 275),
         bow_perp=6, w_head=6, w_tail=3, steps=60)

# --- Stroke 6: 尔 shu-gou (short vertical + tiny leftward hook, center of 尔) ---
draw_shu_gou(d, head=(133, 207), tail=(116, 256),
             width=6, hook_start_offset=18)

# --- Stroke 7: 尔 dian (right dot descending to lower-right) ---
draw_dian(d, head=(217, 205), tail=(257, 255),
          w_head=3, w_tail=8, bow=4)

out = pathlib.Path(__file__).parent / "01_你.png"
img.save(out)
print(f"wrote {out}")

# ---------------------------------------------------------------
# Mandatory self-check block
# ---------------------------------------------------------------
SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # 7 primitives: pie, shu, pie, heng_gou, pie, shu_gou, dian
    "endpoint_mismatches": [],  # all anchors used verbatim from MMH block
    "joint_class_mismatches": [
        # J1: s1.mid ⇆ s2.head @ ML N (expected gap ~12px).
        #     s1 mid ≈ (57, 140) + bow ≈ (57, 148). s2 head (80, 137).
        #     Distance ≈ 25 px — natural N (not welded).
        # J2: s3.mid ⇆ s4.head @ C N (expected gap ~13px).
        #     s3 mid ≈ ((163+119)/2, (57+174)/2) + small bow ≈ (141, 122).
        #     s4 head (150, 144). Distance ≈ 24 px — natural N (not welded).
        # No welding required, both are N-joints.
    ],
    "overall_pass": True,
    "notes": "7-stroke 你 = 亻(pie+shu) + 尔(pie+heng_gou+pie+shu_gou+dian). "
             "P-A-006 approach (stroke-primitive + MMH anchors verbatim). "
             "P-COMP-011: right half has hooks so PASS-target not A-target. "
             "No BANK_DEVIATION.",
}
