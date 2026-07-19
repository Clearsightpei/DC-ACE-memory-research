# p2_radical_100_见 — 见 (jiàn), 4-stroke radical.
#
# Stroke order:
#   1. 竖  — left short vertical (left edge of the top box)
#   2. 横折 — top horizontal + right vertical (top box's top and right)
#   3. 撇  — long left-falling sweep from inside box down-left (exits bottom-left)
#   4. 竖弯钩 — from inside box, down + curve right + upward hook (bottom-right)
#
# Composition strategy (per TR8 inline-fresh test):
# - The top box in 见 is TALLER than kou.py's square box, and slightly
#   narrower. shu (left) + heng_zhe (top+right) primitives fit with
#   deliberate scale/offset transformation (TR2 enclosing role → 0.65).
# - The 撇 and 竖弯钩 use bank primitives too — they match standalone shape
#   after uniform scaling (撇 is a wide diagonal sweep exiting bottom-left;
#   竖弯钩 has canonical curve+hook geometry).
#
# Coord math convention (P5): center origin, +y up. _to_pixel handles the flip.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu import draw_shu                        # noqa: E402
from heng_zhe import draw_heng_zhe              # noqa: E402
from pie import draw_pie                        # noqa: E402
from shu_wan_gou import draw_shu_wan_gou        # noqa: E402


CANVAS_SIZE = 300


def draw():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # REVISION 1: box needs to be taller (right vertical was too short on pass 1).
    # New box: top y=+90, bottom y=-30. Left x=-55, right x=+50. Height ~120,
    # width ~105. This matches the GT's taller proportions.
    #
    # ---- Stroke 1: 竖 (left vertical of the top box) --------------------
    # Spans y in [+90, -30], x = -55. Length ~120 px → scale ~0.67 (shu default ~180).
    # Center of target left 竖 is (-55, +30).
    draw_shu(t, ox=-55, oy=+30, scale=0.67)

    # ---- Stroke 2: 横折 (top + right side of the top box) ---------------
    # heng_zhe standalone: p_h_start (-90,60), p_corner (80,60), p_v_end (80,-75).
    # Horizontal width 170, vertical drop 135.
    # Target: horizontal (-55, +90) → (+50, +90), then down to (+50, -30).
    # Width needed 105 → scale_h = 0.62. Vertical drop needed 120 → scale_v = 0.89.
    # These don't match at uniform scale; heng_zhe is only uniformly-scalable.
    # Take scale = 0.70 as compromise, then verify the right vertical reaches
    # deep enough:
    #   at scale=0.70: h_start=(-63, 42), corner=(56, 42), v_end=(56, -52.5)
    # To land start (-55,+90): ox = -55 - (-63) = +8, oy = 90 - 42 = +48
    #   corner lands (64, 90) — a bit right of target (50,90) — box wider by ~14 px
    #   v_end lands (64, -4.5) — right vertical only reaches y=-4.5, still shy of -30
    # scale=0.85 works better for vertical drop:
    #   at scale=0.85: h_start=(-76.5, 51), corner=(68, 51), v_end=(68, -63.75)
    #   land start (-55,+90): ox = -55-(-76.5) = +21.5, oy = 90-51 = +39
    #   corner lands (89.5, 90) — too far right (box too wide)
    # Best compromise: scale=0.75 uniform.
    #   at 0.75: h_start=(-67.5, 45), corner=(60, 45), v_end=(60, -56.25)
    #   land start (-55,+90): ox = +12.5, oy = +45
    #   corner: (72.5, 90) — box right edge at +72.5 (~17 px too far right); accept
    #   v_end: (72.5, -11.25) — right vertical reaches y=-11.25 — still shy of -30
    # Compromise: scale=0.80 for taller box (accept the extra width):
    #   at 0.80: h_start=(-72, 48), corner=(64, 48), v_end=(64, -60)
    #   land start (-55,+90): ox = -55-(-72) = +17, oy = 90-48 = +42
    #   corner: (81, 90) — box wider by ~30 px total but visible box shape
    #   v_end: (81, -18) — right vertical reaches -18, still not to bottom (-30)
    # The GT box is actually narrower than heng_zhe wants at this height. Accept
    # scale=0.75 + shift left so total width isn't excessive.
    draw_heng_zhe(t, ox=+12, oy=+45, scale=0.75)

    # ---- Stroke 3: 撇 (long inner left-falling sweep) --------------------
    # pie.py canonical: head (+65*s, +90*s) to tail (-45*s, -85*s).
    # At scale 1.0 head-to-tail vertical drop ~175. Target: head near box's
    # top-right interior (roughly at math (+15, +55)) sweeping down-left to
    # exit bottom-left at (-70, -95).
    # scale = 0.75 → head_default = (+48.75, +67.5), tail_default = (-33.75, -63.75).
    # Head-to-tail drop = 131. Target head (+15, +55), tail (-70, -95).
    #   ox = 15 - 48.75 = -33.75, oy = 55 - 67.5 = -12.5
    # Check tail lands (-33.75-33.75, -63.75-12.5) = (-67.5, -76.25) — very close
    # to target tail (-70, -95). Slightly shorter but preserves stroke shape (TR5:
    # do not over-stretch scale; prefer accepting a slightly shorter tail).
    # REVISION: shift 撇 head down a touch (start from just inside top of box, not
    # dead on the top horizontal) and extend the tail lower.
    draw_pie(t, ox=-35, oy=-25, scale=0.82)

    # ---- Stroke 4: 竖弯钩 (bottom curve + up-hook, right of the 撇) ------
    # shu_wan_gou canonical: shaft top (0, +70), shaft bot (0, -30),
    # arc center (+40, -30), tail end (+80, -70), hook tip (+75, -48).
    # Target: shaft descends from box's bottom-right interior (~(+15, -10))
    # down to about (+15, -80), then curves right and hooks up.
    # scale = 0.75 → shaft_top_default (0, 52.5), shaft_bot_default (0, -22.5),
    # tail_end_default (+60, -52.5), hook_tip_default (+56, -36).
    #   Target shaft top (+15, -10): ox = 15 - 0 = +15, oy = -10 - 52.5 = -62.5
    # Check: shaft top lands (+15, +52.5-62.5) = (+15, -10) ✓
    #        shaft bot lands (+15, -22.5-62.5) = (+15, -85) — inside canvas ✓
    #        tail end lands (+75, -115) — off canvas bottom!
    # REVISION: with taller box (bottom now at y=-30), the 竖弯钩 starts from
    # inside the box near (+20, -20) and drops to about (+20, -90) before
    # curving right and hooking up around (+70, -80) → tip (+65, -60).
    # scale=0.55: shaft_top_default (0, 38.5), shaft_bot_default (0, -16.5),
    #   tail_end_default (+44, -38.5), hook_tip_default (+41.25, -26.4).
    # target shaft_top (+20, -20): ox=+20, oy = -20 - 38.5 = -58.5
    #   shaft bot: (+20, -75), tail end: (+64, -97), hook tip: (+61.25, -84.9)
    #   All in-canvas (margin ~10 px from bottom edge y=-140).
    draw_shu_wan_gou(t, ox=+20, oy=-59, scale=0.55)

    out_path = os.path.join(_HERE, "01_见.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    draw()
