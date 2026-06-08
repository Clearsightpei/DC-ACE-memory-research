<!--
This file is owned by the Teacher role (.claude/skills/teacher/SKILL.md).
It is the Teacher's pedagogy: what to teach, in what order, why, and how
that strategy is evolving in response to what the Drawer has done.

No human has seeded this file. The Teacher writes it from scratch on
cycle 1 and revises it freely thereafter.
-->

# Teaching plan — run_4 (three-bank-memory era)

## Ultimate goal

Teach the Drawer to draw the best Chinese characters possible — same
goal as run_3, but with a redesigned memory architecture, two-phase
(skeleton → brushwork) drawing, and **one focus character per
cycle** instead of 6-per-batch.

## Why this run exists

`runs/run_3/POSTMORTEM.md`: run_3 hit a composition-precision wall
on ~3 OCR-boundary characters (也/寸/万) and the memory file grew
into a 250-line error log that slowed transfer rather than
accelerating it. Six architectural changes for run_4:

1. Three-bank memory (Success Bank A / Principle Bank B / Sandbox C).
2. Visual anchor cards — Drawer sees its own past wins.
3. Skeleton → brushwork as two phases; skeleton compared to GT by
   Curator (GT *is* skeleton — no brushwork to leak).
4. Component-tagged Success Bank with query-by-tag.
5. Drawer self-preview (max 2 internal iterations before commit).
6. One focus character per cycle, with Teacher-enforced prerequisite
   check.

## Pedagogy

### One focus character per cycle

Each cycle teaches ONE atomic stroke, 部首, or character. The cycle
ends when either:
- the focus is mastered (added to Success Bank), OR
- the focus needs a prerequisite first (Teacher abandons + switches
  next cycle's focus to the missing prerequisite), OR
- 3 consecutive cycles on the same focus all fail; the Teacher then
  promotes a contrastive principle to Principle Bank §3 and tries
  an adjacent approach next cycle.

### Prerequisite verification (mandatory before introducing a character)

Before introducing a character, the Teacher must verify ALL its
component primitives are present in the Success Bank. Example
chain for 天:

```
天 = 二 + 人
二 = 横 (×2)
人 = 撇 + 捺
横, 撇, 捺 = atomic strokes (Phase 1)
```

If a prerequisite is missing, the Teacher MUST switch the focus to
the missing prerequisite. The Drawer is never asked to compose from
unmastered parts.

### Phase progression (revised)

| Phase | What is taught | Mastery gate |
|-------|---------------|--------------|
| 1     | Atomic strokes: 横, 竖, 撇, 捺, 提, 点 | rubric ≥ 7 no 0 |
| 2     | Compound strokes: 横折, 竖钩, 横折钩, 竖弯钩, 横撇, 横折弯钩, 竖折, ... | rubric ≥ 7 no 0 |
| 3     | Single-component characters (1–4 strokes): 一, 二, 三, 十, 人, 八 | is_correct AND conf ≥ 0.4 AND rubric ≥ 7 no 0 |
| 4     | Multi-component characters using Success Bank parts: 大, 木, 林, 火, ... | same |
| 5     | Complex compositions | same |

Phase boundaries are soft and Teacher-judged.

## Mastery checklist

(Empty — built up as run_4 progresses. One row per Success Bank entry.)

| item | phase | success_bank file | first mastered cycle | component tags |
|------|-------|-------------------|----------------------|----------------|

## Carry-over / no-skip rules

- `is_correct == false` OR `ocr_confidence < 0.4` forces carry-over.
- "OCR-wall" is not a valid retirement label.
- Strict rubric (any criterion 0 → fail).
- 3-attempt rule: if the same focus fails 3 cycles, write a
  contrastive principle to Principle Bank §3 before attempt 4.
