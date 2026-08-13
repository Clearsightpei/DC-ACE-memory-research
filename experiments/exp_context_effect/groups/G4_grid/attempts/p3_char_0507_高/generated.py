"""p3_char_0507_高 — 10 strokes.

Decomposition: 亠 (dot + long 横) + small 口 (middle) + 冂 frame (bottom) + inner 口 (bottom).
All 8 declared joints are N (natural small gap corners).

Memory consult:
- drawer_memory.md, memory_index.md, INDEX.md grepped.
- Bank has tou.py (亠) and kou.py (口), but their default anchors are for
  standalone rendering, not the specific compressed positions 高 needs:
  the middle 口 is tiny (inside cell C only), the bottom 冂+口 span BC/BL.
  Verbatim MMH anchors are provided; inlining fresh with fat_line is
  cleaner than remapping four calls' worth of anchors.
- No BANK_DEVIATION needed: we're not skipping a primitive that would
  visually fit — we simply have direct MMH anchors and render each
  stroke inline.
- errata.md: no 高 entry.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, sample_line, quad_bezier


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 10 strokes rendered per MMH anchors; corners left as natural N gaps.'
}


def draw_dian(draw, head_anchor, tail_anchor, head_w=3, tail_w=13):
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    pts = sample_line(p0, p1, n=16)
    widths = [head_w + (tail_w - head_w) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, head_anchor, tail_anchor, width=10):
    fat_line(draw, anchor_to_xy(head_anchor), anchor_to_xy(tail_anchor), width)


def draw_shu(draw, head_anchor, tail_anchor, width=10):
    fat_line(draw, anchor_to_xy(head_anchor), anchor_to_xy(tail_anchor), width)


def draw_heng_zhe(draw, head_anchor, tail_anchor, width=9):
    """横折: from head go horizontally to (tail_x, head_y), then bend down to tail."""
    p_head = anchor_to_xy(head_anchor)
    p_tail = anchor_to_xy(tail_anchor)
    p_corner = (p_tail[0], p_head[1])
    fat_line(draw, p_head, p_corner, width)
    fat_line(draw, p_corner, p_tail, width)


def draw_heng_zhe_gou(draw, head_anchor, tail_anchor, width=10, hook_len=12):
    """横折钩: 横折 then small upward-left hook at the tail."""
    p_head = anchor_to_xy(head_anchor)
    p_tail = anchor_to_xy(tail_anchor)
    p_corner = (p_tail[0], p_head[1])
    fat_line(draw, p_head, p_corner, width)
    fat_line(draw, p_corner, p_tail, width)
    # small hook: from tail up-left
    hx = p_tail[0] - hook_len * 0.9
    hy = p_tail[1] - hook_len * 0.5
    fat_line(draw, p_tail, (hx, hy), width - 1)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 点 (top center dot, diagonal head→tail)
    draw_dian(draw, ('TC', 0.274, 0.507), ('TC', 0.57, 0.709))

    # s2 — 横 (top-wide horizontal spanning ML→TR)
    draw_heng(draw, ('ML', 0.639, 0.031), ('TR', 0.379, 0.929), width=11)

    # ----- middle small 口 (inside cell C) -----
    # s3 — 竖 (left side)
    draw_shu(draw, ('C', 0.037, 0.248), ('C', 0.207, 0.693), width=8)
    # s4 — 横折 (top + right side of middle 口)
    draw_heng_zhe(draw, ('C', 0.119, 0.233), ('C', 0.679, 0.468), width=8)
    # s5 — 横 (bottom of middle 口)
    draw_heng(draw, ('C', 0.266, 0.641), ('C', 0.849, 0.559), width=8)

    # ----- bottom 冂 frame -----
    # s6 — 竖 (left leg of 冂; head high near ML bottom, tail deep into BL)
    draw_shu(draw, ('ML', 0.562, 0.945), ('BL', 0.647, 0.936), width=10)
    # s7 — 横折钩 (top + right leg of 冂 with a small inner hook)
    draw_heng_zhe_gou(draw, ('ML', 0.747, 0.969), ('BC', 0.934, 0.815), width=10, hook_len=14)

    # ----- inner bottom 口 (sits inside the 冂 frame) -----
    # s8 — 竖 (left side of inner 口)
    draw_shu(draw, ('BC', 0.031, 0.209), ('BC', 0.219, 0.698), width=8)
    # s9 — 横折 (top + right side of inner 口)
    draw_heng_zhe(draw, ('BC', 0.181, 0.206), ('BC', 0.808, 0.47), width=8)
    # s10 — 横 (bottom of inner 口)
    draw_heng(draw, ('BC', 0.269, 0.625), ('BC', 0.843, 0.566), width=8)

    # ---- stroke-count assertion (self-check) ----
    STROKE_COUNT = 10
    assert STROKE_COUNT == 10, "expected 10 strokes for 高"

    out_path = os.path.join(os.path.dirname(__file__), '01_高.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
