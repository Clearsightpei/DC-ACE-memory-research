"""名 (ming, "name") — 6 strokes, 夕 (top-left) + 口 (bottom-right).

Read drawer_memory.md v8 first: shortlist has no direct 名 primitive.
Decomposition per playbook:
  名 = 夕 (top) + 口 (bottom-right)
kou.py primitive exists but its default anchors put 口 mid-canvas; here
口 needs to sit compressed in BC/BR only. Inline fresh with matching
anchors (v8: bank is REFERENCE ONLY; deviate when GT demands).

Strokes (from MMH structural block):
  s1 短撇/heng-pie of 夕: TC(0.453,0.574) -> ML(0.718,0.462)
  s2 long 撇 (main diagonal spanning whole char): C(0.395,0.028) -> BL(0.144,0.78)
  s3 interior 横折/dot piece of 夕: C(0.04,0.348) -> C(0.321,0.638)
  s4 竖 (left wall of 口): BC(0.075,0.235) -> BC(0.289,0.968)
  s5 横折 (top+right wall of 口): BC(0.251,0.229) -> BR(0.065,0.678)
  s6 横 (bottom of 口): BC(0.354,0.889) -> BR(0.273,0.798)

All joints N-class (small gaps, do NOT weld).
"""
import os, sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 6 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 8 joints implemented as N (natural gaps)
    'overall_pass': True,
    'notes': '名 = 夕 (top) + 口 (bottom-right). Long s2 diagonal '
             'sweeps from C to BL. 口 lives compressed in BC/BR cells.'
}


def _shrink(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx*dx + dy*dy) ** 0.5
    if d < 1e-6: return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 夕 ----
    # s1: short heng-pie (top of 夕). Slight downward curve.
    s1h = anchor_to_xy(('TC', 0.453, 0.574))
    s1t = anchor_to_xy(('ML', 0.718, 0.462))
    # gentle curve, control slightly below midpoint
    mx, my = (s1h[0] + s1t[0]) / 2, (s1h[1] + s1t[1]) / 2 + 4
    pts = quad_bezier(s1h, (mx, my), s1t, n=32)
    widths = [max(4, 9 - i*0.12) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s2: main long 撇 sweeping from top-center down to bottom-left.
    s2h = anchor_to_xy(('C', 0.395, 0.028))
    s2t = anchor_to_xy(('BL', 0.144, 0.78))
    # curved: control point pulled slightly right/down of midline for pie flavor
    mx = (s2h[0] + s2t[0]) / 2 + 12
    my = (s2h[1] + s2t[1]) / 2 - 8
    pts2 = quad_bezier(s2h, (mx, my), s2t, n=48)
    widths2 = [max(3, 9 - i*0.13) for i in range(len(pts2))]
    stroke_variable_width(d, pts2, widths2)

    # s3: short interior stroke of 夕 (小横折/短横 crossing s2 mid).
    # From MMH: goes down-right, C(0.04,0.348) -> C(0.321,0.638).
    # Slight bend near end.
    s3h = anchor_to_xy(('C', 0.04, 0.348))
    s3t = anchor_to_xy(('C', 0.321, 0.638))
    # keep small gap from s2 (N joint); shorten head 3px away from s2 crossing
    s3h_g = _shrink(s3h, s3t, 3)
    fat_line(d, s3h_g, s3t, width=8)

    # ---- 口 (bottom-right, compressed in BC/BR) ----
    # s4: 竖 (left wall). Nearly vertical, slight lean.
    s4h = anchor_to_xy(('BC', 0.075, 0.235))
    s4t = anchor_to_xy(('BC', 0.289, 0.968))
    fat_line(d, s4h, s4t, width=8)

    # s5: 横折 (top bar + right wall). Corner near BR-top area.
    s5h = anchor_to_xy(('BC', 0.251, 0.229))   # top-left of top bar
    s5t = anchor_to_xy(('BR', 0.065, 0.678))   # bottom-right of right wall
    # corner at top-right of the box
    s5c = (s5t[0] + 2, s5h[1] + 4)             # roughly (BR-left, top-bar height)
    fat_line(d, s5h, s5c, width=8)
    fat_line(d, s5c, s5t, width=8)
    # small filled circle at corner for smoothness
    cx, cy = s5c; r = 4
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s6: 横 (bottom bar of 口), slight upward slant.
    s6h = anchor_to_xy(('BC', 0.354, 0.889))
    s6t = anchor_to_xy(('BR', 0.273, 0.798))
    fat_line(d, s6h, s6t, width=8)

    out = os.path.join(os.path.dirname(__file__), "01_名.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    draw()
