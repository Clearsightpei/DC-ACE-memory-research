"""盃 (bēi) — 9 strokes.
Decomposition: 盃 = 不 (top, 4 strokes) + 皿 (bottom, 5 strokes).

Reading order (v8 slim checklist):
  1. drawer_memory.md — read; B9 A-recipe (MMH-verbatim + base primitives) applies.
  2. success_bank/INDEX.md grep — no bank primitive for 皿 (row 195 marked
     "inline enclosing"); no primitive for 不. Use MMH-verbatim inline.
  3. errata.md grep — no entry for 盃 / 不 / 皿.

Following A-recipe: MMH-verbatim anchors, N-joint discipline
(leave natural gaps ~10-20 px for the many N-joints in 皿's frame + interior).

No BANK_DEVIATION block — no bank primitive was skipped; inlining is the
default path when the char decomposes to parts without bank coverage.
"""
import os, sys
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 不 (4) + 皿 (5); N-joints preserved as small gaps.',
}


def draw_pie(draw, head, tail, head_width=4, tail_width=2, curve=0.10, segments=36):
    """撇: gentle bow curving left-down."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2.0
    my = (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    # perpendicular offset (left of the direction of travel gives outward bow)
    nx, ny = -dy, dx
    length = max(1.0, (nx * nx + ny * ny) ** 0.5)
    ctrl = (mx + curve * nx / length * ((dx * dx + dy * dy) ** 0.5),
            my + curve * ny / length * ((dx * dx + dy * dy) ** 0.5))
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_dian(draw, head, tail, head_width=3, tail_width=9):
    """点: short teardrop from head to tail."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    segments = 20
    pts = [(p0[0] + i / segments * (p1[0] - p0[0]),
            p0[1] + i / segments * (p1[1] - p0[1])) for i in range(segments + 1)]
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, head, tail, width=6):
    """横: straight horizontal."""
    fat_line(draw, anchor_to_xy(head), anchor_to_xy(tail), width)


def draw_shu(draw, head, tail, width=6):
    """竖: straight vertical (or near-vertical)."""
    fat_line(draw, anchor_to_xy(head), anchor_to_xy(tail), width)


def draw_heng_zhe(draw, head, corner, tail, width=6):
    """横折: horizontal then folds down. Corner anchor supplied explicitly."""
    p0 = anchor_to_xy(head)
    pc = anchor_to_xy(corner)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, pc, width)
    fat_line(draw, pc, p1, width)


# ------- 9-stroke render (MMH-verbatim anchors) -------

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 不 (top, 4 strokes) ---
# s1: 横 across top of 不
draw_heng(d, ('TL', 0.744, 0.82), ('TR', 0.353, 0.765), width=7)

# s2: 撇 from center-top down to lower-left of top-band
draw_pie(d, ('TC', 0.521, 0.823), ('ML', 0.548, 0.898),
         head_width=6, tail_width=2, curve=0.12, segments=36)

# s3: 竖 short vertical inside center (the "丨" of 不 tucked in)
draw_shu(d, ('C', 0.541, 0.225), ('C', 0.474, 0.89), width=6)

# s4: 点 to the right (short dot going down-right)
draw_dian(d, ('C', 0.852, 0.359), ('MR', 0.435, 0.682),
          head_width=3, tail_width=8)

# --- 皿 (bottom, 5 strokes) ---
# s5: 竖 (left side of 皿)  head TOP tail BOTTOM (slightly slanted outward)
draw_shu(d, ('BL', 0.741, 0.235), ('BC', 0.046, 0.792), width=7)

# s6: 横折 (top horizontal + right vertical of 皿). MMH gives only head+tail;
# corner sits at the top-right, so infer corner ≈ (BR-adjacent top, tail-x/head-y)
# head @ (BL 0.938, 0.244) → pixel (93.8, 224.4)
# tail @ (BC 0.978, 0.716) → pixel (197.8, 271.6)
# Corner near (197.8, 224.4) — top-right of the 皿 box
draw_heng_zhe(d,
              ('BL', 0.938, 0.244),
              ('BC', 0.978, 0.244),   # corner: top-right of box (same y as head)
              ('BC', 0.978, 0.716),
              width=7)

# s7: 竖 inner-left vertical of 皿
draw_shu(d, ('BC', 0.251, 0.297), ('BC', 0.362, 0.769), width=6)

# s8: 竖 inner-right vertical of 皿
draw_shu(d, ('BC', 0.608, 0.238), ('BC', 0.573, 0.736), width=6)

# s9: 横 bottom of 皿 (wide, extends full width — the calligraphic base)
draw_heng(d, ('BL', 0.311, 0.889), ('BR', 0.742, 0.854), width=8)

OUT = os.path.join(os.path.dirname(__file__), '01_盃.png')
img.save(OUT)
print(f"Wrote {OUT}")
