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

**Hard mastery gate** (after run_5 c5 review):

To promote an entry, the attempt must pass **ALL THREE**:

1. **OCR identifies the character correctly with confidence > 0.95.**
2. **`visual_score > 0.9`** (Dice + Chamfer + proportion vs the GT,
   from `tools/judge.py`).
3. **Claude vision** identifies the render unambiguously as the
   target character.

A single missing gate → carry-over, not promotion. Claude vision
alone is necessary but **not sufficient** — c5's revoked 人/入
promotions demonstrated that. The numeric gates (OCR + visual) act
as a check on the model's vision verdict.

**Renderer**: all current entries use `turtle.Turtle` (carried from
run_4 c1). The run_5 c1-c5 PIL renderer experiment is revoked.
