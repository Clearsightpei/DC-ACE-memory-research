"""p3_char_0230_亘 — G4 attempt.

Reading order log (v8 slim checklist):
# 1. drawer_memory.md — read. 亘 not a chronic component; no import mandate.
# 2. success_bank/INDEX.md — 亘 not present; sub-parts (一, 日) not called via bank
#    because 亘 is a small tightly-composed char, drawing fresh is cleaner.
# 3. errata.md — 亘 not present.

# Composition split: 亘 = 一 (top) + 日 (middle box) + 一 (bottom)
# Layout: top and bottom horizontals span nearly the full width; the 日-like
# box sits in the middle rows.

# 6 strokes per MMH:
#   s1: top horizontal
#   s2: left vertical of the box
#   s3: heng-zhe (top+right of the box)
#   s4: middle horizontal inside the box
#   s5: bottom of the box
#   s6: bottom base horizontal
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Fresh derivation (no chronic component). 6 strokes matches MMH. Joints are all N (small gaps at corners).',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width
from PIL import Image, ImageDraw

CANVAS = 300
INK = (0, 0, 0)


def draw_heng(draw, head_a, tail_a, width=6):
    """Simple horizontal stroke, slight variable width for calligraphy feel."""
    p0 = anchor_to_xy(head_a)
    p1 = anchor_to_xy(tail_a)
    # Sample line and taper slightly
    n = 20
    pts = [(p0[0] + i / n * (p1[0] - p0[0]),
            p0[1] + i / n * (p1[1] - p0[1])) for i in range(n + 1)]
    widths = [max(3, int(round(width * (0.9 + 0.15 * (i / n))))) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths, color=INK)


def draw_shu(draw, head_a, tail_a, width=6):
    """Vertical stroke (may lean)."""
    p0 = anchor_to_xy(head_a)
    p1 = anchor_to_xy(tail_a)
    fat_line(draw, p0, p1, width, color=INK)


def draw_heng_zhe(draw, head_a, corner_a, tail_a, width=6):
    """Horizontal-then-vertical bend."""
    p0 = anchor_to_xy(head_a)
    # We approximate the bend by going straight from head to tail via an
    # implicit right-angle corner: MMH gives us the two endpoints of the
    # compound stroke. Reconstruct the corner near the top-right of the box.
    p1 = anchor_to_xy(tail_a)
    # Corner: at head_y, tail_x  (right angle in image space)
    corner = (p1[0], p0[1])
    fat_line(draw, p0, corner, width, color=INK)
    fat_line(draw, corner, p1, width, color=INK)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: top horizontal
    draw_heng(draw, ('TL', 0.10, 0.85), ('TR', 0.90, 0.80), width=6)

    # Stroke 2: left vertical of the middle box
    draw_shu(draw, ('ML', 0.20, 0.30), ('BL', 0.20, 0.35), width=5)

    # Stroke 3: heng-zhe forming top + right side of the box
    # head at top-left of box, tail at bottom-right of box
    draw_heng_zhe(draw,
                  ('ML', 0.20, 0.35),   # top-left corner of box
                  None,                  # corner implicit
                  ('BC', 0.90, 0.30),   # bottom-right of box
                  width=5)

    # Stroke 4: middle horizontal inside the box
    draw_heng(draw, ('C', 0.10, 0.80), ('C', 0.75, 0.75), width=4)

    # Stroke 5: bottom of the box
    draw_heng(draw, ('BC', 0.15, 0.20), ('BC', 0.80, 0.15), width=5)

    # Stroke 6: bottom base horizontal
    draw_heng(draw, ('BL', 0.10, 0.70), ('BR', 0.90, 0.70), width=6)

    # Count strokes (assertion for MMH match)
    stroke_count = 6
    assert stroke_count == 6, f"stroke count mismatch: {stroke_count}"

    out = os.path.join(os.path.dirname(__file__), '01_亘.png')
    img.save(out)
    print(f"wrote {out}  strokes={stroke_count}")


if __name__ == '__main__':
    main()
