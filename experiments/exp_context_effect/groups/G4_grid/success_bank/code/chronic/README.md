# Chronic-cluster canonical primitives (position 300, B5→B6)

These are **hand-written pixel-perfect primitives** for the 5 items that
have failed at retry_n ≥ 2 across four batches (B2 through B5) despite
increasingly literal errata fixes:

- `pie_radical.py`  — standalone 丿 radical, TR9 anti-diagonal
- `dao_char.py`      — 刀 as a 2-stroke character
- `jiong_frame.py`   — 冂 enclosing frame
- `gong_bow.py`      — 弓 3-tier stack
- `ma_horse.py`      — 马 3-stroke horse

## Why they exist

Position-250 evidence (B4 → B5): the MANDATORY LOOKUP CHECKLIST moved
citation from 18% to 100% AND graduated three chronic retries (力, 冖,
凵). But B5 retries for these 5 items ALL failed again despite
literal-application-in-comments discipline. 丿 retry_3's docstring
cited the errata verbatim and then overrode it — "GT shows a more
vertical sweep." 马 retry_2 applied every rule in the errata (TR8
column-share, TR9 span, shu_zhe_zhe_gou reuse, hook up-left, N-gap
25 px), asserted invariants — and still failed the panel check.

Conclusion: **the retrieval-to-implementation gap is not the ceiling
for chronic items. The gap is between "what the errata prescribes"
and "what a canonical shape actually looks like."** These 5 items
lack canonical anchors in memory. Drawers keep inventing new anchor
plans and losing the panel test.

## Usage

Drawers reach these primitives via the normal `success_bank/INDEX.md`
grep. Each function has NO required arguments beyond `draw` — the
anchors are baked in and drawn onto a 300×300 canvas. Call:

```python
from chronic.pie_radical import draw_pie_radical
draw_pie_radical(draw)  # renders canonical 丿 into `draw`
```

If a drawer wants a slightly transformed version (e.g. 丿 as a
sub-component in a bigger character), they should NOT modify these —
they should inline fresh per TR6. These canned versions exist ONLY
for the standalone-radical / standalone-character task where the
canonical shape is the goal.

## What this changes

- Chronic items are **retrieval calls**, not design tasks.
- Panel-test the primitive ONCE (this batch); if it passes, all
  future attempts of that item PASS by definition.
- If it fails, the primitive is wrong — fix the primitive, not the
  errata note.

## What this does NOT change

- G4's 米字格 + P/T/N/S core (all anchors here are cell-based tuples).
- The mandatory-lookup checklist for all other items.
- The form_catalog / joint_atlas / principles_meta split.
