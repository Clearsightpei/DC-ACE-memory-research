"""痄 (zhà) — 10 strokes.
Decomposition: 痄 = 疒 (top-left 5-stroke frame) + 乍 (bottom-right 5 strokes).

Reading trail (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — 疒 named pattern `ne_sick_top_left_frame_for_*`
     (B13 codified). 5-stroke frame inline, MMH-verbatim, dot LAST.
     Interior sub-radical fills bottom-right slot.
  2. success_bank/INDEX.md grep — no primitive for 乍 nor for 疒;
     inline via base primitives.
  3. errata.md grep — no prior 痄 entry.

Applying B9-B13 A-recipe:
  - Explicit decomposition (this docstring).
  - MMH-verbatim anchors (dispatcher-injected block; all 10 tuples used
    unchanged).
  - SELF_CHECK block.
  - Base primitives only (fat_line + stroke_variable_width via _anchor).
  - N-joint discipline: leave natural gaps (all 8 joints are N-class).
  - 疒 top dot (s1) rendered LAST defensively (per B6/B13 rule).
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 draw calls, matches MMH
    'endpoint_mismatches': [],  # all MMH-verbatim
    'joint_class_mismatches': [],  # all 8 joints implemented as N (natural gap)
    'overall_pass': True,
    'notes': ('10 strokes MMH-verbatim; 疒 top dot drawn LAST defensively; '
              'all 8 N-joints left as natural gaps (no welds).'),
}


# ---- MMH-verbatim anchor tuples (dispatcher block) ----
S1_H = ('TC', 0.491, 0.557); S1_T = ('TC', 0.816, 0.776)   # 疒 top 点
S2_H = ('C',  0.104, 0.063); S2_T = ('TR', 0.329, 0.943)   # 疒 top 一
S3_H = ('TL', 0.873, 0.987); S3_T = ('BL', 0.457, 0.854)   # 疒 long 撇
S4_H = ('ML', 0.466, 0.292); S4_T = ('ML', 0.688, 0.497)   # 疒 inner 点
S5_H = ('BL', 0.214, 0.139); S5_T = ('ML', 0.82,  0.819)   # 疒 inner 提

S6_H  = ('C',  0.327, 0.321); S6_T  = ('BC', 0.069, 0.095) # 乍 top 撇
S7_H  = ('C',  0.433, 0.67 ); S7_T  = ('MR', 0.394, 0.509) # 乍 upper 一
S8_H  = ('C',  0.644, 0.714); S8_T  = ('BC', 0.74,  1.076) # 乍 long 竖
S9_H  = ('BC', 0.813, 0.098); S9_T  = ('MR', 0.312, 0.983) # 乍 middle 一
S10_H = ('BC', 0.816, 0.473); S10_T = ('BR', 0.367, 0.367) # 乍 bottom 一


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


def draw_dot(draw, ah, at, head_w=5, tail_w=10, segs=20):
    """Short tapered dot / 点 — thickens toward tail."""
    p0 = anchor_to_xy(ah)
    p1 = anchor_to_xy(at)
    pts = [(p0[0] + i / segs * (p1[0] - p0[0]),
            p0[1] + i / segs * (p1[1] - p0[1])) for i in range(segs + 1)]
    widths = [head_w + (tail_w - head_w) * (i / segs) for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_ti(draw, ah, at, head_w=9, tail_w=1, segs=30):
    """提 — rising stroke, thick base to thin flick."""
    p0 = anchor_to_xy(ah)
    p1 = anchor_to_xy(at)
    pts = [(p0[0] + i / segs * (p1[0] - p0[0]),
            p0[1] + i / segs * (p1[1] - p0[1])) for i in range(segs + 1)]
    widths = [head_w + (tail_w - head_w) * (i / segs) for i in range(segs + 1)]
    stroke_variable_width(draw, pts, widths)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 疒 frame (draw s2..s5 first, s1 dot LAST) ----
    # s2 — top heng 一
    fat_line(d, anchor_to_xy(S2_H), anchor_to_xy(S2_T), width=6)
    # s3 — long pie 撇 (main tapered left-sweep)
    draw_pie_stroke(d, S3_H, S3_T, head_w=11, tail_w=1, curve=0.08, segs=48)
    # s4 — inner short 点 (small, slanting down-right)
    draw_dot(d, S4_H, S4_T, head_w=4, tail_w=8, segs=16)
    # s5 — inner 提 (rising)
    draw_ti(d, S5_H, S5_T, head_w=8, tail_w=1, segs=30)

    # ---- 乍 body (5 strokes 6..10) ----
    # s6 — top 撇 short
    draw_pie_stroke(d, S6_H, S6_T, head_w=8, tail_w=1, curve=0.05, segs=32)
    # s7 — upper 一 short heng
    fat_line(d, anchor_to_xy(S7_H), anchor_to_xy(S7_T), width=5)
    # s8 — long 竖 (vertical, uniform)
    fat_line(d, anchor_to_xy(S8_H), anchor_to_xy(S8_T), width=7)
    # s9 — middle 一
    fat_line(d, anchor_to_xy(S9_H), anchor_to_xy(S9_T), width=5)
    # s10 — bottom 一
    fat_line(d, anchor_to_xy(S10_H), anchor_to_xy(S10_T), width=5)

    # ---- s1 疒 top dot LAST (defensive per B6 rule) ----
    draw_dot(d, S1_H, S1_T, head_w=4, tail_w=8, segs=16)

    out = os.path.join(os.path.dirname(__file__), '01_痄.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    render()
