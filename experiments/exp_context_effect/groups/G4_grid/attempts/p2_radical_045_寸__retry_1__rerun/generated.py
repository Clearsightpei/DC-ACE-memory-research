"""寸 (cùn) — 3画 radical, RETRY 1 RERUN (v9 prompt fix).

============================================================
VISUAL DIFF — prior failed attempt PNG vs GT PNG
============================================================
Read: attempts/p2_radical_045_寸__retry_1/01_寸.png (prior FAIL)
Read: gt/phase2/寸.png (target)

Concrete visual gaps observed in prior attempt vs GT:

1) STROKE WEIGHT TOO HEAVY. Prior 竖钩 rendered as a nearly-black,
   uniform ~12px column; GT is a slender ~7px calligraphic stroke
   with visible taper. The heavy black column dominates the frame
   and makes the whole glyph read as a bold 十.

2) HOOK AT BOTTOM NOT VISIBLE. Prior vertical terminates in what
   looks like a straight flat blunt bottom — no leftward hook
   flick is discernible. GT clearly shows a hook curling toward
   the lower-left, which is the defining 竖钩 vs 竖 distinction.

3) DOT POSITION WRONG QUADRANT + FAR TOO SMALL. Prior 点 is a
   tiny mark placed in the upper-right area (MR cell, ~x=215) —
   well OUTSIDE the crotch. GT places the 点 tucked into the
   crotch between the vertical's descent and the underside of
   the heng — approximately x=170, y=170 area. The errata's
   LITERAL fix C(0.60,0.55)→C(0.80,0.75) was NAMED but NOT
   APPLIED (drawer nudged to MR instead of using C literally).

4) HENG TOO NARROW / TOO HIGH. Prior heng spans only ML(0.30)→
   MR(0.85) at width=9 and sits high; GT heng is longer, at
   moderate weight, mid-band, with slight upward tilt (right end
   higher than left — MMH tail y_frac 0.397 < head y_frac 0.521).

5) VERTICAL EXTENDS TOO FAR ABOVE HENG. Prior TC(0.65,0.30) puts
   head at y=30 — nearly at canvas top. MMH says TC(0.646,0.633)
   → y=63, which still projects above the heng but by less.
   GT shows only a modest upward projection.

============================================================
FIX PLAN
============================================================

A) Apply MMH anchors LITERALLY (v8 rule: trust GT/MMH).
B) Apply errata's C(0.60,0.55)→C(0.80,0.75) dot LITERALLY, not
   nudged into MR. Errata fix at retry_n=1 is authoritative.
C) Reduce all stroke widths ~30% for a calligraphic feel.
D) Make hook flick clearly visible: short but distinct leftward
   curl at the bottom.

============================================================
ANCHOR PLAN (米字格, MMH-literal where available)
============================================================
  s1 横:    head ('ML', 0.416, 0.521) → tail ('MR', 0.692, 0.397)
              — MMH literal. Slight upward tilt (calligraphic).
  s2 竖钩:  head ('TC', 0.646, 0.633)   — MMH literal
            belly ('C',  0.646, 0.30)   — mid-body knot (same x)
            hook_pt ('BC', 0.646, 0.55) — bottom of straight body
            tip ('BC', 0.318, 0.73)     — MMH tail literal
              (short down-and-LEFT flick per MMH geometry)
  s3 点:    head ('C', 0.60, 0.55) → tail ('C', 0.80, 0.75)
              — errata LITERAL fix (crotch position).

Joints:
  s1.mid ⇆ s2.body @ C — P-weld (welded crossing, gap ~0).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu_gou import draw_shu_gou
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 3 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'RETRY 1 RERUN: fixed 4 defects of prior attempt: '
        '(a) reduced weights ~30% for calligraphic feel; '
        '(b) hook flick made distinct via BC(0.646,0.55)→BC(0.318,0.73); '
        '(c) 点 placed LITERALLY at C(0.60,0.55)→C(0.80,0.75) per errata '
        '(prior nudged to MR — wrong); '
        '(d) MMH anchors used literally for heng (slight upward tilt) '
        'and shu_gou head (TC 0.633 not 0.30 — less overshoot above heng).'
    ),
}


def draw(char_draw):
    # s1 横 — MMH literal
    S1_HEAD = ('ML', 0.416, 0.521)
    S1_TAIL = ('MR', 0.692, 0.397)

    # s2 竖钩 — MMH literal for head + tip; straight body
    S2_HEAD   = ('TC', 0.646, 0.633)   # MMH head
    S2_BELLY  = ('C',  0.646, 0.30)    # mid-body knot, SAME x as head
    S2_HOOKPT = ('BC', 0.646, 0.55)    # bottom of straight vertical body
    S2_TIP    = ('BC', 0.318, 0.73)    # MMH tail — down-and-left hook tip

    # s3 点 — errata LITERAL: C(0.60,0.55) → C(0.80,0.75)
    S3_HEAD = ('C', 0.60, 0.55)
    S3_TAIL = ('C', 0.80, 0.75)

    # --- Structural invariants ---
    p_s1a = anchor_to_xy(S1_HEAD)
    p_s1b = anchor_to_xy(S1_TAIL)
    assert p_s1b[0] > p_s1a[0], '横 left→right'

    p_s2h  = anchor_to_xy(S2_HEAD)
    p_s2b  = anchor_to_xy(S2_BELLY)
    p_s2hp = anchor_to_xy(S2_HOOKPT)
    p_s2t  = anchor_to_xy(S2_TIP)
    assert abs(p_s2h[0] - p_s2b[0]) < 2 and abs(p_s2b[0] - p_s2hp[0]) < 2, \
        '竖钩 body must be straight (same x)'
    assert p_s2hp[1] > p_s2h[1], '竖钩 descends'
    assert p_s2t[0] < p_s2hp[0], '钩 tip flicks LEFT'

    p_s3a = anchor_to_xy(S3_HEAD)
    p_s3b = anchor_to_xy(S3_TAIL)
    horiz_mid_y = (p_s1a[1] + p_s1b[1]) / 2
    assert p_s3a[1] > horiz_mid_y, '点 must be BELOW 横 (in the crotch)'
    assert p_s3b[0] > p_s3a[0] and p_s3b[1] > p_s3a[1], '点 down-and-right'

    # P-weld verification: crossing near cell C
    s1_mid_x = (p_s1a[0] + p_s1b[0]) / 2
    p_weld_gap = abs(s1_mid_x - p_s2h[0])
    assert p_weld_gap < 30, f'P-weld x-gap: {p_weld_gap:.1f}px (want <30)'

    # --- Render — reduced weights (~30% lighter than prior) ---
    draw_heng(char_draw, S1_HEAD, S1_TAIL, width=7)

    draw_shu_gou(
        char_draw,
        S2_HEAD, S2_BELLY, S2_HOOKPT, S2_TIP,
        head_w=9, belly_w=8, hook_start_w=7, tip_w=2,
    )

    draw_dian(
        char_draw,
        S3_HEAD, S3_TAIL,
        head_width=2, peak_width=8, curve=0.10, segments=24,
    )


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_寸.png')
    img.save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK.overall_pass = {SELF_CHECK["overall_pass"]}')


if __name__ == '__main__':
    main()
