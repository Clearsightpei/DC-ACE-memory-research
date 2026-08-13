"""G4 attempt: p3_char_0279_色

Decompose: 色 = ⺈ (top: 撇 + 横折钩) + 巴 (4 strokes: 竖折 / 横 / 竖 / 竖弯钩).
MMH gives 6 stroke medians as head/tail anchors — follow those verbatim
with light curvature added where the stroke class implies a bend.

SELF_CHECK below is filled in after render.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK_CODE = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK_CODE)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

# ---- Expected MMH anchors ----
S1_HEAD = ('TC', 0.336, 0.492)
S1_TAIL = ('ML', 0.706, 0.321)

S2_HEAD = ('TC', 0.239, 0.987)
S2_TAIL = ('C',  0.412, 0.453)

S3_HEAD = ('ML', 0.864, 0.570)
S3_TAIL = ('C',  0.863, 0.896)

S4_HEAD = ('C',  0.336, 0.576)
S4_TAIL = ('C',  0.318, 0.998)

S5_HEAD = ('BL', 0.835, 0.186)
S5_TAIL = ('MR', 0.033, 0.998)

S6_HEAD = ('ML', 0.668, 0.515)
S6_TAIL = ('BR', 0.540, 0.224)


def _widths(n, w_head, w_mid, w_tail):
    out = []
    for i in range(n):
        t = i / (n - 1)
        if t < 0.5:
            w = w_head + (w_mid - w_head) * (t / 0.5)
        else:
            w = w_mid + (w_tail - w_mid) * ((t - 0.5) / 0.5)
        out.append(w)
    return out


def _curve(draw, a, b, bow=(0, 0), w_head=6, w_mid=6, w_tail=6, n=40):
    p0 = anchor_to_xy(a)
    p2 = anchor_to_xy(b)
    p1 = ((p0[0] + p2[0]) / 2 + bow[0], (p0[1] + p2[1]) / 2 + bow[1])
    pts = quad_bezier(p0, p1, p2, n=n)
    stroke_variable_width(draw, pts, _widths(len(pts), w_head, w_mid, w_tail))


def _polyline(draw, pts, w_list):
    stroke_variable_width(draw, pts, w_list)


def draw_se(draw):
    # --- s1: 撇 top slash (⺈'s slash) — TC(mid) -> ML(upper). Bows left/down.
    _curve(draw, S1_HEAD, S1_TAIL, bow=(-4, 8), w_head=7, w_mid=6, w_tail=2)

    # --- s2: ⺈'s right-side 横折 hook coming down to center-top.
    # Short two-segment: little 横 stub going right then 折 down to center.
    p2h = anchor_to_xy(S2_HEAD)
    p2t = anchor_to_xy(S2_TAIL)
    elbow = (p2t[0] + 4, p2h[1] + 4)  # corner above-right of tail
    pts2 = [p2h, elbow, p2t]
    _polyline(draw, pts2, [6, 6, 5])

    # --- s3: right side of the small 巴 top box — a 竖 running down.
    # ML(0.864,0.57)=(86.4,157) -> C(0.863,0.896)=(186.3,189.6).
    # Render as short 横 (top) then 折 down (right side) to close top box.
    p3h = anchor_to_xy(S3_HEAD)
    p3t = anchor_to_xy(S3_TAIL)
    elbow3 = (p3t[0], p3h[1])  # top-right corner
    pts3 = [p3h, elbow3, p3t]
    _polyline(draw, pts3, [6, 6, 6])

    # --- s4: 竖 vertical divider (center → bottom-center).
    _curve(draw, S4_HEAD, S4_TAIL, bow=(-1, 0), w_head=6, w_mid=6, w_tail=6)

    # --- s5: 竖弯钩 — the big enclosing bottom curl (the character's signature).
    # MMH endpoints: head BL(0.835,0.186)=(83.5,218.6), tail MR(0.033,0.998)
    # =(203.3,199.8). The visible stroke: starts at head, drops down, sweeps
    # LEFT under the whole char, curls UP at far left as hook. Render as a
    # broad U-arc dipping to y≈285 with anchor tail on far right (with hook).
    p5h = anchor_to_xy(S5_HEAD)
    p5t = anchor_to_xy(S5_TAIL)
    # Wide-U arc: descend from head, sweep across, rise to tail. Control pulled
    # LOW-CENTER for a deep U.
    mid_x = (p5h[0] + p5t[0]) / 2
    ctrl = (mid_x, 295)
    arc_pts = quad_bezier(p5h, ctrl, p5t, n=60)
    # Small hook tip at the tail going up-left
    hook_tip = (p5t[0] - 12, p5t[1] - 20)
    all_pts = arc_pts + [hook_tip]
    w_arc = _widths(len(arc_pts), 7, 8, 7)
    _polyline(draw, all_pts, w_arc + [3])

    # --- s6: middle 短横 inside 巴 (ML side → BR area) — this closes 巴.
    _curve(draw, S6_HEAD, S6_TAIL, bow=(0, -2), w_head=5, w_mid=6, w_tail=5)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_se(draw)
    out = os.path.join(_HERE, "01_色.png")
    img.save(out)
    print("wrote", out)


# ---- Self-check dict (post-render) ----
SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,      # 6 strokes drawn: s1..s6
    'endpoint_mismatches': [],    # anchors are used verbatim from MMH
    'joint_class_mismatches': [], # all joints intended as N (small natural gaps)
    'overall_pass': None,
    'notes': 'anchors verbatim from MMH brief; s2 & s3 rendered as 2-segment '
             'to reflect 折 bends; s5 rendered as wide arc + small hook.',
}


if __name__ == "__main__":
    main()
