"""p3_char_0490_俘 — G5 attempt

俘 = 亻 (left, 2 strokes) + 孚 (right, 7 strokes: 爫 top 4 + 子 bottom 3).
Total 9 strokes per MMH.

Per-sub-component reasoning trace (P-A-008):

  [1] 亻 left: bank draw_ren_left native footprint W=78 H=219 AR=0.356.
      Target from MMH anchors (300x300 cell decode):
        s1 head TL(.861,.636)=(86,64), tail ML(.185,.89)=(19,189)
        s2 head ML(.688,.427)=(69,143), tail BL(.732,.801)=(73,280)
      Target W=68 H=216 AR=0.315.
      AR ratio 0.315/0.356 = 0.88 (within P-A-007-v2 [0.55, 1.2] band).
      Uniform scale ~0.94 → whole-radical BANK, no DEVIATION.

  [2] 爫 top: bank draw_zhao_claw_top native W=122 H=71 AR=1.72.
      Target from MMH (s3..s6):
        s3 head TR(.057,.715)=(206,72), tail TC(.283,.908)=(128,91)
        s4 (leftmost dian) C(.184,.131)=(118,113) → C(.412,.354)=(141,135)
        s5 (middle dian)   C(.556,.008)=(156,101) → C(.737,.198)=(174,120)
        s6 head TR(.244,.85)=(224,85), tail C(.907,.28)=(191,128)
      Target W=106 H=63 AR=1.68.
      AR ratio 1.68/1.72 = 0.98 (basically identical).
      Uniform scale ~0.87 → whole-radical BANK, no DEVIATION.

  [3] 子 bottom: no whole-radical zi_child bank primitive exists.
      Inline via draw_heng_pie + draw_wan_gou + draw_heng at MMH anchors
      (same pattern as p3_char_0173_仔 PASS attempt).
      No BANK_DEVIATION comment needed — inlining because bank has no
      corresponding whole-radical entry, not because a bank entry
      was skipped.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK_DIR))

from ren_left import draw_ren_left       # noqa: E402
from zhao_claw_top import draw_zhao_claw_top  # noqa: E402
from heng_pie import draw_heng_pie       # noqa: E402
from wan_gou import draw_wan_gou         # noqa: E402
from heng import draw_heng               # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,     # 2 (亻) + 4 (爫) + 3 (子) = 9 ✓
    "endpoint_mismatches": [],   # bank primitives cover 6 strokes; 3 inline at MMH pts
    "joint_class_mismatches": [
        # s1.mid ⇆ s2.head : N (natural gap from ren_left spacing)
        # s2.mid ⇆ s9.head : N (s9 heng crosses at right, s2 shu bottom is separate)
        # s3.tail ⇆ s4.head : N (dian s4 sits below s3 tail)
        # s3.tail ⇆ s5.head : N (dian s5 sits below s3)
        # s3.head ⇆ s6.head : N (both start upper-right region, natural gap)
        # s4.tail ⇆ s7.mid  : N (爫 leftmost dian above 子 top-curve)
        # s5.tail ⇆ s6.tail : N (爫 middle dian near right pie's foot)
        # s6.tail ⇆ s7.mid  : N (爫 right foot above 子 top-curve)
        # s7.tail ⇆ s8.head : N (子 top ends near where wan_gou begins)
        # s7.tail ⇆ s9.mid  : N (子 top-curve near heng-crossing at right)
        # s8.mid(0.16) ⇆ s9.mid(0.47) : P (wan_gou vertical crosses heng — welded)
    ],
    "overall_pass": True,
    "notes": (
        "亻 bank whole-radical scale=0.94; 爫 bank whole-radical scale=0.87; "
        "子 inline (no whole-radical bank entry) at MMH anchors."
    ),
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 (strokes 1-2) via bank ---------------------------------------
    # Native s1_tail (80.6, 211.2) at scale 0.94 → (75.8, 198.5).
    # Want s1_tail at target (19, 189) → ox=-56.8, oy=-9.5.
    draw_ren_left(d, ox=-57, oy=-10, scale=0.94)

    # ---- 爫 (strokes 3-6) via bank ---------------------------------------
    # Native s1_head (189.3, 56.2) at scale 0.87 → (164.7, 48.9).
    # Want s3 head (target for 俘) at (206, 72) → ox=41.3, oy=23.1.
    draw_zhao_claw_top(d, ox=41, oy=23, scale=0.87)

    # ---- 子 (strokes 7-9) inline at MMH endpoints ------------------------
    # s7: 子 top heng-pie-gou. Compact; apex/corner overrides tuned as in 仔.
    draw_heng_pie(d, head=(125, 155), tail=(177, 188),
                  apex_x=173, corner_x=176)

    # s8: 子 wan-gou (curved vertical + terminal hook left-flick).
    # Tail at (138, 282) is the shaft end before the hook flick.
    draw_wan_gou(d, head=(162, 189), tail=(138, 282),
                 belly_right=16, hook_len=22, hook_up=12,
                 w_head=6, w_body=6, w_tail=2)

    # s9: 子 heng (long horizontal, welds with s8 shaft — P joint).
    draw_heng(d, head=(91, 214), tail=(278, 202),
              width_head=8, width_tail=9)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_俘.png",
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
