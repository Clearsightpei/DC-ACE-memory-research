# G2 memory index — entry point for the drawer

*Maintained by the curator. Drawer reads this file first every cycle,
then follows the pointers below (or explores the group directory
freely if you need to find something not listed).*

---

## TIER-0 (v7.3, pos 326): READ THESE THREE THINGS BEFORE ANYTHING ELSE

Distilled from B5 evidence that drawers stop reading after ~3 short items.
If nothing else, absorb the following three items — they cover ~70% of
recurring-failure identity bits without opening any other file.

### A. Sibling-risk targets — copy-verbatim protocol

If your target label is one of these, **open
`sibling_signature_checklist.md` and paste the matching row verbatim
into your generated.py docstring as a `# SIGNATURE CHECK:` block**.
Do NOT deviate on GT-tracing grounds.

Targets: 人, 入, 士, 土, 干, 千, 于, 己, 已, 巳, 匕, 七, 大, 户, 尸,
贝, 见, 木, 未, 末, 术, 刁, 丁, 亍, 个, 丸, 孑, 孓, 子, 尢, 九, 之,
山, 门, 上, 下, 亾.

### B. Hook flick directions (inlined so no file-open needed)

Whenever your target contains any 钩, its terminal flicks UP-and-LEFT,
never DOWN. Six specific stroke families:

| stroke-family | flick direction |
|---------------|-----------------|
| 竖钩 (亅) | UP-and-slightly-LEFT (~-100° to -110°) |
| 竖弯钩 | UP-and-LEFT after the arc (~-105° to -115°) |
| 横折钩 (any) | UP-and-LEFT at the terminal (~-105° to -120°) |
| 横折弯钩 (飞, 几, 九) | UP-and-LEFT after the sweeping arc (~-115°) |
| 斜钩 (戈) | UP-and-LEFT at the arc's end (~-110° to -120°) |
| 卧钩 (心) | UP-and-LEFT from the bowl's right end (~-145°) |

**Never** flick DOWN, DOWN-right, or straight up. When in doubt: the
hook always flicks back INTO the character body (toward the interior),
not outward. **This was the #1 root cause of B4/B5 retry FAILs.**

### D. Compound-character sibling bits (NEW v7.4, pos 388)

Sibling_signature_checklist rows apply to COMPONENTS of compound
characters too — not just standalone renders. B6 fails 仕 (亻+士),
去 (士+厶), 比 (匕+匕 — apply row TWICE, once per 匕) all failed
because the sibling row was ignored when the sibling-risk radical
appeared as a sub-glyph. If your target contains 士, 土, 干, 匕, 七,
己, 已, 巳, 未, 末, 术, 木, 大, 户, 尸, 贝, 见, 人, 入 as a
COMPONENT, paste the matching sibling row into your docstring AND
enforce the length-ratio inside the component sub-glyph. See
drawer_memory pos-388 addition.

### E. Retry cohort RETIRED (v7.4, pos 388)

Every item you see from B7 onwards is a NEW P3 target (no more retry
attempts). Errata is preserved as reference, but the drawer prompt no
longer dispatches retries. Ignore any "retry_n" tracking — treat every
attempt as first-attempt.

### H. Components MUST touch (NEW v7.6, pos ~650) — B12 emergent rule

**B12 evidence**: every PASS this batch had components (radical +
right-body, or top-lid + bottom-body, or wrap + inner) that TOUCH
along their shared boundary — no visible gap. Every LR-spacing FAIL
had a >~15 px gap between components. This holds across all 12
B12 successes.

**Rule**: after drafting your generated.py, mentally trace the join
between each pair of components. If you would see white space
between them at final render, MOVE one component 5-15 px toward the
other so their strokes overlap by ~5 px. 亻 竖 must touch or start
within its right component's 撇/横 sweep, not stand off in a
detached column. Canopy characters (广, 疒, 尸, 户) — the body must
be tucked INSIDE the canopy's 撇 sweep, not sitting under it.

### C. Signature-bit override (v7.1 HARD RULE, retained)

If the label matches a sibling-pair table, DO NOT override the
signature via "the GT shows something slightly different". The
signature IS the character's identity. B3's 人 failure and B5's 见
failure were both this pattern.

### F. Calligraphic-weight 4-move (NEW v7.5, pos 600) — the C-to-PASS and PASS-to-A lift

**Direct cause of B11's 0-A regression: all 7 C items used
`d.line(pts, width=6)` uniform polylines with zero taper. Do NOT
render Phase-3 characters with uniform-width straight lines.**
Every 5+-stroke compound target — especially 亻/讠/氵/礻/纟/疒/口-
prefix characters — MUST apply these four moves before submitting:

1. **Teardrop taper** — every 撇, 捺, 点 uses variable width along
   the stroke (thin→thick or thick→thin). Two accepted patterns:
   - `stroke(pts, widths=(11, 5))` helper that samples ellipses at
     each point with interpolated radius (see drawer_memory.md line 151);
   - `[5.0, 4.8, 4.3, 3.5, 1.8]` per-point width array.
   Uniform `width=6` polyline strokes REGRESS a correct signature
   from PASS to C.
2. **Shoulder dab at every 折 joint** — one extra `d.ellipse` at
   radius ~1.3× stroke radius at every corner, BEFORE the second
   segment starts. Missing shoulder dabs make `折`/`钩` corners
   read as ruler-square rectangles (see B11 佶 口, B11 侖 冂).
3. **Bezier for any curved sweep** — 撇 (bowed), 捺 (S-curve),
   横撇 (hooked pie), 竖弯钩 (arc). Straight-line 撇 is a fail-mode
   signature. Import the `bez(p0, p1, p2, p3, n=60)` helper (see
   drawer_memory.md line 170 or copy from p3_char_0338_佘 attempt).
4. **Correct hook flick** — TIER-0 rule B applies. UP-and-LEFT,
   into the character body. B11 说's 兑 lost 6→7 quality points
   from a straight-down hook alone.

**Full recipe with worked example**: read
`groups/G2_free_form/attempts/p3_char_0338_佘/generated.py`
(75 lines, B10's first A verdict, uses all 4 moves). Copy the
`bez()` + `stroke()` helper pattern into your own generated.py
before drawing anything.

### G. Frozen-radical alarm (NEW v7.5, pos 600) — attested-5x-failed radicals

**If your target contains 讠, 戈, 攵/攴, 匕, 纟, 弓 as a component,
open `frozen_cohort.md` FIRST**. These radicals have failed 3-5x
across B7-B11 and identical memory guidance has not transferred.
The frozen_cohort file is the sole per-radical fix hypothesis
sheet — TIER-0 alone will not tell you the fix.

Attested counts as of B13 (pos ~700):
- 讠 family: 5x failed (记, 证, 话, 说, 转, 线, 规)
- 戈 family: 5x failed (代, 伐, 我, 找, 或)
- 攵/攴 family: 3x failed (改, 放, 畋)
- 匕/兑 hook family: continuing (dozens of fails)
- 纟 family: 2x recent + frozen carryover
- 弓 family: 1x this batch (张 in B10 already noted)
- **疒 family: 14x attested (7 in B12 + 7 in B13). Recipe applied
  in B13 but did NOT transfer.** See frozen_cohort.md 疒 row —
  hypothesis falsified. If you draw a 疒-family target: apply the
  5-stroke decomposition, AND geometrically constrain the inner
  点+提 pair to sit inside the wedge bounded by 横 (above) and 撇
  (left). Shrink the body ~20% and pack it fully under the 撇's
  belly. **Neither of these fixes is verified to transfer** — draw
  carefully and expect the identity may still not read.
- **辶/走 wrap family: 6x attested (选 B12 + 5 in B13:
  适/通/造/速/起). NEW cluster this batch.** See frozen_cohort.md
  辶 row for wrap-topology fix hypothesis (interior body sits ABOVE
  the 平捺 sweep, 捺 starts to the LEFT of interior and sweeps
  RIGHT to past its right edge). Untested but geometrically
  motivated. If your target contains 辶, 廴, or 走: **do NOT** draw
  the radical to the LEFT of the body — draw the body FIRST at
  y=30..200, then draw 辶's 平捺 sweep from x_left_of_body,y=205
  to x_right_of_body+15,y=230, foot flare up-right. Interior body
  MUST have its bottom stroke overlap the 平捺 start.
- **田-body-with-rare-top family: 6x attested (畚/畛/畜/畝/畟/畢
  B13).** Rare tops (龹, 㐱, 玄, 亳, 華-lookalike) have no encoding.
  **Do not invent the top's structural class from the label** —
  trace the GT stroke by stroke, emit each in GT order. 田 body
  encoding is fine (see 田/由/町/畎 PASSes).

---

## When the top-3 do not apply, consult:

1. **`form_catalog.md`** — stroke forms indexed by (class × context).
   Cited by 33% of B5 attempts and by 100% of prior batches' retry-
   PASSes. This is the highest-transfer file G2 has.
2. **`errata.md`** — has the specific per-item retry note if your
   target has failed before. NEW B5 fails now live in a compact table
   at the bottom of errata (not full sections) — grep for your item_id.
3. **`drawer_memory.md`** — technique reference (PIL brush-dabs,
   Bezier, arc primitive). Consult when rendering, not when planning.

## RETIRED (v7.3, pos 326): HOT LOOKUP table

The B4 and B5 citation audits confirmed the HOT LOOKUP retrieval
table at the top of this file had 0/64 (B4) and 0/50 (B5 main) cites.
It has been removed. Its function is now covered by TIER-0 above
(for sibling targets) and by direct form_catalog grep (for
composition-role questions). See evolution.md pos 326 for the
pruning rationale.

## FROZEN retry cohort (v7.3, pos 326)

Six items reached retry_n=3 and are FROZEN (will not be retried in
B6): 马, 夂, 车, 风, 旡, 牛. These items have received identical
memory guidance across 3 batches without transfer. They are kept in
errata for reference but are not eligible for the retry pool. If a
related char PASSes in future batches (e.g. 攵 for the 夂 family, or
a 二-lid compound for the 旡 family), curator will re-open the
corresponding freeze on evidence.

## The v7 restructure (2026-07-18 @ pos 168)

The B2 collapse (83→70→40%) proved that global meta-rules alone
don't help. Memory now separates **contextual form knowledge** from
**meta-rules and technique**. **Consult in this order**:

1. **First**: `radical_position_rules.md` — silhouette + aspect
   ratio + center-of-mass check. Do this BEFORE drawing.
2. **Second**: `form_catalog.md` — the stroke-form catalog indexed
   by `(class × context)`. Find the entry that matches the specific
   context of the stroke you're about to draw (e.g. "撇 as top-of-
   radical single flick" not "撇 in general").
3. **Third, only if 1+2 don't cover it**: `drawer_memory.md` —
   the older meta-rules and per-batch principle collection. Kept
   as backstop and technique reference (PIL brush-dabs, arc primitive,
   beat-count rule). Item mastery ledgers live here too.

## What memory G2 currently holds

- **`sibling_signature_checklist.md`** — NEW (v7.2, pos 277): small
  dense pre-drawing checklist for sibling-risk items. 34 bright-line-
  bits rows + 6 bright-line-flicks rows. Copy-verbatim protocol.

- **`radical_position_rules.md`** — NEW (v7 restructure): whole-
  radical layout, aspect ratios, silhouette-first heuristic, the
  米字格 eyeball aid.

- **`form_catalog.md`** — NEW (v7 restructure): stroke forms indexed
  by (class × context). Entries: 撇 in 4 contexts, 点 in 4 contexts,
  竖 in 3, 横 in 3, 折-shoulder in 2, 捺 in 3, sibling-pair topology
  table, left-position radical compression rules.

- **`drawer_memory.md`** — the older free-form file. RETAINED as
  a technique reference (PIL brush-dabs, Bezier sampling, arc
  primitive, beat-count rule) and as the append-log of per-batch
  distilled principles. Includes:
  - Radical-composition principles (bootstrap, B1)
  - "Draw the flick" hook rules
  - Length-ratio distinguishers (superseded by form_catalog sibling
    table but retained for cross-reference)
  - Topology overhang, multi-fold body-connection rules
  - Stroke-direction reminders, hook family, folder family, 弯
    family, tangent arc primitive, beat-count rule, standalone-vs-
    compound scaling
  - Batch mastery ledgers (which items PASSed per batch)

- **`errata.md`** — the 错题集. Failed items with per-item diagnosis,
  fix ideas, retry_n counter.

- **`scans/`** — per-position errata scan decisions.

- **`retry_log.jsonl`** — append-only retry log.

- **`curator_satisfaction_log.jsonl`** — per-attempt "would-I-stop?"
  verdicts (calibration data, not gating).

- **`evolution.md`** — append-only log of structural changes to
  memory. See it for the "why" behind reshuffles.

## When to consult what — updated

- **Drawing any Phase-2 radical**:
  1. Open the GT PNG.
  2. Read `radical_position_rules.md` — decide aspect-ratio family
     and center-of-mass.
  3. For each named stroke, grep `form_catalog.md` for a matching
     `class × context` entry. If found, use its form guidance.
  4. If no entry matches, fall back to `drawer_memory.md`'s
     stroke-direction reminders + hook family + folder family.
  5. If drawing a sibling of a nearby glyph (匕/七, 士/土, 己/已/巳,
     人/入 …), check the "Sibling-pair topology signatures" table
     in `form_catalog.md`.
- **Drawing an unfamiliar shape**: draw fresh from the GT the way
  G1 would. Memory is supplementary, per shared_rules.
- **Wondering if this item has been attempted before**: grep the
  batch mastery ledgers at the bottom of `drawer_memory.md`.
- **You've drawn once and want to revise**: use the silhouette check
  from `radical_position_rules.md` (aspect ratio + center of mass)
  as your revision compass — if you got THOSE wrong, restart the
  layout; if only local strokes are wrong, tweak.

## Change history

See `evolution.md` for the append-only log of structural changes to
G2's memory organization.

---

*v7 restructure — batch B2 curator (pos 168) created
`radical_position_rules.md` and `form_catalog.md` and re-pointed the
drawer's entry order. Rationale in evolution.md.*
