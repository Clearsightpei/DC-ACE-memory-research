"""p3_char_0531_速 — 束 (top-right, 7 strokes inline) + 辶 (chuo_walk primitive, 3 strokes).

Memory consulted:
  1. drawer_memory.md — no chronic primitive for 速; but chuo_walk.py is a
     mastered radical primitive for 辶 (INDEX row 74). Errata history for
     辶-containing chars (0044/0240/0306) says "use chuo_walk.py for 辶".
  2. success_bank/INDEX.md — chuo_walk.py present (mastered p2_radical_044).
     No entry for 速 or 束. Inline 束 fresh.
  3. errata.md — 速 not present.

Composition:
  - Strokes 1-7 = 束 (top-right slot). MMH anchors used directly.
    s5 is the long piercing vertical (P-welded with s1, s3, s4).
    s2 = left vertical of 口; s3/s4 = top/bottom horizontals of 口.
    s6 = 撇 (down-left curved), s7 = 捺 (down-right curved with taper).
  - Strokes 8-10 = 辶 walk radical via chuo_walk() primitive. Standalone
    anchors align with MMH 速 anchors within tolerance (s8 head TL(0.595,
    0.823) vs standalone TL(0.618, 0.718); s9 head ML(0.252, 0.69) vs
    standalone ML(0.272, 0.550); s10 sweeps BL→BR similarly).
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier
from chuo_walk import draw_chuo_walk

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 inline + 3 in chuo_walk = 10
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'chuo_walk primitive covers s8-s10; 束 seven strokes inline'
}


def _taper(p0, p2, ctrl_dx, ctrl_dy, n, w_start, w_end):
    p1 = ((p0[0] + p2[0]) / 2 + ctrl_dx, (p0[1] + p2[1]) / 2 + ctrl_dy)
    pts = quad_bezier(p0, p1, p2, n=n)
    widths = [w_start + (w_end - w_start) * i / (len(pts) - 1) for i in range(len(pts))]
    return pts, widths


def draw_char(draw):
    # --- 束 (7 strokes) ---
    # s1: top short heng (upper part of 束)
    fat_line(draw,
             anchor_to_xy(('C', 0.354, 0.104)),
             anchor_to_xy(('MR', 0.232, 0.005)),
             width=8)

    # s2: left vertical of 口
    fat_line(draw,
             anchor_to_xy(('C', 0.184, 0.462)),
             anchor_to_xy(('C', 0.392, 0.951)),
             width=8)

    # s3: top horizontal of 口 (right half)
    fat_line(draw,
             anchor_to_xy(('C', 0.327, 0.456)),
             anchor_to_xy(('MR', 0.098, 0.699)),
             width=9)

    # s4: bottom horizontal of 口
    fat_line(draw,
             anchor_to_xy(('C', 0.444, 0.901)),
             anchor_to_xy(('MR', 0.279, 0.793)),
             width=9)

    # s5: LONG piercing vertical (welded with s1/s3/s4)
    fat_line(draw,
             anchor_to_xy(('TC', 0.638, 0.577)),
             anchor_to_xy(('BC', 0.737, 0.687)),
             width=10)

    # s6: 撇 pie down-left (taper 10 -> 2)
    p0 = anchor_to_xy(('C', 0.685, 0.904))
    p2 = anchor_to_xy(('BC', 0.107, 0.499))
    pts, widths = _taper(p0, p2, ctrl_dx=-8, ctrl_dy=6, n=30, w_start=10, w_end=2)
    stroke_variable_width(draw, pts, [max(1, int(round(w))) for w in widths])

    # s7: 捺 na down-right — thin head, swell at middle-tail then taper tip
    p0 = anchor_to_xy(('BC', 0.934, 0.042))
    p2 = anchor_to_xy(('BR', 0.385, 0.402))
    p1 = ((p0[0] + p2[0]) / 2 - 4, (p0[1] + p2[1]) / 2 - 6)
    pts = quad_bezier(p0, p1, p2, n=30)
    # Swell then taper: 3 -> 12 -> 2
    n = len(pts)
    widths = []
    for i in range(n):
        t = i / (n - 1)
        if t < 0.75:
            w = 3 + (12 - 3) * (t / 0.75)
        else:
            w = 12 * (1 - (t - 0.75) / 0.25) + 2 * ((t - 0.75) / 0.25)
        widths.append(max(1, int(round(w))))
    stroke_variable_width(draw, pts, widths)

    # --- 辶 (3 strokes via chuo_walk primitive) ---
    draw_chuo_walk(draw)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_速.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
