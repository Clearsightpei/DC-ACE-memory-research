# G4 drawer_memory (v8, position 350)

*Free-form persistent memory added at v8 unlock. Same shape as G2's
memory. Curator writes here; drawer reads it via `memory_index.md`.
Read this BEFORE the structured bank — for many items it will already
name the primitive to call.*

*The grid bank (`success_bank/code/`) + principles + form_catalog +
joint_atlas remain available as REFERENCE. Nothing in them is mandatory
under v8. When this file and the structured bank disagree, follow this
file.*

---

## Fast lookup — call these primitives directly

The single highest-value action per B6 evidence: **when a character
contains one of these components as a sub-part, IMPORT and CALL the
primitive**. Do not reinvent. B6 had ~15 items where reuse would have
saved the attempt; ~8 of them FAILed by drawing fresh instead.

### Chronic canonical primitives (mandatory imports)

If the target contains 丿, 刀, 冂, 弓, 马 as a component: **import the
chronic module**. B6 showed drawers cite these in comments but never
import them; that is treated as a mechanism failure. From B7 onward,
comment-only mention is not sufficient.

```python
from chronic.pie_radical import draw_pie_radical    # 丿
from chronic.dao_char     import draw_dao_char       # 刀 (and 刅, 刀-containing chars)
from chronic.jiong_frame  import draw_jiong_frame    # 冂 (and 用, 内, 円, 内, 门-containing chars)
from chronic.gong_bow     import draw_gong_bow       # 弓 (and 引, 弗, 弘)
from chronic.ma_horse     import draw_ma_horse       # 马 (and 乌, 鸟)
```

If the character contains the component but at a different position/
scale, still call the chronic primitive first and shift its output via
the `offset_x`/`offset_y`/`scale` parameters where available, rather
than redrawing.

### High-value component primitives

For left-radical or bottom-radical compositions, these bank files are
worth importing:

```python
from ren_side  import draw_ren_side    # 亻 (仔/付/打/化/他/仝/仕 all reused this in B6)
from shou_side import draw_shou_side   # 扌
from xin_side  import draw_xin_side    # 忄
from si_silk   import draw_si_silk     # 纟
from chi_step  import draw_chi_step    # 彳
from you_again import draw_you_again   # 又 (needed for 反 又 对 权 etc)
from bi        import draw_bi          # 匕 (mirror for 比; call TWICE for 比)
from li        import draw_li          # 力 (needed for 办 加 男)
from bao_char  import draw_bao_char    # 勹 (needed for 勻 匀 匆)
from er_legs   import draw_er_legs     # 儿 (needed for 元 兄 光)
from xin       import draw_xin         # 心 (needed for 必)
from tu        import draw_tu          # 土 (needed for 去 圭 坐)
from si_private import draw_si_private # 厶 (needed for 去 台 参)
from shan      import draw_shan        # 山 (call TWICE stacked for 出)
```

### Never-tune-anchors rule for reused primitives

When you import a primitive, call it with its DEFAULT signature. If
the primitive doesn't fit exactly, prefer inlining fresh (per shared
rules "supplementary aid") — do NOT try to override 3+ anchors of a
mastered primitive. That path caused the p2_082_子 chronic saturation
in B4.

---

## Compositional playbook — how to think about 3+-part characters

B6 diagnosis: all 24 main FAILs are multi-part characters where the
sub-parts don't visually cohere. All 26 main PASSes are either
simple 3-4 stroke chars or 亻/扌/宀-prefixed reuses. **The failure
mode is composition, not stroke rendering.**

**Step 1**: split the target into named sub-radicals BEFORE looking at
anchors. Write the split as a comment: `# 反 = 厂 + 又`.

**Step 2**: for each sub-radical, look for a mastered bank primitive
in the shortlist above OR in `success_bank/INDEX.md`. If one exists,
IMPORT it.

**Step 3**: place the sub-radicals in a grid layout:
- **Left-right** (亻+X, 扌+X): left in x∈[0.05, 0.40], right in x∈[0.45,
  0.95]. Both fill y∈[0.10, 0.90].
- **Top-bottom** (宀+X, 一+X, 亠+X): top in y∈[0.05, 0.35], bottom in
  y∈[0.35, 0.95].
- **Enclosing** (囗+X, 门+X, 冂+X): frame fills [0.10, 0.90] both axes;
  inner sub-radical fills middle 60% both axes.
- **Stacked repeated** (出=山+山, 比=匕+匕): use SAME primitive twice
  with mirrored or offset anchors.

**Step 4**: enforce compositional coherence — every sub-radical must
share at least one anchor pixel with an adjacent sub-radical, or leave
a visible ~15-25 px gap. Never touch AND never disconnected.

---

## B6 systematic failure notes

**Enclosing frames (冂/门/囗-containing chars)**: 用, 们, 内 all failed
by not calling `chronic/jiong_frame.py`. If the target contains an
enclosing frame, the FIRST line of code should be
`from chronic.jiong_frame import draw_jiong_frame`.

**Left 阝 radical is missing from the bank.** 队 FAILed because there
is no primitive for 阝-left. Right 阝 exists (`fu_right.py`) but is
NOT a mirror. Until a `fu_left.py` promotion arrives, decompose 阝-left
as: short 撇 top + 竖 left + 横折 bend + tail — 3 strokes in x∈[0.05,
0.35] column.

**Stroke-count omissions**: 水 keeps rendering as 3 strokes (missing
right 捺); 礻 keeps rendering as 3 strokes (missing top dot). Add an
explicit `assert len(strokes) == expected` before rendering, and add a
retry pass if the count is off.

**Symmetry pairs (比, 丱, 从, 双)**: these characters are TWO copies
of the same sub-radical. Compute anchors ONCE, then mirror x_frac via
`(cell, 1 - x_frac, y_frac)` for the mirrored copy. Do NOT hand-derive
two independent copies — they will not match.

**顶部单点 items (礻 主 亠-family)**: the top dot is often the first
thing dropped by the drawer. Render the dot LAST as a defensive step
so it can't be overwritten by later strokes.

**Chronic-mechanism import discipline**: when the target maps to a
chronic primitive, the drawer's `generated.py` MUST include the
`from chronic.<x> import draw_<x>` line and MUST call it. A comment
citing the primitive is NOT sufficient (B6 evidence: 18 comment
mentions, 0 imports across all history since position 300).

---

## What NOT to do (drawer traps from B1–B5)

- Do not chain multiple beziers to fake a compound stroke. Use
  `stroke_variable_width` with a single polyline. (see 飞 chronic fails)
- Do not draw two separate strokes for what MMH lists as one compound.
  (e.g. 及, 廷, 建 need `heng_zhe_zhe_zhe.py` NOT 3 pieces.)
- Do not tune the anchors of a chronic primitive. Call it as-is. If
  it looks wrong to you, that means your visual read of the GT differs
  from the panel's — the panel wins.
- Do not skip `errata.md` on repeat items. Every retry is against a
  drawer's own prior failure, and the errata fix is the panel's summary
  of what needs to change.
- Do not soft-interpret an errata fix. "Widen to anti-diagonal ('TR',
  0.85, 0.15) → ('BL', 0.15, 0.85)" means those exact tuples, not
  "something more diagonal than before."

---

## Interpretation window (from v8 rules)

Everything in the bank + principles + form_catalog + joint_atlas is
REFERENCE ONLY. If your visual read of the GT disagrees with them,
follow your read. But: when an item has failed 2+ times and the errata
gives a literal fix, the interpretation window closes — follow the
errata verbatim. The 4-batch chronic-cluster saga (see `evolution.md`
position 300) is the negative evidence.

---

## v9 addendum — VISUAL DIFF STEP 0 (from B7r evidence)

Under the v9 retry prompt, drawers open the prior failed PNG side-by-
side with the GT before touching code and write a `VISUAL DIFF` block
at the top of `generated.py` naming concrete gaps ("prior right half
collapsed to 乙 curl because s3 and s4 heads coincide at MR(0.55,0.10)").
Both B7r PASSes (比, 文) did this. The 10 B7r FAILs also did it, so
visual-diff is necessary-not-sufficient — but it is CHEAP and it
converts "chronic invisible topology bugs" into named diagnoses the
next retry can literally fix. **On any retry, do Step 0 in prose
before writing anchor tuples.**

Concrete lessons from the 2 v9 PASSes:
- **比 (retry_1 v9)**: prior halves were centered at x≈55 and x≈250 —
  too far apart, off-center. GT halves live at x∈[55,145] and
  x∈[145,265]. Fix was to trust MMH anchors verbatim (they are more
  centered than any hand-tuned attempt). When a symmetry-pair is
  failing, MMH-verbatim is stronger than clever mirror math.
- **文 (retry_2 v9)**: prior X-cross had both pie head and na head at
  the same point on the heng — reads as 人 (inverted V), not X. Fix
  was `CROSS_ANCHOR = ('BC', 0.385, 0.225)` welded at pie-MID and
  na-MID (not at their heads). The X-cross weld point is BELOW the
  heng, not on it.

---

## B7 failure pattern (post-batch — 25 FAILs, 4 clusters)

**Cluster 1 — frame-plus-interior (5 items)**: 冊, 册, 冋, 冎, 冯.
All contain 冂 or 马 as a dominant part. `chronic/jiong_frame.py` /
`chronic/ma_horse.py` were NEVER imported (0/6 candidates checked; 4
mentioned in comments then reinvented). The chronic-mechanism import
failure from B6 REPEATS in B7. `drawer_memory.md` already contains
the mandatory-import snippets and it is still not being followed.
Next batch: consider stronger enforcement (e.g., dispatcher pre-check
that greps generated.py for `from chronic.` when the target contains
a chronic component, and stalls if missing).

**Cluster 2 — 一 + horizontal-fold-stack (4 items)**: 亘, 亙, 会,
that-family. All have a top-and-bottom heng bracketing a compressed
middle. FAIL mode: the two brackets don't align vertically and the
middle collapses. Fix pattern: enforce `s1.head.y == s_last.head.y`
alignment; middle content in y∈[0.25, 0.75] band only.

**Cluster 3 — 亻/讠-prefix + non-bank right (4 items)**: 仡, 仫, 记.
亻 side is fine (imports ren_side); right sub-component is not in the
bank and comes out fragmented. No fix beyond promoting the missing
sub-components (乞, 么, 己-full).

**Cluster 4 — X-cross topology (5+ items)**: 癶, 处, 処, 乩, 那.
Same topology bug that v9 rerun caught for 文: apex pixel not shared,
so 撇+捺 reads as 人 not X. **Standard fix**: define a `CROSS_ANCHOR
= (cell, x_frac, y_frac)` tuple and pass it as MID (not head) to
both pie and na. This is now a pattern worth spelling out here.

### Ready-to-copy X-cross snippet

```python
# X-cross weld pattern (from B7r 文 success)
CROSS = ('BC', 0.5, 0.25)  # adjust per item
# Route both pie and na through CROSS as their MID control:
draw_pie(d, head=('TC', 0.45, 0.10), tail=('BL', 0.20, 0.90),
         mid=CROSS)  # or use quad_bezier with CROSS as ctrl
draw_na(d, head=('C', 0.35, 0.15), tail=('BR', 0.30, 0.85),
        mid=CROSS)
# Verify shared pixel: anchor_to_xy(CROSS) same for both calls.
```

---

## Bank-utilization guidance (post-B7 prune)

Post-B7 prune round 2 removed ~10 additional never-imported thin
wrappers (see `evolution.md`). Files that survive represent primitives
with either (a) proven reuse, or (b) high-value slots the v8 mechanism
is trying to activate. Do NOT re-derive functionality that a surviving
bank file provides. When in doubt, prefer IMPORT over INLINE, even
if MMH anchors seem to disagree — the panel accepts bank-canonical
shapes with wide anchor tolerance.


---

## B8 addendum (position 450) — bank-import discipline + 亻+X pattern

**B8 outcome**: 20/50 mains (40%); 0/7 retries. Bank import rate
cratered: 40/50 mains inlined everything via `_anchor + fat_line`.
The 30 FAILs are almost all 亻+X or radical-radical compositions
where inlining the right-half loses coherence.

### If your target contains 亻 (as left radical) — this is 25/50 of B8

- **DO**: `from ren_side import draw_ren_side` and use its default
  anchors. Do not hand-place the 亻 strokes; the primitive already
  handles the pie+shu joint. B8 evidence: 亻 chars with imported
  ren_side PASS more than those with hand-derived 亻.
- **DO**: for the right sub-radical, LOOK UP whether it exists in
  `success_bank/INDEX.md` under any of its forms. B8 lost items
  where kou/nv/zi/mian/ren/bi/li could have handled the right half
  but drawer inlined instead.
- **DO NOT** override ren_side default anchors because they "sit in
  TC/C/BC" and you want TL/ML/BL — that was p3_char_0252_伊's
  documented FAIL note. If you need a different column, inline the
  2 strokes yourself; do not partially-override the primitive.

### If your target contains 冂 or 用/内/门/円 shape

**MANDATORY**: `from chronic.jiong_frame import draw_jiong_frame`.
Failure to import is a mechanism failure regardless of visual result.
B8 evidence: 3 chronic-component targets (再, 同, 西), all 3 mentioned
chronic in comments, 0 imported. Comment-only mention has been
insufficient for 3 batches (B6/B7/B8) — the import statement
is what enforces adoption.

### The 7 canonical primitives that DO NOT exist

Position 400 queued canonical primitives for 长, 夂, 夊, 水, 礻, 无,
气 but **the files were never written**. If your target contains any
of these radicals as a sub-part, DO NOT try to `from chronic.chang_long
import draw_chang_long` — the file is not there. Fall back to MMH-
verbatim anchors + inline base primitives (pie, shu, na, heng). These
7 items are marked TERMINAL_FROZEN in the retry log.

### Compositional-coherence check — new mandatory step for 6-stroke
### 2-radical chars

Before rendering, verify:
1. Left radical occupies x∈[0.05, 0.42] (2-3 strokes).
2. Right radical occupies x∈[0.48, 0.95] (3-4 strokes).
3. Combined stroke count matches MMH `expected_strokes`.
4. Every stroke is drawn by a NAMED primitive (either imported or
   inline). If more than 4 draw calls are inline `fat_line`, that
   is a signal to look for a bank primitive.

B8 FAIL pattern: 14 of 30 mains had ZERO bank draw calls. The
render-from-scratch approach hits panel-visible coherence failures
on ~60% of 2-radical chars.

---

## B9 A-recipe (position 500) — how to produce reference-quality (A) renders

B9 landmark: 11 A verdicts (10 mains + 1 retry) in a single batch.
G4 is the only group producing A verdicts at scale. Common pattern
extracted from all 11 A-verdict `generated.py` files:

### The 5-point A-recipe

1. **Explicit decomposition comment at the top** naming every
   sub-radical + total stroke count:
   ```python
   """佉 (qū) — 7 strokes.
   Decomposition: 佉 = 亻 (left) + 去 (right); 去 = 土 (top) + 厶 (bottom).
   """
   ```

2. **MMH-verbatim anchors** — pass every dispatcher-injected anchor
   tuple UNCHANGED into your stroke calls. Do not "tune" them, do
   not "clean them up", do not use clever mirror-math on symmetric
   halves. When your visual read of the GT disagrees with MMH, trust
   MMH. B9 evidence: every A used MMH literally.

3. **SELF_CHECK block** declaring stroke count and joint class:
   ```python
   SELF_CHECK = {
       'visual_ok': True,
       'stroke_count_ok': True,
       'endpoint_mismatches': [],
       'joint_class_mismatches': [],
       'overall_pass': True,
       'notes': '7 strokes MMH-verbatim; all N-joints preserved as gaps.',
   }
   ```

4. **Base primitives (`_anchor + fat_line` + `pie/shu/heng/na/dian/pie_zhe`)
   over compound bank primitives**. When MMH placement disagrees with
   a compound primitive's defaults (ren_side, mian, etc.), inline the
   sub-radical with MMH anchors + base primitives rather than partially
   override the compound primitive. B8 evidence (p3_char_0252_伊):
   partial override of a compound primitive is the #1 way to lose a
   near-A. B9 evidence: 4 of 10 A items explicitly rejected ren_side
   because MMH placed 亻 far-left of ren_side's TC/C defaults, and
   inlined with pie+shu MMH anchors.

5. **N-joint discipline**: declare every joint's class in the header
   comment or SELF_CHECK. **Leave the natural gap** (~15-25 px) for
   N-joints. Novices try to weld everything; A-drawers respect the gap.

### Compare to PASS vs FAIL patterns (B9)

- **PASS items (10 mains)**: follow points 1-3 but sometimes skip
  point 4 (use a compound primitive that happens to fit MMH well
  enough).
- **FAIL items (30 mains)**: most miss BOTH point 1 (no decomposition
  comment) AND point 4 (over-invest in compound primitives whose
  defaults don't match MMH placement, causing coherence loss).

### The counterintuitive finding

The A-recipe is NOT "import more bank primitives". It is "trust MMH
literally + structure the code around the decomposition". The bank
mostly serves as a low-level (single-stroke) toolbox; compound
primitives help when MMH placement matches their defaults, hurt when
it doesn't. This inverts the v6/v7 mandate-more-imports philosophy.

---

## v13 BANK_DEVIATION channel — no usage in B9

The v13 prompt added a `BANK_DEVIATION` block for drawers to signal
"I deviated from bank on purpose; here is what I changed and why".
B9 usage: **0/66 attempts**. Either drawers didn't read the v13
addendum, or every deviation was implicit under point 2 above
("trust MMH over memory"). No worked example exists yet.

If you deviate from a bank primitive (e.g., override its default
anchors, or inline fresh instead of importing when a mastered
primitive exists), add a BANK_DEVIATION block at the top of your
`generated.py`:

```python
# BANK_DEVIATION:
#   ren_side.py default anchors sit at (TC, 0.5) + (C, 0.5); MMH places
#   亻 at (TL, 0.8) + (ML, 0.6). Inlining pie+shu with MMH anchors
#   instead of importing ren_side. Reason: partial override of compound
#   primitive caused p3_char_0252_伊 FAIL in B8.
```

Curator promotes successful deviations as `<name>_A.py`, `<name>_B.py`,
or `chronic/<name>_v2.py` variants. Without your signal, the curator
cannot see the deviation from anchor-diff alone.

---

## B9 chronic-mandatory mechanism — falsified (3 batches)

Chronic-import rate: B7 = 0/6, B8 = 0/3, B9 = 0/5. Three negative
batches on the same mechanism. The "MANDATORY `from chronic.<x>
import draw_<x>`" text in the top of this file has been ignored
by every drawer since position 300 (except for comment-only
mentions).

**Effective decision for B10+**: treat the chronic-mandatory section
as REFERENCE (not mandatory). If your target contains 丿/刀/冂/弓/马
and you can import the chronic primitive with anchors that match MMH,
do so — it will save you code. If MMH placement clashes with the
chronic default, inline via base primitives per the A-recipe point 4.

---

## B10 addendum (position 550) — BANK_DEVIATION channel evidence + refined A-recipe

**B10 outcome**: 19/50 mains (38%; 10 A + 9 PASS), 6/16 retries (38%;
3 A + 3 PASS). 13 A verdicts total (10 mains + 3 retries) — the
strongest calligraphic-quality signal to date. Cumulative through B10:
50% success, 20 A's before B10 (24 with B10 adjustments).

### BANK_DEVIATION channel — first live batch, first evidence

The v13 channel produced its first data. 13 attempts included a
`BANK_DEVIATION` block; 8 of those 13 were on PASS/A attempts (4 A + 4
PASS). **The channel is producing A-quality when drawer judgment about
primitive mismatch is correct.** All 8 successful deviations shared
one meta-pattern:

> Bank primitives (ren_side, ri, cao_grass_radical, wei_enclose,
> shou_side, bao_char, zhi_stop, er_legs) render their component at
> STANDALONE scale — filling the canvas. When that component is
> embedded in a compound character, MMH shifts it to a specific slot
> (far-left column, top-band, BC-compression, right-half compression,
> inset-frame). Partial anchor override of the compound primitive is
> the p3_char_0252_伊 FAIL pattern (B8, documented). Inlining via base
> primitives with MMH-verbatim anchors preserves the compositional
> proportion.

Concrete B10 A/PASS deviations:

| item | verdict | skipped primitive | slot pattern |
|------|---------|-------------------|--------------|
| 佟 (A) | A | ren_side | 亻 at TL/ML/BL far-left column |
| 者 (A) | A | ri | 日 compressed to BC cell (bottom-center) |
| 花 (A) | A | cao_grass_radical | 艹 in top band (y ~110), leave room for 化 |
| 佔 (A) | A | ren_side + bu + kou | multi-slot compression |
| 皃 (A) | A | er_legs | 儿 under narrow 白, compressed |
| 步 (PASS) | PASS | zhi_stop | 止 around C/TR, abuts bottom 少 |
| 别 (PASS) | PASS | kou + li + dao_side | left-block + right 刂 slot |
| 的 (PASS) | PASS | bao/bao_char | 勺 right-half compressed |
| 国 (PASS) | PASS | wei_enclose + wang | inset frame with 玉 interior |
| 把 (PASS retry) | PASS | shou_side | 扌 far-left ML column |

**No new variant primitives promoted this batch.** The curator's
rationale: creating `cao_grass_top.py` / `ri_compressed.py` /
`wei_enclose_compact.py` etc. would REINTRODUCE the very compound-
primitive-standalone-scale problem the deviations are avoiding. The
A-recipe point 4 already codifies "inline base primitives with MMH
anchors" — no variant is needed. Defer promotion until a specific
fresh_component fires on 2+ PASSing attempts across future batches.

### When to use BANK_DEVIATION (drawer decision tree)

1. Compound primitive default anchors match MMH within ±0.15 in
   x_frac AND y_frac for every stroke? → **USE the bank primitive**.
2. Compound primitive would need 3+ anchor overrides? → **SKIP,
   inline via base primitives, write BANK_DEVIATION block**.
3. Bank primitive is chronic (`chronic/*.py`) AND MMH matches within
   the tolerance? → **USE the chronic primitive**.
4. Component is being embedded in a compound with slot compression?
   → **SKIP the compound primitive, inline** (per point 2 above).
5. Component appears standalone or at full-canvas scale? → **USE the
   bank primitive as-is** (that is what it was written for).

### BANK_DEVIATION on FAIL items — what to avoid

Four B10 deviations landed on FAIL/C outcomes with sound reasoning
but insufficient execution:

- **张 (C)**: skipped `chronic/gong_bow.py` because 弓 is left-column
  compressed. The reasoning was CORRECT (chronic gong_bow is
  hardcoded full-canvas 300×300; can't share space with 长 on the
  right). But the fresh inline 弓 had joint misalignment. If future
  attempts skip chronic/gong_bow with the same left-column reasoning
  AND pass, promote `chronic/gong_bow_v2.py` (left-column variant).
- **改 (FAIL)**: skipped `yi_already.py` because target's left is 己
  (not 已) and left-third compressed. Sound reasoning, but the 己
  inline confused 己 vs 已 topology. Errata note added.
- **乩 (retry_3 FAIL)**: skipped bu + kou + yi_hook. Composition
  scaling remained off — X-cross bug persists.
- **那 (retry_3 FAIL)**: skipped fu_right + heng_pie_wan_gou for a
  single-bezier. Cleaner-looking but 阝-right's ear shape lost.

### Refined B10 A-recipe (extends B9 A-recipe)

The 5-point B9 recipe (explicit decomposition + MMH-verbatim anchors +
SELF_CHECK + base primitives + N-joint discipline) continues to hold.
B10 adds:

**6. BANK_DEVIATION signal for compound-slot embedding**. When you
   inline a component that has a compound bank primitive because MMH
   places it in a non-standalone slot, add the `BANK_DEVIATION`
   comment block. This gives the curator evidence to eventually
   promote variants when a pattern proves out. Format below.

**7. Chronic-full-canvas awareness**. `chronic/*.py` primitives
   (pie_radical, dao_char, jiong_frame, gong_bow, ma_horse) all bake
   full-canvas 300×300 anchors. If your target puts 丿/刀/冂/弓/马 in
   less than the full canvas (e.g. left column of a compound char),
   the chronic primitive won't fit — skip and inline with a
   BANK_DEVIATION block. B10 evidence: 张 (C, sound skip but
   execution bug).

**8. X-cross topology remains a chronic weakness**. B10 X-cross
   FAILs: 癶 (retry_3), 処 (retry_3), 乩 (retry_3), 那 (retry_3),
   亥 (retry_2), 亦 (retry_2). The B7r 文 fix (CROSS_ANCHOR shared
   between pie-mid and na-mid) generalizes only when the X-cross is
   isolated. When X-cross sits inside a compound char (那 = 冄 + 阝-r
   with 冄 having internal cross), CROSS_ANCHOR alone doesn't save
   it. No mechanism proposed yet. Consider these items
   TERMINAL_FROZEN candidates after retry_3.

### BANK_DEVIATION block format (recap)

```python
# BANK_DEVIATION
# skipped: <bank_file.py>  (or: "replaced: <bank_file.py> with local render")
# reason: <one-sentence visual/compositional reason — name the slot pattern>
# fresh_component: <name the fresh sub-element, e.g. "cao_grass_top_for_花">
```

Multiple skips OK: list them all under `skipped:`. Keep `reason` to
one-two sentences naming the SLOT (top-band, far-left column,
BC-compression, right-half, inset-frame, etc.). The
`fresh_component` name is what the curator uses to decide variant
promotion — pick a name that describes the SLOT + CONTEXT, not the
specific char.

---

## Retry queue for B11 (curator picks post-B10)

Selection criteria: (a) failed once with a diagnosable fix, (b) not
already at retry_3 saturation, (c) X-cross cluster gets ONE more
chance under a new tactic. B11 queue (13 items):

- **X-cross retry_3+ candidates (SATURATION check)**: 癶, 処, 乩, 那
  — all at retry_3 FAIL. If B11 fails, mark TERMINAL_FROZEN and
  promote `chronic/x_cross_composite.py`.
- **New retries at retry_1**: 佚, 社, 佛, 即, 改, 到, 事, 所, 学.
- **Escalating**: 亥 (→retry_3), 亦 (→retry_3), 更 (→retry_2),
  龹 (→retry_2).

---

## B11 addendum (position 600) — best batch (62% mains, 34% A) + named-pattern codification + X-cross TERMINAL_FROZEN

**B11 outcome**: 31/50 mains (62%; 17 A + 14 PASS) — the strongest
G4 batch on record. Retries 3/17 (18%). BANK_DEVIATION channel:
29/50 uses; 21/29 → A/PASS (72% deviation-to-success, up from B10's
62%). Cumulative through B11: 51% success, 37 A's, 6.7% A rate.

### Refined A-recipe (extends B9+B10; still 8 points, points 6–8 sharpened)

Points 1–5 from B9 hold verbatim. Points 6–8 from B10 also hold with
this B11 refinement:

**6. BANK_DEVIATION for compound-slot embedding** — B11 confirmed. 29/50
   uses; 72% success on deviations. Signal is now proven; use freely
   when the compound primitive's default anchors don't match the slot
   MMH puts the component in.

**7. Chronic-full-canvas awareness** — B11 no new evidence; B10 rule
   holds unchanged.

**8. X-cross topology inside compound char** — **TERMINAL_FROZEN as of
   B11**. 4 items (癶, 処, 乩, 那) exhausted the retry ladder at retry_4.
   Mechanisms tried: CROSS_ANCHOR shared-pixel (works isolated, partial
   compound); single-Bezier through apex (loses accompanying detail);
   stroke_variable_width single-polyline (didn't reach PASS). If your
   B12 target contains X-cross-in-compound and you have time to burn,
   the surest tactic is still CROSS_ANCHOR shared between pie-mid AND
   na-mid — but do not expect PASS unless the surrounding topology is
   simple (isolated X, or X + a small dot).

### Named-pattern codification — 亻 far-left column (10+ passing precedent)

The fresh_component name `ren_side_far_left` (and variants:
`ren_side_farleft_for_*`, `ren_side_far_left_for_compound`, etc.)
recurred **8 times in B11** on PASS/A items (佯 A, 佴 A, 併 A, 佶 A,
佽 A, 侈 A, 佬 PASS, 侍 PASS, 侑 PASS, 佼 PASS + inclusive of B10 佟 A,
佔 A). This is now a stable named pattern.

**Why NO variant primitive was promoted**: creating
`ren_side_far_left.py` would set fixed default anchors that the next
compound char's MMH would not exactly match — the drawer would then
partial-override and hit the p3_char_0252_伊 anti-pattern. Inline with
per-item MMH-verbatim anchors preserves the discipline. The variant
primitive would defeat the mechanism.

**How to draw 亻 in a far-left column slot** (canonical recipe from
B11 A-verdicts):

```python
# Per-item MMH-verbatim anchors — read from dispatcher-injected block.
# Typical B11 slot-pattern (this ranges per item):
#   pie head ≈ TL(0.80-0.95, 0.60-0.75)
#   pie tail ≈ ML(0.15-0.27, 0.87-1.00)
#   shu head ≈ ML(0.60-0.70, 0.40-0.50)
#   shu tail ≈ BL(0.65-0.77, 0.77-1.00)
draw_pie(draw, S1_H, S1_T, head_width=12, tail_width=1, curve=0.10, segments=48)
draw_shu(draw, S2_H, S2_T, width=9)
# BANK_DEVIATION block explaining why ren_side.py was skipped.
```

Same pattern applies to `shou_side` (扌 far-left, cf. 把 B10 PASS),
`chi_step` (彳 far-left, cf. 往 B11 A), `si_silk` (纟 far-left, cf. 线
C — sound skip, execution flaw), `yan_speech` (讠 far-left, cf. 话 B11
PASS), `shui` (氵 far-left, cf. 治 B11 PASS + 油 B11 PASS).

### Other recurring fresh_component names (2× precedent, deferred to variant)

- `cao_grass_top_for_*` — B10 花 A + B11 苦 PASS. 艹 in top-band.
- `kou_bc_compressed_for_*` — B11 治 PASS + 苦 PASS. 口 in bottom-center slot.
- `kou_right_half_for_*` — B11 知 PASS. Right-half compression.
- `mian_top_band_for_*` — B11 实 PASS. 宀 in top-band with room below.
- `ji_gather_top_for_*` — B11 侖 PASS. 亼 stacked-top form.
- `nv_bottom_slot_for_*` — B11 要 PASS. 女 in bottom-slot.

All the same rule: inline per-item MMH-verbatim anchors, do NOT create
a fixed-default variant.

### C-mains diagnosis — where deviation reasoning was correct but execution slipped

B11 had 8 C's (borderline). 5 of 8 used BANK_DEVIATION with sound
slot-reasoning (佻, 佾, 例, 或, 说). The deviation itself was correct;
the FAILURE was in the RIGHT-HALF or interior sub-part where MMH
anchors don't specify enough detail (兆's inner-column spacing, 月's
inner-heng placement, 兑's 3-part stack proportions, 戈's hook angle).

**Rule for B12**: BANK_DEVIATION alone is not sufficient — you also
need explicit sub-part y-band / x-band assertions AFTER you commit
to inlining. See B11 errata C-mains fix-idea list for per-item
recipes queued for retry_1.

### B11 fail patterns (11 mains)

**Cluster A — no-bank both-parts (5 items)**: 疡, 亚, 亟, 侌, 侔. Both
sub-components have no bank primitive AND MMH decomposition is
non-obvious. No mechanism fix — these need decomposition guidance
in the brief.

**Cluster B — compressed right-half with unusual sub-structure (3 items)**:
侉 (夸 = 大+亏), 表 (三+衣), 转 (专). Standard inline path but the
right-half sub-structure is unusual and MMH anchors don't decompose
cleanly.

**Cluster C — X-cross in inner sub-component (2 items)**: 畈 (反 has X),
放 (方 needs 横折钩). Same B7 cluster 4 pattern — hard.

**Cluster D — top-dot dropped again (1 item)**: 疡 (疒 top dot).
Position 350 rule still holds: draw top dots LAST.

### Chronic-mandatory-import — 5th null batch

B7=0, B8=0, B9=0, B10=~1, B11=0 imports on chronic-component mains.
Officially retired as a mandate. Continue to treat chronic/*.py as
REFERENCE.

---

## B12 retry queue (curator picks post-B11)

Selection: (a) items with diagnosable fix, (b) not TERMINAL_FROZEN,
(c) each C given a retry_1 with the errata fix from B11 section.

**B12 queue (14 items)**:

**8 C's from B11 mains → retry_1**: 物, 佻, 佾, 受, 例, 或, 说, 畋.
Each has a concrete B11 errata fix idea. Follow LITERALLY per v8
interpretation-window rule.

**3 FAIL retry_1s carried over → retry_2**: 佚, 社, 佛, 即 (pick top 3 —
suggest 佚 + 社 + 即 as most tractable — 佛 has unusual 弗 structure
worth deferring).

**1 borderline retry_3 → retry_4 or FREEZE**: 亥 (retry_3, C) — one more
attempt with X-cross apex + interior 亠 explicit y-band. If FAIL,
TERMINAL_FROZEN.

**2 fresh retry_1s from B11 FAIL mains**: 转 (专's 撇折 recipe), 侉
(夸 = 大 + 亏 explicit).

**NEW at B12**: a comparison group G5 (G3 memory format + MMH injection)
will be added at B12 to isolate the MMH contribution. This does NOT
affect G4 curation — G4 continues under v13 with unchanged memory
architecture.

---

## B12 addendum (position 650) — regression to mean, ren_side_far_left DEGRADES, right-half is the failure surface

**B12 outcome**: 20/50 mains (40%; 8 A + 12 PASS + 10 C + 20 FAIL).
Retries 5/14 (36%; 0 A, 5 PASS, 1 C, 8 FAIL). Cumulative through B12:
~50% mains success, ~45 A total (~7.5% A rate). Regression toward mean
from B11's 62% best-batch — expected. A-rate still highest of all
groups; format-effect isolation (G5 = G3 memory + MMH ran at 34%/2 A
vs G4 40%/8 A) shows the `fat_line`-per-endpoint-width primitive
delivers **+6 points success and 4× A rate at MMH parity**.

**Post-v14-rollback context**: An earlier B12v1 attempt disabled MMH
for G4, collapsed to 16%, and was rolled back same-day. All B12v1
attempts were deleted; the current B12 is a re-run with MMH restored.
Nothing about G4's memory changed across the rollback.

### The right-half is now the primary failure surface

B12's failure profile inverts B11's. In B11, most FAILs were structural
(X-cross, chronic clusters, no-primitive components). In B12, the
dominant FAIL cluster is **亻+X-with-unusual-right** (6 items: 侉夸,
侷局, 係系, 俅求, 俉吾, 俊夋). In every case the 亻 far-left inline
was executed correctly; the FAIL happened in the right sub-radical
where no bank primitive exists and MMH anchors don't specify enough
mid-stroke detail (curve, hook, taper). BANK_DEVIATION reasoning was
sound; execution slipped in the SECOND half of the character.

**Rule for B13**: when your target is 亻/氵/纟/彳/讠/扌+unusual-right,
the ren_side_far_left inline is a NECESSARY but NOT SUFFICIENT
condition. After inlining 亻 with MMH-verbatim anchors, add explicit
per-stroke width/curve/taper for each right-half stroke — because MMH
gives you endpoints only, not curve amount. Refer to `form_catalog.md`
for per-stroke-class taper defaults if you don't have a bank
primitive.

### ren_side_far_left DEGRADED from 8/8 → 2/9

B11 recorded `ren_side_far_left` at 8/8 PASS/A recurrences. **B12
recorded 2/9 (22%)**: PASS on 侶 and A on 保; C on 便; FAIL on 侯,
侷, 係, 俅, 俉, 俊, and retry-侉. The 亻 slot inline was still done
correctly in every case; the failure surface migrated to the right
sub-radical (see prior section). **Do NOT interpret this as evidence
against ren_side_far_left inline**: the tactic is still correct for
the 亻 slot. The signal is that the right-half needs its own explicit
recipe when no primitive is available.

Named-pattern remains valid; codification unchanged.

### New / strengthened fresh_component names in B12

| fresh_component | B12 evidence | Cumulative precedent | Decision |
|-----------------|--------------|----------------------|----------|
| `shui_far_left_for_*` | 济 A | 治 PASS + 油 PASS + 济 A (3 batches, 3 hits) | Named pattern; still no variant primitive (per B11 rationale) |
| `cao_top_band_for_*` | 草 PASS | 花 A + 苦 PASS + 草 PASS (3 batches, 3 hits) | Named pattern |
| `ri_right_half_for_compound` | 相 A | 是 A (B11) + 相 A (B12) — 2 hits on A | Named pattern |
| `kou_top_band_compressed_for_*` | 保 A + 盅 PASS | 2 hits in B12 alone | Named pattern (new — first codified this batch) |
| `ren_side_far_left_for_*` | 保 A + 侶 PASS | 10+ prior; DEGRADED to 2/9 in B12 | Named pattern (retained; degradation is about right-half not 亻 slot) |

**Decision continues**: promote NONE. Codify all as named patterns.
The B11 rationale (variant defaults would defeat MMH-verbatim
discipline; recurring pattern IS the discipline, not the function
identity) is unchanged. See `evolution.md` position-650.

### The 疒 cluster is emerging (6 items, 0 PASS in B12)

疒-family characters: 疣 FAIL, 疫 FAIL, 疬 FAIL, 疮 FAIL (mains); 疤 C,
疥 C (mains). 疒 has 5 strokes forming a top-left frame (dot + heng +
撇 + 点 + 提). Consistent failure mode: 5-stroke top-frame renders but
interior sub-part loses cohesion because 疒's frame occupies the entire
top-left ~50% of canvas, leaving only compressed interior slot. No
bank primitive for 疒. **Candidate for canonical `chronic/ne_sick.py`
hand-write** if B13 疒 items also FAIL. Not promoting yet (evidence-
driven) but flagging for curator attention.

### 土-left variant: 提 not 横 (form_catalog gap)

城 FAIL: drawer correctly BANK_DEVIATION-skipped tu.py noting the
bottom stroke must be 提 (rising), not 横 (flat), when 土 sits as
LEFT radical of a compound. tu.py bakes flat-bottom. Form-catalog
gap for future entries: `土 as left-radical → s3 = 提, not 横`.

### A-recipe (still 8 points, no change from B11)

B12 confirmed the B9+B10+B11 A-recipe. 8 A-verdict codepaths:
- 6 A used base primitives (pie/shu/heng/na/dian) inline with MMH-
  verbatim anchors. No compound primitives.
- 2 A used compound primitives (ren_side + kou in 信 A; shui skipped
  in 济 A). 信 A is notable: **first B12 A that used ren_side
  directly** — not far-left inline — because MMH placed 亻 in a
  standard TC/C slot for 信. Rule: if MMH puts 亻 in standard
  center-column, use ren_side default anchors; if MMH puts 亻 in
  far-left column, inline pie+shu with MMH-verbatim.

### Retry PASS mechanism — literal errata is strong

5 retry PASSes (0 A, 5 PASS): 物, 佾, 例, 或, 畋 — all C→PASS at
retry_1 via LITERAL errata fix. This is the strongest retry signal
G4 has produced. **When a retry brief includes a literal errata fix
(from a prior batch's curator diagnosis), follow it verbatim — do
not soft-interpret.** All 5 PASSes did exactly this.

Retry FAILs (8) were all cases where the errata fix was directional
("proportions off", "3-tier collapsed") not literal — those needed
mechanism, not verbatim application. Chronic escalations (佚 R2,
社 R2, 即 R2) tried but the underlying components (失-X-cross, 礻-
no-primitive, 皀-complex) resist the retry mechanism.

### X-cross cluster grew: 亥 TERMINAL_FROZEN at R4

亥 R4 FAIL confirmed. TERMINAL_FROZEN executed. X-cross cluster now
5 items: 癶, 処, 乩, 那, 亥. All exhausted retry ladder at R4.
Escalation ROI at R5 is near-zero; requires a new mechanism
(candidate: `chronic/x_cross_composite.py` per-character baked
composite). Not attempting this batch.

---

## B13 retry queue (curator picks post-B12)

Selection: C-mains from B12 (retry_1 with concrete fix idea), plus a
small number of retry-escalations that still have diagnosable fixes.
Excludes TERMINAL_FROZEN items (X-cross cluster including 亥). Also
excludes chronic-difficulty items where the underlying sub-component
lacks a bank primitive AND the errata is directional not literal.

**B13 queue (14 items)**:

**9 C-mains from B12 → retry_1** (literal fix from B12 errata section):
1. **畎** (犬 slot): follow errata literal — inline 犬 as 一 + 撇 + 捺 + 点 (4 strokes) with 大 upper y-band.
2. **畏** (田-top compressed): 田 in y∈[0.02, 0.40], bottom 长 with 撇/捺 legs at y∈[0.55, 1.0].
3. **将** (爿 left, no primitive): inline 爿 as 4-stroke L-frame in x∈[0.0, 0.32]; 夕+寸 in right two-thirds.
4. **疤** (疒 + 巴): 疒 top-frame; 巴 bottom-right slot with 竖弯钩 tail.
5. **疥** (疒 + 介): 疒 top-frame; 介 bottom-right slot; 人-cap + 丨/丶 legs.
6. **度** (广 + 廿 + 又): 又 in bottom-left slot NOT bottom-center; X-cross apex at (BC, 0.35, 0.65).
7. **亲** (立 + 木): 木 bottom y-band [0.55, 1.0]; 一 spans wide; 竖 aligned with 立 vertical axis; 撇/捺 short.
8. **神** (礻 + 申): 礻 left column x∈[0, 0.35] with dot LAST; 申 right two-thirds; central shu spans full height.
9. **便** (亻 + 更): 亻 far-left; 更 right-half; explicit right-half stroke widths per taper table.

**3 retry-escalations to retry_2** (still tractable):
10. **说** (retry_2): B12 R1 was C; 讠 clean-L + 兑 3-part stack more literal — 八 ~15 px each.
11. **佻** (retry_2): B12 R1 was FAIL; 兆's mid-gap needs narrowing further — pull heads to x=0.28-0.32.
12. **侉** (retry_2): B12 R1 was FAIL; 夸 = 大 (top, y∈[0.10, 0.50]) + 亏 (bottom, y∈[0.55, 0.95]) with 亏's hooked shu.

**2 final-chance retry escalations** (TERMINAL_FROZEN if B13 fails):
13. **佚** (retry_3, FINAL): X-cross apex in 失 needs shared-pixel weld.
14. **社** (retry_3, FINAL): 礻 top dot LAST (defensive); 土 right-half slot.

**Deferred / not queued**:
- **癸** (C) — X-cross cluster TERMINAL_FROZEN candidate; skip retry.
- **前, 乹, 疣, 疫, 疬, 疮, 皅, 皈, 侯, 侷, 係, 俅, 俉, 俊, 480_俊,
  城** — B12 FAIL mains; deferred to a future batch or written off
  pending canonical primitives (疒, 皿, 土-左).
- **佛** (retry escalation) — deferred again (弗 structure).
- **佾, 物, 例, 或, 畋** (B12 retry_1 PASS) — graduated; not queued.
- **即** (retry_3) — 皀 complex, deferred pending canonical.
- **转** (retry_2) — 车/专 no primitives; deferred pending canonical.
- **受** (retry_2) — 3-tier chronic; deferred pending mechanism.
- **改, 到, 事, 所, 学** (B11 retry_1 FAIL, un-queued in B12) — deferred.


---

## B13 addendum (position 700) — recipe holds, 疒 named-pattern codified, X-cross cluster grows

**B13 outcome**: 18/50 mains (36%; 6 A + 12 PASS + 11 C + 21 FAIL).
Retries 5/14 (36%; 3 A + 2 PASS). Cumulative through B13:
~48% mains success, ~51 A total (7.8% A rate). Regression from B11's
62% best-batch continues to settle around 36-40% baseline.

**Format-effect isolation** (G5 = G3 memory + MMH ran at 18%/1 A vs
G4 40%/6 A this batch — cumulative G5 = 3.0% A, G4 = 7.8% A):
**format effect at MMH parity WIDENED** — the grid + fat_line
combination is lifting A rate ~2.5× at equal MMH input. Continue the
current mechanism.

### A-recipe unchanged (8 points from B11)

All 6 B13 A's follow the B9-B12 recipe verbatim. No new principle
discovered. Points 1-8 (explicit decomposition + MMH-verbatim +
SELF_CHECK + base primitives + N-joint gaps + BANK_DEVIATION for
slot-embedded + chronic-full-canvas awareness + X-cross-in-compound
TERMINAL_FROZEN) continue to hold.

**B13 evidence of point 2 (MMH-verbatim beats hand-tuned)**:
- 适 A: **used** chuo_walk directly because MMH placed 辶 within ±0.05
  of chuo_walk defaults. Bank primitive fit → USE.
- 都 A: skipped ri + fu_right because MMH compressed both to non-
  standalone slots. Full-canvas defaults would overrun. DEVIATE.
- 特 A: no BANK_DEVIATION — 牜 + 寺 rendered from bank primitives that
  happened to match MMH within tolerance.
- 疽 A: no primitive existed for 疒; inlined 5-stroke frame + 且 all
  MMH-verbatim.

### 疒 cluster — mechanism WORKS; codify as named pattern

**B12 疒 cluster**: 6 items 0 PASS. Flagged as `chronic/ne_sick.py`
candidate.
**B13 疒 cluster**: 8 items → 1 A (疽) + 1 PASS (疸) + 4 C + 2 FAIL.
**75% non-FAIL rate** (vs B12's 33%). The 疒 frame inlined via
5-stroke base primitives + MMH-verbatim endpoints reached A quality.

**Curator decision: NO `chronic/ne_sick.py` promotion.** Same rationale
as `ren_side_far_left`: baked slot defaults would defeat the MMH-
verbatim discipline that made B13's improvement happen. Register as
**named pattern `ne_sick_top_left_frame_for_*`**.

**How to draw 疒 in a compound char** (canonical recipe from 疽 A + 疸 PASS):

```python
# 5-stroke top-left frame (all MMH-verbatim from dispatcher):
# s1  top 点  (TC region, small dot)   — DRAW LAST (defensive per B6)
# s2  top 一  (TL→TC, short heng)
# s3  long 撇  (ML→BL sweep, tapered)
# s4  inner 点  (ML region, small dot)
# s5  inner 提  (BL→ML rising ti)
# All 5 anchors from MMH block. Interior sub-radical fills the
# BOTTOM-RIGHT SLOT (typically x∈[0.35, 0.95], y∈[0.30, 1.0]).
# Interior slot needs per-character MMH-verbatim endpoints AND
# per-stroke-class taper — do NOT try to compress a full-canvas primitive
# into the slot.
```

**疒 FAIL diagnosis (2 items)**:
- 疱 (包 inner): 5-stroke 巳 got compressed into 勹 outer's tight
  bottom slot; bao_char.py full-canvas would have overrun. Inline was
  correct choice; execution needs tighter y-band on 巳.
- 疳 (甘 inner): 5-stroke 2-vertical-grid; verticals collapsed together.
  Needs explicit x-band assertion for the two shu strokes.

### Right-half taper is still the primary failure surface

Cluster A of B13 FAILs (7 items: 俑, 俘, 俜, 俛, 俞, 除, 复) all have
correct 亻/阝-left slot execution but FAIL on right sub-radical.
Same pattern as B12. MMH gives endpoints only — not curve amount,
not hook depth, not taper rate. Two batches now on this cluster
without a fix.

**Rule for B14+**: when your target is `亻/氵/纟/彳/讠/扌 + unusual-right`
AND no primitive exists for right sub-radical:
- Inline 亻 via `ren_side_far_left` pattern (correct in every B12/B13 case).
- BEFORE drawing right half, consult `form_catalog.md` for per-stroke-
  class taper defaults (pie head_w 12 tail_w 1, na head_w 3 peak_w 14
  tail_w 1, etc.).
- Add explicit `head_width=` / `tail_width=` / `curve=` per right-half
  stroke — MMH won't specify these.
- If right sub-radical is 3+ strokes without a primitive, treat it as
  a NEW FAILURE MODE and log to `sandbox.md` — accumulating evidence
  toward a per-stroke-class taper table upgrade.

### X-cross cluster grew: 佚 → TERMINAL_FROZEN at R3

Cluster now **6 items**: 癶, 処, 乩, 那, 亥, 佚. All exhausted retry
ladder. R4+ ROI near zero without new mechanism. Candidate mechanism
still `chronic/x_cross_composite.py` — per-character baked composites.
Not attempted this batch.

### 礻-compound cluster candidate (new — 社 TERMINAL_FROZEN)

社 R3 FAIL → TERMINAL_FROZEN. 礻 dot-LAST defensive rule works; the
FAIL was 土 slouching into 礻's slot. This is a **compositional-
coherence** failure, not a frame failure. Watch for 神 (also C in B13
R1) and other 礻-compound chars in future batches. If 2+ more 礻-
compounds hit R2+ FAIL, consider `chronic/shi_altar_compound.py` for
the LEFT slot only (礻 as left-column radical with slot-width parameter).

### Retry mechanism — literal errata continues to work (5/14 R1 graduations)

B13 retry graduations: 畎 A, 将 A, 度 A, 亲 PASS, 说 PASS (R2).
All 5 applied a LITERAL geometry fix from B12 errata.

The 6 R1/R2 FAILs (畏, 神, 佻, 侉, 佚, 社) had directional errata
("proportions off", "too weak") or were chronic (X-cross, 礻-compound).
**Rule confirmed for B14: only queue retries with LITERAL errata; skip
directional-errata items unless mechanism is upgraded.**

### Named-pattern registry (post-B13)

| fresh_component | B13 hit | Total precedent | Status |
|-----------------|---------|-----------------|--------|
| `ren_side_far_left_for_*` | 6+ B13 mains (俐, 俚, 俑, 俘, 俜, 俛, 便, 519_候…) | 12+ batches | named pattern; no variant |
| `ne_sick_top_left_frame_for_*` | 6/8 B13 items PASS-or-better | first codified this batch | **NEW named pattern**; no variant |
| `shui_far_left_for_*` | (海 FAIL — not a hit; but pattern still valid for `shui_far_left`) | 3 batches, 3 hits before B13 | named pattern (no B13 recurrence; watching) |
| `cao_top_band_for_*` | no B13 hit | 3 batches, 3 hits before B13 | named pattern (no B13 recurrence; watching) |
| `ri_right_half_for_compound` | no B13 hit | 2 batches, 2 A's | named pattern (watching) |
| `ri_bl_compressed_for_都` | 都 A | first codified this batch | slot-specific; watching for reuse |
| `fu_right_narrow_column_for_都` | 都 A | first codified this batch | slot-specific; watching for reuse |
| `dao_side_tight_pair_for_3radical` | 俐 A | first codified this batch | slot-specific; watching for reuse |

**Decision continues (5 batches now)**: promote NONE. Codify all as
named patterns. Variant primitives would defeat the discipline that
produces the improvements.

### Solo-wins observation — Obs-01 (no curator action)

3 G1 solo-A verdicts in B13 (俜, 畟, 热). G4 got C on 热 (best of
memory groups); FAIL on 俜 and 畟. Naive rendering beats memory-
directed rendering on some items where memory pulls the drawer down
a wrong compositional path. Logged to root `OBSERVATIONS.md`. No G4
memory action; noting for awareness.

---

## B14 retry queue (12 items)

See `errata.md` B14 section for per-item literal fix. Composition:
- 5 fresh C-mains → R1 (怎, 能, 乘, 候, 热)
- 5 疒-cluster C-mains → R1 (疰, 疴, 疹, 痂, 速) — testing named-
  pattern discipline
- 2 疒-escalations → R2 (疤, 疥)

Excludes: 便/神 (directional errata); 佻 R3, 侉 R3, 畏 R2 (chronic);
21 FAIL mains (defer pending mechanism); 佚/社 (TERMINAL_FROZEN).
