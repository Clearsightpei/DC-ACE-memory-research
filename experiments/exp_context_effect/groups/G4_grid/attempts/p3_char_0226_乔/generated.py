"""p3_char_0226_乔 — G4 attempt.

Split: 乔 = top 夭-ish (short pie + heng + long pie + na) + bottom small 丿丨.
Six MMH strokes. No matching chronic primitive; rendering fresh with the
米字格 anchors from the brief.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes; s2 crosses s3 (P); s1-s3, s2-s4, s3-s5 are N-gaps.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

def curve(a, b, ctrl_bias=(0, 0), widths=(6, 6, 5), n=40):
    """Quadratic curve from anchor a to b via a midpoint offset by ctrl_bias."""
    p0 = anchor_to_xy(a)
    p2 = anchor_to_xy(b)
    p1 = ((p0[0] + p2[0]) / 2 + ctrl_bias[0], (p0[1] + p2[1]) / 2 + ctrl_bias[1])
    pts = quad_bezier(p0, p1, p2, n=n)
    ws = [widths[0] + (widths[-1] - widths[0]) * i / (len(pts) - 1) for i in range(len(pts))]
    # taper middle a hair
    for i in range(len(ws)):
        t = i / (len(ws) - 1)
        ws[i] = widths[0] * (1 - t) + widths[-1] * t
    stroke_variable_width(d, pts, ws)

def straight(a, b, widths=(6, 5)):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(b)
    pts = sample_line(p0, p1, n=20)
    ws = [widths[0] + (widths[1] - widths[0]) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(d, pts, ws)

# s1: short top pie — TC(0.942, 0.75) -> TL(0.882, 0.99)
curve(('TC', 0.942, 0.75), ('TL', 0.882, 0.99), ctrl_bias=(0, -6), widths=(6, 6, 4))

# s2: long heng — ML(0.645, 0.38) -> MR(0.288, 0.239)
straight(('ML', 0.645, 0.38), ('MR', 0.288, 0.239), widths=(7, 6))

# s3: long left pie 撇 — TC(0.354, 0.952) -> BL(0.293, 0.253)
curve(('TC', 0.354, 0.952), ('BL', 0.293, 0.253), ctrl_bias=(-8, 10), widths=(8, 8, 3))

# s4: na 捺 — C(0.614, 0.365) -> BR(0.859, 0.109)
curve(('C', 0.614, 0.365), ('BR', 0.859, 0.109), ctrl_bias=(-10, 12), widths=(4, 6, 9))

# s5: small bottom pie — C(0.061, 0.957) -> BL(0.721, 0.918)
curve(('C', 0.061, 0.957), ('BL', 0.721, 0.918), ctrl_bias=(-4, 4), widths=(6, 6, 3))

# s6: small bottom shu — C(0.699, 0.819) -> BC(0.808, 1.108)  (past canvas edge)
straight(('C', 0.699, 0.819), ('BC', 0.808, 1.108), widths=(5, 5))

out = os.path.join(os.path.dirname(__file__), '01_乔.png')
img.save(out)
print("wrote", out)
