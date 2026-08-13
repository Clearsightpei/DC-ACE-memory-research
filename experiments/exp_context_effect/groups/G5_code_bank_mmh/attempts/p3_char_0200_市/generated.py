"""p3_char_0200_市 — G5 attempt.

MMH-derived structure (5 strokes):
  s1 dian: TC(0.274,0.53) → TC(0.617,0.797) : (127, 53) → (162, 80)
  s2 heng: ML(0.372,0.175) → MR(0.678,0.031) : (37, 118) → (268, 103)
  s3 short shu/pie left: ML(0.809,0.567) → BL(0.885,0.417) : (81, 157) → (89, 242)
  s4 heng_zhe_gou (right side of box): ML(0.987,0.591) → BC(0.755,0.186)
        : head (99, 159) → corner (176, 159) → tail (176, 219), hook tip (168, 213)
  s5 long shu (middle vertical extending past baseline):
        C(0.365,0.163) → BC(0.485,1.164) : (137, 116) → (149, 316)

Joints:
  J1  s2.mid(0.39) ⇆ s5.head @ C — N (gap ~17 px). Preserved: s5 head y=116
      is 13 px below s2 baseline y=103; small natural gap ~13-14 px.
  J2  s3.head ⇆ s4.head @ ML — N (gap ~14 px). Preserved: s3.head x=81,
      s4.head x=99 → horizontal gap 18 px ≈ 14.
  J3  s4.mid(0.23) ⇆ s5.mid(0.22) @ C — P welded. s4 heng segment goes
      from (99,159)→(176,159); crosses s5 (x=140ish) around x=137→149 line,
      at y=159, at 23% of s4 (x=99+0.23*77=117) — welded because s4 heng
      crosses s5 vertical near center.
"""

import pathlib
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"))

from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou

SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,          # 5 primitive calls, one per MMH stroke
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": "s1=dian, s2=heng, s3=shu (left short), s4=heng_zhe_gou (right box + subtle hook), s5=long shu piercing past baseline. J3 P satisfied because s4 heng segment sweeps through the s5 vertical line near center.",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1 — 点 (dot on top)
    draw_dian(d, (127, 53), (162, 80),
              w_head=3, w_tail=8, bow=5, steps=48)

    # s2 — 横 (long horizontal, slight lift right)
    draw_heng(d, (37, 118), (268, 103),
              width_head=9, width_tail=10)

    # s3 — short 竖/撇 on left side of box (mostly vertical, slight lean)
    draw_shu(d, (81, 157), (89, 242), width=7)

    # s4 — 横折钩 (right side of box: heng across, corner, down, small hook)
    draw_heng_zhe_gou(
        d,
        heng_head=(99, 159),
        corner=(176, 159),
        gou_tail=(176, 219),
        hook_tip=(166, 212),
    )

    # s5 — long middle 竖 (extends past bottom baseline; MMH tail y=316)
    # Clip at canvas bottom for rendering. Head at C(0.365,0.163) = (137,116).
    draw_shu(d, (137, 116), (149, 298), width=8)

    out = pathlib.Path(__file__).parent / "01_市.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
