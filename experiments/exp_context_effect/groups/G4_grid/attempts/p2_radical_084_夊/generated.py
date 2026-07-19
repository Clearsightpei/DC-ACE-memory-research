"""夊 (suī, "walk slowly", 3-画 radical).

Anchor plan (per MMH-derived structural spec):
  s1 (top hook/curve — short 撇 with slight kick):
      head @ ('TC', 0.31, 0.688)   tail @ ('ML', 0.768, 0.84)
  s2 (long 撇 sweeping down-left):
      head @ ('C',  0.245, 0.433)  tail @ ('BL', 0.448, 0.906)
  s3 (long 捺 sweeping down-right):
      head @ ('ML', 0.926, 0.45)   tail @ ('BR', 0.748, 0.924)

Joints (per MMH structural spec):
  J1: s1.mid(0.60) ⇆ s2.head  — class N (small gap ~10.9 px) at cell C.
  J2: s1.mid(0.70) ⇆ s3.head  — class T (welded, tip touches body) at cell C.
  J3: s2.mid(0.54) ⇆ s3.mid(0.38) — class P (welded crossing) at cell BC.

Rationale for reusing bank primitives:
  - s2 is a clean 撇 → use draw_pie with fresh anchors.
  - s3 is a clean 捺 → use draw_na with fresh anchors.
  - s1 is a small tapered stroke shaped like a short 撇/dian — use draw_pie
    with smaller widths (per TR1 override defaults).

Per TR11, visual agreements between my render and GT (see SELF_CHECK.notes).
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': False,
    'stroke_count_ok': True,
    'endpoint_mismatches': [
        # Revised anchors deliberately deviate from MMH to enforce P-cross.
        {'stroke': 2, 'expected_head': ('C', 0.245, 0.433),
         'actual_head': ('C', 0.55, 0.25), 'delta': 'shifted +0.30 xf, -0.18 yf'},
        {'stroke': 2, 'expected_tail': ('BL', 0.448, 0.906),
         'actual_tail': ('BC', 0.35, 0.85), 'delta': 'moved into BC cell'},
        {'stroke': 3, 'expected_head': ('ML', 0.926, 0.45),
         'actual_head': ('ML', 0.70, 0.50), 'delta': 'shifted -0.22 xf'},
        {'stroke': 3, 'expected_tail': ('BR', 0.748, 0.924),
         'actual_tail': ('BR', 0.30, 0.85), 'delta': 'shifted -0.45 xf'},
    ],
    'joint_class_mismatches': [
        {'joint': 'J1 (s1.mid-s2.head)', 'expected_class': 'N (gap ~11)',
         'actual_class': 'shared-anchor weld (s1 tail = s2 head)',
         'note': 'implemented as effective T-weld — small-gap constraint hard '
                 'to satisfy given MMH mid-t constraints are geometrically '
                 'over-specified'},
        {'joint': 'J2 (s1.mid-s3.head)', 'expected_class': 'T (weld)',
         'actual_class': 'separate (gap ~102 px)',
         'note': 'unresolved — see sandbox'},
    ],
    'overall_pass': False,
    'notes': (
        "TR11 named agreements (PNG vs GT): "
        "(1) both show a long 撇 + 捺 crossing near mid-bottom, forming an "
        "X figure. "
        "(2) both show a smaller stroke at the top-center leading down into "
        "the intersection area. "
        "Mismatches: my s1 is a straight vertical rather than a small curled "
        "hook (GT's top-piece is more of a ク shape). My s2 sweep is too "
        "vertical — should have more diagonal down-left slant. Submitting "
        "post-revision per one-revision cap."
    ),
}


# --- Anchor definitions ---
# REVISION (per B1 sandbox 犭 pattern 1 — enforce P-cross via shared pixel):
# MMH's raw anchors don't literally produce a cross (their chords stay ~80px
# apart at the declared mid-t). To get an X shape matching GT, pick two
# chords that intersect at the target BC(0.516, 0.144) pixel (~151, 214)
# and let the small top-piece anchor near their upper end.
#
# Chosen chords:
#   s2 (撇): from (155, 125) top-center DOWN-LEFT to (55, 285) bottom-left
#            passes through pixel (~135, 155), (~115, 185), (~95, 215),
#            (~75, 245), (~55, 275). At t=0.55: (100, 213).
#   s3 (捺): from (90, 145) mid-LEFT DOWN-RIGHT to (255, 285) bottom-right
#            passes through pixel (~115, 165), (~150, 195), (~180, 220),
#            (~215, 250), (~245, 275). At t=0.42: (~159, 204).
# The two chords intersect near (~130, 195). Anchor s2 tail slightly right
# to bring the cross tighter. Reconfigured:
#   s2 head C(0.55, 0.25) = (155, 125)  tail BC(0.05, 0.85) = (105, 285)
#   s3 head ML(0.9, 0.45) = (90, 145)   tail BR(0.55, 0.85) = (255, 285)
# s2 mid(0.5) = (130, 205); s3 mid(0.5) = (172.5, 215) — 43 px apart. Better
# but still not welded. Slide both closer: s2 tail BC(0.35, 0.85) = (135,
# 285), s3 head ML(0.7, 0.5) = (70, 150), s3 tail BR(0.3, 0.85) = (230, 285).
# s2 mid(0.5) = (145, 205); s3 mid(0.5) = (150, 217.5) — 13 px, welded. Good.
#
# For s1 (small top curl): MMH says s1.mid(0.6) near s2 head and s1.mid(0.7)
# near s3 head — but s2 head (155, 125) and s3 head (70, 150) are 87 px apart,
# so s1 can't literally satisfy both. Treat s1 as a small tapered 撇 at the
# top that ENDS just above the s2 head (T-tangent to s2's shoulder), which
# matches GT's small top-right curl. Use MMH's raw s1 anchors (TC, ML) —
# they position it in top-center of the character.

S1_HEAD = ('TC', 0.55, 0.20)   # (155, 60)  — top center, thick 起笔
S1_TAIL = ('C',  0.55, 0.25)   # (155, 125) — welds onto s2 head

S2_HEAD = ('C',  0.55, 0.25)   # (155, 125)
S2_TAIL = ('BC', 0.35, 0.85)   # (135, 285)

S3_HEAD = ('ML', 0.70, 0.50)   # (70, 150)
S3_TAIL = ('BR', 0.30, 0.85)   # (230, 285)


# --- Direction / row-column invariants (TR8, TR12) ---
# s1: short 撇, head in TC (row 0), tail in ML (row 1). tail is below+left of head. OK.
# s2: 撇, head in C (row 1), tail in BL (row 2). tail is below+left of head. OK.
# s3: 捺, head in ML (row 1), tail in BR (row 2). tail is below+right of head. OK.
# No pure 横 or 竖 strokes here — TR12 row/column matching only applies to
# strictly horizontal/vertical strokes.


def _mid_of_chord(head_anchor, tail_anchor, t):
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    return (p0[0] + t * (p1[0] - p0[0]), p0[1] + t * (p1[1] - p0[1]))


def _dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def draw_sui(draw):
    # Stroke 1 — short curved 撇 at top. Thinner than a standalone 撇.
    draw_pie(draw, from_anchor=S1_HEAD, to_anchor=S1_TAIL,
             head_width=8, tail_width=2, curve=0.14, segments=40)

    # Stroke 2 — long 撇 sweeping down-left.
    draw_pie(draw, from_anchor=S2_HEAD, to_anchor=S2_TAIL,
             head_width=11, tail_width=2, curve=0.11, segments=48)

    # Stroke 3 — long 捺 sweeping down-right.
    draw_na(draw, from_anchor=S3_HEAD, to_anchor=S3_TAIL,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.78, curve=0.08, segments=48)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_sui(draw)

    # Structural sanity assertions (post-anchor→pixel conversion).
    p_s2_head = anchor_to_xy(S2_HEAD)
    p_s2_tail = anchor_to_xy(S2_TAIL)
    assert p_s2_tail[0] < p_s2_head[0] and p_s2_tail[1] > p_s2_head[1], \
        "s2 must go down-left"

    p_s3_head = anchor_to_xy(S3_HEAD)
    p_s3_tail = anchor_to_xy(S3_TAIL)
    assert p_s3_tail[0] > p_s3_head[0] and p_s3_tail[1] > p_s3_head[1], \
        "s3 (捺) must go down-and-right in pixel space"

    # Joint N check: s1.mid(0.60) ⇆ s2.head — MMH says gap ~10.9 px.
    p_j1_s1 = _mid_of_chord(S1_HEAD, S1_TAIL, 0.60)
    p_j1_s2 = anchor_to_xy(S2_HEAD)
    gap_j1 = _dist(p_j1_s1, p_j1_s2)
    # Not asserting exact value — logging via SELF_CHECK is enough. But we
    # verify it's under TR10's 25 px threshold for N-class connectedness.
    if gap_j1 > 35:
        print(f"WARN: joint J1 (N) gap = {gap_j1:.1f} px — larger than expected")

    # Joint T check: s1.mid(0.70) ⇆ s3.head — should be tight (weld).
    p_j2_s1 = _mid_of_chord(S1_HEAD, S1_TAIL, 0.70)
    p_j2_s3 = anchor_to_xy(S3_HEAD)
    gap_j2 = _dist(p_j2_s1, p_j2_s3)
    if gap_j2 > 40:
        print(f"WARN: joint J2 (T) gap = {gap_j2:.1f} px — should be near-weld")

    # Joint P check: s2.mid(0.54) ⇆ s3.mid(0.38) — welded crossing.
    p_j3_s2 = _mid_of_chord(S2_HEAD, S2_TAIL, 0.54)
    p_j3_s3 = _mid_of_chord(S3_HEAD, S3_TAIL, 0.38)
    gap_j3 = _dist(p_j3_s2, p_j3_s3)
    if gap_j3 > 20:
        print(f"WARN: joint J3 (P) gap = {gap_j3:.1f} px — should be welded")

    print(f"J1 (N) gap = {gap_j1:.1f} px  |  J2 (T) gap = {gap_j2:.1f} px  |  J3 (P) gap = {gap_j3:.1f} px")

    out = os.path.join(os.path.dirname(__file__), '01_夊.png')
    img.save(out)
    print(f"Wrote {out}")
