"""p2_radical_085_贝 — G3 attempt.

贝 radical (4 画, simplified form). Structure per GT:
  1. 竖  — left vertical of the top box
  2. 横折 — top horizontal + right vertical (right side extends down past
           bottom of box, ending mid-canvas)
  3. 撇  — long left leg from bottom of left vertical, sweeping down-left
  4. 丶  — dot at bottom-right (heavy tapered point)

The top forms a small rectangle-frame open at the bottom. The bottom of
the left vertical (~y=0) is where the 撇 begins. The right side of the
横折 continues down past where the box "closes" (no bottom heng) to
about y=-30, but is actually the SAME shu that closes the box (no
separate stroke). Wait — with only 4 strokes and no bottom heng, the
frame is unclosed at bottom; the 撇 starts near left-bottom-corner and
the 丶 sits near right-bottom-corner.

TR6/TR8 compliance:
- Left 竖 (stroke 1): fresh inlined tapered line (short vertical, need
  matched thin width with the 横折's arms — inline-fresh, not draw_shu
  which defaults to a fatter/longer stroke).
- 横折 (stroke 2): inline as one continuous horizontal + right-turn
  vertical polyline with a 顿笔 blob at the elbow (per P6). Trying
  draw_heng_zhe at scale ~0.5 would compress its brushwork; matched
  width with left 竖 requires inline.
- 撇 (stroke 3): draw_pie at scale ~0.55, placed with head near the
  bottom of the box's left vertical, tail sweeping to lower-left.
  Bank pie is a good match here — the target's left leg IS a diagonal
  sweep.
- 丶 (stroke 4): draw_dian at scale ~0.55, placed lower-right below
  the right edge.

Coord convention (math): center origin, +y up, canvas 300x300.
Left vertical top: (-40, +60), bottom (-40, -5).
Right vertical top: (+30, +60), bottom (+30, -30).
Top horizontal: (-40, +60) to (+30, +60).
撇 head near (-40, 0), tail near (-95, -90).
丶 near (+30, -75).
"""

import os
import sys
from PIL import Image, ImageDraw

_ATTEMPT_DIR = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_ATTEMPT_DIR, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie   # noqa: E402
from dian import draw_dian  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    """Math coords (center, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _tapered_segment(t, p0, p1, w0, w1, n=30):
    """Draw a straight tapered ink segment from p0 to p1 in math coords."""
    prev = None
    for i in range(n + 1):
        u = i / n
        mx = p0[0] * (1 - u) + p1[0] * u
        my = p0[1] * (1 - u) + p1[1] * u
        px, py = _to_pixel(mx, my)
        w = w0 * (1 - u) + w1 * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_bei(t):
    """Draw 贝 radical, 4 strokes. Revision: larger box, longer right
    vertical, longer 撇, dot moved down-right per GT.

    Frame corners (math coords):
      top-left  = (-45, +75)
      top-right = (+40, +75)
      box-bot-L = (-45, -25)   ← where the 撇 begins
      right leg extends further down to (+40, -110)  ← very long right
    """
    # Stroke 1: 左竖 — from (-45, +75) down to (-45, -25). Width ~10.
    _tapered_segment(t, (-45, 75), (-45, -25), w0=10, w1=10, n=30)

    # Stroke 2: 横折 — top heng + long right shu, one continuous stroke.
    #   Top heng: (-45, +75) -> (+40, +75), width ~10.
    _tapered_segment(t, (-45, 75), (40, 75), w0=10, w1=10, n=30)
    #   Elbow blob at (+40, +75).
    ex, ey = _to_pixel(40, 75)
    t.ellipse([ex - 6, ey - 6, ex + 6, ey + 6], fill=(0, 0, 0))
    #   Right shu extends far down past the box to y=-110, tapering
    #   slightly at bottom.
    _tapered_segment(t, (40, 75), (40, -110), w0=10, w1=8, n=45)

    # Stroke 3: 撇 — long left leg from near bottom of the box's left
    # vertical (-45, -25) sweeping down-left to (-115, -120).
    # Bank pie's canonical head (65, 90), tail (-45, -85). At scale 0.7:
    #   head@0.7 = (45.5, 63), tail@0.7 = (-31.5, -59.5).
    #   Want head at (-45, -25): ox = -45 - 45.5 = -90.5, oy = -25 - 63 = -88.
    #   Then tail lands at (-90.5 - 31.5, -88 - 59.5) = (-122, -147.5) — too low.
    # Try scale 0.6:
    #   head@0.6 = (39, 54), tail@0.6 = (-27, -51).
    #   ox = -45 - 39 = -84, oy = -25 - 54 = -79.
    #   tail = (-84 - 27, -79 - 51) = (-111, -130) — close to target
    #   (-115, -120), acceptable.
    draw_pie(t, ox=-84, oy=-79, scale=0.6)

    # Stroke 4: 丶 — dot at lower-right, below the right leg's end.
    # Position tail near (+30, -95). Bank dian tail at scale 0.55:
    #   tail@0.55 = (9.9, -11). Offset: ox=+20, oy=-84.
    # Actually the GT dot is slightly INSIDE the right vertical (to its
    # left), starting mid-right and sweeping down-right. Let's put its
    # head near (0, -70) and tail near (+25, -95).
    draw_dian(t, ox=8, oy=-83, scale=0.55)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_bei(t)
    out = os.path.join(_ATTEMPT_DIR, "01_贝.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
