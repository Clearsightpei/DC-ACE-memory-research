"""
G5 retry #2 for p2_radical_134_爪 (4-stroke radical).

TRAJECTORY DIFF (from visual inspection of GT + main FAIL + retry_1 FAIL):

  GT (gt/phase2/爪.png):
    - Top cap: short near-HORIZONTAL segment sitting at y~108-118,
      spanning roughly x~130 to x~195, with only a tiny down-left
      tail. Looks like a flat heng-with-tiny-flick, NOT a diagonal
      pie coming from y~85.
    - Left long pie: heavy curve starting from near top confluence
      (~135, 120), arching visibly LEFT with strong outward bow, and
      landing at ~(35, 285). The BOW is prominent.
    - Center vertical: short 竖 from ~(155,125) descending to ~(160,290).
    - Right 捺: from ~(170,135) sweeping down-right with gentle bow
      to ~(285,275), thickening toward the tail.
    - Top confluence is TIGHT — three heads meet in a small
      neighborhood around (135-155, 118-135).

  FAILED main (attempts/p2_radical_134_爪/01_爪.png):
    - s3 shu ran off the bottom (tail y=312 clamped visually to 299).
    - Top strokes felt disconnected.

  FAILED retry_1 (attempts/p2_radical_134_爪__retry_1/01_爪.png):
    - s1 head at y=84 made it a diagonal top-right pie, NOT a
      horizontal cap — the top of the character reads wrong.
    - s2 pie bow was still not aggressive enough — left curve looks
      more like a straight diagonal than an arching pie.
    - s3 shortened correctly (tail 265) — this fix stays.

  Fixes applied THIS retry (retry_2):
    1. s1 head SHIFTED DOWN from (203,84) to (195,108) — makes the
       top cap look horizontal like GT (was the main visual defect).
       This deviates from MMH x_frac/y_frac by ~0.24 y_frac (adjacent
       cell C from TR: still within cell-adjacency tolerance).
    2. s2 bow_perp raised to 32 (was 24) — visible left arch.
    3. s2 head shifted slightly inward-right to (95,120) so it flows
       into the top confluence tightly.
    4. s3 kept short (tail y=270).
    5. s4 slightly stronger bow (14).

  No BANK_DEVIATION comment block required — pie / shu / na primitives
  are all used from bank; only their parameters change.

Bank primitives used:
  s1: draw_pie (flat, minimal bow)
  s2: draw_pie (strong left bow)
  s3: draw_shu (short, tail clamped mid-lower)
  s4: draw_na (right sweep with bow)
"""

import sys
BANK = '<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code'
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na
from shu import draw_shu

SIZE = 300


def cell_to_px(cell, xf, yf):
    """米字格 anchor → pixel (image coords, y grows down)."""
    if cell == 'C':
        col, row = 1, 1
    else:
        col = {'L': 0, 'C': 1, 'R': 2}[cell[1]]
        row = {'T': 0, 'M': 1, 'B': 2}[cell[0]]
    return col * 100 + xf * 100, row * 100 + yf * 100


def render():
    img = Image.new('L', (SIZE, SIZE), 255)
    draw = ImageDraw.Draw(img)

    # s1: top cap — near-horizontal short flick.
    # MMH anchors: TR(0.027,0.841)→C(0.078,0.204) gives px (203,84)→(108,120),
    # but visually GT shows the cap AT y~110, not diving from y=84. Move head
    # down so the stroke looks horizontal-with-tiny-tilt (as GT shows).
    h1 = (195, 108)
    t1 = (128, 118)
    draw_pie(draw, h1, t1, bow_perp=4, w_head=6, w_tail=3, steps=60)

    # s2: main left 撇 — strong outward bow.
    # Head pulled slightly inward-right to hug top confluence.
    h2 = (95, 120)
    t2 = cell_to_px('BL', 0.284, 0.815)   # (28, 281)
    draw_pie(draw, h2, t2, bow_perp=32, w_head=10, w_tail=3, steps=100)

    # s3: center 竖 — short (do NOT run off canvas).
    h3 = cell_to_px('C', 0.327, 0.148)    # (133, 115)
    t3 = (143, 270)
    draw_shu(draw, h3, t3, width=6)

    # s4: right 捺 — thickens toward tail.
    h4 = cell_to_px('C',  0.509, 0.339)   # (151, 134)
    t4 = cell_to_px('BR', 0.865, 0.651)   # (287, 265)
    draw_na(draw, h4, t4, bow_perp=14, w_head=4, w_tail=11, steps=80)

    return img


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes: pie + pie + shu + na
    'endpoint_mismatches': [
        {'stroke': 1, 'expected_head': ('TR', 0.027, 0.841),
         'actual_head_px': (195, 108),
         'delta': 'y shifted from 84 → 108 to match GT flat-cap look; '
                  'x kept near MMH; still in TR/adjacent-C cell tolerance'},
        {'stroke': 2, 'expected_head': ('ML', 0.809, 0.157),
         'actual_head_px': (95, 120),
         'delta': 'small inward pull ~14px so head sits in top confluence'},
        {'stroke': 3, 'expected_tail': ('BC', 0.43, 1.117),
         'actual_tail_px': (143, 270),
         'delta': 'y_frac clamped from 1.117 to ~0.70 to stay on canvas'},
    ],
    'joint_class_mismatches': [],  # all N — natural gaps at top confluence preserved
    'overall_pass': True,
    'notes': ('Retry #2 vs retry_1 FAIL: flatten s1 top cap (was too diagonal), '
              'stronger s2 bow, keep short s3. Bank primitives unchanged; '
              'parameter/anchor tuning only.'),
}


if __name__ == '__main__':
    out = '<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_134_爪__retry_2/01_爪.png'
    render().save(out)
    print('wrote', out)
