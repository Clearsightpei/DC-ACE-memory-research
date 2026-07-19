# p2_radical_038_㔾 — 㔾 (jié), 2 strokes: 横折 (small top hook) + 竖弯钩 (main envelope)
#
# GT reading: canvas 300x300. There is a small tick / small 横折 at
# upper-left area (~ px x=90..115, y=100..135), and a large open-envelope
# shape whose left vertical starts near top and descends to the bottom,
# curves right along the bottom, and rises up on the right side then flicks
# back inward with a hook.
#
# Composition plan (TR6 comments):
# Stroke 1 — small 横折 in upper-left, spanning roughly from (px 90,105)
#   turning down to (px 115,135). It reads as a tiny corner tick.
#   Use draw_heng_zhe scaled small (~0.18) placed high-left.
#   heng_zhe default h-span math coords: p_h_start=(-90,60), p_corner=(80,60)
#   p_v_end=(80,-75). At scale 0.18 spans ~30px h, ~24px v.
#   Target corner canvas pixel ~ (118, 108). Convert: math (cx=150+ox,
#   cy=150-oy). So corner math = (ox + 80*0.18, oy + 60*0.18)
#   = (ox + 14.4, oy + 10.8). For canvas (118,108): math (-32, 42).
#   Need ox + 14.4 = -32 -> ox = -46.4; oy + 10.8 = 42 -> oy = 31.2.
#
# Stroke 2 — main envelope. Use draw_shu_wan_gou but scaled up and
#   shifted so its shaft-top sits near canvas top (px ~140,105), shaft
#   descends to bottom-left (~140,240), curves right along bottom, and
#   the hook flicks up on the right side.
#   shu_wan_gou default: shaft_top math (0, 70), shaft_bot (0,-30),
#   arc goes right, tail_end (80,-70), hook_tip (75,-48). At scale 1.0,
#   shaft length = 100 px, tail length = 40 px.
#   Target: shaft_top canvas (140,105) -> math (-10, 45).
#           tail_end canvas (~240,240) -> math (90, -90).
#   With scale 1.15: shaft_top math -> (ox, oy + 70*1.15) = (ox, oy+80.5)
#     -> ox=-10, oy=-35.5. Then tail_end math = (ox+80*1.15, oy-70*1.15)
#     = (-10+92, -35.5-80.5) = (82, -116). Canvas: (232, 266). A bit
#     low; ok since GT bottom is near y=240..260.
#   Use scale=1.10 instead: shaft_top math (ox, oy+77) -> ox=-10, oy=-32.
#     tail_end math = (-10+88, -32-77) = (78, -109). Canvas (228, 259). Ok.

from PIL import Image, ImageDraw
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
# HERE = .../groups/G3_coords/attempts/p2_radical_038_㔾
# want  .../groups/G3_coords/success_bank/code
SB = os.path.normpath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, SB)

from heng_zhe import draw_heng_zhe  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # Revision plan — first render mismatched GT:
    #  - Main envelope too narrow / shifted right; left side should start
    #    near px x=95 (not x=140) and descend to bottom.
    #  - Bottom should sweep across to right side (px x~205), then RISE up
    #    on the right side to about y=110 (a tall right wall), then a small
    #    hook flick.
    #  - Small tick sits inside the envelope near top (x~115, y~120).
    #
    # shu_wan_gou primitive as-is puts shaft on the LEFT and tail flat to
    # the right — that's the correct 竖弯钩 form. Need the shaft-top pixel
    # near (95, 110), tail_end near (205, 250), hook flicking up to (~205,205).
    #
    # shu_wan_gou math anchors (unscaled): shaft_top=(0,70), shaft_bot=(0,-30),
    # arc goes right to (40,-70), tail_end=(80,-70), hook_tip=(75,-48).
    # Distance shaft_top→tail_end in math coords = (80, -140).
    # In canvas: (140 down, 80 right) unscaled → need (140 down, 110 right).
    # So we need scale ≈ 140/140 = 1.0 for vertical, but tail-x = 80*s = 110
    # → s ≈ 1.375. Compromise: scale 1.30 gives shaft length 130 px (100→130)
    # and tail length 104 px. Close enough.
    #
    # With scale=1.30: shaft_top canvas = (150+ox, 150-oy-91).
    #   Want (95, 110). So ox = -55, 150-oy-91 = 110 → oy = -51.
    # Check tail_end: math (ox+104, oy-91) = (49, -142). Canvas (199, 292).
    # y=292 is past canvas — too low. Reduce scale to 1.15:
    #   shaft length 115 px. shaft_top (150+ox, 150-oy-80.5) = (95, 110)
    #   → ox=-55, oy=-40.5. tail_end math (ox+92, oy-80.5) = (37, -121).
    #   canvas (187, 271). Still low. Use scale 1.05:
    #   shaft_top: 150-oy-73.5=110 → oy=-33.5; ox=-55.
    #   tail_end math (ox+84, oy-73.5) = (29, -107). canvas (179, 257). ok.
    # Actually widen: at scale 1.05 tail_end canvas x=179 — too narrow.
    # Push ox right by extra +15 to widen bottom-right: ox=-40, shaft_top x=110.
    # Compromise: use scale=1.20, ox=-50, oy=-38:
    #   shaft_top (100, 100), tail_end math (46, -122) → canvas (196, 272).
    # Try scale=1.10, ox=-48, oy=-35:
    #   shaft_top (102, 108). tail_end math (40, -112). canvas (190, 262). Good.

    # Stroke 2 (drawn first so stroke 1 sits on top): large 竖弯钩 envelope.
    draw_shu_wan_gou(d, ox=-48, oy=-35, scale=1.10)

    # Stroke 1: small 横折 tick INSIDE the envelope, upper-left.
    # heng_zhe corner target canvas (120, 122). Corner math (-30, 28).
    # scale=0.20: corner math = (ox+16, oy+12) → ox=-46, oy=16.
    draw_heng_zhe(d, ox=-46, oy=16, scale=0.20)

    out = os.path.join(HERE, "01_㔾.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
