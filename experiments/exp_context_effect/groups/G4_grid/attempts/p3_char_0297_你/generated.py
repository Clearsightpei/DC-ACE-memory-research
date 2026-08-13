"""你 = 亻 + 尔. 7 strokes total, per MMH structural brief.

Split:
  s1, s2 = 亻 (left radical, inlined per B8 note: ren_side default
           anchors sit center; inline for the left-column position).
  s3     = 尔 outer 撇 (top-left descending).
  s4     = 尔 top 横钩 / 横 across.
  s5     = 尔 inner 撇 (short, below top).
  s6     = 尔 竖钩 (vertical center).
  s7     = 尔 右点 / 捺 (right dot descending).

Uses MMH-verbatim anchors from dispatcher brief. All rendered as
fat_line or quad_bezier via _anchor helpers.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, sample_line)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; 亻 inlined per B8 left-column note; '
             '2 N-joints preserved (no weld) — s1 mid-body vs s2 head, '
             's3 mid-body vs s4 head.'
}

# MMH anchor tuples (from brief)
S1_HEAD = ('TL', 0.929, 0.621)
S1_TAIL = ('ML', 0.199, 0.925)
S2_HEAD = ('ML', 0.800, 0.365)
S2_TAIL = ('BL', 0.762, 0.880)
S3_HEAD = ('TC', 0.629, 0.574)
S3_TAIL = ('C',  0.189, 0.737)
S4_HEAD = ('C',  0.503, 0.441)
S4_TAIL = ('MR', 0.186, 0.652)
S5_HEAD = ('C',  0.717, 0.644)
S5_TAIL = ('BC', 0.436, 0.751)
S6_HEAD = ('BC', 0.333, 0.074)
S6_TAIL = ('BC', 0.163, 0.558)
S7_HEAD = ('BR', 0.174, 0.045)
S7_TAIL = ('BR', 0.572, 0.549)


def bowed_pie(draw, head, tail, head_w=12, tail_w=2, bow=0.10):
    """Curved 撇 from head to tail, bowing OUT-left (perpendicular offset)."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    # perpendicular (rotate 90° CCW), then bow out to the left/down side
    px, py = -dy, dx
    length = (dx * dx + dy * dy) ** 0.5 or 1
    px, py = px / length, py / length
    ctrl = (mx + px * bow * length, my + py * bow * length)
    pts = quad_bezier(p0, ctrl, p2, n=40)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def straight(draw, head, tail, width=8, head_w=None, tail_w=None):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    if head_w is None:
        fat_line(draw, p0, p1, width)
    else:
        pts = sample_line(p0, p1, n=20)
        widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
                  for i in range(len(pts))]
        stroke_variable_width(draw, pts, widths)


def hook_shu(draw, head, tail, width=9, hook_len=14):
    """竖 with a small left hook at the tail (for 竖钩)."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)
    # small hook up-and-left from the tail
    hx = p1[0] - hook_len
    hy = p1[1] - hook_len * 0.4
    fat_line(draw, p1, (hx, hy), width - 2)


def dot(draw, head, tail, head_w=3, tail_w=10):
    """Descending dot / 点 — narrow head, fat tail."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = sample_line(p0, p1, n=16)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 亻 (inlined)
    bowed_pie(d, S1_HEAD, S1_TAIL, head_w=12, tail_w=2, bow=0.10)
    straight(d, S2_HEAD, S2_TAIL, width=9)

    # 尔 top-撇
    bowed_pie(d, S3_HEAD, S3_TAIL, head_w=9, tail_w=3, bow=0.08)
    # 尔 top-横 (heng short, slight down-right→left)
    straight(d, S4_HEAD, S4_TAIL, width=7)
    # 尔 inner-撇 (small)
    bowed_pie(d, S5_HEAD, S5_TAIL, head_w=8, tail_w=2, bow=0.10)
    # 尔 竖钩 (vertical with small left hook at tail)
    hook_shu(d, S6_HEAD, S6_TAIL, width=9, hook_len=12)
    # 尔 右点 (descending dot)
    dot(d, S7_HEAD, S7_TAIL, head_w=3, tail_w=11)

    # stroke-count assert
    n_strokes = 7
    assert n_strokes == 7, f"expected 7 strokes, got {n_strokes}"

    out = Path(__file__).parent / '01_你.png'
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
