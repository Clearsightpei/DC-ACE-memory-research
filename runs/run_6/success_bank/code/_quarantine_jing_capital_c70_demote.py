"""京 (jīng, "capital") — mastered c75 (with aligned-corner box-fix). 8 strokes."""
def draw_jing_capital(t):
    from _anchor import anchor_to_xy  # noqa
    from dian import draw_dian; from heng import draw_heng; from shu import draw_shu
    from heng_zhe import draw_heng_zhe; from pie import draw_pie; from na import draw_na
    draw_dian(t, ("TC", 0.4, 0.0), ("TC", 0.5, 0.3))
    draw_heng(t, ("TL", 0.4, 0.4), ("TR", 0.6, 0.4))
    draw_shu(t, ("ML", 0.9, 0.3), ("ML", 0.9, 0.9))
    draw_heng_zhe(t, ("ML", 0.9, 0.3), ("MR", 0.1, 0.3), ("MR", 0.1, 0.9))
    draw_heng(t, ("ML", 0.9, 0.9), ("MR", 0.1, 0.9))
    draw_shu(t, ("BC", 0.5, 0.0), ("BC", 0.5, 1.0))
    draw_pie(t, ("BL", 0.7, 0.3), ("BL", 0.3, 1.0))
    draw_na(t, ("BR", 0.0, 0.3), ("BR", 0.5, 1.0))
