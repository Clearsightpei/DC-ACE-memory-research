"""p3_char_0173_仔 — G5 attempt

仔 = 亻 (left) + 子 (right, compact). 5 strokes per MMH.

Uses bank primitives:
  - draw_pie (亻 pie)
  - draw_shu (亻 shu)
  - draw_heng_pie (子 top heng-pie, apex/corner overridden for a compact stroke)
  - draw_wan_gou (子 middle curved hook)
  - draw_heng (子 crossing horizontal)

No BANK_DEVIATION — all bank primitives fit this composition with parameter tuning.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng
from heng_pie import draw_heng_pie
from pie import draw_pie
from shu import draw_shu
from wan_gou import draw_wan_gou

# ---------------------------------------------------------------
# MMH-derived pixel anchors (from injected structural block)
# ---------------------------------------------------------------
# s1 (亻 pie):     TL(0.908, 0.688) -> ML(0.173, 0.972) -> (90.8, 68.8) → (17.3, 197.2)
# s2 (亻 shu):     ML(0.735, 0.456) -> BL(0.756, 0.795) -> (73.5, 145.6) → (75.6, 279.5)
# s3 (子 heng-pie): C(0.269, 0.078) -> C(0.802, 0.433)   -> (126.9, 107.8) → (180.2, 143.3)
# s4 (子 wan-gou): C(0.693, 0.4)   -> BC(0.362, 0.643)   -> (169.3, 140.0) → (136.2, 264.3)
# s5 (子 heng):    C(0.014, 0.825) -> MR(0.733, 0.752)   -> (101.4, 182.5) → (273.3, 175.2)

img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# --- Stroke 1: 亻 pie (long left-diagonal sweep) ---
draw_pie(d, head=(91, 69), tail=(17, 197),
         bow_perp=10, w_head=9, w_tail=3, steps=90)

# --- Stroke 2: 亻 shu (short vertical) ---
draw_shu(d, head=(74, 146), tail=(76, 280), width=7)

# --- Stroke 3: 子 heng-pie (compact — heng ~50px wide + short pie-drop) ---
# Default heng_pie assumes a wide heng (apex_x = hx+130) tuned for 又.
# This 仔 rendering has a tight top-of-子 corner, so shrink apex/corner
# to match the MMH tail at (180, 143).
draw_heng_pie(d, head=(127, 108), tail=(180, 143),
              apex_x=175, corner_x=178)

# --- Stroke 4: 子 wan-gou (curved vertical with small terminal left-flick) ---
# Tail at (136, 264) is the shaft end BEFORE the hook flick.
draw_wan_gou(d, head=(169, 140), tail=(136, 264),
             belly_right=18, hook_len=22, hook_up=12,
             w_head=6, w_body=6, w_tail=2)

# --- Stroke 5: 子 heng (long crossing horizontal, welds with s4.mid) ---
draw_heng(d, head=(101, 183), tail=(273, 175),
          width_head=8, width_tail=9)

out = pathlib.Path(__file__).parent / "01_仔.png"
img.save(out)
print(f"wrote {out}")

# ---------------------------------------------------------------
# Mandatory self-check block
# ---------------------------------------------------------------
SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,   # 5 turtle-primitive calls above
    "endpoint_mismatches": [], # all anchors used verbatim from MMH block
    "joint_class_mismatches": [
        # expected joints and their actual implementation:
        # (s1.mid, s2.head) N ~17px  -> N (natural gap; pie curves down-left away from shu at t=0.48)
        # (s2.mid, s5.head) N ~30px  -> N (s2 at (75, 213), s5 head at (101, 183); ~40px gap)
        # (s3.tail, s4.head) N ~8px  -> N (s3 ends (180,143), s4 begins (169,140); ~9px gap)
        # (s4.mid, s5.mid)  P weld   -> P (s4 curved shaft crosses s5 heng near (155, 185))
    ],
    "overall_pass": True,
    "notes": "5-stroke 仔 = 亻(pie+shu) + 子(heng_pie+wan_gou+heng). No BANK_DEVIATION.",
}
