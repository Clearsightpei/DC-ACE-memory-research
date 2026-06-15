"""果 (guǒ, "fruit") — mastered c74. Tags: tag:character, tag:8-strokes. Panel 3/3."""
def draw_guo_fruit(t):
    from _anchor import anchor_to_xy  # noqa
    from shu import draw_shu
    from heng_zhe import draw_heng_zhe
    from heng import draw_heng
    from pie import draw_pie
    from na import draw_na
    draw_shu(t, ("TL", 0.48, 0.532), ("ML", 0.856, 0.632))
    draw_heng_zhe(t, ("TL", 0.604, 0.508), ("TC", 0.9, 0.508), ("C", 0.9, 0.44))
    draw_heng(t, ("ML", 0.94, 0.056), ("TC", 0.784, 0.944))
    draw_heng(t, ("ML", 0.936, 0.54), ("C", 0.856, 0.356))
    draw_heng(t, ("BL", 0.068, 0.076), ("MR", 0.808, 0.936))
    draw_shu(t, ("TC", 0.316, 0.576), ("BC", 0.412, 1.3))
    draw_pie(t, ("BC", 0.296, 0.064), ("BL", -0.032, 1.256))
    draw_na(t, ("BC", 0.536, 0.048), ("BR", 1.272, 1.188))
