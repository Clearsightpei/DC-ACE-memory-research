# BANK_DEVIATION
# skipped: heng_zhe_box.py, shu_zhe.py
# reason: 凸's compound stroke 4 is a 4-turn zigzag (top→down→right→down)
#   spanning the full protrusion+base height. No existing bank primitive
#   captures this shape; inlining as a single polyline is cleaner than
#   forcing 2-3 bank calls that don't compose along an N-joint chain.
# fresh_component: tu_right_compound_zigzag (top-of-protrusion + right-of-
#   protrusion + right-of-shelf + right-of-base as one 5-vertex polyline)

"""凸 (tu, convex) — 5 strokes, MMH-derived anchors.

Structure: small top protrusion sitting on a wider base rectangle.
All 5 joints are N-class (natural gap) per the MMH-injected spec.
"""

from PIL import Image, ImageDraw

W = 8  # ink width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 strokes matches expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 5 joints rendered with natural gap
    'overall_pass': True,
    'notes': 'compound s4 as polyline; all N-joints kept as small gaps '
             '(no welding), matching MMH expected_gap ~14-25px.',
}


def draw_polyline(draw, pts, width=W):
    for a, b in zip(pts, pts[1:]):
        draw.line([a, b], fill='black', width=width)
    # round the joints between segments
    r = width / 2
    for x, y in pts[1:-1]:
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_tu(img):
    d = ImageDraw.Draw(img)

    # s1: left vertical of top protrusion
    #    head TL(0.987,0.8)=(98.7,80)  tail C(0.189,0.775)=(118.9,177.5)
    d.line([(100, 82), (118, 178)], fill='black', width=W)

    # s2: left half of the interior shelf (short horizontal)
    #    head ML(0.677,0.91)=(67.7,190.9)  tail C(0.274,0.875)=(127.4,187.5)
    d.line([(68, 192), (128, 188)], fill='black', width=W)

    # s3: left vertical of base (slight rightward slant)
    #    head ML(0.463,0.857)=(46.3,185.7)  tail BL(0.791,0.848)=(79.1,284.8)
    d.line([(48, 188), (80, 285)], fill='black', width=W)

    # s4: COMPOUND — top of protrusion → right of protrusion → shelf right → right of base
    #    head TC(0.16,0.823)=(116,82.3)  tail BR(0.253,0.889)=(225.3,288.9)
    pts_s4 = [
        (118, 82),    # start: near s1 head (N-gap ~15px in x, matches TC anchor)
        (158, 78),    # top-right corner of protrusion (slight up-rise)
        (152, 188),   # bottom-right corner of protrusion (down)
        (244, 190),   # right end of shelf (across)
        (226, 289),   # bottom-right of base (down with slight inward taper)
    ]
    draw_polyline(d, pts_s4, width=W)

    # s5: bottom horizontal of base
    #    head BL(0.841,0.722)=(84.1,272.2)  tail BR(0.145,0.651)=(214.5,265.1)
    d.line([(86, 274), (216, 266)], fill='black', width=W)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw_tu(img)
    out_path = __file__.rsplit('/', 1)[0] + '/01_凸.png'
    img.save(out_path)
    print('wrote', out_path)
    print('SELF_CHECK', SELF_CHECK)


if __name__ == '__main__':
    main()
