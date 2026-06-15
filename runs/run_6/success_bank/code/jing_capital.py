"""京 (jīng, "capital") — RE-VERIFIED c72 with MMH-derived anchors (panel 3/3 YES).

Tags: tag:character, tag:8-strokes
History: c75 original (hand-aligned anchors), demoted 2026-06-14 (batch reset),
         c72 re-verified with MMH-derived anchors + programmatic heng_zhe corner.
"""
def draw_jing_capital(t):
    from _anchor import anchor_to_xy  # noqa
    from dian import draw_dian
    from heng import draw_heng
    from shu import draw_shu
    from heng_zhe import draw_heng_zhe
    from pie import draw_pie
    from na import draw_na
    draw_dian(t, ("TC", 0.224, 0.156), ("TC", 0.684, 0.492))
    draw_heng(t, ("ML", -0.036, 0.028), ("TR", 1.124, 0.844))
    draw_shu(t, ("ML", 0.724, 0.432), ("BC", 0.064, 0.224))
    draw_heng_zhe(t, ("ML", 0.808, 0.408), ("C", 0.91, 0.41), ("C", 0.908, 0.884))
    draw_heng(t, ("BC", 0.132, 0.144), ("BR", 0.128, 0.028))
    draw_shu(t, ("BC", 0.392, 0.148), ("BC", 0.036, 1.284))
    draw_pie(t, ("BL", 0.668, 0.484), ("BL", 0.276, 1.176))
    draw_na(t, ("BR", 0.044, 0.484), ("BR", 0.74, 1.192))
