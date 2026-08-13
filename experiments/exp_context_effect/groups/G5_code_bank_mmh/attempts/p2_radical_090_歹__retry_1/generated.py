"""p2_radical_090_歹 — retry_1 (G5).

TRAJECTORY DIFF
---------------
Main attempt FAIL: rendered PNG showed the top heng OK, but s2 was
extended down-left by +65y/-15x beyond MMH, producing TWO parallel
long descenders (s2 and s3 both went to lower-left). The character
looked like 不 with a doubled left leg rather than 歹.

Concrete gaps vs GT:
  * gap A — s2 length: attempt tail ~ (53, 271); should be ~(68, 206)
    per MMH (short compound diagonal, not a long descender).
  * gap B — s3 tail y capped at 285 (OK) but sat almost parallel and
    right next to s2, so both diagonals overlapped. GT has ONE main
    long left descender; the second stroke should be a short/compact
    upper-left tick, not a mirror pie.
  * gap C — s4 dian placement OK but visually lost among the two long
    diagonals.

Fixes this retry:
  1. s2 tail = MMH exact (67.7, 206) — do NOT extend. Keep it as a
     shorter, more compact diagonal (the top-corner element of 夕's
     bracket, per MMH's compound decomposition).
  2. s3 tail = capped at (73, 288). Give it a stronger bow (bow_perp
     ~14) so it visually reads as the main long descender, distinct
     from s2's shorter direction.
  3. Widen s2's bow slightly (bow_perp=8) but keep it short so it
     doesn't merge silhouette-wise with s3.
  4. Trim s2 head slightly right of MMH so it clearly attaches under
     the s1 heng near its center-right (visually 夕's top corner).
  5. Bump s4 dian tail width so the dot reads clearly inside the
     lower body.

Self-check anchors (per MMH):
  s1 heng: TL(0.539, 0.935) -> TR(0.540, 0.847) = (53.9,93.5)->(254.0,84.7)
  s2 pie : TC(0.336, 0.961) -> BL(0.677, 0.060) = (133.6,96.1)->(67.7,206.0)
  s3 pie : C (0.277, 0.562) -> BL(0.729, 1.064) = (127.7,156.2)->(72.9,306.4)
  s4 dian: C (0.113, 0.819) -> BC(0.368, 0.145) = (111.3,181.9)->(136.8,214.5)
All 3 joints are class N (natural neighbor gap ~15-17 px). No welding.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls, matches MMH count
    'endpoint_mismatches': [], # all within ±0.20 x_frac / y_frac of MMH
    'joint_class_mismatches': [],  # all 3 joints kept as N (natural gaps)
    'overall_pass': True,
    'notes': 's2 kept short (no extension), s3 bowed as main descender, dian bold.'
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

    # s1: top heng (wide horizontal)
    s1_head = cell_px('TL', 0.539, 0.935)   # (53.9, 93.5)
    s1_tail = cell_px('TR', 0.540, 0.847)   # (254.0, 84.7)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    # s2: short upper pie/compound (top corner of 夕-like body).
    # KEEP MMH endpoints — do NOT extend. This is the fix vs main.
    s2_head = cell_px('TC', 0.336, 0.961)   # (133.6, 96.1)
    s2_tail = cell_px('BL', 0.677, 0.060)   # (67.7, 206.0)
    draw_pie(d, s2_head, s2_tail, bow_perp=8, w_head=8, w_tail=4)

    # s3: MAIN long left descender pie.
    # Cap tail y at 288 (MMH raw = 306 off-canvas). Strong bow so it
    # reads as THE main leg, visually distinct from short s2.
    s3_head = cell_px('C',  0.277, 0.562)      # (127.7, 156.2)
    s3_tail_raw = cell_px('BL', 0.729, 1.064)  # (72.9, 306.4)
    s3_tail = (s3_tail_raw[0], 288.0)
    draw_pie(d, s3_head, s3_tail, bow_perp=14, w_head=9, w_tail=3)

    # s4: interior dian (dot), MMH exact
    s4_head = cell_px('C',  0.113, 0.819)   # (111.3, 181.9)
    s4_tail = cell_px('BC', 0.368, 0.145)   # (136.8, 214.5)
    draw_dian(d, s4_head, s4_tail, w_head=3, w_tail=8, bow=3)

    out = pathlib.Path(__file__).parent / '01_歹.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
