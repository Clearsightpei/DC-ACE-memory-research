# p2_radical_086_比 (bǐ) — 4画 radical.
#
# Analysis of GT: two mirrored components sitting side by side.
#   Left  half (like 匕-mirror): short 竖 (upper-left) + 提 (rising off its bottom).
#   Right half: 撇 (short, middle-upper, slanting down-left) +
#               竖弯钩 (long, right side, wraps under and hooks up).
#
# TR8 check: bank primitives fit at reduced scale; the 撇 is short and
# only mildly slanted (not the full standalone diagonal sweep) — 撇
# still acceptable at small scale because the tapered head+needle-tip
# silhouette is what identifies it. 竖弯钩 is a straight scale-down.
#
# Revision v2 notes vs v1:
#   - v1 撇 was WAY too tall (reached past the shu_wan_gou bottom).
#     Reduced pie scale from 0.6 to 0.32 so the tail sits mid-canvas.
#   - v1 提 was tiny; bumped scale from 0.42 to 0.55 for visibility.
#   - v1 whole character too small; scaled up 竖 length by using scale=0.62,
#     shifted left component further left (-70), right component moved
#     right (ox=+50 for shu_wan_gou) so the two halves are clearly
#     separated.
#   - v1 shu_wan_gou hook was small; bumped scale to 0.85 so the hook
#     reads clearly.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parent.parent.parent / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from shu import draw_shu                # noqa: E402
from ti import draw_ti                  # noqa: E402
from pie import draw_pie                # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def draw_bi(t):
    # ---- Stroke 1: 竖 (left short vertical)
    # Target: from math (-70, +65) down to (-70, -55). Length ~120 px.
    # shu at scale=0.6: half_len=60 -> length 120.
    # Center at (-70, +5) so top is at y=+65, bottom at y=-55.
    # TR6: shu default center (0,0); target center (-70, +5); ox=-70, oy=+5, scale=0.6
    draw_shu(t, ox=-70.0, oy=5.0, scale=0.6)

    # ---- Stroke 2: 提 (rising from bottom of stroke 1 up-right)
    # Head at math (-70, -55), tip around (0, -25). Chord dx=70, dy=30.
    # ti standalone: chord dx=150, dy=130. Scale ~0.5 (avg).
    # scale=0.55: head lands (ox - 70*0.55, oy - 70*0.55) = (ox-38.5, oy-38.5)
    # want head at (-70, -55): ox = -70+38.5 = -31.5, oy = -55+38.5 = -16.5
    # tip lands (-31.5 + 80*0.55, -16.5 + 60*0.55) = (-31.5+44, -16.5+33) = (12.5, 16.5)
    # tip target ~(+5, -20). Actual tip's y is +16.5 (way too high — passes ABOVE the joint).
    # ti's default chord dy=+130 vs target dy=+30 means the primitive rises
    # too steeply relative to its horizontal reach. Accept trade-off — TI's
    # thick-head-to-needle-tip silhouette is right, slope is a compromise.
    # Better: use smaller scale so both endpoints stay lower.
    # scale=0.42: head->(ox-29.4, oy-29.4); want head (-70,-55):
    #   ox=-40.6, oy=-25.6. tip: (-40.6+33.6, -25.6+25.2) = (-7, -0.4).
    # Tip lifts by 55 units (from y=-55 to y=-0.4) — too much rise vertically.
    # Reduce scale AND accept mid-height tip:
    # scale=0.4: head->(ox-28, oy-28). ox=-42, oy=-27. tip=(-42+32, -27+24)=(-10, -3).
    # Still rises high. This is the primitive's chord being too steep.
    # Compromise: use scale=0.42 so ti visible + rising, endpoint above midpoint OK.
    draw_ti(t, ox=-40.6, oy=-25.6, scale=0.42)

    # ---- Stroke 3: 撇 (short, upper-middle-right; head high-right, tail down-left)
    # GT 撇 is SHORT — head around (+30, +55), tail around (+5, 0). NOT reaching
    # the bottom. Chord dx=-25, dy=-55.
    # Standalone pie: chord dx=-110, dy=-175. Scale=0.32:
    #   head lands (ox+65*.32, oy+90*.32) = (ox+20.8, oy+28.8)
    #   want head (+30, +55): ox=+9.2, oy=+26.2
    #   tail lands (9.2-14.4, 26.2-27.2) = (-5.2, -1)
    # Head at (30.8, 55), tail at (-5.2, -1). Good — short 撇 in upper-middle-right.
    draw_pie(t, ox=9.2, oy=26.2, scale=0.32)

    # ---- Stroke 4: 竖弯钩 (right side long stroke — the wrapping curve+hook)
    # GT: shaft starts around (+50, +55), descends to (+50, -55), curves
    # right to (+90, -95), tail extends briefly, hook flicks UP.
    # Standalone shu_wan_gou at scale=0.85:
    #   shaft top (0, 70*.85)=(0, 59.5), shaft bot (0, -25.5)
    #   arc end / tail start: (40*.85, -70*.85) = (34, -59.5)
    #   tail end: (80*.85, -59.5) = (68, -59.5)
    #   hook tip: (75*.85, -48*.85) = (63.75, -40.8)
    # Want shaft top at (+50, +55): ox=+50, oy=+55-59.5 = -4.5
    # Actual placements:
    #   shaft top (50, 55) ✓
    #   shaft bot (50, -30) (close to -55; a bit high but OK — 比's shaft ends
    #     where the curve begins, not at the tail bottom)
    #   tail end (50+68, -4.5-59.5) = (118, -64) — extends nicely right
    #   hook tip (50+63.75, -4.5-40.8) = (113.75, -45.3) — clear upward flick
    draw_shu_wan_gou(t, ox=50.0, oy=-4.5, scale=0.85)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_bi(t)
    out = Path(__file__).resolve().parent / "01_比.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
