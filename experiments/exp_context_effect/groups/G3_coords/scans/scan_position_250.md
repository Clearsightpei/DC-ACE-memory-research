# Errata Scan — G3 (coord-bank) — Curriculum Position 250

Scan performed at position 250 (end of B4 / start of B5). This is the
**third scan under v7 self-evolution** (see `evolution.md` position 250
third-pass entry). Upcoming 50 items span 251–300 (all Phase-3
characters at 3–4 画): 屮 马 巛 工 川 义 幺 乡 廾 弋 不 丹 为 乌 以
予 中 亓 天 亢 方 仂 日 仃 无 仄 分 仇 心 仉 见 仌 公 仑 从 仓 气
內 五 兮 文 円 长 冈 太 龶 切 冗 内 冘.

## Batch context — the alignment moment

B4 retry pass rate = **1/8 (12.5%)** — a single graduate (082_子)
followed the "inline all three strokes with matched taper" errata
recipe. **All 8 B4 retry attempts, including the one PASS, imported
zero composition helpers** (`kiss_apex`, `pie_point`,
`mirror_dian_pair`). This confirms B3's suspicion, escalated in
`evolution.md` position 250: the **retry-path memory retrieval is
broken**, not just the content. Main-attempt drawers use helpers at
~24% import rate; retry-attempt drawers were 0/8 in B2, 7/13 in B3
with 0 PASSes, 0/8 in B4.

Curator response for B5 (see memory_index v7.3):
1. **RETRY-TIME CHECKLIST** injected as the FIRST section of
   `memory_index.md`. Requires every retry `generated.py` to open
   with three ANSWER comments (Q1 errata / Q2 form_catalog / Q3
   helpers) before any code. This is the only observable signal that
   memory was consulted.
2. **Char↔radical cross-transfer table** documenting the B4 pattern
   where 兀/门/子 PASSed as chars while their radicals stayed in
   errata with different (worse) recipes. Back-porting the char
   recipe to the radical is now a first-class retry lever.

## The alignment moment

Position 250 is the FIRST scan where BOTH:
- **(a) content** (kiss_apex / pie_point / mirror_dian_pair, in the
  bank since scan_200) AND
- **(b) retrieval** (RETRY-TIME CHECKLIST, this scan)

are simultaneously active. Additionally:
- **The chronic-fail X-crossing family cooldown lifts** at pos 250
  (last retried pos 200 → eligible pos 250): 015_刀, 021_丷, 025_力,
  028_人, 030_入, 046_大, 077_忄, 083_丬, 088_长, 098_火, 100_见,
  113_犬, 117_手.
- **The upcoming window has X-crossing chars** (义/太/从/公) that will
  need the SAME primitives, giving a strong (a) prospective bonus.

If this scan's retry pass rate is still ~0%, the diagnosis is no
longer "retrieval gap" — it's "the helpers themselves are wrong for
these shape families" and the direction needs deeper introspection.

## Terminal-freeze re-examination

Per `errata.md` B4 retry-priority notes, 大/人/入/丷/忄/己/㔾/犭 all
sit at retry_n=4 — "ALREADY OVER the retry cap. Should be
terminal-frozen unless **explicit new lever emerges**."

The RETRY-TIME CHECKLIST + prior composition helpers, combined, ARE
an explicit new lever specifically for X-crossing/mirror-dot items:
neither existed in B3 and neither was enforced in B4. Per
`shared_rules.md` §"Terminal freeze": the 1000-char sweep hasn't
ended, and the shared_rules only mandate freeze at sweep-end. The
retry_n=3/4 warnings in errata are curator-imposed caution, not hard
rules.

**Decision**: unfreeze the X-crossing / mirror-dot subset where the
new lever demonstrably applies. Retry them with an explicit rationale
in the retry_log (`retry_n_prev → retry_n_new`) and mark them as
"final chance before hard-freeze" so if B5 also fails 0%, the next
curator freezes them without further deliberation.

## Cooldown status @ position 250

- **13 X-crossing/mirror-dot items just cooldown-lifted** (last retry
  pos 200): 015_刀, 021_丷, 025_力, 028_人, 030_入, 046_大, 077_忄,
  083_丬, 088_长, 098_火, 100_见, 113_犬, 117_手. **Now eligible.**
- **8 B4 retries just cooldown-locked** (last retry pos 250):
  047_飞, 059_门, 061_女, 074_兀, 080_尢, 081_夂, 084_夊 —
  **BLOCKED** until pos 300. (082_子 GRADUATED, removed.)
- **retry_n=2 items last retried scan_100** (053_己, 038_㔾, 062_犭):
  eligible; still no direct helper for their curl-hook family.
- **retry_n=0 items** (B1/B2/B3 fails never retried) — always eligible.

## Prospective (a) map — errata × 251–300

### Radical-in-errata → same-char slot in upcoming window

| errata item | curriculum slot in 251–300 | notes |
|---|---|---|
| 040 屮 | pos 251 屮 | direct identity-alias candidate |
| 058 马 | pos 252 马 | direct |
| 042 巛 | pos 253 巛 | direct |
| 078 幺 | pos 257 幺 | direct |
| 079 弋 | pos 260 弋 | direct |
| 093 方 | pos 271 方 | direct |
| 135 无 | pos 275 无 | direct |
| 100 见 | pos 281 见 | direct + cooldown-lifted |
| 111 气 | pos 287 气 | direct |
| 088 长 | pos 293 长 | direct + cooldown-lifted |

### X-crossing / mirror-dot family → upcoming composition slots

| errata item | upcoming composition | (a) strength |
|---|---|---|
| 028 人 | pos 285 从 (人+人), pos 256 义 (乂-family), pos 295 太 (大+dot), pos 283 公 (八 top) | **very strong** — 3+ direct downstream |
| 030 入 | pos 256 义 (X-crossing family), pos 285 从 | strong |
| 046 大 | pos 295 太 (大 + dot), pos 256 义 | **very strong** |
| 015 刀 | pos 297 切 (七 + 刂/刀 body — has 刀-adjacent hook) | moderate |
| 025 力 | none direct in 251–300 | weak |
| 098 火 | (火 not in this window; 灬 already handled) | weak — deprioritise |
| 113 犬 | none direct | weak |
| 117 手 | none direct (手 was pos 213 — passed window) | weak |
| 021 丷 | pos 283 公 (八 top = 丷 mirror), pos 290 兮 (八 top) | strong |
| 077 忄 | none direct in 251–300 | weak |
| 083 丬 | none direct | weak |
| 100 见 | pos 281 见 (identity alias) | **direct** |
| 088 长 | pos 293 长 (identity alias) | **direct** |

### Non-errata upcoming characters already bank-covered or alias-only

- 254 工, 255 川, 254 工, 259 廾, 268 亓, 269 天 (== 大 + 一, X-family),
  273 日 (ri.py already bank), 279 心 (xin.py already bank), 291 文
  (wen.py already bank), 292 円 (囗 bank + 一), 294 冈, 296 龶.
- 273 日, 279 心, 291 文 are alias-only — no retry needed.

## Retrospective (b) map — active memory × errata

| item | failure mode (errata) | new lever this scan | (b) |
|---|---|---|---|
| 028 人 | pie+na don't kiss at apex (SAME across all retries) | kiss_apex(u=0.0) + RETRY-TIME CHECKLIST forcing helper import | **very strong** |
| 030 入 | same as 人 (u=0.3) | kiss_apex(u=0.3) + CHECKLIST | **very strong** |
| 046 大 | pie+na+heng midpoint miss (per B4 char fail note) | new err-idea "compute heng-midpoint pixel first, then kiss_apex u=0.5" + CHECKLIST | **strong** |
| 021 丷 | mirror-dot bow sign wrong on retry | mirror_dian_pair + CHECKLIST | **strong** |
| 077 忄 | mirror + shaft dominates | mirror_dian_pair + CHECKLIST | **strong** |
| 100 见 | box aspect + descender weld | jiong-inline recipe + form_catalog "never force kou" + CHECKLIST | **strong** |
| 113 犬 | X-crossing + dian offset | kiss_apex + mirror_dian_pair for dot placement + CHECKLIST | strong |
| 098 火 | 人-body + 2 side dots | kiss_apex(u=0.0) + mirror_dian_pair + CHECKLIST | strong |
| 088 长 | swept 捺 + composition | variant_na bow_perp≈+12 + CHECKLIST | moderate–strong |
| 117 手 | shou_pang + top pie | variant_pie prepend + CHECKLIST | moderate |
| 015 刀 | hook-shaft weld | pie_point/bezier_point + CHECKLIST | moderate |
| 083 丬 | compact dot spread | mirror_dian_pair(spread ≈ 15) + CHECKLIST | moderate |
| 025 力 | heng_zhe_gou + crossing 撇 | pie_point + CHECKLIST | moderate |
| — | — | — | — |
| 040 屮 | (no strong new lever, but char slot 251 makes (a) direct) | inline 竖 + 山-arm + 竖 with matched thin widths per P12 | (a)-only |
| 058 马 | (5-stroke) | inline + P12 thin widths | (a)-only |
| 093 方 | 横折钩 + 撇 misaligned | pie_point for pie→box weld | (a)+(b) moderate |
| 135 无 | top-heng + 撇 + 竖弯钩 | shu_wan_gou primitive + variant_pie | (a)+(b) moderate |
| 078 幺 | fold angles wrong | none direct | (a)-only weak |
| 079 弋 | 斜钩 belly lost | variant_na with strong perp bow | (a)+(b) moderate |
| 111 气 | 横撇 + inner curl | none direct | (a)-only weak |

## Decisions

### RETRY (17)

Position 250 is the **content+retrieval alignment moment**. The X-crossing
and mirror-dot family have BOTH the exact helpers designed for them AND
the RETRY-TIME CHECKLIST forcing consultation. The upcoming window will
demand these primitives regardless (义/太/从/公/见/长). Retrying the
family now is the only way to convert stagnant errata into bank recipes
that upcoming main attempts can reuse.

We aim ~40% eligible-retry rate — higher than scan_200's 19% because
the alignment is real, but well short of maximalism to avoid re-flooding
the retry channel with under-diagnosed items.

Priority tiers:

**Tier 1 — X-crossing family (both a-strong AND b-very-strong)**:
1. **p2_radical_028_人** — retry_n=4→5. **FINAL** before hard-freeze.
   Recipe: `kiss_apex(pie_head, pie_tail, na_tail, u_pie=0.0)` per
   form_catalog X-crossing worked example. Prereq for 从/义 downstream.
2. **p2_radical_030_入** — retry_n=4→5. **FINAL**. Same recipe with
   u_pie=0.3. Prereq for 义/从.
3. **p2_radical_046_大** — retry_n=4→5. **FINAL**. Recipe: compute
   heng-midpoint pixel FIRST, then kiss_apex u=0.5 with pie_head at
   that pixel. Prereq for 太 (pos 295), 天 (pos 269).
4. **p2_radical_098_火** — retry_n=2→3. Recipe: kiss_apex(u=0.0) for
   人-body + mirror_dian_pair for 2 side dots. (a) weak this window but
   (b) very strong — first non-cooldown test of both helpers combined.

**Tier 2 — Mirror-dot family (b-strong; a directly matches 公/兮)**:
5. **p2_radical_021_丷** — retry_n=4→5. **FINAL**. mirror_dian_pair.
   Prereq for 283 公 (八-top == 丷 mirror), 290 兮.
6. **p2_radical_077_忄** — retry_n=4→5. **FINAL**. mirror_dian_pair
   with shu_gou shaft. (a) weak this window but (b) very strong —
   the mirror was the exact motivating case.

**Tier 3 — Char↔radical back-port opportunities (via new cross-transfer
table)**:
7. **p2_radical_100_见** — retry_n=4→5. **FINAL**. Recipe: inline
   box (tall rectangle per form_catalog "never force kou") + 2
   descenders welding to box floor. (a) direct (pos 281 见).
8. **p2_radical_088_长** — retry_n=4→5. **FINAL**. Recipe:
   variant_na with bow_perp≈+12 for the long 捺. (a) direct
   (pos 293 长).

**Tier 4 — Radical-in-errata with direct upcoming char slot ((a)-strong)**:
9. **p2_radical_040_屮** — retry_n=0→1. Direct alias for pos 251 屮.
   Recipe: inline 3 near-vertical strokes at matched thin widths (P12).
10. **p2_radical_058_马** — retry_n=0→1. Direct alias for pos 252 马.
    Inline 5-stroke fresh with matched taper.
11. **p2_radical_093_方** — retry_n=0→1. Direct alias for pos 271 方.
    Recipe: dian + heng + inline 横折钩 with rounded corner + variant_pie
    for the 撇 (per errata fix idea).
12. **p2_radical_135_无** — retry_n=0→1. Direct alias for pos 275 无.
    Recipe: top-heng + variant_pie + shu_wan_gou primitive.
13. **p2_radical_079_弋** — retry_n=0→1. Direct alias for pos 260 弋.
    Recipe: variant_na with strong perp bow + cross dot per errata.

**Tier 5 — Ancillary composition (moderate all around)**:
14. **p2_radical_042_巛** — retry_n=0→1. Direct alias for pos 253 巛.
    3 inline hooked verticals, matched widths.
15. **p2_radical_015_刀** — retry_n=3→4. Cooldown-lifted. Recipe:
    continuous polyline with hook sharing last 5 px of shaft (P9) +
    pie_point for crossing 撇 weld. Prereq for pos 297 切 (七 + 刂
    body includes 刀-family hook).
16. **p2_radical_083_丬** — retry_n=4→5. **FINAL**. Recipe:
    mirror_dian_pair(spread ≈ 15) at compact position + shaft. (b)
    strong; last chance before hard-freeze.
17. **p2_radical_111_气** — retry_n=0→1. Direct alias for pos 287 气.
    Recipe: inline 横撇 top + inner 乙-like sweep as one bezier
    polyline.

### SKIP (rationale summary)

- **8 items just cooldown-locked at pos 250**: 047_飞, 059_门, 061_女,
  074_兀, 080_尢, 081_夂, 084_夊. Eligible again at position 300.
- **Phase-1 hook fails (7 items)** including STALE p1_stroke_26:
  no new lever this scan.
- **retry_n=2 cooldown-expired without new lever** (053_己, 038_㔾,
  062_犭): still no direct helper for their curl-hook family. Skipped
  in scan_150 and scan_200 for the same reason.
- **X-crossing family with weak (a) AND already-tested (b) at retry_n=4**
  (113_犬, 117_手, 025_力): each was tested at pos 200 without helpers.
  Skipping is a calibration call — Tier 1/2 fully saturates the
  X-crossing/mirror-dot test; adding 犬/手/力 would triple-test the
  same helper class with no per-item lever beyond what 人/入/大 already
  cover. If Tier 1 passes, next curator can promote 犬/手/力 with
  higher confidence in scan_300.
- **B3 new fails without direct helper and no upcoming slot**:
  119_水, 120_瓦, 121_尣, 122_王, 123_韦, 125_毋, 127_牙, 132_支,
  133_止, 134_爪. Defer.
- **B4 new fails without a good rescue lever**: 038_匕 char, 042_丬 char,
  044_丸, 047_也, 048_乇, 056_亾, 059_么, 060_卂, 061_与, 065_及,
  068_纟, 073_飞 char, 075_千, 076_孓, 077_习, 079_已, 081_女 char,
  082_尢 char, 083_才. Most either share a family with a Tier 1–4
  item (and will benefit passively) or lack a specific new lever.
- **Radicals in errata with no upcoming char slot** (many): 020_阝,
  032_厶, 035_讠, 036_廴, 041_彳, 050_弓, 055_彑, 056_巾, 078_幺
  (weak (a)-only justification insufficient at this scan's budget),
  096_戈, 097_户, 099_旡, 101_斤, 105_肀, 107_爿, 108_片, 109_攴,
  110_攵, 112_欠, 115_氏, 118_殳, 085_贝, 086_比, 089_车, 091_斗,
  094_风.

## Summary

- **Errata items considered**: ~63 net-active.
- **RETRY**: 17 items.
- **SKIP**: ~46 items (8 of which are cooldown-blocked, not
  discretionary skips).
- **Discretionary retry rate = 17 / (63 − 8) ≈ 31%** — up from
  scan_200's 19% because the alignment (helpers + CHECKLIST +
  X-crossing cooldown-lift + X-crossing char slots) is genuine and
  concentrated; not spread thin across marginal picks.
- **Terminal-freeze warning**: 8 of the 17 are marked **FINAL** —
  retry_n≥3, all at (or past) the curator caution line. If any FAIL
  a second time this cycle, curator at scan_300 should hard-freeze
  them per shared_rules terminal-freeze rule (invoked early by
  curator judgment, since sweep-end is still ~700 items away).

## Retry priority order (Drawer, attempt in this order)

Order chosen so that (i) X-crossing 人 lands FIRST — it's the linchpin
for 入/大/义/从/太; (ii) 兀-family char-recipe back-ports happen after
the direct family test; (iii) alias-radicals last because they don't
depend on helper adoption.

1. **人 (028)** — X-crossing linchpin; kiss_apex(u=0.0).
2. **入 (030)** — kiss_apex(u=0.3), depends on 人 recipe.
3. **大 (046)** — kiss_apex(u=0.5) with pre-computed heng midpoint.
4. **火 (098)** — kiss_apex(u=0.0) + mirror_dian_pair.
5. **丷 (021)** — mirror_dian_pair (pure test).
6. **忄 (077)** — mirror_dian_pair + shu_gou shaft.
7. **见 (100)** — inline tall box + descenders.
8. **长 (088)** — variant_na bow_perp≈+12.
9. **屮 (040)** — inline 3 near-verticals thin.
10. **马 (052)** — inline 5-stroke.
11. **巛 (042)** — inline 3 hooked verticals.
12. **弋 (079)** — variant_na + cross dot.
13. **方 (093)** — dian + heng + inline 横折钩 + variant_pie.
14. **无 (135)** — top-heng + variant_pie + shu_wan_gou.
15. **气 (111)** — inline 横撇 + bezier sweep.
16. **刀 (015)** — continuous polyline + pie_point.
17. **丬 (083)** — mirror_dian_pair compact.

Each drawer prompt MUST include the RETRY-TIME CHECKLIST reminder and
be marked as retry (`__retry_N` suffix in item_id). Curator at
scan_300 will grep for `# Q1`, `# Q2`, `# Q3` header lines to verify
compliance.

## Post-scan validation criterion

If B5 retry pass rate on Tier 1+2 (人, 入, 大, 火, 丷, 忄) < 33%,
the helpers themselves are wrong for the X-crossing / mirror-dot
family (not just retrieval), and evolution.md at scan_300 must
propose a deeper redesign (e.g., per-family default profiles baked
into the helpers, or a "compose then judge" iteration loop within
the drawer). If ≥ 50%, the helpers work when actually consulted, and
the retrieval-forcing CHECKLIST is the causal fix — future memory
evolutions should treat retrieval-discipline as a first-class
concern.

If pass rate on Tier 4 (radical-alias 屮/马/巛/方/无/弋) ≥ 60% —
which is the mode for well-composed identity aliases — the
char↔radical cross-transfer table validates as a routing device.
