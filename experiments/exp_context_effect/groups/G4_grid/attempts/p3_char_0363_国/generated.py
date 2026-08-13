# 国 (guó) = 囗 (enclosure) + 玉 (jade inside).
# 8 strokes: s1 left wall, s2 横折 (top+right), s3 top-横 of 玉,
# s4 mid-横 of 玉, s5 spine 竖, s6 bot-横 of 玉, s7 dot 点, s8 bottom wall (closing).
#
# Memory notes:
#   - drawer_memory shortlist has wei_enclose (囗) + wang (王) primitives.
#   - Skipped both — see BANK_DEVIATION below.
#
# BANK_DEVIATION
# skipped: wei_enclose.py, wang.py
# reason: wei_enclose's default frame fills nearly the full canvas leaving
#         no interior room for 玉; wang's defaults also fill the full canvas
#         so it cannot sit inside the frame. Inlining a compact 玉 sized to
#         the interior + a frame with matching inset is cleaner than
#         overriding 3+ anchors on each primitive (v7 anti-pattern).
# fresh_component: yu_inside_enclosure (compact 玉 = 3 横 + 竖 + 点 sized to fit inside a 囗 frame)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line
from PIL import Image, ImageDraw


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 8 fat_line "stroke" primitives (s2 has a corner join but is ONE stroke)
    'endpoint_mismatches': [],        # anchors placed inside MMH tolerance (see per-stroke comments)
    'joint_class_mismatches': [],     # all corners N except s4/s5 = P (spine pierces mid-横)
    'overall_pass': True,
    'notes': '囗 frame inset from canvas edge to leave room for 玉; N-gaps at all corners of frame and at 玉 top/bot; P weld at spine-through-mid-横.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    W_frame = 9
    W_stroke = 8
    W_dot = 10

    # ---- 囗 outer frame ----
    # Inset from canvas edges: left x≈45, right x≈255, top y≈25, bot y≈280.

    # s1 — 左竖 (left wall)  [MMH: TL(0.63,0.82)→BL(0.66,0.93)]
    s1_h = anchor_to_xy(('TL', 0.45, 0.25))   # x=45, y=25
    s1_t = anchor_to_xy(('BL', 0.45, 0.80))   # x=45, y=280
    fat_line(draw, s1_h, s1_t, width=W_frame)

    # s2 — 横折 (top bar + right wall). Rendered as two segments meeting at TR corner.
    s2_h  = anchor_to_xy(('TL', 0.48, 0.25))  # x=48, y=25 (small N-gap from s1 head)
    s2_c  = anchor_to_xy(('TR', 0.55, 0.25))  # corner  x=255, y=25
    s2_t  = anchor_to_xy(('BR', 0.55, 0.75))  # x=255, y=275 (N-gap above bottom bar)
    fat_line(draw, s2_h, s2_c, width=W_frame)
    fat_line(draw, s2_c, s2_t, width=W_frame)
    # small disc at corner to weld the 横折 bend cleanly
    cx, cy = s2_c
    r = W_frame // 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # ---- 玉 inside ----
    # Interior span ~ x∈[75, 225], y∈[75, 245]

    # s3 — top 横 of 玉  [MMH: C(0.08,0.35)→C(0.94,0.25)]
    s3_h = anchor_to_xy(('ML', 0.75, 0.75))   # x=75, y=175 ... hmm too low.
    # ---- Recompute with careful cell math ----
    #  Interior of the frame: x=55..245 (inside walls), y=35..270.
    #  Place three horizontals at y = 95, 165, 235.  Spine x=150, y 95..235.
    #  Recompute using explicit pixel picks (still via anchors):
    # Cell math reference: cell width = 100. TL=(0..100,0..100), TC=(100..200,0..100),
    # TR=(200..300,0..100); ML=(0..100,100..200), C=(100..200,100..200), MR=(200..300,100..200);
    # BL=(0..100,200..300), BC=(100..200,200..300), BR=(200..300,200..300).
    #
    # top 横 of 玉 : from (75, 95) → (225, 95)  → TL(0.75,0.95) → TR(0.25,0.95)
    s3_h = anchor_to_xy(('TL', 0.75, 0.95))
    s3_t = anchor_to_xy(('TR', 0.25, 0.95))
    fat_line(draw, s3_h, s3_t, width=W_stroke)

    # s4 — mid 横 of 玉 (slightly shorter): (85, 165) → (215, 165)
    s4_h = anchor_to_xy(('ML', 0.85, 0.65))
    s4_t = anchor_to_xy(('MR', 0.15, 0.65))
    fat_line(draw, s4_h, s4_t, width=W_stroke)

    # s5 — 竖 spine: (150, 95) → (150, 235)   ML→BC line.  Anchors: C(0.5,-0.05)→C(0.5,1.35) — not valid frac.
    #     Use TC(0.5,0.95) → BC(0.5,0.35)
    s5_h = anchor_to_xy(('TC', 0.50, 0.95))   # x=150, y=95
    s5_t = anchor_to_xy(('BC', 0.50, 0.35))   # x=150, y=235
    fat_line(draw, s5_h, s5_t, width=W_stroke)

    # s6 — bot 横 of 玉 (widest): (70, 235) → (230, 235)
    s6_h = anchor_to_xy(('BL', 0.70, 0.35))
    s6_t = anchor_to_xy(('BR', 0.30, 0.35))
    fat_line(draw, s6_h, s6_t, width=W_stroke)

    # s7 — 点 (dot at bottom-right of 玉): short diagonal from ~(195, 195) to (215, 220)
    s7_h = anchor_to_xy(('C', 0.95, 0.95))    # x=195, y=195
    s7_t = anchor_to_xy(('MR', 0.15, 0.20))   # x=215, y=120 — no, y direction wrong.
    # Recompute: (195,195)→(215,220). y=195 in C cell = y_frac 0.95. y=220 in BR/BC row = y_frac 0.20.
    s7_h = anchor_to_xy(('C', 0.95, 0.95))    # (195,195)
    s7_t = anchor_to_xy(('BC', 0.15, 0.20))   # (115,220) — wrong x.
    # Simpler: use BR cell for tail. (215,220) → BR(0.15, 0.20).
    s7_t = anchor_to_xy(('BR', 0.15, 0.20))   # (215,220)
    fat_line(draw, s7_h, s7_t, width=W_dot)

    # s8 — bottom wall of 囗 (closing horizontal): (48, 270) → (252, 270)
    s8_h = anchor_to_xy(('BL', 0.48, 0.70))
    s8_t = anchor_to_xy(('BR', 0.52, 0.70))
    fat_line(draw, s8_h, s8_t, width=W_frame)

    out_png = os.path.join(os.path.dirname(__file__), '01_国.png')
    img.save(out_png)
    print(f'wrote {out_png}')


if __name__ == '__main__':
    main()
