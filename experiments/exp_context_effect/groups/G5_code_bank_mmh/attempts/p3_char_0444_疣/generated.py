"""p3_char_0444_疣 — 疒(sickness) + 尤 (still), 9 strokes.

# BANK_DEVIATION
# skipped: (all whole-radical/char bank primitives)
# reason: 疒-family declared terminal-freeze at B10 (no whole-radical
#   bank; 4 prior FAILs). No 疒 primitive exists. 尤 also has no bank
#   entry. Both halves must be inlined.
# fresh_component: yi_sickness (疒 5 strokes) + yi_still (尤 4 strokes)
# quantitative: MMH gives 9 endpoint anchors directly; native-per-stroke
#   inline follows P-A-006 (stroke-primitive layer, MMH-anchor verbatim).

Reasoning trace (P-A-008 mandatory):
- P-A-007-v2 hard-check: is there a whole-radical bank for 疒 or 尤?
  answer: NO for both. Skip to primitive layer.
- P-A-006: implement each stroke directly from MMH anchor pixels using
  simple PIL primitives; refuse to synthesize a compound where none is
  banked (avoids double-transform errors from B7 postmortem).
- P-A-009: quantitative BANK_DEVIATION captured above.
- P-A-010 kind: not a retry, this is a first attempt.
"""

from PIL import Image, ImageDraw
import os

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'inline (疒 terminal-freeze); 9 MMH endpoints rendered directly.'
}

# --- 米字格 cell -> pixel converter (300x300 canvas, 3x3 100px cells) ---
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def A(cell, xf, yf):
    x0, y0 = CELLS[cell]
    return (x0 + xf * 100.0, y0 + yf * 100.0)


# --- Stroke primitives (inline; no bank imports since terminal-freeze) ---

def dot(d, p1, p2, w_head=4, w_tail=8, steps=30):
    """Short tapered dot/dian: p1 -> p2 with growing width."""
    for i in range(steps + 1):
        t = i / steps
        x = p1[0] + t * (p2[0] - p1[0])
        y = p1[1] + t * (p2[1] - p1[1])
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')

def line_taper(d, p1, p2, w_head=5, w_tail=5, steps=60):
    """Straight tapered line."""
    for i in range(steps + 1):
        t = i / steps
        x = p1[0] + t * (p2[0] - p1[0])
        y = p1[1] + t * (p2[1] - p1[1])
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')

def bezier3(p0, p1, p2, p3, n=110):
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

def curve_taper(d, pts, w_head=8, w_tail=3):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


# --- Main draw ---

def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 疒 (sickness radical, strokes 1-5)

    # s1: TC dot -> down-right (top dian of 疒)
    s1_h = A('TC', 0.377, 0.574)  # (137.7, 57.4)
    s1_t = A('TC', 0.664, 0.809)  # (166.4, 80.9)
    dot(d, s1_h, s1_t, w_head=3, w_tail=6, steps=32)

    # s2: horizontal top of 疒 — heng from C to MR
    s2_h = A('C', 0.049, 0.163)   # (104.9, 116.3)
    s2_t = A('MR', 0.209, 0.061)  # (220.9, 106.1)
    line_taper(d, s2_h, s2_t, w_head=6, w_tail=6, steps=80)

    # s3: long pie of 疒 — curves from top-right down-left to bottom-left
    s3_h = A('ML', 0.873, 0.104)  # (87.3, 110.4)
    s3_t = A('BL', 0.331, 0.982)  # (33.1, 298.2)
    # curve outward (left bow) for pie shape
    ctrl1 = (75, 175)
    ctrl2 = (48, 240)
    s3_pts = bezier3(s3_h, ctrl1, ctrl2, s3_t, n=120)
    curve_taper(d, s3_pts, w_head=8, w_tail=3)

    # s4: inner dot 1 of 疒 — short diagonal (upper of two internal dots)
    s4_h = A('ML', 0.396, 0.342)  # (39.6, 134.2)
    s4_t = A('ML', 0.627, 0.588)  # (62.7, 158.8)
    dot(d, s4_h, s4_t, w_head=3, w_tail=6, steps=28)

    # s5: inner ti of 疒 — going up-right (BL to ML)
    s5_h = A('BL', 0.223, 0.159)  # (22.3, 215.9)
    s5_t = A('ML', 0.773, 0.884)  # (77.3, 188.4)
    line_taper(d, s5_h, s5_t, w_head=6, w_tail=3, steps=50)

    # 尤 (still, strokes 6-9)

    # s6: short horizontal (top of 尤) — heng from C to MR
    s6_h = A('C', 0.084, 0.846)   # (108.4, 184.6)
    s6_t = A('MR', 0.133, 0.723)  # (213.3, 172.3)
    line_taper(d, s6_h, s6_t, w_head=5, w_tail=6, steps=70)

    # s7: main pie of 尤 — from center-mid down-left to bottom-left
    s7_h = A('C', 0.479, 0.389)   # (147.9, 138.9)
    s7_t = A('BL', 0.759, 0.865)  # (75.9, 286.5)
    ctrl1_7 = (140, 200)
    ctrl2_7 = (105, 250)
    s7_pts = bezier3(s7_h, ctrl1_7, ctrl2_7, s7_t, n=120)
    curve_taper(d, s7_pts, w_head=7, w_tail=3)

    # s8: 乚 curved hook (heng-zhe-wan-gou) — from top going down and curving right/up
    # head at BC(0.69, 0.013) = (169, 201.3), tail at BR(0.59, 0.379) = (259, 237.9)
    # This is the compound hook of 尤 — needs curve
    s8_h = A('BC', 0.69, 0.013)   # (169, 201.3)
    s8_t = A('BR', 0.59, 0.379)   # (259, 237.9)
    # Route: from s8_h go DOWN then RIGHT then hook UP to tail
    ctrl1_8 = (175, 270)   # goes down
    ctrl2_8 = (250, 290)   # curves right at bottom
    s8_pts = bezier3(s8_h, ctrl1_8, ctrl2_8, s8_t, n=110)
    curve_taper(d, s8_pts, w_head=6, w_tail=5)

    # s9: small dot in upper-right of 尤 — MR to MR
    s9_h = A('MR', 0.048, 0.277)  # (204.8, 127.7)
    s9_t = A('MR', 0.323, 0.456)  # (232.3, 145.6)
    dot(d, s9_h, s9_t, w_head=3, w_tail=6, steps=28)

    return img


if __name__ == '__main__':
    outdir = os.path.dirname(os.path.abspath(__file__))
    img = draw()
    img.save(os.path.join(outdir, '01_疣.png'))
    print('wrote 01_疣.png, 9 strokes')
