"""林 (lín, "forest") — mastered c70 (first 8-stroke char).

Tags: tag:character, tag:8-strokes, tag:component-of(森,琳)
MMH stroke count: 8 (two 木 left+right)
Gate readings: OCR=林 (0.49+), visual_score=0.87, panel 3/3 YES.
"""

def draw_lin(t):
    from _anchor import anchor_to_xy  # noqa
    from heng import draw_heng
    from shu import draw_shu
    from pie import draw_pie
    from na import draw_na
    # left 木
    draw_heng(t, ("ML", -0.112, 0.588), ("C", 0.168, 0.408))
    draw_shu(t, ("TL", 0.504, 0.38), ("BL", 0.588, 1.3))
    draw_pie(t, ("ML", 0.568, 0.636), ("BL", -0.288, 0.964))
    draw_na(t, ("ML", 0.764, 0.9), ("BC", 0.048, 0.144))
    # right 木
    draw_heng(t, ("C", 0.376, 0.432), ("MR", 0.792, 0.204))
    draw_shu(t, ("TC", 0.808, 0.232), ("BC", 0.928, 1.3))
    draw_pie(t, ("C", 0.876, 0.516), ("BC", 0.012, 0.82))
    draw_na(t, ("MR", 0.096, 0.648), ("BR", 1.3, 0.728))
