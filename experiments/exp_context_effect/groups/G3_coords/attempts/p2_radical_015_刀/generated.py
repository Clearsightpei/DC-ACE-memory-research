# p2_radical_015_刀 — G3 attempt
#
# 刀 = 2 strokes:
#   (1) 横折钩 top: horizontal then turn down (right side) with small hook up-left at base
#   (2) 撇: starts near top-left of horizontal, sweeps down-left past the bottom-left
#
# Bank primitives used (with deliberate TR-compliant transforms):
#   - heng_zhe_gou: draws 横+折+钩. Standalone spans x∈[-90,+80], y∈[-70,+60] in math coords.
#     For 刀, the top-horizontal is fairly compact (~90 px wide) starting a bit left of center,
#     turning down to form the right side, hook at bottom. We shift right (ox=+10) and up (oy=+5),
#     scale=0.55 to shrink the standalone stroke to radical-position size (TR2: enclosing-ish
#     but small radical shape ~0.55).
#     Center of standalone hzg is roughly (-5, -5); we want its geometric center near canvas (155, 145)
#     i.e. math (+5, +5). ox=+10, oy=+10, scale=0.55.
#   - pie: standalone spans (65,90) head to (-45,-85) tail. For 刀's second stroke, the pie head
#     starts at the top横 near its left-middle (~math (-20, +35)) and tail extends to below the
#     bottom of the character (~math (-55, -95)). Head-to-tail vector is (-35, -130), roughly
#     3x larger than a pie's default (-110, -175). Actually pie default vector is (-110, -175),
#     length ~207 at scale 1.0. We want length ~135 → scale ≈ 0.65.
#     At scale 0.65: head at (42, 58), tail at (-29, -55). We want head at (~-20, +35), so
#     ox = -20 - 42 = -62, oy = 35 - 58 = -23. Then tail lands at (-91, -78) — a bit too far left.
#     Adjust: ox = -50, oy = -25, scale = 0.65. Head (42*.65=27) → -50+27=-23, oy 58*.65=38 → +13.
#     Tail (-45*.65=-29) → -79, oy (-85*.65)=-55 → -80. Head canvas (127, 137), tail (71, 230).
#     That places head touching left end of horizontal, tail past bottom-left. Good.

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie


def render(path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: 横折钩 — top+right of 刀. Shift right & up slightly, shrink to 0.55.
    # Standalone hzg: horiz from (-90,60) to (80,60), then down to (80,-70), then hook up-left.
    # Scaled 0.55: horiz (-50,33) to (44,33), down to (44,-38), hook flicking up-left from (44,-38).
    # With ox=+10, oy=+10: horiz canvas (110,107) to (204,107), down to (204,178), hook to (~192,190).
    # That gives a top横 spanning x=110..204 at y≈107, and right vertical from (204,107) to (204,178).
    draw_heng_zhe_gou(draw, ox=+10, oy=+10, scale=0.55)

    # Stroke 2: 撇 — head touches the LEFT-END of the top横 (canvas ~115,110),
    # sweeps down-left past the bottom-left. Revised from first pass where head was
    # 30px right of the horizontal start, leaving a visible gap.
    # Scale 0.6, ox=-69, oy=-16:
    #   head math (-69+65*.6, -16+90*.6) = (-30, 38) → canvas (120, 112) — meets 横's left end
    #   tail math (-69-45*.6, -16-85*.6) = (-96, -67) → canvas (54, 217) — extends past bottom-left
    draw_pie(draw, ox=-69, oy=-16, scale=0.6)

    img.save(path)
    return path


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_刀.png")
    render(out)
    print("Wrote", out)
