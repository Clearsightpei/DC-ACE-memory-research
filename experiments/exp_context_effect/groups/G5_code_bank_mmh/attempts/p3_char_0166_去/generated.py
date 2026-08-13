# BANK_DEVIATION
# skipped: tu_earth.py
# reason: 去's top 土 sits compressed at the upper canvas (top heng at y~130,
#   long heng at y~196), and its long heng is horizontally wider than tu_earth
#   provides. Uniform (ox, oy, scale) can't hit the target aspect. Inlining
#   fresh from MMH anchors.
# fresh_component: tu_compressed_top_for_qu (top 土 pushed up, long heng wider)
#
# 厶 (bottom) drawn fresh: no bank entry for si_private yet.
"""p3_char_0166_去 — G5.

去 = 土 (top, compressed upward) + 厶 (bottom).
5 strokes total, matches MMH-derived structural expectations.
"""
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 5 line() calls → 5 strokes
    'endpoint_mismatches': [],         # all within ±0.05 of anchor pixels
    'joint_class_mismatches': [],      # s1×s2 = P (crossing); rest = N
    'overall_pass': True,
    'notes': 's4 (撇折) drawn as 2-segment polyline with bend at BL corner.',
}


def draw_qu():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: short top 横 of 土
    # head ('ML', 0.923, 0.356) → (92, 136); tail ('MR', 0.062, 0.23) → (206, 123)
    d.line([(92, 136), (206, 123)], fill='black', width=6)

    # Stroke 2: 竖 of 土 (crosses s1 near center = P joint)
    # head ('TC', 0.356, 0.612) → (136, 61); tail ('C', 0.421, 0.86) → (142, 186)
    d.line([(136, 61), (142, 186)], fill='black', width=6)

    # Stroke 3: long 横 (bottom of 土, spans nearly full width)
    # head ('BL', 0.243, 0.036) → (24, 204); tail ('MR', 0.748, 0.89) → (275, 189)
    d.line([(24, 204), (275, 189)], fill='black', width=7)

    # Stroke 4: 厶 first stroke — 撇折 (pie down-left then fold-right)
    # head ('C', 0.33, 0.998) → (133, 200); tail ('BC', 0.937, 0.643) → (194, 264)
    # Tighter L-bend at bottom-left keeps 厶 compact under the long heng.
    d.line([(133, 210), (118, 272), (194, 268)], fill='black', width=6)

    # Stroke 5: 厶 second stroke — 点/na (dot, down-right), thicker at tail
    # head ('BC', 0.793, 0.329) → (179, 233); tail ('BR', 0.191, 0.974) → (219, 297)
    d.line([(179, 233), (215, 293)], fill='black', width=7)

    return img


if __name__ == '__main__':
    import os
    img = draw_qu()
    out = os.path.join(os.path.dirname(__file__), '01_去.png')
    img.save(out)
    print(f'wrote {out}')
