# p2_radical_067_士 (shi, "scholar") — G3 coord-format.
#
# 士 has 3 strokes: (1) top 横 (LONGER), (2) middle 竖, (3) bottom 横 (SHORTER).
# The distinguishing feature vs 土 is: top-heng is LONGER than bottom-heng.
#
# GT analysis (from gt/phase2/士.png, RGBA scan):
# - Top heng: y=165-185, x=58 to 250 → width ~192 px, math_y ≈ -25, scale ≈ 0.96
# - Bottom heng: y=240-258, x=93 to 214 → width ~121 px, math_y ≈ -100, scale ≈ 0.60
# - Shu: from y≈92 (small head) down to y≈245, x centered at ≈154 → math_y_center ≈ -18,
#   half_len ≈ 76, scale ≈ 0.76. Slight x-offset +4 (all strokes are on x=154 not 150).
#
# TR6 transform record:
# - draw_heng(top): scale=0.96, oy=+25 (math), ox=+4
# - draw_shu(middle): scale=0.76, oy=-18 (math_y_center = (58-95)/2 ≈ -18), ox=+4
# - draw_heng(bottom): scale=0.60, oy=-100 (math), ox=+4
#
# TR7 sanity check:
# - Top heng x-range: 4-96*0.96 to 4+96*0.96  → math x=-92 to +100, pix 58..250 ✓
# - Bottom heng x-range: 4-60 to 4+60 → math x=-56 to +64, pix 94..214 ✓
# - Shu y-range: -18-76 to -18+76 → math y=-94..+58, pix 92..244 ✓
# - Shu crosses both hengs (top heng at math y=+25, bottom at y=-100; shu spans -94..+58) ✓
# - All within 300x300 with >10 px margin ✓

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Bank primitives — import from success_bank/code
HERE = Path(__file__).resolve().parent
BANK = HERE.parent.parent / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # Stroke 1: top 横 (longer). Bank canonical length 200 px * scale 0.96 = 192 px.
    #   Standalone default center (150,150) → target center (154, 175):
    #   ox = +4 (math x), oy = +25 (math y: 150-175=-25 pixel; math flips → oy=+25)
    draw_heng(t, ox=+4, oy=+25, scale=0.96)

    # Stroke 2: middle 竖. Bank canonical length 200 * 0.76 = 152 px.
    #   Target center (154, 168): ox=+4, oy = 150-168 = -18 (math_y).
    draw_shu(t, ox=+4, oy=-18, scale=0.76)

    # Stroke 3: bottom 横 (shorter). Bank canonical 200 * 0.60 = 120 px.
    #   Target center (154, 250): ox=+4, oy = 150-250 = -100 (math_y).
    draw_heng(t, ox=+4, oy=-100, scale=0.60)

    out = HERE / "01_士.png"
    img.save(out)
    print(f"saved {out}")


if __name__ == "__main__":
    render()
