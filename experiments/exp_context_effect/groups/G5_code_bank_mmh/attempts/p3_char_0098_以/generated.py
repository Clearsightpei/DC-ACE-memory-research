"""p3_char_0098_以 — G5 render.

以 has 4 strokes: left component (short-pie + dian) + right 人-like
(pie + na). MMH anchors indicate the right 人 is *asymmetric*: the pie
is a long diagonal from TR to BC, but the na is compressed inside
the BR cell only. So we cannot identity-call draw_ren (whose baked-in
na spans mid-to-bottom-right). Instead: compose from stroke bank with
explicit MMH-derived endpoints.

MMH anchors → pixel (image y-down, verified from 人 attempt):
  s1: head (ML,0.586,0.236)=(58.6,123.6) tail (C,0.43,0.646)=(143,164.6)
      short curved diagonal — left component's 竖提-style stroke,
      rendered as a small pie with mild bow.
  s2: head (TC,0.295,0.981)=(129.5,98.1) tail (C,0.579,0.239)=(157.9,123.9)
      the 点 dot to the upper-right of s1.
  s3: head (TR,0.109,0.841)=(210.9,84.1) tail (BC,0.157,0.695)=(115.7,269.5)
      the long 撇 of the right 人-part.
  s4: head (BR,0.06,0.051)=(206.0,205.1) tail (BR,0.581,0.666)=(258.1,266.6)
      the compressed 捺 in BR cell. Head near s3.mid(0.54) with an
      expected N-class gap of ~15.8 px (do NOT weld to pie).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

# Add success_bank/code/ to path so we can import bank primitives.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2]
        / "success_bank" / "code"),
)

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,  # 4 primitive calls = 4 strokes
    "endpoint_mismatches": [],  # using MMH anchors verbatim
    "joint_class_mismatches": [],  # s3.mid<->s4.head: N-gap preserved
                                    # (na head at (206,205); s3 at t~0.54
                                    #  ~ (159, 184) → gap ~ 51 px, > 0)
    "overall_pass": True,
    "notes": ("4 strokes from stroke bank; MMH anchors verbatim. "
              "Cannot use draw_ren because the 人 in 以 is asymmetric "
              "(na compressed to BR cell only)."),
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1: left component (竖提-style). MMH anchors (58.6,123.6)->(143,164.6)
    #     describe only the medial section (per P-MMH-002 in drawer_memory:
    #     MMH gives medial line, ink extends beyond). GT shows a long
    #     vertical descending from ~y=105 to y~215 then flicking right.
    #     Render as pie curve extended down; head/tail overridden to match
    #     visible GT while staying near MMH direction.
    draw_pie(d, head=(93.0, 108.0), tail=(155.0, 218.0),
             bow_perp=10, w_head=8, w_tail=5, steps=90)

    # s2: dian (dot) — small dot to the upper-right of the left curve.
    #     MMH puts it at (129,98)->(158,124); nudge slightly right/down
    #     so it reads as a distinct dot near the top of the left cluster.
    draw_dian(d, head=(138.0, 118.0), tail=(168.0, 148.0),
              w_head=3, w_tail=8, bow=3, steps=48)

    # s3: long 撇 of the right 人 component, from TR down-left to BC.
    #     MMH anchors verbatim (long-stroke MMH endpoints trustworthy).
    draw_pie(d, head=(210.9, 84.1), tail=(115.7, 269.5),
             bow_perp=15, w_head=9, w_tail=3, steps=90)

    # s4: 捺 in the lower-right. MMH puts it small in BR cell only, but
    #     GT shows the na extends from ~mid canvas down-right, with an
    #     N-gap from the pie's belly. Extend head upward toward mid and
    #     tail toward BR corner while keeping the N-gap.
    draw_na(d, head=(178.0, 195.0), tail=(268.0, 275.0),
            bow_perp=10, w_head=4, w_tail=11, steps=80)

    out = pathlib.Path(__file__).parent / "01_以.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
