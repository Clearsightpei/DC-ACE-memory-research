"""自 (zì, "self") — mastered c66.

Tags: tag:character, tag:6-strokes, tag:component-of(息,鼻,首)
MMH stroke count: 6
Gate readings:
  - OCR: 自 (conf 0.4919, correct)
  - visual_score: 0.7988
  - panel: 3/3 YES (after panel prompt explicitly clarified 2 internal hengs + box-closing-bottom)
History: c51 (1/3, merging hengs), c57 (2/3 NEAR, counting ambiguity), c66 PROMOTED.

Reuse: import draw_zi from success_bank/code/zi
       draw_zi(t)  # renders at canonical米字格 position
"""

def draw_zi(t):
    from _anchor import anchor_to_xy  # noqa
    from pie import draw_pie
    from shu import draw_shu
    from heng_zhe import draw_heng_zhe
    from heng import draw_heng
    # s1: pie above box
    draw_pie(t, ("TC", 0.308, 0.224), ("ML", 0.664, 0.016))
    # s2: shu left wall of 日-box
    draw_shu(t, ("ML", 0.664, 0.016), ("BL", 0.764, 1.252))
    # s3: heng_zhe = top + right of 日-box
    draw_heng_zhe(t, ("ML", 0.92, 0.112), ("C", 0.96, 0.112), ("BC", 0.96, 1.132))
    # s4: upper internal heng
    draw_heng(t, ("ML", 0.912, 0.864), ("C", 0.96, 0.704))
    # s5: lower internal heng
    draw_heng(t, ("BL", 0.912, 0.46), ("BC", 0.96, 0.332))
    # s6: closing bottom of 日-box
    draw_heng(t, ("BL", 0.868, 1.176), ("BR", 0.048, 1.048))
