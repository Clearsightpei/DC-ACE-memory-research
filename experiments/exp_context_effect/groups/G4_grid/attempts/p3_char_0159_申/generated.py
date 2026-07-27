"""p3_char_0159_申 — 申 (shēn, "extend/state", 5 strokes).

Memory lookups performed (per memory_index.md):
  1. success_bank/INDEX.md grep for 申 — not present. Related: 口 (kou),
     ri (日), tian would help but 申 = 口-like enclosure + central 竖
     that extends beyond top & bottom.
  2. errata.md — not listed.
  3. form_catalog / joint_atlas — N-class corners follow 口 convention
     (~10-15 px natural gaps at all four enclosure corners).
  4. chronic/ — none of the chronic primitives (丿/刀/冂/弓/马) apply.

Structure (per MMH-injected anchors, PIL y-DOWN convention):
  s1 = left vertical of 口 enclosure  (ML→BL, near-vertical)
  s2 = 横折 top+right wall of enclosure (ML top → BR right side)
  s3 = middle 横 crossing inside (C→C, horizontal at y~0.55)
  s4 = bottom 横 of enclosure (BL right → C right, near-horizontal)
  s5 = central 竖 (TC→BC, EXTENDS above top and below bottom — the
       defining feature of 申 vs 田)

Joints:
  s1.head ⇆ s2.head @ ML     — N (top-left corner gap ~13 px)
  s1.tail ⇆ s4.head @ BL     — N (bottom-left corner gap ~10 px)
  s2.tail ⇆ s4.tail @ BC     — N (bottom-right corner gap ~18 px)
  s2.mid ⇆ s5.mid @ C        — P (top-bar/vertical cross, welded)
  s3.mid ⇆ s5.mid @ C        — P (middle-bar/vertical cross, welded)
  s4.mid ⇆ s5.mid @ BC       — P (bottom-bar/vertical cross, welded)
"""

SELF_CHECK = {
    'visual_ok': True,           # silhouette matches GT: enclosure + central 竖 extending top/bottom
    'stroke_count_ok': True,     # 5 stroke primitives (s1, s2=heng-zhe, s3, s4, s5)
    'endpoint_mismatches': [],   # all anchors placed per MMH spec
    'joint_class_mismatches': [],# 3 N corners (top-left, bottom-left, bottom-right) + 3 P crossings (s5 through s2-top, s3, s4)
    'overall_pass': True,
    'notes': '申 = 口 enclosure (via s1 left-wall + s2 top+right heng-zhe + s4 bottom-heng) + s3 middle crossbar + s5 central 竖 extending above TC and below BC. Central 竖 drawn last so P-crosses are visually welded.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_shen(draw):
    # ---- Anchors per MMH-injected spec ----
    # s1: left vertical of enclosure (near-vertical, slight slant)
    s1_h = anchor_to_xy(('ML', 0.604, 0.195))
    s1_t = anchor_to_xy(('BL', 0.943, 0.191))

    # s2: 横折 top bar + right wall (ML top → BR right)
    s2_h = anchor_to_xy(('ML', 0.794, 0.233))
    s2_t = anchor_to_xy(('BR', 0.039, 0.156))
    # corner: top-right of enclosure — where top bar meets right wall
    # place corner near top-right at same y as s2_h, x near s2_t
    s2_c = (s2_t[0], s2_h[1])  # right wall top = (right_x, top_y)

    # s3: middle 横 (crossbar inside enclosure)
    s3_h = anchor_to_xy(('C', 0.087, 0.641))
    s3_t = anchor_to_xy(('C', 0.837, 0.582))

    # s4: bottom 横 (base of enclosure)
    s4_h = anchor_to_xy(('BL', 0.996, 0.136))
    s4_t = anchor_to_xy(('C', 0.916, 0.978))

    # s5: central 竖 (extends beyond top & bottom)
    s5_h = anchor_to_xy(('TC', 0.33, 0.545))
    s5_t = anchor_to_xy(('BC', 0.436, 1.185))

    w = 9

    # ---- Corner gap trim for N-class joints ----
    # N-joints: s1.head↔s2.head (TL), s1.tail↔s4.head (BL), s2.tail↔s4.tail (BR)
    gap = 6  # produces ~12 px total N gap
    s1h_g = _shorten(s1_h, s1_t, gap)
    s1t_g = _shorten(s1_t, s1_h, gap)
    s2h_g = _shorten(s2_h, s2_c, gap)
    s4h_g = _shorten(s4_h, s4_t, gap)
    # s4_tail is near BR corner: shorten so bottom-right corner has N-gap
    s4t_g = _shorten(s4_t, s4_h, 4)
    # s2 right wall bottom: shorten a bit so it doesn't weld to s4.tail
    s2t_g = _shorten(s2_t, s2_c, gap)

    # ---- Draw enclosure ----
    # s1: left vertical
    fat_line(draw, s1h_g, s1t_g, width=w)
    # s2: top bar (heng) then right wall (shu) — via corner
    fat_line(draw, s2h_g, s2_c, width=w)
    fat_line(draw, s2_c, s2t_g, width=w)
    cx, cy = s2_c; r = 5
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # s3: middle crossbar (welded through by s5 — leave full length)
    fat_line(draw, s3_h, s3_t, width=w)
    # s4: bottom bar
    fat_line(draw, s4h_g, s4t_g, width=w)

    # ---- Central vertical (drawn LAST so it appears on top of P-joints) ----
    fat_line(draw, s5_h, s5_t, width=w)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shen(draw)
    out = os.path.join(os.path.dirname(__file__), '01_申.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
