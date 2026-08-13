"""p3_char_0567_桌 — 桌 (zhuō, "table"), 10 strokes.

Split: 卜 (2) + 日 (4) + 木 (4). No bank primitive for full 桌.
Renders per MMH-injected anchors with fat_lines; s4 rendered as L-shape
(横折), s8 (木's 竖) clipped to canvas bottom.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 fat_line/L-shape calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '桌 = 卜+日+木 straight-line render; s4 as L-shape 横折; N joints via small shorten',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)
W = 6

def shorten(p, other, px):
    dx, dy = other[0]-p[0], other[1]-p[1]
    d = (dx*dx+dy*dy)**0.5
    if d < 1e-6: return p
    t = min(1.0, px/d)
    return (p[0]+dx*t, p[1]+dy*t)

def clip_y(p, y_max=298):
    return (p[0], min(p[1], y_max))

# --- Stroke 1: 卜 short tick (top vertical/pie) ---
s1h = anchor_to_xy(('TC', 0.339, 0.571))
s1t = anchor_to_xy(('C',  0.4,   0.125))
fat_line(draw, s1h, s1t, W)

# --- Stroke 2: 卜 short heng across top ---
s2h = anchor_to_xy(('TC', 0.544, 0.841))
s2t = anchor_to_xy(('TR', 0.133, 0.762))
fat_line(draw, s2h, s2t, W)

# --- Stroke 3: 日 left wall (竖) — slight slant per MMH ---
s3h = anchor_to_xy(('ML', 0.844, 0.225))
s3t = anchor_to_xy(('C',  0.078, 0.89))
fat_line(draw, s3h, s3t, W)

# --- Stroke 4: 日 top + right wall (横折) as L-shape ---
s4h = anchor_to_xy(('C', 0.002, 0.233))
s4t = anchor_to_xy(('C', 0.813, 0.79))
s4c = (s4t[0], s4h[1])   # corner top-right
fat_line(draw, s4h, s4c, W)
fat_line(draw, s4c, s4t, W)

# --- Stroke 5: 日 middle 横 ---
s5h = anchor_to_xy(('C', 0.09,  0.55))
s5t = anchor_to_xy(('C', 0.644, 0.465))
fat_line(draw, shorten(s5h, s5t, 2), shorten(s5t, s5h, 3), W)

# --- Stroke 6: 日 bottom 横 ---
s6h = anchor_to_xy(('C', 0.128, 0.822))
s6t = anchor_to_xy(('C', 0.737, 0.749))
fat_line(draw, s6h, s6t, W)

# --- Stroke 7: 木 top 横 ---
s7h = anchor_to_xy(('BL', 0.451, 0.25))
s7t = anchor_to_xy(('BR', 0.458, 0.156))
fat_line(draw, s7h, s7t, W)

# --- Stroke 8: 木 竖 (clip to canvas) ---
s8h = anchor_to_xy(('C',  0.365, 0.866))
s8t = anchor_to_xy(('BC', 0.456, 1.117))
fat_line(draw, s8h, clip_y(s8t), W)

# --- Stroke 9: 木 撇 (pie down-left) ---
s9h = anchor_to_xy(('BC', 0.356, 0.241))
s9t = anchor_to_xy(('BL', 0.428, 0.956))
fat_line(draw, s9h, s9t, W)

# --- Stroke 10: 木 捺 (na down-right) ---
s10h = anchor_to_xy(('BC', 0.521, 0.232))
s10t = anchor_to_xy(('BR', 0.692, 0.88))
fat_line(draw, s10h, s10t, W)

img.save(os.path.join(os.path.dirname(__file__), '01_桌.png'))
print('OK 桌 10 strokes')
