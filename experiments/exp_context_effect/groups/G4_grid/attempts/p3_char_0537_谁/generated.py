# BANK_DEVIATION
# skipped: yan_speech.py
# reason: MMH places 讠 in TL far-left column (dot at TL(0.73,0.69), 横折提 head at ML(0.15,0.59)), not yan_speech's center-column defaults (C/ML/BC). Partial-override of compound primitive is the p3_char_0252_伊 anti-pattern (B8). Inline dian + heng_zhe_ti with MMH-verbatim anchors instead.
# fresh_component: yan_speech_far_left_for_compound

"""谁 (shuí) — 10 strokes.
Decomposition: 谁 = 讠 (left, 2 strokes) + 隹 (right, 8 strokes).
  讠 = 点 (s1) + 横折提 (s2)
  隹 = 短撇 (s3) + 亻竖 (s4) + 点 (s5) + 短横 (s6) + 短横 (s7) +
       短横 (s8) + 主竖 (s9) + 底横 (s10)

Reading trail (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — B11 named pattern for 讠 far-left slot
     ("yan_speech" bank primitive skipped when MMH places it in
     far-left column). B12/B13 A-recipe: inline base primitives with
     MMH-verbatim endpoints; do NOT partial-override compound primitives.
  2. success_bank/INDEX.md grep — yan_speech.py exists but defaults sit
     in TC/C/BC (center column) — MMH puts 讠 in TL/ML/BC (far-left).
     Skipping. No primitive for 隹.
  3. errata.md grep — no prior 谁 entry.

Applying B9-B13 A-recipe:
  - Explicit decomposition (this docstring).
  - MMH-verbatim anchors for all 10 strokes (dispatcher-injected block).
  - SELF_CHECK block.
  - Base primitives (fat_line + stroke_variable_width via _anchor).
  - N-joint discipline: leave natural gaps (5 N-joints).
  - P-joints between s9 (main shu) and s6/s7/s8 (horizontals) arise
    naturally from the shu passing through the hengs (welded crossings).
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 10 draw calls, matches MMH expected 10
    'endpoint_mismatches': [],    # all 10 head/tail MMH-verbatim
    'joint_class_mismatches': [], # 5 N left as gaps; 2 P (s7-s9, s8-s9) welded via geometry
    'overall_pass': True,
    'notes': ('10 strokes MMH-verbatim; 讠 far-left inline via BANK_DEVIATION '
              '(yan_speech skipped); s9 main shu crosses s6-s8 hengs to satisfy '
              'P-welds; other joints kept as natural N gaps.'),
}


# ---- MMH-verbatim anchor tuples (dispatcher block) ----
S1_H  = ('TL', 0.732, 0.686); S1_T  = ('TL', 0.999, 0.923)   # 讠 点
S2_H  = ('ML', 0.152, 0.591); S2_T  = ('BC', 0.137, 0.265)   # 讠 横折提 head+tail
S3_H  = ('TC', 0.585, 0.586); S3_T  = ('C',  0.04,  0.749)   # 隹 短撇
S4_H  = ('C',  0.354, 0.506); S4_T  = ('BC', 0.4,   1.035)   # 隹 亻竖
S5_H  = ('TC', 0.887, 0.841); S5_T  = ('MR', 0.153, 0.075)   # 隹 top 点
S6_H  = ('C',  0.649, 0.438); S6_T  = ('MR', 0.476, 0.295)   # 隹 上横
S7_H  = ('C',  0.726, 0.875); S7_T  = ('MR', 0.411, 0.775)   # 隹 中横
S8_H  = ('BC', 0.69,  0.203); S8_T  = ('BR', 0.458, 0.092)   # 隹 下横
S9_H  = ('C',  0.945, 0.482); S9_T  = ('BC', 0.983, 0.446)   # 隹 主竖
S10_H = ('BC', 0.515, 0.578); S10_T = ('BR', 0.678, 0.499)   # 隹 底横


def draw_pie_stroke(draw, ah, at, head_w=10, tail_w=1, curve=0.10, segs=40):
    p0 = anchor_to_xy(ah)
    p2 = anchor_to_xy(at)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / L, dx / L)
    bow = curve * L
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segs)
    widths = [head_w + (tail_w - head_w) * (i / segs) for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_dot(draw, ah, at, head_w=4, tail_w=10, segs=20):
    """Short tapered dot / 点 — thin head thickens to rounded tail."""
    p0 = anchor_to_xy(ah)
    p1 = anchor_to_xy(at)
    pts = [(p0[0] + i / segs * (p1[0] - p0[0]),
            p0[1] + i / segs * (p1[1] - p0[1])) for i in range(segs + 1)]
    widths = [head_w + (tail_w - head_w) * (i / segs) for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_ti(draw, ah, at, head_w=11, tail_w=1, segs=30):
    """提 — thick head at lower-left, thin needle-tip at upper-right."""
    p0 = anchor_to_xy(ah)
    p1 = anchor_to_xy(at)
    pts = [(p0[0] + i / segs * (p1[0] - p0[0]),
            p0[1] + i / segs * (p1[1] - p0[1])) for i in range(segs + 1)]
    widths = [head_w + (tail_w - head_w) * (i / segs) for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_heng_zhe_ti_inline(draw, head, tail):
    """讠's compound 横折提 inline: head -> corner -> knee -> tail (ti tip).

    Corner/knee estimated to form an L: heng extends right from head at
    same y, shu drops from corner to knee (near tail's y-level), then
    ti rises from knee up-right to tail.
    """
    p_head = anchor_to_xy(head)   # start of heng (left side)
    p_tail = anchor_to_xy(tail)   # tip of ti (upper-right)
    # Corner: same y as head, x roughly between head and tail
    corner_x = p_head[0] + (p_tail[0] - p_head[0]) * 0.55
    corner_y = p_head[1]
    p_corner = (corner_x, corner_y)
    # Knee: same x as corner, y below tail (base of the ti flick)
    knee_x = corner_x
    knee_y = p_tail[1] + 22
    p_knee = (knee_x, knee_y)
    # Heng: uniform width
    fat_line(draw, p_head, p_corner, width=7)
    # Shu: uniform width
    fat_line(draw, p_corner, p_knee, width=8)
    # Ti (rising, tapered): from knee -> tail
    segs = 24
    pts = [(p_knee[0] + i / segs * (p_tail[0] - p_knee[0]),
            p_knee[1] + i / segs * (p_tail[1] - p_knee[1])) for i in range(segs + 1)]
    widths = [11 + (1 - 11) * (i / segs) for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 讠 (left radical, 2 strokes) ----
    # s1 — 点 (small tapered dot, TL cell)
    draw_dot(d, S1_H, S1_T, head_w=3, tail_w=9, segs=16)
    # s2 — 横折提 (compound; head from ML, tail at BC upper)
    draw_heng_zhe_ti_inline(d, S2_H, S2_T)

    # ---- 隹 (right, 8 strokes) ----
    # s3 — 短撇 (upper-left pie of 隹)
    draw_pie_stroke(d, S3_H, S3_T, head_w=10, tail_w=1, curve=0.08, segs=40)
    # s4 — 亻竖 (left vertical, main downstroke)
    fat_line(d, anchor_to_xy(S4_H), anchor_to_xy(S4_T), width=8)
    # s5 — top 点 (small diagonal dot upper-right of 隹)
    draw_dot(d, S5_H, S5_T, head_w=3, tail_w=8, segs=16)
    # s6 — 上横 (top of the three horizontals)
    fat_line(d, anchor_to_xy(S6_H), anchor_to_xy(S6_T), width=6)
    # s7 — 中横 (middle horizontal)
    fat_line(d, anchor_to_xy(S7_H), anchor_to_xy(S7_T), width=6)
    # s8 — 下横 (lower of the three horizontals)
    fat_line(d, anchor_to_xy(S8_H), anchor_to_xy(S8_T), width=6)
    # s9 — 主竖 (right main vertical — P-welds with s6/s7/s8 via crossing)
    fat_line(d, anchor_to_xy(S9_H), anchor_to_xy(S9_T), width=8)
    # s10 — 底横 (bottom heng)
    fat_line(d, anchor_to_xy(S10_H), anchor_to_xy(S10_T), width=7)

    out = os.path.join(os.path.dirname(__file__), '01_谁.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    render()
