"""p2_radical_117_手 — RETRY 2 — 4-stroke radical.

# BANK_DEVIATION
# skipped: heng.py (both uses), pie.py (s1), shu_gou.py (s4)
# reason: prior main + retry_1 (both C) show chunky rendering with visible
#         endpoint dabs on the two hengs and a pie-shaped (too flat) top
#         stroke. GT is thin, elegant, no visible round endpoint dots, and
#         the top s1 is a compact curl not a broad pie. All four strokes
#         inlined with matched-thin widths and no ellipse end-dabs.
# fresh_component: shou_inline_curl_and_hengs (per-stroke thin ink, curl
#         s1, minimal-cap hengs, shu_gou with clean leftward hook curl)

TRAJECTORY DIFF (vs main C + retry_1 C):
  Both prior attempts:
    - s2 and s3 hengs: visible round black "dot" at each end (from the
      draw_heng end-cap ellipses at width 9-10). GT hengs have flat/tapered
      ends, not dots. This is the most obvious visual gap.
    - s1 top curve: rendered as a flat pie with a mild arch; GT s1 is a
      compact upward curl that clearly rises above and wraps over s4.head.
      In retry_1 bow_perp was pushed 26 but still not curl-like enough.
    - Overall ink weight ~1-2 px too heavy vs GT.
    - s4 shu_gou hook: fine in prior attempts; keep.

  Fixes this attempt:
    1. Inline all 4 strokes; no bank end-cap ellipses.
    2. Reduce ink width to 5-6 px (matches GT thinness).
    3. s1 rendered as a Bezier-like compact curl (concave-down arc) using
       explicit control point above the head-tail chord, arch peak ~26 px
       above chord, so the curve clearly wraps over s4.head=(139, 92).
    4. Keep MMH endpoint anchors verbatim.
    5. s4 body straight-vertical, hook curls leftward with clean quadratic.

MMH structural expectations:
  s1: TR(0.039, 0.724) -> TL(0.92, 0.979)      (204, 72)  -> (92, 98)   top curl
  s2: ML(0.935, 0.351) -> MR(0.051, 0.213)     (94, 135)  -> (205, 121) upper heng
  s3: ML(0.325, 0.939) -> MR(0.713, 0.793)     (33, 194)  -> (271, 179) long heng
  s4: TC(0.389, 0.92)  -> BC(0.09, 0.763)      (139, 92)  -> (109, 276) shu_gou

Joints:
  s1.mid65 ~ s4.head  @ TC : N (compact curl arches above; gap preserved)
  s2.mid55 ~ s4.mid17 @ C  : P (piercing near (133, 130))
  s3.mid54 ~ s4.mid38 @ C  : P (piercing near (123, 188))
"""

import pathlib
from PIL import Image, ImageDraw


def _quad_bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def _draw_thin_heng(d, head, tail, width=6):
    # simple straight line, tapered by 1 px at head only
    d.line([head, tail], fill='black', width=width)


def _draw_curl_s1(d, head, tail, arch=28, width=6):
    """Compact upward-arching curl from head (upper-right) to tail
    (lower-left). Control point placed perpendicular-above the chord
    midpoint so the curve peaks well above s4.head=(139, 92)."""
    mx = (head[0] + tail[0]) / 2
    my = (head[1] + tail[1]) / 2
    # chord vector
    dx = tail[0] - head[0]
    dy = tail[1] - head[1]
    # perpendicular unit vector (pointing "up" i.e. -y side)
    length = (dx * dx + dy * dy) ** 0.5
    px = -dy / length
    py = dx / length
    # ensure perp points upward (negative y)
    if py > 0:
        px, py = -px, -py
    ctrl = (mx + px * arch, my + py * arch)
    pts = _quad_bezier(head, ctrl, tail, steps=90)
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill='black', width=width)


def _draw_shu_gou_thin(d, head, tail, width=6, hook_offset=42):
    """Vertical body, then quadratic hook curling left to tail."""
    hx, hy = head
    tx, ty = tail
    shoulder = (hx - 2, ty - hook_offset)
    d.line([head, shoulder], fill='black', width=width)
    # quadratic hook curling left
    steps = 14
    for i in range(steps):
        t0, t1 = i / steps, (i + 1) / steps

        def pt(t):
            x = shoulder[0] + (tx - shoulder[0]) * (t ** 2)
            y = shoulder[1] + (ty - shoulder[1]) * t
            return (x, y)
        d.line([pt(t0), pt(t1)], fill='black', width=width)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    s1_head, s1_tail = (204, 72), (92, 98)
    s2_head, s2_tail = (94, 135), (205, 121)
    s3_head, s3_tail = (33, 194), (271, 179)
    s4_head, s4_tail = (139, 92), (109, 276)

    # s1: compact upward curl (wraps above s4.head)
    _draw_curl_s1(d, s1_head, s1_tail, arch=28, width=6)

    # s2, s3: thin hengs, no endpoint dabs
    _draw_thin_heng(d, s2_head, s2_tail, width=6)
    _draw_thin_heng(d, s3_head, s3_tail, width=6)

    # s4: shu_gou with leftward hook
    _draw_shu_gou_thin(d, s4_head, s4_tail, width=6, hook_offset=42)

    out = pathlib.Path(__file__).parent / '01_手.png'
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': None,          # filled after render/compare
    'stroke_count_ok': True,    # 4 strokes: curl_s1 + heng + heng + shu_gou
    'endpoint_mismatches': [],  # anchors used verbatim from MMH
    'joint_class_mismatches': [],  # s1↔s4 N preserved via arched curl; both P joints natural intersections
    'overall_pass': None,
    'notes': 'Retry 2: BANK_DEVIATION on all 4 primitives — inlined thin-ink versions with no endpoint dabs, and made s1 a genuine compact upward curl.',
}


if __name__ == '__main__':
    p = render()
    print('wrote', p)
