# run_5 POSTMORTEM

Frozen 2026-06-10 at cycle 25 (22 character entries promoted, ~25% of attempts).

## Core problem this run surfaced

The 4-gate (OCR is_correct + ocr_margin ≥ 0.3 + visual_score > 0.8 + 3-judge panel unanimous YES) is **insufficient for structural fidelity**. It catches gross morphological failures (missing strokes, wildly wrong proportions, OCR confusion) but absorbs subtle structural errors where an extra or misplaced stroke gets tucked into existing ink — the dilated Dice metric and the panel both forgive what they shouldn't.

Concrete leaks: **五 c20** (5 turtle calls vs MMH's 4 strokes — extra closing-bottom heng) and **丘 c24** (6 vs 5 — extra right shu between middle and bottom heng). Both promoted with panel 3/3 YES. The Success Bank is now contaminated with two entries that the system believes are mastered but that don't structurally match MMH.

Compound stroke practice was also skipped: 横折 / 竖钩 / 横折钩 / 竖弯钩 / 横撇 / 竖折 / 横折弯钩 were carried over from run_4 as already-mastered without any run_5 cycle where the Drawer actually rendered them in isolation and got gated. The Teacher loafed on the curriculum.

## Why it motivates the next run (run_6)

The memory architecture stores numbers (ox, oy, scale) per character. The AI memorizes magic numbers, not structure. So the gates that protect the memory are forced to be pixel-based, which is what allowed the leaks.

**Run_6 changes WHAT is being memorized**: 米字格 (9-cell grid) + anchor notation + per-character joint specs derived from MMH medians. The Success Bank entries become structural descriptions — which cells the strokes cross, where they meet, which side has the head. The same architecture that produces compositional reuse is the architecture that admits a structural verification gate. Stroke-count mismatch becomes a hard rejection. Anchor placement (15 px tolerance) and joint placement (20 px tolerance inside declared cell) become numeric, mechanical checks that don't rely on vision.

Run_6 also makes the Teacher honest: 6 atomic strokes (c1–c6) followed by 7 compound strokes (c7–c13), each practiced in isolation and gated, before any character cycle. At 1 task per cycle (vs run_5's 3), depth replaces breadth.

The plan that produced run_6 is at `~/.claude/plans/should-i-install-rapid-lexical-lantern.md` (Parts 1–6).
