<!--
Append-only history. Teacher adds one block per cycle. Do not edit
prior entries.
-->

## Cycle 1 — 2026-06-08

- Phase: 1 (1–3 stroke characters with unambiguous MMH GTs)
- Slate: 一, 二, 三
- Carry-overs: none (cycle 1)
- New picks: progression from 1→2→3 strokes, all 横-stacks, lets the
  Drawer establish the brushwork primitive (横 with `max(3, w(s))`
  width floor + 顿笔) and verify reuse across stacked variants.
- Why this slate: simplest possible MMH GTs (proper skeletons, not
  weak hand-coded strokes); single primitive (横) tested 1×/2×/3×
  so any width-floor / brushwork drift is visible immediately.
- Mastery audit of cycle 0: N/A (first cycle).

## Cycle 2 — 2026-06-08

- Phase: 1
- Slate: 一, 二, 三 (all carry-overs from c1)
- Carry-overs: 3/3 — Curator's strict-vision gate held in c1: vision identity passed but rubric < 7 because dunbi was inverted (bell-curve width profile peaked in the middle and tapered thin at the right end, which is the opposite of 楷书 收笔).
- New picks: none — devoting all 3 slots to fixing the brushwork before moving on. Quality over quantity.
- Why this slate: the c1 attempt vs GT visual difference was tiny but the brushwork inversion is exactly the kind of false-positive class run_5 is designed to catch. Re-attempt with corrected width profile (entry 16 → shaft 11 → closing 19) and the same composition.
- Mastery audit of cycle 1: vision-checked all 3 attempt PNGs vs GTs. All read as the target character; none passes the rubric gate.

## Cycle 3 — 2026-06-08

- Phase: 1 (continuing — introduce 竖)
- Slate: 十, 上, 下
- Carry-overs: none (cycle 2 promoted 3/3 — slate is all new picks).
- New picks: 十/上/下 all combine the mastered 横 primitive with a new 竖 primitive. 十 is the canonical 横+竖 cross; 上 puts 竖 at the top (above the long base 横); 下 puts 竖 below (the top 横 is long).
- Why this slate: leverages the c2-mastered heng + introduces a new primitive (竖) in three distinct positional contexts.
- Mastery audit of cycle 2: vision-checked all 3 attempts. All unambiguously the target. Width-fix worked; promoted.

## Cycle 4 — 2026-06-08

- Phase: 1 (continuing)
- Slate: 下 (carry), 干, 工
- Carry-overs: 1 (下) — c3 attempt failed because the 竖 pierced above the top heng (read as 十-with-dot); Sandbox specifies the structural fix.
- New picks: 干 (heng+heng+shu cross — three-stroke variant of 十), 工 (heng+shu+heng — 竖 spans between two hengs).
- Why this slate: tests the three positional patterns of 竖 vs heng (piercing / hanging / spanning) in three characters. If all three pass, the structural distinction is solid and the next cycle can introduce 撇 with confidence.
- Mastery audit of cycle 3: vision-checked all 3 attempts. 十 and 上 unambiguous; 下 ambiguous (reads as 十+dot, OCR confirmed). Promoted 十/上, carried over 下.

## Cycle 5 — 2026-06-08

- Phase: 1 (introducing 撇 + 捺 — the diagonal-sweep pair)
- Slate: 八, 人, 入
- Carry-overs: none (c4 promoted 3/3).
- New picks: three structurally distinct 撇+捺 compositions. These are the exact characters that produced the run_4 false positives (入 c20 visual 0.58, "ambiguous slash"). run_5 design point: the Drawer now SEES each GT and the Curator gate is strict-vision identity, not OCR. This cycle is the explicit test of whether the architecture fix solves the run_4 problem.
- Why this slate: 八 (gap between 撇 head and 捺 head), 人 (shared apex), 入 (捺 dominant + 撇 attaches as secondary). The structural distinctions are real and human-visible.
- Mastery audit of cycle 4: vision-checked all 3 attempts. 下/干/工 all unambiguous; the structural fix from c3 Sandbox worked first try on 下. Promoted 3/3.

## Cycle 6-8 — width experiments on 一/二/三 (post-reset)

After the user-imposed hard-gate reset (vision + OCR>0.95 + visual>0.9), I re-attempted 一/二/三 three times with different stroke widths to crack visual > 0.9:
- c6 brushed (run_4 width 11-19): visual 0.85/0.88/0.88, OCR conf 0.79/0.99/1.00.
- c7 thin uniform (width 3): visual 0.82/0.87/0.87, OCR conf 0.55/0.99/1.00.
- c8 band-matched (width 5): visual 0.83/0.88/0.88, OCR conf 0.43/1.00/1.00.

The Dice component caps at ~0.82 across all widths because anti-aliasing differences between turtle and MMH-postscript renders prevent pixel-perfect overlap. User then relaxed the gate to: OCR correct (any conf) + visual > 0.8 + vision unambiguous. Under that gate, all three c6 attempts pass.

## Cycle 9 — 2026-06-09

- Phase: 1
- Slate: 八, 人, 入 (the unfinished business)
- Why: 人 and 入 are the run_4 false-positive class. c5 attempts (PIL renderer) were revoked. Need to re-attempt with run_4 turtle 撇 + 捺 primitives and the relaxed gate.
