# Sandbox

## Current focus: 人 (carry-over from c19)

c19 attempted 3 compositions of 撇+捺:
1. Shared apex, balanced lengths → OCR returned 入 (visual 0.37)
2. Longer 撇 (0.65 scale), shorter 捺 (0.50 scale) → still 入 (visual 0.35)
3. 撇 dominant + 捺 head slightly below apex → still 入 (visual 0.38)

The brushed primitives are correct (rubric 8/10) but OCR confidence is high enough on "入" that the silhouette must be visibly different from 入.

**Hypothesis for next attempt**: Run_3 c4 mastered 人 with simpler brushed primitives (no fancy two-segment 捺 with kick). The flat-kick of 捺 may be making this read as 入. Try drawing the 捺 portion as a SIMPLE downward sweep (like 撇 mirrored — using draw_pie with X flipped) instead of using na.py's flat-kick variant.

## Generalizable findings (drafts)

(none yet — 人 not mastered)
