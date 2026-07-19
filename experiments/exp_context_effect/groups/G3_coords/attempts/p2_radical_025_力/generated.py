# p2_radical_025_力 — G3 coord-bank rendering.
#
# 力 = 2 strokes:
#   Stroke 1: 横折钩 (top-horizontal → turn down → hook up-left at base)
#   Stroke 2: 撇 (left-falling sweep starting from the top horizontal ~40% right,
#                 descending down-left to bottom).
#
# GT observation:
#   - Top horizontal spans about the middle-upper region, moderately narrow.
#   - Corner is a soft/small 顿笔; the descender bows slightly leftward
#     then flicks a short hook up-and-left at the base.
#   - The 撇 starts on the top horizontal (about ~40-50% from its left),
#     descends and terminates at the bottom-left area.
#
# Bank fit analysis (TR1/TR5):
#   - success_bank/heng_zhe_gou.py MATCHES stroke 1's shape idiom, but the
#     canonical primitive spans x∈[-90, +80] which is wider than 力's top
#     horizontal (which reads shorter — top width ~100 px, corner drops
#     ~135 px). Also stroke 1 in 力 shifts up-right relative to canvas.
#     → USE heng_zhe_gou with scale=0.75, ox=+5, oy=+15 (deliberate placement,
#     not default; TR6-compliant).
#   - success_bank/pie.py MATCHES stroke 2's idiom but the canonical
#     endpoints (65,90)→(-45,-85) start from far upper-right. In 力 the
#     撇 should start on the top horizontal (near x≈0, y≈+50 math-coords)
#     and end at (~-55, -110). The default primitive begins too far right
#     and slightly too short. Use scale=0.90 with ox=-38, oy=+10 so the
#     head lands near the top horizontal and the tail extends past the
#     hook to bottom-left. Verified numerically below.
#
# TR4 joint check: stroke-2's head at scale=0.90, ox=-38, oy=+10:
#   head math-coords = (65*0.90 + (-38), 90*0.90 + 10) = (20.5, 91.0)
#   → PIL pixel = (150+20.5, 150-91) = (170.5, 59). That is too high; adjust.
#   Better: scale=0.85, ox=-45, oy=-2:
#     head = (65*0.85 - 45, 90*0.85 - 2) = (10.25, 74.5) → PIL (160, 75.5).
#     Top horizontal (from stroke 1 at scale 0.75, oy shift +15):
#       heng runs y=60*0.75+15 = 60 → PIL y = 150-60 = 90.
#     Head is ABOVE the horizontal by ~15 px — not on it. Not right.
#   Better: scale=0.75, ox=-52, oy=-15:
#     head = (65*0.75 - 52, 90*0.75 - 15) = (-3.25, 52.5) → PIL (147, 97.5).
#     Top-horizontal y=90 (from stroke 1). Head at PIL y≈97 → head sits
#     just below the horizontal (crossing/touching). GOOD.
#     tail = (-45*0.75 - 52, -85*0.75 - 15) = (-85.75, -78.75)
#       → PIL (64, 228.75). Bottom-left. GOOD.
#
# Final choice: heng_zhe_gou(scale=0.75, ox=+5, oy=+15) + pie(scale=0.75, ox=-52, oy=-15).

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # REVISION 1 rationale (self-check vs GT):
    #   - Pass 1 was too high on canvas and too wide. GT centers the
    #     character mid-canvas with the top horizontal at ~PIL y=115.
    #   - 撇 was too short and didn't start on the horizontal.
    #   - Hook was barely visible.
    #
    # New placement:
    #   heng_zhe_gou at scale=0.70, ox=-5, oy=-15:
    #     top horizontal y = 60*0.70 - 15 = 27 (math) → PIL y = 123. GOOD.
    #     top horizontal x: -90*0.70 - 5 = -68 → PIL 82, to 80*0.70 - 5 = 51
    #       → PIL 201. Width ~120 px. GOOD (GT ~110-130 px).
    #     corner PIL (201, 123). Descender to (80*0.70, -70*0.70) + offsets
    #       = (51, -64) → PIL (201, 214). Descender ~90 px tall. GOOD.
    #     hook tip: (80-22)*0.70 - 5 = 35.6, (-70+22)*0.70 - 15 = -48.6
    #       → PIL (186, 199). Small up-left flick from base (201,214). GOOD.
    #   pie at scale=0.80, ox=-50, oy=-25:
    #     head: 65*0.80 - 50 = 2, 90*0.80 - 25 = 47 (math) → PIL (152, 103).
    #       Top horizontal PIL y=123. Head slightly above horizontal —
    #       need to lower head onto horizontal. Adjust oy=-35:
    #       head y = 72 - 35 = 37 → PIL 113. Still ~10 above. Try oy=-45:
    #       head y = 27 → PIL 123. On horizontal. GOOD.
    #     head x with ox=-45: 65*0.80 - 45 = 7 → PIL 157. On horizontal
    #       (which runs PIL 82→201), sits at ~40% from left of horizontal. GOOD.
    #     tail: -45*0.80 - 45 = -81, -85*0.80 - 45 = -113 (math)
    #       → PIL (69, 263). Bottom-left. Descends past hook baseline. GOOD.
    draw_heng_zhe_gou(d, ox=-5, oy=-15, scale=0.70)
    draw_pie(d, ox=-45, oy=-45, scale=0.80)

    out = Path(__file__).parent / "01_力.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
