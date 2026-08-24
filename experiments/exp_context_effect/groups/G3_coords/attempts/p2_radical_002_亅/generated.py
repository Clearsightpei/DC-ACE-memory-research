"""p2_radical_002_亅 — G3 coord-bank Drawer.

亅 is orthographically identical to 竖钩 (shu_gou) — a vertical shaft
with an up-and-left hook at the bottom (P7: radicals-are-strokes reuse
rule). GT inspection: shaft is centered slightly to the RIGHT of canvas
center (~x=175/300) and slightly SHORTER than the standalone shu_gou
default (GT shaft ~y=90..225 pixels → ~135 px tall vs the primitive's
180 px canonical).

TR1-TR7 transform derivation:
- Standalone shu_gou default center: (150, 150) canvas pixels,
  shaft height 180 px (half_len=90 math units), thickness 12 px.
- Target center in canvas pixels: (~178, ~158) from GT visual read.
- ox = 178 - 150 = +28 (canvas px right shift).
- oy in math coords: primitive center is at canvas (150,150) which
  maps to (ox=0, oy=0). Target center canvas (~158) is 8 px below
  canvas center → math oy = -8.
- Scale: GT shaft ~135 px vs canonical 180 px → scale ≈ 0.75.
  scale=0.75 keeps thickness at ~9 px which reads calligraphic.
- Hook at bottom flicks up-and-left ~25*0.75 ≈ 19 px, matching GT.

Eyeball sanity (TR7):
- Shaft top: (178, 158-67) = (178, 91). Bottom: (178, 158+67) = (178, 225).
- Hook tip: (178 - 19, 225 - 16) = (159, 209). Reads as an up-left flick.
- All within 300x300 with >10px margin.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Bank primitive import
BANK_CODE = Path(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G3_coords/success_bank/code"
)
sys.path.insert(0, str(BANK_CODE))
from shu_gou import draw_shu_gou  # noqa: E402


OUT = Path(__file__).parent / "01_亅.png"


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # 亅 = shu_gou, right-shifted, near-full scale to match GT weight.
    # Self-check pass 1 → hook read fine but shaft was too thin/short vs GT.
    # Revision: scale 0.75 → 0.85 (shaft height 180*0.85 = 153 px, thickness
    # ~10 px), ox slightly reduced to +22 since GT shaft center was ~x=175,
    # oy=-5 for center around canvas y=155.
    draw_shu_gou(t, ox=+22, oy=-5, scale=0.85)

    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
