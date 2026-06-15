"""信 (xìn) — mastered c81. 9 strokes: 亻 + 言."""
def draw_xin_trust(t):
    from _anchor import anchor_to_xy  # noqa
    from pie import draw_pie; from shu import draw_shu; from heng import draw_heng; from dian import draw_dian
    draw_pie(t, ("TL", 0.672, 0.352), ("BL", -0.228, 0.032))
    draw_shu(t, ("ML", 0.44, 0.436), ("BL", 0.46, 1.3))
    draw_dian(t, ("TC", 0.7, 0.236), ("TR", 0.172, 0.636))
    draw_heng(t, ("ML", 0.932, 0.192), ("MR", 1.088, 0.008))
    draw_heng(t, ("C", 0.424, 0.656), ("MR", 0.428, 0.548))
    draw_heng(t, ("BC", 0.392, 0.136), ("BR", 0.444, 0.028))
    draw_shu(t, ("BC", 0.252, 0.624), ("BC", 0.516, 1.3))
    draw_heng(t, ("BC", 0.488, 0.644), ("BR", 0.34, 1.092))
    draw_heng(t, ("BC", 0.596, 1.3), ("BR", 0.6, 1.252))
