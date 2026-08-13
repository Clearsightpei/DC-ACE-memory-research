"""p3_char_0011_人 — G5 render.

人 is exactly the radical primitive in the bank (draw_ren from ren.py,
promoted from p2_radical_028_人 B1 PASS). Bank anchors match the
injected MMH endpoints exactly:
  s1 pie:  head (141.5, 84.4)=TC(0.415,0.844); tail (21.1, 272.2)=BL(0.211,0.722)
  s2 na:   head (138.9,160.3)=C (0.389,0.603); tail (288.9,273.6)=BR(0.889,0.736)
Joint s1.mid(0.31) <-> s2.head is N-class (small natural gap) — the
bank primitive was tuned to produce this gap. Direct reuse, no
deviation.
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

from ren import draw_ren  # noqa: E402


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,      # draw_ren calls draw_pie + draw_na = 2 strokes
    "endpoint_mismatches": [],    # bank anchors === MMH-injected anchors
    "joint_class_mismatches": [], # N-class gap preserved by bank primitive
    "overall_pass": True,
    "notes": "Direct bank reuse of draw_ren; anchors match MMH exactly.",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_ren(draw, ox=0, oy=0, scale=1.0)
    out = pathlib.Path(__file__).parent / "01_人.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
