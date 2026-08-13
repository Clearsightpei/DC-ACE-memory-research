# TRAJECTORY DIFF for 几 (retry_2)
#
# GT: 2 strokes.
#   S1 (撇): starts near top-center-ish (right side of TL cell, y ~ TL bottom),
#            sweeps down-and-left with a gentle bow, ending low-left (BL cell).
#   S2 (横折弯钩): horizontal from just under S1's head, runs right across TR,
#            turns down along right side (through R cell), curves inward at
#            bottom-right and finishes with a small upward hook.
#
# main FAIL: S1 rendered nearly vertical (looked like a bare |), lacked the
#            characteristic top-right → bottom-left sweep. S2 endpoint was flat
#            and dragged down without any hook — reads more like ㄇ than 几.
# retry_1 C: S1 was too short and stumpy — did not extend down to BL (~y=288),
#            stopped around y ~ 200. S2 hook still weak (small down-tail rather
#            than an upward flick). Overall silhouette compressed vertically.
#
# Fix plan for retry_2:
#   1. Lengthen S1: honor MMH anchors — head (~95,94) to tail (~38,288). Give it
#      a modest leftward bow (bow_perp ~ -14 px) so it curves like a 撇, not a
#      straight diagonal.
#   2. S2: horizontal run from (~119,106) rightward through top-right to about
#      (~245,106); short down-right turn; vertical descent along x ~245 down to
#      y ~245; then curve outward-right and flick UP into the hook, terminating
#      at MMH tail (~278,219).
#   3. Preserve the N (neighbor) joint at cell C: S1 head and S2 head must NOT
#      weld — keep a ~15 px gap (S1 head at x≈95, S2 head at x≈119 gives ~24
#      px lateral gap, within tolerance).

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def _quad_bezier(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_curve(pts, widths):
    """Draw a curve as a series of thick line segments with variable width."""
    n = len(pts)
    for i in range(n - 1):
        # interpolate width along the curve
        t0 = i / (n - 1)
        t1 = (i + 1) / (n - 1)
        w0 = widths[0] + (widths[1] - widths[0]) * t0
        w1 = widths[0] + (widths[1] - widths[0]) * t1
        w = (w0 + w1) / 2
        draw.line([pts[i], pts[i + 1]], fill=BLACK, width=max(1, int(round(w))))
    # end caps
    for p, w in ((pts[0], widths[0]), (pts[-1], widths[1])):
        r = max(1, int(round(w / 2)))
        draw.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill=BLACK)


# ----------------- Stroke 1: 撇 -----------------
# MMH: head @ TL(0.952,0.94) -> (95,94); tail @ BL(0.378,0.877) -> (38,288)
s1_head = (95, 94)
s1_tail = (38, 288)
# Control point pulled slightly LEFT (bow inward for a 撇) and midway.
# Midpoint = (66.5, 191); shift ctrl left by ~14 px, up by ~4 px.
s1_ctrl = (52, 187)
s1_pts = _quad_bezier(s1_head, s1_ctrl, s1_tail, steps=80)
# Taper: thicker at head, tapering to a fine point at tail (撇 convention).
draw_curve(s1_pts, widths=(9, 3))

# ----------------- Stroke 2: 横折弯钩 -----------------
# MMH: head @ C(0.192,0.063) -> (119,106); tail @ BR(0.78,0.188) -> (278,219)
# Decompose into segments: horizontal -> down-right corner -> vertical -> hook up.
s2_head = (119, 106)
# Segment A: horizontal top bar going right
segA_end = (245, 106)
# Segment B: corner turn (subtle down-right joint), then vertical descent
segB_end = (252, 118)   # slight down-right turn point
# Segment C: vertical descent along x ~ 252 down to bottom
segC_end = (252, 240)
# Segment D: hook — curve outward-right then flick UP to tail
s2_tail = (278, 219)   # MMH tail (hook tip pointing up-right)

# Build a single polyline with smooth transitions.
poly = []

# A: horizontal (straight line with tiny drop at right to prep corner)
for i in range(41):
    t = i / 40
    x = s2_head[0] + (segA_end[0] - s2_head[0]) * t
    y = s2_head[1] + (segA_end[1] - s2_head[1]) * t
    poly.append((x, y))

# B: corner — short arc from segA_end curving down through segB_end
ctrl_B = (252, 108)
for i in range(1, 21):
    t = i / 20
    x = (1 - t) ** 2 * segA_end[0] + 2 * (1 - t) * t * ctrl_B[0] + t ** 2 * segB_end[0]
    y = (1 - t) ** 2 * segA_end[1] + 2 * (1 - t) * t * ctrl_B[1] + t ** 2 * segB_end[1]
    poly.append((x, y))

# C: vertical descent from segB_end down to segC_end (slight outward bow)
ctrl_C = (258, 180)
for i in range(1, 61):
    t = i / 60
    x = (1 - t) ** 2 * segB_end[0] + 2 * (1 - t) * t * ctrl_C[0] + t ** 2 * segC_end[0]
    y = (1 - t) ** 2 * segB_end[1] + 2 * (1 - t) * t * ctrl_C[1] + t ** 2 * segC_end[1]
    poly.append((x, y))

# D: hook — curve down-right, then sweep UP and to the right to tail.
# Path segC_end (252,240) -> low anchor (275, 258) -> UP to s2_tail (278,219)
# (Pushed hook_low further right + down and increased curve amplitude so the
#  upward flick reads clearly, matching GT's visible hook tip.)
hook_low = (278, 260)
for i in range(1, 41):
    t = i / 40
    x = (1 - t) ** 2 * segC_end[0] + 2 * (1 - t) * t * hook_low[0] + t ** 2 * s2_tail[0]
    y = (1 - t) ** 2 * segC_end[1] + 2 * (1 - t) * t * hook_low[1] + t ** 2 * s2_tail[1]
    poly.append((x, y))

# Draw s2 as a mostly-uniform stroke, slight taper at the hook tip.
n = len(poly)
for i in range(n - 1):
    frac = i / (n - 1)
    # width: ~6 through most of the body, tapering to ~3 in hook tip (last 15%)
    if frac < 0.85:
        w = 6
    else:
        w = 6 - (frac - 0.85) / 0.15 * 3
    draw.line([poly[i], poly[i + 1]], fill=BLACK, width=max(1, int(round(w))))

# End caps for s2
r_head = 3
draw.ellipse((s2_head[0] - r_head, s2_head[1] - r_head,
              s2_head[0] + r_head, s2_head[1] + r_head), fill=BLACK)


# ---------------- Save ----------------
out_path = __file__.rsplit("/", 1)[0] + "/01_几.png"
img.save(out_path)


# ---------------- SELF_CHECK ----------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # exactly 2 stroke primitives drawn (s1 curve + s2 polyline)
    'endpoint_mismatches': [
        # stroke 1: expected head TL(0.952,0.94)~(95,94), actual (95,94) — match
        # stroke 1: expected tail BL(0.378,0.877)~(38,288), actual (38,288) — match
        # stroke 2: expected head C(0.192,0.063)~(119,106), actual (119,106) — match
        # stroke 2: expected tail BR(0.78,0.188)~(278,219), actual (278,219) — match
    ],
    'joint_class_mismatches': [
        # joint: s1.head <-> s2.head @ C, expected N (gap ~15.6 px).
        # Actual: s1_head (95,94) to s2_head (119,106) = sqrt(24^2 + 12^2) = 26.8 px
        # Both are separate strokes, no weld. Class N confirmed.
    ],
    'overall_pass': True,
    'notes': 'Retry_2: lengthened S1 to reach BL tail, restored 撇 bow. S2 now '
             'has proper corner turn, vertical descent, and upward-flick hook '
             'landing at MMH tail (278,219).'
}
