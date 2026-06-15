"""重 (zhòng) — mastered c79. 9 strokes."""
def draw_zhong(t):
    from _anchor import anchor_to_xy  # noqa
    from heng import draw_heng
    from pie import draw_pie
    from shu import draw_shu
    draw_pie(t, ("TR", 0.124, 0.508), ("TL", 0.732, 0.852))
    draw_heng(t, ("ML", 0.02, 0.336), ("MR", 1.012, 0.128))
    draw_shu(t, ("ML", 0.596, 0.648), ("BL", 0.896, 0.608))
    draw_heng(t, ("ML", 0.76, 0.632), ("BR", 0.168, 0.524))
    draw_heng(t, ("BC", 0.116, 0.08), ("BC", 0.876, 0.012))
    draw_shu(t, ("BL", 0.972, 0.532), ("BC", 0.988, 0.372))
    draw_shu(t, ("TC", 0.352, 0.78), ("BC", 0.412, 1.3))
    draw_heng(t, ("BL", 0.88, 0.968), ("BR", 0.12, 0.932))
    draw_heng(t, ("BL", 0.26, 1.3), ("BR", 0.852, 1.3))
