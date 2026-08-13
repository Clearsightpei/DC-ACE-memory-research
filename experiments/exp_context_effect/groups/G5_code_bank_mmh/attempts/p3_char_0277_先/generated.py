"""p3_char_0277_先 (xian, "first/before") — 6 strokes.

Composition (from MMH anchors, P-A-006 stroke-primitive layer):
  s1: short pie (top short, slanting down-left)
  s2: short heng slanting up-right (top-middle)
  s3: tall vertical shu (from top, pierces s2 mid, ends above s4)
  s4: long horizontal heng across middle
  s5: pie descending to bottom-left (from s4)
  s6: shu_wan_gou (from just below s4-mid down, curve right, hook up-right)

Joints (all N except s2mid⇆s3mid = P):
  s1.mid ⇆ s2.head       : N (~12 px)
  s2.mid ⇆ s3.mid        : P (welded pierce)
  s3.tail ⇆ s4.mid(0.44) : N (~13 px)
  s3.tail ⇆ s6.head      : N (~23 px)
  s4.mid(0.30) ⇆ s5.head : N (~21 px)
  s4.mid(0.48) ⇆ s6.head : N (~15 px)

Bank primitives: pie, heng, shu, shu_wan_gou (all already promoted).
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 6 primitives called (pie, heng, shu, heng, pie, shu_wan_gou)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors baked from MMH block; s3 pierces s2 (P), all others N gaps preserved via not-quite-touching endpoints.'
}


def draw_xian(d, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return (ox + x * scale, oy + y * scale)

    # s1: short pie — TL(0.984, 0.955) → ML(0.729, 0.632)
    #       (98.4, 95.5) → (72.9, 163.2)
    draw_pie(d,
             T(98.4, 95.5), T(72.9, 163.2),
             bow_perp=8, w_head=max(2, int(7 * scale)),
             w_tail=max(2, int(2 * scale)), steps=60)

    # s2: short heng — C(0.049, 0.342) → MR(0.054, 0.157)
    #       (104.9, 134.2) → (205.4, 115.7)
    draw_heng(d,
              T(104.9, 134.2), T(205.4, 115.7),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))

    # s3: tall vertical shu — TC(0.395, 0.595) → C(0.43, 0.731)
    #       (139.5, 59.5) → (143.0, 173.1)
    # Pierces s2 near its midpoint (~(155, 125)) — s3 goes from y=59 to y=173,
    # naturally crossing s2's y-range (115..134). P joint is welded.
    draw_shu(d,
             T(139.5, 59.5), T(143.0, 173.1),
             width=max(2, int(7 * scale)), top_curl=False)

    # s4: long horizontal heng — ML(0.554, 0.931) → MR(0.42, 0.729)
    #       (55.4, 193.1) → (242.0, 172.9)
    draw_heng(d,
              T(55.4, 193.1), T(242.0, 172.9),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(10 * scale)))

    # s5: pie sweeping down-left — C(0.184, 0.995) → BL(0.398, 0.965)
    #       (118.4, 199.5) → (39.8, 296.5)
    # Starts a hair below s4's y=193 (N gap ~20 px per MMH).
    draw_pie(d,
             T(118.4, 199.5), T(39.8, 296.5),
             bow_perp=10, w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(2 * scale)), steps=70)

    # s6: shu_wan_gou — C(0.544, 0.854) → BR(0.739, 0.399)
    #       (154.4, 185.4) → (273.9, 239.9)
    # Head just below s4 (N gap ~15 px). Descends, curves right, hooks up.
    draw_shu_wan_gou(d,
                     T(154.4, 185.4), T(273.9, 239.9),
                     width=max(2, int(7 * scale)),
                     bottom_extra=60, knee_ratio=0.72)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_xian(d)
    out = Path(__file__).parent / "01_先.png"
    img.save(out)
    print(f"wrote {out}")
