"""春 (chūn) — mastered c76. 9 strokes: 3 hengs + pie + na + 日-like box."""
def draw_chun(t):
    from _anchor import anchor_to_xy  # noqa
    from heng import draw_heng
    from pie import draw_pie
    from na import draw_na
    from shu import draw_shu
    draw_heng(t, ("TL", 0.72, 0.788), ("TR", 0.2, 0.62))
    draw_heng(t, ("ML", 0.66, 0.26), ("MR", 0.124, 0.1))
    draw_heng(t, ("ML", -0.072, 0.832), ("MR", 0.924, 0.608))
    draw_pie(t, ("TC", 0.272, 0.228), ("BL", -0.1, 0.864))
    draw_na(t, ("C", 0.716, 0.74), ("BR", 1.3, 0.544))
    draw_shu(t, ("BL", 0.8, 0.388), ("BL", 0.904, 1.3))
    draw_shu(t, ("BL", 0.98, 0.384), ("BC", 0.948, 1.3))
    draw_heng(t, ("BC", 0.04, 0.996), ("BC", 0.604, 0.916))
    draw_heng(t, ("BC", 0.012, 1.3), ("BC", 0.748, 1.3))
