# p2_radical_106_牛 — G3 attempt.
# 牛 (ox, 4 strokes): a short 撇 (top-left, tapering down toward the shaft),
# a short upper 横 (right of the pie's tail), a long middle 横 (widest),
# and a long central 竖 that runs from just above the upper heng down to
# the bottom, crossing both hengs.
#
# Structure (math coords, +y up, center origin):
#   Stroke 1 — pie: starts high-center-ish (~+0, +90), curves down-left
#              to tail around (-55, +30). Short, near-vertical scoop.
#   Stroke 2 — upper heng: short (~65 px wide), centered around (+15, +45).
#   Stroke 3 — middle heng: long (~180 px wide), centered around (+10, 0).
#              Widest stroke, spans the character.
#   Stroke 4 — shu: long vertical, top at ~(+3, +75), bottom at (+3, -110).
#              Crosses both hengs cleanly.
#
# TR-notes:
# - draw_heng scales: upper heng scale 0.325 (~65 px), middle heng scale 0.9 (~180 px). TR2 (top radical / component).
# - draw_shu scale 0.925 taller-than-standalone would over-run canvas;
#   use 0.925 with offset oy=-17.5 to shift downward so shaft extends
#   from y=+75 down to y=-110 (length ~185 px).
# - draw_pie tail-only, small (scale 0.55): pie's canonical head is at
#   (+65,+90) tail at (-45,-85) — scaling 0.55 gives head (+35,+50),
#   tail (-25,-47). To place tail at ~(-55,+30) we need
#   ox = -55 - (-25) = -30, oy = +30 - (-47) = +77. Head then at
#   (-30+35, +77+50) = (+5, +127) — a bit high, acceptable as the pie
#   head sits above the upper heng.
# - Alt: inline a shorter, less-bowed pie for tighter fit — the primitive
#   at 0.55 flattens fine (TR8 test: 撇 shape is well-matched, uniform scale ok).

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng   # noqa: E402
from shu import draw_shu     # noqa: E402
from pie import draw_pie     # noqa: E402


def render(out_path):
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # Stroke 1 — 撇 (pie): short, tapering down-left toward the shaft.
    # Revision: first attempt's pie head extended too high (above the top
    # crown of the character). GT shows pie head only slightly above the
    # upper heng, then descending diagonally to a tail well left of the
    # shaft near the middle heng level. Use scale 0.45 and lower origin.
    # scale 0.45: canonical head (65,90)→(+29,+40), tail (-45,-85)→(-20,-38).
    # Target tail ~(-45, +5), target head ~(+5, +75).
    # ox = -45 - (-20) = -25, oy = +5 - (-38) = +43. Head lands at
    # (-25+29, +43+40) = (+4, +83) — slightly above upper heng ✓.
    draw_pie(t, ox=-25, oy=+43, scale=0.45)

    # Stroke 2 — short upper 横 (heng): width ~65 px, y ~ +45.
    # heng canonical length 200; scale 0.325 → 65 px. Center at (+15, +45).
    draw_heng(t, ox=+15, oy=+45, scale=0.325)

    # Stroke 3 — long middle 横 (heng): width ~180 px, y ~ 0.
    # scale 0.9 → 180 px. Slightly right of center: ox=+10, oy=0.
    draw_heng(t, ox=+10, oy=0, scale=0.9)

    # Stroke 4 — 竖 (shu): shaft from top (~y=+75) down to bottom (~y=-110).
    # Length 185 px → scale 0.925. Half-len 92.5. Center oy = (+75 + -110)/2 = -17.5.
    # ox = +3 (near center, slight right bias matching hengs).
    draw_shu(t, ox=+3, oy=-17.5, scale=0.925)

    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_牛.png")
    render(out)
    print(f"wrote {out}")
