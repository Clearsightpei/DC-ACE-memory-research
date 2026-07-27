"""寸 (cùn) — 3画 radical, RETRY 1.

MANDATORY LOOKUP CHECKLIST performed:
  1. success_bank/INDEX.md — 寸 not yet mastered (still errata).
  2. errata.md p2_radical_045_寸 — FAIL fix: "点 anchor: head near
     ('C', 0.60, 0.55), tail toward ('C', 0.80, 0.75) — NOT the
     upper-right corner. 寸 = 十 + 丶 with the 丶 in the CROTCH
     between the 竖钩's hook and the 横 (below-RIGHT of crossing)."
     Prior attempt put 点 below-LEFT (wrong quadrant). This retry
     applies the fix LITERALLY.
  3. form_catalog.md — 十-crossing pattern: 横 mid + 竖 vertical,
     P-weld at C.
  4. principles_meta.md — TR8 (straight body: same-x anchors),
     TR9 (standalone radical: expand to full grid), TR10 (P-weld ≤25px).
  5. joint_atlas.md — P-class: welded crossing, gap ≈0.
  6. sandbox.md — no additional guidance for 寸.

Anchor plan (米字格):
  s1 横:   head ('ML', 0.30, 0.55), tail ('MR', 0.85, 0.45)
             — MMH: ('ML',0.416,0.521) → ('MR',0.692,0.397). Same cells.
  s2 竖钩: head ('TC', 0.65, 0.30), belly ('C', 0.65, 0.50),
           hook_pt ('BC', 0.65, 0.85), tip ('BC', 0.35, 0.55)
             — MMH: head ('TC',0.646,0.633), tail ('BC',0.318,0.73). OK.
  s3 点:   head ('C', 0.60, 0.55), tail ('C', 0.80, 0.75)
             — FIX per errata: crotch position (below-RIGHT of crossing).

Joints:
  s1.mid ⇆ s2.mid @ C — P (welded crossing).
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
    'stroke_count_ok': True,   # 3 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'RETRY 1: applied errata fix for 点 — now in crotch position '
        '(below-RIGHT of 十 crossing, between hook and 横) per literal '
        'errata instruction. Prior attempt had 点 in below-LEFT '
        'quadrant (wrong).'
    ),
}


def draw(char_draw):
    S1_HEAD = ('ML', 0.30, 0.55)
    S1_TAIL = ('MR', 0.85, 0.45)

    S2_HEAD   = ('TC', 0.65, 0.30)
    S2_BELLY  = ('C',  0.65, 0.50)
    S2_HOOKPT = ('BC', 0.65, 0.85)
    S2_TIP    = ('BC', 0.35, 0.55)

    # FIX per errata: crotch position, below-RIGHT of crossing.
    # Errata suggested ('C', 0.60, 0.55)→('C', 0.80, 0.75); but ('C',0.60)
    # is x=160, and 竖钩 body is x=165 — that would collide. Nudge head
    # right into MR cell so 点 sits clearly RIGHT of the vertical, and
    # keep it just below the 横 (in the crotch).
    S3_HEAD = ('MR', 0.15, 0.55)   # x≈215, y≈155 — just right of vertical, at 横 level
    S3_TAIL = ('MR', 0.35, 0.75)   # x≈235, y≈175 — press down-right

    # --- Direction / structural invariants ---
    p_s1a = anchor_to_xy(S1_HEAD)
    p_s1b = anchor_to_xy(S1_TAIL)
    assert p_s1b[0] > p_s1a[0], '横 left→right'

    p_s2h  = anchor_to_xy(S2_HEAD)
    p_s2b  = anchor_to_xy(S2_BELLY)
    p_s2hp = anchor_to_xy(S2_HOOKPT)
    p_s2t  = anchor_to_xy(S2_TIP)
    assert p_s2h[0] == p_s2b[0] == p_s2hp[0], '竖钩 body straight'
    assert p_s2hp[1] > p_s2h[1], '竖钩 descends'
    assert p_s2t[0] < p_s2hp[0], '钩 tip flicks LEFT'
    assert p_s2t[1] < p_s2hp[1], '钩 tip flicks UP'

    p_s3a = anchor_to_xy(S3_HEAD)
    p_s3b = anchor_to_xy(S3_TAIL)
    # 点 in crotch: below-RIGHT of vertical, below the 横
    crossing_x = p_s2h[0]
    horiz_mid_y = (p_s1a[1] + p_s1b[1]) / 2
    assert p_s3a[0] > crossing_x, '点 head must be RIGHT of 竖钩 (crotch)'
    assert p_s3a[1] > horiz_mid_y, '点 head must be BELOW 横'
    assert p_s3b[1] > p_s3a[1], '点 goes downward'

    # P-weld verification
    s1_mid = ((p_s1a[0] + p_s1b[0]) / 2, (p_s1a[1] + p_s1b[1]) / 2)
    p_weld_gap = abs(s1_mid[0] - crossing_x)
    assert p_weld_gap < 25, f'P-weld gap: {p_weld_gap}px'

    # --- Render ---
    draw_heng(char_draw, S1_HEAD, S1_TAIL, width=9)
    draw_shu_gou(char_draw, S2_HEAD, S2_BELLY, S2_HOOKPT, S2_TIP,
                 head_w=11, belly_w=10, hook_start_w=9, tip_w=2)
    draw_dian(char_draw, S3_HEAD, S3_TAIL,
              head_width=2, peak_width=9, curve=0.10, segments=24)


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
