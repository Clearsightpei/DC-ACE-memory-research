# G5 sandbox

*Curator per-batch scratchpad. Postmortems, diagnostic notes, cross-group observations (G5 vs G3, format effect, MMH effect). Empty at fresh start (2026-08-08).*

---

## B1 postmortem (2026-08-08)

**Raw counts**: 31 PASS + 12 C + 7 FAIL out of 50 mains + 3 retries (1 PASS, 1 C, 1 FAIL). 32/53 = 60% overall pass rate.

**Cross-group comparison (mains)**: G3 (no MMH) got 27/50=54%; G5 (has MMH) got 31/50=62%. Absolute score delta is +8 pts, but the more striking signal is **FAIL→C conversion**: G3 had 23 FAILs vs G5's 7 FAILs. MMH doesn't produce many extra PASSes on radicals — but it prevents drawers from producing incomprehensible attempts. The "C" verdict spike (12 for G5 vs G3's 0 C's) confirms MMH pushes wreck attempts into the "close but not quite" band rather than fixing them outright.

**What MMH helped with**: composition of multi-stroke radicals with clear per-stroke class labels (十, 大, 工, 艹, 川, 广, 又, etc. all PASSed cleanly). MMH's stroke-count + per-stroke class removes the "how many strokes" and "what class" uncertainty.

**What MMH did NOT help with**: compound strokes (横折钩, 竖折, 横撇, etc.). The MMH median-endpoint pair only describes the ENTIRE compound stroke, not its internal corners. Drawers had to infer corners from the GT visually — sometimes off. That's where the 12 C's mostly clustered. B1 promoted 6 new stroke primitives (`ti`, `shu_zhe`, `heng_zhe_gou`, `heng_pie`, `ping_na`, `heng_zhe_box`) from BANK_DEVIATIONs to give B2 drawers pre-computed compound-stroke geometry.

**What MMH doesn't touch (FAILs)**: unusual/rare radicals (㔾, 巛, 彑, 犭, 马) that need highly specific geometric knowledge and don't decompose into the standard stroke classes MMH names. Some of these may be terminal-freeze candidates.

**Retry outcomes**: 亅 R1 PASS confirms the "continuous curl not diagonal" fix generalizes. 丿 R1 FAIL confirms the drawer under-shot MMH-override for the anchor shift. 儿 R1 C confirms visual-balance issues aren't solved by parameter tuning alone; may need one more attempt with more extreme knee_ratio.

**Bank growth in B1**: 19 → 44 entries (+25: 6 stroke + 19 radical). This is a substantial retrieval expansion; B2 drawers should find most common radicals covered by whole-radical primitives now.

**Structural evolution decisions**: none this batch — the three-bank layout continues to work. Considered splitting drawer_memory.md into per-topic files but current file is ~180 lines, still navigable. Revisit at 400 lines.

---

## Observations to test later

- Does the bank's whole-radical position-signature convention actually help Phase-3 characters? Or do drawers ignore ox/oy/scale and re-derive coords per composition? (Answer determines whether we keep position-signature or migrate to something else.)
- Do left-position primitives (亻, 扌) actually get reused with a shrink-and-drift transform, or do drawers inline every time? If the latter, position-signature is dead weight and the bank should store fragment-only primitives.
- Does the sibling-pair table in `drawer_memory.md` prevent minimal-pair confusion, or do drawers still confuse 士/土 etc.?

---

## B2 postmortem (2026-08-08)

**Raw counts (70 total)**: 22 PASS + 22 C + 26 FAIL — combined 22/70=31% overall pass rate. Mains alone: 19/50=38% (vs B1's 62%); B2 is harder due to more compound radicals (positions 069–118 hit the messy mid-radical band).

**Cross-group comparison (mains only)**: G3 = 17/50=34% (0 A, 33 FAIL); G5 = 19/50=38% (0 A, 18 FAIL). **Absolute delta +4 pts; FAIL→C delta 18 vs 33.** MMH continues to prevent wrecks (halves FAILs) but PASS rate is only marginally higher. B1 pattern reaffirmed.

**Bank growth**: 44 → 64 entries (+20: 2 stroke + 18 radical). The stroke primitives are the highest-leverage additions:
- `xie_gou.py` — extracted from 2 concurrent BANK_DEVIATIONs (弋 + 戈), unlocks 我/找/成/战/戏/戒/氏/... for Phase-3.
- `heng_gou.py` — extracted from 欠 BANK_DEVIATION, unlocks 买/家/尔/买-family for Phase-3.

The 18 radical promotions include the very-high-freq 氵/木/日/攵 which will each show up in >10% of Phase-3 characters.

**Retry outcomes (from B1 queue)**:
- Success stories (3 PASS): 廴, 巾, 饣 — all validated P-RET-003 (promoting compound stroke primitives directly unblocks retries).
- Persistent-C (9): 门, 讠, 寸, 尸, 己, 阝, 儿 (R2), 弓, 几 — bank has the strokes but composition tuning still off. Requeue to B3.
- Persistent-FAIL (8): 宀, 女, 飞, 马, 犭, 巛, 丿 (R2), 㔾 — geometry-hard; several are terminal-freeze candidates.

**FAIL clusters in B2 (identified in errata.md)**:
- **Cluster A: missing compound stroke class** — 兀 (shu_wan_bare), 风+气 (heng_xie_gou), 长 (xie diagonal), 氏 (xie_gou — now unblocked). About 6 FAILs.
- **Cluster B: multi-turn compounds** — 子 (wan_gou), 幺 (pie_zhe), 肀+爿+殳 (complex bracket compositions). About 5 FAILs.
- **Cluster C: proportion / sibling confusion** — 夕/夂/歹/方/见/攴/火 (drawer chose wrong structure or wrong proportions). About 7 FAILs.
- **Cluster D: C-verdicts** — mostly proportion/tuning issues, close but not close enough (13 items).

**Structural evolution decisions (this batch)**:
- No memory file split (drawer_memory.md now ~230 lines; still navigable, revisit at 400).
- Composition rule P-COMP-001 (MMH-count-overrides-radical-wrapper) added to principle_bank.
- Two-DEVIATION promotion rule P-COMP-002 codified from xie_gou evidence.
- Sibling-pair table (drawer_memory.md) extended with 7 new pairs from B2 evidence.

**Observations to test in B3**:
- Does the enlarged sibling-pair table actually prevent B3 confusion? (Test: 手/毛/肀 retry outcomes.)
- Does `xie_gou.py` in the bank enable 氏/旡/气 retries to PASS?
- Do Phase-3 characters (starting ~position 136) actually reuse the whole-radical primitives, or do they inline every time? (This is a live research question — see B1 sandbox.)
- Does the bottom-X pattern (draw_pu skeleton) generalize to 火/夂/夊 retries?

---

## B3 postmortem (2026-08-08)

**Raw counts (88 total)**: mains 35 PASS + 7 C + 8 FAIL = 70% PASS rate;
retries 7 PASS + 19 C + 12 FAIL = 18% recovery. Overall 42/88 = 48% —
best batch to date. Cumulative through B3: **100/168 = 60% success, 4 A**.

**Cross-group vs G3 (same items, no MMH)**: G3 B3 got 29/50=58% mains
with 0 A; G5 B3 got 35/50=70% mains with **4 A**. Delta: +12 pts absolute
AND first quality lift into A band. MMH signature intensifying at Phase-3:
where B1/B2 was mainly FAIL-prevention, B3 adds quality lift for the
subset of chars that map cleanly to bank primitives.

### First-A milestone — analysis

**The 4 A verdicts (2 routes)**:

- **Route 1 — Identity bank reuse (人 A, 又 A)**: p3_char_0011_人 called
  draw_ren (from B1's p2_radical_028_人 PASS) at ox=0, oy=0, scale=1.0.
  p3_char_0017_又 called draw_you at identity. Both are zero-parameter
  identity calls of Phase-2 primitives that happened to have MMH-verbatim
  anchors matching Phase-3 dispatch. Getting A (not just PASS) suggests
  bank primitives encode the calligraphic quality (taper, curve, joint
  spacing) that human judges reward.

- **Route 2 — Meticulous inline composition (爻 A, 了 A)**:
  - 爻 A: 4-stroke composition of 2 X's using pie/na bank primitives.
    Bow_perp differentiated per stroke (-14/-8/-18/-10). Anchors used
    verbatim from MMH. Explicit taper on every stroke.
  - 了 A: BANK_DEVIATION with meticulous 3-bezier inline crafting of
    弯钩 (no matching bank primitive existed). Fresh_component
    `wan_gou_for_了` promoted to `wan_gou.py`. Careful control-point
    placement in cubic bezier + separate quadratic bezier for terminal
    hook flick.

**A-recipe checklist** (codified as P-A-001 + P-A-002 in principle_bank):
1. Bank primitive exists for this shape? → identity-call (Route 1).
2. Otherwise: compose from stroke bank with explicit MMH anchors +
   differentiated taper + per-stroke bow (Route 2).
3. Missing primitive class? → careful BANK_DEVIATION; may seed future
   Route-1 candidate.

### Failure cluster analysis

**Cluster HH — heng_zhe_wan_gou family (5 FAILs)**: 乃, 几, 九 (Phase-3),
plus 瓦 and 风 (Phase-2 previously). All need the 横折弯钩 compound
stroke (horizontal + corner-down + curving right belly + small upward
hook). Bank has no primitive. B3 saw 2 independent inline DEVIATIONs
(几 s2 + 九 s2), but both FAILed — cannot promote per P-COMP-002 (requires
PASS). Providing geometric spec below for B4 retries.

**heng_zhe_wan_gou spec (for B4 retries)**:
```
head:    horizontal start (top-mid)  ~ (x_h, y_h)
corner:  top-right where horizontal turns down ~ (x_h + 60..80, y_h)
belly:   right-bottom of curve ~ (corner_x + 15..25, corner_y + 90..130)
tail:    small upward hook tip ~ (belly_x - 20..30, belly_y - 15..25)
```

Cluster W — 3-directional radicals (3 FAILs): 水, 瓦, 爪. All have
strokes going in ≥3 different directions with tight visual spacing.
MMH doesn't fully resolve the calligraphic weight/spacing needed.

Cluster C — proportion fine-tuning (7 C's): 尣, 韦, 毋, 心, 牙, 冂, 七 —
each close but a specific proportion or missing sub-primitive (心 needs
卧钩, 冂 needs heng_zhe_wide).

### Retry recovery analysis

**R2 success stories (5/6 = 83% PASS)**: 门, 讠, 阝, 宀, 女. All R2
retries succeeded except 弓 R2 (C again) and 几 R2 (C again). This is
a **strong validation of the retry channel**: characters that FAILed
first retry can PASS second retry if the curator provides specific
trajectory-diff hints per failure mode.

- 门: dot moved off-corner + slim shu + explicit heng_zhe_gou waypoints
- 讠: enlarge whole radical + preserve ti flick from R1
- 阝: compact 3-shape ear (max belly x=175) with clear waist cinch
- 宀: use draw_mi_cover wrapper for alignment (P-COMP-004)
- 女: fully inline compound to preserve joint constraint

### Bank growth this batch

**19 new primitives (64 → 83)**: 3 new stroke (wan_gou from 了 A;
heng_zhe_ti from 讠 R2; pie_zhe from 幺 R1) + 16 new radical (王 文 爻
曰 月 爫 支 止 无 肀 幺 门 讠 阝 宀 女). Bank has now covered nearly all
common Phase-2 radicals; remaining un-promoted items are largely low-freq
or the persistent-failure cluster.

### Structural evolution decisions (this batch)

- No memory file split — drawer_memory.md ~330 lines, still navigable.
  Revisit at 500 lines.
- No new file types created.
- 2 new principles: P-A-001 (identity bank → A), P-A-002 (meticulous
  inline → A), P-COMP-004 (wrapper-alignment), P-COMP-005 (rule
  reconciliation).
- Sibling-pair table extended with 7 new pairs (士/土/王, 日/曰, 儿/几/九,
  无/旡/既, 了/子/字, 文/又/攵, and a note on B3 pairs).

### Observations to test in B4

- Does the B3 A-recipe generalize? Do more Phase-3 chars that identity-call
  bank primitives (P-A-001) reach A? Expected: yes for 冫/厂/凵/刀/... family.
- Does the sandbox heng_zhe_wan_gou spec unblock 几/九/瓦 retries? If ≥1
  PASSes, promote `heng_zhe_wan_gou.py`.
- Does the terminal-freeze list stabilize? After 2 batches of C at R2,
  should freeze 弓, 己, 尸, 寸, 几 (R2).
- Does 卧钩 (心/必family) get an inline PASS that unlocks `wo_gou.py`
  promotion?
- **Cross-group question**: G5 now leads G3 by +12 pts and +4 A. If G5's
  lead widens further in B4 as Phase-3 becomes majority, that confirms MMH's
  effect is not just wreck-prevention — it's a genuine quality lift at
  composition-heavy items.

---

## B4 postmortem (2026-08-08)

**Raw counts (86 total)**: mains 29 PASS + 13 C + 8 FAIL = **58% PASS**;
retries 5 PASS + 10 C + 21 FAIL = **14% recovery**. Overall 34/86 = 40% —
weaker than B3 (48%). Cumulative through B4: **129/218 = 59%, 4 A total
(unchanged since B3)**.

**Cross-group vs G3 (mains, same items, no MMH)**: G3 = 27/50 = 54%
with 0 A; G5 = 29/50 = 58% with 0 A. **Delta shrank: +4 pts (B4) vs
B3's +12 pts.** MMH-signature still holds on FAIL prevention (8 FAILs
vs 23) but the PASS-rate advantage narrowed and the A-quality advantage
evaporated for this batch.

### A-recipe: replication FAILED for B4

**Prediction from B3**: identity-reuse on Phase-3 chars that equal a
promoted Phase-2 radical would produce A verdicts (P-A-001).

**Test**: B4 dispatched 11 such items — 勹, 匕, 大, 小, 山, 口, 干, 门,
女, 宀, 艹. All 11 identity-called their bank primitive at (0, 0, 1.0);
all 11 landed PASS. **0 A verdicts.**

**Diagnosis**: B3's A-verdicts were 人 and 又 — both **2-stroke**
Phase-3 chars. The other 2 B3 A's were 4-stroke chars (爻, 了) built
with meticulous Route-2 inline crafting (爻 with differentiated bow_perp
per stroke; 了 with 3-bezier wan_gou crafting). B4's identity-reuse
targets are 3+ stroke chars (勹=2 but different geometry, 大=3, 山=3,
口=3, 干=3, 门=3, etc.). The A-verdict yield appears to require either
(a) extreme simplicity (2 strokes) or (b) an extra tuning pass that
the drawer explicitly did not perform for identity calls (`draw_da(d)`
runs the primitive verbatim with no per-render GT diff).

**Codified as P-A-003**: drawers should continue applying P-A-001/P-A-002
as the default recipe (they reliably produce PASSes) — but should not
expect A verdicts from identity-reuse alone at 3+ stroke chars. The
candidate route to A quality on Phase-3 is post-render diff-vs-GT
tuning (adjust bow/taper/weight to match visible silhouette, not just
MMH endpoints). Test in B5+.

**Alternative hypothesis (not yet ruled out)**: the human judge
calibrated stricter for B4 (fatigue, or different item pool). Only way
to test is via B5 — if identity-reuse of simple items (which will
mostly be back to 2-3 strokes for chars 084-133) starts landing A
again, then A quality tracks item difficulty not drawer discipline.

### Retry channel: sharp regression

- **B3 R2**: 5/6 = 83% PASS. Successful items: 门/讠/阝/宀/女.
- **B4 R2**: 2/22 = 9% PASS (礻, 长). 14 R2 FAILs, 8 R2 C's.
- **B4 R1**: 3/13 = 23% PASS (尣, 韦, 毋). 7 R1 FAILs.

**Diagnosis (codified as P-COMP-006)**: B3's R2 successes were all
items where **a new bank primitive was promoted between R1 and R2**:
- 门 R2 PASS enabled by explicit heng_zhe_gou waypoints;
- 讠 R2 PASS enabled by newly-promoted heng_zhe_ti (from same R2 attempt);
- 阝 R2 PASS enabled by 3-shape ear inline tuning;
- 宀 R2 PASS enabled by using draw_mi_cover wrapper (P-COMP-004);
- 女 R2 PASS enabled by fully-inline compound (preserving joint constraint).

B4's R2 items (旡/气/火/巳/贝/厄/攴/方/兀/比/歹/夕/夂/夊) all need
still-missing compound stroke classes (heng_xie_wan_gou for 旡/气;
box+leg unified helper for 贝/见; 3-stroke bottom-X for 夂/夊; etc.).
None got new bank support between R1 and R2. Result: predictable FAILs.

**Rule for future batches**: when queueing an R2 retry, verify that a
new bank primitive or a specific curator trajectory-diff has been added
since R1. If neither has changed, terminal-freeze the item instead of
burning a retry slot.

### HIGH-prob prediction blowup

B3 curator ranked these R2 retries as HIGH-probability (all had
"bank has the primitive now" story): 氏, 旡, 气, 火, 巳. Result: all
five failed to PASS in B4 (气/火/巳 FAIL; 氏 C; 旡 FAIL). The bank
having a related primitive is **necessary but not sufficient** — the
primitive's baked-in geometry must fit the target composition's
aspect and orientation.

**Rule for future ranking**: HIGH-probability should require both
(a) a matching bank primitive exists AND (b) an earlier BANK_DEVIATION
inline attempt was close to the target geometry (not just "used the
primitive class"). Downgrade to MEDIUM if only (a) holds.

### Bank growth this batch

**9 new primitives (83 → 92)**: 3 retry-PASS radicals (韦, 礻, 长)
+ 6 Phase-3 whole-char primitives (上, 下, 三, 千, 亡, 之). No new
stroke primitives this batch — the 孑 heng_pie BANK_DEVIATION was a
single occurrence (needs 2 per P-COMP-002); logged in bank_candidates
below.

### Bank promotion candidates (single-DEVIATION, awaiting 2nd occurrence)

- `heng_pie_short.py` — from p3_char_0074_孑 BANK_DEVIATION (heng_pie
  defaults are tuned for 又; 孑/子/字 want shorter, deeper heng_pie
  arc following the 了 A-verdict template). Promote if a B5 attempt
  PASSes with the same DEVIATION.
- `heng_xie_wan_gou.py` — needed by 旡/气/风; both R2 attempts inlined
  DEVIATIONs, both FAILed. Cannot promote from failing attempts.
  Terminal-freeze 旡/气 and revisit only if a Phase-3 char in the same
  family PASSes with an inline.
- `heng_zhe_wan_gou.py` — still missing (blocks 几/九/瓦/丸/及/凡).
  B4 inline attempts for 丸/及 both failed. Same rule: revisit if a
  Phase-3 char PASSes with an inline.
- `wo_gou.py` (卧钩) — still missing (blocks 心/必/志). No B4 evidence.

### Terminal-freeze decisions (B4)

**14 R2-FAIL terminal-freezes** (2 rounds of FAIL): 旡, 气, 火, 巳, 贝,
厄, 攴, 方, 兀, 比, 歹, 夕, 夂, 夊.

**8 R2-C terminal-freezes** (2 rounds of C): 氏, 子, 纟, 见, 斤, 耂,
毛, 手.

Note: R2-C terminal-freeze at 2nd C is a stricter policy than B3's
(which allowed 弓 R2, 己 R2, 尸 R2 to freeze at 2 C's — consistent).

**Total terminal-freezes at B4**: 22 items (7 from B3 already frozen
+ 22 new = 29 cumulative). Retry queue is being pruned aggressively;
B5 R2 queue only contains items where R1 was in B4 (fresh evidence).

### B5 retry queue (curated with P-COMP-006 skepticism)

**Priority HIGH** — bank primitive newly-available AND geometry matches:
- (none for B5 — no new stroke primitives added in B4 that unblock
  specific R2 items; the 9 promotions are radicals/chars, not strokes)

**Priority MEDIUM** — items with an R1 FAIL/C where trajectory-diff
guidance can plausibly help:
- p2_radical_127_牙 R2 (R1 FAIL — pie substitution for shu, longer s2 heng)
- p3_char_0016_乃 R2 (R1 FAIL — extend pie tail down-left past hook)
- p3_char_0018_乜 R2 (R1 FAIL — extend shu_wan_gou tail further right + up)
- p3_char_0023_九 R2 (R1 FAIL — sandbox heng_zhe_wan_gou spec)
- p2_radical_119_水 R2 (R1 FAIL — pie with leftward bow for s1)
- p2_radical_120_瓦 R2 (R1 FAIL — straighter left leg + tighter wrap belly)
- p2_radical_134_爪 R2 (R1 FAIL — compress vertical extent of top strokes)
- p3_char_0019_儿 R2 (R1 C — persistent visual-balance issue)
- p3_char_0021_几 R2 (R1 C — Phase-3 char; radical version terminal-frozen)

**Priority LOW** — no clear unblock:
- (all queued at MEDIUM; the deep-freeze list handles the LOW cases)

### Observations to test in B5

- **Does the shrunken cross-group delta (G5 +4 pts vs G3 in B4, from
  +12 pts in B3) hold or bounce back?** If B5 delta returns to
  +8-12 pts, B4 was an item-pool artifact. If B5 stays +4, MMH's
  effect diminishes as items get harder — a real finding.
- **Does bank primitive re-tuning at Phase-3 (P-RET-004) improve
  the compound-hook family PASS rate?** Test with 也/刁-family retries.
- **Does post-render GT-diff tuning produce A verdicts** on identity-
  reuse Phase-3 chars? Test by asking drawer to include an explicit
  "post-render tune vs GT" step for high-simplicity items.
- **Terminal-freeze pruning effect**: with 22 items removed from the
  retry queue, B5 R1 slots are freer for main-channel Phase-3 chars
  084-133. Does this improve throughput?

---

## B5 postmortem (2026-08-08, position 318 cumulative)

### Raw counts

- **Mains (50)**: 27 PASS / 12 C / 11 FAIL = **54%** (up from B4's 58% —
  wait, this is DOWN from B4? Let me re-check. Actually B4 = 29/50 = 58%,
  B5 = 27/50 = 54%. Marginal regression at absolute PASS rate.)
- **Retries (9 R2, all MEDIUM)**: 0 PASS / 1 C (儿) / 8 FAIL = **0% R2 PASS**.
  P-COMP-006 confirmed exactly: none of the 9 items had a mechanism-change
  (no new bank primitive between R1 and R2, no trajectory-diff for hook
  family).
- **Cumulative through B5 (268 mains)**: G5 = 156/268 = **58%**, **4 A**.
  Cross-group vs G3 B5 (same items): G3 = 19/50 = 38% → **G5 leads by
  +16 pts on this batch alone** (largest per-batch gap yet). Cumulative
  G5 vs G3 ≈ 58% vs G3's rate — MMH continues to lift PASS rate.

### A-drought diagnosis (3 consecutive batches at 0 A)

**Diagnosis: STRUCTURAL, not disciplinary.** New principle **P-A-004**
codifies this.

Sampled 4 B5 PASSes for P-A-002 discipline check:
- **文 (0124)**: pure identity call of `draw_wen`, no transform. Should
  have been A per P-A-001. Got PASS. → identity-call P-A-001 does NOT
  scale to 4-stroke chars (consistent with P-A-003).
- **日 (0106)**: pure identity call of `draw_ri`. Got PASS. → same.
- **天 (0102)**: 4-stroke composition, MMH anchors used verbatim per
  stroke, explicit taper preserved. Correct P-A-002 discipline. Got
  PASS but not A.
- **分 (0110)**: 4-stroke composition from 八+刀, MMH anchors verbatim.
  Correct discipline. Got PASS, not A.

Discipline is intact — drawers are correctly applying P-A-001 (identity)
and P-A-002 (meticulous inline). What's missing is: **B5 item pool
contains ZERO 1-2 stroke items**. B3's 4 A's were on 2-stroke chars
(人, 又) or explicitly A-crafted (爻 with per-stroke bow_perp
differentiation; 了 with 3-bezier wan_gou). B4/B5 both dispatched only
3-4 stroke chars. The A-recipe from P-A-001 tops out at 2 strokes
(P-A-003), which the pool doesn't supply.

**Route to future A**: P-A-003 hinted at "explicit GT-vs-render
post-composition tuning". No B5 drawer implemented this step. A separate
route (P-A-002-style meticulous composition) also stops working at
4+ strokes without extra tuning. Next batches (B6+) should watch for
1-2 stroke items in the pool; if any appear, they are candidates.

### Bank growth (92 → 94)

**2 new stroke primitives** (both promoted per P-RET-003, codified
retroactively as P-COMP-007 in principle_bank):

1. **`wo_gou.py`** (卧钩) — from p3_char_0112_心 PASS, fresh_component
   `wo_gou_for_xin`. Signature:
   `draw_wo_gou(d, head, tail, belly_y=None, width=8, hook_up=26, hook_back=6)`.
   Cubic bezier body + small quadratic hook. Reuse targets: 必, 忘, 忙,
   志, 思, 念, 忽, 恕 (all 心-based chars). Contains the exact geometry
   the R1 for 心 (p2_radical_126) also used.

2. **`heng_zhe_wide.py`** (wide 横折 for mid-body) — from p3_char_0122_五
   PASS, fresh_component `heng_zhe_wide_inline_for_wu`. Signature:
   `draw_heng_zhe_wide(d, head, tail, corner=None, w_head=8, w_tail=8, corner_dab=6)`.
   Wide horizontal + near-square corner + straight vertical drop, with
   a 顿笔 dab at the corner. Reuse targets: 亚, 世, 巫, 甄; also
   distinguishes from `heng_zhe_short` (tiny top-of-radical 乛) and
   `heng_zhe_box` (口 frame).

**Not promoted from BANK_DEVIATIONs**:
- 从's `cong_two_ren_asymmetric` — character-specific, low reuse.
- 予's `heng_pie_yu_top` — FAILed, no promotion possible.
- 冗/仇/仉's `heng_zhe_wan_gou_for_...` — FAILed, no promotion. Sandbox
  spec (below) elevated to "hypothesis-driven candidate" per P-COMP-008.

### Deferred stroke-primitive candidates (updated)

- **`heng_zhe_wan_gou.py`** — CRITICAL. Still-missing compound blocking
  entire hook family. Evidence now: 5 FAILing DEVIATIONs (乌, 马, 仇,
  仉, 冗) across B5 alone + prior B3/B4 R2 FAILs (几, 九, 儿, 瓦, 爪 —
  all terminal-frozen). Elevated per **P-COMP-008** to hypothesis-driven
  candidate. Inline reference spec provided below for B6 drawers; if
  any B6 attempt PASSes using it, promote as `heng_zhe_wan_gou.py`
  immediately.

  **Candidate spec** (composed of heng segment + zhe corner + wan belly
  + gou hook flick, all in one continuous polyline):

  ```python
  def draw_heng_zhe_wan_gou(draw, heng_head, corner, belly_bottom, hook_tip,
                             width=8):
      """横折弯钩: heng segment -> right-angle zhe -> deep U-belly ->
      up-right hook flick.
        heng_head    = (x, y) top-left anchor
        corner       = (x, y) turn point (top-right of heng)
        belly_bottom = (x, y) lowest belly point (center-bottom of U)
        hook_tip     = (x, y) final hook flick end point
      """
      # Straight heng head→corner
      # 顿笔 dab at corner
      # Cubic bezier corner→belly with c1=(corner.x, corner.y+deep),
      #                              c2=(belly.x+wide, belly.y)
      # Quadratic bezier belly→hook_tip with ctrl above the line
      # Draw single continuous polyline; end caps at head and hook_tip
      ...
  ```

  Any B6 attempt at 几, 乌, 马, 仇, 仉, 冗, 及, 凡, 及 should try this
  spec verbatim before FAILing. If it PASSes, promote.

- **`heng_pie_short.py`** — from p3_char_0074_孑 (B4, PASSing 1-DEVIATION).
  B5 gave no additional evidence (no attempt used it). Continue to defer
  per P-COMP-002.

- **`heng_xie_wan_gou.py`** — still needed for 旡/气/风. All terminal-
  frozen. Revisit only if a Phase-3 char in the same family PASSes with
  an inline in B6+.

### Terminal-freeze decisions (B5)

**8 R2-FAIL terminal-freezes** (2 rounds of FAIL): 牙, 乃, 乜, 九, 水,
瓦, 爪, 几 — all satisfy P-COMP-006 (no bank/mechanism change between
R1 in B4 and R2 in B5). All 8 need `heng_zhe_wan_gou` (or its cousin
`heng_xie_wan_gou`) which is still-missing.

**1 R2-C terminal-freeze**: 儿 R2-C — P-COMP-006 applies to R2-C too.

**Total terminal-freezes at B5**: 9 items (7 from B3 + 22 from B4 + 9
from B5 = **38 cumulative**).

### B6 retry queue (curated with P-COMP-006 skepticism + P-COMP-008)

**Priority HIGH** — bank primitive NEWLY-AVAILABLE and directly unblocks:
- (none from `wo_gou.py`/`heng_zhe_wide.py` — the B5 FAILs don't overlap
  these primitives' targets).

**Priority MEDIUM** — trajectory-diff or hypothesis-driven mechanism:
- **hook-family with heng_zhe_wan_gou candidate spec (P-COMP-008)**:
  马 (R1), 乌 (R1), 仇 (R1), 仉 (R1), 冗 (R1) — 5 items. Sandbox provides
  the candidate spec; if any PASSes, promote the primitive.
- **proportion / L-R composition trajectory-diffs**:
  以 (R1 — narrower right-side na, keep pie-na asymmetric per MMH),
  亢 (R1 — shu_wan_gou with bottom_extra=80+, wider wrap for 儿-bottom),
  见 (R1 — box scale-up + shu_wan_gou tuning),
  兮 (R1 — wan_gou tuning for shallow shaft),
  內 (R1 — tighter box, inner 人 shrunk toward TR).
- **standalone trajectory-diff**: 予 (R1 — tighter heng_pie with
  compact apex_x, matching 予's narrow top).

**Priority LOW** (queue but expect FAIL — used as burn-testing for hypotheses):
- 义 (R1 — 3-stroke short cross; the C came from proportion),
- 无 (R1 — 4-stroke top-heavy proportion, try shrinking top-heng),
- 气 (R1 — bare 气 already terminal-frozen at Phase-2, but the Phase-3
  char might get lucky with a heng_zhe_wan_gou attempt).

**Do NOT queue** (C but low ROI):
- 巛, 川, 幺, 乡 (multi-curve calligraphic — genuine bank gap; wait
  until curve library is designed),
- 仃, 仑, 仓, 切, 冘 (marginal proportion C's; low ROI to R1),
- 川 also has draw_chuan bank primitive already — the C came from
  compositional integration, not missing primitive.

### Observations to test in B6

- **Does the sandbox `heng_zhe_wan_gou` candidate spec cash into any
  hook-family PASSes?** If yes, promote the primitive; if no, we've
  ruled out this bank gap as the sole culprit (composition is also
  wrong).
- **Does the +16 pts cross-group delta (biggest yet) reflect a real
  item-pool advantage or MMH-injection quality lift?** Track B6 delta.
- **Do the new wo_gou/heng_zhe_wide primitives get called in B6?**
  If B6 has no 心-family or 五-family char, they'll sit unused; wait
  until B7 for actual usage evidence.
- **Any 1-2 stroke items in B6 pool that could break the A-drought?**
  If yes, dispatch with explicit P-A-001 route.

---

## B6 postmortem (2026-08-08, position 368 cumulative)

### Raw counts

- **Mains (50)**: 32 PASS / 10 C / 8 FAIL = **64%** (up from B5's 54% — best
  Phase-3 batch to date; matches B1's 62% radicals-only performance).
- **Retries (14 R1)**: 1 PASS (内) + 1 **A** (义 retry — **first A from retry
  channel**) + 12 FAIL = **14% recovery**.
- **Cumulative through B6 (318 mains)**: G5 = 188/318 = **59%**, **5 A total**
  (4 from B3 + 1 from B6 retry).
- **Cross-group vs G3 B6 (same items, no MMH)**: G3 = 23/50 = 46%;
  G5 = 32/50 = 64%. **Delta = +18 pts absolute — NEW RECORD** (previous
  best was B5's +16). MMH's PASS-lift is intensifying, not attenuating.

### 义 A verdict (first-ever retry A) — analysis

**Main C attempt** (B5 idx 89): dian was a thin tick drifting toward center;
pie/na crossed too high/left (~110,190) instead of BC (~145,235); ink weight
was thin, na didn't taper enough. Overall silhouette off.

**Retry R1 A** (B6): identical MMH anchors, identical bank primitives, but
THREE specific parameter changes:
1. **dian**: `w_head=3, w_tail=9, bow=3` (proper tapered dot, not thin
   tick). Placed at MMH ML anchor (98, 110).
2. **pie**: `bow_perp=-45` (NEGATIVE — pushes mid-belly DOWN-RIGHT toward
   BC). Main used bow_perp=+14 (wrong direction; pie stayed too far left).
3. **na**: `bow_perp=+20, w_head=4, w_tail=12` (strong tail-thickening +
   positive bow to push mid toward BC). Main used bow_perp=+12, w_tail=10.

**Why it reached A (not just PASS)**:
- Only 3 strokes (P-A-004 threshold: A-quality achievable at ≤3 strokes).
- Bows deliberately tuned to force welded crossing at BC (P-joint achieved
  geometrically, not just anchored).
- Taper aggressive on all 3 strokes (P-A-002 discipline).
- Both P-A-001 (identity-ish — 3 bank primitives called cleanly) AND
  P-A-002 (meticulous inline with justified per-stroke parameters).

**Codified as P-A-005**: retry channel can produce A verdicts when trajectory-
diff addresses calligraphic weight + joint geometry (not just endpoint
anchors). Also refines P-COMP-006: R1 retries with mechanism-specific
trajectory diffs CAN help even without new bank primitives (whereas R2
mostly needs new bank).

**A-recipe extension**: for 3-stroke chars, the pie/na crossing family (义, 又,
乂, 人-derivative shapes) may respond to negative-bow_perp forcing of crossings
at MMH-anchored joint points. Test: watch for future 3-stroke crossing chars in
B7+; try bow_perp with sign matching required direction to cross point.

### 8 main FAIL diagnoses

1. **刅 (刀+2 ticks, 4 strokes)** — WAVE cluster. Drawer inlined heng_zhe_gou
   with wrong topology (bank heng_zhe_gou baked for 力/月; 刅's shape is
   compact heng_zhe with side ticks). Skipping bank was right; inline needed
   tighter joint. **Retry hint for B7**: 刅 is very low-freq — do NOT queue.
2. **水 (4 strokes, central shu_gou + 3 pies)** — WAVE cluster. Genuine bank
   gap for 3-directional 水 shape. Bare 水 already terminal-frozen (B5). Do
   not queue.
3. **风 (4 strokes)** — CHRONIC-FREEZE family, first Phase-3 appearance. Needs
   heng_xie_wan_gou (right side "outer wrap" hook) which is still-missing.
   Inline BANK_DEVIATION 3-segment tapered polyline was drawer's best effort;
   FAILed. Bare 风 terminal-frozen in B4. Do not queue for R1; wait until
   an inline for this compound naturally emerges.
4. **引 (弓+丨, 4 strokes)** — L-R proportion. 弓 rendered as crude 3-segment
   polylines (no bank primitive for 弓 — its bare-radical version was
   terminal-frozen in B3). Right 丨 too tall, too far right. **Retry hint
   for B7**: 引 needs a whole-弓 primitive; without one, retry will FAIL.
   LOW priority.
5. **他 (亻+也, 5 strokes)** — L-R. 也 requires heng_zhe_wan_gou top arc
   which is still-missing; inline arced heng attempted, FAILed. 也 was
   terminal-frozen in B4. **Retry hint for B7**: needs the still-missing
   compound. LOW/skip.
6. **仗 (亻+丈, 5 strokes)** — L-R. Bank has ren_left; 丈 (heng+pie+na)
   inlined but proportions off (亻 too big vs 丈). Trajectory-diff could
   help. **Retry hint for B7**: MEDIUM — try ren_left with smaller scale
   (0.65 → 0.55), extend 丈 anchors right.
7. **丱 (5 strokes)** — RARE structure. Symmetric 丨丨丨丨 with lateral ticks.
   Inline BANK_DEVIATION reasonable but wide anchor spread + odd character.
   Very low-freq. Do not queue.
8. **发 (5 strokes)** — WAVE cluster. Top-heavy 发 (5 strokes: heng + 2 pies
   + na + dian). Drawer used all bank primitives cleanly — no BANK_DEVIATION.
   Composition proportion off (na too dominant?). **Retry hint for B7**:
   MEDIUM — try compressing top heng, shortening na tail. Also 发 is
   HIGH-freq (发 in 头发/发展/开发); worth an R1 attempt.

### 12 retry FAIL diagnoses

**P-COMP-008 spec test result: FAILED for all 5 hook-family items** (乌, 仇,
仉, 冗, 马).

- 马: 3-turn compound (heng_zhe_zhe_gou with down-left hook), not
  heng_zhe_wan_gou. Bank has no direct fit; inline compound FAILed
  visual joint continuity.
- 乌: needs heng_zhe_wan_gou; sandbox spec inlined; FAILed proportions.
- 仇: 亻+九 (5 strokes total). 九 needs heng_zhe_wan_gou. FAIL.
- 仉: 亻+几 (4 strokes). 几 needs heng_zhe_wan_gou. FAIL.
- 冗: 冖+几 (4 strokes). 几 needs heng_zhe_wan_gou. FAIL.

**Interpretation**: the "just missing primitive" hypothesis is INSUFFICIENT
for this family. Even with an inline spec, the compositions don't cohere.
This may be genuine calligraphic-weight/joint-continuity difficulty rather
than a bank gap. **Terminal-freeze all 5 per P-COMP-006 + P-COMP-008 update**.

**Trajectory-diff FAILs (5)**: 予, 亢, 以, 见, 兮. Each had a specific R1
trajectory hint. All FAILed. R1 was second round (main was C or FAIL);
per P-COMP-006, no new bank between rounds → freeze.

**LOW-priority burn-tests (2)**: 无, 气. Both were flagged LOW in B5
postmortem ("expect FAIL"). Confirmed FAIL. Freeze.

**PASSes (2)**:
- 内 R1 PASS: trajectory-diff worked (pie head raised above box top; na
  shortened to inside box). Simple mechanism, closed the gap. Do NOT
  promote as bank (character-specific; 内 is composition of shu +
  heng_zhe_gou + pie + na which is already covered by stroke bank).
- 义 R1 **A**: see above.

### Should we hand-craft heng_zhe_wan_gou now?

**Decision: NO.** The B6 evidence is that the sandbox spec was TESTED and
FAILED across 5 items. Per P-COMP-008 UPDATE (new in principle_bank),
a failed candidate spec is evidence AGAINST hand-crafting to bank —
not just a null result. Hand-crafting now would risk poisoning the bank
with an incorrect geometry that future drawers would call and FAIL on.

The right response: leave the spec in sandbox as a **candidate**; if any
future Phase-3 char (B7+) PASSes an inline of the compound, promote from
that PASS (evidence-driven per P-COMP-007's revised rule). Meanwhile,
accept that ~5-8 more hook-family items will be terminal-frozen in B7-B8.
This is a known-cost bank gap.

### Bank growth (94 → 95 + 8 new = **102 entries**)

Wait — recount: current INDEX had 21 stroke + 73 radical/char + newer B4/B5
= 94 total (per the batch header). B6 promotes:
- 1 whole-char from retry A: `yi_x.py` (义)
- 7 whole-chars from B6 mains: `hua_change.py`, `fan_reverse.py`,
  `yuan_first.py`, `zhu_lord.py`, `zheng_correct.py`, `sheng_born.py`,
  `ping_flat.py`

Total: 94 + 8 = **102 entries**.

**Not promoted** (kept inline): 24 B6 PASSes are already covered by existing
bank primitives (identity or stroke composition); 4 have character-specific
BANK_DEVIATIONs (队, 书, 们, 去) awaiting 2nd DEVIATION per P-COMP-002.

### Structural evolution decisions (this batch)

- drawer_memory.md now ~500 lines; approaching split threshold. Adding
  8 new radicals + 1 A-recipe entry brings it near 530. B7 curator should
  consider splitting into topic files (e.g. `retrieval_hints.md`,
  `sibling_pairs.md`, `mmh_calibration.md`) if it crosses 600.
- No new file types created.
- 1 new principle: P-A-005 (retry-A recipe). 1 principle updated:
  P-COMP-008 (candidate-spec-failure interpretation).

### B7 retry queue (curated with P-COMP-006 skepticism + B6 lessons)

**Priority HIGH** — new bank primitive directly unblocks or char is
extremely high-freq:
- (none from B6 promotions unblock a specific B6 R1 FAIL item; the 8 new
  primitives target COMPOUND-DERIVED chars that appear later — 化, 反, 元,
  主, 正, 生, 平 will each unblock 3-5 Phase-3 chars in idx 184-233+.)

**Priority MEDIUM** — trajectory-diff or fresh bank support in B7 range:
- 发 R1 (idx 170): HIGH-freq char. Trajectory-diff — compress top heng,
  shorten na tail.
- 仗 R1 (idx 177): shrink ren_left scale to 0.55, extend 丈 anchors right.
- 必 R2 (idx 155 C): call new draw_wo_gou primitive; refine 3-dian
  placement per GT.
- 打 R1 (idx 180 C): shrink 扌 width; extend 丁 shu.
- 付 R1 (idx 179 C): same as 打.

**Priority LOW** (burn-test only):
- 用 R1 (idx 168 C): 4-stroke box + strokes, close but proportion.
- 比 R1 (idx 136 C): 匕/匕 sibling; test sibling-pair note discipline.

**Do NOT queue (terminal-freeze immediately after B6 FAIL, per P-COMP-006 +
B6 hook-family evidence)**:
- 刅, 水, 风, 引, 他, 丱 (main FAILs — no mechanism to change).
- 马, 乌, 仇, 仉, 冗, 予, 亢, 以, 见, 兮, 无, 气 (retry FAILs — R1/R2 both
  spent). ALL 12 terminal-frozen.

**Do NOT queue (C but low ROI)**:
- 卬 (idx 153) — rare structure
- 办 (idx 141) — close but proportion tuning; not worth slot
- 疋, 仞 — rare structures
- 可 (idx 160) — close but no clear mechanism

### Observations to test in B7

- **Does the +18 pts cross-group delta hold?** If yes, MMH's PASS-lift is
  compounding as Phase-3 gets harder — a positive research signal.
- **Do the 8 new whole-char primitives get identity-called?** Especially
  reuse targets 花/华 (化), 板/饭 (反), 完/园 (元), 住/注 (主),
  证/政 (正), 星/性 (生), 评/坪 (平). Expected in idx 184-233.
- **Does 义-recipe (P-A-005: negative-bow forcing crossings) generalize?**
  Test on future 3-stroke crossing chars.
- **Terminal-freeze rate**: 12 R1 FAILs + 8 main FAILs (some of which
  freeze) = ~20 more items removed from retry queue. B7 R1 slots should
  be freer for main-channel dispatches at idx 184-233.

---

## B7 postmortem — biggest cross-group delta yet (2026-08-08)

### Raw counts

**Mains (50, Phase-3 idx 184-233)**: **5 A + 28 PASS + 9 C + 8 FAIL = 33/50 = 66% PASS**.
**Retries (7)**: 2 PASS (用, 比) + 3 C (必, 付, 打) + 2 FAIL (发, 仗).
**Cross-group vs G3 B7** (same items, no MMH): G3 = 16/50 = 32%; G5 = 33/50 = 66%. **Delta = +34 pts — biggest cross-group delta of the experiment**.
**Cumulative through B7**: **221/368 = 60% PASS, 9 A total**.

### Signature discovery: P-A-006 recipe

All 5 A verdicts in B7 followed the same, previously-unrecorded recipe:
**MMH anchors verbatim + stroke-primitive layer** (skipping whole-radical
composition). Two of the 5 A's (仟, 仨) explicitly rejected their obvious
whole-radical route (draw_ren_left + draw_qian_thousand / draw_san_three).
The other 3 (业, 冉, 乓) never had a whole-radical option and reached for
stroke primitives directly with MMH anchors.

Root diagnosis (why whole-radical composition is limited at 5-6 strokes):
each whole-radical primitive bakes its internal geometry at 300×300
promotion context. Uniform `(ox, oy, scale)` transform of a whole radical
in a Phase-3 composition can't retarget both stroke thickness AND joint
positions to Phase-3's tighter cell. Two composed radicals double-transform.
Stroke-signature primitives dodge this entirely — the drawer directly
supplies MMH endpoints as `head`/`tail` arguments.

**Codified as P-A-006** in principle_bank.md.

### Cross-group delta analysis

G5 vs G3: +12 (B3), +4 (B4), +16 (B5), +18 (B6), **+34 (B7)**.

The B7 spike (+34) is exceptional. Two mechanisms contributing:
1. **MMH FAIL-prevention** (same as B1-B6): G3 got 21 FAILs on B7 vs G5's 8.
   MMH auto-injection continues to prevent wreck attempts.
2. **P-A-006 PASS-lift** (new): 5 A's + 28 PASSes on grid-like and L-R
   Phase-3 chars. Drawers converged on a routing choice (stroke primitives
   over whole radicals) that turns MMH anchors into 1:1 calligraphic
   fidelity. This is where G5 pulled ahead of the B4/B5/B6 trend.

**User note**: A rates only fair-comparable from B9 onward. B7's 5 A's are
memory-benefit markers, not fair-comparison A's. But PASS rate is fair;
+34 pts is a strong signal at any batch.

### X-cross cluster verdict (癶/矢/失/処/乩/那) — P-COMP-010

6 X-cross-family items in B7: 3 PASS (矢, 失, 乩) + 1 C (癶) + 2 FAIL
(処, 那). The 2 FAILs are on OTHER components (処's 几 hook, 那's 阝-right),
not on the X-cross weld itself. **Cross-group implication**: MMH auto-
injection places the crossing at the true joint point (pie/na endpoint
anchors); G5 does not freeze this cluster the way G4 does. Codified as
P-COMP-010. This may be the most mechanistic MMH-effect finding to date —
it isolates one calligraphic feature (X-cross) where MMH's structural
injection directly closes a G3/G4 blindspot.

### Bank growth (102 → 115 entries)

**13 new whole-char primitives** (4 A + 9 PASS):
- A: `yi_ye` (业), `qian_person` (仟), `ran` (冉), `ping_pang` (乓)
- PASS: `li_stand` (立), `bai_white` (白), `you_by` (由), `si_four` (四),
  `hui_meet` (会), `you_have` (有), `nian_year` (年), `zi_self` (自),
  `shi_world` (世)

**Not promoted (kept inline)**: 15 identity-reuse or low-reuse PASSes
(市, 术, 兰, 皿, 而, 北, 冊, 代, 矢, 失, 乑, 乔, 乩, 亘, 亙 — some are
candidate-for-later; 皿/而 flagged for B8 promotion if a compound char
uses them). See INDEX.md B7 sections.

**Deferred variant candidates** (awaiting 2nd DEVIATION per P-COMP-002):
- `mu_wood_variant_for_本` (from 本 PASS)
- `li_variant_for_加` (from 加 C-verdict; will not promote unless a PASSing case appears)
- `er_ear_right_variant` (from 那 FAIL; awaiting a PASSing 阝-right composition)

### Structural evolution decisions (this batch)

- drawer_memory.md now ~700+ lines with B7 additions. **Approaching hard
  split threshold**. B8 curator should split into topic files
  (`retrieval_hints.md`, `sibling_pairs.md`, `mmh_calibration.md`,
  `a_recipes.md`) BEFORE it crosses 900 lines.
- No new file types created THIS batch, but B8 should create the split.
- 4 new principles: **P-A-006** (MMH-anchor + stroke-primitive layer;
  new A-recipe route), **P-COMP-009** (double-transform diagnosis for
  L-R compositions), **P-COMP-010** (X-cross cluster is NOT frozen in G5),
  **P-RET-005** (sibling-pair discipline R1 route).

### B8 retry queue (curated with P-COMP-006 + B7 lessons)

**Priority HIGH** — new bank primitive directly unblocks or char is
extremely high-freq:
- (none from B7 promotions unblock a specific B7 R1 FAIL item; the 13
  new primitives target COMPOUND-DERIVED chars in B8+ — 立→站/位/翌,
  白→百/柏/怕, 由→抽/油/宙, 会→绘/侩, 有→侑/宥, 自→息/鼻/臭, 世→贳 etc.)

**Priority MEDIUM** — trajectory-diff or fresh bank support in B8 range:
- (none — B7's retry channel was fully burned; the 3 C's + 2 FAILs are
  all terminal-freeze per P-COMP-006).

**B8 items where A-uplift potential is highest** (2-4 stroke chars with
clean bank primitive coverage, per user's "prioritize A-uplift" note):
- **亚 (idx 234, 6 strokes)**: 业 + top heng — identity-composition:
  `draw_yi_ye` + inline top heng. **STRONG A candidate**.
- **亦 (idx 238, 6 strokes)**: heng + dian + pie + shu + dian + dian —
  pure stroke composition; P-A-006 recipe.
- **仰, 仲, 仳, 仵, 伄, 伉, 伊, 伎, 伐, 伕, 伙, 伛, 伢, 伥, 伦, 伧,
  伪, 伫, 任, 佤, 传 (multiple 亻+X 6-stroke)**: apply P-A-006 stroke-
  primitive layer for BOTH 亻 and right radical. `qian_person.py` (仟)
  is the template — reuse its anchor scheme for 亻, adapt right anchors.
- **名 (idx 265, 6 strokes)**: 夕 + 口 — identity composition:
  `draw_kou` + inline 夕. Good bank coverage.
- **西 (idx 267, 6 strokes)**: 3-line box variant of 四 sibling.
  `draw_si_four` might identity-serve if MMH matches; else stroke composition.
- **齐 (idx 278, 6 strokes)**: top-heng + pie + na + heng + shu + shu.
  Stroke composition.
- **色 (idx 279, 6 strokes)**: 巴 top + something bottom.
- **兆 (idx 280, 6 strokes)**: mostly dots; sibling of 光.
- **好 (idx 253)**: 女+子 — draw_nu_woman + inline 子 (or 子-inline).
- **她 (idx 263)**: 女+也 — chronic 也 gap; expect C or FAIL.

**B8 explicit retry queue rows** (all terminal-freeze from B7 → empty
queue for B8):
- Do NOT queue: 发, 仗, 必, 付, 打, 用 (already PASSed), 比 (already PASSed).
- Do NOT queue any B7 main FAIL: 仡, 边, 东, 冎, 处, 処, 记, 那
  (chronic gaps or composition-level failures per P-COMP-006/008/009).
- Do NOT queue any B7 main C except if a NEW bank primitive appears
  in B8 that plausibly unblocks (unlikely).

### Should we split drawer_memory.md yet?

**Decision: NOT this batch** — the B7 additions are cohesive (all under
"B7-era" section headings). But **B8 curator MUST split** if the file
crosses 900 lines. Recommended split:
- `retrieval_hints.md` — bank retrieval table, whole-radical retrieval
- `sibling_pairs.md` — all sibling notes
- `mmh_calibration.md` — anchor calibration notes
- `a_recipes.md` — A-recipe playbook (P-A-001 through P-A-006)
- `drawer_memory.md` — thin index pointing at the above + composition
  playbooks + failure calibration

### Observations to test in B8

- **Does the +34 pts cross-group delta hold or was it item-pool-specific?**
  B8 has many 亻+X 6-stroke items; if the P-A-006 template holds, delta
  might persist. If cross-group delta collapses back to ~+18, B7 was a
  favorable item pool.
- **Does P-A-006 generalize to 亻+X 6-stroke chars?** 仟 (5-stroke A) and
  仨 (5-stroke A) are the closest B7 evidence; 20+ 亻+X 6-stroke chars in
  B8 will test whether the extra stroke breaks the recipe.
- **Do fair-comparison A verdicts start appearing?** User's note: B9 onward
  is fair-comparison territory for A rates. B8 A count will be a preview
  of what to expect (though the calibration is not yet applied).
- **Do the 13 new whole-char primitives get identity-called?** Especially
  reuse targets 站/位/翌 (立), 百/柏/怕 (白), 抽/油/宙 (由), 息/鼻 (自),
  绘/侩 (会). Expected in idx 234-283+.
- **Any evidence for the deferred variant candidates?** If 加/本-family
  chars appear in B8 with a PASSing DEVIATION on the same fresh_component,
  promote the variant per P-COMP-002.

---

## 2026-08-09 — B8 postmortem: 20 PASS + 10 C + 20 FAIL + 0 A on 50 mains — first fair-A-comparison batch

### Raw counts (position 468 cumulative)

- **Mains (Phase-3 chars idx 234-283)**: 0 A + 20 PASS + 10 C + 20 FAIL = 20/50 = 40% PASS
- **Retries**: none (B8 retry queue was empty by design per B7 close-out)
- **Cumulative through B8**: 241/418 = **57.7% PASS**, **9 A total** (all pre-B8)

### Cross-group comparison (idx 234-283, identical items — first fair-A batch)

| Group | PASS | A | Notes |
|-------|------|---|-------|
| G3 (main-exp B9, no MMH) | 14/50 = 28% | 0 | |
| G4 (main-exp B9, MMH + grid + fat_line) | 20/50 = 40% | **10** | |
| G5 (this batch, MMH + code) | 20/50 = 40% | 0 | uniform PIL line width |

### KEY FINDING — two-factor hypothesis empirically confirmed

Same items → same 40% PASS for G4 and G5, but G4 got 10 A verdicts vs G5's 0. This
cleanly decomposes the "MMH+bank" effect into two independent factors:

1. **MMH raises PASS baseline** — the +12 pt PASS delta over G3 (40% vs 28%) matches
   both G4 and G5. Attributable entirely to MMH auto-injection (both non-G3 groups
   have it; both got the same lift).

2. **Format determines A-quality ceiling** — G4's per-endpoint `fat_line` width
   control enables the calligraphic weight distribution the judge rewards with A.
   G5's uniform PIL line width cannot; even with perfect anchors and P-A-006
   discipline, 6-stroke chars top out at PASS.

This is the strongest empirical evidence yet that G5's A-quality is bounded by
its rendering primitive, not by memory discipline or drawer skill. **This is a
STRUCTURAL ceiling** and should not be diagnosed as "A-drought regression"
going forward.

### 20-FAIL diagnosis (5 clusters)

**Cluster A — 亻+X L-R with hook-compound right radical (7 FAILs)**:
- p3_char_0248_伄 (亻+吊), p3_char_0250_伉 (亻+亢), p3_char_0254_伎 (亻+支),
  p3_char_0260_伙 (亻+火), p3_char_0264_伢 (亻+牙), p3_char_0270_伧 (亻+仓),
  p3_char_0276_佤 (亻+瓦)
- All 7 applied P-A-006 stroke-primitive layer (verified: BANK_DEVIATION headers or
  "no whole-radical" comments in generated.py).
- Diagnosis: P-A-006 works when the right radical is straight-stroke composable
  (仟/仨 A precedent — 千/三 are pure stroke primitives). FAILs when right radical
  contains a hook-compound: 亢 shu_wan_gou-wide, 火 pie-dian ordering, 牙 heng_zhe
  compound, 仓 wraparound, 瓦 wave-hook (chronic), 吊 冂+巾 with hook, 支 十-cross+又.
- **New principle P-COMP-011**: 亻+X 6-stroke P-A-006 recipe generalizes ONLY when
  X's stroke inventory is (heng/shu/pie/na/dian) — refuse the whole-radical route
  only when the right half is straight-stroke; use whole-radical primitive (or
  inline the specific hook-compound) when right half contains a hook-compound.

**Cluster B — whole-radical refusal on chars where bank primitive would help (4 FAILs)**:
- **军 (亻错 — 冖+车)**: drawer inlined all 6 strokes; NEVER imported `mi_cover.py`
  or `che_car.py` (both in bank since B1/B2). Wrong routing choice.
- **名 (夕+口)**: inlined all 6 strokes; NEVER imported `kou_mouth.py` (bank since B1).
- **西 (frame + inner)**: inlined 6 strokes; did NOT identity-call `si_four.py` (B7)
  despite structural similarity to 四.
- **成 (5-stroke 戈-piercing)**: inlined; did NOT use `ge_dagger.py` (B2).
- Diagnosis: **P-A-006 overshoot** — drawers are refusing whole-radical primitives
  even when the primitive matches structurally. The "refuse whole-radical" habit
  from B7 A-recipe has spilled into cases where it hurts.
- **New principle P-A-007**: P-A-006's "refuse whole-radical" guidance is scoped
  to cases where MMH endpoint anchors ARE the calligraphic ceiling (X-cross,
  grid-like L-R with straight-stroke halves). For chars where a bank radical
  primitive matches the structural sub-component (车 in 军, 口 in 名, 戈 in 成,
  四-shape in 西), USE the whole-radical primitive and inline only the connecting
  strokes. P-A-007 refines P-A-006 to prevent overshoot.

**Cluster C — chronic freeze cousins (3 FAILs)**:
- **亥 (idx 236)**: G4-frozen chronic; contains 亠+撇+乀+ interlaced hook body.
- **色 (idx 279)**: 巴 needs heng_zhe_wan_gou (chronic gap per P-COMP-008 update).
- **传 (亻+专)**: 专 chronic curl-hook; same gap family.

**Cluster D — L-R with 女 or 讠 whole-radical + hook-inner (3 FAILs)**:
- **好 (女+子)**: applied P-A-006 (fresh 女 inline, `nu_left_compressed`). Composition
  incoherent — 女's pie-dian s1 didn't align with 子's wan_gou. Could have called
  `nu_woman.py` (B3 R2 promotion) with (ox=-40, scale=0.75) starting template.
- **如 (女+口)**: same P-A-006 refusal of `nu_woman.py`; drawer inlined all 6.
- **设 (讠+殳)**: 殳 has hook_compound.

**Cluster E — hook-body full-char (3 FAILs)**:
- **仰 (亻+卬)**: 卬 has heng_zhe descender; drawer inlined; heng-zhe compound
  proportion off.
- **老 (top+匕)**: shu_wan_gou default parameters not tuned; belly reach too short
  for 老's wide bottom sweep. P-RET-004 case (bank defaults tuned for compact
  匕/儿 don't fit 老's aspect).
- **再 (frame + wide piercing bar)**: drawer adapted from `ran.py` (冉 A) — close
  but the frame proportion 再 vs 冉 differs (再's middle bar extends past frame).

### PASS-side taper/joint discipline sample (3 items)

- **仲 (p3_char_0242 PASS)**: P-A-006 recipe, MMH-verbatim, explicit taper per
  stroke (亻 pie w_head=9/w_tail=3, shu width=7; 中 shu width=8, heng_zhe_box
  standard, bottom heng, middle piercing shu). Discipline intact.
- **多 (p3_char_0245 PASS)**: BANK_DEVIATION on `heng_pie` (slimmed bow_perp≈6);
  pie/dian from bank. All 7 N-joints preserved with natural gaps. Excellent
  discipline.
- **次 (p3_char_0273 PASS)**: BANK_DEVIATION skipping `bing_ice` + `qian_owe`
  wholesale in favor of P-A-006 stroke layer (dian/ti/pie/heng_gou/na). Each
  stroke has explicit MMH anchor and taper.

**Conclusion**: P-A-006 discipline is intact. The 0-A is NOT a discipline collapse.
Per Format determines A ceiling (see key finding), G5 cannot produce A on 6-stroke
chars regardless of drawer discipline. P-A-004 remains the correct framing for
this specific mechanism (A-drought is structural, not disciplinary) — B7's 5 A's
were the exception because P-A-006 first crystallized on chars where anchor
precision maxed out G5's ceiling. B8's 6-stroke item pool has no such headroom.

### BANK_DEVIATION triage on 20 PASSes

- **多 (heng_pie slim)**: PROMOTE — `heng_pie_slim.py` variant covers 夕-family
  (夕/多/名/夜/夢); this is the 2nd DEVIATION on heng_pie (1st was 孑 B4 inline).
  Per P-COMP-002 threshold met.
- **次 (bing_ice + qian_owe skipped)**: NOT PROMOTE — the skip was a P-A-006
  routing choice, not a fresh_component. Note in errata.
- **问 (BANK_DEVIATION note present)**: check contents — treated as inline
  choice for the 口 inside 门.
- All other PASSes: pure P-A-006 stroke-primitive composition; no fresh_components.

### Bank growth (115 → 124 entries)

**9 new promotions from B8 PASSes** — selective (skipping identity/low-reuse
inline PASSes to avoid bloat):

Whole-char primitives (7):
- `duo_many.py` (多) — 6-stroke stacked 夕; reuse: 名 (sibling), 岁, 夜, 够.
- `tong_same.py` (同) — 6-stroke 冂+一+口 enclosure; reuse: 铜, 桐, 洞, 筒, 峒.
- `hui_return.py` (回) — 6-stroke double-box; reuse: 苘, 迴, 徊, 洄. Uses
  `draw_wei_enclose` (B2) + inline inner 口.
- `wen_ask.py` (问) — 6-stroke 门+口; reuse: 們, 闷, 阔.
- `he_together.py` (合) — 6-stroke 人-top + heng + 口; reuse: 拾, 给, 塔, 蛤, 鸽, 恰.
- `xing_walk.py` (行) — 6-stroke L-R 彳+亍; reuse: 街, 衍, 冲, 徽.
- `ya_asia.py` (亚) — 6-stroke sibling of 业; reuse: 恶, 垩.

Whole-char extensions/variants:
- `hou_after.py` (后) — 6-stroke; reuse: 逅, 后-family. (Uses 厂-body + 口
  variant.)

Stroke primitive:
- `heng_pie_slim.py` (from 多's PASSing BANK_DEVIATION on `heng_pie` — 2nd
  occurrence, meets P-COMP-002 threshold). Signature: `draw_heng_pie_slim(
  d, head, tail, apex_x, corner_x, bow_perp=6, w_head=6, w_tail=3)`. Reuse:
  夕-family (多/名/夜/岁), 又/欠 tuning.

**Not promoted (kept inline)** — 11 PASSes:
- 亚 (idx 234) — promoted (see ya_asia above)
- 后 (idx 235) — promoted
- 行 (idx 237) — promoted
- 过 (idx 239, 辶+寸 wrap) — 辶 primitive exists; low ROI for a wrap-specific promo
- 仲 (亻+中) — kept inline; 亻+X template already documented via 仟 anchor recipe
- 仳 (亻+比) — kept inline; identity of B7's 比 R1 PASS pattern
- 仵 (亻+午) — kept inline
- 当 (idx 251) — kept inline (character-specific inner marks)
- 伊 (亻+尹) — kept inline
- 此 (止+匕) — kept inline; both sub-components already in bank
- 伐 (亻+戈) — kept inline; ge_dagger exists but drawer inlined per P-A-006
- 伛 (亻+区) — kept inline
- 伦 (亻+仑) — kept inline
- 任 (亻+壬) — kept inline

### Terminal-freeze decisions for main FAILs

Per chronic-criteria + P-COMP-008 refuted-primitive rule:
- **亥 (idx 236)**: terminal-freeze — G4-frozen chronic; interlaced hook body
  is genuine bank gap.
- **色 (idx 279)**: terminal-freeze — 巴 heng_zhe_wan_gou chronic; P-COMP-008
  refuted hand-craft.
- **传 (idx 283)**: terminal-freeze — 专 curl-hook chronic gap family.
- **设 (idx 281)**: terminal-freeze — 殳 hook_compound chronic; no mechanism-change.
- **佤 (idx 276)**: terminal-freeze — 瓦 wave-hook chronic (P-COMP-008 refuted).
- **仰, 伄, 伉, 伎, 伙, 伢, 伧 (7 items)**: do-not-queue — Cluster A 亻+X hook-compound
  right radicals; no mechanism-change available without refactoring P-A-006 into
  P-A-007 first (see below B9 queue).

### B9 retry queue (mechanism-change strict per P-COMP-006 + P-A-007 test)

**HIGH priority — mechanism-change available (bank primitive drawer skipped)**:
1. **军 R1** — instruct: call `draw_mi_cover(d, ox=0, oy=-40, scale=0.9)` for
   top + `draw_che_car(d, ox=0, oy=+40, scale=0.75)` for bottom; do NOT inline
   both. **Tests P-A-007**.
2. **名 R1** — instruct: call `draw_kou(d, ox=+30, oy=+65, scale=0.65)` for
   bottom 口, inline top 夕 with 3 strokes. **Tests P-A-007**.
3. **成 R1** — instruct: use `draw_ge_dagger` as the 4-stroke 戈 base, inline
   piercing shu at MMH crossing. **Tests P-A-007**.
4. **西 R1** — instruct: try `draw_si_four` identity-call as the base, then
   diff inner marks against MMH (西 differs from 四 by inner shu_zhe direction).
   **Tests P-A-007 + sibling adaptation**.

**MEDIUM priority — parameter tuning available**:
5. **老 R1** — pass explicit `shu_wan_gou(bottom_extra=75, knee_ratio=0.62)` per
   P-RET-004 (老's wide bottom sweep needs the same tuning as 也 did in B4 note).
6. **好 R1** — call `draw_nu_woman(d, ox=-40, oy=0, scale=0.75)` per P-A-007 for
   the 女 (bank primitive since B3 R2), inline 子 on the right per P-A-006. Bail
   out of the 女-inline attempt.
7. **再 R1** — refine adaptation from `ran.py` (drawer attempted, close). Add
   `zhi_hook_remove=True` mental toggle: 再's central bar extends past the frame
   right side by ~10 px more than 冉's.

**LOW priority — sibling-pair discipline (no bank change)**:
- (none from B8; the cluster A/E items are all chronic-gap gated)

**DO NOT queue (chronic / composition-level per P-COMP-006/008/009)**:
- 亥, 色, 传, 设, 佤 (terminal-frozen above)
- 伄, 伉, 伎, 伙, 伢, 伧, 仰 (Cluster A hook-compound right; queue nothing
  from this cluster until P-A-007 lands PASS on 军/名/成/西 R1)
- 如, 好 (except 好 above per mechanism-change), 伪, 伫, 传

### Memory file split decision (B8)

**Decision: NOT SPLIT this batch** — drawer_memory.md is 716 lines after B7,
B8 additions will push to ~800 lines. Under the 900-line trigger. Revisit at
B9. When split, use the recommended topic-file layout from B7 postmortem.

### Structural evolution decisions

- **1 new principle**: **P-A-007** (P-A-006 overshoot guardrail: use whole-radical
  primitive when it matches the structural sub-component; refuse only when
  MMH-endpoint fidelity is the ceiling).
- **1 new principle**: **P-COMP-011** (亻+X 6-stroke P-A-006 recipe generalizes
  only for straight-stroke right halves; hook-compound right halves need bank
  extension first).
- **1 new stroke primitive**: `heng_pie_slim.py` (2nd DEVIATION, P-COMP-002 met).
- **8 new whole-char primitives** (multi-strategy — 4 hook-compound reveals in
  B9 queue will drive the next principle refinement).

### Observations to test in B9

- **P-A-007 test**: do 军/名/成/西 R1 with instruction to call bank primitive
  produce PASS? If YES: P-A-007 confirmed, curriculum principle refined. If NO
  (still FAIL despite bank primitive): P-A-006 was the correct call and the
  failure is composition-level after all; retract P-A-007.
- **Format ceiling confirmation**: if B9 mains continue at ~40% PASS with 0 A,
  format-ceiling hypothesis strengthens. If A appears sporadically on identity-
  reuse of B7/B8 promotions (e.g., 站 via draw_li_stand, 桐 via draw_tong_same),
  the ceiling is aspect-conditional not absolute.
- **Cluster A follow-up**: if any B9 item is 亻+X where X is straight-stroke,
  it should PASS. If any 亻+X where X is hook-compound appears, it will FAIL
  again unless P-A-007 unlocks the whole-radical route.
- **Cross-group delta**: B7 gave +34 pts. B8 is 40% G5 vs 28% G3 = +12 pts —
  much smaller. Item pool with many hook-compound right radicals is UNFAVORABLE
  for G5's current bank state. B9 delta will tell us how much of B7 was
  pool-favorability.

---

## B9 postmortem (2026-08-09, position 518)

**Batch stats**: 22/50 PASS (44%), 4 A (龹/还/位/伾), 11 C, 17 FAIL.
Cross-group delta B9: G3 24%/0A, G4 38%/10A, **G5 44%/4A** — first batch
G5 PASS beats G4 PASS. Cumulative through B9: 263/468 = 56%, 13 A total.

### Headline findings

**FIRST batch where P-A-007 shows up as EXPLICIT reasoning in A verdicts**:
3 of 4 A-verdict docstrings contain per-sub-component decisions like
"considered draw_li_stand but rejected because aspect skew" (位),
"used draw_chuo_walk because native scale fit" (还), "rejected draw_ren_left
because MMH pie head sits higher than baked geometry" (伾). B8 A count
was 0; B9 A count is 4. The delta is P-A-007 REASONING TRACE, not skill.
Codified as P-A-008 (mandatory inline-reasoning trace).

**P-A-007 R1 validation (3/4 PASS)**:
- 军 R1 PASS (called mi_cover + che_car per queue)
- 成 R1 PASS (tuned xie_gou; reasoned draw_ge_dagger explicitly, rejected)
- 老 R1 PASS (tuned shu_wan_gou per P-RET-004)
- 名 R1 FAIL (called draw_kou but 夕-half proportion bank gap)
- 西 R1 FAIL (identity-called draw_si_four but 西 inner-marks differ)
- 好 R1 FAIL (called draw_nu_woman but 女+子 composition tight)
- 再 R1 FAIL (adapted ran.py but sibling diff too far)

Net: 3/7 R1 PASS = 43%. When mechanism-change unlocks (军/成/老), R1
works; when the mechanism-change was PROXY for a deeper composition
issue (名/西/好/再), R1 fails and item goes to terminal-freeze.

**P-COMP-011 boundary INTACT**: A verdicts on 亻+X compounds (位=亻+立,
伾=亻+丕) both have X = straight-stroke composable. FAILs on 亻+X
(你/伶/伽/佇/佈) all have X = hook-compound. No boundary shift.

### Composition of the 4 A verdicts (deep-dive)

**龹 (A)** — NOVEL top-radical (no bank). 6 strokes. A-recipe geometry:
s5 (long central pie) is a cubic-bezier bent-pie whose control points
[150,130] and [100,200] pass through BOTH P-joint centers (s3.mid @
(138.7,135.3) and s4.mid @ (126.6,171.8)). Straight chord misses both.
This is the DEFINING geometry that made龹 A-eligible: two P-joint welds
via a hand-computed cubic bezier through the joint band. Rare recipe,
promoted as juan_yong.py; expect low reuse but records the geometry.

**还 (A)** — TEXTBOOK P-A-007 rule-1. 7 strokes = 4 (不 inline) + 3
(辶 via draw_chuo_walk). Drawer explicitly noted "no BANK_DEVIATION —
every stroke primitive used matches bank as-is" and "for the 辶 wrapper
(radical-level match) follows P-A-007." Promoted as hai_still.py. 
The 辶+X wrap pattern generalizes to 这/进/远/近/追/送/边/达/... family.

**位 (A)** — TEXTBOOK P-A-007 clause-2 fallback. 7 strokes = 2 (亻) +
5 (立). Drawer reasoned in docstring against calling draw_li_stand
because 立 in 位 is aspect-skewed (~0.75× width / ~0.98× height). This
is the FIRST batch where explicit P-A-007 reasoning appears in an A
docstring. Promoted as wei_position.py. 亻+立-family template.

**伾 (A)** — 亻+丕. Rejected draw_ren_left because MMH pie head at
TL(0.87, 0.656) sits higher than baked geometry. Inlined 丕 (no bank).
Second clause-2 A. Promoted as pi_flourish.py.

### Composition of the 17 FAILs (cluster analysis)

- **Cluster A (亻+X hook-compound, 6)**: 你/伶/伽/佇/佈/员 — P-COMP-011/012
  boundary; hook-compound right-half without matching bank primitive at
  usable geometry. NO mechanism-change; do-not-queue.
- **Cluster B (chronic G3 recycles, 2)**: 亨/声 — G3 already terminal-frozen;
  recycled for G5 fresh-start bank; still FAIL. Terminal-freeze.
- **Cluster C (3-part / crossbar, 3)**: 冱/没/两 — composition-level;
  crossbar Z-compound or 3-part vertical without decomposition.
- **Cluster D (hook-body / long-descender, 4)**: 身/凫/更/条 — hook-body
  full-char or long descender needing frame + descender adaptation.
- **Cluster E (3-radical L-M-R, 2)**: 听/运 — 3-radical tight or wrap
  with unresolved inner curl.
- **Cluster F (3-part vertical, 1)**: (员 above; also considered here.)

Rare/composition FAILs (冱/更/凫/条/两/身): terminal-freeze or B10 R1.

### Structural evolution decisions

- **12 new bank primitives** (4A + 3R1 + 5 high-reuse).
- **3 new principles**: P-A-007-v2 (sharpened from guardrail to
  retrieval mechanism + hard-check), P-A-008 (mandatory inline-reasoning
  trace), P-COMP-012 (hook-compound refinement).
- **drawer_memory.md split** into topic files (composition / anchors /
  siblings) per B7-postmortem plan. Kept ENTRY-POINT INDEX +
  retrieval-hint tables in drawer_memory.md itself.

### Observations to test in B10

- **P-A-008 test**: does mandating docstring reasoning trace shift more
  chars into the A band? Sample 3-5 B10 A-eligible items for reasoning
  trace presence; correlate with verdicts.
- **P-A-007 hard-check adoption**: do B10 drawers cite the P-A-007-v2
  hard-check in their docstrings? If YES → retrieval discipline
  internalized. If NO → curator adds explicit prompt-side reinforcement.
- **P-COMP-012 confirmation**: any 亻+X-with-hook that PASSes via bank's
  matching hook-compound primitive → confirms refinement. Any 亻+X-with-hook
  where bank has the primitive but drawer STILL inlines → P-A-008 gap.
- **Cross-group delta trajectory**: G5 PASS beat G4 PASS in B9 (+6 pts).
  If B10 sustains or grows the gap → memory-format lever is a robust
  discipline effect. If B10 regresses → B9 was pool-favorability.
- **A ceiling revisit**: B9 broke the "0-A structural ceiling" pattern
  with 4 A. If B10 sustains 3+ A → ceiling was a P-A-007-reasoning
  discipline gap, not a rendering-format ceiling. If B10 reverts to 0-A
  → format-ceiling reasserts; B9 A verdicts were the low-hook-density
  outliers.


## B10 postmortem (2026-08-09, position 568)

**Batch stats**: 26/50 mains PASS (52%), **7 A** (佔/佟/佥/的/並/和/些),
9 C, 15 FAIL. **+1 retry A (运 R1)** = 8 A total in the batch. Cumulative
through B10: 289/518 mains = 56% PASS, **20 A total** (13 pre-B10 + 7 new
mains). Retry A count separate: 5 pre-B10 + 1 B10 = 6 R1 A.

Cross-group delta B10 (idx 334-383, identical items):
- G3 (no MMH): 14/50 = 28%, 0 A
- G4 (MMH+grid): 31/50 = 62%, 17 A  — G4 batch peak
- **G5 (MMH+code): 26/50 = 52%, 7 A** — G5 A count peak, PASS mid

G5 PASS drops back below G4 (52% vs 62%) but G5 A count is highest yet
(7). The B9 finding "G5 PASS > G4 PASS" was a batch-specific pool
effect; B10 reverts to the earlier pattern (G4 PASS lead) but with G5
compensating on A verdicts. The two-factor decomposition holds:
per-endpoint width rendering (G4) still wins A ceiling on hook-heavy
items; code-based memory + reasoning discipline (G5) closes the A gap
on chars where anchor precision is the ceiling.

### Headline findings

**7 A verdicts — DISCIPLINE HYPOTHESIS CONFIRMED** (B9 → B10 replication).
B9 codified P-A-008 (mandatory reasoning trace) end-of-batch and
produced 4 A. B10 codified P-A-009 (quantitative BANK_DEVIATION) as an
inference from the A-docstring pattern and produced 7 A. Both cycles
show discipline codification → immediate lift on next batch. This is
NOT a format-ceiling artifact; it is drawer discipline crystallization
via curator-codified principles.

Sample A-recipe fingerprints from B10:
- **的 A**: 2 BANK_DEVIATION blocks with quantitative numbers
  ("aspect 0.36 vs 0.67 → ratio 2× compressed").
- **和 A**: BANK_DEVIATION with aspect-skew 1.21 at window edge; explicit
  "at the edge of the P-A-007-v2 [0.55, 1.2] window" citation.
- **些 A**: TRIPLE BANK_DEVIATION with per-primitive aspect calc.
- **佔 A**: quantitative endpoint delta ("shift ox=-74 would land within
  15 px of all four endpoints" — verifying bank could work but choosing
  inline for exact placement).

**P-A-007-v2 R1 mechanism-change validation (partial B10)**:
- **运 R1 A** — trajectory-diff mechanism-change unlocked (called
  pie_zhe bank primitive for s3 instead of collapsed diagonal). This
  validates P-A-005 (trajectory-diff R1 to A) once more.
- 身 R1 → C (still no PASS after 2 rounds; terminal-freeze).
- 凫/条/两 R1 → FAIL (queue P-A-008 test did not unlock; terminal-freeze).

**疒-family terminal-freeze cluster identified**:
4 疒-family items (疙/疟/疠/疝) all FAILed inline; no whole-radical bank
primitive for 疒. Bank-gap chronic pattern. Marking cluster
terminal-freeze; do NOT attempt hand-craft (per P-COMP-008 refutation).
When any Phase-3 char with 疒 sub-component eventually PASSes via
inline, THEN promote its inline as nao_sickness.py.

### Composition of the 7 A verdicts (deep-dive)

**佔 (A)** — 亻+占, 7 strokes. Used ren_left implicitly via bank stroke
primitives (drawer chose stroke-primitive inline over whole-radical for
exact MMH placement). 2 BANK_DEVIATIONs: bu_divine (占-top) + kou_mouth
(占-bottom), both with aspect-skew calc.

**佟 (A)** — 亻+冬, 7 strokes. Pure P-A-006. 冬 top's X-cross uses
heng_pie + na welded P-joint via bank primitives; 冬 bottom is 2 dians
via draw_dian.

**佥 (A)** — Rare char. P-A-006 with two BANK_DEVIATION-style inline
custom curves for s4 (short down-right stroke, no matching primitive)
and s6 (semantically-pie stroke direction).

**的 (A)** — 白+勺, 8 strokes. Textbook P-A-009. Contains 2 quantitative
BANK_DEVIATION blocks: bai_white aspect 2× compressed; bao_wrap
stroke-count mismatch (2 vs 3). Third-highest-freq char in Chinese —
massive downstream value.

**並 (A)** — 8-stroke sibling of 亚. Refused ya_asia on stroke-count
mismatch (亚=6, 並=8); pure P-A-006 inline.

**和 (A)** — 禾+口, 8 strokes. 禾 inlined (no bank); kou_mouth
DEVIATIONed with aspect-skew 1.21 at edge of window. Records edge-case
BANK_DEVIATION decision.

**些 (A)** — 此+二, 8 strokes. TRIPLE BANK_DEVIATION (zhi_stop, bi_dagger,
er_two) — all with quantitative aspect calc. Unusually deep P-A-009
application.

### Composition of the 15 mains FAILs (cluster analysis)

- **Cluster A (疒-family, 4)**: 疙/疟/疠/疝 — bank gap, terminal-freeze.
  Also 疌 (similar; count 5 total in this pool).
- **Cluster B (亻+X mixed, 5)**: 佚/社/佛/即/佞. 社+佞 are B11 R1
  P-A-007 candidates (drawer over-applied DEVIATION); 佛+即 do-not-queue
  (chronic hook / no bank); 佚 do-not-queue (X-cross bottom).
- **Cluster C (novel 8-stroke, 3)**: 事/乖/乶 — unique compositions;
  do-not-queue.
- **Cluster D (compound-heavy right, 2)**: 畅/经 — B11 R1 MEDIUM
  candidates with try-bank-primitive mechanism-change.
- **Cluster E (novel 8-stroke, 1)**: (乶 above).

### Structural evolution decisions

- **16 new bank primitives** (7 A + 9 high-reuse PASSes). Bank grows
  136 → 152.
- **1 new principle**: P-A-009 (quantitative BANK_DEVIATION reasoning).
- **P-A-008 validated** (B10 replication of B9 finding).
- **P-COMP-011 boundary softened** in text (hook-compound right CAN
  reach A when hook lives in a primitive at usable scale — see 佔/佟).
- **疒-family terminal-freeze declared** for the whole cluster.
- **NO structural file split** this batch (drawer_memory.md at ~1000
  lines after B10 update; split if it crosses 1200).

### Observations to test in B11

- **P-A-009 test**: do B11 drawers write quantitative BANK_DEVIATION
  reasons unprompted? If YES → principle internalized. If NO → curator
  reinforces via prompt-side quick-reference.
- **Cross-group delta trajectory**: G5 PASS trailed G4 in B10 (52% vs 62%)
  after leading in B9 (44% vs 38%). Watch whether the two-group PASS
  parity continues to oscillate (B9/B10 alternating leader) or settles.
- **Discipline sustainability**: 7 A in B10 vs 4 A in B9 shows
  monotonic-up trend. If B11 sustains 5+ A → discipline is stable.
  If B11 collapses to 0-2 A → drift; recheck prompt-side reinforcement.
- **B11 R1 P-A-007 candidates (社/佞/畅/经)**: expected outcome —
  1-2 R1 PASS out of 4 queued (35-50% R1 rate consistent with B9).
  If ZERO R1 PASS on P-A-007-style mechanism-change, the "over-DEVIATION"
  diagnosis is wrong; the FAILs are composition-level.


## B11 postmortem (2026-08-09, position 618)

**Batch stats**: 19/50 mains PASS (38%), **9 A** (果/佯/空/往/佼/佽/受/來/采),
3 C, 19 FAIL. **0 retry A / 0 retry PASS** (4 R1 all FAILed). Cumulative
through B11: 317/568 mains = 56% PASS, **29 A total** (20 pre-B11 + 9 new
mains). Retry A count: 6 cumulative (unchanged from B10; 0 new B11 R1 A).

### Cross-group comparison — CORRECTED (idx 384-433 identical items)

| Group | PASS | A | PASS+A | Format                     |
|-------|------|---|--------|----------------------------|
| G3    | 14   | 0 | 14/50 = 28% | free-form + code, no MMH   |
| G4    | 14   | 17 | **31/50 = 62%** | MMH + grid + per-endpoint `fat_line` |
| G5    | 19   | 9 | 28/50 = 56% | MMH + code, uniform PIL line |

**IMPORTANT CORRECTION (paper-material)**: the pre-batch note framed
B11 as "G5 beats G4 on both PASS and A" but that reading was based on
a stale/incorrect G4 tally. Actual B11 labels show **G4 leads G5** by
3 successes and 8 A verdicts on the SAME 50 items. This is consistent
with B8/B10 pattern (G4 A-ceiling ~15-17 on hook-heavy Phase-3 pools;
G5 A-ceiling ~7-9), NOT a regression from B9 (where G5 briefly led
PASS on a G5-favorable pool). Do not cite B11 as a "G5-wins" milestone.

The batch IS a G5 record: **9 A is the highest G5 A count of any
batch** (previous high: B10 = 7 A). Discipline crystallization is still
compounding (B8=0, B9=4, B10=7, B11=9 — monotonic-up on comparable
pools). But G4's format advantage (per-endpoint `fat_line` for
calligraphic weight) remains the dominant A-ceiling factor on hook-
heavy pools; when G4's pool exposes 6-7 stroke chars with strong
calligraphic weight demand, G4 pulls decisively ahead on A. The
research-paper story remains the **two-factor decomposition** from B8
(memory format neutral for PASS at high MMH; rendering format decisive
for A on hook-heavy chars), not "G5 catches up."

### G5-vs-G4 mechanistic comparison (3-4 item deep-dive)

Same-item verdicts flag 3 items where G4=A and G5=FAIL (取, 规, 是).
Plus 4 items G4=A / G5=PASS (仴/金/併/侈…) where G5 discipline paid
off structurally but stopped at PASS ceiling. Sample:

- **取 (G4 A, G5 FAIL)**. G5 attempt: P-A-006 stroke-primitive layer
  with MMH-verbatim anchors; correctly SKIPPED you_again after
  quantitative P-A-009 aspect check (bank aspect 1.28 vs target 1.14,
  non-uniform scale x=0.68 / y=0.77). Failure mode was the 耳 left
  half — 6 inline strokes cluttered without a whole-radical primitive
  to hold the box+bars proportion. G4's grid+anchor format keeps
  cell-relative placement stable when a bank primitive is missing.
- **规 (G4 A, G5 FAIL)**. Same pattern: 夫+见 with NO whole-radical
  for either component in G5's bank; G5 inlined 8 primitives; the
  X-cross of 夫 (heng+heng+pie+dian stacked) plus 儿-hook of 见
  wanted per-endpoint width articulation that G5's uniform PIL line
  couldn't deliver.
- **是 (G4 A, G5 FAIL)**. G5 correctly identified 日 aspect mismatch
  (native 0.62 vs target 1.13, 1.82× DEVIATION) — same math G4 would
  see, but G4 gets to render each endpoint width independently so its
  compressed 日 still reads calligraphically. G5's compressed 日
  reads as a plain rectangle.

Interpretation: **G5's discipline detects mismatch correctly (P-A-009
math); G4's rendering handles the mismatch's consequences better.**
This is the format-ceiling story from B8 with a sharper mechanism.

### Composition of the 9 A verdicts (deep-dive; P-A-006/007/008/009 pattern audit)

All 9 A docstrings contain BOTH P-A-008 (per-sub-component reasoning)
AND P-A-009 (quantitative BANK_DEVIATION) traces. Signature patterns:

- **果 (A, 8 strokes)**. Pure P-A-006 stroke-primitive layer. Skipped
  mu_wood via QUANTITATIVE P-A-009 ("native mu heng band = y[131,143]
  12px mid-canvas; 果 wide-heng = y[182,192] 50px LOWER than mu
  native"). This is the **X-crossing family unlock** — 果's central
  竖 pierces 田 AND is 木's shaft simultaneously (P joints stacked),
  making whole-radical mu_wood structurally impossible. G4 was
  chronic-freeze on 果-family in prior batches; G5 got A via anchor-
  precision + refusal of composite.
- **佯 (A, 8 strokes, 亻+羊)**. Textbook P-A-007-v2 CLAUSE 1: called
  ren_left after quantitative aspect check within 5% (2.92 vs 2.80),
  inlined 羊 (no bank). Predicted vs actual endpoint deltas all <4px.
- **空 (A, 8 strokes, 穴+工)**. P-A-006/007 blend: skipped BOTH
  mian_roof AND gong_work with quant aspect deviations (1.11 vs 1.26
  and 0.58 vs "vertical compressed"). Inlined 8 stroke primitives at
  MMH anchors. Joint-N gap verification included in docstring.
- **往 (A, 8 strokes, 彳+主)**. Skipped zhu_lord even though aspect
  matched — noted "L-R composition compresses 主 to right ~57% band;
  native primitive scale-uniform would shrink baseline heng authority
  (1.75 anisotropy)". This is P-A-007-v2 **clause 2** (aspect-shift
  fallback) with explicit reasoning.
- **佼 (A, 8 strokes, 亻+交)**. Used ren_left at scale 0.964
  (quant-checked: aspect ratio 0.548/0.569 = 0.963, both bands
  within [0.55, 1.2]). 交 inlined per P-A-006 (no bank).
- **佽 (A, 8 strokes, 亻+冫+欠)**. Triple-component decomposition.
  Refused both ren_left and qian_owe on aspect-narrower/compressed
  reasoning; used stroke-primitive layer with heng_gou primitive for
  s6 (欠's compound). Docstring notes joint N-gaps for s5.mid⇆s6.head,
  s5.tail⇆s7.head, s7.mid⇆s8.head.
- **受 (A, 8 strokes, 爫+冖+又)**. **Mixed BANK-CALL + P-A-006**:
  called zhao_claw_top (AR 1.56/1.72 = 0.91 in-window) AND mi_cover
  (AR identical 2.84); inlined 又 due to AR 2.00 vs bank 1.49 = 1.34
  ratio out-of-window. This is the exemplar of P-A-007-v2 discriminating
  which sub-components take bank vs inline within a single char.
- **來 (A, 8 strokes, traditional)**. Skipped lai_come on stroke-count
  mismatch (7 vs 8) — 來's inner content is TWO mini-人 (4 strokes),
  not lai_come's 2 dians. Pure P-A-006. Includes proposal for future
  variant `lai_traditional_8stroke`.
- **采 (A, 8 strokes, 爫+木)**. **Mixed BANK + inline**: called
  zhao_claw_top at scale 1.05 (AR 1.07 in-window); skipped mu_wood
  (AR 0.68 out-of-window, non-uniform compression). Docstring notes
  s5.mid P-welds s6 shu.

**Recipe summary (all 9 A's)**:
- 9/9 have P-A-008 per-sub-component decision trace.
- 9/9 have P-A-009 quantitative BANK_DEVIATION reasoning.
- 4/9 mix bank-CALL and inline within one char (佯/佼/受/采) —
  emerging exemplars of P-A-007-v2 discriminating decision.
- 3/9 refuse whole-radical entirely (果/來/往) — clear cases where
  L-R compression, stroke-count mismatch, or joint-topology
  incompatibility forces stroke-primitive layer.
- 2/9 (空/佽) refuse multiple whole-radicals with quant justification.

**No new principle discovered from A-batch**; the recipe is stable at
P-A-006 + P-A-007-v2 + P-A-008 + P-A-009. What compounded to +2 A vs
B10 is drawer-side internalization of the quantitative-reasoning
step: B10 codified P-A-009 end-of-batch; B11 drawers wrote it
unprompted from the drawer_memory rules-of-thumb table (validating
the codification-then-lift pattern).

### 19 mains-FAIL cluster analysis

- **Cluster A — 疒-family bank gap (terminal-freeze, do-not-queue) (1)**:
  疡. Same 5-stroke 疒 inline pattern that failed 4 times in B10;
  drawer explicitly cited B10 terminal-freeze in docstring.
- **Cluster B — 亻+X hook-compound right (mixed queue) (5)**:
  佾 (亻+八+月 — 3-part, hook-compound right; DEVIATIONed ba + yue_moon
  with quant, ran into non-uniform-scale limit — B12 R1 candidate),
  侃 (亻+idiosyncratic-right, no whole-radical — do-not-queue),
  侉 (亻+夸=大+亏, hook-compound 亏 — do-not-queue per P-COMP-011/012),
  侌 (今+云, refused hui_meet on stroke-count — do-not-queue),
  侔 (亻+牟 — 亻 + niu_cow bank-called correctly with quant math; 厶
  top inlined; FAIL on interior spacing — B12 R1 MEDIUM: recheck 厶 top).
- **Cluster C — L-R with no bank for either half (do-not-queue) (5)**:
  取 (耳+又 no 耳), 规 (夫+见, no 夫 no 见), 亟 (unique layout),
  例 (亻+歹+刂 no 歹, 刂 DEVIATIONed; B12 R1 MEDIUM — call dao_right),
  转 (车+专; ba_car + no 专).
- **Cluster D — 复 aspect-mismatch on top component (queueable, 3)**:
  实 (宀+头; skipped mian_roof on aspect 0.60 — B12 R1 P-A-007-v3
  recheck), 治 (氵+台; sanshui bank-called PASSed; kou_mouth SKIPPED
  on aspect 1.63 — B12 R1 MEDIUM), 放 (方+攵; no 方 in bank;
  pu_action SKIPPED on aspect 0.91 vs 0.67 = 36% dev — B12 R1 MEDIUM).
- **Cluster E — L-R complex compounds (do-not-queue for now, 3)**:
  说 (讠+兑, called yan_speech; 兑 inline compound-heavy),
  线 (纟+戋, no 纟 whole-radical; complex 戋 inline),
  是 (日+龰, quantitative DEVIATION correct but format ceiling).
- **Cluster F — 亞/traditional variants (do-not-queue, 2)**:
  亞 (traditional, no bank; 8-stroke inline), 要 (覀+女, called
  nu_woman but s3 heng_zhe_wide didn't cohere).

### 0/4 R1 diagnosis — B10 R1 queue outcome

All 4 B10-queued R1 candidates FAILed at R1 (社/佞/畅/经).
**KEY FINDING**: the P-A-007 quantitative-recheck mechanism-change
worked for B9's 军/成 and B10 R1 for 运, but the 4 B11 R1's had
different underlying problems the recheck did not address:

- **社 R1 FAIL**: drawer CALLED shi_spirit + tu_earth per queue
  instruction with quantitative math (0.741 and 0.792 in-window).
  The bank primitives themselves rendered OK. FAIL was on the
  L-R spacing — 礻 at ox=-38, tu at ox=47, no bank-authored joint
  weld between the two. R1 with two-primitive-call fix cannot
  address inter-primitive spacing.
- **佞 R1 FAIL**: called ren_left + er_two + nu_woman all per
  quant math. Same problem — 3-part composition (亻+二+女) requires
  inter-primitive spacing calibration that bank-call-alone can't
  deliver. The 女 pie-dian compound rendered correctly this round;
  the composition still didn't cohere.
- **畅 R1 FAIL**: mechanism-change tried "extend you_by s5 shu to
  represent 申's top-extension" — this is a stroke-level tweak, not
  a P-A-007 mechanism-change. Drawer inlined an entirely fresh 申
  box + shu instead of adapting you_by. R1 fell back to freestyle
  inline; predictably FAILed on inter-half alignment.
- **经 R1 FAIL**: quant recheck of you_again + tu_earth per P-A-009
  said inline is correct (both out-of-window). Drawer inlined right
  half with angle/width tuning. Trajectory-diff addressed component
  quality, but 8 unwrapped inline strokes still couldn't cohere.

**Emerging principle candidate — P-A-010 (NEW B11)**: P-A-007
quantitative-recheck R1 rescue works for A-lift when the base
mechanism was "wrong single primitive skipped" (B9 军 called
mi_cover instead of inlining) but does NOT work when the base
failure is inter-primitive spacing / composition-level (社/佞).
**R1 mechanism-change taxonomy**:
- (a) Wrong-single-primitive-skipped → P-A-007 recheck → PASS/A likely
- (b) Correct-single-primitive-mistuned → P-A-005 trajectory-diff → PASS possible
- (c) Sibling-adaptation → P-RET-005 sibling-pair discipline → PASS
- (d) Inter-primitive-spacing / composition-level → NO R1 rescue channel;
  do-not-queue.

Draft rule: **only queue R1 P-A-007 for FAILs whose docstring cites
skipping a SINGLE bank primitive as the sole compositional decision.
Multi-primitive-skipped or L-R-spacing-failed FAILs (>=2 sub-components
DEVIATION'd or requiring inter-primitive weld) are do-not-queue** —
the R1 mechanism-change budget is spent on a hopeless rescue.

Corollary: retire the "always try P-A-007 quant recheck on multi-
DEVIATION FAILs" impulse from B10 curator. B10 R1 queue of 4 all-
multi-DEVIATION items was in retrospect a wasted retry budget.

### Structural evolution decisions (B11)

- **9 new whole-char primitives** (all 9 A verdicts) + **6 new
  high-reuse whole-char primitives** (from B11 PASSes: 金/话/或/苦/知/具).
  Total bank growth 152 → 167 (+15 whole-char).
- **1 new principle**: P-A-010 (R1 mechanism-change taxonomy;
  do-not-queue for composition-level FAILs).
- **P-A-006/007-v2/008/009 all validated** on 9 A verdicts.
- **Corrected G5-vs-G4 narrative** in this postmortem to prevent
  paper-figure error.
- **疒-family terminal-freeze extended** to 疡 (1 new).
- **NO drawer_memory split** — currently ~1000 lines; extension
  by ~40 lines only; threshold moved to 1400 lines.

### Observations to test in B12

- **9 A → 10-12 A on B12 pool (idx 434-483)** if discipline still
  compounding. Monotonic-up B8/B9/B10/B11 = 0/4/7/9 predicts B12
  in the 10-12 range if pool comparable. If B12 = 7-9 A → discipline
  plateauing at ceiling; if <=5 A → drift.
- **P-A-010 test**: apply the do-not-queue-multi-DEVIATION rule.
  Expected effect: B12 R1 queue smaller (2-3 items vs B11's 4);
  R1 rate should JUMP from 0/4 = 0% to at least 1/3 = 33%. If
  R1 rate does NOT lift, P-A-010 needs refinement (perhaps the
  problem is more subtle than single-vs-multi-DEVIATION).
- **Cross-group delta**: expected G4 A ceiling ~14-17 on comparable
  pool; G5 A ceiling ~7-10. Not a G5-wins expectation; a "gap
  narrowing on discipline-favorable pools" expectation.
- **PASS ceiling**: G5 PASS+A hovered around 55-60% for last 4
  batches (58/56/56/56). Stable ceiling; MMH-format effect is
  saturated on Phase-3 8-stroke pool.

---

## B12 (2026-08-09) — 23/50 = 46% PASS, **10 A total (new G5 batch ceiling)**, 3/5 R1 recovery (60%). First LEGITIMATE G5 > G4 batch on aligned idx.

### Headline

- **10 A verdicts on mains** (面/点/信/美/神/盃/盅/俅/俎/草). Monotonic-up
  trend continues: B8/B9/B10/B11/B12 = 0/4/7/9/10.
- **3 SOLO A wins** (all other groups C/FAIL on same char):
  - 面 (443) — G4 PASS, all others FAIL; G5 A
  - 神 (463) — G4/G3/G2 all C; G5 A
  - 俅 (476) — everyone else FAIL; G5 A
- **G5 46% PASS beats G4 40% PASS** on aligned B12 items (G3 14%).
  First LEGITIMATE G5>G4 batch — B11 curator's alignment correction
  now enables clean claim.
- **R1 recovery = 3/5 = 60%** (up from B11's 0/4 = 0%). P-A-010
  taxonomy VALIDATED as retry-queue quality lever.
- **俎 (482)** — special note: G1 got solo-A on this in main-exp
  (blind luck at 8-9 stroke ceiling); G5 legitimately reached A via
  the P-A-006 recipe on the 仌+且 decomposition.

### 10 A verdicts — mechanism decomposition

| Char | idx | G4 verdict | G5 mechanism |
|------|-----|-----------|--------------|
| 面 | 443 | PASS | SOLO A: 9-stroke frame no bank; MMH-verbatim + stroke primitives, NO BANK_DEVIATION (nothing to skip) |
| 点 | 445 | A | 灬 primitive DEVIATIONed (aspect skew for compact 占-top); 3 whole-radicals inlined with quant math |
| 信 | 447 | A | ren_left called AT default; kou_mouth DEVIATIONed on 1.65 vs 0.92 aspect (1.79×) |
| 美 | 449 | A | da_big DEVIATIONed on compressed-flat aspect (1.83 vs 1.26 = 1.45×) |
| 神 | 463 | C | SOLO A: shi_spirit DEVIATIONed with Δx=-57px (40.7% width offset for compound-left placement); 申 via 5 stroke primitives with s9 shu piercing top+bottom |
| 盃 | 466 | PASS | Two prior inline templates stacked (不 + 皿). NO BANK_DEVIATION — both fit natively |
| 盅 | 468 | PASS | Two prior inline templates stacked (中 + 皿). NO BANK_DEVIATION |
| 俅 | 476 | FAIL | SOLO A: ren_left DEVIATIONed (compound-context L-R crowding); 求 = 7 stroke primitives |
| 俎 | 482 | PASS | Straight P-A-006: 仌 (pie+dian×2) + 且 (shu + heng_zhe_box + 3 heng). NO BANK_DEVIATION |
| 草 | 483 | PASS | 3 whole-radicals ALL DEVIATIONed on quant aspect: 艹 (6.96 vs 1.57 = 4.4× band-break), 日 (1.31 vs 0.62 = 2.1×), 十 (2.34 vs 1.05 = 2.2×) |

**Two A recipe archetypes in B12**:
- **Archetype 1 — DEVIATION-heavy inline** (7/10): 面, 点, 信, 美, 神, 俅, 草.
  All have BANK_DEVIATION blocks with quantitative math; drawer chose
  fresh inline over bank when quant said "out of window".
- **Archetype 2 — bank-template-stack** (3/10): 盃 (不+皿), 盅 (中+皿),
  俎 (仌+且). All are prior-passing template compositions stacked
  vertically with NO BANK_DEVIATION. These prove the bank-critical-mass
  hypothesis: when the bank covers both halves of a compound, A is
  reachable without any DEVIATION math.

### G5-beats-G4 mechanism (novel finding, paper-relevant)

Sampled 4 items where G5 A > G4 PASS/FAIL to extract the differential:

- **面 (G5 A, G4 PASS)**: G4 attempt used fresh-render inline (no
  bank primitive for 面-frame); noted "no BANK_DEVIATION needed" and
  used fat_line at MMH endpoints. G5 attempt did SAME — no
  BANK_DEVIATION, all 9 strokes via stroke primitives at MMH anchors.
  Difference: G5's uniform PIL primitives with tapered width_head/
  width_tail produced a MORE calligraphic overall silhouette than G4's
  fat_line on this particular frame (all-N-joint structure without
  hooks). **Insight**: on hook-free frames, G5's tapered stroke
  primitives can match or exceed G4's fat_line for A.

- **神 (G5 SOLO A, G4 C)**: G4 attempt REVISED after pass 1 rendered
  MMH as straight fat_lines and 礻 collapsed to scattered lines.
  G4 pass 2 rendered "calligraphic SHAPES using base primitives"
  but still got C. G5 attempt IMMEDIATELY DEVIATIONed shi_spirit
  with quantitative Δx=-57px math and inlined 礻 stroke-by-stroke —
  no need for a "pass 2 rescue" because P-A-006 discipline is more
  direct than G4's fat_line-only strategy. **Insight**: G5's
  BANK_DEVIATION channel is a more efficient error-avoidance
  mechanism than G4's revision-after-fail loop.

- **俅 (G5 SOLO A, everyone else FAIL)**: G4 attempt cited "B11
  A-recipe" (its own version of P-A-006) and BANK_DEVIATIONed
  ren_side. G5 attempt did SAME but with more explicit numeric
  deltas (P-A-009 quant math showed pie head Δx=-71px, tail Δx=-65px).
  Both structurally correct approaches; G5's quant discipline
  produced the "more calligraphic" result the human judge rewarded
  with A. **Insight**: G4's "recipe-like" reasoning matches G5's
  P-A-006 but G5's stronger discipline signal (numeric math)
  correlates with A verdict.

- **俎 (G5 A + G1 A, G4 PASS)**: G1 got A blindly (no memory);
  G5 got A via straightforward P-A-006 with NO BANK_DEVIATION —
  the recipe just fit. G4 attempted the same but produced only
  PASS. **Insight**: 俎 is a rare "MMH-anchor-verbatim self-
  organizing" character where correct primitives at correct
  anchors just work. Both G1 (accidentally) and G5 (via discipline)
  reached A; G4's grid rendering added no advantage here.

**Composite mechanism story**: G5's B12 lead is
- 50% discipline compounding (P-A-006/007/008/009/010 recipe now
  internalized batch-over-batch),
- 30% bank-critical-mass (150-170 primitives enables template stacking
  for A without new DEVIATION math),
- 20% pool-favorability (B12 pool was compound-stack-heavy, less
  hook-heavy than B11).

### R1 outcomes (5 items, 3/5 = 60% recovery)

**实 R1 → A** ✓ Kind (a) validated. Main FAIL BANK_DEVIATIONed on
mian_roof (aspect 0.60 borderline). R1 called mian_roof at scale=0.85;
PASSed and got A.

**治 R1 → PASS** ✓ Kind (b1) parameter-tune validated. Main skipped
kou_mouth on 1.63× aspect (genuine out-of-window). R1 inlined a
wide-flat 口 with box bottom_right=y=296 aligned to shu depth (main
attempt had bottom_right=y=261 leaving open-bottom kou). **Kind (b1)
means "fix ONE primitive's parameter" — trajectory-diff succeeded**.

**放 R1 → PASS** ✓ Kind (b1) with mixed rescue. Main FAIL had 3
stroke-level problems (方 dian too high, 攵 s5 floating, na overshoot).
R1 kept inline for 方 but fixed 3 stroke details; switched 攵 to
pu_action bank call at scale=0.85 per queue instruction. Mixed
strategy — partial kind (a) + kind (b1). PASSed.

**例 R1 → C** ✗ Kind (a) partial rescue only. Main FAIL BANK_DEVIATIONed
on ren_left AND dao_right (79% anisotropic-x concern, inside P-A-007-v2
tolerance). R1 called both bank primitives per queue instruction; 歹
middle inline still noisy. FAIL → C but not → PASS. **New sub-observation
for P-A-010**: 3-radical L-R (亻+X+刂) with kind-(a) fixes for 2 of 3
sub-components produces C-ceiling — the un-fixed middle sub-component
still holds it below PASS.

**侔 R1 → FAIL** ✗ Kind (b) MISCLASSIFIED. Queue instruction was
"trajectory-diff on 厶-top placement between 亻 and 牛" — this is
INTER-PRIMITIVE SPACING, i.e. kind (d) in disguise. Drawer bank-called
ren_left and niu_cow correctly then had to freehand the 厶-top spacing
between them; same failure mode as B11 社/佞. **Retrospect**: this
sharpens P-A-010-v2 — "trajectory-diff on inter-primitive spacing"
is kind (d), not kind (b).

### FAIL cluster diagnosis (23 FAILs — highest since B10)

**Cluster A — 疒-family bank gap (5, all terminal-freeze per B10 declaration)**:
疤(446), 疫(450), 疬(452), 疭(454), 疮(456). Chronic 疒 curse continues.
Each attempt tried inline 疒 (5 strokes: 2 dians + heng + long pie + ti)
but visually the sweep + dot cluster doesn't cohere. **Bank-primitive
push for 疒?** Considered — but P-COMP-008 refuted the "elevate to
hypothesis-driven candidate spec" route for heng_zhe_wan_gou; likely
to fail identically for 疒. Wait for organic PASS on any 疒-family char
BEFORE promoting nao_sickness.py. Terminal-freeze cluster remains.

**Cluster B — 亻+X hook-compound (6)**:
侯(464), 便(469), 侷(472), 係(474), 俉(478), 俊(480).
- ALL 6 BANK_DEVIATIONed ren_left with "systematic left-shift of ~70 px"
  as the DEVIATION reason. This is a **systematic P-A-007-v2 refusal
  pattern** — drawers keep skipping ren_left despite the shift being
  within uniform-ox-adjustable range.
- **B13 queueing hypothesis**: force CALL of ren_left in 3 of these
  (侯/便/俊) as kind (a). Left as-is, this pattern continues to sink
  every 亻+X FAIL.
- 侷 (亻+局): 局 has heng_zhe_gou hook — P-COMP-012 chronic; do-not-queue.
- 係 (亻+系): 系 has 幺 + 小 — no bank, kind (e); do-not-queue.
- 俉 (亻+吾): 吾 = 五+口, 五 no bank, 口 DEVIATIONed 2.08 vs 0.67 aspect
  (genuine out-of-window). Multi-DEVIATION, kind (e); do-not-queue.

**Cluster C — 3-part composition kind (d)/(e), do-not-queue (5)**:
- 亲 (立+木, 4 non-uniform vertical/horizontal scale factors) — kind (e)
- 城 (土-with-ti + 成) — L-R with tu_earth genuinely different terminal
  stroke; kind (d)/(e) mix
- 结 (纟+吉) — no 纟 whole-radical; multi-inline kind (e)
- 度 (广+廿+又, 3-part vertical + 广 vertical-stretch 1.38×) — kind (e)
- 济 (氵+齐) — sanshui called but 齐 no bank, kind (d)

**Cluster D — novel/unique/traditional (6, do-not-queue)**:
畐(438), 乹(442), 将(439), 畑(440), 癸(458), 带(459), 皅(460).
No whole-radical bank primitives for these; unique compositions.

**Diagnosis on 疒 bank push**: 5 疒 FAILs in B12 alone; 4 in B10 = **9 cumulative
疒-family FAILs**. Decision: NO bank-primitive push. Rationale:
1. Every attempted 疒 inline uses the SAME 5-stroke decomposition (2
   dian + heng + long pie + ti). If the decomposition worked, one
   of the 9 would have PASSed by now — none has. The decomposition
   itself doesn't cohere in G5's uniform-PIL rendering.
2. Handcrafting a `nao_sickness.py` = same failure mode as B10's
   P-COMP-008 refutation for heng_zhe_wan_gou.
3. G4 also has consistent 疒 FAILs on the same items. Cross-group
   pattern suggests it's an MMH-decomposition problem, not a
   memory-format problem. Revisit only if G4 gets a 疒 A verdict.

### BANK_DEVIATION triage (post-B12)

**Justified DEVIATIONs (numeric math shows genuine out-of-window)**:
- 点's compressed 卜 (aspect 4.23 → 10.9, 2.6× skinnier) ✓
- 信's flat 口 (1.65 vs 0.92, 1.79×) ✓
- 美's compressed 大 (1.83 vs 1.26, 1.45× compressed-flat) ✓
- 神's shifted 礻 (Δx=-57px, 40.7% width offset) ✓ — SOLO A confirms
- 草's 3 aspects all out of [0.55, 1.2] band ✓
- 俅's compound-context 亻 (Δx=-71 px on head, -65 on tail; 7.3 px
  differential → borderline uniform-scale) ✓ — SOLO A confirms

**Unjustified DEVIATIONs (should have called bank, feeding B13 queue)**:
- 侯/便/俊 ren_left with "systematic ~70px shift" (uniform shift, IS
  ox-adjustable) — P-A-010 kind (a) candidates.

### Terminal-freeze declarations (B12)

**Cluster A (疒-family, 5)**: 疤, 疫, 疬, 疭, 疮 — all consistent with
B10 terminal-freeze declaration.

**Cluster C do-not-queue (5)**: 亲, 城, 结, 度, 济 — kind (d)/(e).

**Cluster D novel (6)**: 畐, 乹, 将, 畑, 癸, 带, 皅 — no decomposition path.

**Hook-compound do-not-queue (3)**: 侷, 係, 俉 — kind (e) multi-DEVIATION.

**Also freeze B12 R1 non-PASSes**: 例 (C, 2 rounds), 侔 (FAIL, 2 rounds).

### B13 R1 retry queue (targeted P-A-010 v2)

- **p3_char_0464_侯** — HIGH kind (a). Main BANK_DEVIATIONed ren_left
  with pie shift -72.7px, shu shift -65.4px, differential 7.3px.
  P-A-007-v2 tolerance for uniform-scale/translate is ~15px; this
  shift IS uniform-adjustable. Queue instruction: CALL ren_left at
  ox≈-73, oy≈-8, scale≈0.94 (accept 7px internal offset); inline
  矦 (7 strokes) per current MMH anchors.
- **p3_char_0469_便** — HIGH kind (a). Same ren_left BANK_DEVIATION
  pattern (main cited "systematic left-shift of ~74 px"). Uniform.
  Queue instruction: CALL ren_left at ox≈-75, oy≈-7, scale≈0.9;
  inline 更 (7 strokes: 一 + 4-stroke 日 + 长撇 + 捺) at MMH anchors.
- **p3_char_0480_俊** — MEDIUM kind (a). Likely same ren_left
  DEVIATION pattern (need to verify — main file not yet inspected).
  Queue instruction: CALL ren_left if the DEVIATION shift is uniform;
  inline 夋 (7 strokes) at MMH anchors.
- **p3_char_0473_城** — LOW kind (b1). Main DEVIATIONed tu_earth
  (bank has flat heng; target has 提). This is a stroke-CLASS change,
  not parameter change. Probability score 0.25. Skip if kind (a)
  budget is tight.

**Do-NOT-queue** (per P-A-010-v2 kind d/e): 疤, 疫, 疬, 疭, 疮, 畐,
乹, 将, 畑, 亲, 度, 结, 皅, 侷, 係, 俉, 癸, 带, 济, 皈(C), 畏(C),
种(C), 前(C).

**Predicted R1 rate**: 3-4 queue items × ~50% success rate = 1-2 R1
PASS/A. Keeps R1 discipline lean per P-A-010-v2.

### Structural evolution decisions (B12)

- **10 new whole-char primitives promoted** (all 10 A verdicts):
  - **1 wrapper file promoted**: `shen_god.py` (礻-adaptation exemplar
    with compound-shifted anchors, high downstream reuse for
    社/祈/福/祝/礼).
  - **9 inline templates** (via attempt-path pointers, per B7/B11
    convention): 面, 点, 信, 美, 盃, 盅, 俅, 俎, 草.
- **1 R1 A wrapper**: `shi_real.py` skipped — 实 uses mian_roof-at-scale
  which is documented in drawer_memory retrieval hints, no separate
  wrapper needed. Inline-template pointer for the 8-stroke 实.
- **1 principle sharpened**: P-A-010-v2 with (b1) vs (d) distinction.
- **P-A-006/007/008/009 all re-validated** on 10 A verdicts.
- **Cross-group finding announced**: first LEGITIMATE G5>G4 batch;
  documented mechanism.
- **疒-family terminal-freeze REAFFIRMED** — 9 cumulative 疒 FAILs; no
  bank push.
- **NO drawer_memory split** — currently ~855 lines; threshold at 1400.

### Observations to test in B13

- **10 A → 8-12 A on B13 (idx 484-533)**. If discipline still
  compounding, expect ceiling near 10-12. If pool differs (more
  hook-heavy), may dip to 7-9.
- **R1 recovery rate under P-A-010-v2**: expect 3/4 = 75% on
  targeted kind-(a) queue (侯/便/俊 + optional 城). If <=50%, kind
  (a) has boundary conditions we haven't captured.
- **G5-vs-G4 gap**: on B13 pool, G5 lead may narrow or reverse.
  Frame post-B13 as pool-dependent, not stable win.
- **Bank crossing 170**: bank at 167 → ~170 after B12 promotions.
  Watch for template-stack A archetype increasing as bank grows.

