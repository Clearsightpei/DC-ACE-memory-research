"""又 (yòu, "again/hand", 2 strokes: 横撇 + 捺) — B1 pass.

Strokes:
  s1 — 横撇 (top horizontal bending into a 撇 sweep).
  s2 — 捺 (diagonal from upper-left down-right, with peak swell).

Joint: s1 pie chord ⇆ s2 na chord → P (welded crossing, verified by
segment-cross assertion).
"""
from heng_pie import draw_heng_pie
from na import draw_na


def draw_you(draw,
             S1_HEAD=('TL', 0.75, 0.95), S1_CORNER=('TC', 0.95, 0.85),
             S1_TIP=('BL', 0.95, 0.55),
             S2_HEAD=('C', 0.15, 0.35), S2_TAIL=('BR', 0.45, 0.45)):
    draw_heng_pie(draw, head=S1_HEAD, corner=S1_CORNER, tip=S1_TIP,
                  head_w=6, corner_w=11, tip_w=2)
    draw_na(draw, from_anchor=S2_HEAD, to_anchor=S2_TAIL,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.75, curve=0.08, segments=48)
