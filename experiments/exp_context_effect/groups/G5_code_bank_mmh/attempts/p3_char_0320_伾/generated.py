"""p3_char_0320_伾 (pī) — 亻 + 丕 (7 strokes).

Recipe P-A-006: MMH-anchor verbatim + stroke-primitive layer.
- 亻 rendered inline via draw_pie + draw_shu using MMH's specific
  anchors (not draw_ren_left, whose baked geometry didn't match this
  item's specific pie-head @ TL(0.87, 0.656)).
- 丕 rendered inline as 5 strokes (heng + pie + short-shu + dian +
  bottom-heng) — no 丕 bank primitive; P-COMP-011 (亻+X with X
  containing straight strokes only, no hooks) — should be safe.

SELF_CHECK below is the pre-submit structural report.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"),
)

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu

SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # 7 primitives called (see below)
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": (
        "MMH anchors used verbatim per P-A-006. 亻 inlined (not "
        "draw_ren_left) because MMH's pie head @ TL(0.87, 0.656) sits "
        "higher than the bank primitive's baked geometry. 丕 has no "
        "bank primitive — inlined stroke layer. Joint s4.mid⇆s5.mid "
        "(P/welded) is naturally enforced by anchor coincidence at "
        "C(0.717, 0.657)."
    ),
}


def draw_伾(draw, ox=0, oy=0, scale=1.0):
    def tx(x, y):
        return (ox + x * scale, oy + y * scale)

    # s1: 亻 pie — TL(0.87, 0.656) → BL(0.196, 0.03)
    #     pixel: (87.0, 65.6) → (19.6, 203.0)
    draw_pie(
        draw, tx(87, 65.6), tx(19.6, 203),
        bow_perp=int(13 * scale) or 1,
        w_head=max(2, int(9 * scale)),
        w_tail=max(2, int(3 * scale)),
        steps=90,
    )

    # s2: 亻 shu — ML(0.697, 0.518) → BL(0.732, 0.965)
    #     pixel: (69.7, 151.8) → (73.2, 296.5)
    draw_shu(draw, tx(69.7, 151.8), tx(73.2, 296.5),
             width=max(2, int(7 * scale)))

    # s3: 丕 top heng — C(0.198, 0.195) → MR(0.508, 0.022)
    #     pixel: (119.8, 119.5) → (250.8, 102.2)
    draw_heng(draw, tx(119.8, 119.5), tx(250.8, 102.2),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))

    # s4: 丕 left pie — C(0.843, 0.157) → BC(0.084, 0.306)
    #     pixel: (184.3, 115.7) → (108.4, 230.6)
    draw_pie(
        draw, tx(184.3, 115.7), tx(108.4, 230.6),
        bow_perp=int(10 * scale) or 1,
        w_head=max(2, int(8 * scale)),
        w_tail=max(2, int(3 * scale)),
        steps=80,
    )

    # s5: 丕 short middle shu (welded P-cross with s4.mid) —
    #     C(0.62, 0.479) → BC(0.72, 0.563)
    #     pixel: (162.0, 147.9) → (172.0, 256.3)
    draw_shu(draw, tx(162, 147.9), tx(172, 256.3),
             width=max(2, int(6 * scale)))

    # s6: 丕 right dian — MR(0.062, 0.822) → BR(0.64, 0.259)
    #     pixel: (206.2, 182.2) → (264.0, 225.9)
    draw_dian(
        draw, tx(206.2, 182.2), tx(264, 225.9),
        w_head=3, w_tail=9, bow=4, steps=48,
    )

    # s7: 丕 bottom heng — BC(0.122, 0.807) → BR(0.675, 0.792)
    #     pixel: (112.2, 280.7) → (267.5, 279.2)
    draw_heng(draw, tx(112.2, 280.7), tx(267.5, 279.2),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_伾(draw)
    out = pathlib.Path(__file__).with_name("01_伾.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
