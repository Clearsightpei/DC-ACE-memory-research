<!--
Append-only history. Teacher adds one block per cycle. Do not edit
prior entries.
-->

## Cycle 1 — 2026-06-07

- Educational phase: 1 (atomic strokes)
- Focus: 横 (heng, horizontal stroke)
- Prerequisites: none (atomic).
- Cycle structure: **single phase** (no skeleton split for atomic
  strokes — see teaching_plan.md). Drawer renders brushed stroke
  directly; Curator scores vision rubric.
- Eval: `vision`. use_ocr=false.
- Why this focus: 横 is the most-used Chinese brush primitive;
  appears in 一/二/三/十 and inside hundreds of compound chars.
  It's the natural opening of Phase 1.
- Success Bank entries before: 0.

## Cycle 2 — 2026-06-07

- Educational phase: 1 (atomic strokes)
- Focus: 竖 (shu, vertical) — 垂露 (rounded-bottom) variant.
- Prerequisites: none (atomic).
- Eval: `vision`. Single-phase.
- Why this focus: second atomic stroke after 横. 垂露竖 is more reusable
  inside compound characters than 悬针竖; pick the universal first.
- Success Bank size before: 1 (横).

## Cycle 3 — 2026-06-07

- Educational phase: 1 (atomic strokes)
- Focus: 撇 (pie, 斜撇 diagonal-sweep variant).
- Prerequisites: none.
- Eval: `vision`. Single-phase.
- Why this focus: third atomic. First stroke with a TRUE taper-to-point
  (vs the symmetric barbells of 横/竖) — introduces the "tail to pensize 3"
  pattern needed for fine-tip strokes (also 提, eventually).
- Success Bank size before: 2 (横, 竖).

## Cycle 4 — 2026-06-07

- Educational phase: 1 (atomic strokes)
- Focus: 捺 (na, 斜捺 variant with flat-kick tail).
- Prerequisites: none.
- Eval: `vision`. Single-phase.
- Why this focus: fourth atomic. The right-diagonal counterpart of 撇,
  with REVERSED width profile (thin entry → heavy tail) and a
  distinctive flat-kick at the end. Pairing 撇+捺 unlocks 人/八/入/大/...
  characters in Phase 3.
- Success Bank size before: 3 (横, 竖, 撇).


## Cycle 5 — 2026-06-07

- Phase 1. Focus: 提.
- Same family as 撇 (tapered-tip), shorter (~250 px).
- Success Bank size before: 4.

## Cycle 6 — 2026-06-07

- Phase 1. Focus: 点. Last atomic.
- Different family — short, teardrop-shaped, both ends thin.
- Success Bank size before: 5.

## Cycle 7 — 2026-06-07

- Phase 2 (compound strokes) BEGINS. Focus: 横折.
- First compound stroke using the §1.5 two-segment pattern from c4.
- Success Bank size before: 6 (all 6 atomics).

## Cycle 8 — 2026-06-07
- Phase 2. Focus: 竖钩.
- Same two-segment pattern as 横折 but the second segment is a tapered hook (like 撇's tail family).
- Success Bank size before: 7.

## Cycle 9 — 2026-06-07
- Phase 2. Focus: 横折钩.
- Combines c7 (横折) + c8 (hook). Three segments per §1.5.
- Success Bank size before: 8.

## Cycle 10
- Phase 2. Focus: 竖弯钩. The 钩 family signature stroke.
- Three segments — first compound with a true CURVED middle segment (not a straight arm + sharp turn).

## Cycle 11
- Phase 2. Focus: 横撇.
- Two segments: short heng + 撇-tail (taper to point). Composes c3 (撇 family) with corner-顿笔.

## Cycle 12
- Phase 2. Focus: 竖折. Bottom-left L frame for 山/凶/区.

## Cycle 13
- Phase 2 LAST compound. Focus: 横折弯钩.
- 4 segments — composes c7 heng+turn + c10 curve+hook.

## Cycle 14
- Phase 3 BEGINS. Focus: 一. FIRST two-phase cycle (skeleton + brushwork).
- Prerequisites verified: 横 in Success Bank.
- Numeric heng target derived from graphics.txt: (-160,-100)→(+160,-100).

## Cycle 15
- Phase 3. Focus: 二.
- Composes 横 (×2) with translate/scale. Short top + long bottom convention.

## Cycle 16
- Phase 3. Focus: 三. Three-call composition of 横.

## Cycle 17 — 十. heng+shu intersection.

## Cycle 18 — 八. 撇+捺 separated (gap-top).

## Cycle 19 — 人. Same as 八 but 撇/捺 SHARE apex.
