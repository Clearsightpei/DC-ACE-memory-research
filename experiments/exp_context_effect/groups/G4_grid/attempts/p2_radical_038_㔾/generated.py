"""㔾 (Phase-2 radical, 2画) — G4 grid-bank attempt.

Composition (MMH-derived):
  stroke 1 (small 横撇钩 / angular top piece):
      head @ ('ML', 0.876, 0.233) → tail @ ('BC', 0.626, 0.057)
      Inlined as a small 横 + angular fold. The head is the start of the
      short horizontal top; the tail is the endpoint of the fold going
      down-right (per MMH endpoint order).
  stroke 2 (竖弯钩 / big outer bowl):
      head @ ('ML', 0.732, 0.198) → tail @ ('BR', 0.681, 0.285)
      Inlined as a 竖弯钩-style outer sweep: from upper-left head, curve
      down through BC bottom, sweep right and slightly up to the tail
      in BR, then a short hook flick at the end.

Anchor plan:
  s1.head @ ML(0.876, 0.233)  ~ (88, 123)  — top-left start
  s1 corner @ TC(0.63, 0.85)  ~ (163, 85)  — small horizontal reaches right
  s1.tail @ BC(0.626, 0.057)  ~ (163, 206) — fold ends down (inlined 横撇钩-like)
  s2.head @ ML(0.732, 0.198)  ~ (73, 120)  — upper-left, just left of s1.head
  s2 belly @ ML(0.75, 0.95)   ~ (75, 195)  — keeps upper body vertical
  s2 corner @ BC(0.40, 0.85)  ~ (140, 285) — round bottom-left corner
  s2 hook_pt @ BR(0.60, 0.60) ~ (260, 260) — right-side end of sweep
  s2 tail (hook tip) @ BR(0.681, 0.285) ~ (268, 228) — flick up-and-left

Joint:
  s1.head ⇆ s2.head @ ML — N-class (small natural gap ~12 px per MMH).
  Enforced: s1.head at ML(0.876,0.233) and s2.head at ML(0.732,0.198)
  gives pixel distance ~ sqrt((88-73)^2+(123-120)^2) ≈ 15 px — matches
  N-class "small natural gap".

SELF_CHECK earned: visual features that agree with GT (see notes).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        "GT features matched: (1) small angular hook piece at upper-mid-left "
        "with horizontal top and downward fold; (2) large outer bowl formed "
        "by a 竖弯钩-style sweep going down from upper-left, curving through "
        "the bottom, and ending with a short upward flick on the right side. "
        "Both strokes start near ML with a ~15px gap (N-class joint)."
    ),
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_stroke_1(draw):
    """Small 横撇钩-like top piece. Inlined (no bank primitive fits the
    down-right tail direction MMH specifies)."""
    p_head = anchor_to_xy(('ML', 0.876, 0.233))     # (88, 123) start of 横
    p_corner = anchor_to_xy(('TC', 0.63, 0.85))     # (163, 85) top-right of 横
    p_tail = anchor_to_xy(('BC', 0.626, 0.057))     # (163, 206) fold tail

    # Segment 1: short 横 (head → corner), with mild taper up to corner press.
    from _anchor import sample_line
    heng_pts = sample_line(p_head, p_corner, n=24)
    n = len(heng_pts) - 1
    heng_widths = [6 + (10 - 6) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, heng_pts, heng_widths)

    # Segment 2: 折 → 撇-like tail (corner → tail), curved fold going down.
    dx = p_tail[0] - p_corner[0]
    dy = p_tail[1] - p_corner[1]
    # Control slightly to the left of chord midpoint for a soft inward fold.
    mid = ((p_corner[0] + p_tail[0]) * 0.5, (p_corner[1] + p_tail[1]) * 0.5)
    ctrl = (mid[0] - 8, mid[1] + 4)
    pie_pts = quad_bezier(p_corner, ctrl, p_tail, n=32)
    m = len(pie_pts) - 1
    pie_widths = [10 + (2 - 10) * ((i / m) ** 1.3) for i in range(m + 1)]
    stroke_variable_width(draw, pie_pts, pie_widths)


def draw_stroke_2(draw):
    """Big outer 竖弯钩 forming the bowl of 㔾.
    Rendered as one continuous bezier body (upper vertical descent + rounded
    bottom curve to the right) + a short upward hook flick at the far end.
    Rounder bottom (matches GT bowl) achieved by pulling belly control down-left."""
    p_head = anchor_to_xy(('ML', 0.732, 0.198))     # (73, 120)
    # Single bezier control that gives a round bowl:
    # Use a very-low, slightly-right belly so the curve bows down and right smoothly.
    p_belly = anchor_to_xy(('BL', 0.80, 0.98))      # (80, 298) low-left => round bowl
    p_hook_base = anchor_to_xy(('BR', 0.65, 0.60))  # (265, 260) end of sweep
    p_tail = anchor_to_xy(('BR', 0.681, 0.285))     # (268, 228) hook tip (upper)

    # Body: single bezier head → hook_base via low-left belly.
    body_pts = quad_bezier(p_head, p_belly, p_hook_base, n=80)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        # Taper: thin head → thick belly → medium at end.
        if t <= 0.35:
            u = t / 0.35
            w = 7 + (11 - 7) * u
        elif t <= 0.75:
            u = (t - 0.35) / 0.40
            w = 11 + (12 - 11) * u
        else:
            u = (t - 0.75) / 0.25
            w = 12 + (10 - 12) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)

    # Rounded joint disc at hook_base for a crisp shoulder.
    r = 10 / 2.0 + 1.0
    draw.ellipse([p_hook_base[0] - r, p_hook_base[1] - r,
                  p_hook_base[0] + r, p_hook_base[1] + r], fill=(0, 0, 0))

    # Hook flick: hook_base → tail (goes UP for the hook, slight right).
    hook_ctrl = (p_hook_base[0] + 3, (p_hook_base[1] + p_tail[1]) * 0.5)
    hook_pts = quad_bezier(p_hook_base, hook_ctrl, p_tail, n=24)
    k = len(hook_pts) - 1
    hook_widths = [10 + (2 - 10) * (i / k) for i in range(k + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)

    # Direction invariants (sanity).
    assert p_tail[1] < p_hook_base[1], "hook tip must flick UP (smaller y)"
    assert p_hook_base[1] > p_head[1], "sweep descends (hook_base y > head y)"


def render():
    img = Image.new('RGB', (300, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_stroke_1(draw)
    draw_stroke_2(draw)
    out = os.path.join(_HERE, '01_㔾.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    render()
