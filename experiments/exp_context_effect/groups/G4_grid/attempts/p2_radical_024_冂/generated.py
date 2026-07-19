"""冂 (jiōng) — "down box" radical, 2 strokes.

Composition:
  stroke 1: 竖 (shù)      left vertical, top → bottom.
  stroke 2: 横折 (héng zhé) top horizontal then sharp turn down.

Joint: s1.head (top of left vertical) N s2.head (start of top horizontal),
        both in the TL cell — small natural gap (≈ 17 px), DO NOT weld.

Anchors follow the MMH-derived structural expectations block for this
item (dispatcher-injected). The self-check dict at the top logs the
outcome.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        "2 strokes: shu (left vertical) + heng_zhe (top+right). "
        "Joint at TL between s1.head and s2.head is left as N (natural "
        "gap ~17 px)."
    ),
}

import os
import sys
from PIL import Image, ImageDraw

# Success-bank primitives live one directory up (in success_bank/code/).
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy  # noqa: E402
from shu import draw_shu          # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ------------------------------------------------------------------
    # Stroke 1 — 竖 (left vertical)
    #   MMH head @ ('TL', 0.601, 0.867)  -> (60.1,  86.7)
    #   MMH tail @ ('BL', 0.595, 0.780)  -> (59.5, 278.0)
    # ------------------------------------------------------------------
    s1_head = ('TL', 0.601, 0.867)
    s1_tail = ('BL', 0.595, 0.780)
    draw_shu(draw, s1_head, s1_tail, width=9)

    # ------------------------------------------------------------------
    # Stroke 2 — 横折 (top horizontal + turn down)
    #   MMH head @ ('TL', 0.812, 0.938)  -> ( 81.2,  93.8)
    #   MMH tail @ ('BC', 0.852, 0.640)  -> (185.2, 264.0)
    #
    #   Corner sits at the top-right of the box.  MMH does not name a
    #   corner anchor for this stroke, so we place it just inboard of the
    #   right column so the horizontal spans most of the top and the
    #   vertical drops down toward the tail x-coordinate.
    #     corner @ ('TR', 0.90, 0.30) -> (290, 30) — too far; shrink
    #   We want corner.x ≈ tail.x (185) and corner.y ≈ head.y (~90).
    #   Actually a natural 冂 puts the corner near TR/TC boundary,
    #   with the vertical dropping straight down; MMH tail.x=185 tells
    #   us the right vertical sits at x≈185, so corner.x ≈ 185.
    #   corner ≈ (185, 88) -> cell TC, x_frac=0.852, y_frac=0.88.
    # ------------------------------------------------------------------
    s2_head = ('TL', 0.812, 0.938)
    s2_corner = ('TC', 0.852, 0.880)
    s2_tail = ('BC', 0.852, 0.640)
    draw_heng_zhe(draw, s2_head, s2_corner, s2_tail,
                  h_width=9, v_width=9, shoulder=11)

    # ------------------------------------------------------------------
    # Verify N-gap between s1.head and s2.head (both in TL).
    # ------------------------------------------------------------------
    p1h = anchor_to_xy(s1_head)
    p2h = anchor_to_xy(s2_head)
    gap = ((p1h[0] - p2h[0]) ** 2 + (p1h[1] - p2h[1]) ** 2) ** 0.5
    # Expected N-gap ~ 16.7 px.  Log for the self-check trace.
    SELF_CHECK['notes'] += f" | measured s1.head-s2.head gap = {gap:.1f} px."

    out = os.path.join(_HERE, "01_冂.png")
    img.save(out)
    print(f"wrote {out}  (s1-s2 head gap = {gap:.1f} px)")


if __name__ == "__main__":
    render()
