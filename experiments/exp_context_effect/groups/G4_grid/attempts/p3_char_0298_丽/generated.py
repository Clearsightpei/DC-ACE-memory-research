"""p3_char_0298_丽 — G4 attempt.

Reading order followed:
  1. drawer_memory.md — v8 checklist; no dedicated 丽 entry; chronic
     jiong_frame is oversized (230x210) for the twin-narrow compartments
     that MMH endpoints imply → inline 冂 twice with MMH-anchored L-shapes.
  2. success_bank/INDEX.md — no 丽; 冂 chronic exists but wrong scale for
     side-by-side twin narrow compartments in this glyph.
  3. errata.md — 丽 not listed.

Composition (7 strokes per MMH):
  s1 一 (top horizontal, spans canvas)
  s2 丨 left leg of LEFT compartment
  s3 横折 (heng-zhe) top+right of LEFT compartment
  s4 short mark inside LEFT compartment
  s5 丨 left leg of RIGHT compartment
  s6 横折 top+right of RIGHT compartment
  s7 short mark inside RIGHT compartment

All 4 joints are N-neighbors (do NOT weld).
"""
import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def draw_li(draw):
    # ---- s1: 一 top horizontal ----
    p1a = anchor_to_xy(('ML', 0.489, 0.081))
    p1b = anchor_to_xy(('TR', 0.534, 0.967))
    fat_line(draw, p1a, p1b, width=9)

    # ---- LEFT compartment ----
    # s2: left vertical
    p2a = anchor_to_xy(('ML', 0.642, 0.503))
    p2b = anchor_to_xy(('BL', 0.645, 0.83))
    fat_line(draw, p2a, p2b, width=8)

    # s3: heng-zhe (top + right leg), L-shape via bezier corner
    p3a = anchor_to_xy(('ML', 0.794, 0.538))
    p3b = anchor_to_xy(('BL', 0.92, 0.681))
    corner3 = (p3b[0], p3a[1])   # right, then down
    seg_a = [(p3a[0] + (corner3[0]-p3a[0]) * i/8,
              p3a[1] + (corner3[1]-p3a[1]) * i/8) for i in range(9)]
    seg_b = [(corner3[0] + (p3b[0]-corner3[0]) * i/20,
              corner3[1] + (p3b[1]-corner3[1]) * i/20) for i in range(21)]
    pts3 = seg_a + seg_b[1:]
    widths3 = [8] * len(pts3)
    stroke_variable_width(draw, pts3, widths3)

    # s4: short mark inside LEFT compartment (dot-like)
    p4a = anchor_to_xy(('ML', 0.823, 0.931))
    p4b = anchor_to_xy(('BC', 0.055, 0.133))
    fat_line(draw, p4a, p4b, width=7)

    # ---- RIGHT compartment ----
    # s5: left vertical of right compartment
    p5a = anchor_to_xy(('C', 0.564, 0.447))
    p5b = anchor_to_xy(('BC', 0.594, 0.892))
    fat_line(draw, p5a, p5b, width=8)

    # s6: heng-zhe (top + right leg) of right compartment
    p6a = anchor_to_xy(('C', 0.731, 0.482))
    p6b = anchor_to_xy(('BC', 0.939, 0.742))
    corner6 = (p6b[0], p6a[1])
    seg_a = [(p6a[0] + (corner6[0]-p6a[0]) * i/10,
              p6a[1] + (corner6[1]-p6a[1]) * i/10) for i in range(11)]
    seg_b = [(corner6[0] + (p6b[0]-corner6[0]) * i/20,
              corner6[1] + (p6b[1]-corner6[1]) * i/20) for i in range(21)]
    pts6 = seg_a + seg_b[1:]
    widths6 = [8] * len(pts6)
    stroke_variable_width(draw, pts6, widths6)

    # s7: short mark inside RIGHT compartment
    p7a = anchor_to_xy(('C', 0.74, 0.922))
    p7b = anchor_to_xy(('BR', 0.019, 0.162))
    fat_line(draw, p7a, p7b, width=7)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_li(draw)
    out = os.path.join(os.path.dirname(__file__), '01_丽.png')
    img.save(out)
    print('wrote', out)


SELF_CHECK = {
    'visual_ok': None,           # filled after render inspection
    'stroke_count_ok': True,     # 7 strokes drawn (s1..s7)
    'endpoint_mismatches': [],   # anchors used verbatim from MMH spec
    'joint_class_mismatches': [], # all four joints implemented as N (no welding)
    'overall_pass': None,
    'notes': 'inline 冂 twice; N-joints preserved by using distinct heads for s2/s3 and s5/s6.'
}

if __name__ == '__main__':
    main()
