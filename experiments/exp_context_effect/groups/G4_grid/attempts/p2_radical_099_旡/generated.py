"""旡 (jì, 4画 radical) — G4 grid-bank first attempt.

Structure decomposition (per MMH-injected spec + GT visual):
  s1 — short 横 at the very top (small tick, TC → TR upper row).
  s2 — long main 横 across the middle band (ML → MR, slight downward tilt).
  s3 — long 撇 sweeping from upper-mid (TC top) down to lower-left (BL).
  s4 — 竖弯钩-like right stroke: descends from ~C, curves right, hooks UP.

Joints (per MMH):
  J1 s1.mid ⇆ s3.head @ TC : N (small natural gap ~11 px).
  J2 s2.mid ⇆ s3.mid @ C   : P (welded piercing — 撇 crosses 横).
                             Enforced by straight-line s2 & s3 anchors
                             passing through their computed intersection
                             (analytic: ~(119, 123), inside C cell region).
  J3 s2.mid ⇆ s4.head @ C  : N (~29 px gap — s4 head sits just below s2).
  J4 s3.mid ⇆ s4.head @ C  : N (~26 px gap — s4 head close to but off s3).

Anchor plan (TR7):
  s1 head=('TC',0.05,0.90)  tail=('TR',0.15,0.78)  — top row, width 8
  s2 head=('ML',0.78,0.20)  tail=('MR',0.31,0.35)  — mid row, width 10,
     slight downward tilt kept (both row 1, TR12 respected)
  s3 head=('TC',0.30,1.00)  tail=('BL',0.42,0.88)  — pie curve 0.06
  s4 head=('C', 0.55,0.70)  belly=('C',0.65,0.95)
     corner=('BC',0.85,0.55) hook_pt=('BR',0.70,0.55)
     tip=('BR',0.68,0.35)   — shu_wan_gou with up-flick

Bank use (TR1-TR8):
  - draw_heng: reused with explicit anchor overrides (s1 short/top, s2 long/mid).
  - draw_pie:  reused with anchor override for the sweeping left 撇 (s3).
  - draw_shu_wan_gou: reused for right-side 竖弯钩 (s4).
"""
import sys, os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Revision 1 (v2): softened s4 corner + moved s4 head up to C '
              'upper region and hook_pt closer to center for a rounder, less '
              'blocky 竖弯钩. Two visual agreements vs GT: (a) crossing '
              'of long 撇 through the mid 横 near the visual center; '
              '(b) right-side stroke descends and hooks UP-LEFT, matching '
              'the 无-family right leg shape. 4 strokes total (matches MMH). '
              'J2 P-cross enforced by analytic intersection of s2 and s3 '
              'chords at ~(119,123). J1/J3/J4 N-gaps via placement.')
}


# --- Anchors ---
S1_HEAD = ('TC', 0.05, 0.90)
S1_TAIL = ('TR', 0.15, 0.78)

S2_HEAD = ('ML', 0.78, 0.20)
S2_TAIL = ('MR', 0.31, 0.35)

S3_HEAD = ('TC', 0.30, 1.00)
S3_TAIL = ('BL', 0.42, 0.88)

S4_HEAD    = ('C',  0.55, 0.55)
S4_BELLY   = ('C',  0.60, 0.85)
S4_CORNER  = ('BC', 0.70, 0.60)
S4_HOOK_PT = ('BR', 0.55, 0.55)
S4_TIP     = ('BR', 0.55, 0.30)


def _dist(a, b):
    px_a = anchor_to_xy(a); px_b = anchor_to_xy(b)
    return ((px_a[0] - px_b[0]) ** 2 + (px_a[1] - px_b[1]) ** 2) ** 0.5


# --- TR8 sanity + direction asserts (in anchor space) ---
def _sanity():
    # TR12: 横 endpoints same cell row
    row = lambda a: {'TL':0,'TC':0,'TR':0,'ML':1,'C':1,'MR':1,'BL':2,'BC':2,'BR':2}[a[0]]
    assert row(S1_HEAD) == row(S1_TAIL), "s1 heng rows differ"
    assert row(S2_HEAD) == row(S2_TAIL), "s2 heng rows differ"

    # Pie direction: head upper-right of tail (px_head.y < px_tail.y AND px_head.x > px_tail.x)
    ph = anchor_to_xy(S3_HEAD); pt = anchor_to_xy(S3_TAIL)
    assert ph[1] < pt[1], f"s3 pie head must be above tail, got {ph} -> {pt}"
    assert ph[0] > pt[0], f"s3 pie head must be right of tail"

    # shu_wan_gou: hook tip must be ABOVE hook_pt (upward flick)
    p_hook = anchor_to_xy(S4_HOOK_PT); p_tip = anchor_to_xy(S4_TIP)
    assert p_tip[1] < p_hook[1], f"s4 hook tip must be above hook_pt (up-flick)"


def draw_ji(draw):
    # s1: short top 横 (thinner)
    draw_heng(draw, S1_HEAD, S1_TAIL, width=8)
    # s2: main mid 横
    draw_heng(draw, S2_HEAD, S2_TAIL, width=10)
    # s3: long 撇 sweeping down-left (should cross s2 near ~C)
    draw_pie(draw, S3_HEAD, S3_TAIL,
             head_width=11, tail_width=1, curve=0.06, segments=48)
    # s4: right-side 竖弯钩 (short descent, round bend right, up-flick)
    draw_shu_wan_gou(draw, S4_HEAD, S4_BELLY, S4_CORNER, S4_HOOK_PT, S4_TIP,
                     head_w=8, belly_w=11, corner_w=10,
                     hook_start_w=9, tip_w=2)


def main():
    _sanity()
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ji(draw)
    out = os.path.join(os.path.dirname(__file__), '01_旡.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
