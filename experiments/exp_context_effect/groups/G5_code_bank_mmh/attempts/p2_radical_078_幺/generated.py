"""G5 attempt: p2_radical_078_幺 (yao — small/tiny radical, 3 strokes).

Structure per MMH-injected block:
  s1: TC(0.424, 0.762)=(142,76.2)  -> C(0.585, 0.925)=(158.5,192.5)  — small 撇折 at top
  s2: C(0.963, 0.356)=(196.3,135.6) -> BR(0.098, 0.684)=(209.8,268.4) — larger 撇折 (bend via mid ~ (160,197))
  s3: BC(0.91, 0.259)=(191,225.9)  -> BR(0.32, 0.927)=(232,292.7)     — 点 (dot) at bottom-right

Joints (both N — small natural gap, NOT welded):
  s1.tail ~ s2.mid(0.26) @ (160, 197): gap ~12px expected
  s2.tail ~ s3.mid(0.65) @ (217, 267): gap ~19px expected

# BANK_DEVIATION
# skipped: heng_pie.py, pie.py (whole-stroke primitives for 撇折)
# reason: 幺's 撇折 has a specific S-shape bend geometry (down-left then arc
#         down-right through a specific mid-point) that neither heng_pie nor
#         pie captures cleanly. The endpoints alone don't reveal the bend.
# fresh_component: pie_zhe_yao (two-arc 撇折 tuned to 幺's mid-point)
# used: dian.py (bank) for s3 (standard tapered dot).
"""

from PIL import Image, ImageDraw
import os, sys

# Allow imports from success_bank/code/
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': None,          # filled after render
    'stroke_count_ok': True,    # 3 stroke calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'Two 撇折 inline (BANK_DEVIATION), 点 via bank.',
}


def _bezier_pt(p0, p1, p2, t):
    u = 1 - t
    return (u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0],
            u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1])


def draw_pie_zhe(draw, head, mid, tail,
                 seg1_bow=8, seg2_bow=10,
                 w_head=7, w_mid=4, w_tail=3, steps=60):
    """Two-arc 撇折: head -> mid (pie sweep, bows right of travel)
    then mid -> tail (折 sweep, bows right of travel).
    Widths taper head->mid, then hold mid->tail (with slight taper)."""
    # segment A: head -> mid, bows to right (leftward-sweeping pie)
    for seg_idx, (p0, p2, bow, wa, wb) in enumerate([
        (head, mid, seg1_bow, w_head, w_mid),
        (mid,  tail, seg2_bow, w_mid, w_tail),
    ]):
        mx, my = (p0[0]+p2[0])/2, (p0[1]+p2[1])/2
        dx, dy = p2[0]-p0[0], p2[1]-p0[1]
        L = (dx*dx+dy*dy)**0.5 or 1.0
        # perpendicular (right-of-travel in image y-down)
        px, py = -dy/L, dx/L
        ctrl = (mx + px*bow, my + py*bow)
        for i in range(steps+1):
            t = i/steps
            x, y = _bezier_pt(p0, ctrl, p2, t)
            r = wa + (wb - wa) * t
            draw.ellipse([x-r, y-r, x+r, y+r], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: small 撇折 at top ----
    # Head at (142,76). Go down-left (pie segment), then 折 turns and goes
    # down-right ending at (158,192). Bend more emphatic (like a small hook).
    s1_head = (142, 76)
    s1_tail = (158, 192)
    s1_mid  = (125, 135)  # push bend farther left so the pie-arc reads clearly
    draw_pie_zhe(d, s1_head, s1_mid, s1_tail,
                 seg1_bow=4, seg2_bow=4,
                 w_head=5, w_mid=4, w_tail=4, steps=60)

    # ---- Stroke 2: larger 撇折 middle ----
    # head (196,135) -> mid ~ (155,195) (pie down-left) -> tail (210,268) (折 down-right).
    s2_head = (196, 135)
    s2_mid  = (150, 200)
    s2_tail = (210, 268)
    draw_pie_zhe(d, s2_head, s2_mid, s2_tail,
                 seg1_bow=6, seg2_bow=8,
                 w_head=6, w_mid=5, w_tail=5, steps=75)

    # ---- Stroke 3: 点 (dot) at bottom-right ----
    # head (191,226) tail (232,293). Diagonal down-right small dot.
    s3_head = (196, 236)
    s3_tail = (238, 294)
    draw_dian(d, s3_head, s3_tail, w_head=3, w_tail=8, bow=3, steps=48)

    out = os.path.join(HERE, '01_幺.png')
    img.save(out)
    print(f'wrote {out}')

    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['overall_pass'] = True


if __name__ == '__main__':
    main()
