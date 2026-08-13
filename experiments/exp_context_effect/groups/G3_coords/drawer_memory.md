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

## B7 addition (2026-07-27): the V9 visual-diff recipe

Three retries GRADUATED in the B7r rerun (大, 主, 疒) — the first non-trivial
retry lift in five batches. The recipe extracted from their generated.py
headers is:

**Step 0 — open the prior failed PNG next to the GT.** Not paraphrase from
errata; actually look. In every one of the three passes the drawer's
`VISUAL DIFF` block named THREE OR MORE specific pixel-level gaps
(dot direction, heng-width ladder, apex-vs-crossing position, taper
weight, shoulder-blob artefact). Without this block the retry falls
back to re-imagining the character, which is what happened under v8
prompt and produced 0/10 PASS.

**Step 1 — enumerate the gaps as concrete `(what prior did) vs (what GT shows)`
pairs.** Example from 主's pass:
```
Gap 1: prior 丶 leans lower-left→upper-right; GT 丶 leans upper-left→lower-right.
Gap 2: prior heng widths are flat + step; GT is a graduated ladder.
Gap 3: prior shu over-extends above top heng; GT starts AT top heng.
Gap 4: prior dot-to-heng gap is 27-45px; GT gap is ~15px.
```

**Step 2 — REJECT baked-in bank/helper abstractions that contradict GT.**
All three passes explicitly rejected something:
- 大 rejected `kiss_apex` (helper's apex-above-heng vs GT's apex-in-heng).
- 主 rejected the "descending dots" reading and switched to canonical 点 lean.
- 疒 rejected `draw_guang` (bank primitive's aggressive taper made the
  envelope descender invisible).

**Step 3 — inline fresh at MMH-thin ink (P12) with the fixes.**

The 7 rerun FAILs also produced excellent visual diffs; they just couldn't
translate the diagnosis into a hand-render that passed judgment. That is a
DIFFERENT failure mode (execution ceiling, not diagnosis ceiling) — and
one worth naming separately in scan/evolution: **for hard cursive items
(马, 人, 入 X-crossing) the callable-Python line-primitive vocabulary is
the binding constraint, not the drawer's perception**.

### Notable pattern surfaced by B7 mains (34 FAILs)

Looking across the fails, **the X-crossing family recurs at position-scale**:
矢, 失, 乔, 会, 兵, 天, 夹 all fail on the same apex-vs-heng geometry that
大 fails on. This is not a memory gap (drawer_memory has playbooks) — it
is that ONE PIL line-segment can't render the "curved-pie continues
through the heng crossing while na starts fresh at that pixel" topology
without a bezier + width-taper. When 大 graduated in B7r it was via a
hand-rolled tapered bezier, not a helper call.

**Retry priority under this observation (positions 401-450)**: the
X-crossing family is now KNOWN-SOLVABLE if the drawer follows the 大 recipe.
Add 矢/失/乔 to the B8 retry queue as first-round candidates, with an
explicit pointer at 大's bank entry as the template. Do NOT re-add 人/入
— they hit the ceiling again on rerun despite correct diagnosis.

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


---

## B8 addition (2026-07-27) — dominant B8 fail modes + recipes

**B8 main pass rate: 9/50 = 18% (worst yet).** Below G1 control by
~30 pp. The item pool at positions 401–450 is dense with 亻-compound
Phase-3 chars whose RIGHT-SIDE sub-radical is not yet in bank.

### The single dominant B8 fail mode: 亻 + unsolved-right-sub-radical

**19 of 41 fails** are 亻+X where the X is a sub-radical we haven't
mastered:
- **匕-family** (仳, 比, 化, 花, 老-bottom, 匕 itself) — 匕 now
  TERMINAL_FROZEN after retry_5. **Give up on 匕 as a bank primitive**;
  when a compound needs it, inline TWO thin lines that resemble the
  匕's 撇 + hooked shu. Do NOT try mirror_dian_pair or a helper —
  they don't render.
- **也-family** (她, 他, 池, 驰) — 也 has no bank entry. Inline as:
  横折钩 (top+right+small hook) + inner 竖 + horizontal-with-tick.
  Keep uniform thin ~5px; don't try envelope-with-curve.
- **戈-family** (成, 伐, 戈) — 斜钩 is the arc. Inline as long
  slightly-curved diagonal + top 一 + inside-crook 撇 + dot. The arc
  requires a tapered bezier, NOT a straight line.
- **X-crossing right side** (伕=夫, 伙=火, 次=欠) — same 大-family
  ceiling. Apply da_char recipe (bank #201): continuous 撇-curve above/
  through 一, separate 捺 from crossing pixel.
- **牙/尹/弔/支/瓦/为/壬 rights** — each unique; no shortcut. Inline
  ~5-stroke primitives from GT observation.

### Second cluster: mirror-symmetric splay (亚, 亦, 齐, 兆)

4-arm outward mirror splay is a NEW pattern in B8 that has ZERO bank
support. Do not try to compose from bank ba (八) — the splay is
4-arm not 2-arm. Inline recipe:
1. Central shaft (vertical) as anchor.
2. Two upper-outer arms mirror-slanting outward AWAY from shaft.
3. Two lower-inner arms shorter, mirror-slanting AWAY too.
Widths thin 4-5px per P12. Positions symmetric around shaft x.

If this cluster recurs in B9, promote a mirror_splay helper to
_shared_helpers.py.

### The 兇 recipe (B8 entry #212) — reject-bank-for-weight

**兇 PASSED** by fully inlining 8 strokes with uniform thin 5px INK,
EXPLICITLY rejecting bank er_ren (which is calligraphically heavy).
Same pattern as B7 v9 graduates (大 rejected kiss_apex, 主 rejected
descending-dots, 疒 rejected guang's taper).

**Reject-bank-for-weight rule**: when GT is MMH-style thin uniform,
bank primitives with calligraphic embellishment (heavy taper, blob
shoulder, wide na-flare) will always LOSE the panel judgment. Prefer
inline PIL with thin 4-5px widths over the bank primitive in that
context. This applies most strongly to:
- er_ren (儿) — too heavy for chars like 兇, 先, 兆.
- kiss_apex family — apex-above-heng needed for 大-family.
- guang (广) — taper too aggressive for MMH-style 疒.
- Any 捺 primitive with calligraphic flare — for thin GTs, hand-render.

### Compound-with-frame-and-interior recipe (from B8 回 PASS)

回 PASSED via pure identity-alias composition: `wei_radical` outer
at scale 1.0 + `kou` inner at scale 0.55, oy=+5. **When BOTH frame
AND interior have bank mastered aliases, and the interior is scaled
around ~0.5 of the frame, identity-alias composition works.** Extend
this recipe to 困/囚/因/园 in the upcoming curriculum.

### Retry-channel finding — v9 diminishing returns

**B8 retries 0/7 under v9 prompt.** All 7 wrote correct visual diffs,
diagnosed prior-attempt gaps correctly, and STILL couldn't cross the
panel. The 3 v9 graduations in B7r (大, 主, 疒) look increasingly
like a one-time effect on items whose prior PNG had easily-namable
visual gaps. On genuinely hard items (X-crossing, apex-kiss, 匕-family)
even correct diagnosis doesn't translate to a passing render.

**v10 change coming (B9)**: retries will see the FULL attempt
trajectory — every prior attempt (including any past PASSes labeled).
This may help on items like 仔 (which has past 子 PASS in bank #122)
where the drawer previously inlined instead of calling zi_char. For
items whose only trajectory is "3 different-flavored fails," v10
probably won't help either.

### What to watch in B9 (positions 451–500)

- 亻-family density stays high — see if v8 posture (bank composition
  for the L, inline for the R) continues at ~50% recovery.
- Check for mirror-splay repeat (亚 family) — promote a helper if 3+
  more occur.
- Under v10 trajectory-view, retries with a bank ancestor (仔 → zi_char,
  平 → main-line renderer) may finally graduate.


---

## B9 addition (2026-07-30) — code-format ceiling diagnosed, retrieval leak identified

**B9 pass rate: 14/50 = 28%. Zero A verdicts.** G4 same-batch: 40% + 11 A.
G3 vs G4 gap is now measurable and structural, not stochastic.

### The code-format ceiling (finally named)

G3's `def draw_<name>(t, ...)` + PIL line/bezier primitives operates at
the LINE layer. G4's 米字格 anchors + P/T/N/S joint specs operates at
the STROKE-JOINT layer — closer to how a Chinese-calligraphy judge sees
a character. Judges reward joint modulation, ink taper at brush lift,
and where two strokes weld pixel-share; PIL rasterisation of two
line-segments meeting at a computed vertex does not produce this
signature no matter how carefully the vertex is computed.

**What this means for the drawer**: the ceiling on A verdicts is
STRUCTURAL to the format, not to your effort. Continuing to hand-tune
tapered_bezier widths chasing "calligraphic weight" past 4-6 px INK
does not translate into panel A verdicts (see B7 v9 graduations 大/主/疒
— none earned A, only PASS). Do not spend cycles hand-tuning below the
already-thin MMH width; spend them on structure.

### What IS still winnable — priority order for B9+ compositions

Rank each B10 item you see against this list; the earlier the rank,
the higher the historical hit rate.

1. **Bank-part + bank-part identity-alias L-R composition.** Both left
   and right components have a `.py` in `success_bank/code/`. Copy the
   scale table verbatim (see drawer_memory L-R table).
   *B9 exemplars: 佃 (亻 + inline 田), 但 (亻 + 旦), 佇 (亻 + 宁),
   佐 (亻 + 左), 伯 (亻 + 白), 甸 (勹 + 田), 町 (田 + 丁 via ding_char),
   作 (亻 + 乍).*

2. **Bank envelope + bank interior.** 辶/勹/囗/门 + a bank-mastered
   inner component. *B9 exemplars: 这 (辶 + wen bank), 进 (辶 + 井
   inline that reads clean), 甸 above.*

3. **Bank-radical + inline 5-stroke right.** Only if the 5-stroke right
   is COMPACT geometry (box, 3-line stack, single dominant vertical).
   *B9 exemplars: 亩 (亠 + 田 inline), 里 (田-like + 土-like stack).*

4. **Fresh compositions with clear symmetry / repetition.** *B9 exemplar:
   光 (⺌ + 一 + 儿 all inline; xiong-family reject-bank-heaviness recipe
   from B8).*

**DO NOT SPEND CYCLES ON:**
- 大-family X-crossing (伶, 伾, 我, 来, 更, 305_还, 289_我, 293_来 all
  failed in B9 despite v9 recipe available; format ceiling confirmed
  across 2 batches).
- Mirror-splay 4-arm (亦, 齐, 兆, 亚, 丽 in B9). No PIL recipe reads.
- Cursive envelopes with interior curls (身, 乌, 巴). No bank; inline
  degenerates.
- TERMINAL sub-radicals (匕, 也, 厶, 讠, 丬, 夂, 力, 巾, 斤, 巴). If
  compound needs one, expect FAIL.

### The composition-retrieval leak — B10 retry priority

**5 B9 fails had ALL PARTS BANK-MASTERED but the drawer inlined fresh:**
- **295_时** — bank ri (日) + bank cun (寸). Inlined 寸 lost the hook.
- **296_串** — bank kou ×2. Boxes too small (0.42 scale) — shu didn't
  protrude visibly.
- **304_疖** — bank ne_sick (疒) + bank jie_radical (卩). Inlined 卩.
- **306_亨** — bank tou_char (亠) + bank kou + bank liao (了). All bank
  but stacked proportions wrong.
- **315_声** — bank shi_male (士) + bank shi_radical (尸). Proportions.

These are HIGH-VALUE B10 retry candidates. Under v10 trajectory-view,
seeing the past PASS PNGs of ri.py/cun.py/kou.py/ne_sick.py/jie_radical.py
should surface the right identity-alias call pattern. If any of these
graduate on retry, the drawer memory is working; if none do, the
retrieval leak is deeper (drawer is choosing inline over bank-call even
when both are available).

### B9 recipe additions to the L-R scale table

Extending the drawer_memory L-R table with B9 confirms:

| Char | Left | Right | L scale | R scale | L ox | R ox | Recipe |
|------|------|-------|---------|---------|------|------|--------|
| 佃   | ren_pang (bank) | 田 (inline) | 0.55 | – | -45 | +30 | box + interior cross |
| 但   | inline 亻 | inline 旦 | – | – | – | – | 亻 hugs left third; 日 upper + 一 spans full right |
| 佇   | inline 亻 | inline 宁 | – | – | – | – | 宀 (bao_gai_tou) top + 丁 (ding_char) bottom on right |
| 伯   | inline 亻 | inline 白 | – | – | – | – | 亻 top-pie + shu kiss; 白 = 撇 + 3-line box |
| 佐   | inline 亻 | inline 左 | – | – | – | – | 亻 + heng-pie top + 工 bottom |
| 作   | inline 亻 | inline 乍 | – | – | – | – | 亻 + short-pie-heng top + shu + 2 hengs |
| 町   | 田 (inline) | ding_char (bank) | – | 0.75 | -30 | +50 | frame_L + bank ding_char |
| 甸   | bao_char (bank) | 田 (inline) | 1.0 | 0.60 | – | – | envelope + interior box |

**Pattern**: when the LEFT is a 亻/亠/勹/辶/扌 with a bank alias,
using the bank primitive works. When the RIGHT is a 田/口/丁 with a
bank alias, calling the bank primitive works. The B9 5-item retrieval
leak all failed the RIGHT-side bank call.


---

## B10 addition (2026-07-31) — v13 BANK_DEVIATION channel is live + retrieval-leak partial fix

**B10 pass rate: 12/50 = 24% mains, 2/7 retries. Zero A across 500 items.**

### v13 BANK_DEVIATION works — here's when to use it

**Rule of thumb (from 16 B10 deviations, 3 PASS)**: skip a bank primitive
when its absolute pixel coords can't shrink into your composition slot
AND you can name a known variant shape as replacement. Do NOT skip
merely because you don't like the bank's aesthetic — you'll lose the
identity-alias advantage.

**PASS-with-deviation recipe (from 皃, 畀, 的)**:
1. Name the exact bank file you're skipping and the exact reason
   (width overshoot, absolute-coord conflict, shape mismatch).
2. Sketch the fresh_component with a short one-line name
   (`bai_compressed_for_de`, `bi_field_over_ji`, `bai_top_for_stack`).
3. Inline PIL at thin (5-9px) uniform widths. Do NOT add calligraphic
   embellishment when the deviation is for size/placement.
4. Self-check: does the fresh render fit the slot without overlapping
   its sibling component? If yes, submit.

**FAIL-with-deviation recipe (from 疌, 甾, 改, 疙, 找 etc.)**:
When you deviate for a NEW shape (聿, 巛-scoop, 己, 乞, 戈) that isn't
in the bank AND you don't have a variant example, the fresh render
often fails. In those cases:
- Check `pass_index.md` for any past attempt that drew a similar shape
  (even in a different compound context).
- If none found, warn yourself in the header — you're taking a risk.

### New bank variants added this batch (v13 promotion policy)

- **`bai_char_compressed_for_LR.py`** — 白 at 80px width, left of a
  right component. Motivating context: 的. Use for 帕/皎/皖.
- **`bai_char_for_top_stack.py`** — 白 in top half of canvas.
  Motivating context: 皃. Use for 貌/皂/皇 (any 白-atop-radical).
- **`er_ren_for_bottom_stack.py`** — 儿 spread wide across y=155..288
  with thin 6px ink. Motivating context: 皃. Use for 兒/兄/光/見 (any
  儿-below-radical). This is the "reject-bank-heaviness" family — same
  lesson as 大/主/疒/兇.

**Originals untouched**: `bai_char.py`, `er_ren_char.py` still work
for their original contexts (standalone-radical size).

### Retrieval-leak partial fix (v13 explicit-bank-call)

The B9 leak analysis identified 5 items where "all parts bank-mastered
but drawer inlined fresh." In B10 retry, 2/5 GRADUATED:
- **时** — bank ri (日) + bank cun (寸). PASSed on retry.
- **串** — bank kou × 2 stacked with tall shu. PASSed on retry.

The other 3 (**疖**, **亨**, **声**) FAILed retry despite bank-call
instructions. Pattern: leak-fix works when composition is
side-by-side (时) or stack (串), fails when composition needs proportion
tuning (亨 needs vertical-3-stack with 亠 small / 口 medium / 了 large;
疖 needs narrow-column 疒 + narrow-column 卩; 声 needs士-top + 尸-envelope
proportion).

**Lesson**: bank-call instruction alone isn't enough; the drawer also
needs proportion guidance for stacks-of-3+ and narrow-column layouts.

### Errata additions to know for B11

- **X-crossing on retry_3** (矢, 失): both at retry_3 fail. In B11 they
  hit retry_4 (last-chance-before-freeze). Use da_char recipe (bank
  #201) as template — continuous pie curve above/through heng.
- **C-attempt targeted retries**: 志 (tighten 卧钩), 盯 (widen 目 +
  shorten 丁 heng), 甾 (curl 巛 tails + add gap), 和 (thin 禾 pie/na +
  tighten 口), 法 (larger 氵 dots + linked 厶).

### Content-gap items to notice in B11 mains

- 亻 + [它, 弗, 句, 女, 冬, 佥, 亭] — right sub-radicals unmastered.
- 讠, 攵, 弋/戈, 乞, 己, 巳-variants, 疋 — all unmastered sub-radicals.
- Cursive/curly primitives (虐, 万, 少, 忐, 忒 tops) — no bank primitives.

### The zero-A observation

**500 items, 10 batches, 0 A verdicts.** G4 has multiple A. G3's
PIL-line-primitive can produce PASS-tier compositions but the panel
distinguishes "recognizable" from "calligraphically beautiful" — and
line primitives can't cross that threshold. Do not spend cycles
hand-tuning stroke widths past the 4-9px MMH band chasing A. Prioritize
compositional correctness (right recipe, right slot proportions) —
that keeps you in PASS band. If a variant demonstrably improves PASS
rate, promote it; if a variant only improves aesthetics without moving
the panel verdict, don't bother.

---

## B11 addition (2026-08-03) — v13 channel steady; 4 new variants; zero-A confirmed

**B11 main pass rate: 14/50 = 28% (up from B10's 24%; best G3 since B9's 28%).
Retry: 0/5. Cumulative through 550: ~44%. Zero A across 11 consecutive batches.**

### 4 new bank variants promoted (v13 BANK_DEVIATION channel)

Available immediately for B12 drawers. Each has clear reuse targets:

- **`zhu_master_for_LR_right.py`** (from 往): 主 shifted to right column,
  parameterized `mx_off` + `scale`. USE FOR: 住 (亻+主), 注 (氵+主),
  柱 (木+主), 驻 (马+主), 蛀 (虫+主). Default (mx_off=55, scale=0.85)
  works for narrow-left radicals (亻/氵); try (mx_off=65, scale=0.80)
  for wider lefts (木/马).
- **`you_frame_up.py`** (from 油): 由-frame with central 竖 extending
  ABOVE the box. USE FOR: 由 char itself, 曲 (add extra internal heng),
  any 由-topology compound. Note: bank had jia_first/shen_extend/ri for
  the 甲/申/日 sub-family but NOTHING for 由's shu-up geometry. Mirror-shape
  of jia_first (which has shu-down); cannot be produced by scaling.
- **`tu_cun_stacked_for_LR_right.py`** (from 侍): 寺 = 土 over 寸, right
  column, PIL-pixel inline. USE FOR: 待 (彳+寺), 恃 (忄+寺), 詩 (訁+寺),
  峙 (山+寺). Adjust `ox` parameter to slide left/right.
- **`you_have_for_LR_right.py`** (from 侑): 有 shifted/compressed to
  right ~60%. USE FOR: 郁 (有+阝), 洧 (氵+有).

### v13 BANK_DEVIATION channel — stable behavior across B10+B11

Combined stats (100 items, 34 deviations, 7 variants promoted):
- Deviation rate: 34% (drawer skips a bank primitive ~1/3 of the time).
- Promotion rate among deviations: 20.6% (curator promotes ~1/5).
- Promotion rate overall: 7% (7 new variants per 100 items).

**When PASS-with-deviation → promoted as variant**: fresh_component
belongs to an OBVIOUS shape family (compressed 白, wide 儿, shifted 主,
由-frame, 寺-stack, right-slot 有) with 3+ plausible near-cousins.

**When PASS-with-deviation → NOT promoted**: fresh_component is a
one-off inline of a specific character (guo_mu_under_tian, ju_char,
kong_char, biao_char, hua_speak). Promoting these would bloat the bank
without producing reuse.

**When FAIL-with-deviation**: fresh_component was a NOVEL shape not
in any bank family (亞 mirror-envelope, 侃 frame-with-pillars, 转 车/专,
侉 夸, 侌 今/云, 是 stack-on-日, 畈 田-with-反, 畋 田+攵). No promotion
(v13 evidence rule).

### The zero-A finding (research write-up ready)

**550 items × 11 batches × 4 format-freedom unlocks (v8/v9/v10/v13) ×
2 prose overlays × 2 retry mechanism cycles = 0 A verdicts.** G4's
米字格 anchor+joint format earns A regularly (15%+ in B9-B11). The
gap is structural, not effortful.

For the drawer in B12+: do NOT hand-tune widths below the 4-6px MMH
band chasing A. Prioritize:
1. Identity-alias when both sides bank-mastered (highest single-lever).
2. New v13 variants above (for right-column 主/有/寺, 由-frame).
3. Explicit-bank-call for 2-part side-by-side (works: B10 时/串 PASSed).
4. Inline with thin uniform ink for genuinely novel shapes.

DO NOT waste cycles on: X-crossing family (matched 大 recipe still C
at retry_4 for 矢/失; now TERMINAL), mirror-splay 4-arm, cursive
envelopes with interior curls.

### Retry queue for B12 (positions 601+)

- **CONTINUE retries (R2 → R3)**: 疖, 亨, 声 — all B9 leak candidates
  that survived B10's leak-fix and B11's proportion attempt. Add
  explicit y-band hints per P-DEV2 in B12 retries.
- **TERMINAL_FROZEN (do NOT retry)**: 矢 (R4 C), 失 (R4 C). Format
  ceiling for X-crossing confirmed via 4 unsuccessful retries under
  progressive unlocks. Move out of active pool.
- **NEW C-attempt retry candidates from B11**: 物 (C), 佾 (C),
  受 (C), 说 (C). Add each with specific geometric fix idea (see
  errata.md B11 additions).

---

## B12 addition (2026-08-04) — ★★★ FIRST-EVER A + P-DEV4 pathway + 3 terminal freezes

**B12 main pass rate: 7/50 = 14% (1 A + 6 PASS). Retry: 0/3 → all
TERMINAL_FROZEN. Cumulative through 600: ~42% pass, 1 A verdict.**

### ★★★ THE 畎 A VERDICT — WHAT YOU CAN USE FROM IT ★★★

`p3_char_0434_畎` (田 + 犬) is G3's first A verdict in 600 items.
See PNG: `attempts/p3_char_0434_畎/01_畎.png`.

**Two new variants promoted directly from this render:**

- **`quan_tian_for_LR_left.py`** — compressed 田 for LR-left slot.
  Signature: `draw_quan_tian_for_LR_left(d, x_left=30, x_right=125,
  y_top=100, y_bot=220, w=5, wm=4)`. USE FOR: 略 (田+各), 畔 (田+半),
  畝, 畦, 畯, 畹. Also directly usable for retry candidates 畈, 畋.

- **`quan_dog_for_LR_right.py`** — 犬 in LR-right slot with explicit
  shared-pixel cross-apex. Signature includes tunable pie_top/na_tail/
  dian_head/dian_tail coords. USE FOR: 猷 (酉+犬). Also proves out
  the P-DEV4 compression-pathway for the 大-family in L-R rights.

### P-DEV4 — the compression pathway (READ THIS if your character has X-crossing)

X-crossing family (大/矢/失/人/入) is TERMINAL_FROZEN at full canvas.
But COMPRESSED into an L-R sub-slot ≤ 55% of canvas, thin-ink X-crossing
CAN pass the panel (this is how 畎 earned A).

**Try P-DEV4 pathway when**:
1. Target is L-R or U-D; X-crossing radical fits in ≤ 55% of one axis.
2. You compute the cross-apex as a shared pixel (e.g. `cross = (x, y)`)
   BEFORE drawing pie and na.
3. Ink weight ≤ 5px; two-cubic pie (head segment + body segment).
4. The sibling half is a stable envelope/frame (田, 口, 目, 日, 山, 木).

**Do NOT try P-DEV4 for standalone 大/矢/失/太/夫**. Those remain
TERMINAL_FROZEN. Do not attempt to un-freeze.

### 3 new TERMINAL_FROZEN characters (do NOT retry in B13)

- **疖** (疒+卩) — B9 leak, R1 FAIL, R2 FAIL, R3 C. All hints applied.
- **亨** (亠+口+了) — R1 FAIL, R2 FAIL, R3 FAIL. y-band hints ignored
  or under-rendered.
- **声** (士+尸-envelope) — R1 FAIL, R2 FAIL, R3 FAIL. Middle 竖 of
  士 never survives to render at discriminable pixels.

If any of these appears in a B13 retry brief by mistake, skip and log.

### v13 BANK_DEVIATION channel — B12 stats

- Deviation rate: **60/50 mains = 120%** (many attempts skipped multiple
  bank entries — highest yet).
- Promotions: 2 variants (both from the 畎 A verdict).
- Promotion rate among deviations: 2/60 = 3.3% (down from B10's 18.75%
  and B11's 22.2%).
- Reason for lower rate: this batch's item pool hit many novel-shape
  right-radicals (侯/便/侷/俅/俉/俊 bodies) that P-DEV1 rule 2 flags
  as "do NOT deviate, no bank family". Drawer deviated anyway (no
  choice) and mostly FAILed. This is content-gap, not memory failure.

### Retry queue for B13 (positions 651+)

- **CONTINUE new R1 candidates** (use new B12 variants + specific fixes):
  - 畈 (田+反) — use `quan_tian_for_LR_left`
  - 畋 (田+攵) — use `quan_tian_for_LR_left`
  - 给 (纟+合) — compressed inline 纟 + bank kou
  - 结 (纟+吉) — compressed 纟 + bank shi_male + bank kou
  - 神 (礻+申) — inline compressed 申
  - 盃 (不+皿) — inline compressed 皿-bottom
  - 侶 (亻+呂) — bank ren_pang + 2 stacked bank kou (small)
  - 係 (亻+系) — bank ren_pang + inline 系

- **TERMINAL_FROZEN** (do NOT retry): 疖, 亨, 声, 矢, 失, 大, 人, 入, 匕.

- **Watch for validation items**: 猷 (validates quan_dog_for_LR_right),
  略/畔/畝/畦 (validates quan_tian_for_LR_left).

### Language update

Previous batches said "zero A across all G3 batches". As of B12:
**"1 A verdict in 600 items (0.17%), earned via P-DEV4 L-R-slot
compression pathway; full-canvas X-crossing format ceiling unchanged."**
G4's per-batch A rate (15%+) still dominates. The 1 A is a narrow
exception, not a format break.

---

## B13 curator notes (2026-08-05, position ~651)

### Two new bank variants — use them

- **`ren_pang_pil_for_LR_left.py`** (row 251). Canonical PIL-inline 亻
  for LR-left slot. Use whenever the right radical is being rendered
  in PIL coords (not turtle). Call: `draw_ren_pang_pil_for_LR_left(d,
  cx=75, y_top=90, y_bot=225)`. Widths default to MMH thin ~5px;
  override for heavier ink.
- **`zou_zhi_thin_pil_envelope.py`** (row 252). Canonical PIL-inline
  辶 envelope in MMH-thin ink. Call: `draw_zou_zhi_thin_pil_envelope(d)`.
  Interior radical goes in the upper-right chamber (x ∈ [110, 285],
  y ∈ [55, 235]). If the interior is 吉/舌/甬/前/甫/角/隹, hang it
  above the 平捺.

### 疒 envelope pattern is holding — this is a stable radical PASS mode

B13 evidence: 疰, 疴, 疸, 痂 all PASSed with `ne_sick.draw_ne_chuang`
(envelope) + inline interior. The 疒 envelope has crossed into "reliably
gets the panel". When you see any 疒-char, START with `ne_sick`, then
inline the interior in the belly slot (x ∈ ~[100, 240], y ∈ ~[110, 260]).
Only C's / FAILs on 疒-chars this batch had interior-shape problems
(疹's 㐱 interior; 疽's 且 nearly there; 疱 novel 包 shape).

### G3 beat G5 on B13 — item-level observation (research signal)

For the first time across 13 batches G3's PASS rate (20%) exceeded
G5's (18%). G3 won on 13 items (mostly by having a PASSing render
where G5 got C or FAIL); G5 won on 12. **Pattern of G3 wins**: cluster
on 疒-envelope chars (疰/疴/疸 all G3 PASS while G5 C or FAIL) and on
established composition modes (适 with 辶 envelope + upper-right
interior; 响 with 口+向 L-R). **Pattern of G5 wins**: cluster on
X-crossing / mixed-glyph chars where MMH median coords tip the render
into "human-look" (痂 G3 PASS but G5 A; 特, 值, 真 all G5 PASS but G3
FAIL). Working hypothesis: for radical families that the bank has
crystallized into a stable envelope + interior slot (疒, 辶, 亻), G3's
memory now compensates for the absence of MMH; MMH becomes noise that
occasionally disrupts a would-be PASS. For X-crossing / novel-body
chars where the bank has no envelope, MMH is a lifeline for G5. This
is worth a paragraph in the paper — memory format interacts with
external cue availability. See sandbox.md B13 note for the raw counts.

### Variant post-mortem: 畈, 畋 R1 FAILs

Both B13 R1 predictions FAILed. The `quan_tian_for_LR_left` primitive
rendered CLEANLY in both attempts (see 畈 R1's 田 — clean rectangle;
see 畋 R1's 田 — clean rectangle). What failed was the RIGHT radical:
反 collapsed to a curl and 攵 became a floating dash + tiny 人. **The
lesson (codified as P-DEV5 in principle_bank.md)**: promoting a
one-slot variant does NOT unlock characters whose sibling radical is
still novel. When you propose to retry 略/畔/畝/畦/畯 with
`quan_tian_for_LR_left`, first check that the RIGHT radical (各/半/亩/
圭/夋) has a bank primitive or a documented recipe. If not, the retry
will fail on that side regardless of how good the box is.

### B14 retry queue (6 items — see sandbox.md for full rationale)

Prioritized R1 candidates (all B13 C's):
1. **能 (0499)** — near-miss; composition visually right, thick/mechanical.
2. **疽 (0528)** — 疒 envelope + 且. Same pattern as 疰/疴/疸 PASSes;
   just interior needs sharper geometry.
3. **疹 (0526)** — 疒 envelope + 㐱 (人+彡). Envelope known; 㐱 is the
   variable. Try with explicit 3-cascading-pie 彡 body.
4. **都 (0503)** — 者+阝 L-R. Adapt 阝 recipe from 那 attempt.
5. **亳 (0532)** — 亠+口+冖+乇 4-stack tower. Try with explicit y-band
   per piece (P-DEV2 rule for 3+-stacks).
6. **部 (0525)** — 咅+阝 L-R. Same 阝 recipe as 都; distinct interior.
