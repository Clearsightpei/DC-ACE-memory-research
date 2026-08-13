"""G5 attempt — p2_radical_091_斗 (dou — dipper), 4 strokes.

Composition (per MMH-injected anchors):
  s1: small dian, TC(0.002,0.876) → C(0.368,0.131)   = (100, 88) → (137, 113)
  s2: small dian, ML(0.905,0.392) → C(0.248,0.641)   = (90, 139) → (125, 164)
  s3: long heng,  BL(0.258,0.019) → MR(0.751,0.904)  = (26, 202) → (275, 190)
  s4: long shu,   TC(0.535,0.545) → BC(0.708,1.199)  = (154, 55) → (171, 300)

Joint: s3.mid ⇆ s4.mid @ C — P (welded crossing) at ~(171, 190).
No BANK_DEVIATION — bank primitives (dian, heng, shu) fit cleanly.
"""

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1 — upper dian (small tapered dot, thin head → thick tail)
    draw_dian(d, head=(100, 88), tail=(137, 113),
              w_head=3, w_tail=7, bow=3)

    # s2 — lower dian (parallel to s1, slightly larger)
    draw_dian(d, head=(90, 139), tail=(125, 164),
              w_head=3, w_tail=7, bow=3)

    # s3 — long heng, crossing full width; slightly tilted up-to-right per MMH
    draw_heng(d, head=(26, 202), tail=(275, 190),
              width_head=8, width_tail=9)

    # s4 — long shu, welded across s3 at cell C (P joint)
    # Tail clipped to canvas bottom (MMH y=1.199 in BC = 320 → 300)
    draw_shu(d, head=(154, 55), tail=(171, 300), width=8)

    return img


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 turtle-equivalent calls: dian, dian, heng, shu
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s3×s4 @ C implemented as P (welded crossing)
    'overall_pass': True,
    'notes': 's4 tail MMH y=1.199 (below canvas) clipped to y=300; heng+shu cross at ~(171,190) — natural weld.',
}


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_斗.png")
    render().save(out)
    print(f"wrote {out}")
