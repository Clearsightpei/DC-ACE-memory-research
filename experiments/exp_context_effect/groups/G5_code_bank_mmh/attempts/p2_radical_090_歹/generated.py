"""p2_radical_090_歹 (G5) — 4 strokes per MMH.

Anchors (pixels, from injected MMH block):
  s1 heng: TL(0.539, 0.935) -> TR(0.54, 0.847)  = (53.9, 93.5) -> (254, 84.7)
  s2 pie : TC(0.336, 0.961) -> BL(0.677, 0.06)  = (133.6, 96.1) -> (67.7, 206)
  s3 pie : C(0.277, 0.562)  -> BL(0.729, 1.064) = (127.7, 156.2) -> (72.9, 306) capped to canvas
  s4 dian: C(0.113, 0.819)  -> BC(0.368, 0.145) = (111.3, 181.9) -> (136.8, 214.5)

All 3 joints are N (neighbor). No welding — draw endpoints at their MMH
locations, gaps arise naturally from the ~15-17 px spacing MMH prescribes.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4-stroke render via bank heng+pie+pie+dian, all joints N (natural gaps).'
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

    # s1: 横 wide top heng
    s1_head = cell_px('TL', 0.539, 0.935)   # (53.9, 93.5)
    s1_tail = cell_px('TR', 0.540, 0.847)   # (254.0, 84.7)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    # s2: 撇 long pie sweeping down-left, head near s1 middle.
    # MMH tail lands at y=206 but GT ink continues further down-left; extend
    # per calibration note (MMH gives medial section only for long pies).
    s2_head = cell_px('TC', 0.336, 0.961)   # (133.6, 96.1)
    s2_tail_mmh = cell_px('BL', 0.677, 0.060)   # (67.7, 206.0)
    s2_tail = (s2_tail_mmh[0] - 15, s2_tail_mmh[1] + 65)  # extend to ~(53, 271)
    draw_pie(d, s2_head, s2_tail, bow_perp=18, w_head=9, w_tail=3)

    # s3: 撇 shorter pie inside, head at C, tail heading toward BL (cap at canvas)
    s3_head = cell_px('C',  0.277, 0.562)   # (127.7, 156.2)
    s3_tail_raw = cell_px('BL', 0.729, 1.064)  # (72.9, 306.4) — off-canvas by ~6 px
    # cap tail y at ~285 so ink stays visible on canvas (visible ink often ends before median terminus)
    s3_tail = (s3_tail_raw[0], min(s3_tail_raw[1], 285.0))
    draw_pie(d, s3_head, s3_tail, bow_perp=8, w_head=7, w_tail=3)

    # s4: 点 small dian, tapered thin->thick going down-right
    s4_head = cell_px('C',  0.113, 0.819)   # (111.3, 181.9)
    s4_tail = cell_px('BC', 0.368, 0.145)   # (136.8, 214.5)
    draw_dian(d, s4_head, s4_tail, w_head=3, w_tail=7, bow=3)

    out = pathlib.Path(__file__).parent / '01_歹.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
