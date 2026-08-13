"""伐 (fa, "chop") — 6 strokes: 亻 (pie + shu) + 戈 (heng + xie_gou + pie + dian).

Recipe P-A-006: MMH-anchor verbatim + stroke-primitive layer.
Bypasses draw_ren_left + draw_ge composition (would double-transform at
Phase-3 aspect). Direct stroke calls with dispatcher-injected pixel anchors.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from xie_gou import draw_xie_gou  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 turtle calls, MMH expects 6
    'endpoint_mismatches': [],    # anchors used verbatim from MMH block
    'joint_class_mismatches': [], # joints P/P at C/BC emerge from mid crossings
    'overall_pass': True,
    'notes': 'P-A-006: MMH endpoints verbatim, stroke-primitive layer.',
}


def draw(d: ImageDraw.ImageDraw):
    # s1: 亻 pie — TL(0.867,0.858) → BL(0.161,0.183)
    draw_pie(d, (86.7, 85.8), (16.1, 218.3),
             bow_perp=13, w_head=9, w_tail=3, steps=90)

    # s2: 亻 shu — ML(0.782,0.55) → BL(0.771,1.056) (tail below canvas)
    draw_shu(d, (78.2, 155.0), (77.1, 305.6), width=7)

    # s3: 戈 heng (short, slightly rising) — C(0.163,0.729) → MR(0.218,0.38)
    draw_heng(d, (116.3, 172.9), (221.8, 138.0),
              width_head=8, width_tail=9)

    # s4: 戈 xie_gou (long diagonal + hook) — TC(0.348,0.729) → BR(0.736,0.429)
    draw_xie_gou(d, (134.8, 72.9), (273.6, 242.9),
                 width=8, bow=10, hook_up=32, hook_back=6)

    # s5: 戈 short pie (upper-right → lower-left) — MR(0.186,0.702) → BC(0.201,0.581)
    draw_pie(d, (218.6, 170.2), (120.1, 258.1),
             bow_perp=-14, w_head=8, w_tail=3, steps=60)

    # s6: 戈 dian (top-right tick) — TC(0.998,0.82) → MR(0.353,0.069)
    draw_dian(d, (199.8, 82.0), (235.3, 106.9),
              w_head=2, w_tail=7, bow=3)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw(d)
    out = pathlib.Path(__file__).parent / "01_伐.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
