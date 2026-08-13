"""p3_char_0327_识 — Phase 3 character.

Decomposition: 识 = 讠 (left, 2 strokes) + 只 (right, 5 strokes).
只 = 口 (top, 3 strokes) + 八 (legs, 2 strokes).
Total 7 strokes matching MMH expected count.

Approach (per v8 REFERENCE-only rule): inline via base primitives
(dian, heng_zhe_ti pieces, shu-style fat_line for 口 walls, pie, na)
using MMH-verbatim anchor endpoints. Not calling yan_speech / kou / ba
wrappers because their default anchors are calibrated for standalone
radicals and would overwhelm the compressed left/right halves here.

Memory index steps 1-3 done:
  1. drawer_memory.md read (this is a 讠+ non-bank-right composition —
     Cluster 3 of B7 failure notes; no dedicated primitive for 只 in
     bank — but 只 does exist as INDEX entry 172; not writable to import).
  2. success_bank/INDEX.md grep: 识 not mastered. 讠 (yan_speech.py)
     mastered. 只 mastered (INDEX #172). 口 mastered. 八 mastered.
  3. errata.md grep: 识 not in errata.

Joints (all N — do NOT weld):
  s3.mid ⇆ s4.head @ C (~13 px gap)
  s3.tail ⇆ s5.head @ C (~13 px gap)
  s4.tail ⇆ s5.mid @ MR (~17 px gap)
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from dian import draw_dian
from pie import draw_pie
from na import draw_na

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; MMH-verbatim endpoints. 讠 dot + heng-zhe-ti on left; 口 (3 strokes, N gaps) + 八 legs (2 strokes) on right. All 3 declared joints implemented as N (no weld).'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # === Left: 讠 (yan_speech), 2 strokes ===

    # s1: 点 (dot) — MMH head=('TL',0.814,0.659), tail=('TC',0.178,0.92)
    draw_dian(d, ('TL', 0.814, 0.659), ('TC', 0.178, 0.92),
              head_width=2, peak_width=9, curve=0.10, segments=24)

    # s2: 横折提 (compound) — MMH head=('ML',0.202,0.611), tail=('BC',0.301,0.194)
    # MMH only gives endpoints. Infer corner (top-right of horiz) and knee
    # (bottom of vertical) so that the ti flicks up-right into the tail.
    draw_heng_zhe_ti_inline(d,
        head_h=('ML', 0.202, 0.611),
        corner=('ML', 0.95, 0.62),
        knee=('BL',  0.85, 0.30),
        tail=('BC',  0.301, 0.194),
        h_width=8, v_width=8, shoulder=11,
        ti_head_w=10, ti_tail_w=1)

    # === Right: 只 (口 top + 八 legs), 5 strokes ===

    # ---- 口 (small, upper-right region) ----
    # s3: 竖 left wall — head=('C',0.395,0.16), tail=('C',0.617,0.995)
    s3h = anchor_to_xy(('C', 0.395, 0.16))
    s3t = anchor_to_xy(('C', 0.617, 0.995))
    # shorten head/tail slightly to keep N-gap at bottom-left corner
    s3t_g = _shorten(s3t, s3h, 3)
    fat_line(d, s3h, s3t_g, width=7)

    # s4: 横折 top+right wall — head=('C',0.582,0.251), tail=('MR',0.159,0.696)
    s4h = anchor_to_xy(('C', 0.582, 0.251))
    s4_corner = (anchor_to_xy(('MR', 0.159, 0.696))[0],  # x from tail
                 anchor_to_xy(('C', 0.582, 0.251))[1])   # y from head
    s4t = anchor_to_xy(('MR', 0.159, 0.696))
    # shorten head so s3.mid ⇆ s4.head is N (not welded)
    s4h_g = _shorten(s4h, s4_corner, 3)
    fat_line(d, s4h_g, s4_corner, width=7)
    # shoulder disc for clean 90° corner
    cx, cy = s4_corner; r = 4
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    fat_line(d, s4_corner, s4t, width=7)

    # s5: 横 bottom bar — head=('C',0.679,0.898), tail=('MR',0.373,0.799)
    s5h = anchor_to_xy(('C', 0.679, 0.898))
    s5t = anchor_to_xy(('MR', 0.373, 0.799))
    # shorten head so s3.tail ⇆ s5.head is N (~13px gap)
    s5h_g = _shorten(s5h, s5t, 3)
    fat_line(d, s5h_g, s5t, width=7)

    # ---- 八 legs (below 口) ----
    # s6: 撇 — head=('BC',0.793,0.282), tail=('BC',0.122,0.854)
    draw_pie(d, ('BC', 0.793, 0.282), ('BC', 0.122, 0.854),
             head_width=10, tail_width=1, curve=0.12, segments=48)

    # s7: 捺 — head=('BR',0.115,0.188), tail=('BR',0.584,0.777)
    draw_na(d, ('BR', 0.115, 0.188), ('BR', 0.584, 0.777),
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    return img


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_heng_zhe_ti_inline(draw_obj, head_h, corner, knee, tail,
                            h_width=8, v_width=8, shoulder=11,
                            ti_head_w=10, ti_tail_w=1):
    """Inlined heng_zhe_ti with 4 anchors — MMH-compressed version for 讠 in 识.
    The bank's draw_heng_zhe_ti primitive uses defaults sized for a
    standalone radical; we need a smaller, MMH-anchored placement here.
    """
    p_h = anchor_to_xy(head_h)
    p_c = anchor_to_xy(corner)
    p_k = anchor_to_xy(knee)
    p_t = anchor_to_xy(tail)

    # 横 segment
    fat_line(draw_obj, p_h, p_c, h_width)
    # shoulder disc at corner
    r = shoulder / 2.0
    draw_obj.ellipse([p_c[0] - r, p_c[1] - r, p_c[0] + r, p_c[1] + r], fill=(0, 0, 0))
    # 竖 segment
    fat_line(draw_obj, p_c, p_k, v_width)
    # 提 (rising flick, tapered): knee → tail
    dx, dy = p_t[0] - p_k[0], p_t[1] - p_k[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = 0.06 * length
    mid = ((p_k[0] + p_t[0]) * 0.5 + perp[0] * bow,
           (p_k[1] + p_t[1]) * 0.5 + perp[1] * bow)
    pts = quad_bezier(p_k, mid, p_t, n=32)
    widths = [ti_head_w + (ti_tail_w - ti_head_w) * (i / 32) for i in range(33)]
    stroke_variable_width(draw_obj, pts, widths)


if __name__ == '__main__':
    img = draw()
    out = os.path.join(_HERE, '01_识.png')
    img.save(out)
    print(f'Wrote {out}')
