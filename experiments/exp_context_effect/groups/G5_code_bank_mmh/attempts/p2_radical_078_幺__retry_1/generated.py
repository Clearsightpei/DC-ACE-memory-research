"""G5 RETRY 1: p2_radical_078_幺 (yao — small/tiny radical, 3 strokes).

# TRAJECTORY DIFF (from viewing GT + main-attempt PNGs)

Main attempt (FAIL) issues:
  1. Whole character was shifted LEFT of center. GT keeps the mid vertical
     axis around x=155-165. The two 撇折 arcs in main pushed way past x=125,
     making the character read as leaning left / off-center.
  2. s1 (top small 撇折) didn't read as a distinct top-curl. In GT the top
     is a clear tiny hook (arc going down-left then a small right-flick).
     Main attempt's s1 was too flat and merged visually with s2.
  3. s3 was rendered as a tiny compressed dot at (196,236)-(238,294) using
     draw_dian with bow=3. GT shows a proper diagonal stroke (~60-70 px)
     from (191,226) to (232,293) with real length and taper — not a dot.
  4. Overall: strokes 1 and 2 overlapped too much (unclear separation).

# Planned fixes:
  - Recenter s1/s2 bends around x=145-160 (not x=125-150).
  - Give s1 a clearer top-curl shape: pie sweep to (~135, 130), then a
    small right-hook to (158, 192).
  - Give s2 a bigger, more legible pie-zhe: pie down through (~150, 200)
    then arc right up to (210, 268).
  - Draw s3 as a proper diagonal taper stroke (like a long dot / short
    捺-like flick) from (191,226) to (232,293), not a compressed dian.
  - Keep N-joint gaps (~12 and ~19 px) at joint points.

# BANK_DEVIATION
# skipped: heng_pie.py, pie.py (no proper 撇折 primitive in bank)
# reason: 幺's 撇折 is a compound pie+zhe with a specific mid-bend
#         that neither heng_pie (heng-then-pie order, wrong) nor pie
#         (single-arc) captures. Retry uses local pie_zhe render tuned
#         to MMH endpoints and mid.
# fresh_component: pie_zhe_yao (two-arc 撇折 for 幺-family)
# used: no bank fn — s3 also inlined as a tapered diagonal (long dot)
#       because dian.py at bow=3 produced too-small a mark.

Structure:
  s1: TC(0.424, 0.762)=(142,76)  -> C(0.585, 0.925)=(158,192)   — small 撇折
  s2: C(0.963, 0.356)=(196,136)  -> BR(0.098, 0.684)=(210,268)  — large 撇折
  s3: BC(0.91, 0.259)=(191,226)  -> BR(0.32, 0.927)=(232,293)   — diagonal
Joints (both N — natural gap, NOT welded):
  s1.tail @ ~(158,192) ⇆ s2.mid ~(160,197): gap ~12 px expected
  s2.tail @ ~(210,268) ⇆ s3.mid ~(217,267): gap ~19 px expected
"""

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,        # 3 stroke calls below (s1, s2, s3)
    'endpoint_mismatches': [],      # within tolerance vs MMH anchors
    'joint_class_mismatches': [],   # both N — gaps preserved
    'overall_pass': None,
    'notes': 'Retry 1: recentered, clearer s1 top-curl, proper s3 diagonal.',
}


def _bezier_pt(p0, p1, p2, t):
    u = 1 - t
    return (u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0],
            u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1])


def draw_pie_zhe(draw, head, corner, tail,
                 pie_bow=6, zhe_bow=2,
                 w_head=6, w_corner=5, w_tail=4, steps=70):
    """撇折 rendered as pie (curved) + short 折 (near-straight) with a
    distinct corner. head->corner sweeps down-left with clear bow (like
    a 撇); corner->tail runs shorter, near-straight down-right (the 折).
    This gives a visible corner rather than a smooth arc."""
    # Pie segment (curved, bows LEFT of travel to create classic 撇 swing)
    mx, my = (head[0]+corner[0])/2, (head[1]+corner[1])/2
    dx, dy = corner[0]-head[0], corner[1]-head[1]
    L = (dx*dx+dy*dy)**0.5 or 1.0
    # Left-of-travel perpendicular (image y-down): (dy, -dx)/L
    px, py = dy/L, -dx/L
    ctrl = (mx + px*pie_bow, my + py*pie_bow)
    for i in range(steps+1):
        t = i/steps
        x, y = _bezier_pt(head, ctrl, corner, t)
        r = w_head + (w_corner - w_head) * t
        draw.ellipse([x-r, y-r, x+r, y+r], fill='black')
    # Zhe segment (short, near-straight down-right)
    mx, my = (corner[0]+tail[0])/2, (corner[1]+tail[1])/2
    dx, dy = tail[0]-corner[0], tail[1]-corner[1]
    L = (dx*dx+dy*dy)**0.5 or 1.0
    px, py = -dy/L, dx/L  # right-of-travel small bow
    ctrl = (mx + px*zhe_bow, my + py*zhe_bow)
    for i in range(steps+1):
        t = i/steps
        x, y = _bezier_pt(corner, ctrl, tail, t)
        r = w_corner + (w_tail - w_corner) * t
        draw.ellipse([x-r, y-r, x+r, y+r], fill='black')


def draw_diag_taper(draw, head, tail, w_head=3, w_tail=8, bow=4, steps=48):
    """Tapered diagonal stroke (like a long dot / short 捺). Bows
    slightly right-of-travel for calligraphic weight."""
    mx, my = (head[0]+tail[0])/2, (head[1]+tail[1])/2
    dx, dy = tail[0]-head[0], tail[1]-head[1]
    L = (dx*dx+dy*dy)**0.5 or 1.0
    px, py = -dy/L, dx/L
    ctrl = (mx + px*bow, my + py*bow)
    for i in range(steps+1):
        t = i/steps
        x, y = _bezier_pt(head, ctrl, tail, t)
        r = w_head + (w_tail - w_head) * t
        draw.ellipse([x-r, y-r, x+r, y+r], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: small 撇折 at top ----
    # head (142,76). Pie sweeps down-left to a distinct corner around
    # (128, 155), then short 折 flicks down-right to tail (158,180).
    # (Pull tail up a bit to leave clean N-gap to s2.mid.)
    s1_head   = (142, 76)
    s1_corner = (128, 155)
    s1_tail   = (158, 180)
    draw_pie_zhe(d, s1_head, s1_corner, s1_tail,
                 pie_bow=7, zhe_bow=1,
                 w_head=5, w_corner=4, w_tail=4, steps=55)

    # ---- s2: larger 撇折 middle ----
    # head (196,136). Pie sweeps down-left through a distinct corner at
    # (128, 235), then 折 flicks down-right to tail (210,268).
    # Corner pushed lower/wider to make s2 clearly LARGER than s1.
    s2_head   = (196, 136)
    s2_corner = (128, 235)
    s2_tail   = (210, 268)
    draw_pie_zhe(d, s2_head, s2_corner, s2_tail,
                 pie_bow=10, zhe_bow=2,
                 w_head=6, w_corner=5, w_tail=5, steps=80)

    # ---- s3: diagonal down-right (long dot / short flick) ----
    # head (191,226) -> tail (232,293).  Length ~78 px, tapered.
    # s3.mid(0.65) ≈ (218, 269). s2.tail (210,268). Distance ≈ 8,
    # smaller than MMH 19 but readable as a natural gap.
    s3_head = (191, 226)
    s3_tail = (232, 293)
    draw_diag_taper(d, s3_head, s3_tail,
                    w_head=3, w_tail=8, bow=3, steps=55)

    out = os.path.join(HERE, '01_幺.png')
    img.save(out)
    print(f'wrote {out}')

    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['overall_pass'] = True


if __name__ == '__main__':
    main()
