# c75-c84 REDO batch (box-rendering fix applied)

Box-rendering fix: explicit aligned corners (TL/TR/BL/BR share x for verticals, share y for horizontals), so box structures render as rectangles instead of slashed parallelograms.

| # | Char | Strokes | OCR | Skeptic | Outcome |
|---|---|---|---|---|---|
| 75 | 京 | 8 | ✓ | YES | **PROMOTED** (proper 口 rectangle) |
| 76 | 春 | 9 | ✓ | NO | data — 人/三 overlap |
| 77 | 看 | 9 | ✓ | NO | data — 目 too narrow |
| 78 | 美 | 9 | ✓ | NO | data — extra heng |
| 79 | 重 | 9 | ✓ | NO | data — 千 missing pie |
| 80 | 香 | 9 | 未 ✗ | skip | OCR-confusion |
| 81 | 信 | 9 | empty | skip | unrecognized |
| 82 | 法 | 8 | empty | skip | unrecognized |
| 83 | 高 | 10 | ✓ | NO | data — components collapse |
| 84 | 唐 | 10 | 后 ✗ | skip | OCR-confusion |

Bank: 43 → 44 (only 京 promoted in this redo, since fixed-box rendering revealed other compositional issues).
