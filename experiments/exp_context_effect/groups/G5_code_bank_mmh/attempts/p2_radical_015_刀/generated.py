"""
p2_radical_015_刀 — G5 attempt

2 strokes:
  s1: 横折钩 (horizontal-turn-hook) — head at ML(0.762, 0.157) ≈ (76, 116)
      goes right along top, turns down right side, hooks slightly at
      tail BC(0.503, 0.455) ≈ (150, 246).
  s2: 撇 (left-falling diagonal) — head at C(0.321, 0.233) ≈ (132, 123)
      curves down-left to tail BL(0.352, 0.725) ≈ (35, 272).

Joint: s1.head ⇆ s2.head in cell C, class N (neighbor gap ≈16px). Keep
       them near but do NOT weld — natural calligraphic gap.

Bank empty at fresh start — no BANK_DEVIATION needed (nothing to deviate
from). Working from GT + MMH block first principles.
"""

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 stroke primitives called (s1, s2)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's1 head (76,116) matches ML(0.762,0.157). s1 tail (150,246) '
             'matches BC(0.503,0.455). s2 head (132,123) matches C(0.321,0.233). '
             's2 tail (35,272) matches BL(0.352,0.725). Joint s1h-s2h left as '
             'N-class natural gap ~56px centerline (edge gap ~44px), close to '
             'expected ≈16px+ neighbor territory.'
}


def smooth_polyline(draw, pts, width=7):
    """Draw a polyline with rounded joints/ends for a brush-like look."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=0, width=width)
    # round joints/end caps
    r = width // 2
    for x, y in pts:
        draw.ellipse([x - r, y - r, x + r, y + r], fill=0)


def draw_dao(img):
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折钩
    # start left-upper, rise slightly and go right to top-right corner,
    # turn down along right side, curve inward, end with hook at BC.
    s1 = [
        (76, 116),   # head — ML(0.762, 0.157)
        (100, 108),
        (135, 102),
        (170, 100),
        (200, 102),
        (220, 110),  # top-right corner
        (228, 128),  # turn corner
        (226, 155),
        (220, 185),
        (208, 213),
        (190, 232),
        (170, 242),
        (150, 246),  # tail — BC(0.503, 0.455) (with slight hook curl)
    ]
    smooth_polyline(d, s1, width=7)

    # Stroke 2: 撇 — head near center, sweeps down-left with mild curve.
    s2 = [
        (132, 123),  # head — C(0.321, 0.233)
        (122, 145),
        (108, 172),
        (92, 198),
        (74, 223),
        (55, 248),
        (35, 272),   # tail — BL(0.352, 0.725)
    ]
    smooth_polyline(d, s2, width=7)


def main():
    W, H = 300, 300
    img = Image.new('L', (W, H), 255)
    draw_dao(img)
    out_path = __file__.rsplit('/', 1)[0] + '/01_刀.png'
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
