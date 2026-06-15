# Batch c81-c85 summary (10-stroke ramp, 2-attempt rule)

PROMOTED (0). FROZEN (5): 高 c81, 真 c82, 都 c83, 笑 c84, 部 c85.
Bank still 44.

Common pattern: OCR is_correct=True for all 5, but panel skeptics see structural issues:
- 高: missing 冂 mid-frame
- 真: 8 dots detached, 十 vertical missing
- 都: 日 has slash, 阝 ear not closed
- 笑: ⺮ radical halves collapsed/merged
- 部: 阝 ear loop too compressed

Diagnosis: 10-stroke chars stress MMH→primitive mapping more than 8-stroke. Many compound radicals (⺮, 阝) need primitives the success_bank doesn't have. OCR is permissive but panel is strict — gap widens at 10 strokes.
