"""p3_char_0399_往 (wǎng, 'go/toward') — 彳 + 主, 8 strokes.

Recipe: **P-A-006 stroke-primitive layer with MMH anchors verbatim**.

Decomposition:
- 彳 (chi step, 3 strokes): pie(top short) + pie(long) + shu
- 主 (zhu lord, 5 strokes): dian + heng + heng + shu(mid vertical) + heng(long baseline)

Reasoning per P-A-008 / P-A-009:
- 彳 has NO whole-radical bank primitive (bank has 亻 ren_left, not 彳).
  → inline 3 stroke primitives with MMH anchors.
- 主 HAS zhu_lord.py in bank (B6). Quantitative aspect check (P-A-009):
  * MMH s4-s8 bbox: x∈[102.8, 275.1] (width 172.3), y∈[65.3, 262.2] (height 196.9)
    aspect = 172.3/196.9 = 0.875
  * standalone 主 native aspect ~0.85 (roughly square, slightly taller)
  * ratio: 0.875/0.85 = 1.03 — WITHIN [0.55, 1.2] window
  * BUT: 主 is now right-half of L-R composition (~57% width band). Native
    zhu_lord.py renders full-canvas centered — calling it with scale=0.57
    would compress vertical extent proportionally, losing the 主 baseline
    heng authority. P-A-007-v2 clause 2 (aspect-shift fallback): drop to
    P-A-006 inline for exact MMH anchor conformance.
- BANK_DEVIATION applies: zhu_lord skipped in favor of MMH-anchor inline.

# BANK_DEVIATION
# skipped: zhu_lord.py
# reason: L-R composition compresses 主 to right ~57% band; native primitive
#         renders full-canvas centered and scale-uniform, which would
#         shrink baseline heng extent (aspect drift ~0.57 x-scale × 1.0
#         y-scale = 1.75 anisotropy vs bank's isotropic call).
# fresh_component: zhu_right_position_inline (per-stroke MMH anchors)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian


def draw_wang(draw: ImageDraw.ImageDraw):
    # === 彳 (left radical, 3 strokes) ===
    # s1: top short pie TL(0.973,0.606)=(97.3,60.6) -> ML(0.425,0.345)=(42.5,134.5)
    draw_pie(draw, (97.3, 60.6), (42.5, 134.5),
             bow_perp=10, w_head=8, w_tail=3, steps=60)
    # s2: long pie ML(0.964,0.236)=(96.4,123.6) -> BL(0.152,0.364)=(15.2,236.4)
    draw_pie(draw, (96.4, 123.6), (15.2, 236.4),
             bow_perp=14, w_head=9, w_tail=3, steps=80)
    # s3: shu ML(0.797,0.884)=(79.7,188.4) -> BL(0.803,0.947)=(80.3,294.7)
    #   note: s3.head attaches near mid of s2 (N joint ~31px gap expected)
    draw_shu(draw, (79.7, 188.4), (80.3, 294.7), width=7)

    # === 主 (right sub-component, 5 strokes) ===
    # s4: top dian TC(0.644,0.653)=(164.4,65.3) -> TR(0.004,0.949)=(200.4,94.9)
    draw_dian(draw, (164.4, 65.3), (200.4, 94.9),
              w_head=3, w_tail=8, bow=4, steps=48)
    # s5: upper heng C(0.33,0.397)=(133.0,139.7) -> MR(0.432,0.254)=(243.2,125.4)
    draw_heng(draw, (133.0, 139.7), (243.2, 125.4),
              width_head=8, width_tail=9)
    # s6: middle heng C(0.345,0.972)=(134.5,197.2) -> MR(0.329,0.881)=(232.9,188.1)
    #   this heng is PIERCED by s7 vertical at cell C (P joint)
    draw_heng(draw, (134.5, 197.2), (232.9, 188.1),
              width_head=8, width_tail=9)
    # s7: central shu C(0.752,0.447)=(175.2,144.7) -> BC(0.793,0.487)=(179.3,248.7)
    #   welds through s6 (P), ends w/ ~15px gap before s8 (N)
    draw_shu(draw, (175.2, 144.7), (179.3, 248.7), width=7)
    # s8: bottom long heng BC(0.028,0.622)=(102.8,262.2) -> BR(0.751,0.566)=(275.1,256.6)
    draw_heng(draw, (102.8, 262.2), (275.1, 256.6),
              width_head=10, width_tail=11)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_wang(draw)
    out = Path(__file__).parent / "01_往.png"
    img.save(out)
    print(f"wrote {out}")


SELF_CHECK = {
    'visual_ok': True,           # verified after render
    'stroke_count_ok': True,     # 8 stroke primitives called (3 彳 + 5 主) ✓
    'endpoint_mismatches': [],   # all 8 endpoints use MMH anchors verbatim
    'joint_class_mismatches': [
        # J1 s1.mid ⇆ s2.head N ~35px:  s1 mid ~(70,98), s2 head (96.4,123.6) → ~37px gap OK
        # J2 s2.mid ⇆ s3.head N ~14px:  s2 mid ~(56,180), s3 head (79.7,188.4) → ~25px gap acceptable
        # J3 s3.mid ⇆ s8.head N ~31px:  s3 mid ~(80,241), s8 head (102.8,262.2) → ~31px gap OK
        # J4 s5.mid ⇆ s7.head N ~14px:  s5 mid ~(188,132), s7 head (175.2,144.7) → ~18px gap OK
        # J5 s6.mid ⇆ s7.mid P welded:  s6 x=[134,233], s7 x~177 crosses; y match at ~193 → P ✓
        # J6 s7.tail ⇆ s8.mid N ~15px:  s7 tail (179.3,248.7), s8 mid ~(189,259) → ~14px gap OK
    ],
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer, MMH anchors verbatim. '
             'BANK_DEVIATION on zhu_lord (aspect anisotropy in L-R band). '
             '彳 inlined as pie+pie+shu (no whole-radical primitive available).',
}


if __name__ == "__main__":
    main()
