# Principles — Meta-Cognitive Transformation Rules (G4)

*Split out of the old 429-line principle_bank.md at position 150 (batch B2).
This file holds ONLY the meta-cognitive TRs — when to use the bank, how to
transform primitives, how to sanity-check anchors. Joint conventions moved
to `joint_atlas.md`. Per-stroke × per-context form knowledge moved to
`form_catalog.md`. See `evolution.md` for the split rationale.*

**Read this file FIRST every cycle before touching a primitive.** Then
consult `form_catalog.md` for the specific stroke × context you're
about to draw. Consult `joint_atlas.md` only when a joint class or
P/T/N gap decision is uncertain.

## TR1 — Every primitive call must supply NEW anchor tuples

Bank primitives are defined for STANDALONE use with anchors spanning the
full 米字格. To reuse one inside a composed radical/character you MUST
override its default anchors. Never call a primitive with defaults inside
a composition.

Before calling ANY bank primitive, answer three questions:
1. Which cells should its head/tail land in?
2. What x_frac/y_frac inside those cells?
3. What width — component strokes are usually thinner than standalone
   (default × 0.7–0.85)?

If you can't answer all three, don't call the primitive — inline instead.

## TR2 — Radical-position anchor conventions

Component role → typical cell span (relative to standalone which fills TL→BR):

| Role         | Cells span                       | x_frac        | y_frac        |
|--------------|----------------------------------|---------------|---------------|
| Left radical | TL/ML column → BL/ML column      | 0.10–0.60     | full          |
| Right radical| TR/MR column → BR/MR column      | 0.50–0.90     | full          |
| Top radical  | TL/TC/TR row                     | full          | 0.00–0.40     |
| Bottom       | BL/BC/BR row                     | full          | 0.60–1.00     |
| Enclosing    | all cells (leave ~5% edge margin)| 0.05–0.95     | 0.05–0.95     |
| Standalone   | fills full 米字格                 | at cell edges | at cell edges |

## TR3 — Cell selection IS the transformation

G4 has no `ox/oy/scale` — moving a primitive means CHOOSING DIFFERENT
CELLS for its anchors. Want it right? Head goes in TR column instead
of TL/TC. Want it lower? Use B* row.

## TR4 — Joint enforcement via shared anchor tuples

When two strokes should weld (P) or share a tip (T):
- Compute the shared anchor tuple explicitly.
- Pass it verbatim to both primitives.
- Don't pick anchors independently and hope they land close.

## TR5 — Scale via anchor SPAN, not a scale parameter

Smaller = shorter anchor span. To shrink: move head anchor's fracs
closer to tail's, or fit into fewer cells.

## TR6 — If a primitive doesn't fit, INLINE the recipe

Signs to inline instead of override:
- Composition needs a joint class not in the primitive's spec.
- Primitive's internal curve/bezier control is baked to defaults and
  doesn't rescale cleanly.
- Anchors would fall outside the primitive's expected cells.

When inlining: copy the rendering code into `generated.py`, adjust
anchors + hardcoded constants, add a joint-spec comment. This
preserves the shape idiom while allowing per-item tuning.

**B1+B2 empirical**: successful attempts consistently either (a) used a
1画-wrapper primitive with cleanly overridden anchors, or (b) inlined
the stroke fresh. Attempts that force-fit a 3+画 primitive into a
composition it wasn't designed for tend to fail.

## TR7 — Every composition documents its anchor plan BEFORE render

Write a comment block naming every stroke's head/tail cells + fracs +
width, plus joint class per pivot. Bare `draw_pie(draw); draw_shu(draw)`
= guaranteed failure on any non-十 composition.

## TR8 — Sanity check anchors before render

Before `python3 generated.py`:
1. For each stroke, is head anchor pixel-above/left of tail (or wherever
   direction demands)?
2. For each expected joint, are the two anchors IDENTICAL (weld) or
   within 0.15 x_frac/y_frac (N-class small gap)?
3. Do all anchors sit inside the 米字格 (fracs in [0,1])?
4. If a primitive has internal geometry constraints (e.g. `shu_gou`
   requires `belly.x == head.x` for straight body), verify anchors
   satisfy them. If not, OVERRIDE or INLINE. Do NOT render with
   known-broken input (刂 lesson).
5. **Every 横**: both endpoints share the same cell ROW (T*, M*, or
   B*). Mixing rows tilts the "horizontal" by 100 px → renders as
   diagonal (彐 lesson).
6. **Every 竖**: both endpoints share the same cell COLUMN (*L, *C,
   or *R).

## TR9 — MMH anchors are a FLOOR for standalone radicals

MMH stroke-median data is derived from character glyphs; radicals-as-
components rarely fill the 米字格. For a STANDALONE Phase-2 radical,
expand MMH anchors to full-grid span:
- 丿-family: head ('TR', 0.85, 0.15), tail ('BL', 0.15, 0.85)
- 一-family: head ('ML', 0.10, 0.5), tail ('MR', 0.90, 0.5)
- 丨-family: head ('TC', 0.5, 0.10), tail ('BC', 0.5, 0.95)
- 乚-family: head TC/upper, tail reaches BR
- Enclosing (口, 门, 囗): all fracs 0.05–0.95

Verbatim MMH = fine for Phase 3 characters; UNDER-SPANS for standalone
Phase 2. **B2 confirms**: 囗 PASSed only with TR9 expansion (0.15→0.90);
门 retry PASSed after clamping ALL three strokes into the enclosing
frame.

## TR10 — N-class joints must LOOK connected (pixel proximity ≤ 25 px)

"Natural gap ~15–20 px" ≠ "strokes visually independent." Verify
pixel distance between the two N-endpoints is ≤ 25 px. If MMH gives
anchors in different cells producing >30 px gap, override to
near-weld: share the anchor tuple exactly (upgrade to T) or place
both in the SAME cell with fracs within 0.15.

Failure mode if you don't: character fragments visually.
Bootstrap 厂 and 刀 both failed by treating N as literal separation.

## TR12 — Same-row horizontals, same-column verticals

Already merged into TR8 rule 5+6 above. Kept as a named rule for cross-
reference in older sandbox notes.

---

## Retired rules (kept as historical context)

### TR11 (RETIRED at position 150) — SELF_CHECK.visual_ok "must be earned"

Original rule: name TWO SPECIFIC visual agreements between rendered PNG
and GT before setting `visual_ok=True`.

**Why retired**: B1 cross-tabulation showed TR11-compliant SELF_CHECKs
had 63% pass rate vs 74% for non-compliant. TR11 compliance did NOT
correlate with human pass. Retries skipped TR11 entirely and still
hit 4/6 on B1 (mechanical errata-fixes carried them). Naming
agreements is honest labor but is neither necessary nor sufficient
for the human-PASS gate.

**What replaces it**: honest self-diagnosis — if you notice a specific
mismatch (wrong span, wrong joint class, missing curve), log it in
`sandbox.md` and either revise or submit with `overall_pass=False`.
Do NOT rubber-stamp `overall_pass=True` when you know it's off. The
positive calibration cases (犭, 彐 bootstrap) show submit-and-flag
is the right move when the render doesn't come out.

## Bank is supplementary, not mandatory

Success + Principle bank are *supplementary* memory, not a required
call-graph. When a primitive fits the composition cleanly (correct
joint class, anchor flexibility, taper), use it via TR1–TR8. When it
doesn't, inline (TR6). Cognitive budget is finite — don't wrestle a
primitive into a shape it wasn't built for.
