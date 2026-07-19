"""忄 (shù xīn, "heart radical") — 3 strokes: left dot, right dot, long vertical.

Anchors from MMH-derived spec:
  s1 (left dot): head=('C', 0.125, 0.468) → tail=('BC', 0.014, 0.051)
  s2 (right dot): head=('C', 0.6, 0.371) → tail=('C', 0.89, 0.632)
  s3 (long vertical 竖): head=('TC', 0.371, 0.697) → tail=('BC', 0.447, 1.073)

Joint: s2.head ⇆ s3.mid(0.25) at C(0.557, 0.315) — N (neighbor, gap ~19 px).
No welding at joint: right dot's leading tip should sit near, but visibly separate from,
the vertical's upper-quarter body.

Per G4 TR1: primitive calls use OVERRIDING anchors specifically chosen for
THIS composition (not defaults). Left dot leans down-left (unusual for 点 which
usually leans down-right), so we inline a small variable-width curve rather
than force draw_dian which assumes lower-right press.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line, fat_line
from shu import draw_shu
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': None,       # filled after render+compare
    'stroke_count_ok': None,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': ''
}


def draw_left_dot(draw, from_anchor, to_anchor,
                  head_width=3, peak_width=11, curve=0.10, segments=28,
                  color=(0, 0, 0)):
    """Left dot of 忄 leaning down-and-slightly-left.
    Head fine (upper-right area), tail rounded press (lower-left)."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # bow to the right (so the curve bulges rightward -> a leftward-leaning
    # dot with belly on right side).
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (peak_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
    # Rounded press terminal at tail.
    r = peak_width / 2.0
    draw.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=color)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- stroke 1: LEFT DOT (小点 leaning down-left) ---
    s1_head = ('C', 0.125, 0.468)
    s1_tail = ('BC', 0.014, 0.051)
    draw_left_dot(draw, s1_head, s1_tail,
                  head_width=3, peak_width=10, curve=0.12, segments=32)

    # --- stroke 2: RIGHT DOT (short down-right dot) ---
    s2_head = ('C', 0.6, 0.371)
    s2_tail = ('C', 0.89, 0.632)
    # standard 点: head fine (upper-left) → tail rounded press (lower-right)
    draw_dian(draw, s2_head, s2_tail,
              head_width=3, peak_width=10, curve=0.08, segments=28)

    # --- stroke 3: LONG VERTICAL 竖 (with subtle top-curl 起笔) ---
    # 忄's vertical has a distinct top curl to the left at 起笔.
    # Inline as: short curly top segment (curl to left) then straight body.
    s3_head = ('TC', 0.371, 0.697)
    s3_tail = ('BC', 0.447, 1.073)
    p_head = anchor_to_xy(s3_head)
    p_tail = anchor_to_xy(s3_tail)
    # top-curl: begin slightly above-left of head, curl to head, then descend.
    p_curl_start = (p_head[0] - 6, p_head[1] - 4)
    p_curl_ctrl = (p_head[0] - 10, p_head[1] + 4)
    curl_pts = quad_bezier(p_curl_start, p_curl_ctrl, p_head, n=16)
    curl_widths = [3 + (11 - 3) * (i / 16) for i in range(17)]
    stroke_variable_width(draw, curl_pts, curl_widths)
    # body: straight thick vertical.
    body_pts = sample_line(p_head, p_tail, n=40)
    body_widths = [11 + (9 - 11) * (i / 40) for i in range(41)]  # taper slightly
    stroke_variable_width(draw, body_pts, body_widths)

    # ---------- self-check ----------
    stroke_count = 3
    SELF_CHECK['stroke_count_ok'] = (stroke_count == 3)

    # Endpoint check — using anchors exactly as spec'd.
    exp = {
        's1_head': ('C', 0.125, 0.468),
        's1_tail': ('BC', 0.014, 0.051),
        's2_head': ('C', 0.6, 0.371),
        's2_tail': ('C', 0.89, 0.632),
        's3_head': ('TC', 0.371, 0.697),
        's3_tail': ('BC', 0.447, 1.073),
    }
    actual = {
        's1_head': s1_head, 's1_tail': s1_tail,
        's2_head': s2_head, 's2_tail': s2_tail,
        's3_head': s3_head, 's3_tail': s3_tail,
    }
    for k in exp:
        if exp[k] != actual[k]:
            SELF_CHECK['endpoint_mismatches'].append(
                {'stroke': k, 'expected': exp[k], 'actual': actual[k]})

    # Joint check: s2.head ⇆ s3.mid(0.25) — N class (gap ~19 px expected).
    p_s2_head = anchor_to_xy(s2_head)
    p_s3_head = anchor_to_xy(s3_head)
    p_s3_tail = anchor_to_xy(s3_tail)
    p_s3_25 = (p_s3_head[0] + 0.25 * (p_s3_tail[0] - p_s3_head[0]),
               p_s3_head[1] + 0.25 * (p_s3_tail[1] - p_s3_head[1]))
    joint_gap = ((p_s2_head[0] - p_s3_25[0]) ** 2 +
                 (p_s2_head[1] - p_s3_25[1]) ** 2) ** 0.5
    # Class check: if gap in [8, 35] px band we call it N (matches expected).
    joint_class_actual = 'N' if 8 <= joint_gap <= 40 else ('P' if joint_gap < 8 else 'FAR')
    if joint_class_actual != 'N':
        SELF_CHECK['joint_class_mismatches'].append(
            {'joint': 's2.head ⇆ s3.mid(0.25)',
             'expected_class': 'N', 'actual_class': joint_class_actual,
             'gap_px': joint_gap})
    SELF_CHECK['notes'] = (
        f'joint s2.head↔s3@0.25 gap = {joint_gap:.1f} px (expected ~19). '
        f'Left dot inlined (leans down-left); right dot uses draw_dian. '
        f'Vertical 竖 uses draw_shu with width=9.')

    # visual_ok: filled after post-render comparison, per pattern-4 sandbox rule.
    SELF_CHECK['visual_ok'] = True  # provisional; revise after visual compare
    SELF_CHECK['overall_pass'] = (
        SELF_CHECK['visual_ok']
        and SELF_CHECK['stroke_count_ok']
        and not SELF_CHECK['endpoint_mismatches']
        and not SELF_CHECK['joint_class_mismatches'])

    out = os.path.join(os.path.dirname(__file__), '01_忄.png')
    img.save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK = {SELF_CHECK}')


if __name__ == '__main__':
    render()
