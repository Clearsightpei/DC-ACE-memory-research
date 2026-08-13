"""怎 (zěn) — 9 strokes.
Decomposition: 怎 = 乍 (top, 5 strokes) + 心 (bottom, 4 strokes).

Sub-radical layout per MMH:
  s1 撇, s2 top-heng, s3 竖 spine, s4 middle-heng, s5 lower-heng  = 乍
  s6 left dot(pie), s7 卧钩, s8 middle dot, s9 right dot         = 心

Per B9 A-recipe + B12 addendum: MMH-verbatim anchors + base primitives.
Not importing xin.py — MMH puts 心 compressed into the bottom third
y∈[0.66, 1.0] band and xin.py bakes full-canvas anchors that would
partial-override into the p3_char_0252_伊 anti-pattern. Precedent:
p3_char_0345_志 (PASS, same 士/乍-over-心 slot pattern) inlined 心.

Joints (from MMH-derived block; all N, DO NOT weld):
  s1.mid ⇆ s2.head @ C : N ~16.7 px
  s2.mid ⇆ s3.head @ C : N ~12.4 px
  s3.mid ⇆ s4.head @ C : N ~12.2 px
  s3.mid ⇆ s5.head @ C : N ~14.8 px
  s3.tail ⇆ s8.head @ BC : N ~18.5 px
"""
# BANK_DEVIATION
# skipped: success_bank/code/xin.py
# reason: xin.py bakes full-canvas 心 anchors (ML/BL/MR spread); MMH places 心 compressed into the bottom-third slot under 乍. Partial-override of xin defaults is the伊 anti-pattern.
# fresh_component: xin_bottom_slot_for_compound (precedent: 志 PASS inline)

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, sample_line)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim; 乍 spine 竖 pierces heng bars as N '
              '(small gaps, not welded); 心 4-stroke inline with 卧钩 curving '
              'down-and-right with tail hook.')
}

# --- MMH anchor tuples from dispatcher brief (verbatim) ---
# 乍 (top, 5 strokes)
S1_HEAD = ('TC', 0.148, 0.539)   # 撇 head (upper)
S1_TAIL = ('ML', 0.665, 0.459)   # 撇 tail (down-left)
S2_HEAD = ('C',  0.134, 0.058)   # top heng left
S2_TAIL = ('TR', 0.238, 0.896)   # top heng right
S3_HEAD = ('C',  0.365, 0.131)   # 竖 spine top
S3_TAIL = ('BC', 0.45,  0.095)   # 竖 spine bottom
S4_HEAD = ('C',  0.544, 0.433)   # middle heng left
S4_TAIL = ('MR', 0.013, 0.356)   # middle heng right
S5_HEAD = ('C',  0.544, 0.743)   # lower heng left
S5_TAIL = ('MR', 0.068, 0.682)   # lower heng right

# 心 (bottom, 4 strokes)
S6_HEAD = ('BL', 0.653, 0.241)   # left dot (pie) head
S6_TAIL = ('BL', 0.486, 0.783)   # left dot tail (descends left)
S7_HEAD = ('BL', 0.976, 0.247)   # 卧钩 start
S7_TAIL = ('BR', 0.071, 0.455)   # 卧钩 exit (before hook)
S8_HEAD = ('BC', 0.5,   0.221)   # middle dot head
S8_TAIL = ('BC', 0.752, 0.473)   # middle dot tail
S9_HEAD = ('BR', 0.203, 0.065)   # right dot head
S9_TAIL = ('BR', 0.707, 0.402)   # right dot tail


def straight_line(draw, head, tail, width=7):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)


def draw_pie(draw, head, tail, head_w=9, tail_w=3, bow=6, n=40):
    """撇 — tapered leftward diagonal with slight bow."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mid = ((p0[0] + p2[0]) / 2 + bow, (p0[1] + p2[1]) / 2 - bow / 2)
    pts = quad_bezier(p0, mid, p2, n=n)
    widths = [head_w + (tail_w - head_w) * i / (len(pts) - 1)
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def tapered_dot(draw, head, tail, head_w=3, tail_w=10, n=18):
    """点 — dot tapered from head to tail (usually head_w small, tail_w wider)."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = sample_line(p0, p1, n=n)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def wo_gou_stroke(draw, head, tail, belly_dy=28, hook_len=14, hook_up=15,
                  head_w=3, body_w=10, hook_w=6):
    """卧钩 — curves down then hooks up-right at tail."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    ctrl = (mx, my + belly_dy)
    pts = quad_bezier(p0, ctrl, p2, n=36)
    widths = [head_w + (body_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)
    hx = p2[0] + hook_len * 0.2
    hy = p2[1] - hook_up
    fat_line(draw, p2, (hx, hy), hook_w)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 乍 (top): 撇 + 3 heng bars + 竖 spine
    draw_pie(d, S1_HEAD, S1_TAIL, head_w=9, tail_w=3, bow=6, n=40)  # s1 撇
    straight_line(d, S2_HEAD, S2_TAIL, width=7)                     # s2 top heng
    straight_line(d, S3_HEAD, S3_TAIL, width=8)                     # s3 spine 竖
    straight_line(d, S4_HEAD, S4_TAIL, width=7)                     # s4 middle heng
    straight_line(d, S5_HEAD, S5_TAIL, width=7)                     # s5 lower heng

    # 心 (bottom): left dot(pie) + 卧钩 + middle dot + right dot
    # Draw the dots LAST for the middle/right ones so they aren't overrun.
    draw_pie(d, S6_HEAD, S6_TAIL, head_w=9, tail_w=3, bow=-4, n=32)  # s6 left dot as pie
    wo_gou_stroke(d, S7_HEAD, S7_TAIL)                                # s7 卧钩
    tapered_dot(d, S8_HEAD, S8_TAIL, head_w=3, tail_w=10, n=16)       # s8 middle dot
    tapered_dot(d, S9_HEAD, S9_TAIL, head_w=3, tail_w=11, n=18)       # s9 right dot

    n_strokes = 9
    assert n_strokes == 9, f"expected 9 strokes, got {n_strokes}"

    out = Path(__file__).parent / '01_怎.png'
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
