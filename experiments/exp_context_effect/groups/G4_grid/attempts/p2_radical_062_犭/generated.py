"""犭 (quǎn — 反犬旁) — 3-stroke standalone radical.

Anchor plan (米字格, PIL-native y-down):
  stroke 1: short 撇 crossing near top. Head TR area, tail down-left into C.
            Head ('TR', 0.15, 0.15)  →  tail ('C', 0.35, 0.45).
            width: head 10, tail 2 (tapered 撇).
  stroke 2: long 撇 forming the spine. From upper-mid sweeping down to BL.
            Head ('TC', 0.55, 0.05)  →  tail ('BL', 0.20, 0.90).
            width: head 12, tail 2, curve 0.10.
  stroke 3: 弯 body — a curved sweep from mid down-and-right hooking left.
            Head ('C', 0.15, 0.35)    (touches spine at ~mid, N-class)
            belly ('MR', 0.20, 0.55)  (bulges right)
            tail ('BC', 0.65, 0.85)   (ends near bottom-center)

Joints (per MMH + TR9/TR10):
  s1 crosses s2 near cell C — P (welded crossing). Anchor-space check:
    s1 chord passes ~(('C', 0.35, 0.45)) area
    s2 chord passes near same C region at similar y — near-crossing.
  s2.mid  ⇆  s3.head near C — N (small natural gap, ≤25 px per TR10).

SELF_CHECK is at top; two-pass render allowed.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width

# ----- anchors -----
# GT analysis: stroke 1 is a short 撇 that CROSSES the top of stroke 2
# (P-class weld near the upper-third). Stroke 2 is the dominant spine
# sweeping from upper-mid down to lower-left. Stroke 3 is the belly
# 弯 curve — starts on the spine mid, bulges right, ends near bottom.
# Placement: they intersect near ('TC',0.6,0.7) ≈ px (170, 90) so both
# strokes must pass through that vicinity.

S1_HEAD = ('TC', 0.80, 0.10)   # upper-right of top-center
S1_TAIL = ('TC', 0.20, 0.85)   # lower-left of top-center — short 撇 within TC
# stroke 1 lives mostly in the TC cell so it stays a SHORT 撇 near the top.

S2_HEAD = ('TC', 0.45, 0.05)   # start slightly left of center, top row
S2_TAIL = ('BL', 0.20, 0.90)   # sweep to bottom-left corner

# Stroke 3 belly — head sits ON stroke 2's body around mid (N-class per MMH;
# but per TR10 we place it very close to the spine so it reads as connected).
S3_HEAD  = ('C',  0.30, 0.45)  # on spine mid area
S3_BELLY = ('MR', 0.05, 0.65)  # bulges right
S3_TAIL  = ('BC', 0.55, 0.90)  # ends near bottom-center


def draw_pie_stroke(draw, head, tail, head_w=12, tail_w=2, curve=0.10, segments=48):
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx*dx + dy*dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0]+p2[0])*0.5, (p0[1]+p2[1])*0.5)
    ctrl = (mid[0] + perp[0]*bow, mid[1] + perp[1]*bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i/segments) for i in range(segments+1)]
    stroke_variable_width(draw, pts, widths)
    return pts


def draw_belly_curve(draw, head, belly, tail, head_w=8, belly_w=11, tail_w=3, segments=60):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(belly)
    p2 = anchor_to_xy(tail)
    pts = quad_bezier(p0, p1, p2, n=segments)
    widths = []
    for i in range(segments+1):
        t = i / segments
        if t <= 0.5:
            u = t / 0.5
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.5) / 0.5
            w = belly_w + (tail_w - belly_w) * u
        widths.append(w)
    stroke_variable_width(draw, pts, widths)
    return pts


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # stroke 1 — short 撇 (top)
    s1_pts = draw_pie_stroke(draw, S1_HEAD, S1_TAIL,
                             head_w=10, tail_w=2, curve=0.08)

    # stroke 2 — long spine 撇
    s2_pts = draw_pie_stroke(draw, S2_HEAD, S2_TAIL,
                             head_w=12, tail_w=2, curve=0.10)

    # stroke 3 — belly / 弯 curve
    s3_pts = draw_belly_curve(draw, S3_HEAD, S3_BELLY, S3_TAIL,
                              head_w=8, belly_w=11, tail_w=4)

    # ---- sanity assertions ----
    p_s1_head = anchor_to_xy(S1_HEAD)
    p_s1_tail = anchor_to_xy(S1_TAIL)
    p_s2_head = anchor_to_xy(S2_HEAD)
    p_s2_tail = anchor_to_xy(S2_TAIL)
    p_s3_head = anchor_to_xy(S3_HEAD)
    p_s3_tail = anchor_to_xy(S3_TAIL)

    # s1 goes down-and-left (撇): tail below head, tail left of head
    assert p_s1_tail[1] > p_s1_head[1], 's1 tail must be below head'
    assert p_s1_tail[0] < p_s1_head[0], 's1 tail must be left of head'
    # s2 same
    assert p_s2_tail[1] > p_s2_head[1], 's2 tail must be below head'
    assert p_s2_tail[0] < p_s2_head[0], 's2 tail must be left of head'
    # s3 belly curve: tail is below-right of head (下弯 out to right)
    assert p_s3_tail[1] > p_s3_head[1], 's3 tail below head'
    assert p_s3_tail[0] > p_s3_head[0], 's3 tail right of head'

    # N-joint check: s2 midpoint pixel distance to s3 head
    s2_mid = s2_pts[len(s2_pts)//2]
    n_gap = ((s2_mid[0]-p_s3_head[0])**2 + (s2_mid[1]-p_s3_head[1])**2) ** 0.5
    print(f'N-joint s2.mid ⇆ s3.head gap = {n_gap:.1f} px')

    # P-joint check: s1 crosses s2 near center
    # find closest approach between s1_pts and s2_pts
    best = 1e9
    for a in s1_pts[::4]:
        for b in s2_pts[::4]:
            d = ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5
            if d < best:
                best = d
    print(f'P-joint s1 ⇆ s2 closest approach = {best:.1f} px')

    out = os.path.join(os.path.dirname(__file__), '01_犭.png')
    img.save(out)
    print(f'saved -> {out}')


SELF_CHECK = {
    'visual_ok': False,  # Honest: s1 does not visibly CROSS s2 (gap 21.6 px,
                         # not a welded P). GT shows a clear X-cross at top.
    'stroke_count_ok': True,       # 3 strokes rendered (s1 short 撇, s2 long 撇, s3 belly)
    'endpoint_mismatches': [
        # TR9 override: MMH anchors are sub-region hints; expanded to
        # full 米字格 span for a standalone radical.
        {'stroke': 1, 'expected': "('TC',0.594,0.741)/('ML',0.894,0.673)",
         'actual':   "('TC',0.80,0.10)/('TC',0.20,0.85)",
         'delta':    'TR9 override: short 撇 kept inside TC cell'},
        {'stroke': 2, 'expected': "('TC',0.072,0.943)/('BC',0.154,0.692)",
         'actual':   "('TC',0.45,0.05)/('BL',0.20,0.90)",
         'delta':    'TR9 override: full anti-diagonal spine'},
        {'stroke': 3, 'expected': "('C',0.518,0.623)/('BL',0.817,0.522)",
         'actual':   "('C',0.30,0.45)/('BC',0.55,0.90)",
         'delta':    'TR9 override: belly bulges right, ends near BC'},
    ],
    'joint_class_mismatches': [
        # s1×s2 was declared P but pixel gap 21.6 px is a near-cross, not
        # a welded intersection. Real cross would have gap 0.
        {'joint': 's1×s2', 'expected_class': 'P', 'actual_class': 'N (near-cross, 21.6 px)'},
        # s2.mid ⇆ s3.head declared N (≤25 px). Actual 61.9 px — too far.
        {'joint': 's2.mid ⇆ s3.head', 'expected_class': 'N (≤25 px)',
         'actual_class': 'N-fragmented (61.9 px)'},
    ],
    'overall_pass': False,
    'notes': (
        'Two agreements vs GT (TR11): (1) both show a long 撇 spine '
        'sweeping from upper-mid down to lower-left; (2) both show a '
        'curved belly bulging right of the spine and ending near the '
        'bottom. Remaining defects (submitted after 2 passes as per '
        'shared_rules limit): the top X-cross between s1 and s2 does '
        'not visibly weld — a small ~22 px gap remains where GT has a '
        'clear intersection. The s2/s3 mid-joint reads as fragmented '
        '(62 px) rather than N-connected. Root cause hypothesis: s3 '
        'head anchor should share stroke 2\'s midpoint pixel-x, not '
        'sit statically at C(0.30, 0.45). Deferred to sandbox for '
        'future 3-stroke 撇 radicals.'
    ),
}


if __name__ == '__main__':
    main()
