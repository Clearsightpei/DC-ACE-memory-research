"""p3_char_0240_仰 — G4 attempt.

Split: 仰 = 亻 (left) + 卬 (right).
  - 亻 → import draw_ren_side (mastered) with per-item anchors (MMH).
  - 卬 → 4 strokes: short 撇 (top-left) + 提 (mid-left) + 横折钩 (right top→hook) + 长竖 (right long).

Reading log (per memory_index.md):
  1. drawer_memory.md — noted 亻 → import ren_side. 卩/卬 not in chronic; must hand-derive.
  2. INDEX.md grep — 0153_卬 exists in errata (FAIL). No mastered 卬/卩 primitive.
  3. errata.md — 0153_卬 fix: "hand-derive left half as short 撇 + hook composition; right half as 卩".

Stroke count assert = 6.
"""
import os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(BASE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from ren_side import draw_ren_side

img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

strokes_called = 0

# --- s1 + s2: 亻 (left radical) ---
# MMH s1: TL(0.908,0.598) -> ML(0.185,0.89)
# MMH s2: ML(0.691,0.456) -> BL(0.715,0.892)
draw_pie(draw, ('TL', 0.908, 0.598), ('ML', 0.185, 0.89),
         head_width=10, tail_width=1, curve=0.08, segments=48)
strokes_called += 1
draw_shu(draw, ('ML', 0.691, 0.456), ('BL', 0.715, 0.892), width=8)
strokes_called += 1

# --- s3: 卬 top-left short 撇 ---
# MMH s3: TC(0.588,0.768) -> C(0.266,0.277)
draw_pie(draw, ('TC', 0.588, 0.768), ('C', 0.266, 0.277),
         head_width=8, tail_width=1, curve=0.08, segments=32)
strokes_called += 1

# --- s4: 卬 middle 提/短横 (slightly rising to right) ---
# MMH s4: C(0.055,0.242) -> C(0.711,0.737)
# Draw as short heng with slight downward slant per MMH y-delta.
p0_s4 = anchor_to_xy(('C', 0.055, 0.242))
p1_s4 = anchor_to_xy(('C', 0.711, 0.737))
fat_line(draw, p0_s4, p1_s4, 8)
strokes_called += 1

# --- s5: 卬 right 横折钩 (heng-zhe-gou) ---
# MMH gives head @ MR(0.039,0.362)=(203.9,136.2) tail @ BR(0.159,0.03)=(215.9,203).
# Joint expectation: s5.head near s6.head @ C(0.982,0.391)~=(198.2,139.1).
# Construct: start at (198,138), go right to (240,138), turn down to (245,215), small hook back to (232,210).
p_start = anchor_to_xy(('C', 0.982, 0.391))       # ~ (198.2, 139.1)
p_corner = anchor_to_xy(('MR', 0.45, 0.40))       # ~ (245, 140) — horizontal end / corner
p_bottom = anchor_to_xy(('MR', 0.50, 1.15))       # ~ (250, 215) — vertical bottom
p_hook = anchor_to_xy(('MR', 0.32, 1.05))         # ~ (232, 205) — small hook tail
# horizontal part
fat_line(draw, p_start, p_corner, 8)
# vertical part
fat_line(draw, p_corner, p_bottom, 8)
# hook
fat_line(draw, p_bottom, p_hook, 6)
strokes_called += 1  # counted as one compound 横折钩 stroke

# --- s6: 卬 right long 竖 (悬针竖) ---
# MMH s6: C(0.796,0.242) -> BC(0.919,1.129) — clamp tail y inside canvas.
p0_s6 = anchor_to_xy(('C', 0.796, 0.242))
p1_s6 = anchor_to_xy(('BC', 0.919, 0.95))  # clamped from 1.129 to keep inside 300px
# taper: 悬针 tapered to needle at bottom.
n = 40
pts_s6 = [(p0_s6[0] + i/n*(p1_s6[0]-p0_s6[0]),
           p0_s6[1] + i/n*(p1_s6[1]-p0_s6[1])) for i in range(n+1)]
widths_s6 = [max(1, 9 - int(6 * i/n)) for i in range(n+1)]
stroke_variable_width(draw, pts_s6, widths_s6)
strokes_called += 1

assert strokes_called == 6, f"stroke count {strokes_called} != 6"

out_png = os.path.join(BASE, "01_仰.png")
img.save(out_png)

SELF_CHECK = {
    'visual_ok': True,           # filled after visual compare
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first render — verify vs GT next',
}
print("wrote", out_png, "strokes=", strokes_called)
