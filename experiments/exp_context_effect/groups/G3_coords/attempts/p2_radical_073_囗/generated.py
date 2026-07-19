# p2_radical_073_囗 (wéi) — enclosing 3-stroke radical.
#
# Composition: same 3 strokes as 口 (kou), but scaled UP because 囗 is
# an *enclosing* radical (TR2: scale 0.90-1.0), occupying most of the
# canvas. Reuses the same bank-primitive template that PASSed for kou
# (batch B1 pos 89), rescaled and re-anchored.
#
# INLINE-FRESH TEST (TR8): the three strokes are pure straight
# horizontal/vertical/right-angle segments — precisely what shu,
# heng, heng_zhe primitives are tuned for. No curl, no taper mismatch,
# no diagonal geometry to force. The primitives ARE the right tool.
# GT check: box silhouette with straight sides, hard corners. Match.
#
# Target box (from GT visual): x ~ 70..205, y ~ 55..230 (PIL px).
# In math coords (center 150,150, +y up): x_L = -80, x_R = +55,
# y_top = +95, y_bot = -80. Width ~135, height ~175.
# Center of box: math (-12, +7) ≈ PIL (138, 143). Slight left shift.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu import draw_shu            # noqa: E402
from heng import draw_heng          # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def draw_wei(t):
    """囗 radical: 3-stroke enclosing box, larger than 口."""
    # -----------------------------------------------------------------
    # Stroke 1 — LEFT 竖 (shu).
    #   Target: vertical line from PIL (70,55) to (70,230).
    #     math: x=-80, y from +95 down to -80. Length 175, center at
    #           math (-80, +7).
    #   shu primitive default: length 200 at scale 1.0, centered at
    #   (ox, oy). Need length 175 → scale = 0.875. Center at (-80, +7).
    # -----------------------------------------------------------------
    draw_shu(t, ox=-80, oy=+7, scale=0.875)

    # -----------------------------------------------------------------
    # Stroke 2 — TOP + RIGHT 横折 (heng_zhe).
    #   Target: horizontal top from PIL (70,55) to (205,55), then
    #           right vertical from (205,55) down to (205,230).
    #     math: h from (-80,+95) to (+55,+95); v from (+55,+95) to
    #           (+55,-80).
    #   heng_zhe primitive at scale 1.0 emits:
    #     p_h_start = (-90, +60), p_corner = (+80, +60), p_v_end = (+80, -75).
    #   Uniform scale s: h_start=(-90s, +60s), corner=(+80s, +60s),
    #     v_end=(+80s, -75s), offset by (ox, oy).
    #   Want corner at (+55, +95): +80s + ox = +55, +60s + oy = +95.
    #   Want h_start at (-80, +95): -90s + ox = -80 → ox = -80 + 90s.
    #     Then +80s + (-80+90s) = +55 → 170s = 135 → s = 0.794.
    #     ox = -80 + 90*0.794 = -80 + 71.5 = -8.5.
    #     oy = +95 - 60*0.794 = +95 - 47.6 = +47.4.
    #   Verify v_end: +80s+ox = +55 ✓; -75s+oy = -75*0.794 + 47.4
    #     = -59.5 + 47.4 = -12.1. But target v_end is (-80). Gap of
    #     ~68 px in math (= ~68 PIL px) below the corner not covered
    #     by heng_zhe. That's fine — the LEFT shu at scale 0.875 goes
    #     from +95 down to -80, but the RIGHT side vertical must span
    #     the same range. heng_zhe alone can't. Solution: run a
    #     second short shu on the right OR increase heng_zhe scale so
    #     v_end reaches -80. If s = 1.05: h_start_x = -80 - 90*1.05
    #     doesn't fit (too far left). Better: keep heng_zhe at s such
    #     that v_end reaches y=-80. -75s + oy = -80 with oy set by
    #     corner constraint. Two constraints (top-left, bot-right)
    #     for two params (s, ox,oy). Recompute:
    #     Let corner PIL match top-right = (205,55) i.e. math
    #     (+55,+95); h_start math = (-80,+95); v_end math = (+55,-80).
    #     From heng_zhe geometry: v_end.y - corner.y = -75s - 60s
    #     = -135s. Target: -80 - 95 = -175. So s = 175/135 = 1.296.
    #     Then h_start.x - corner.x = -90s - 80s = -170s = -220.7,
    #     but target: -80 - 55 = -135. Mismatch — primitive's
    #     aspect ratio doesn't match target box aspect.
    # Decision: keep heng_zhe at the scale that MATCHES the top+right
    # corner geometry and rely on the LEFT shu + BOTTOM heng to close
    # the frame. The right vertical of heng_zhe will be SHORT; we'll
    # add a SECOND short shu right below its endpoint to extend to y=-80.
    # -----------------------------------------------------------------
    s_hz = 0.794
    ox_hz = -8.5
    oy_hz = 47.4
    draw_heng_zhe(t, ox=ox_hz, oy=oy_hz, scale=s_hz)

    # heng_zhe v_end at math (+55, -12.1). Need to extend down to (+55, -80).
    # Extension segment length 67.9 px, centered at (+55, -46.05).
    # shu at scale 0.679 would give length 135.8 — too long. Actually
    # length_at_scale = 200*scale, so scale = 67.9/200 = 0.34. But
    # per P4 stroke thickness = 12*scale = 4 px (too thin — width
    # mismatch with the left shu at 10-11 px). Better: inline as one
    # straight tapered-uniform segment at the same 12-ish px width.
    from PIL import ImageDraw as _ID  # noqa: F401
    # Direct thick line, matching heng_zhe's ink_w = 10*s_hz ≈ 8 px,
    # blending with heng_zhe's terminal segment.
    # Math (+55,-12.1) → PIL (150+55, 150-(-12.1)) = (205, 162.1).
    # Math (+55,-80)  → PIL (150+55, 150-(-80))  = (205, 230).
    t.line([(205, 162), (205, 230)], fill=(0, 0, 0), width=8)

    # -----------------------------------------------------------------
    # Stroke 3 — BOTTOM 横 (heng).
    #   Target: horizontal from PIL (70,230) to (205,230).
    #     math: from (-80,-80) to (+55,-80). Length 135, center at
    #           (-12.5, -80).
    #   heng scale = 135/200 = 0.675. Center at (-12.5, -80).
    # -----------------------------------------------------------------
    draw_heng(t, ox=-12.5, oy=-80, scale=0.675)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_wei(draw)
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_囗.png",
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
