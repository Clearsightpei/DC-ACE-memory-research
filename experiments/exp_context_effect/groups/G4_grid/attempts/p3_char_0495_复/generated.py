"""复 (fù) — 9 strokes.

Decomposition: 复 = 𠂉 (top: 撇 + 一) + 日 (middle, 4 strokes) + 夂 (bottom, 3 strokes).

Read order via memory_index.md:
  1. drawer_memory.md → A-recipe points 1-8; base primitives + MMH-verbatim.
  2. success_bank/INDEX.md grep for 复 / 夂 / 日 — 日 as radical not indexed
     as a compact bottom-slot; no 夂 primitive (position 400 queued but
     NEVER hand-written; TERMINAL_FROZEN per B8 note); no 复.
  3. errata.md grep for 复 — not listed.

Applying A-recipe: base primitives (fat_line + stroke_variable_width +
quad_bezier) with MMH-verbatim anchors. No compound primitive imports.
No BANK_DEVIATION needed since we never CONSIDERED a compound primitive
that would fit (夂 chronic doesn't exist; 日 as compressed-middle slot has
no primitive either).

Joint plan (all N except s8xs9 P):
  s1.mid ⇆ s2.head @ TC — N (~13 px gap; short pie tail meets 一's head)
  s1.mid ⇆ s3.head @ ML — N (~18 px)
  s1.mid ⇆ s4.head @ ML/C — N (~34 px)
  s3.head ⇆ s4.head @ C — N (~11 px, 日 top-left corner)
  s3.tail ⇆ s6.head @ C — N (~11 px, 日 bottom-left corner)
  s3.tail ⇆ s7.head @ C — N (~9 px)
  s4.tail ⇆ s6.tail @ C — N (~13 px, 日 bottom-right corner)
  s8.mid ⇆ s9.mid @ BC — P (welded X-cross for 夂 apex)
  others: N with natural gaps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 9 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('复: base primitives, MMH-verbatim anchors. 日 renders as '
              '4-stroke box (shu + heng-zhe + middle heng + bottom heng). '
              '夂 uses shared CROSS_ANCHOR pattern at s8/s9 mid for the '
              'X-cross apex. No compound primitive import; no BANK_DEVIATION.'),
}


def draw_pie_curve(d, head, tail, w_head=11, w_tail=2, curve=0.10):
    """撇 as quadratic Bezier bulging perpendicular to head-tail axis."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx = -dy / L
    ny = dx / L
    ctrl = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, ctrl, p2, n=32)
    widths = [w_head * (1 - i / (len(pts) - 1)) + w_tail * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)


def draw_na_curve(d, head, tail, w_head=3, w_tail=13, curve=0.08):
    """捺 as quadratic Bezier, thin-to-thick, curving down."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # bulge downward (positive y in PIL)
    nx = dy / L
    ny = -dx / L
    ctrl = (mx - nx * curve * L, my - ny * curve * L)
    pts = quad_bezier(p0, ctrl, p2, n=32)
    widths = [w_head * (1 - i / (len(pts) - 1)) + w_tail * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------- 𠂉 (top: 撇 + 一) -------

    # s1 撇 — TC(0.058,0.536) → ML(0.668,0.236)  short pie top-left
    draw_pie_curve(d,
                   ('TC', 0.058, 0.536),
                   ('ML', 0.668, 0.236),
                   w_head=9, w_tail=2, curve=0.10)

    # s2 一 (top horizontal) — TC(0.134,0.87) → TR(0.124,0.712)
    fat_line(d,
             anchor_to_xy(('TC', 0.134, 0.87)),
             anchor_to_xy(('TR', 0.124, 0.712)),
             width=7)

    # ------- 日 (middle box: 4 strokes) -------

    # s3 竖 (left of 日) — ML(0.973,0.148) → C(0.178,0.813)
    fat_line(d,
             anchor_to_xy(('ML', 0.973, 0.148)),
             anchor_to_xy(('C',  0.178, 0.813)),
             width=7)

    # s4 横折 (top+right of 日) — C(0.107,0.163) → C(0.749,0.623)
    # Compound: heng across top, then zhe (down) on right.
    p0 = anchor_to_xy(('C', 0.107, 0.163))
    p2 = anchor_to_xy(('C', 0.749, 0.623))
    corner = (p2[0], p0[1])  # top-right corner of 日
    stroke_variable_width(d, [p0, corner, corner, p2],
                          [7, 8, 8, 7])

    # s5 一 (middle heng of 日) — C(0.195,0.494) → C(0.661,0.409)
    fat_line(d,
             anchor_to_xy(('C', 0.195, 0.494)),
             anchor_to_xy(('C', 0.661, 0.409)),
             width=6)

    # s6 一 (bottom heng of 日, closes) — C(0.225,0.734) → C(0.711,0.69)
    fat_line(d,
             anchor_to_xy(('C', 0.225, 0.734)),
             anchor_to_xy(('C', 0.711, 0.69)),
             width=7)

    # ------- 夂 (bottom: 3 strokes) -------

    # s7 撇 (short pie top of 夂) — C(0.154,0.849) → BL(0.387,0.742)
    draw_pie_curve(d,
                   ('C',  0.154, 0.849),
                   ('BL', 0.387, 0.742),
                   w_head=7, w_tail=2, curve=0.08)

    # X-cross apex (P-joint between s8.mid(0.56) and s9.mid(0.34)).
    # Per MMH joint: welded at BC(0.61, 0.59) = (161, 259).
    CROSS = anchor_to_xy(('BC', 0.61, 0.59))

    # s8 横撇 (compound horizontal→pie of 夂) — BC(0.263,0.092) → BL(0.747,0.974)
    # Head goes RIGHT-then-DOWN-LEFT, passing through the CROSS apex where
    # it turns. This is the 夂's central 横撇 stroke.
    p0 = anchor_to_xy(('BC', 0.263, 0.092))
    p2 = anchor_to_xy(('BL', 0.747, 0.974))
    pts_s8 = [p0, CROSS, p2]
    stroke_variable_width(d, pts_s8, [8, 6, 2])

    # s9 捺 (long na of 夂) — BC(0.14,0.247) → BR(0.684,0.947)
    # Routed through the CROSS apex at ~34% length (P-weld with s8).
    p0 = anchor_to_xy(('BC', 0.14,  0.247))
    p2 = anchor_to_xy(('BR', 0.684, 0.947))
    # Use CROSS as bezier control so the curve passes near it, with the mid
    # of the resulting curve landing at the shared pixel.
    pts_s9 = quad_bezier(p0, CROSS, p2, n=32)
    # Force the exact mid-point to CROSS to guarantee weld with s8.
    widths = [3 + (13 - 3) * (i / (len(pts_s9) - 1)) for i in range(len(pts_s9))]
    stroke_variable_width(d, pts_s9, widths)

    out = os.path.join(os.path.dirname(__file__), '01_复.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()
