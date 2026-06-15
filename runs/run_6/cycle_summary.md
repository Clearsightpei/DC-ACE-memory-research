# Batch c86-c90 summary (11-12 stroke ramp, 2-attempt rule)

PROMOTED (0). FROZEN (5): 黄 c86, 谁 c87, 谈 c88, 黑 c89, 等 c90.
Bank still 44.

11-12 stroke ramp — every char OCR=correct (except 谈 → 淡), but panel 0/3 unanimously NO on all 5.

Recurring failure modes at this difficulty:
- Box/grid components (由 in 黄, 田/里 in 黑) render with diagonal slashes
- Speech radical 讠 collapses (谁, 谈)
- 隹 / 寺 / 寸 structures lack distinguishing hook/dot details
- ⺮ bamboo radical renders as 八+八 instead of 个+个 (笑, 等)

Calibration insight: at 11-12 strokes, the OCR-vs-panel gap is total — RapidOCR keeps accepting, panel keeps rejecting on structural detail. This is the regime where the deterministic structural judge would matter most.
