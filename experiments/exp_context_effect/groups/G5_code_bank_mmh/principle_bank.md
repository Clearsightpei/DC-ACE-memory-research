# G5 principle bank

*Curator writes here. Promoted principles (P-DEV*, retrieval rules, cross-batch generalizations) live here as they emerge.*

*Bootstrap 2026-08-08: seeded light. B1 (2026-08-08): +2 principles, based on B1 evidence.*

---

## Retrieval / composition principles

**P-RET-001** — For any dispatched item whose MMH block names a stroke class we already have as a bank primitive (see `drawer_memory.md` retrieval table), consult the bank first. Skip only for real compositional mismatch, and log via `BANK_DEVIATION`.

**P-RET-002** — For radicals appearing as sub-components of Phase-3 characters, prefer the whole-radical position-signature primitive (`draw_bi`, `draw_ba`, `draw_shou`, etc.) over re-composing from stroke primitives. Reason: the composite already encodes the joint spacing that PASSed.

**P-RET-003 (NEW B1)** — When a BANK_DEVIATION at Batch N produced a fresh sub-element that later batches will plausibly reuse, curator promotes it as a **new stroke primitive**, not a variant. B1 promoted 6: `ti`, `shu_zhe`, `heng_zhe_gou`, `heng_pie`, `ping_na`, `heng_zhe_box`. Rule: if two future items would call the fresh element, promote it. Do not wait for evidence of two calls before promoting — the point of the bank is proactively covering compound classes MMH names.

---

## MMH-vs-GT priority

**P-MMH-001** — When MMH-derived anchors and the GT PNG disagree on stroke placement (rare, but see 丿 in bootstrap), the GT is authoritative. MMH gives the median endpoint pair — accurate for path direction but not always for calligraphic silhouette centroid. The judge scores from GT, not MMH.

**P-MMH-002 (NEW B1)** — For compound strokes (横折钩, 竖折, 横撇, etc.), MMH gives the median line of the ENTIRE compound — not the corner or the endpoint of each sub-segment. The drawer must infer the corner position from the GT visually. Corollary: 力 (s1 head at MMH ~(67,147) but GT ~(95,105)) and 艹 (verticals extending well past MMH endpoints) both PASSed only after this override. B2 dispatchers should treat compound-stroke MMH endpoints as approximate.

---

## Rendering / decoration principles

**P-DEC-001** — Hook decorations (顿笔 entry ticks, terminal hooks) must be part of the same continuous stroke path, not disjoint line segments. Failure mode observed: 亅 bootstrap C came from rendering a top tick as a diagonal line disconnected from the shaft. R1 PASS confirmed the fix: single continuous curl-into-shaft.

---

## Composition principles

**P-COMP-001 (NEW B2)** — When MMH's stroke count for the current item differs from a plausibly-relevant whole-radical primitive's stroke count, compose from stroke primitives instead of calling the wrong-count radical. Validated by 日 (4 strokes) not calling draw_kou (3 strokes) and by 囗 (3 strokes but big-canvas anchors) not calling draw_kou either. Rule: **MMH stroke count and MMH endpoint spread jointly override any whole-radical primitive whose bakes-in geometry disagrees**.

**P-COMP-002 (NEW B2)** — Two independent BANK_DEVIATIONs on the same fresh_component are sufficient to promote that fresh_component as a new stroke primitive at curator time. Validated: xie_gou promoted after 弋 s2 + 戈 s2 both PASSed inline. Do NOT wait for a third occurrence.

**P-COMP-003 (NEW B2)** — Sibling minimal-pair failures cluster on distinguishing feature. In B2: 户/尸 (top dot), 攴/攵 (卜+又 vs pie+heng+pie+na), 弋/戈 (3 vs 4 strokes). When a drawer knows the sibling pair exists, PASS rate is much higher. When the drawer treats the item in isolation, it collapses toward the more-common sibling. Curator responsibility: extend `sibling / minimal-pair notes` in drawer_memory.md after every batch where a new distinguishing feature is observed.

---

---

## A-recipe principles (NEW B3, from first 4 A verdicts)

**P-A-001 (NEW B3)** — Identity-call bank reuse can lift PASS to A. When
a Phase-3 char is literally the same shape as a PASSed Phase-2 radical
AND MMH anchors match the bank primitive's baked-in geometry exactly,
calling `draw_<radical>(d, ox=0, oy=0, scale=1.0)` produces A quality —
not just PASS. Evidence: p3_char_0011_人 A (draw_ren) and p3_char_0017_又
A (draw_you). Both were zero-parameter identity calls of B1 primitives.
Implication: **the bank is not merely error-reducing; it is a quality
lever**. Corollary: when the drawer sees MMH anchors matching a bank
primitive within ~5 px, use the bank primitive; do NOT re-inline "for
customization" — that discards the A quality baked into the primitive.

**P-A-002 (NEW B3)** — Meticulous inline composition can also reach A
when (a) stroke count matches MMH exactly, (b) MMH anchors used verbatim
or overridden with justified per-stroke reason, (c) EVERY stroke has
explicit taper (w_head != w_tail — no default widths), (d) compound
strokes use multi-segment bezier with explicit control points, (e) for
crossing-X patterns, bow_perp is differentiated per stroke so the two
strokes read as distinct swings. Evidence: p2_radical_128_爻 A (4-stroke
stacked-X composition; bow_perp = -14/-8/-18/-10) and p3_char_0009_了 A
(BANK_DEVIATION with 3-bezier inline 弯钩 crafting).

## Composition principles (extended B3)

**P-COMP-004 (NEW B3)** — Composed primitives that share an alignment
constraint should be called through a single wrapper, not summed from
independent pieces. Evidence: 宀 R2 PASSed by calling `draw_mi_cover` for
the left-dian + roof combined (they must align), then adding the top
dian separately. R1 FAILed because the two dians and roof were drawn
independently and did not visually cohere. Applied in the promoted
`draw_mian_roof` primitive.

**P-COMP-005 (NEW B3)** — When MMH's stroke count for the current item
differs from a plausibly-relevant whole-radical primitive's stroke count,
compose from stroke primitives (already stated in P-COMP-001), **BUT**
if the shape IS structurally identical to a PASSed sub-radical, use the
whole-radical primitive with (ox, oy, scale) — see P-A-001. Reconciling
the two rules: **structural identity (same stroke count + same MMH
anchors) → use whole-radical primitive**. Anchor-spread or count
mismatch → compose from stroke primitives.

---

---

## B4 (2026-08-08) — post-B4 evidence

**P-A-003 (NEW B4) — A-recipe qualifier: identity-reuse and meticulous-inline
both continue to lift a Phase-3 char to PASS reliably, but B3's A-verdict
lift does not automatically generalize to 3+ stroke chars.** Evidence: B4
dispatched 11 identity-call P-A-001 attempts (勹/匕/大/山/口/干/门/宀/女/艹/小)
and 1 P-A-002 attempt (千); all 12 landed PASS, 0 landed A. B3's 4 A verdicts
were on 2-stroke chars (人, 又) or on chars with an explicit 4-stroke
composition (爻, 了 with meticulous bezier crafting). The **A-quality lift
requires either (a) extreme simplicity (< 3 strokes) or (b) explicit
GT-vs-render post-composition tuning** — not merely a clean bank call.
Corollary: drawers should continue applying P-A-001 and P-A-002 as the
default recipe (they produce clean PASSes and prevent FAILs) — but should
not expect A verdicts from identity-reuse alone. If capacity permits, a
post-render diff pass against GT (tweaking bow/taper/stroke-weight to
match the visible GT silhouette, not just MMH endpoints) is the candidate
route to A. Test in B5+.

**P-RET-004 (NEW B4) — Bank primitives baked for a Phase-2 radical context
may need per-composition re-tuning at Phase-3.** Evidence: 也 FAILed
despite calling draw_shu_wan_gou with MMH anchors — the primitive's
default `bottom_extra=60, knee_ratio=0.75` is calibrated for 匕/儿's
compact bottom sweep, but 也's wrap extends much further right (wants
`bottom_extra=75+, knee_ratio=0.62`). Similarly 与 FAILed because
draw_heng_zhe_gou defaults are tuned for 力's compact size, not 与's
full-height frame. Rule: **when calling a bank primitive with MMH
anchors that span a noticeably different aspect than the primitive's
promotion context, pass explicit tuning parameters (bottom_extra,
knee_ratio, hook_len, etc.) — do not rely on defaults.** This does NOT
require BANK_DEVIATION (the primitive is still being called; only its
knobs are tuned) — but the drawer should note the tuning in a code
comment for the curator.

**P-COMP-006 (NEW B4) — Retry escalation has diminishing returns beyond
R2.** Evidence: B3 R2 rate was 5/6 = 83% PASS; B4 R2 rate collapsed to
5/36 = 14% (14 R2 FAILs, 8 R2 C's). The B3 R2 successes (门/讠/阝/宀/女)
were all cases where a **specific stroke primitive was newly added to
the bank between R1 and R2** — MMH-injected structure + new primitive
did the work. B4's R2 items had no such newly-promoted stroke primitive
between rounds (bank grew radicals + wan_gou/heng_zhe_ti/pie_zhe in B3,
but the remaining R2 items — 旡/气/火/巳/贝/厄/攴/方 — all need
still-missing compound classes like heng_xie_wan_gou, 卧钩, 3-turn
compound frames). Rule: **when queueing an R2 retry, verify that a new
bank primitive (or a specific curator trajectory-diff) has been added
since R1. If neither has changed, R2 will FAIL/C again — terminal-freeze
the item instead of burning a slot.**

---

## B5 (2026-08-08) — post-B5 evidence

**P-COMP-007 (NEW B5) — Aggressive proactive promotion of high-reuse missing
compound classes on 1st successful BANK_DEVIATION.** Evidence: B5 promoted
`wo_gou.py` (from p3_char_0112_心 only 1 PASSing DEVIATION) and
`heng_zhe_wide.py` (from p3_char_0122_五 only 1 PASSing DEVIATION), citing
P-RET-003. Rationale: for compound classes MMH names as a distinct stroke
type (卧钩, 横折 wide-corner variant), the 1st PASS *is* proof the
geometry works; the general P-COMP-002 "wait for 2 DEVIATIONs" rule is
correct for *character-specific* fresh components but too conservative
for reusable stroke classes. Rule: **when the fresh_component matches a
distinct MMH stroke class NAMED in the injection, promote on 1st
PASSing DEVIATION**; when it's a character-specific composition
(*_for_*_名前), continue to require 2 DEVIATIONs per P-COMP-002. Test:
if either B5 promotion goes unused through B7, retire.

**P-A-004 (NEW B5) — A-drought at depth: identity-call P-A-001 stops
producing A verdicts once the item pool crosses ~4 strokes with no
1-2-stroke identity candidates left in the batch.** Evidence: B5 dispatched
ZERO 1-2 stroke char items (idx 084-133 all Phase-3, mostly 3-4 strokes);
27 PASSes but 0 A verdicts. Batch-level candidates for P-A-001 lift
(文/日/中/工 — all identity-called existing bank primitives) all landed PASS,
consistent with P-A-003's "identity-reuse alone doesn't reach A at 3+
strokes". Cross-batch pattern: B3 had 4 A's on 2-stroke chars; B4/B5
have 0 A's with mostly 3-4-stroke chars. Corollary: A-drought is
STRUCTURAL to the curriculum, not a drawer-discipline collapse.
**Practical implication for curator**: do not diagnose A-drought as a
regression until the post-render GT-diff tuning hypothesis
(from P-A-003) is actually tested in a batch. Also: watch B6 items
idx 134-183 — if any are simple radicals with no siblings, they are the
next A-lift candidates.

**P-COMP-008 (NEW B5) — Compound-class terminal-freezes propagate to
compound-derived characters unless the bank is extended between
rounds.** Evidence: 9 Phase-2 items were terminal-frozen at R2 across
B3/B4/B5 (爪, 水, 瓦, 牙, 乜, 乃, and the 儿/几/九 hook-family). Every
one of those hook-family retries R2-FAILed with the same missing
compound class (heng_zhe_wan_gou). Corollary: promoting a still-missing
compound class BEFORE running R2 on those items would have been the
mechanism-change P-COMP-006 requires. **Rule for curator**: whenever
a terminal-freeze pattern points at a single missing bank primitive,
elevate the promotion decision from evidence-driven ("wait for a
PASS") to hypothesis-driven ("promote inline reference spec into
sandbox as a *candidate* primitive; if any B_{N+1} attempt PASSes with
it, promote to bank")*. Sandbox now carries the `heng_zhe_wan_gou`
candidate spec (see B5 postmortem).

---

## B6 (2026-08-08) — post-B6 evidence

**P-A-005 (NEW B6) — RETRY channel can produce A verdicts when the trajectory-diff
specifically addresses the calligraphic weight AND joint geometry issues (not
just endpoint anchors).** Evidence: p3_char_0089_义 was a B5 main C; B6 R1
became the **first-ever A verdict from a retry**. The main C's failures were:
(a) thin/mispositioned dian, (b) pie/na crossing off-anchor. Retry_1 fixed all
three via SPECIFIC parameter changes: dian tapered (w_head=3, w_tail=9) at
MMH-anchored ML position; pie called with **NEGATIVE bow_perp=-45** so
mid-belly is pushed DOWN-RIGHT toward BC crossing anchor; na called with strong
tail-thickening (w_head=4, w_tail=12) and bow_perp=+20 so mid crosses pie
near BC. Two lessons: (1) A-recipe extension for 3-stroke chars requires
BOTH taper differentiation AND deliberate bow to force joint geometry — not
just verbatim MMH anchors. (2) Retry channel is a viable A route when the
trajectory-diff is mechanism-specific (not just "move it 10 px right"). This
also updates P-COMP-006: R2 doesn't help only "no mechanism change" — but
R1 CAN help even without new bank if the trajectory-diff surfaces a specific
calligraphic mechanism the main missed.

**P-COMP-008 UPDATE (B6 evidence): hypothesis-driven candidate spec FAILED
for 5 retry items** (乌, 仇, 仉, 冗, 马). The sandbox `heng_zhe_wan_gou`
spec was made available to B6 R1 drawers via retry_log/errata hints. 4/5
inlined it; all 4 FAILed. 马 inlined a distinct `heng_zhe_zhe_gou`
(down-left hook), also FAILed. This **rules out the "just missing primitive"
hypothesis** for these items — the failure is composition-level, not just
missing bank primitive. The `heng_zhe_wan_gou` candidate spec remains in
sandbox for possible future PASS (a Phase-3 char with cleaner composition
may still cash it in), but P-COMP-008 elevation from evidence-driven to
hypothesis-driven does NOT justify **promoting** without a PASSing case.
Concretely: **do NOT hand-craft the primitive spec into the bank without a
PASS**, because our test showed the missing-primitive hypothesis was
insufficient. The composition-level issue is real.

Note: this does not retract P-COMP-008 (the mechanism of "elevate to
hypothesis-driven candidate in sandbox" is still valid). It just means for
this specific family the hypothesis was tested and refuted. Continue to
elevate other missing-primitive candidates the same way; but recognize
that a failed candidate spec is EVIDENCE against, not just a null result.

---

---

## B7 (2026-08-08) — post-B7 evidence (biggest cross-group delta yet: +34 pts vs G3)

**P-A-006 (NEW B7) — "MMH-anchor verbatim + stroke-primitive layer" is a
new A-recipe route for 5-6 stroke chars.** Evidence: ALL 5 A verdicts in
B7 (业, 仟, 仨, 冉, 乓) followed the same pattern:
1. Read MMH endpoint anchors verbatim (no override / no re-derivation).
2. Call **stroke-signature** bank primitives (`draw_pie`, `draw_shu`,
   `draw_heng`, `draw_dian`, `draw_heng_zhe_gou`) with those anchors as
   `head`/`tail`/`corner` arguments.
3. **Refuse the whole-radical route** — even when a plausible whole-radical
   primitive existed (`draw_ren_left` + `draw_qian_thousand` for 仟;
   `draw_ren_left` + `draw_san_three` for 仨; `draw_ba` for 业's top-dians),
   the drawer chose to inline stroke-level and skipped the composite. The
   docstrings explicitly justify this ("bypasses double-transform artifacts",
   "MMH gives exact endpoints; want 1:1 pixel match without scale/shift").

Interpretation: whole-radical primitives with `(ox, oy, scale)` signature
introduce **cumulative offset error** when nested inside multi-radical
Phase-3 compositions (each sub-primitive's internal geometry is baked at
its promotion context; scaling breaks joint welds; two composed primitives
double-transform). Stroke-signature primitives with `(head, tail, ...)`
signature align 1:1 with MMH-injected endpoints and preserve joint
geometry exactly. This is a **calligraphic-fidelity ceiling** — the A
verdict requires 1:1 endpoint fidelity, and whole-radical composition
cannot deliver that at 5-6 stroke complexity.

**Corollary for drawers**: for 4+ stroke Phase-3 chars with MMH-clean
endpoints, prefer stroke-primitive composition over whole-radical
composition, EVEN IF a whole-radical primitive matches. Use whole-radical
primitives (P-A-001, P-RET-002) for 1-3 stroke identity chars and for
positional cases (where the primitive occupies its full 300×300 canvas
naturally). Use stroke-primitive layer (P-A-006) for multi-component
chars where anchor fidelity determines PASS/A.

**Corollary for curator**: promote whole-char primitives generously
(they're A-recipe records), but do NOT expect them to be identity-called
in downstream L-R compositions — expect their internal endpoints to be
consulted (or the file re-read) rather than the wrapper being invoked.

**Extends** P-A-001, P-A-002, P-A-003, P-A-005 (all remain valid recipes;
P-A-006 is the newly-identified route for 5-6 stroke chars specifically).
**Does NOT retract** P-A-004 (A-drought at depth) — A-drought was defined
BEFORE the P-A-006 recipe was crystallized; B7 evidence shows depth
per se is not the barrier — the routing choice is.

---

**P-COMP-009 (NEW B7) — Double-transform failure on whole-radical L-R
compositions.** Evidence: 边 (辶+力 wrap) FAILed calling
`draw_chuo_walk(scale=0.9)` + `draw_li_power(scale=0.65, ox=+60)`. Both
primitives were internally correct; the composition read as two mis-scaled
sub-figures glued together. Diagnosis: each whole-radical primitive's
geometry is baked at its promotion canvas (300×300); scaling shrinks
strokes AND joints uniformly, but Phase-3 L-R compositions need
component-specific proportion (e.g., 辶 wants baseline stretch, 力 wants
compact height). The uniform scale knob can't retarget both.

Rule: **when a Phase-3 char is L-R composition of TWO whole-radical
primitives, prefer inline stroke composition using MMH endpoints for
whichever component the composition compresses/asymmetrizes**. Only call
whole-radical when the component appears at its "native" size (usually
top-position 亠/艹/宀, or standalone). This refines P-RET-002.

Also relates to `p3_char_0187_仡` FAIL (draw_ren_left + inline 乞) and
`p3_char_0214_记` FAIL (draw_yan_speech + inline 己) — both are
whole-radical LEFT + inline RIGHT compositions, both FAILed on the inlined
right component. The problem is not just the inline geometry (drawers
attempted P-A-006-style stroke composition); it's that the LEFT primitive
consumed proportion budget the RIGHT inline couldn't recover.

---

**P-COMP-010 (NEW B7) — X-cross cluster (癶/矢/失/処/乩/那) is NOT
categorically frozen in G5.** Evidence: of 6 B7 X-cross-family items,
G5 got 3 PASS + 1 C + 2 FAIL. Compare G4's chronic-freeze reputation on
the same cluster (see cross-group observations). Diagnosis: MMH auto-
injection gives explicit per-stroke pie/na endpoint anchors that let
G5 drawers place the crossing at the MMH-anchored joint point rather
than guessing from silhouette. The 2 FAILs (処, 那) failed on OTHER
components (chronic 几-hook family, 阝-position issue), not on the
X-cross itself.

Corollary: X-cross weld quality is bounded by anchor precision — MMH
gives that in G5. This is a mechanistic **cross-group finding** worth
recording: MMH's compensation is strongest for cluster-blocked failure
modes that have clean median-endpoint geometry. It is weakest for chronic
compound-stroke gaps (heng_zhe_wan_gou family — still frozen).

---

**P-RET-005 (NEW B7) — Retry-PASS from sibling-pair discipline
(without new bank).** Evidence: 比 R1 PASSed by rebalancing left/right
竖弯钩 halves per B6 sibling-pair note; no new bank primitive; no
mechanism-change other than "read the sibling-pair table and apply".
Refines P-COMP-006 further (which already got the P-A-005 refinement):
R1 can PASS from either (a) new bank added between rounds, (b) mechanism-
specific trajectory-diff (per P-A-005), OR now (c) applying an existing
sibling-pair/calibration note the main-attempt missed. All three are
"mechanism-changes"; the P-COMP-006 warning still holds for R1/R2 with
no mechanism-change of any of the three kinds.

---

---

## B8 (2026-08-09) — post-B8 evidence (first fair-A batch: PASS = 40% vs G4 40%, but A = 0 vs G4 10)

**P-A-007 (NEW B8) — P-A-006 overshoot guardrail: use whole-radical
primitive when it matches the structural sub-component; refuse only when
MMH-endpoint fidelity is the ceiling.**

Evidence: 4 of B8's 20 FAILs were cases where drawers applied P-A-006's
"refuse whole-radical" rule to characters where the bank primitive was
the correct choice:
- **军** — drawer inlined 6 strokes; NEVER imported `mi_cover.py` or
  `che_car.py` (both bank since B1/B2). Both would have served.
- **名** — inlined all 6; NEVER imported `kou_mouth.py` (bank since B1).
- **成** — inlined; did NOT use `ge_dagger.py` (bank since B2).
- **西** — inlined; did NOT identity-call `si_four.py` (B7) despite
  structural similarity to 四.

Diagnosis: B7's P-A-006 (which routed 5 A verdicts via stroke-primitive
layer refusing whole-radical composites) crystallized on grid-like /
straight-stroke L-R chars where whole-radical composition genuinely
double-transformed. Carrying that recipe as an ABSOLUTE rule into B8's
mixed pool caused 4 avoidable FAILs where the whole-radical primitive
was NOT going to double-transform (because the sub-component occupies
its natural aspect within the target char).

**Rule (P-A-007)**:
1. If the target char contains a sub-component whose structural identity
   matches a bank whole-radical primitive AND the sub-component sits at
   ~native scale (>= 0.6, no severe aspect skew), CALL the bank primitive
   with `(ox, oy, scale)` tuning. Inline only the connecting strokes.
2. If the sub-component must be severely compressed (< 0.55 scale) or
   aspect-skewed (L-R with dominant other half), fall back to P-A-006
   stroke-primitive layer.
3. If the char is grid-like or has stroke-count exactly matching MMH
   without whole-radical structural units (业/仟/冉/乓/仨 pattern), use
   P-A-006.

**Does NOT retract P-A-006** — the P-A-006 domain (X-cross, grid-like,
straight-stroke L-R) is still where the A-recipe lives. P-A-007 scopes
P-A-006 to prevent the "always refuse whole-radical" overshoot pattern.

**Corollary for curator**: when reviewing a FAIL, check whether the
drawer's `generated.py` imports the bank primitives that structural
sub-components would have used. If not, the FAIL is a P-A-007 candidate
mechanism-change for retry (queue with instruction to call the specific
bank primitive).

---

**P-COMP-011 (NEW B8) — 亻+X 6-stroke P-A-006 recipe generalizes ONLY
when X is straight-stroke composable.**

Evidence: 7 of B8's 20 FAILs are 亻+X 6-stroke chars where all 7 drawers
correctly applied P-A-006 (verified: BANK_DEVIATION headers refusing
`draw_ren_left`; stroke-primitive layer). All 7 still FAILed because X
contains a hook-compound stroke class:
- 伄 (亻+吊 — 冂+巾 with hook), 伉 (亻+亢 — shu_wan_gou wide-wrap),
  伙 (亻+火 — pie-dian ordering), 伢 (亻+牙 — heng_zhe compound + shu_gou),
  伧 (亻+仓 — wraparound cover), 佤 (亻+瓦 — wave-hook chronic),
  伎 (亻+支 — 十-cross + 又).

Contrast with 亻+X PASSes in the SAME batch (仲 亻+中, 仳 亻+比, 仵 亻+午,
伊 亻+尹, 伐 亻+戈, 伛 亻+区, 伦 亻+仑, 任 亻+壬) — all P-A-006, all X is
straight-stroke composable.

Extends B7's `qian_person.py` (仟 A) template:
- **仟 A precedent** = 亻+千 (straight-stroke); works via P-A-006.
- **B8 boundary** = if X has any hook-compound, P-A-006 doesn't reach PASS.

**Rule (P-COMP-011)**: For 亻+X 6-stroke L-R chars, before applying
P-A-006, verify X's stroke inventory. If (heng/shu/pie/na/dian/ti only),
P-A-006 is the recipe. If any hook-compound (heng_zhe_wan_gou,
heng_xie_wan_gou, wo_gou, wraparound), the recipe won't PASS without
bank extension covering that hook-compound OR without P-A-007-style
whole-radical primitive call (see P-A-007).

**Retry queue implication**: 亻+X hook-compound-right FAILs should NOT
be queued for retry per P-COMP-006 (no mechanism-change available)
UNTIL the relevant hook-compound primitive lands PASS elsewhere.

**Extends**: P-COMP-009 (double-transform on L-R) and P-A-006 (A-recipe
route). Together with P-A-007, completes the L-R routing decision tree.

---

**STRUCTURAL A CEILING observation (NEW B8, not a principle but a
recorded curriculum finding)**:

B8 was the first fair-A comparison batch (per user note: G4/G5 A rates
only comparable from B9 onward, but B8 approximates it). On identical
items:

| Group | PASS | A | Format |
|-------|------|---|--------|
| G3 | 28% | 0 | free-form + code, no MMH |
| G4 | 40% | 10 | MMH + grid + `fat_line` per-endpoint width |
| G5 | 40% | 0 | MMH + code, uniform PIL line width |

Same PASS rate for G4 and G5 (both MMH-injected); G4 gets 10 A while
G5 gets 0. **The A-quality delta is entirely attributable to rendering
format, not memory format**. G5's uniform PIL line width cannot produce
the calligraphic weight distribution the judge rewards with A on 6-stroke
chars.

This means: (a) P-A-004 (A-drought is STRUCTURAL) remains correct; (b)
P-A-006 exceptions (5 A on B7 5-6 stroke chars) were where anchor
precision maxed G5's format ceiling; on 6-stroke chars without that
headroom, G5 tops out at PASS regardless of drawer discipline; (c) the
research paper can now cleanly state that MEMORY FORMAT (code vs anchors)
is neutral for PASS but DECISIVE for A only in combination with per-
endpoint width rendering.

**Practical implication for future curators**: do NOT diagnose 0-A batches
as a discipline regression. Sample 3 PASSes for taper/joint discipline;
if intact, note the ceiling and move on. Only investigate 0-A as a
regression if PASS discipline is also collapsing.

---

**P-A-007 (SHARPENED B9) — validated 3/4 on R1 mechanism-change test;
promoted from guardrail to primary retrieval rule with hard-check.**

B9 R1 outcomes on the 4 P-A-007 test items:
- **军 R1 PASS** — drawer called `draw_mi_cover` + `draw_che_car` per queue
  instruction. Bank primitives carried MMH-tested joint geometry that
  stroke-inline had missed. **Validates rule 1**.
- **成 R1 PASS** — drawer used `draw_xie_gou` bank primitive + tuned bow /
  hook. Bank compound-stroke was correct call. **Validates rule 1**.
- **老 R1 PASS** (MEDIUM-tuning arm) — drawer tuned `shu_wan_gou` params
  per queue. Not P-A-007-strict but same "use bank primitive with tuning
  instead of inlining" mechanism. **Validates by analogy**.
- **名 R1 FAIL** — drawer called `draw_kou` for bottom, still FAILed;
  likely 夕-half proportion issue (not the P-A-007 lever).
- **西 R1 FAIL** — drawer identity-called `draw_si_four`, still FAILed;
  西 inner-mark differs from 四 (top bar + inner shu_zhe direction) —
  sibling adaptation needed beyond identity call.

Net: 3 R1 PASSes (军/成/老) validate the "use bank primitive when structural
match" mechanism. 2 R1 FAILs (名/西) show P-A-007 is necessary but not
sufficient — sibling-adaptation still needed for sub-components that share
structure but differ in interior marks.

**Sharpened rule (P-A-007-v2)** — HARD CHECK to run mentally before
committing an inline stroke-composition:

> Before writing any inline stroke for a sub-component, ask:
>   Q: Does this sub-component correspond to a bank whole-radical / whole-char
>      primitive AND sit at a scale within [0.55, 1.2] of native aspect?
>   If YES → CALL the bank primitive with (ox, oy, scale). Do NOT inline.
>   If NO  → inline via P-A-006 stroke-primitive layer with MMH anchors.

If the drawer omits this check and inlines a sub-component that has a
matching bank primitive at reasonable scale, curator MUST flag the FAIL
as P-A-007 mechanism-change candidate and queue a retry with explicit
"call the bank primitive" instruction.

**Structural evidence that supports the sharpen**: 4 of B9's A verdicts
followed P-A-007's letter-or-spirit:
- **龹** (A) — inline-only for a top-radical no bank has, all stroke
  primitives at MMH anchors (P-A-006 pure; A ceiling broke because s5
  bent-pie curvature was hand-tuned to weld both P joints — anchor
  precision + bezier bow).
- **还** (A) — CALLED `draw_chuo_walk` for 辶 wrap (P-A-007 rule 1),
  inlined 不 (no bank primitive). **Textbook P-A-007 application**.
- **位** (A) — inline for both 亻 and 立; drawer noted "considered
  P-A-007 whole-radical route but 立 is aspect-skewed (~0.75× width
  / ~0.98 height); draw_li_stand only accepts uniform scale, would
  render too short vertically. Falling back to P-A-006 per P-A-007
  clause 2." **Textbook P-A-007 clause-2 fallback**.
- **伾** (A) — inline 亻 (rejected draw_ren_left because pie head at
  TL(0.87, 0.656) sits higher than baked geometry — clause-2 fallback);
  inline 丕 (no bank primitive).

**Key insight**: 3 of the 4 A verdicts explicitly reasoned about the
P-A-007 decision (call bank vs inline) and chose the CORRECT branch.
This is the first batch where P-A-007 reasoning shows up as an explicit
step in the A-quality drawers' docstrings. **P-A-007 is now a
retrieval mechanism, not just a corrective principle.**

**Boundary evidence still standing**: P-A-007 does NOT rescue every
FAIL. 名 and 西 R1 called the bank primitive and still FAILed —
sibling-adaptation (P-RET-005) is a separate lever.

**Corollary for drawers (must be enforced by the docstring self-check)**:
Every generated.py for a compound char MUST have a docstring line or
SELF_CHECK note answering: "For each sub-component, did I check whether
a bank primitive matches at native scale? If I inlined instead, WHY?"
Absence of this reasoning trail = curator will reject on next
FAIL-diagnosis pass and force a mechanism-change retry.

---

**P-COMP-012 (NEW B9) — 亻+X hook-compound FAIL boundary is NOT
shifting; six new FAILs confirm P-COMP-011.**

B9 亻+X FAILs (all 亻+X-with-hook-compound-right): 你 (尔 with heng_gou
+ shu_gou), 伶 (令 with 冫+卩 hook), 伽 (力 heng_zhe_gou + 口), 佇 (宁
with shu_gou), 佈 (布 with heng_zhe_gou), 员 (贝 with hooks), 听 (斤 has
straight strokes BUT this is 口+斤 not 亻+X — miscategorized).

B9 亻+X PASSes (all X = straight-stroke only per P-COMP-011): 位 A
(亻+立, straight), 伾 A (亻+丕, straight), 作 (亻+乍), 伯 (亻+白), 伺
(亻+司 — has hook but s3 heng_zhe_gou handled by bank primitive!), 伲
(亻+尼 C), 佃 (亻+田), 但 (亻+旦), 佉 (亻+去), 佐 (亻+左), 伽 FAIL not PASS.

**Refinement of P-COMP-011**: hook-compound right-half FAILs when the
compound stroke type (heng_zhe_wan_gou, heng_xie_wan_gou, shu_gou,
shu_wan_gou) is NOT one of the bank's cleanly-parameterized primitives.
When it IS (e.g. heng_zhe_gou for 司/伺), the P-A-007 whole-radical
route works: 伺 PASS despite hook-compound right half because
`draw_heng_zhe_gou` in bank handled the outer 4-anchor compound cleanly.

**Boundary now**: hook-compound right FAILs when the specific hook-
compound primitive is missing OR aspect-shifted from bank. The
"straight-stroke-only" rule from P-COMP-011 is a proxy for "bank has
the compound-stroke primitive at usable geometry."

**Retry queue implication**: for a 亻+X FAIL where X has a hook-compound,
check first: does the bank have that specific hook-compound primitive?
If YES (heng_zhe_gou, shu_wan_gou at usable scale) → queue R1 with
explicit primitive call. If NO → do-not-queue (chronic bank gap).

---

**P-A-008 (NEW B9) — INLINE-REASONING TRACE required for compound-char
attempts.**

Discovery from A-verdicts audit: 3 of 4 B9 A verdicts explicitly
reasoned in the docstring about "should I call the whole-radical bank
primitive here, or inline?" 位's docstring is exemplary:

> "Also considered P-A-007 whole-radical route (call draw_ren_left +
>  draw_li_stand), but 立 in 位 is aspect-skewed (~0.75x width /
>  ~0.98y height) vs standalone li_stand — draw_li_stand only accepts
>  uniform scale, would render the 立 too short vertically.
>  Falling back to P-A-006 per P-A-007 clause 2."

Contrast: 你/伶/伽 (FAIL) docstrings note "P-A-006 route" but do NOT
explain why a bank whole-radical was rejected. The absence of the
inline-reasoning trace correlates with FAIL.

**Rule (P-A-008)**: Every generated.py for a Phase-3 compound char MUST
include, in its module docstring, a per-sub-component decision trace:
for each sub-component name it, state whether a bank whole-radical
matches, and if it does, either call it OR justify inlining with an
aspect/scale reason. A silent inline where a matching bank primitive
exists is a bug.

**Enforcement**: curator running B9+ diagnostics will grep the FAIL's
docstring for "P-A-007" or explicit sub-component decisions. If absent,
FAIL is auto-queued for R1 with instruction to add the reasoning trace
and re-decide.

---

*Future principles: add as evidence accumulates. Format = `P-<CATEGORY>-<NNN>` for cross-referencing from other files. Retire (with note) when a principle is contradicted by later evidence.*

---

## B10 (2026-08-09) — post-B10 evidence (7 A verdicts; validates P-A-008 as A-recipe)

**P-A-009 (NEW B10) — Quantitative BANK_DEVIATION reasoning is the
signature of A-quality drawers.**

Evidence: 4 of 7 B10 A verdicts (的, 和, 些, 佔) contain BANK_DEVIATION
blocks with NUMERIC aspect/scale calculations, not qualitative
handwaves. Examples:

- **的 (A)**: "MMH 白 in 的: x-range 39.6..108.1 (~68), y-range 71.5..261.9
  (~190), aspect w/h ~ 0.36. Native-scale width 68/150 = 0.45 → BELOW
  [0.55, 1.2] window; native-scale height 190/223 = 0.85 → inside.
  Aspect skew is ~2×."
- **和 (A)**: "MMH 口 in 和 (from s6/s7/s8 anchors): x-range ~157..255
  (~98), y-range ~153..246 (~93), aspect w/h ~1.05 (near-square). ...
  aspect-skew ratio 0.74/0.61 = 1.21 — right at the edge of the
  P-A-007-v2 window."
- **些 (A)**: "zhi_stop native aspect ~1.19 (wide>tall), but 止-inside-些
  has aspect ~0.88 (tall>wide) at MMH x-range 40..156 vs y-range 78..210".
- **佔 (A)**: "bank s1_head (158.8, 73.8) vs MMH (91.4, 75.3); shift
  ox=-74 aligns bank into the anchor box (within 15 px of all four
  endpoints)."

Contrast with B10 FAILs (社/佛/佞) which contain BANK_DEVIATION blocks
with only qualitative reasoning ("aspect matches native but composition
wants different aspect skew"). The quantitative computation forces the
drawer to actually verify the mismatch is real; qualitative reasoning
lets the drawer skip a bank primitive that would have PASSed.

**Rule (P-A-009)**: When writing a BANK_DEVIATION block, the reason MUST
include NUMERIC aspect/scale/endpoint deltas — not qualitative claims.
Concretely, EITHER:
- Compute native primitive's bounding box (width, height, aspect ratio)
  AND target's bounding box AND report the scale factors and aspect-
  skew ratio; OR
- Compute per-endpoint deltas in pixels between where the bank primitive
  would place stroke endpoints (at chosen ox/oy/scale) and where the
  MMH anchors want them.

Then check: is the native-scale ratio inside [0.55, 1.2]? Is the aspect-
skew ratio inside [0.83, 1.20]? If YES to both → CALL the bank primitive
(the reason for BANK_DEVIATION doesn't actually hold). If NO to either
→ BANK_DEVIATION is justified; inline via P-A-006.

**Extends P-A-007-v2 hard-check + P-A-008 reasoning-trace** — turns the
qualitative "does the primitive match" check into a quantitative,
verifiable computation. This makes the P-A-008 trace auditable.

**Enforcement**: curator will grep BANK_DEVIATION blocks for numeric
values in the "reason" line. Blocks without numeric deltas will be
flagged as unaudited reasoning during FAIL-diagnosis; if a matching
bank primitive would have PASSed at the numeric bands, the FAIL is
queued for R1 with instruction to compute the deltas and re-decide.

---

**P-A-008 VALIDATED (B8→B10 comparison)** — the mandatory inline-
reasoning trace rule crystallizes A-recipe discipline on same-difficulty
compound-char pool.

B8: 20 PASS, **0 A** on Phase-3 idx 234-283 (亻+X + 6-stroke compounds).
B9: 22 PASS, **4 A** on idx 284-333 (P-A-008 codified end-of-batch).
B10: 26 PASS, **7 A** (**+1 retry A**) on idx 334-383 — highest A count
of the experiment on 6-8-stroke compounds. Cumulative: **20 A across
518 mains** = 3.9% A rate (B10 alone = 15% A rate on this batch).

Interpretation: the P-A-008/P-A-009 discipline pair (mandatory reasoning
trace + quantitative BANK_DEVIATION calc) has moved G5's A ceiling from
"structural rendering-format bound" (B8's diagnosis) to "discipline-
bound at ~7-8 A per 50-item batch". Whether this holds on B11 (item
pool has similar 亻+X + 疒-family + novel 8-stroke compositions) will
determine if the ceiling is discipline-shifted or pool-favorable.

Note on B10 pool difficulty vs B8: same MMH-injection format, same
stroke-count range (6-8 for most items). B10 does NOT have easier items
— it has different items with similar decomposition demands. The A
delta (0 → 7) tracks the discipline crystallization, not item pool
easiness.

**Corollary for B11 curator**: expect 5-8 A verdicts if discipline holds;
0-2 A if discipline drift. Sample 3 PASSes' docstrings; if P-A-008 +
P-A-009 traces present, discipline intact.

---

**P-COMP-011 boundary UPDATE (B10)** — the "亻+X" pattern is drifting
away from the strict "straight-stroke only" boundary.

B10 evidence:
- **佔 A** (亻+占) — 占 has 卜 (heng+dian) + 口 (hook-compound heng_zhe_box).
  DID reach A via BANK_DEVIATION of both bu_divine and kou_mouth.
- **佟 A** (亻+冬) — 冬 has heng_pie (compound). DID reach A.
- **佗 PASS** (亻+它) — 它 has shu_wan_gou hook. PASS.
- **佝 PASS** (亻+句) — 句 has heng_zhe_gou hook. PASS.
- **佛 FAIL** (亻+弗) — 弗 has shu_gou hook. Still FAIL.
- **佚 FAIL** (亻+失) — 失 has X-cross (2 straight strokes at joint).
  Called ren_left correctly but 失 inline still FAILed.

Boundary refinement: hook-compound right FAILs specifically when the
compound is a HORIZONTAL frame's hook (heng_zhe_gou at large scale
where the right hook doesn't match the stroke primitive), not when
the hook is INSIDE a smaller sub-radical. When the right-half is
compact and the hook lives inside a stroke primitive at usable scale,
P-A-006/P-A-007-v2 does resolve. This narrows P-COMP-012's ambit.

**Updated rule (P-COMP-011-v2 / P-COMP-012 refined)**: hook-compound
right FAILs when EITHER (a) the compound is at large canvas-spanning
scale needing per-endpoint width control (G5 format ceiling), OR (b)
the compound-stroke primitive is missing at usable geometry. Right-
half compact hook compounds that fit inside a stroke primitive at
scale PASS reliably via P-A-006.

---

**Terminal-freeze cluster identified: 疒-family bank gap (B10)**

Evidence: 4 疒-family FAILs in B10 (疙, 疟, 疠, 疝). All 4 drawers
attempted P-A-006 inline of 疒 as 5 strokes (dian + heng + long pie +
dian + ti). All 4 FAILed. Root cause: no whole-radical primitive for
疒 in bank; the 5 inline strokes at MMH anchors don't cohere as 疒
visually — the 广-shell + 2 dots decomposition doesn't produce the
distinctive slant + interior-mark spacing calligraphically.

Following P-COMP-006 (no retry without mechanism-change), all 4 疒-
family FAILs enter terminal-freeze. Also 疌 (similar 肀-top +
体 bottom bank gap).

**Deliberately do NOT hand-craft a 疒 primitive** — P-COMP-008 refuted
the "elevate to hypothesis-driven candidate spec" route for
heng_zhe_wan_gou; likely to fail identically for 疒. When a Phase-3
item that has 疒 as sub-component PASSes via inline (unlikely without
new stroke primitives), THEN promote the passing inline as `nao_sickness.py`.
Until then, terminal-freeze the entire cluster.

---

## B11 (2026-08-09) — post-B11 evidence (9 A verdicts, 0/4 R1 rescue)

**P-A-010 (NEW B11) — R1 mechanism-change taxonomy: quant-recheck rescues
"wrong single primitive skipped" FAILs but NOT "composition-level"
FAILs.**

Evidence from B11: all 4 R1-queued items (社/佞/畅/经) FAILed at R1
despite drawers correctly applying the queue instruction (call bank
primitives with P-A-009 quantitative math). Root cause: each of the
4 involved multi-primitive DEVIATION or inter-primitive spacing, not
a single wrong-skip.

- **社 R1**: called shi_spirit + tu_earth per quant check (0.741 and
  0.792 in-window); both primitives rendered OK; L-R spacing between
  礻 and 土 was never bank-authored and R1 could not fix it.
- **佞 R1**: called ren_left + er_two + nu_woman all per quant math.
  3-part vertical composition (亻 | 二/女) requires inter-primitive
  weld the bank does not encode.
- **畅 R1**: tried to adapt you_by (由) with s5 shu extended, but this
  is stroke-level tweak, not primitive-swap; drawer inlined 申 fresh
  and failed on inter-half alignment.
- **经 R1**: quant recheck confirmed inline was correct; trajectory-diff
  addressed component quality; 8 unwrapped strokes still didn't cohere.

**R1 mechanism-change taxonomy** (from B7/B9/B10/B11 evidence):

| Failure kind | R1 mechanism | Precedent |
|--------------|--------------|-----------|
| (a) Wrong single primitive skipped | P-A-007 quant recheck → call primitive | B9 军 (mi_cover+che_car), 成 (xie_gou) |
| (b) Correct single primitive mistuned | P-A-005 trajectory-diff on params | B6 义 (bow_perp differentiation), B10 运 (pie_zhe corner) |
| (c) Sibling-adaptation missed | P-RET-005 sibling-pair discipline | B7 比 R1 |
| (d) Inter-primitive spacing / L-R weld / 3-part composition | **NO R1 rescue channel — do-not-queue** | **B11 社/佞** |
| (e) Multi-primitive DEVIATION on independent sub-components | **NO R1 rescue channel — do-not-queue** | **B11 畅/经** |

**Rule (P-A-010)**: Before queuing an R1, classify the FAIL. Only kinds
(a)-(c) are R1-rescueable. Kinds (d)-(e) are do-not-queue: the
mechanism-change budget is spent on a hopeless retry. Specifically:

- If FAIL docstring has ONE BANK_DEVIATION and the quant recheck says
  "should have called" → queue R1 (kind a).
- If FAIL docstring has BANK_DEVIATION with correct quant math and the
  primitive genuinely doesn't fit, AND a trajectory-diff on a single
  primitive can address the visible mismatch → queue R1 with specific
  diff instruction (kind b).
- If FAIL docstring calls a bank primitive but a sibling character
  differs on a specific interior feature → queue R1 with sibling
  reference (kind c).
- If FAIL has >=2 BANK_DEVIATION blocks OR involves L-R spacing
  between two independent sub-components OR is a 3-part vertical/
  horizontal composition → **do-not-queue**.

**Corollary — B12 R1 queue must be smaller and more targeted**:
apply P-A-010 to all B11 FAILs. Retire the impulse of "any multi-
DEVIATION FAIL → queue R1 with quant recheck". That impulse cost
B10 curator 4/4 wasted retry slots.

**Corollary for future curator postmortems**: if any B12+ batch has
R1 rate <20% (0-1 PASS/A out of 5+), rerun the queue-classifier
audit — most likely at least half the queue was kind (d) or (e).

**Extends** P-A-005, P-A-007-v2, P-COMP-006, P-RET-005. **Refines**
the B10-era "always try quant recheck" heuristic that produced the
0/4 B11 R1 outcome.

---

**P-A-006/007/008/009 stability check (post-B11)**: all four recipe
principles hold across 9 B11 A verdicts:
- 9/9 A docstrings contain P-A-008 per-sub-component decision trace.
- 9/9 A docstrings contain P-A-009 quantitative BANK_DEVIATION math.
- 4/9 (佯/佼/受/采) mix bank-CALL + inline within a single char —
  exemplars of P-A-007-v2 discriminating sub-component-by-sub-component.
- No B11 A verdict violates any of the four recipe principles.
- Monotonic-up A count on comparable pool: B8/B9/B10/B11 = 0/4/7/9,
  discipline crystallization compounding.

**Cross-group note (paper-relevant, from B11 postmortem correction)**:
G5's B11 9 A does NOT beat G4's 17 A on the same items. G4 continues
to lead A verdicts on hook-heavy Phase-3 pools by ~7-10 A. The two-
factor decomposition from B8 still holds: memory format neutral for
PASS; rendering format (per-endpoint width in G4 vs uniform PIL in
G5) decisive for A on hook-heavy chars. Discipline (P-A-006 through
P-A-010) narrows but does not close the A gap. Do NOT frame G5
progress as "catching up to G4"; frame it as "closing the discipline
half of the two-factor gap; format half remains structural".

---

## B12 (2026-08-09) — post-B12 evidence (10 A verdicts, 3/5 R1 rescue, first legit G5>G4 batch)

**P-A-010-v2 (SHARPENED B12) — R1 mechanism-change taxonomy validated at 3/5,
sub-kind (b) refined**

Evidence from B12 R1 queue (4 targeted + 1 kind-a inheritance from B11 = 5):
- **实 R1 → A** ✓ Kind (a): main FAIL had BANK_DEVIATION on mian_roof
  (aspect 0.60, just below 0.55 lower bound). R1 called mian_roof at
  scale=0.85 per queue instruction; PASSed → A. Confirms P-A-010 (a):
  primitive-skipped-with-borderline-aspect rescues at R1.
- **治 R1 → PASS** ✓ Kind (b) parameter-tune: main skipped kou_mouth on
  aspect 1.42 vs bank 0.87. R1 inlined a wide-flat 口 as `shu +
  heng_zhe_box + heng` at aligned box endpoints (bottom_right=y=296 to
  match shu depth). NOT a bank-call; instead a **stroke-level trajectory
  diff on the primitive's parameterization** — this is what "kind (b)"
  means when the DEVIATION math is genuine (>2x aspect off): don't force
  the bank call, but *fix the composition detail* the main FAIL missed.
- **放 R1 → PASS** ✓ Kind (b): main FAIL had 3 stroke-level problems
  (方's dian too high, 攵's s5 floating, na overshoot). R1 kept the
  overall inline strategy but (a) enlarged 方's dian to touch heng,
  (b) started descending pie FROM heng line, (c) switched 攵 to
  pu_action bank call at scale=0.85 per queue instruction. Mixed
  strategy (partial bank-call rescue + stroke-level fixes) PASSed.
- **例 R1 → C** ✗ Kind (a) attempted: main FAIL BANK_DEVIATIONed on
  ren_left AND dao_right (anisotropic 79% x-compression concern —
  which is P-A-007-v2 tolerance range). R1 called both bank primitives
  per queue instruction; got C (improved from FAIL but not PASS). Two
  bank primitives rendered cleanly, but 歹-middle inline noisy →
  cluster this as kind (a) partial-rescue. **New sub-observation**:
  when a 3-radical L-R (亻+X+刂) has kind-(a) fixes for ONLY 2 of 3
  sub-components and the middle is inline, R1 lifts FAIL → C but not
  → PASS. Boundary case.
- **侔 R1 → FAIL** ✗ Kind (b) MISCLASSIFIED as kind (d): queue told
  drawer to "trajectory-diff on 厶-top placement — center between 亻
  and 牛". This is **inter-primitive spacing**, not a single-primitive
  trajectory-diff — retrospectively kind (d) in kind-(b) clothing.
  Drawer bank-called ren_left and niu_cow correctly (per math), then
  had to freehand the 厶-top spacing between them — same failure mode
  as B11 社/佞.

**Sharpened P-A-010-v2 rules**:

| Kind | Mechanism | R1 Rescue |
|------|-----------|-----------|
| (a) Single primitive BANK_DEVIATIONed with borderline aspect ratio just outside [0.55, 1.2] band OR inside band mis-argued | CALL primitive at scale-adjust | ✓ high (implicated in 军/成/老/实) |
| (b1) Correct single primitive mistuned — stroke-level trajectory-diff on **one primitive's parameters** | Fix that primitive's params (e.g. 义 bow_perp, 治 kou heng-alignment, 放 pu_action scale-tune) | ✓ mid-high |
| (b2) **NEW — trajectory-diff on inter-primitive spacing** | Reclassify as kind (d) — do NOT queue as kind (b) | ✗ NO rescue (previously mis-queued as B12 侔) |
| (c) Sibling-adaptation missed | Sibling reference (P-RET-005) | ✓ mid |
| (d) Inter-primitive spacing / L-R weld / 3-part composition / multi-inline placement | **Do-not-queue** | ✗ NO rescue |
| (e) Multi-DEVIATION correct-math independent sub-components | **Do-not-queue** | ✗ NO rescue |
| **Partial (a) on 3-radical L-R** (kind a for 2 of 3, middle inline) | Half-lift only: expect FAIL → C, rarely PASS | ~C ceiling (B12 例) |

**Key clarification from B12 outcome (3/5 vs B11's 0/4)**:
- Kind (a) worked in 4/5 historical cases (B9 军/成/老 + B12 实) — most
  reliable rescue channel.
- Kind (b1) — **single-primitive parameter trajectory-diff** — works
  (B12 治/放 PASSes). Do NOT confuse with kind (d) inter-primitive
  spacing tuning. If the "trajectory-diff" adjusts a parameter of ONE
  bank primitive OR fixes ONE stroke's endpoints, it's kind (b1). If
  it adjusts the gap/weld/relative position BETWEEN two primitives,
  it's kind (d).
- Do-not-queue kind (d)/(e) discipline saved 3 slots in B12 vs B11
  (B12 queue = 5 vs B11 queue = 4). Improved queue quality:
  60% success (3 PASS/A) vs 0% (B11). Direct validation of P-A-010.

**Rule (P-A-010-v2 STRICT)**: Before queuing R1, classify by asking
**"what single object gets changed?"**:
- ONE bank primitive gets called (was skipped) → kind (a) ✓ queue
- ONE bank primitive's parameters/scale change → kind (b1) ✓ queue
- ONE stroke's endpoints move to fix visual problem → kind (b1) ✓ queue
- Gap/weld/alignment BETWEEN two sub-components changes → kind (d) ✗ freeze
- Multiple independent sub-components need DEVIATION with correct math
  → kind (e) ✗ freeze

**Extends** P-A-010 (B11) with the (b1) vs (d) distinction. **Refines**
the "trajectory-diff" test into a mechanical decision procedure.

---

**P-A-006/007/008/009 stability check (post-B12)**: all recipe principles
hold across 10 B12 A verdicts:
- 10/10 A docstrings contain P-A-008 per-sub-component decision trace.
- 8/10 A docstrings contain P-A-009 quantitative BANK_DEVIATION math
  (the 2 exceptions — 盃, 盅 — had NO BANK_DEVIATION because both
  components had prior-passing inline templates that fit natively).
- Monotonic-up A count trajectory continues: B8/B9/B10/B11/B12 = 0/4/7/9/10.
  Discipline crystallization compounding for the fifth consecutive batch.
- **Zero P-A-007-v2 refusal errors on 10 A verdicts** — every A had a
  clear reasoning for either "call bank" or "inline with math".

**Signature A-recipe pattern (all 10 B12 A's)**:
1. Look at MMH block first. Cross-reference stroke count + endpoint anchors.
2. Hard-check every whole-radical bank candidate against target aspect
   (P-A-007-v2 [0.55, 1.2] window).
3. Write BANK_DEVIATION block with numeric aspect math (P-A-009) when
   skipping — OR document why no bank candidate exists (no radical
   primitive for this decomposition).
4. Inline stroke primitives at MMH-verbatim anchors (P-A-006).
5. Docstring includes P-A-008 per-sub-component trace with expected
   joint classes and how they emerge from anchor geometry.

---

## Cross-group finding (B12) — first LEGITIMATE G5 > G4 batch on aligned idx

**B12 aligned comparison (idx 434-483, same items across groups)**:
- G3 (no MMH): 7/50 = 14% PASS, 1 A
- G4 (MMH + grid, per-endpoint width): 20/50 = 40% PASS, 8 A
- **G5 (MMH + code, uniform PIL width): 23/50 = 46% PASS, 10 A** ← lead

**This is the FIRST batch where G5 legitimately beats G4 on both PASS
and A on aligned indices** (B11-curator's earlier "G5 beats G4" claims
were indexing-error artifacts and were retracted).

**Mechanism analysis** (from A-verdict cross-comparison for the 10 G5 A's):
- **3 SOLO A wins** (G5 A + all others C/FAIL): 面, 神, 俅
- **4 upgrades from G4 PASS to G5 A**: 面 (G4 PASS), 盃 (G4 PASS), 盅
  (G4 PASS), 草 (G4 PASS). G5 matched G4's PASS baseline then pushed
  to A on 4 chars where G4 stopped at PASS.
- **3 matches with G4 A**: 点, 信, 美 (both A)
- **1 rare pattern**: 俎 got G1-solo-A in main-exp (blind luck), G5
  now also got A, G4 got PASS. G5 discipline caught a pattern G4
  missed.

**Interpretation — three compounding factors, not a single lever**:

1. **Discipline crystallization** (dominant factor). Monotonic A count
   B8-B12 = 0/4/7/9/10 shows the P-A-006 through P-A-010 recipe stack
   is being INTERNALIZED by drawers batch-over-batch. Every B12 A
   docstring cites the recipe explicitly.

2. **Bank-critical-mass threshold plausibly crossed** (~150-170
   primitives). B12 A verdicts show a distinct pattern: 6/10 A's
   have BANK_DEVIATION with quantitative math (fresh inline) and 4/10
   use prior-passing inline templates directly (盃/盅 = 不+皿 and
   中+皿 stacks). When the bank has a template for both halves of a
   compound, A becomes reachable without new BANK_DEVIATION math —
   ratcheting the A ceiling upward. This suggests the mechanism is
   less "individual A skill" and more "compositional bank enables
   template stacking".

3. **G4-favorable pool shrinking** (secondary factor). B12 was NOT
   a G4-regression: G4's 40% is consistent with its B11 62% peak
   being pool-favorable (idx 384-433 was hook-heavy = G4 native
   territory). B12 (idx 434-483) had more MMH-compliant compound-char
   composition, which G5 discipline is better tuned for than G4 grid.
   Not "G4 lost ground"; rather "pool moved toward G5 strength".

**Paper implication**: the two-factor decomposition from B8 (memory-
neutral PASS + format-decisive A) needs a THIRD factor now:
compositional-bank-enabled A. When bank primitives cover both halves
of a compound, uniform PIL rendering matches per-endpoint fat_line
for A verdicts. The G4 A ceiling is only structural in the *absence*
of bank templates. G5's growing bank narrows this differential
batch-over-batch.

**Corollary for B13+**: expect G5-vs-G4 gap to be POOL-DEPENDENT
going forward. On hook-heavy pools, G4 still leads A (per-endpoint
width). On compound-stack pools with bank template coverage on both
halves, G5 matches or exceeds G4 A.


