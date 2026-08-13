"""p3_char_0282_兇 (xiōng, "fierce") — 6 strokes.

Structure: 凶 (top, 4 strokes) + 儿 (bottom, 2 strokes).

Stroke plan (from MMH anchors + GT visual):
  s1: pie (X left leg)     TC(162,57)  -> ML(96,154)
  s2: short na/heng-diag   TC(106,91)  -> C(178,137)   [X-cross with s1: welded P at cell C]
  s3: 竖折-like curve      ML(67,112)  -> C(195,158)   [outer 凵 container, curved bottom]
  s4: short shu (right)    TR(212,91)  -> MR(200,183)  [right vertical of container]
  s5: pie (儿 left leg)    C(110,187)  -> BL(33,302)
  s6: shu_wan_gou (儿 right leg)  C(152,175) -> BR(274,235)

Bank primitives reused: pie, na, heng, shu_wan_gou. s3 is inlined
because no simple 竖折-with-curved-U primitive exists in the bank; it's
the outer container of 凶 and needs the U belly to hit the joint anchors.
# BANK_DEVIATION
# skipped: shu_zhe.py  (does not curve at the bend — 凶's outer 凵 belly is a smooth U)
# reason: MMH s3 mids at (87,152), (109,184), (148,173) require a smooth catenary belly, not an axis-aligned right-angle bend.
# fresh_component: kan_container_for_xiong (a smoothly-U-bellied 竖折 tracing 凵)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from na import draw_na
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes: pie, na, kan_container (inlined), shu (inlined), pie, shu_wan_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'X-cross (s1/s2) welded near cell C center. Container s3 curved through belly points. All 儿 joints are N gaps.'
}


def _bezier3(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def draw_kan_container(d, head, tail, width=7):
    """Fresh inlined 凵-container: down from head, shallow belly, up to tail.

    MMH mid-anchors (path fractions):
      0.21 ~ (87,152)  0.54 ~ (109,184)  0.73 ~ (148,173)
    Belly depth ~y=182 (must sit above s5.head@y=187 with ~11px gap).
    """
    hx, hy = head
    tx, ty = tail
    belly_y = 180
    # Descending phase: from head down and slightly right to the belly-left
    c1 = (hx + 4, hy + 30)
    c2 = (hx + 20, belly_y - 4)
    knee_l = (hx + 42, belly_y)
    seg1 = _bezier3(head, c1, c2, knee_l, n=50)
    # Belly across
    c3 = (hx + 70, belly_y + 2)
    knee_r = (hx + 95, belly_y - 4)
    seg2 = _bezier3(knee_l, c3, (hx + 90, belly_y), knee_r, n=40)
    # Rising phase to tail
    c4 = (knee_r[0] + 15, belly_y - 10)
    c5 = (tx - 6, ty + 8)
    seg3 = _bezier3(knee_r, c4, c5, tail, n=50)
    pts = seg1 + seg2[1:] + seg3[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    d.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_short_shu(d, head, tail, width=7):
    """Fresh short vertical (inlined) for right-side of 凶 container."""
    d.line([head, tail], fill='black', width=width)
    r = width // 2 + 1
    for (x, y) in (head, tail):
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_xiong(d, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return (ox + x * scale, oy + y * scale)

    # s1: pie — TC(162.3, 57.1) -> ML(95.8, 153.5)
    draw_pie(d, T(162.3, 57.1), T(95.8, 153.5),
             bow_perp=6, w_head=7, w_tail=3, steps=70)

    # s2: short na-ish diagonal — TC(105.8, 91.4) -> C(177.8, 136.5)
    # Welded X-cross with s1 near their mids (~cell C).
    draw_na(d, T(105.8, 91.4), T(177.8, 136.5),
            bow_perp=4, w_head=4, w_tail=8, steps=60)

    # s3: outer 凵 container — ML(66.8, 112.2) -> C(195.1, 158.2)
    draw_kan_container(d, T(66.8, 112.2), T(195.1, 158.2), width=7)

    # s4: short right vertical — TR(211.8, 90.8) -> MR(200.16, 182.5)
    # N gap ~24px from s3.tail (195,158) — the tail of s4 (200,183) sits below s3.tail.
    draw_short_shu(d, T(211.8, 90.8), T(200.16, 182.5), width=7)

    # s5: 儿 left leg (pie) — C(112.5, 186.9) -> BL(33.1, 301.8)
    draw_pie(d, T(112.5, 186.9), T(33.1, 301.8),
             bow_perp=12, w_head=9, w_tail=2, steps=80)

    # s6: 儿 right leg (shu_wan_gou) — C(152.3, 175.5) -> BR(273.9, 235.3)
    draw_shu_wan_gou(d, T(152.3, 175.5), T(273.9, 235.3),
                     width=7, bottom_extra=55, knee_ratio=0.70)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_xiong(d)
    out = Path(__file__).parent / "01_兇.png"
    img.save(out)
    print(f"wrote {out}")
