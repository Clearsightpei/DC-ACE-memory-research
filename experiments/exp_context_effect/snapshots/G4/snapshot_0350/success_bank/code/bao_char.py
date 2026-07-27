"""勹 (bāo, 2画) — Phase-3 char, B4 promotion.

Thin wrapper around mastered `bao.py` (p2_radical_010_勹). Character
is identical to the radical, so calling with mastered default anchors
is correct; also exposed explicitly per TR1.

Strokes: 撇 + 横折钩.
Joint: s1.mid ⇆ s2.head @ ML — N (small natural gap ~16 px, do NOT weld).
"""
from bao import draw_bao


def draw_bao_char(draw):
    # OVERRIDE anchors default to bao.py's mastered defaults per TR1 —
    # radical == character here, no compositional adjustment needed.
    draw_bao(draw)
