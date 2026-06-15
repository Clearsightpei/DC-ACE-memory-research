"""美 (měi) — mastered c78. 9 strokes: 羊 + 大."""
def draw_mei(t):
    from _anchor import anchor_to_xy  # noqa
    from heng import draw_heng
    from pie import draw_pie
    from na import draw_na
    from shu import draw_shu
    from dian import draw_dian
    draw_pie(t, ("TL", 0.864, 0.392), ("TC", 0.224, 0.696))
    draw_dian(t, ("TC", 0.868, 0.196), ("TC", 0.568, 0.808))
    draw_heng(t, ("ML", 0.58, 0.132), ("TR", 0.304, 0.924))
    draw_heng(t, ("ML", 0.848, 0.6), ("MR", 0.052, 0.464))
    draw_shu(t, ("C", 0.324, 0.172), ("C", 0.372, 0.924))
    draw_heng(t, ("BL", 0.284, 0.092), ("MR", 0.616, 0.92))
    draw_heng(t, ("BL", 0.496, 0.632), ("BR", 0.468, 0.536))
    draw_pie(t, ("BC", 0.196, 0.136), ("BL", 0.256, 1.3))
    draw_na(t, ("BC", 0.472, 0.66), ("BR", 1.116, 1.3))
