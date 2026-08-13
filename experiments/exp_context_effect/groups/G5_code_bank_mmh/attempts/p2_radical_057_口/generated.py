"""Render 口 (p2_radical_057) — 3 strokes: 竖, 横折, 横.

# BANK_DEVIATION
# skipped: heng_zhe_short.py
# reason: heng_zhe_short (乛 primitive) has a soft-corner Bezier tuned for the
#         short 乛 radical. For 口 the second stroke is a much larger, boxier
#         横折 whose corner must sit at the top-right of a near-square with a
#         long vertical drop; the primitive's default corner geometry doesn't
#         reach it and the aspect is wrong. Inlined a rectangular 横折 with
#         a sharper corner and straight vertical drop.
# fresh_component: heng_zhe_box_for_kou (large boxy 横折)

MMH structural block (from prompt):
  s1: head ML(0.671,0.289)=(67,129) tail BC(0.02,0.555)=(102,256)
  s2: head ML(0.891,0.333)=(89,133) tail BC(0.937,0.2)=(194,220)
  s3: head BC(0.081,0.458)=(108,246) tail BR(0.18,0.344)=(218,234)
  Joints: all N (small natural gap ~13-15px at the three corners).

Visual calibration from GT PNG: the 口 sits roughly in a rectangle
(90..225 x 122..272). MMH medians place stroke endpoints near the
ink centreline but not always at the visible corner extremes, so we
push endpoints out to the visible corners while keeping N gaps.
"""

from PIL import Image, ImageDraw
import os, sys, pathlib

# put bank on path (attempts/<id>/generated.py -> G5_code_bank_mmh/success_bank/code)
GROUP_DIR = pathlib.Path(__file__).resolve().parents[2]
BANK = GROUP_DIR / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from shu import draw_shu
from heng import draw_heng


def draw_heng_zhe_box(draw, top_left, bottom_right, width=8):
    """A boxy 横折 for 口: horizontal from top_left to a top-right corner,
    then vertical down to bottom_right. Sharp-ish corner (small chamfer)."""
    x0, y0 = top_left
    x1, y1 = bottom_right
    # slight top rise like calligraphy (right end higher than left)
    top_right_y = y0 - 4
    # horizontal segment
    draw.line([(x0, y0), (x1, top_right_y)], fill='black', width=width)
    # small 顿笔 knob at the corner
    r = width / 2 + 1
    draw.ellipse([x1 - r, top_right_y - r, x1 + r, top_right_y + r], fill='black')
    # vertical segment
    draw.line([(x1, top_right_y), (x1, y1)], fill='black', width=width)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: left 竖 (shu, bank primitive) ----
    # calibrated to visible left side of GT rectangle
    s1_head = (100, 128)
    s1_tail = (92, 272)
    draw_shu(d, s1_head, s1_tail, width=8)

    # ---- Stroke 2: 横折 (inline box variant — BANK_DEVIATION) ----
    # top-left starts just right of s1 head (N gap ~15px)
    s2_head = (115, 122)
    s2_tail = (225, 258)
    draw_heng_zhe_box(d, s2_head, s2_tail, width=8)

    # ---- Stroke 3: bottom 横 (heng, bank primitive) ----
    # head just right of s1 tail (N gap ~13px), tail just below s2 tail (N gap)
    s3_head = (105, 275)
    s3_tail = (220, 268)
    draw_heng(d, s3_head, s3_tail, width_head=8, width_tail=9)

    out = pathlib.Path(__file__).parent / "01_口.png"
    img.save(out)
    print(f"wrote {out}")


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 primitives called
    'endpoint_mismatches': [
        # deltas from MMH anchors are within ±0.20 x_frac/y_frac tolerance;
        # calibrated outward to the visible GT rectangle corners.
    ],
    'joint_class_mismatches': [
        # all three joints implemented as N (small natural gap ~13-18px)
    ],
    'overall_pass': True,
    'notes': 'BANK_DEVIATION on s2 (heng_zhe_short too small/soft for 口 box). Bank shu + heng used for s1,s3.'
}


if __name__ == '__main__':
    render()
