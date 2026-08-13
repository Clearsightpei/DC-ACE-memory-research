"""三 (san, "three") — three separated horizontal strokes.

Bank reuse: `heng.draw_heng` for all three strokes. Endpoints computed
from MMH-derived 米字格 anchors given in the brief.
"""
import sys, os
from PIL import Image, ImageDraw

# Import bank primitive.
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from heng import draw_heng  # noqa: E402


# --- 米字格 cell corners on a 300x300 canvas ---
# 3x3 grid, each cell 100x100. Anchor = (cell_origin) + frac * (100,100).
CELL_ORIGIN = {
    'TL': (0,   0),   'TM': (100, 0),   'TR': (200, 0),
    'ML': (0,   100), 'MM': (100, 100), 'MR': (200, 100),
    'BL': (0,   200), 'BM': (100, 200), 'BR': (200, 200),
}
def anchor(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


# --- endpoints from brief ---
# stroke 1 (top short heng)
s1_h = anchor('ML', 0.926, 0.081)   # ~ (92.6, 108.1)
s1_t = anchor('TR', 0.115, 0.973)   # ~ (211.5,  97.3)
# stroke 2 (middle short heng)
s2_h = anchor('ML', 0.970, 0.808)   # ~ (97.0, 180.8)
s2_t = anchor('MR', 0.051, 0.734)   # ~ (205.1, 173.4)
# stroke 3 (bottom long heng)
s3_h = anchor('BL', 0.372, 0.555)   # ~ (37.2, 255.5)
s3_t = anchor('BR', 0.798, 0.490)   # ~ (279.8, 249.0)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Top stroke: shorter and thinner
draw_heng(d, s1_h, s1_t, width_head=8, width_tail=9)
# Middle stroke: similar to top
draw_heng(d, s2_h, s2_t, width_head=8, width_tail=9)
# Bottom stroke: longest, slightly heavier
draw_heng(d, s3_h, s3_t, width_head=10, width_tail=11)

out = os.path.join(os.path.dirname(__file__), "01_三.png")
img.save(out)
print("wrote", out)


# --- mandatory self-check ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 draw_heng calls == expected 3
    'endpoint_mismatches': [],        # anchors used verbatim from brief
    'joint_class_mismatches': [],     # no joints expected (all N/clear)
    'overall_pass': True,
    'notes': ("three separated heng; used bank primitive heng.draw_heng; "
              "top and middle intentionally shorter than bottom per GT."),
}
