# p3_char_0016_乃 — G3 attempt
# 乃 has 2 strokes:
#   (1) 横折折折钩 — a horizontal top-bar that turns down, then curves
#       leftward at the bottom into a small upward hook (bottom-left).
#   (2) 撇 — a large left-falling sweep from the upper area (near where
#       stroke 1 turns down) down to the bottom-left corner.
#
# G3 coord format: fresh derivation with PIL inline. No 米字格 anchors.
# Follows P5 math-coord convention (center origin at 150,150, +y up).

import os
import math
import sys

from PIL import Image, ImageDraw

# Import shared helpers (variant_pie for the sweep, tapered_bezier for
# the folded stroke).
_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)
from _shared_helpers import to_px, tapered_bezier, variant_pie, tapered_line  # noqa: E402


CANVAS = 300


def draw_zhe_segment(draw, p0, p1, w0, w1, n=48):
    """A tapered straight segment between two math-coord points."""
    tapered_line(draw, p0, p1, w0, w1, n=n)


def draw_stroke1_heng_zhe_zhe_gou(draw):
    """Stroke 1 for 乃: 横折折折钩.

    Reads (from GT) as: a top-bar goes right; at its right end the ink
    curves down-right and then arcs back leftward-downward into a small
    upward hook near the bottom-middle. Rendered as: heng bar + tapered
    bezier arc down-right→down-left + small hook flick.
    """
    # Top horizontal bar (heng): left-inside to right-end.
    a = (-45, 60)
    b = (55, 60)
    tapered_line(draw, a, b, w0=9, w1=10, n=40)
    # Small 顿笔 blob at right end (b).
    bx, by = to_px(*b)
    draw.ellipse([bx - 6, by - 6, bx + 6, by + 6], fill=(0, 0, 0))

    # Big smooth arc from (b): bulges out to the right, comes down, and
    # curves back leftward to a bottom-middle end (d).
    c_ctrl = (85, -10)     # bulge outward to lower-right
    d = (-5, -70)          # bottom, slightly left of center
    tapered_bezier(draw, b, c_ctrl, d, w_head=10, w_tail=7, n=64)

    # Small upward-left hook (钩) at the end.
    e = (-25, -55)
    tapered_line(draw, d, e, w0=7, w1=1, n=22)


def draw_stroke2_pie(draw):
    """Stroke 2 for 乃: the big 撇 sweeping from the left end of the
    top-bar down to the bottom-left corner."""
    # Head: near the left start of the top-bar.
    head = (-40, 55)
    # Tail: far bottom-left.
    tail = (-95, -95)
    variant_pie(draw, head, tail, bow_perp=-4.0,
                w_head=9.0, w_tail=1.2, n=60)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_stroke1_heng_zhe_zhe_gou(draw)
    draw_stroke2_pie(draw)

    out_path = os.path.join(os.path.dirname(__file__), "01_乃.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
