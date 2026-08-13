"""p3_char_0315_声 — G4 render.

Decomposition: 声 = 士 (top: 横 + 竖 + 横) + 尸-like frame (横 + 竖 + 横 + long 撇).
7 strokes total, verbatim per MMH anchors.

Bank reuse notes:
  - Top three strokes mirror shi_scholar.py structure (横/竖/横 crossing).
  - Long 撇 (s7) drawn fresh via draw_pie — endpoint below canvas is
    expected (MMH y_frac=1.114 in BL row → y=311, PIL clips harmlessly).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng import draw_heng
from shu  import draw_shu
from pie  import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes rendered verbatim from MMH anchors; joints all N except s1xs2 P (natural crossing).',
}


def render(out_png):
    img = ImageDraw.Draw(Image.new('RGB', (300, 300), 'white'))
    im  = img._image if False else None  # keep linter quiet
    canvas = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(canvas)

    # --- 士 (top) ---
    # s1: long top 横
    draw_heng(d, ('ML', 0.691, 0.02), ('TR', 0.294, 0.894), width=9)
    # s2: short 竖 crossing s1 near TC
    draw_shu (d, ('TC', 0.415, 0.583), ('C',  0.459, 0.257), width=9)
    # s3: middle 横 (bottom bar of 士)
    draw_heng(d, ('ML', 0.949, 0.356), ('MR', 0.045, 0.271), width=9)

    # --- 尸-like frame + long 撇 ---
    # s4: horizontal (top of the 尸 opening — slightly sloped down-right)
    draw_heng(d, ('ML', 0.993, 0.667), ('C',  0.937, 0.931), width=9)
    # s5: short inner 竖
    draw_shu (d, ('C',  0.418, 0.702), ('BC', 0.412, 0.004), width=8)
    # s6: bottom 横
    draw_heng(d, ('BL', 0.935, 0.183), ('BR', 0.15,  0.042), width=9)
    # s7: long 撇 sweeping from mid-left down and out of the frame
    draw_pie (d, ('ML', 0.771, 0.611), ('BL', 0.243, 1.114),
              head_width=11, tail_width=2, curve=0.06, segments=56)

    canvas.save(out_png)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_声.png')
    render(out)
    print('wrote', out)
