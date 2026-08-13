"""p3_char_0143_勻 — G5 attempt.

勻 = 勹 (outer wrap; 2 strokes) + two small inner rising strokes (2 strokes).
Strategy: call draw_bao (bank) with a small offset that aligns its baked-in
geometry with the MMH-injected anchors, then inline two heng-like inner marks.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0,
                str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from bao_wrap import draw_bao  # noqa: E402
from heng import draw_heng      # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 strokes: draw_bao produces 2 (pie + wrap), + 2 inner hengs
    'endpoint_mismatches': [
        # s1 head expected TC(118.4,58); bao at ox=11,oy=-9 → (122.6,55.5). Δ≈(4,-2). same cell.
        # s1 tail expected ML(63.6,154.7); bao → (67,159.2). Δ≈(3,4). same cell.
        # s2 head expected C(113.1,121.3); bao → (109.7,124.6). Δ≈(-3,3). same cell.
        # s2 tail expected BC(162.3,268.1); bao → (156.3,265.2). Δ≈(-6,-3). same cell.
        # s3 head expected ML(98.7,170.8); actual (98.7,170.8). match.
        # s3 tail expected C(165.2,166.1); actual (165.2,166.1). match.
        # s4 head expected BL(68.8,229.1); actual (68.8,229.1). match.
        # s4 tail expected BC(180.5,221.5); actual (180.5,221.5). match.
    ],
    'joint_class_mismatches': [
        # joint 1: s1.mid ⇆ s2.head @ C, class N, expected gap ~21.3 px.
        # s1.mid (bao offset) ≈ ((122.6+67)/2, (55.5+159.2)/2) = (94.8, 107.35).
        # s2.head (bao offset) ≈ (109.7, 124.6). dist = sqrt(14.9^2 + 17.25^2) ≈ 22.8 px. N-class match.
    ],
    'overall_pass': True,
    'notes': 'draw_bao(ox=11, oy=-9) shifts bootstrap 勹 geometry to match MMH-勻 endpoints (~5px avg residual). Inner two strokes drawn at MMH exact positions with light taper.'
}


def render():
    img = Image.new('L', (300, 300), 255)
    d = ImageDraw.Draw(img)

    # strokes 1 & 2: outer 勹 wrap via bank primitive (offset to match MMH)
    draw_bao(d, ox=11, oy=-9, scale=1.0)

    # stroke 3: inner UPPER small heng — head ML(0.987, 0.708) → (98.7, 170.8),
    # tail C(0.652, 0.661) → (165.2, 166.1). Rises slightly right (Δy = -4.7).
    draw_heng(d,
              head=(98.7, 170.8),
              tail=(165.2, 166.1),
              width_head=5, width_tail=4)

    # stroke 4: inner LOWER small heng — head BL(0.688, 0.291) → (68.8, 229.1),
    # tail BC(0.805, 0.215) → (180.5, 221.5). Rises slightly right (Δy = -7.6).
    draw_heng(d,
              head=(68.8, 229.1),
              tail=(180.5, 221.5),
              width_head=5, width_tail=4)

    out = pathlib.Path(__file__).resolve().parent / '01_勻.png'
    img.save(out)
    return out


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
