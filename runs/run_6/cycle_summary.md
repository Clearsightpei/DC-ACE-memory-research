# Cycles 65-74 batch summary (calibration-corpus mode)

10 cycles run for calibration corpus expansion. Fast-mode introduced from c72 (direct render, 1 skeptic, 2-attempt max).

| Cycle | Char | Strokes | Outcome | OCR | Skeptic | Notes |
|---|---|---|---|---|---|---|
| 65 | 力 | 2 | FROZEN | 力 ✓ | 0/3 | heng_zhe_gou primitive ceiling |
| 66 | 自 | 6 | PROMOTED | 自 ✓ | 3/3 | counting disambiguation in panel prompt |
| 67 | 个 | 3 | FROZEN | — | 0/3 | shu dunbi-blob below-centerline ceiling |
| 68 | 古 | 5 | FROZEN | 女 | skipped | MMH 口 anchors malformed |
| 69 | 米 | 6 | SKIPPED | — | — | user attestation |
| 70 | 林 | 8 | PROMOTED | 林 ✓ | 3/3 | first 8-stroke char promoted |
| 71 | 明 | 8 | carry-over | empty | skipped | brief heng_zhe corner bug |
| 72 | 明 | 8 | FROZEN | 眸 | skipped | corrected anchors but still fails OCR |
| 73 | 朋 | 8 | FROZEN | 用 | skipped | missing distinguishing pie |
| 74 | 雨 | 8 | not-promoted | 雨 ✓ | 1/1 NO | OCR PASS but skeptic NO; calibration-valuable |

Bank: 41 → 43 (自, 林 promoted).
Calibration corpus: +10 PNGs across 2-8 stroke range with diverse outcomes (2 PROMOTED, 5 FROZEN, 1 skip, 1 carry-over, 1 OCR-PASS-skeptic-NO).
