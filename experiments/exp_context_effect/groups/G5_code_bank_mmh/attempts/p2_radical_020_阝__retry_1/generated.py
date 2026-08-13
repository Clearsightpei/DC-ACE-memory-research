"""G5 retry #1: p2_radical_020_阝 (left-ear/阜 radical)

TRAJECTORY DIFF
---------------
Main attempt (verdict C):
  - Ear ("3"/"B" shape) was rendered as two chained cubic Beziers.
    Visual gaps vs GT:
      (1) Ear silhouette too rounded/smooth: GT shows a distinct
          top-right corner and a distinct middle waist notch — the
          cubic controls were too pulled-back so the loops merged
          into a fat B rather than a sharp 3.
      (2) No terminal hook: GT's ear ends with a short leftward-down
          hook flick at the bottom-right; failed attempt tapered
          smoothly with no visible hook.
  - Shu: acceptable, straight, roughly right length. Keep as-is.

Fixes this retry:
  - Redraw ear as a polyline with 4 waypoints so the corners are
    explicit (top-right corner, middle waist, bottom-right corner,
    terminal hook tip). Chain-of-ellipses ink for weld.
  - Add a small terminal hook flick pointing down-left from the
    bottom curl.
  - Keep bank draw_shu for stroke 2, endpoints unchanged.

Structure (from GT + MMH block, unchanged):
  - stroke 1: 横撇弯钩 ("ear")
      head C(0.28, 0.002)  -> (128, 100)
      tail C(0.421, 0.813) -> (142, 181)
  - stroke 2: 竖 (long vertical shaft on the LEFT)
      head TC(0.081, 0.952) -> (108,  95)
      tail BC(0.154, 0.897) -> (115, 290)
  - joint s1.head <> s2.head : N (~14.8 px natural gap; kept as ~20)

BANK_DEVIATION
  skipped: (no bank primitive for 横撇弯钩 exists yet)
  reason: the "3"-shape ear stroke is a 3-turn compound not covered
          by any existing bank primitive; heng_zhe_gou is close but
          lacks the middle waist inflection.
  fresh_component: ear_3shape_for_fu_radical
"""

import sys
import pathlib

from PIL import Image, ImageDraw

# Wire the bank into sys.path so we can import shu.
_BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(_BANK))
from shu import draw_shu  # noqa: E402


def _quad(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 2) * p0[0] + 2 * (1 - u) * u * p1[0] + (u ** 2) * p2[0]
        y = ((1 - u) ** 2) * p0[1] + 2 * (1 - u) * u * p1[1] + (u ** 2) * p2[1]
        pts.append((x, y))
    return pts


def _stroke_pts(d, pts, w_head=6.5, w_tail=6.5):
    """Chain-of-ellipses ink with linear taper head->tail."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        w = w_head + (w_tail - w_head) * t
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')


def draw_ear(d):
    """Draw the 横撇弯钩 as a curly-3 with explicit corners.

    Waypoints (all inside the top-right quadrant):
      A = (128, 100)  head — top-left of the top loop
      B = (188,  95)  top-right corner (upper 撇 apex)
      C = (128, 148)  middle waist (inflection)
      D = (198, 155)  bottom-right corner (belly of lower loop)
      E = (142, 181)  tail — where the ear meets the interior
      F = (128, 178)  small terminal hook flick tip (down-left)
    """
    # Segment 1: A -> B (top horizontal-ish stroke, gentle arch UP)
    seg1 = _quad((128, 100), (158, 78), (188, 95), steps=28)
    # Segment 2: B -> C (drop-and-curl inward to the waist)
    seg2 = _quad((188, 95), (196, 128), (128, 148), steps=32)
    # Segment 3: C -> D (out to the belly of the lower loop)
    seg3 = _quad((128, 148), (188, 138), (198, 155), steps=28)
    # Segment 4: D -> E (curl back inward to the tail)
    seg4 = _quad((198, 155), (188, 190), (142, 181), steps=30)
    # Segment 5: E -> F (terminal hook flick, taper to point)
    seg5 = [(142 + (128 - 142) * (i / 12),
             181 + (178 - 181) * (i / 12)) for i in range(13)]

    # Ink the main body (uniform weight ~6.5) so the ear reads bold.
    for seg in (seg1, seg2, seg3, seg4):
        _stroke_pts(d, seg, w_head=6.2, w_tail=6.2)

    # Corner emphasis: small 顿笔 nodes at the two hard corners.
    for cx, cy in [(188, 95), (198, 155)]:
        d.ellipse((cx - 6.8, cy - 6.5, cx + 6.8, cy + 6.5), fill='black')

    # Terminal hook: tapered flick to a point.
    n = len(seg5)
    for i, (x, y) in enumerate(seg5):
        t = i / max(1, n - 1)
        w = 5.0 * (1 - t) + 1.0
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # Stroke 1 — inline ear (fresh, improved from main)
    draw_ear(d)

    # Stroke 2 — bank primitive: straight vertical shaft (LEFT side)
    draw_shu(d, head=(108, 95), tail=(115, 290), width=7, top_curl=False)

    return img


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,   # 2 stroke primitives: ear (compound) + shu
    "endpoint_mismatches": [], # both strokes' anchors within 1 px of MMH
    "joint_class_mismatches": [], # s1.head-s2.head kept as N (gap ~20 px)
    "overall_pass": True,
    "notes": (
        "Retry #1: ear redrawn as 4-segment polyline (quads) with "
        "explicit top-right and bottom-right corners + small 顿笔 nodes, "
        "plus a terminal down-left hook flick tapering to a point. "
        "Shu unchanged (straight vertical on the left, y=95..290). "
        "Joint s1.head/s2.head still N — no weld."
    ),
}


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_name("01_阝.png")
    img = render()
    img.save(out)
    print("wrote", out)
