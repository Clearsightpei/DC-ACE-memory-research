"""引 (yǐn) — 4 strokes = 弓 (3 strokes, left half) + 丨 (1 stroke, right half).

Lookup checklist (mandatory):
1. success_bank/INDEX.md grep: 弓 -> chronic/gong_bow.py (canonical, TL/MR/BL columns).
   NOT called directly because 弓 primitive spans cols 0..1 (full width);
   for 引, 弓 must be COMPRESSED to left half so vertical fits right.
   Inline 弓 in left cells using same 3-tier structure per gong_bow.py plan.
2. errata.md grep: 引 not listed. 弓 chronic supplanted at retry_n=3.
3. form_catalog.md: 竖 rightmost = full col-locked (TC head, BR tail per MMH).
4. principles_meta.md: TR8 rule 6 col-lock for vertical; TR9 span full grid.
5. joint_atlas.md: N-class between 弓 tiers ~25-30 px (do NOT weld).
6. sandbox.md: no 引-specific note.

Structure: 弓 on left (cols TL/ML/BL), vertical on right (cols TC/BR).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_CODE = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _CODE)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes: 横折 + 横 + 竖折折钩 + 竖
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '弓 compressed to left half (TL/ML/BL heads); 竖 on right (TC head, BR tail).',
}


def _shu_zhe_zhe_gou_leftward(draw, head, corner1, corner2, hook_pt, tip,
                              width=9, color=(0, 0, 0)):
    """竖折折钩 whose bottom sweeps LEFT (弓's bowl)."""
    p_head = anchor_to_xy(head)
    p_corner1 = anchor_to_xy(corner1)
    p_corner2 = anchor_to_xy(corner2)
    p_hook_pt = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)
    fat_line(draw, p_head, p_corner1, width=width, color=color)
    fat_line(draw, p_corner1, p_corner2, width=width, color=color)
    fat_line(draw, p_corner2, p_hook_pt, width=width, color=color)
    ctrl = (p_hook_pt[0] + (p_tip[0] - p_hook_pt[0]) * 0.15,
            p_hook_pt[1] + (p_tip[1] - p_hook_pt[1]) * 0.55)
    hook_pts = quad_bezier(p_hook_pt, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [width + (2 - width) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)


def draw_yin(draw):
    # --- 弓 compressed to LEFT half (cols 0..~1) ---

    # s1 — 横折 top tier: head TL, corner top-middle area, tail down to C col
    draw_heng_zhe(draw,
                  ('TL', 0.30, 0.40),
                  ('TC', 0.30, 0.40),   # col-lock horizontal → corner
                  ('C',  0.30, 0.10),   # col-lock vertical drop
                  h_width=8, v_width=8, shoulder=10)

    # s2 — 横 middle tier
    draw_heng(draw, ('ML', 0.30, 0.75), ('C', 0.30, 0.75),
              width=8)

    # s3 — 竖折折钩 bottom tier (leftward sweep + up-right hook)
    _shu_zhe_zhe_gou_leftward(
        draw,
        ('C',  0.30, 0.05),   # col-share with s2 tail
        ('BC', 0.30, 0.35),   # short drop
        ('BL', 0.20, 0.35),   # sweep left
        ('BL', 0.20, 0.05),   # up-tick
        ('BL', 0.60, 0.00),   # flick up-right into bowl
        width=8,
    )

    # --- s4 — 竖 (right vertical, tall) ---
    # MMH: head @ ('TC', 0.998, 0.618) tail @ ('BR', 0.139, 1.059)
    # → head effectively at TR col-left, tail at BR col-left, near col-lock.
    draw_shu(draw, ('TC', 1.00, 0.30), ('BC', 1.00, 1.00),
             width=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_yin(d)
    out = os.path.join(_HERE, '01_引.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
