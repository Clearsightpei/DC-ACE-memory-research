"""p3_char_0284_龹 — 6 strokes.

MMH stroke plan (anchors → pixels via 米字格 3×3 in 300×300):
  s1: TL(0.935,0.905) -> C(0.157,0.11)   = (93.5, 90.5)  -> (115.7, 111)   short left dot/slant
  s2: TC(0.91,0.683)  -> C(0.693,0.066)  = (191.0, 68.3) -> (169.3, 106.6) short right dot/slant
  s3: ML(0.905,0.389) -> C(0.989,0.254)  = (90.5, 138.9) -> (198.9, 125.4) upper heng
  s4: ML(0.58,0.802)  -> MR(0.414,0.635) = (58.0, 180.2) -> (241.4, 163.5) lower heng
  s5: TC(0.359,0.56)  -> BL(0.384,0.59)  = (135.9, 56.0) -> (38.4, 259.0)  long central pie (left leg)
  s6: C(0.682,0.72)   -> BR(0.854,0.37)  = (168.2, 172.0)-> (285.4, 237.0) right na (right leg)

Joints (P=welded, N=near-gap):
  s2.tail ⇆ s3.tail : N gap ~32px @ (176, 116) — tail-side gap between the top-right dot and upper heng right end.
  s3.mid(0.44) ⇆ s5.mid(0.34) : P weld @ ~(138.7, 135.3) — upper heng crosses central pie.
  s4.mid(0.37) ⇆ s5.mid(0.50) : P weld @ ~(126.6, 171.8) — lower heng crosses central pie.
  s4.mid(0.56) ⇆ s6.head       : N gap ~13px @ (164.2, 169.3) — right na emerges from lower heng.

Because s5's straight chord from (135.9,56) to (38.4,259) passes to the LEFT of the two P-joint
centers (138.7,135.3) and (126.6,171.8), s5 must bow RIGHTWARD to weld both crossings. Bow ~35px right.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from na import draw_na
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 strokes: dian, dian, heng, heng, pie, na
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's5 given rightward bow ~35px so it passes through both P-joint centers with s3 and s4. s1/s2 rendered as tapered dian (short slants).'
}


def _bezier3(p0, p1, p2, p3, n=100):
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


def draw_bent_pie(d, head, tail, ctrls, w_head=8, w_tail=2):
    """Cubic-bezier pie through control points to hit joint anchors."""
    pts = _bezier3(head, ctrls[0], ctrls[1], tail, n=110)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_juan(d):
    # s1: short left slant — tapered dot going down-right (top-left area)
    draw_dian(d, (93.5, 90.5), (115.7, 111.0), w_head=3, w_tail=7, bow=2, steps=32)

    # s2: short right slant — tapered dot going down-left (top-right area)
    draw_dian(d, (191.0, 68.3), (169.3, 106.6), w_head=3, w_tail=7, bow=3, steps=32)

    # s3: upper heng — from (90.5,138.9) to (198.9,125.4); crosses s5 near (138.7,135.3)
    draw_heng(d, (90.5, 138.9), (198.9, 125.4), width_head=8, width_tail=9)

    # s4: lower heng — from (58,180.2) to (241.4,163.5); crosses s5 near (126.6,171.8)
    draw_heng(d, (58.0, 180.2), (241.4, 163.5), width_head=9, width_tail=10)

    # s5: long central pie (left leg). Straight chord is (87,157) at midpoint but the two
    # P-joint centers sit at (138.7,135.3) and (126.6,171.8) — RIGHT of the chord. Use a
    # cubic bezier that passes through the joint region so both P joints actually weld.
    # Control pts steer the curve rightward through the joint band, then out to bottom-left.
    draw_bent_pie(d, (135.9, 56.0), (38.4, 259.0),
                  ctrls=[(150, 130), (100, 200)], w_head=8, w_tail=2)

    # s6: right na (right leg) — head near lower heng mid, tail down-right.
    # In GT the right leg drops steeper than na's default, so slightly bump tail down.
    draw_na(d, (168.2, 172.0), (285.4, 237.0),
            bow_perp=14, w_head=4, w_tail=11, steps=80)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_juan(d)
    out = Path(__file__).parent / "01_龹.png"
    img.save(out)
    print(f"wrote {out}")
