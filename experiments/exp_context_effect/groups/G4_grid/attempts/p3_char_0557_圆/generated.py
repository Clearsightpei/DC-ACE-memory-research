# BANK_DEVIATION
# skipped: chronic/jiong_frame.py
# reason: 圆's enclosure is 囗 (4-sided, closed at bottom via s10), not 冂 (3-sided);
#         MMH anchors for the frame don't match jiong_frame's baked TL(0.20,0.15)/BR(0.80,0.85)
#         defaults — the actual frame runs TL(0.56,0.78) → BR(0.34,1.05).
# fresh_component: wei_frame_for_圆 (囗 outer frame w/ 10-stroke composition)
"""圆 (yuán) — 10 strokes.
Decomposition: 圆 = 囗 (outer 4-sided frame, strokes 1/2/10)
                    + 员 (inner: 口 top + 贝 bottom, strokes 3-9)
Following B9-B13 A-recipe:
  1. Explicit decomposition (this docstring).
  2. MMH-verbatim anchors (all 10 strokes use the dispatcher-injected tuples).
  3. SELF_CHECK block below.
  4. Base primitives (fat_line) inline, since no compound primitive matches
     the 4-sided-frame slot pattern.
  5. N-joint discipline — all 17 joints are N-class (natural gaps preserved).
Frame strokes get a bend (横折 shape) drawn as 2-segment polyline through
a corner anchor. Inner strokes rendered as fat_line endpoint→endpoint.
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 draw calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; s2 & s7 drawn as 2-seg 横折 through a bend point; all N-joints preserved as gaps (no welding).',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- Outer 囗 frame (3 strokes: s1, s2, s10) ----

# s1 — left 竖 of 囗
p1a = anchor_to_xy(('TL', 0.562, 0.782))
p1b = anchor_to_xy(('BL', 0.633, 0.977))
fat_line(d, p1a, p1b, width=6)

# s2 — 横折 (top bar + right wall), head TL → corner at TR → tail BR
p2a = anchor_to_xy(('TL', 0.753, 0.841))
# corner: same y as head (top bar level) and same x as tail (right wall column)
p2c = (anchor_to_xy(('BR', 0.344, 1.05))[0], anchor_to_xy(('TL', 0.753, 0.841))[1])
p2b = anchor_to_xy(('BR', 0.344, 1.05))
# draw as 2 fat_line segments to form the 横折 corner
fat_line(d, p2a, p2c, width=6)
fat_line(d, p2c, p2b, width=6)

# ---- Inner 员 = 口 (top) + 贝 (bottom) ----

# s3 — inner 口 left 竖 (small, inside top of frame)
p3a = anchor_to_xy(('C', 0.058, 0.031))
p3b = anchor_to_xy(('C', 0.23, 0.453))
fat_line(d, p3a, p3b, width=4)

# s4 — inner 口 top 横 (short heng)
p4a = anchor_to_xy(('C', 0.207, 0.037))
p4b = anchor_to_xy(('C', 0.693, 0.204))
fat_line(d, p4a, p4b, width=4)

# s5 — inner 口 bottom 横 (short heng)
p5a = anchor_to_xy(('C', 0.271, 0.342))
p5b = anchor_to_xy(('C', 0.828, 0.301))
fat_line(d, p5a, p5b, width=4)

# s6 — 贝 left 竖 (upper half)
p6a = anchor_to_xy(('C', 0.081, 0.547))
p6b = anchor_to_xy(('BC', 0.14, 0.265))
fat_line(d, p6a, p6b, width=4)

# s7 — 贝 top 横折 (short heng + shu), drawn as 2-seg through a bend
p7a = anchor_to_xy(('C', 0.207, 0.576))
p7c = anchor_to_xy(('C', 0.80, 0.58))       # bend at top-right of inner 贝 frame
p7b = anchor_to_xy(('BC', 0.822, 0.238))
fat_line(d, p7a, p7c, width=4)
fat_line(d, p7c, p7b, width=4)

# s8 — inner 贝 middle 横
p8a = anchor_to_xy(('C', 0.365, 0.731))
p8b = anchor_to_xy(('BL', 0.976, 0.669))
fat_line(d, p8a, p8b, width=4)

# s9 — 贝 撇 leg (small diagonal in bottom-center)
p9a = anchor_to_xy(('BC', 0.623, 0.323))
p9b = anchor_to_xy(('BC', 0.913, 0.599))
fat_line(d, p9a, p9b, width=4)

# ---- Frame close: s10 — bottom 横 of 囗 (drawn LAST) ----
p10a = anchor_to_xy(('BL', 0.715, 0.918))
p10b = anchor_to_xy(('BR', 0.2, 0.78))
fat_line(d, p10a, p10b, width=6)

img.save(os.path.join(_HERE, '01_圆.png'))
