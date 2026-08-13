"""p3_char_0247_军 — G5 attempt.

Recipe: **P-A-006** — MMH-anchor verbatim + stroke-primitive layer
(refuse whole-radical composition: mi_cover + che_car would double-transform
at Phase-3 aspect, per P-COMP-009).

6 strokes:
  s1 dian (冖 left dot)         : (75.6,73.2)  → (60.9,130.7)
  s2 heng_zhe_short (冖 top)    : (86.4,89.4)  → (204.5,106.9)
      (MMH median is horizontal-only; extend downwards at right for the hook.)
  s3 heng (车 top short)        : (85.3,144.4) → (209.5,130.7)
  s4 pie_zhe (车 top compound)  : head(133.6,97), corner(128.1,143.8),
                                   tail(203.6,191.9)
      — head→corner goes DOWN-LEFT (short pie); corner→tail goes DOWN-RIGHT.
      Corner cell = C, matches joint P(welded) with s3 at (128.1,143.8).
  s5 heng (bottom long)         : (56.2,242.0) → (252.5,235.5)
  s6 shu (central piercer)      : (145.3,163.2) → (154.1,300)  [clip to 300]
"""

import sys
import pathlib
from PIL import Image, ImageDraw

# expose success_bank/code for imports
BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from dian import draw_dian
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short
from pie_zhe import draw_pie_zhe
from shu import draw_shu


SELF_CHECK = {
    "visual_ok": None,
    "stroke_count_ok": True,
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": None,
    "notes": "6 strokes; P-A-006 recipe; s4 = pie_zhe crossing s3 at C(128,144).",
}


def draw_jun(img_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1 — dian (冖 left dot: short, thick-tailed, slight down-left slant)
    draw_dian(d, (75.6, 73.2), (60.9, 130.7),
              w_head=3, w_tail=7, bow=3, steps=48)

    # s2 — heng_zhe_short (冖 top: horizontal + short vertical drop at right)
    draw_heng_zhe_short(d, (86.4, 89.4), (204.5, 118.0),
                        corner_offset=(-4, -4))

    # s3 — heng (车 top short heng)
    draw_heng(d, (85.3, 144.4), (209.5, 130.7),
              width_head=8, width_tail=9)

    # s4 — pie_zhe (车 top compound: head high, corner at C, tail middle-right)
    draw_pie_zhe(d, head=(133.6, 97.0),
                 corner=(128.1, 143.8),
                 tail=(203.6, 191.9),
                 pie_bow=3, zhe_bow=1,
                 w_head=5, w_corner=5, w_tail=4)

    # s5 — heng (bottom long)
    draw_heng(d, (56.2, 242.0), (252.5, 235.5),
              width_head=9, width_tail=11)

    # s6 — shu (central piercer)
    draw_shu(d, (145.3, 163.2), (154.1, 300), width=8)

    img.save(img_path)


if __name__ == "__main__":
    out = pathlib.Path(__file__).parent / "01_军.png"
    draw_jun(out)
    print("saved:", out)
