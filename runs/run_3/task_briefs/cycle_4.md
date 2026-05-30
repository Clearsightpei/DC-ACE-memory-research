# Cycle 4 — Task brief (Phase 2 carry-over: brushwork repair)

**All 6 characters from cycle 3 carry over.** Cycle 3 produced
6/6 OCR-correct but 0/6 mastered (rubric avg 5.67/10). Two specific
brushwork failure modes — diagnosed in `drawer_memory.md` — must be
fixed this cycle. Composition rules (proportions/positions) were
correct; do not change them.

## Judgment

Eval: **gt+ocr+vision** (same as c3).
Pass = `is_correct == true` AND `calligraphy_rubric.total >= 7`
(no 0 criterion).

## The two fixes that must land

1. **Soften the 顿笔 end-discs on heng/shu.** Cycle 3 looked like
   dumbbells — heavy discs separated by a near-hairline middle. The
   end-cap peak should be ≤ ~2× middle width, and the middle-shaft
   width floor must be ~30% of the peak. The transition between
   peak and middle must read as one continuous brushed stroke,
   not two discs + a thread.
2. **Fix the inverted 捺 width profile.** In 人/八 cycle 3 drew 捺
   heavy at the start and tapering to a fine point — that is a
   second 撇, not a 捺. The heavy 顿笔 on a 捺 is at the
   **LOWER-RIGHT pressed tail** (the end), regardless of how the
   primitive parameterizes start/end. The signature flat tail kick
   must be there.

## Required calligraphic detail per stroke

Same as c3: 顿笔, 弧度 (where appropriate — heng/shu near-straight),
粗细 taper varied per-sample, proportion. Use the "which end is
heavy?" cheat sheet in `drawer_memory.md`.

## Tasks (6) — full carry-over

| idx | char | pinyin | notes |
|-----|------|--------|-------|
| 01  | 一   | yi     | single heng — soften end-discs |
| 02  | 二   | er     | bottom heng longer than top ✓ — soften end-discs |
| 03  | 三   | san    | bottom longest, mid shortest, top med ✓ — soften end-discs |
| 04  | 十   | shi    | cross at center, shu slightly more below ✓ — soften end-discs on both strokes |
| 05  | 人   | ren    | 撇 longer + higher than 捺 ✓ — **fix 捺 taper direction (heavy lower-right tail)** |
| 06  | 八   | ba     | gap at top, no shared apex ✓ — **fix 捺 taper direction** |

Save each PNG as `attempts/cycle_4/<idx>_<char>.png`.

Your only inputs are `drawer_memory.md` and this brief. You will not
see the ground truths or the previous cycle's attempts.
