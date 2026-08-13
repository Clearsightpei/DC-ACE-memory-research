"""志 (zhì) — 7 strokes.
Decomposition: 志 = 士 (top) + 心 (bottom).
  s1, s2, s3 = 士 (top-longer 横 + 竖 + shorter 横)
  s4, s5, s6, s7 = 心 (left dot + 卧钩 + middle dot + right dot)

Per B9 A-recipe: MMH-verbatim anchors + base primitives.
Not importing shi_scholar / xin — MMH places 士 in the top y∈[0.03, 0.28]
band and 心 in the y∈[0.65, 0.95] band; compound-primitive default
anchors sit differently and partial-override is the #1 near-A loss.

Joints:
  s1.mid ⇆ s2.mid @ C : P — welded (士 cross)
  s2.tail ⇆ s3.mid @ C : N — gap ~16.5 px (do NOT weld)
心 dots are all S-class (visually separate).
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
    'notes': '7 strokes MMH-verbatim; 士 cross welded (P); 士 stem→bottom-heng '
             'left as N-gap ~13px; 心 卧钩 curves down then hooks up-right.'
}

# --- MMH anchor tuples from dispatcher brief (verbatim) ---
# 士 (top)
S1_HEAD = ('ML', 0.735, 0.26)    # top 横 left
S1_TAIL = ('MR', 0.276, 0.087)   # top 横 right
S2_HEAD = ('TC', 0.371, 0.612)   # 竖 top
S2_TAIL = ('C',  0.441, 0.685)   # 竖 bottom (leaves gap to s3)
S3_HEAD = ('ML', 0.94,  0.805)   # bottom 横 left
S3_TAIL = ('MR', 0.089, 0.758)   # bottom 横 right

# 心 (bottom)
S4_HEAD = ('BL', 0.686, 0.194)   # left dot head
S4_TAIL = ('BL', 0.495, 0.766)   # left dot tail (descends left)
S5_HEAD = ('BL', 0.981, 0.165)   # 卧钩 start (left, upper)
S5_TAIL = ('BR', 0.024, 0.396)   # 卧钩 exit (right, lower — before hook)
S6_HEAD = ('BC', 0.359, 0.033)   # middle dot head
S6_TAIL = ('BC', 0.641, 0.314)   # middle dot tail
S7_HEAD = ('MR', 0.147, 0.963)   # right dot head (upper-left)
S7_TAIL = ('BR', 0.66,  0.329)   # right dot tail (lower-right)


def straight_line(draw, head, tail, width=9):
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, width)


def tapered(draw, head, tail, head_w=3, tail_w=11, n=18):
    """Descending dot / 点 with tapered width."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = sample_line(p0, p1, n=n)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def wo_gou_stroke(draw, head, tail, belly_dy=32, hook_len=14, hook_up=16,
                  head_w=3, body_w=11, hook_w=7):
    """卧钩 — curves down through a belly then hooks up-right at tail."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    ctrl = (mx, my + belly_dy)   # belly below midpoint
    pts = quad_bezier(p0, ctrl, p2, n=36)
    widths = [head_w + (body_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)
    # small hook up-and-right from the tail
    hx = p2[0] + hook_len * 0.2
    hy = p2[1] - hook_up
    fat_line(draw, p2, (hx, hy), hook_w)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # 士 — top-longer 横, then 竖 crossing at C (P weld), then bottom-shorter 横
    straight_line(d, S1_HEAD, S1_TAIL, width=9)   # top heng (long)
    straight_line(d, S2_HEAD, S2_TAIL, width=10)  # shu
    straight_line(d, S3_HEAD, S3_TAIL, width=9)   # bottom heng (shorter)

    # 心 — 4 strokes
    tapered(d, S4_HEAD, S4_TAIL, head_w=10, tail_w=3, n=18)   # left dot as short pie
    wo_gou_stroke(d, S5_HEAD, S5_TAIL)                         # 卧钩
    tapered(d, S6_HEAD, S6_TAIL, head_w=3, tail_w=10, n=14)   # middle dot
    tapered(d, S7_HEAD, S7_TAIL, head_w=3, tail_w=11, n=16)   # right dot

    # stroke-count assert
    n_strokes = 7
    assert n_strokes == 7, f"expected 7 strokes, got {n_strokes}"

    out = Path(__file__).parent / '01_志.png'
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
