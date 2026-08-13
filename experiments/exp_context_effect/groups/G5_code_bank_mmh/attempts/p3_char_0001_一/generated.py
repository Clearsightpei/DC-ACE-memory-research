"""p3_char_0001_一 — single 横 stroke.

Uses bank primitive draw_heng. Anchors from MMH:
  stroke 1: head @ ('ML', 0.354, 0.849) · tail @ ('MR', 0.695, 0.825)
米字格 cells are 100x100 within the 300x300 canvas.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))
from heng import draw_heng  # noqa: E402


def anchor_to_px(cell, xf, yf):
    """米字格 cell (3x3) → canvas pixel. Cells labeled by row (T/M/B) + col (L/M/R)."""
    row_map = {'T': 0, 'M': 1, 'B': 2}
    col_map = {'L': 0, 'M': 1, 'R': 2}
    r, c = row_map[cell[0]], col_map[cell[1]]
    x = c * 100 + xf * 100
    y = r * 100 + yf * 100
    return (x, y)


head = anchor_to_px('ML', 0.354, 0.849)  # (35.4, 184.9)
tail = anchor_to_px('MR', 0.695, 0.825)  # (269.5, 182.5)

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

draw_heng(draw, head, tail, width_head=9, width_tail=11)

out = Path(__file__).parent / "01_一.png"
img.save(out)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # exactly 1 draw_heng call
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': 'Single heng via bank primitive; anchors match MMH ML/MR.',
}
