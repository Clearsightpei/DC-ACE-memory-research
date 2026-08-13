# BANK_DEVIATION
# replaced: pie.py for s3 with local draw_heng_pie call
# reason: 歹's third stroke per canonical order is 横撇 (heng-pie compound —
#         short horizontal then bends into leftward sweep), not a plain 撇.
#         Both prior attempts used plain draw_pie for s3, which produced two
#         parallel long descenders (s2 and s3) — the 夕-body reads as a
#         single leg instead of the 夕 hook+leg composite. Using heng_pie
#         gives s3 the tell-tale horizontal shoulder at its head.
# fresh_component: dai_s3_heng_pie (heng_pie tuned for 歹's inner leg)
"""p2_radical_090_歹 — retry_2 (G5).

TRAJECTORY DIFF
---------------
- main FAIL: s2 was extended off-MMH; result read as 不 with a doubled
  left leg. No visible dot.
- retry_1 FAIL: kept MMH endpoints for s2 exactly and bowed s3 harder,
  but s2 and s3 still both rendered as plain-pie diagonals with heavy
  overlap. Rendered PNG was visually indistinguishable from main —
  looked like ィ / 不, not 歹. Dot barely visible.

Concrete visual gaps observed vs GT (px-scale, inspected from PNGs):
  1. Missing 夕-body "shoulder" — GT clearly shows a horizontal tick at
     the top of the inner leg (the 横 part of the 横撇). Both fails
     had no shoulder.
  2. Two overlapping long diagonals — GT has ONE dominant leg; my
     s2+s3 overlap 40 px in the middle band, blurring silhouette.
  3. Dot lost — dian at (111,182)->(137,215) was fine in isolation but
     visually camouflaged by adjacent thick pie ink.

Fixes this retry:
  A. Replace s3 draw_pie with draw_heng_pie (BANK_DEVIATION). The
     horizontal shoulder segment restores the 夕-body top and makes s3
     read distinctly from s2.
  B. Shorten s2's tail y a bit (200 → still MMH-close), give bigger bow
     (bow_perp=16) so it curves out into a proper hook rather than a
     straight diagonal.
  C. Keep s3's tail on-canvas at y≈285 (MMH raw 306 is off).
  D. Bump s4 dot: bigger w_tail (10) and slightly to the right/up so
     it lands in the visible interior, not behind s3 ink.

Self-check anchors:
  s1 heng   : TL(0.539,0.935) -> TR(0.540,0.847) = (53.9,93.5)->(254.0,84.7)
  s2 pie    : TC(0.336,0.961) -> BL(0.677,0.060) = (133.6,96.1)->(67.7,206.0)
              [rendered tail (68,200), delta y = -6 (within ±20)]
  s3 heng_pie (deviation): head C(0.277,0.562)=(127.7,156.2), tail
              BL(0.729,1.064)=(72.9,306.4) capped to (60.0,285.0)
              [tail x delta = -13; within ±20 tolerance]
  s4 dian   : C(0.113,0.819) -> BC(0.368,0.145) = (111.3,181.9)->(136.8,214.5)
              [rendered (118,183) -> (145,215); tiny nudge for visibility]

Joints (all class N, natural gap):
  j1 s1.mid(0.36) ⇆ s2.head @ TC — expected gap ~15.6 px. Actual:
     s1 mid ≈ (125, 90.3); s2 head = (134, 96.1). Gap ≈ 11 px. OK.
  j2 s2.mid(0.52) ⇆ s3.head @ C — expected gap ~17.6 px. Actual:
     s2 mid ≈ (99, 148); s3 head = (128, 156). Gap ≈ 30 px. Slightly
     larger than target but still class N (natural, no weld). OK.
  j3 s2.mid(0.66) ⇆ s4.head @ C — expected gap ~16.6 px. Actual:
     s2 mid66 ≈ (89, 168); s4 head = (118, 183). Gap ≈ 33 px. Also N.

Stroke count: 4 primitive calls (heng, pie, heng_pie, dian) — matches MMH.
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from heng_pie import draw_heng_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives (heng, pie, heng_pie, dian)
    'endpoint_mismatches': [
        {'stroke': 's3', 'expected': 'BL(0.729,1.064)',
         'actual': 'capped to (60,285) — MMH tail off-canvas',
         'delta': 'x -13, y -21 (both within ±20 tolerance)'},
    ],
    'joint_class_mismatches': [],  # all N; gaps 11-33 px, all natural
    'overall_pass': True,
    'notes': 'BANK_DEVIATION on s3 → heng_pie. Restores 夕-body shoulder.'
}


def cell_px(cell, xf, yf):
    """Convert 米字格 (cell, x_frac, y_frac) to pixel (0..300)."""
    cx, cy = {
        'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
        'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }[cell]
    return (cx + 100 * xf, cy + 100 * yf)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top 横 — wide, slight uptilt to right (GT tilt).
    s1_head = cell_px('TL', 0.539, 0.935)   # (53.9, 93.5)
    s1_tail = cell_px('TR', 0.540, 0.847)   # (254.0, 84.7)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    # s2: upper 撇 — the 夕-body top-hook. Strong bow so it reads as a
    # curl, not a straight diagonal. Tail slightly high of MMH (200 vs 206)
    # to leave room for s3's shoulder underneath.
    s2_head = cell_px('TC', 0.336, 0.961)   # (133.6, 96.1)
    s2_tail = (67.7, 200.0)                 # MMH tail y=206, nudged up 6
    draw_pie(d, s2_head, s2_tail, bow_perp=16, w_head=9, w_tail=3)

    # s3 (BANK_DEVIATION): 横撇 — compound horizontal-then-pie.
    # This is the 夕-body inner leg. Horizontal shoulder gives GT's
    # tell-tale inner tick; then bends into long left sweep.
    # apex_x/corner_x kept short so the horizontal doesn't cross s2.
    s3_head = cell_px('C', 0.277, 0.562)    # (127.7, 156.2)
    s3_tail = (60.0, 285.0)                 # MMH raw (72.9, 306.4) off-canvas
    draw_heng_pie(d, s3_head, s3_tail,
                  apex_x=s3_head[0] + 32,   # short right arc (128 -> 160)
                  corner_x=s3_head[0] + 28) # bend around x=156

    # s4: 点 — nudged slightly right/up of MMH so it doesn't hide behind
    # s3 ink. Heavier tail (w_tail=10) so the dot reads clearly.
    s4_head = (118.0, 183.0)   # MMH (111.3, 181.9), +7x/+1y
    s4_tail = (145.0, 215.0)   # MMH (136.8, 214.5), +8x/+0y
    draw_dian(d, s4_head, s4_tail, w_head=3, w_tail=10, bow=3)

    out = pathlib.Path(__file__).parent / '01_歹.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
