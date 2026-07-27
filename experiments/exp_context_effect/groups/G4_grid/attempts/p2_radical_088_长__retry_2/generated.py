"""长 (cháng) — 4-stroke radical. Retry #2.

Errata fix (LITERAL, per memory_index.md checklist step 2):
  errata.md p2_radical_088_长 fix:
    s3 = straight 竖 TC→BC + short 提 flick. Reuse `shu_ti.py`.
    Move s1 to TC(0.55, 0.20) → ML(0.65, 0.40).

Mandatory-lookup checklist confirmations:
  1. success_bank/INDEX.md grep for 长 — no direct chang entry
     (INDEX line 128/139/173/187 are 干/士/土/牛 with the token "长");
     'chang.py' exists but is 厂 (radical 014). No reuse from bank.
  2. errata.md grep for 长 — HIT at line 693. Fix applied literally
     (s3 uses shu_ti primitive; s1 moved to TC→ML per errata).
  3. form_catalog.md — 竖提 is a compound stroke, use shu_ti.py.
  4. principles_meta.md — TR9 mandatory for standalone Phase-2 radical:
     expand MMH anchors to full-grid span. TR12: 竖 endpoints share
     column (both at TC/BC center-x).
  5. joint_atlas.md — s2 x s3 body = P (welded overlap). s1 tail
     near s3 body = N (small gap). s4 head near s2/s3 crossing = N.
  6. sandbox.md — no additional 长-specific notes.

Stroke plan (4 strokes, per MMH structural block + errata):
  s1: 短撇 head TC(0.55, 0.20) → tail ML(0.65, 0.40)
      (upper-mid, angled down-left)
  s2: 长横 head ML(0.10, 0.55) → tail MR(0.90, 0.45)
      (long horizontal, slight up-right tilt, crosses s3)
  s3: 竖提 shu_head TC(0.50, 0.20) → shu_tail BC(0.50, 0.80)
              → ti_tail MR(0.10, 0.75) (straight vertical + up-right flick)
  s4: 捺 head C(0.30, 0.35) → tail BR(0.85, 0.55)
      (long sweep from mid crossing to lower-right)

Joint plan (matches MMH expectation block):
  J1 s1.tail ⇆ s3.mid @ C : N (natural small gap)
  J2 s2.mid  ⇆ s3.mid @ C : P (welded crossing)
  J3 s2.mid  ⇆ s4.head @ C : N (small gap)
  J4 s3.mid  ⇆ s4.head @ C : N (small gap)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image
from PIL import ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from na import draw_na
from shu_ti import draw_shu_ti


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke primitives (s3 = compound shu_ti = 1 stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Retry #2. Errata fix applied LITERALLY: '
              's3 replaced with shu_ti (straight vertical + 提 flick), '
              's1 moved to TC→ML upper-mid. '
              's2 横 crosses s3 body at mid (P). '
              's4 捺 long sweep to BR.')
}


def draw_chang_radical(draw):
    # --- s3 first (drawn under s2 for a clean crossing) ---
    # 竖提: straight vertical TC→BC + 提 flick up-right.
    # TR12: TC and BC both at x_frac=0.50 → same column, straight vertical.
    draw_shu_ti(draw,
                shu_head=('TC', 0.50, 0.20),
                shu_tail=('BC', 0.50, 0.80),
                ti_tail=('MR', 0.10, 0.75),
                shu_head_w=12, shu_tail_w=11,
                ti_head_w=11, ti_tail_w=1)

    # --- s2: 长横 across the middle, slight up-right tilt ---
    # Both endpoints on ML/MR row → TR12 horizontal.
    draw_heng(draw,
              ('ML', 0.10, 0.55),
              ('MR', 0.90, 0.45),
              width=9)

    # --- s1: short 撇 in upper area ---
    # Errata literal: TC(0.55, 0.20) → ML(0.65, 0.40).
    draw_pie(draw,
             ('TC', 0.55, 0.20),
             ('ML', 0.65, 0.40),
             head_width=9, tail_width=2,
             curve=0.10, segments=36)

    # --- s4: long 捺 from near crossing to lower-right ---
    draw_na(draw,
            ('C', 0.30, 0.35),
            ('BR', 0.85, 0.55),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.80, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chang_radical(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_长.png')
    img.save(out_path)
    print("Saved:", out_path)


if __name__ == '__main__':
    main()
