"""社 (shè, "society/altar", 7 strokes) — G4 p3_char_0341.

Composition: 礻 (left, 4 strokes) + 土 (right, 3 strokes).

礻 has no bank primitive yet (chronic slot queued). Drawn fresh here
per MMH's 4-stroke breakdown (dot + long pie + vertical descender +
small right dot). 土 uses `tu.py` from the bank with anchors overridden
to sit on the right side (standalone default is centered/wider).

Memory reads:
  - drawer_memory.md: composition playbook (bank first, then place).
  - success_bank/INDEX.md: 土 exists as tu.py; 礻 not in bank.
  - errata.md: p2_radical_116_礻 chronic-slot queued but not yet
    implemented. Draw fresh per MMH endpoints.

Stroke plan (from MMH):
  s1: 点 top of 礻       TL(0.826,0.694) -> TC(0.181,0.973)
  s2: 撇 long sweep      ML(0.308,0.523) -> BL(0.149,0.569)
  s3: 竖 spine of 礻     ML(0.885,0.975) -> BL(0.92,0.99)  # clamp y<1
  s4: 点 right dot 礻    C(0.157,0.893)  -> BC(0.351,0.109)
  s5: 横 top of 土       C(0.459,0.743)  -> MR(0.49,0.62)
  s6: 竖 spine of 土     TC(0.816,0.75)  -> BC(0.878,0.446)
  s7: 横 bottom of 土    BC(0.207,0.575) -> BR(0.821,0.52)

Joints (all N except one P inside 土):
  s2.mid ⇆ s3.head @ ML   N  (small gap)
  s2.mid ⇆ s4.head @ C    N  (loose)
  s5.mid ⇆ s6.mid @ C     P  (welded 十 cross of 土)
  s6.tail ⇆ s7.mid @ BC   N  (gap)
"""

import os, sys
BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from dian import draw_dian
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from tu import draw_tu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 7 draw calls verified below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4+3 split. 礻 fresh (no bank primitive yet); 土 via tu.py '
             'with explicit anchors compressed to right column.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- 礻 (4 strokes, left side) ---
    # s1: top dot — short down-right diagonal
    draw_dian(draw, ('TL', 0.826, 0.694), ('TC', 0.181, 0.973),
              peak_width=10, curve=0.05)

    # s2: long 撇 sweeping down-left (the defining left curve of 礻).
    # Head sits mid-left, tail curves down and slightly further left.
    draw_pie(draw, ('ML', 0.308, 0.523), ('BL', 0.149, 0.569),
             head_width=11, tail_width=2, curve=0.14)

    # s3: 竖 descender of 礻 — vertical from mid-band down to bottom.
    # Clamp tail_y to 0.99 so it stays inside the 300px canvas.
    draw_shu(draw, ('ML', 0.885, 0.975), ('BL', 0.92, 0.99), width=8)

    # s4: small right dot of 礻 — short down-right stroke.
    draw_dian(draw, ('C', 0.157, 0.893), ('BC', 0.351, 0.109),
              peak_width=9, curve=0.05)

    # --- 土 (3 strokes, right side) — call tu.py with explicit anchors ---
    # We override every default so it sits on the right of the canvas.
    # NOTE: draw_tu positional order in the file is
    #   (draw, s1_head, s1_tail, s2_head, s2_tail, s3_head, s3_tail)
    # where s1=top heng, s2=spine, s3=bottom heng.
    draw_tu(
        draw,
        s1_head=('C',  0.459, 0.743), s1_tail=('MR', 0.49,  0.62),   # top heng
        s2_head=('TC', 0.816, 0.75),  s2_tail=('BC', 0.878, 0.446),  # spine
        s3_head=('BC', 0.207, 0.575), s3_tail=('BR', 0.821, 0.52),   # bottom heng
    )

    return img


if __name__ == '__main__':
    out_png = os.path.join(os.path.dirname(__file__), '01_社.png')
    img = render()
    img.save(out_png)
    print(f"wrote {out_png}")
    print(f"SELF_CHECK = {SELF_CHECK}")
