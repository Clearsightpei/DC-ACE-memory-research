# Success Bank — README — run_5

This is the **immutable code library** of mastered drawings.

- `INDEX.md` — queryable table of entries with tags.
- `code/<name>.py` — drawing module. Module docstring at the top
  carries all metadata (tags, mastered-cycle, judge numbers, reuse).
- `visual/visual_index.png` — grid of past wins.
- `_revoked/` — entries that were promoted under an older gate and
  no longer pass the current hard gate. Preserved for history. **Do
  not import.**

**Single writer**: the Curator. The Drawer reads but never writes.

**Hard mastery gate** (4-component, after c5+c8 reviews):

To promote an entry, the attempt must pass **ALL FOUR**:

1. **OCR identifies correctly**: `is_correct == true`.
2. **OCR margin**: `ocr_margin >= 0.3` (correct char is top-1, gap
   to next-best ≥ 0.3; or for single-prediction OCR, conf ≥ 0.3).
3. **`visual_score > 0.8`** (Dice + Chamfer + proportion vs GT).
4. **Judge panel unanimous YES**: 3 fresh-context skeptic
   subagents each see only the attempt PNG, GT PNG, and target
   char — must all say YES.

The Curator's own vision is informational only. The panel removes
the Curator's confirmation-bias leak that c5 exposed.

A single missing gate → carry-over, not promotion. Claude vision
alone is necessary but **not sufficient** — c5's revoked 人/入
promotions demonstrated that. The numeric gates (OCR + visual) act
as a check on the model's vision verdict.

**Renderer**: all current entries use `turtle.Turtle` (carried from
run_4 c1). The run_5 c1-c5 PIL renderer experiment is revoked.
