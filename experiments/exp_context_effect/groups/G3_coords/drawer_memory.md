# G3 free-form memory (created v8 @ position 350; first populated by B6 curator @ 2026-07-26)

*This is G3's free-form partner to the code bank. Write prose observations,
tables, and natural-language principles here — anything that doesn't
belong as a `def draw_<name>(...)` in the bank. Drawer reads this file
via `memory_index.md`.*

*Under v8, the code bank + principle files are REFERENCE ONLY. If what
you SEE in the GT contradicts a bank primitive or a principle — trust
GT. That single lesson (from B5's 丷 graduation) is now the top-level
posture: memory informs, does not compel.*

---

## Division of labor between memory files

- **`success_bank/code/*.py`** — the concrete storage unit. Each entry
  is a callable Python function that reproduces one mastered item.
  Signature is your choice (v8). Use these when a mastered item's
  shape matches yours (identity alias) or when you want a starting
  scaffold to modify.
- **`_shared_helpers.py`** — parameterized primitives (`variant_pie`,
  `variant_na`, `variant_dian`, `kiss_apex`, `pie_point`,
  `mirror_dian_pair`, tapered/bezier utilities). Use these when you
  need to draw a fresh stroke with tunable knobs, or when two strokes
  must share a computed pixel.
- **`form_catalog.md`** — indexed table of stroke × context with
  concrete numeric parameters (angles, widths, bow) from prior PASSes.
  Consult when you need "what widths do 撇 take in a 亻-left position?"
- **`principles_meta.md`** — TR1-TR7 (how to use the bank). REFERENCE.
- **`principles_stroke_family.md`** — P1-P12 (stroke-family knowledge:
  hook direction, math convention, ink thickness). REFERENCE.
- **`errata.md`** — per-item FAIL diagnoses + fix ideas. Check for the
  current item first if it or a close cousin has failed before.
- **THIS FILE (`drawer_memory.md`)** — free-form prose that doesn't
  code well: composition recipes as natural language, right-component
  playbooks, when-to-trust-GT lessons, sibling-pair notes.

---

## Composition playbooks (B6-derived)

These are patterns extracted from B6 passes/fails where the code bank
alone was insufficient but a short prose recipe works.

### 亻 + right-component (5-stroke chars)

**Left is easy: `ren_pang` at `ox=-45, scale=0.55` always works.**

The failure cluster in B6 (化, 他, 仔, 仕, 仗, 仞 all FAILed; 付 PASSed
only by inlining fresh) is entirely on the right. The right components
that fail:

- **匕 (in 化)** — 匕 has no bank primitive. When drawing, place a short
  descending 撇 whose tail lands ON the top of a 竖弯钩 shaft (not
  above, not below — ON). See sandbox "p2_radical_011_匕 GT" note for
  the joint geometry.
- **也 (in 他)** — do NOT compose 3 primitives (横+竖+竖弯钩); the
  envelope MUST be one continuous 竖弯钩 shape with a heng and shu
  inserted through it. Inline fresh, do not use `shu_wan_gou` at
  radical scale.
- **子 (in 仔)** — call `zi_char` from bank #122 at scale 0.65 with
  ox=+40. This is a proven identity path; drawers who invent a fresh
  子 recipe on the right lose.
- **士 (in 仕)** — two hengs (top short, bottom slightly wider) with a
  central shu passing through. No bank primitive. Inline as
  `_thin_heng` × 2 + `_thin_shu`, all at W=5 (P12).
- **丈 (in 仗)** — MUST have a top 一 (short heng around y=+80).
  Without it, the character reads as 乂. The top heng is the sole
  distinguisher.
- **刃 (in 仞)** — 刀 with a dot at the hook shoulder. Start from
  `dao_pang_char` (bank), add a small `variant_dian` at the corner.

**Recipe to bookmark**: `men_plural.py` (bank #174) is the cleanest
example of 亻 + bank-right composition — 亻(ren_pang, ox=-45,scale=0.55)
+ full-right (men_char, ox=+50, scale=0.55). When the right IS a bank
primitive, copy this ox/scale pair verbatim.

### L-R composition scale table (from B6 PASSes)

| Char | Left component | Right component | L scale | R scale | L ox | R ox |
|------|----------------|-----------------|---------|---------|------|------|
| 们   | ren_pang       | men_char        | 0.55    | 0.55    | -45  | +50  |
| 对   | you            | cun             | 0.65    | 0.75    | -40  | +30  |
| 打   | shou_pang      | ding_char       | 0.80    | 0.75    | -60  | +50  |
| 付   | (inline 亻)    | (inline 寸)     | –       | –       | –    | –    |
| 外   | xi             | (inline 卜)     | 1.0     | –       | –    | –    |

Pattern: L-R chars split roughly 40/60 with L at 0.55-0.80 and R at
0.55-0.75. Rarely does one side need to exceed 0.80 in a 5-stroke
compound. Bigger scales overflow into each other's territory.

### Box-based chars (甲/申/由/田 family)

- **申 (PASSed as `shen_extend`)** — box in middle band (x=85..215,
  y=100..210) + central 竖 protruding above (top ~y=30) and below
  (bot ~y=280). One interior heng at box midheight. This is the
  reference recipe.
- **甲 (PASSed as `jia_first`)** — box in upper (y=55..175) + interior
  heng + long central 竖 extending down to y=285. Recipe differs from
  申 mainly in vertical extent below (甲 extends much further).
- **甴, 田 (甴 FAILed in B6)** — same family, need to observe GT for
  interior heng count and position. Bank pattern for 申/甲 is the
  starting point.

### Top-cap + body chars (亠/宀/十 tops)

- Small dots on top of a heng (as in 主, 平, 兮, 尹): **dots MUST sit
  ABOVE the heng, not hang from it as descending strokes**. B6's 平
  failed because the drawer drew descending slashes instead of tiny
  perched dots. Use `variant_dian` with w_head=6, w_tail=3 sitting at
  y ≈ heng_y + 20 with small horizontal spread ±10.

### Envelope + interior (风/勿/勻 family — 3 PASSes in B6)

- Use `bao_char` (勹 envelope) as the envelope layer, then draw
  interior strokes inside the envelope's opening.
- 勻 recipe: `bao_char` + 2 thin interior hengs at x=110..195.
- 勿 recipe: `bao_char` + 2 long interior 撇 sweeping down-left.
- 风 recipe: this one uses `variant_pie` for the left leg + inline
  envelope + interior 乂 (variant_pie + inline na). Envelope must be
  ONE continuous stroke; drawing it as heng + shu + hook produces
  right-angle corners that don't read as 风.

---

## When to trust GT over the bank / helpers (B5 lesson, still binding)

The single retry PASS across B5+B4+B3 that came from EITHER graduation
(丷 in B5) passed by explicitly REJECTING its recommended helper. The
principle:

- If the GT you see contradicts the recommended helper's abstraction —
  believe GT. Example: `mirror_dian_pair` assumes symmetric dots; if
  the GT shows asymmetric dots, draw them asymmetric.
- If the bank primitive's shape doesn't match your composition at
  simple uniform rescale — inline fresh with the width/taper knobs.
  Do NOT force-fit the primitive with an extreme (ox, oy, scale).

Under v8, this posture is codified: memory is reference, not command.
The drawer is a first-principles renderer that CONSULTS memory, not
an executor of it.

---

## Sibling-pair observations (natural-language)

- **化 / 花 / 华** — all use 匕 or a 匕-like right component. Solve 匕
  first (inline recipe per errata) before attempting these compounds.
- **仔 / 孑 / 孓 / 子 char** — 子-family shares one recipe (bank #122,
  `zi_char`). Different insertions/mirrors matter — 孓 mirrors 子's
  提 direction. Not all 子-shaped chars can identity-alias, but 仔 CAN
  (right-side identity + 亻 left).
- **甲 / 申 / 由 / 田** — box-family with varying protrusion count and
  direction of the central 竖. Recipes differ by 1-2 lines.
- **仕 / 仝 / 仞 / 仔 / 仗** — 亻-family: 亻 is easy (see above),
  right is the game.

---

## What curator will NOT do here

- No item-mastery claims for un-judged items (drawer already forbidden
  to write these; curator repeats the constraint here for symmetry).
- No hard rules — only prose recipes and observations.
- No "you MUST use helper X" — v8 principle: helpers are reference.

If a hard rule emerges from a pattern (e.g. "dots ABOVE heng, not
descending"), promote it to `principles_stroke_family.md` as a P-*
principle. Prose here is for cases that don't crystallize as a rule.
