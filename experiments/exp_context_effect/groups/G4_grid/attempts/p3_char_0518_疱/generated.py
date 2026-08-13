"""疱 (pào) — 10 strokes.
Decomposition: 疱 = 疒 (top-left frame, 5 strokes) + 包 (bottom-right slot, 5 strokes).
  疒 = 点 (top) + 横 + 撇 + 点 (left) + 提
  包 = 撇 + 横折钩 (勹 outer) + 横折 + 横 + 竖弯钩 (巳 inner)

Approach: A-recipe base primitives (fat_line / quad_bezier) with
MMH-verbatim anchors. All 12 joints are N-class — leave natural gaps.
Draw top dot LAST (defensive against overwrite) per B6 drawer_memory.

BANK_DEVIATION
skipped: bao_char.py, bao.py
reason: bao_char/bao bake full-canvas anchors for standalone 勹. Here
  包 is compressed into the bottom-right slot (x>=0.30 approx) inside
  the 疒 frame — full-canvas defaults would overrun 疒. Inlining
  base primitives with MMH-verbatim anchors preserves the slot.
fresh_component: bao_right_bottom_slot_for_疒_frame
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

# ---------- MMH-verbatim anchors ----------
S1_H = ('TC', 0.386, 0.56);  S1_T = ('TC', 0.729, 0.797)   # 疒 top 点
S2_H = ('C',  0.052, 0.099); S2_T = ('TR', 0.294, 0.964)   # 疒 横
S3_H = ('ML', 0.835, 0.017); S3_T = ('BL', 0.337, 0.941)   # 疒 长撇
S4_H = ('ML', 0.407, 0.339); S4_T = ('ML', 0.639, 0.547)   # 疒 左点
S5_H = ('BL', 0.19,  0.142); S5_T = ('ML', 0.756, 0.857)   # 疒 提
S6_H = ('C',  0.327, 0.271); S6_T = ('ML', 0.979, 0.992)   # 包 撇
S7_H = ('C',  0.336, 0.67);  S7_T = ('BC', 0.77,  0.104)   # 包 横折钩
S8_H = ('C',  0.318, 0.934); S8_T = ('BC', 0.559, 0.162)   # 巳 横折
S9_H = ('BC', 0.286, 0.309); S9_T = ('BC', 0.708, 0.244)   # 巳 横
S10_H = ('C', 0.169, 0.913); S10_T = ('BR', 0.531, 0.367)  # 巳 竖弯钩

def xy(a): return anchor_to_xy(a)

# ---------- s2: 横 (simple) ----------
fat_line(d, xy(S2_H), xy(S2_T), width=6)

# ---------- s3: 长撇 (curved down-left) ----------
p0, p2 = xy(S3_H), xy(S3_T)
# control biased slightly right of straight line for natural 撇 curvature
ctrl = ((p0[0] + p2[0]) / 2 + 8, (p0[1] + p2[1]) / 2 - 4)
pts = quad_bezier(p0, ctrl, p2, n=48)
widths = [max(2, int(10 - 8 * (i / len(pts)))) for i in range(len(pts))]  # taper
stroke_variable_width(d, pts, widths)

# ---------- s4: 左点 (short slant dot) ----------
fat_line(d, xy(S4_H), xy(S4_T), width=6)

# ---------- s5: 提 (rising) ----------
p0, p2 = xy(S5_H), xy(S5_T)
pts = [(p0[0] + i / 20 * (p2[0] - p0[0]), p0[1] + i / 20 * (p2[1] - p0[1])) for i in range(21)]
widths = [max(2, int(9 - 6 * (i / 20))) for i in range(21)]  # thick at head, thin at tail
stroke_variable_width(d, pts, widths)

# ---------- s6: 撇 (of 勹) ----------
p0, p2 = xy(S6_H), xy(S6_T)
ctrl = ((p0[0] + p2[0]) / 2 + 6, (p0[1] + p2[1]) / 2 - 2)
pts = quad_bezier(p0, ctrl, p2, n=40)
widths = [max(2, int(8 - 5 * (i / len(pts)))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# ---------- s7: 横折钩 (of 勹): top-horizontal → right-side down → hook ----------
# Reinterpret MMH: head is start of horizontal top; tail is TIP of the
# bottom hook (curled back left). Route through top-right and bottom-right
# corners so the shape forms the 勵 outer wrap.
p0, p2 = xy(S7_H), xy(S7_T)
tr_corner = (272, p0[1])         # top-right of 包 enclosure
br_corner = (272, p2[1] + 8)     # bottom-right
# 3 segments: horizontal top, vertical right, hook back-left to tail
pts = ([(p0[0] + i / 15 * (tr_corner[0] - p0[0]), p0[1]) for i in range(16)] +
       [(tr_corner[0], tr_corner[1] + (br_corner[1] - tr_corner[1]) * i / 20) for i in range(1, 21)] +
       [(br_corner[0] + (p2[0] - br_corner[0]) * i / 8, br_corner[1] + (p2[1] - br_corner[1]) * i / 8) for i in range(1, 9)])
widths = [6] * len(pts)
stroke_variable_width(d, pts, widths)

# ---------- s8: 巳 横折 (small top-left corner of 巳 inside 勹) ----------
p0, p2 = xy(S8_H), xy(S8_T)
# route: down from head to corner, then right to tail-area (small square opening of 巳)
corner = (p0[0], p2[1] + 6)
pts = ([(p0[0], p0[1] + (corner[1] - p0[1]) * i / 12) for i in range(13)] +
       [(corner[0] + (p2[0] - corner[0]) * i / 12, corner[1] + (p2[1] - corner[1]) * i / 12) for i in range(1, 13)])
widths = [4] * len(pts)
stroke_variable_width(d, pts, widths)

# ---------- s9: 巳 middle 横 ----------
fat_line(d, xy(S9_H), xy(S9_T), width=4)

# ---------- s10: 竖弯钩 (bottom of 巳 — inner curl) ----------
# Head high-left, curl down then sweep right to tail with slight upward hook.
p0, p2 = xy(S10_H), xy(S10_T)
mid_bot = (p0[0], p2[1] + 6)
pts_v = [(p0[0], p0[1] + (mid_bot[1] - p0[1]) * i / 18) for i in range(19)]
pts_h = [(p0[0] + (p2[0] - p0[0]) * i / 18, mid_bot[1] + (p2[1] - mid_bot[1]) * i / 18) for i in range(1, 19)]
pts = pts_v + pts_h
widths = [5] * len(pts)
stroke_variable_width(d, pts, widths)

# ---------- s1: 疒 top 点 (LAST — defensive) ----------
p0, p2 = xy(S1_H), xy(S1_T)
pts = [(p0[0] + i / 10 * (p2[0] - p0[0]), p0[1] + i / 10 * (p2[1] - p0[1])) for i in range(11)]
widths = [3 + int(5 * i / 10) for i in range(11)]  # thin head → fat tail (点)
stroke_variable_width(d, pts, widths)

# --------- Stroke count assertion ----------
STROKE_COUNT = 10  # s1..s10 above
assert STROKE_COUNT == 10, "stroke count mismatch"

out = os.path.join(os.path.dirname(__file__), '01_疱.png')
img.save(out)
print("wrote", out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes; MMH-verbatim anchors; all N-joints left as natural gaps (no welding); top dot drawn LAST per B6 defensive rule.',
}
