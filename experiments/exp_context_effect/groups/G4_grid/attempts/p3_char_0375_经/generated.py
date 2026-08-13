# BANK_DEVIATION
# skipped: si_silk.py
# reason: si_silk default anchors fill center-left column (standalone 纟);
#   in 经 the 纟 must compress into the leftmost ~1/3 column (x<100).
#   Never-tune-anchors rule forbids overriding all 8 anchors — inline instead.
# fresh_component: si_silk_left_compressed_for_经

import os
import sys
from PIL import Image, ImageDraw

# Bring bank primitives onto path.
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                    "success_bank", "code"))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width  # noqa: E402
from pie_zhe import draw_pie_zhe  # noqa: E402
from ti import draw_ti  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402
from na import draw_na  # noqa: E402


# 经 decomposition:
#   纟 (left, 3 strokes: 撇折 + 撇折 + 提)
#   又 (top-right, 2 strokes: 横撇 + 捺)
#   工 (bottom-right, 3 strokes: 横 + 竖 + 横)
# Total = 8 strokes (matches MMH count).

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('BANK_DEVIATION for 纟 (inlined compressed to left column). '
              'Right side: 又 (heng_pie + na) top, 工 (heng+shu+heng) bottom. '
              'All 7 declared joints implemented as N-neighbors.')
}


def draw_heng_pie(draw, head, corner, tail,
                  h_width=8, p_head_w=9, p_tip_w=3):
    """横 then 撇 sweep — used for the top of 又."""
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_tail = anchor_to_xy(tail)
    # 横 segment (straight uniform)
    fat_line(draw, p_head, p_corner, h_width)
    # 撇 sweep from corner down-left, tapered
    dx, dy = p_tail[0] - p_corner[0], p_tail[1] - p_corner[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    mid = ((p_corner[0] + p_tail[0]) * 0.5, (p_corner[1] + p_tail[1]) * 0.5)
    off = 0.06 * length
    ctrl = (mid[0] + perp[0] * off, mid[1] + perp[1] * off)
    pts = quad_bezier(p_corner, ctrl, p_tail, n=40)
    n = len(pts) - 1
    widths = [p_head_w + (p_tip_w - p_head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # ---- Left: 纟 compressed to left column (x ~ 10..90), y taller ----
    # s1: top pie_zhe (small loop, upper)
    draw_pie_zhe(draw,
                 head=('TL', 0.55, 0.35),
                 pivot=('TL', 0.10, 0.70),
                 tail=('TL', 0.80, 0.70),
                 pie_head_w=7, pie_tip_w=3, heng_w=5, shoulder=3)
    # s2: mid pie_zhe (slightly larger, right below)
    draw_pie_zhe(draw,
                 head=('ML', 0.55, 0.20),
                 pivot=('ML', 0.10, 0.60),
                 tail=('ML', 0.85, 0.60),
                 pie_head_w=8, pie_tip_w=3, heng_w=5, shoulder=3)
    # s3: 提 (rising flick) — starts lower-left, exits up-right at mid-right
    draw_ti(draw,
            from_anchor=('BL', 0.05, 0.80),
            to_anchor=('BL', 0.95, 0.55),
            head_width=11, tail_width=2, curve=0.08, segments=48)

    # ---- Top-right: 又 (2 strokes) ----
    # s4: 横撇 — horizontal short across top, then diagonal sweep down-left
    draw_heng_pie(draw,
                  head=('TC', 0.35, 0.35),
                  corner=('TR', 0.60, 0.35),
                  tail=('C', 0.55, 0.75),
                  h_width=8, p_head_w=10, p_tip_w=3)
    # s5: 捺 — starts near mid of the 撇 (weld point), goes down-right
    draw_na(draw,
            from_anchor=('C', 0.85, 0.35),
            to_anchor=('MR', 0.85, 0.85),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.85, curve=0.10, segments=48)

    # ---- Bottom-right: 工 (3 strokes) ----
    # s6: top 横
    draw_heng(draw, ('BC', 0.15, 0.20), ('BR', 0.75, 0.20), width=8)
    # s7: 竖
    draw_shu(draw, ('BC', 0.50, 0.22), ('BC', 0.55, 0.62), width=8)
    # s8: bottom 横 (base, wider)
    draw_heng(draw, ('BC', 0.05, 0.65), ('BR', 0.90, 0.65), width=9)

    # ---- Save ----
    out_dir = os.path.dirname(__file__)
    out_png = os.path.join(out_dir, "01_经.png")
    img.save(out_png)
    print(f"wrote {out_png}")


if __name__ == "__main__":
    main()
