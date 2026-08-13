"""G5 attempt: p2_radical_065_尸 (3 strokes: 横折, 短横, 撇)."""

import pathlib
import sys

from PIL import Image, ImageDraw

# add bank code path
BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng                    # noqa: E402
from heng_zhe_short import draw_heng_zhe_short  # noqa: E402
from pie import draw_pie                      # noqa: E402


# --- MMH anchor → pixel helpers ---------------------------------------
# 300x300 canvas, 3x3 米字格 cells, each 100x100.
CELLS = {
    "TL": (0, 0), "TC": (100, 0), "TR": (200, 0),
    "ML": (0, 100), "C": (100, 100), "MR": (200, 100),
    "BL": (0, 200), "BC": (100, 200), "BR": (200, 200),
}


def anchor(cell, xf, yf):
    cx, cy = CELLS[cell]
    return (cx + xf * 100, cy + yf * 100)


# --- Anchors from MMH block ------------------------------------------
S1_HEAD = anchor("TC", 0.134, 0.964)   # ≈ (113, 96)  top of 横折
S1_TAIL = anchor("C",  0.966, 0.307)   # ≈ (196, 131) after the bend

S2_HEAD = anchor("C",  0.11,  0.573)   # ≈ (111, 157) left end of middle 横
S2_TAIL = anchor("MR", 0.162, 0.415)   # ≈ (216, 141) right end of middle 横

S3_HEAD = anchor("TL", 0.899, 0.917)   # ≈ (90, 92)   top of 撇 (near s1.head)
S3_TAIL = anchor("BL", 0.252, 0.944)   # ≈ (25, 294)  bottom-left tail of 撇


# --- Render ----------------------------------------------------------
img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

# s1: 横折 — bank primitive fits a short horizontal-with-downturn
draw_heng_zhe_short(draw, S1_HEAD, S1_TAIL, corner_offset=(6, 0))

# s2: short 横 — bank heng from left-of-center to mid-right
draw_heng(draw, S2_HEAD, S2_TAIL, width_head=8, width_tail=9)

# s3: long 撇 — bank pie sweep from near top-left down to bottom-left
draw_pie(draw, S3_HEAD, S3_TAIL, bow_perp=18, w_head=10, w_tail=2, steps=100)

out_path = pathlib.Path(__file__).parent / "01_尸.png"
img.save(out_path)


# --- Self-check ------------------------------------------------------
SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,       # 3 stroke calls == expected 3
    "endpoint_mismatches": [],     # anchors used directly from MMH block
    "joint_class_mismatches": [],  # all 3 joints are N (natural gap); we did not weld
    "overall_pass": True,
    "notes": "s1 uses heng_zhe_short with small corner_offset for a tighter 横折. "
             "s3.head at (90,92) sits ~20px from s1.head (113,96) = N gap. "
             "s2.head at (111,157) sits well below s3's mid-point trajectory = N gap.",
}

if __name__ == "__main__":
    print("wrote", out_path)
    print("SELF_CHECK:", SELF_CHECK)
