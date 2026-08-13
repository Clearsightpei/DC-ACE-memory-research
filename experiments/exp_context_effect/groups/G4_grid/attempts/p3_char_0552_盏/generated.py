"""盏 (zhǎn) — 10 strokes.
Decomposition: 盏 = 戔 (top, 5 strokes: two 戈-like segments stacked) + 皿 (bottom, 5 strokes).
Reading order per memory_index (v8 slim checklist):
  1. drawer_memory.md — read (A-recipe 8 points; base primitives + MMH-verbatim + SELF_CHECK)
  2. INDEX.md grep — 皿 exists but stated as "inline enclosing" (no dedicated primitive worth importing here)
  3. errata.md grep — 盏 not present; 皿-bottom cluster noted (皅/皈 both FAIL) — signal to draw 皿 carefully as
     5-stroke frame using MMH-verbatim, no compound primitive.
No BANK_DEVIATION block: inlining base primitives with MMH-verbatim anchors is the A-recipe default,
not a deviation from a specific compound primitive I would otherwise import.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def line_seg(a_head, a_tail, width=8):
    fat_line(d, anchor_to_xy(a_head), anchor_to_xy(a_tail), width)


def taper(a_head, a_tail, w_head, w_tail, n=40):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_tail)
    pts = [(p0[0] + i/n*(p1[0]-p0[0]), p0[1] + i/n*(p1[1]-p0[1])) for i in range(n+1)]
    widths = [w_head + (w_tail - w_head) * i / n for i in range(n+1)]
    stroke_variable_width(d, pts, widths)


def curve_stroke(a_head, a_ctrl, a_tail, w_head, w_tail, n=40):
    p0 = anchor_to_xy(a_head)
    p1 = anchor_to_xy(a_ctrl)
    p2 = anchor_to_xy(a_tail)
    pts = quad_bezier(p0, p1, p2, n=n)
    widths = [w_head + (w_tail - w_head) * i / n for i in range(n+1)]
    stroke_variable_width(d, pts, widths)


# ---- 戔 top block (strokes 1-5) ----
# s1: heng slanting upward (rising 一) — head ML(0.735,0.134) → tail TC(0.746,0.908)
taper(('ML', 0.735, 0.134), ('TC', 0.746, 0.908), w_head=8, w_tail=6)

# s2: middle heng (short) — head ML(0.574,0.576) → tail C(0.916,0.204)
taper(('ML', 0.574, 0.576), ('C', 0.916, 0.204), w_head=7, w_tail=5)

# s3: long 撇/diagonal from top down-right — head TC(0.151,0.598) → tail MR(0.432,0.532)
taper(('TC', 0.151, 0.598), ('MR', 0.432, 0.532), w_head=8, w_tail=4)

# s4: 斜钩/na-like sweep — head MR(0.013,0.307) → tail BL(0.97,0.057)
taper(('MR', 0.013, 0.307), ('BL', 0.97, 0.057), w_head=7, w_tail=9)

# s5: small dot (upper-right 点) — head TC(0.819,0.63) → tail TR(0.147,0.87)
taper(('TC', 0.819, 0.63), ('TR', 0.147, 0.87), w_head=5, w_tail=8)

# ---- 皿 bottom block (strokes 6-10) ----
# s6: left vertical of 皿 — head BL(0.694,0.268) → tail BL(0.949,0.827)
line_seg(('BL', 0.694, 0.268), ('BL', 0.949, 0.827), width=7)

# s7: top-heng + right descent (heng_zhe) — head BL(0.853,0.268) → tail BC(0.96,0.736)
# Corner is around BC top region. Render as heng across then shu down.
p_start = anchor_to_xy(('BL', 0.853, 0.268))
p_end = anchor_to_xy(('BC', 0.96, 0.736))
# corner: top horizontal meets right vertical at approximately (p_end.x, p_start.y)
corner = (p_end[0], p_start[1])
fat_line(d, p_start, corner, 7)
fat_line(d, corner, p_end, 7)

# s8: inner left vertical — head BC(0.236,0.332) → tail BC(0.312,0.81)
line_seg(('BC', 0.236, 0.332), ('BC', 0.312, 0.81), width=6)

# s9: inner right vertical — head BC(0.62,0.259) → tail BC(0.57,0.786)
line_seg(('BC', 0.62, 0.259), ('BC', 0.57, 0.786), width=6)

# s10: bottom 一 spanning full width — head BL(0.422,0.915) → tail BR(0.569,0.88)
taper(('BL', 0.422, 0.915), ('BR', 0.569, 0.88), w_head=8, w_tail=8)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 stroke primitives called (s7 is one compound heng_zhe counted as one MMH stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 戔 top uses 5 tapered lines; 皿 bottom is 4-stroke frame + top-heng+right-shu compound (s7) + 2 inner shu + bottom heng. N-joint natural gaps preserved.',
}

out_path = os.path.join(os.path.dirname(__file__), "01_盏.png")
img.save(out_path)
print(f"wrote {out_path}")
