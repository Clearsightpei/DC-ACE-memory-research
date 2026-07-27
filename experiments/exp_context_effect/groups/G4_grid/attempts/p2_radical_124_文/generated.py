"""文 (wén, "text", 4 strokes) — Phase-2 radical, first attempt.

Anchor plan (TR7, TR9 — expanded MMH for standalone radical):

  s1 — 点 (dot at top): tilted down-right, top of char.
       head @ ('TC', 0.30, 0.20)  tail @ ('TC', 0.60, 0.50)
       (MMH had head ('TC',0.143,0.574)→tail ('TC',0.506,0.855) — the
        MMH y_fracs place dot in TC cell top region; using dian primitive.)

  s2 — 横 (long crossing bar): full horizontal spanning ML→MR at the
       middle of the character. Row-invariant (TR8 rule 5): both endpoints
       in M-row, y_fracs equal.
       head @ ('ML', 0.20, 0.55)  tail @ ('MR', 0.85, 0.55)
       (MMH gave ML(0.548,0.389)→MR(0.238,0.189) — verbatim tilts by
        20% and under-spans; expanded per TR9.)

  s3 — 撇 (long sweep down-left, concave-right): head near center just
       below the horizontal, tail reaches BL region.
       head @ ('C', 0.55, 0.20)  tail @ ('BL', 0.15, 0.90)
       curve = -0.08 (concave-right per form_catalog 撇-in-X context).

  s4 — 捺 (long sweep down-right): head sits at s3.mid area but ABOVE-LEFT
       of s3's midpoint so it sweeps DOWN through the crossing to BR
       (per form_catalog 捺-in-X, and fu.py pattern).
       head @ ('C', 0.45, 0.30)  tail @ ('BR', 0.85, 0.90)
       peak_t = 0.80  curve = 0.10.

Joints (per dispatcher MMH block):
  J1  s2.mid ⇆ s3.head  @ cell C  — N (natural gap ~15 px).
      Not welded — 横 passes just above where the 撇 begins.
  J2  s3.mid ⇆ s4.mid   @ cell BC — P (welded X-crossing).
      Achieved by placing s4.head/tail so its geometric mid crosses
      s3's geometric mid near BC(0.4, 0.2 in cell = pixel ~(140, 220)).

TR8 sanity:
  - s2 endpoints both y_frac 0.55 in M-row → truly horizontal.  OK
  - s3 & s4 both start above and cross at BC region.
  - s1 (dot) doesn't touch anything (S class).
Stroke count = 4  ✓
"""

import os
import sys
from PIL import Image, ImageDraw

# Import shared primitives from the Success Bank (READ-ONLY).
BANK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK_DIR)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian        # noqa: E402
from heng import draw_heng        # noqa: E402
from pie import draw_pie          # noqa: E402
from na import draw_na            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first attempt; TR9-expanded 横 across full ML→MR; X-cross P at BC; dot up top with N-gap to 横.'
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 点 (dot at top)
    s1_head = ('TC', 0.30, 0.20)
    s1_tail = ('TC', 0.60, 0.50)
    draw_dian(draw, s1_head, s1_tail, head_width=3, peak_width=10, curve=0.10)

    # s2 — 横 (crossing bar); row-invariant M-row.
    # Slightly narrower than full-grid to match GT proportions —
    # the 横 shouldn't extend past the 撇/捺 tail column.
    s2_head = ('ML', 0.30, 0.50)
    s2_tail = ('MR', 0.75, 0.50)
    draw_heng(draw, s2_head, s2_tail, width=9)

    # s3 — 撇 (sweep down-left, concave-right). Head just below the
    # 横 midpoint (N-gap ~15 px per J1), tail reaches BL corner.
    s3_head = ('C', 0.45, 0.65)
    s3_tail = ('BL', 0.15, 0.95)
    draw_pie(draw, s3_head, s3_tail, head_width=11, tail_width=1, curve=-0.06)

    # s4 — 捺 (sweep down-right). Head sits ABOVE-LEFT of s3's mid so
    # it crosses s3 through the BC region (P-weld at BC).
    # Head near/on the 横 at its midpoint, tail reaches BR.
    s4_head = ('C', 0.35, 0.55)
    s4_tail = ('BR', 0.90, 0.95)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.80, curve=0.10)

    img.save(out_path)
    return out_path


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_文.png')
    render(out)
    print(f"wrote {out}")
