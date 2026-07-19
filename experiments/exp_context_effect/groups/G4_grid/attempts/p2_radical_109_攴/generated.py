"""攴 (pū) — 4画 radical. Top = 卜 (vertical + short tick), bottom = 又 (pie + na crossing).

Anchor plan (from MMH structural brief, adjusted to fill 米字格 per TR9 since standalone):
  s1 (卜 vertical, mostly-shu):
      head @ ('TC', 0.35, 0.20)   → (135, 20)   (extend up per TR9 for standalone)
      tail @ ('C',  0.40, 0.60)   → (140, 160)
      row/col check: head col=1 tail col=1  → straight-ish (col match)  ✓ TR12
      inlined as a slightly tapered stroke (top thinner, bottom press) via draw_shu
  s2 (short tick 横 attached to s1 mid-body — the little bar at top-right of 卜):
      head @ ('C',  0.55, 0.15)   → (155, 115)   (starts on/near s1 body around mid)
      tail @ ('MR', 0.20, 0.05)   → (220, 105)
      Joint: N with s1.mid — small gap ≤25 px (TR10). Head sits ~15 px right of s1 body.
  s3 (撇 of 又):
      head @ ('C',  0.05, 0.72)   → (105, 172)   (near s1.tail, N-class small gap)
      tail @ ('BL', 0.30, 0.90)   → (30, 290)
      Joint: N with s1.tail — head is ~14 px below s1.tail (which is at (140,160)).
      Distance: sqrt((105-140)^2+(172-160)^2) ≈ 37 px — too far. Tighten head.
      Adjusted head @ ('C', 0.20, 0.70)   → (120, 170)  → dist ≈ sqrt(400+100)=22 px ✓
  s4 (捺 of 又, crosses s3):
      P-weld with s3 mid. To weld cleanly we compute the actual midpoint of s3 body
      and use it as s4's belly-through point. Simpler: set s4 head at ('ML', 0.90, 0.85),
      tail at ('BR', 0.85, 0.95). Verify visually the crossing lands mid-又.

Joints:
  s1.mid ⇆ s2.head  : N  (gap ~15-20 px)
  s1.tail ⇆ s3.head : N  (gap ~15-22 px)
  s3.mid ⇆ s4.mid   : P  (welded crossing — the X of 又)
"""

SELF_CHECK = {
    'visual_ok': False,
    'stroke_count_ok': True,   # 4 primitives called (shu, heng, pie, na)
    'endpoint_mismatches': [
        # Some deviation from MMH anchors in service of standalone-radical
        # coverage per TR9 and to place the 又 crossing at BC.
        {'stroke': 1, 'expected_head': ('TC', 0.339, 0.636), 'actual': ('TC', 0.35, 0.20),
         'delta': 'head extended upward per TR9 for standalone'},
        {'stroke': 3, 'expected_head': ('C', 0.017, 0.717), 'actual': ('C', 0.55, 0.60),
         'delta': 'shifted head right to keep pie under 卜; MMH was too far left'},
        {'stroke': 4, 'expected_head': ('ML', 0.973, 0.893), 'actual': ('C', 0.30, 0.80),
         'delta': 'moved right so 捺 head lands near s3 body upper-mid'},
    ],
    'joint_class_mismatches': [
        # Intended P at s3.mid ⇆ s4.mid, but current render shows the two strokes
        # meeting near their heads rather than crossing in the middle — appears as
        # inverted-V (Λ) instead of X. Class P declared, but visually reads more like T.
        {'joint': 's3.mid⇆s4.mid', 'expected_class': 'P', 'actual_class': 'T (near-head touch)'},
    ],
    'overall_pass': False,
    'notes': ('Revision used. 又 X-crossing did not materialize — s3 and s4 meet near '
              'their heads rather than crossing mid-body. Two agreements with GT (TR11): '
              '(a) 卜 vertical + right-tick in upper region present; (b) two diagonal '
              'strokes fanning down to lower corners. Submitting per one-revision cap.'),
}

import os, sys
from PIL import Image, ImageDraw

# Import from success_bank/code so we can reuse promoted primitives.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


def draw_pu(draw):
    # ---- s1: vertical of 卜 (extended per TR9 for standalone). ----
    s1_head = ('TC', 0.35, 0.20)   # (135, 20)
    s1_tail = ('C',  0.40, 0.60)   # (140, 160)
    draw_shu(draw, s1_head, s1_tail, width=8)

    # ---- s2: short tick 横 at top-right of 卜 (starts near s1 mid-body).
    # In GT this tick sits at roughly mid-height of s1 (y~90-100), slanted slightly up-right.
    s2_head = ('C',  0.55, 0.05)   # (155, 105)  — near s1 body at upper-mid
    s2_tail = ('MR', 0.20, 0.00)   # (220, 100)
    draw_heng(draw, s2_head, s2_tail, width=6)

    # ---- 又 component: cross of 撇 and 捺. ----
    # Design the crossing point first, then place both strokes to pass through it.
    # Crossing point per MMH joint spec: BC(0.525, 0.367) → (152.5, 236.7).
    # We'll make the 又 sit in the lower-middle of the canvas, centered under 卜.

    # s3 (撇): starts up-right of the crossing (near s1.tail area), ends bottom-left.
    # Head should be ~15-20 px from s1.tail (140, 160) — an N-class gap.
    s3_head = ('C',  0.55, 0.60)   # (155, 160)  — right next to s1.tail
    s3_tail = ('BL', 0.10, 0.95)   # (10, 295)
    draw_pie(draw, s3_head, s3_tail, head_width=11, tail_width=1, curve=0.14)

    # s4 (捺): head up-left, crosses s3 near s3-mid, tail bottom-right.
    # s3-mid pixel ≈ ((155+10)/2, (160+295)/2) = (82.5, 227.5).
    # For a clean X-crossing, s4 head goes upper-left of s3 (above its body somewhere),
    # then swings down-right through the mid and out to BR. Head sits on/near s3 body upper-middle.
    s4_head = ('C',  0.30, 0.80)   # (130, 240) — near the mid of s3, above the crossing region
    s4_tail = ('BR', 0.85, 0.95)   # (285, 295)
    draw_na(draw, s4_head, s4_tail, head_width=3, peak_width=13, tail_width=1,
            peak_t=0.85, curve=0.10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_pu(draw)
    out = os.path.join(_HERE, '01_攴.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
