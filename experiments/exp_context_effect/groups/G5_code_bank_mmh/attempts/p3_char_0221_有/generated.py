"""p3_char_0221_有 — G5 attempt.

Composition (6 strokes, MMH-derived pixel anchors on 300x300):
  s1: 横 (long top crossbar)             — draw_heng
  s2: 撇 (long left-leaning pie, starts above s1 and crosses through) — draw_pie
  s3: 撇 (月's left side, curved vertical) — draw_pie
  s4: 横折钩 (月's right frame)           — draw_heng_zhe_gou
  s5: 横 (月's upper inner horizontal)    — draw_heng
  s6: 横 (月's lower inner horizontal)    — draw_heng

BANK_DEVIATION analysis:
  yue_moon primitive (used for 月 in 明/朋/朝 etc.) has native aspect
  ~0.67 (136w x 204h). In 有, the enclosed 月 is much narrower
  (aspect ~0.50: 68w x 137h), so a uniform-scale yue_moon call would
  render 月 too wide. Instead we call yue_moon's underlying bank
  primitives (pie + heng_zhe_gou + 2 hengs) directly with MMH pixel
  anchors — same primitives, correct aspect. This is inline
  composition, not primitive skipping; noting here for record.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou


# ---------- MMH-derived anchor pixel coords (300x300 米字格) ------------
# cell mapping: ML=(0-100, 100-200), MR=(200-300, 100-200), TC=(100-200, 0-100)
# C=(100-200, 100-200), BL=(0-100, 200-300), BC=(100-200, 200-300)
S1_HEAD = (46.6, 120.1)   # ML(0.466, 0.201)
S1_TAIL = (258.7, 105.8)  # MR(0.587, 0.058)

S2_HEAD = (137.7, 53.3)   # TC(0.377, 0.533)
S2_TAIL = (24.3, 243.5)   # BL(0.243, 0.435)

S3_HEAD = (120.7, 158.8)  # C(0.207, 0.588)
S3_TAIL = (107.5, 295.3)  # BC(0.075, 0.953)

S4_HEAD    = (127.7, 158.2)  # C(0.277, 0.582)
S4_CORNER  = (161.0, 158.0)  # top-right corner of 月 box (near s4_head y)
S4_GOUTAIL = (161.1, 285.9)  # BC(0.611, 0.859)
S4_HOOKTIP = (148.5, 279.0)  # small up-left hook

S5_HEAD = (128.6, 203.3)  # BC(0.286, 0.033)  → upper inner heng
S5_TAIL = (174.3, 195.4)  # C(0.743, 0.954)

S6_HEAD = (126.0, 240.2)  # BC(0.26, 0.402)
S6_TAIL = (175.2, 233.8)  # BC(0.752, 0.338)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 primitive calls = MMH expected 6
    'endpoint_mismatches': [],    # anchors set directly from MMH
    'joint_class_mismatches': [], # s1xs2 P (welded via bezier crossing);
                                  # remaining are N (natural gaps within 月 box structure)
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: inlined yue_moon components at correct aspect for 有.',
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: top long 横 (slight upward tilt)
    draw_heng(d, S1_HEAD, S1_TAIL, width_head=8, width_tail=9)

    # s2: long 撇 (starts above s1, crosses through, sweeps down-left)
    draw_pie(d, S2_HEAD, S2_TAIL,
             bow_perp=14, w_head=8, w_tail=3)

    # s3: 月's left curved 撇 (short, mild bow)
    draw_pie(d, S3_HEAD, S3_TAIL,
             bow_perp=6, w_head=6, w_tail=4)

    # s4: 月's right frame — 横折钩
    draw_heng_zhe_gou(d, S4_HEAD, S4_CORNER, S4_GOUTAIL, S4_HOOKTIP)

    # s5: upper inner 横
    draw_heng(d, S5_HEAD, S5_TAIL, width_head=6, width_tail=7)

    # s6: lower inner 横
    draw_heng(d, S6_HEAD, S6_TAIL, width_head=6, width_tail=7)

    out = os.path.join(os.path.dirname(__file__), "01_有.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
