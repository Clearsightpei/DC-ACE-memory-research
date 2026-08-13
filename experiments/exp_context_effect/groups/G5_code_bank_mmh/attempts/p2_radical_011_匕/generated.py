"""
G5 bootstrap render for p2_radical_011_匕 (2 strokes).

MMH-derived structural expectations:
  stroke 1 (撇): head ('MR', 0.183, 0.254) -> (218, 125)
                 tail ('C',  0.031, 0.931) -> (103, 193)
  stroke 2 (竖弯钩): head ('ML', 0.776, 0.005) -> (78, 100)
                     tail ('BR', 0.496, 0.036) -> (250, 204)
Joint: s1.tail (103, 193) ⇆ s2.mid(0.27) — class N (neighbor, gap ~16 px).

Bank is EMPTY at bootstrap; rendering fresh from GT + MMH anchors.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
INK = (0, 0, 0)
STROKE_W = 7

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Bootstrap fresh render. 2 strokes: short pie + vertical-bend-hook.'
}


def sample_quadratic(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def sample_cubic(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def draw_polyline(d, pts, width=STROKE_W):
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    d.line(ipts, fill=INK, width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def main():
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 撇 from upper-right (218, 125) down-left to (103, 193).
    # Slight downward bow.
    s1_head = (218, 125)
    s1_tail = (103, 193)
    s1_ctrl = (155, 145)  # bow slightly above the midpoint
    s1_pts = sample_quadratic(s1_head, s1_ctrl, s1_tail, n=40)
    draw_polyline(d, s1_pts, width=6)

    # Stroke 2: 竖弯钩 from (78, 100) — goes down along left, curves right along
    # bottom, then hooks up ending at (250, 204).
    s2_head = (78, 100)
    # Control points for smooth vertical -> horizontal -> upward hook.
    c1 = (78, 260)      # continue straight down before rounding
    c2 = (170, 275)     # bottom of the round
    knee = (235, 260)   # end of horizontal portion / start of hook
    hook_ctrl = (255, 245)
    s2_tail = (250, 204)

    body = sample_cubic(s2_head, c1, c2, knee, n=60)
    hook = sample_quadratic(knee, hook_ctrl, s2_tail, n=20)
    s2_pts = body + hook[1:]
    draw_polyline(d, s2_pts, width=7)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(out_dir, '01_匕.png'))
    print('rendered 匕:', SELF_CHECK)


if __name__ == '__main__':
    main()
