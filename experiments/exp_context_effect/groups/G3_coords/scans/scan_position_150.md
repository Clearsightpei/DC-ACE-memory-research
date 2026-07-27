# Errata Scan — G3 (coord-bank) — Curriculum Position 150

Scan performed at position 150 (end of B2 / start of B3). This is the
**first scan under v7 self-evolution** (see `evolution.md` position
150 entry). Upcoming 50 items span 151–200: 17 Phase-2 radical tail
(水 瓦 尣 王 韦 文 毋 心 牙 爻 曰 月 爫 支 止 爪 无) followed by 33
Phase-3 characters at 1–4 画 (一 丨 乙 丶 丿 乚 乛 亅 了 丩 人 丷
十 乂 二 乃 又 乜 儿 亠 几 亻 九 八 力 冂 七 冖 入 冫 厂 凵 刀).

## Batch context

G3 cumulative pass rate through B2 = 49% (worst of 4 groups); B2 alone
= 34% vs G1 no-memory 38%. The v7 evolution response was substantial:
`form_catalog.md` created; `principle_bank.md` split into three files;
TR8 and TR9 retired; **adaptive helpers `variant_pie`,
`variant_na`, `variant_dian`** added to
`success_bank/code/_shared_helpers.py`. These helpers were designed
in direct response to eight identified "signature-restriction" fails
in B2 (077 忄, 083 丬, 088 长, 098 火, 100 见, 112 欠, 113 犬, 117 手)
where the frozen `(ox, oy, scale)` signature could not express the
angle / taper / bow / mirror the target required.

Per the shared-rules "balance not minimalism" guidance and given that
v7 adds a **genuine new retrospective (b) axis** (adaptive helpers +
form_catalog rows), a noticeably more aggressive retry rate than
prior scans (previous: 18% at scan_50, 27% at scan_100) is justified —
but ONLY when the helper specifically maps to the item's failure mode.

## Cooldown status @ position 150

- **retry_n=2 items** last retried at scan_100 (post-B2 attempt logged
  in retry_log.jsonl at position ~100). 50-item cooldown expires at
  position 150 — **eligible now**.
- **retry_n=1 items** (刀 @ position 100 retry-1 FAIL) cooldown expires
  at position 150 — **eligible now**.
- **retry_n=0 items** (all B2 new fails, including the 8
  signature-restriction items) — no cooldown, always eligible.

## Prospective (a) map — errata × 151–200

| errata item | curriculum slot in 151-200 | notes |
|---|---|---|
| 人 (028) | pos 178 (人 as Phase-3 char) | direct prereq |
| 丷 (021) | pos 179 (丷 as Phase-3 char) | direct prereq |
| 入 (030) | pos 184 (入 as Phase-3 char) | direct prereq |
| 力 (025) | pos 185 (力 as Phase-3 char) | direct prereq |
| 刀 (015) | pos 200 (刀 as Phase-3 char) | direct prereq |
| 犭 (062) | — | no direct slot |
| 大 (046) | — | strategic (犬 solved will need it) |
| 己 (053), 㔾 (038), 女 (061) | — | no direct slot |

All other errata items (远-position Phase-2 radicals) have no direct
prospective use in the 151-200 window.

## Retrospective (b) map — v7 helpers × errata

The eight "signature-restriction" B2 fails explicitly called out in
`evolution.md`. Each row lists the specific v7 asset that addresses
the failure mode:

| item | failure mode | v7 asset that fixes | (b) strength |
|---|---|---|---|
| 077 忄 | mirrored dot pair; primitive one-directional | `variant_dian` for BOTH dots, matched widths, swap head/tail (form_catalog explicit note) | **strong** |
| 083 丬 | dian too heavy at compact position | `variant_dian` with w_tail≈5 (form_catalog explicit) | **strong** |
| 088 长 | 捺 sweep needs bow_perp scale can't produce | `variant_na` with bow_perp≈+12 (evolution log named this item) | **strong** |
| 098 火 | apex-kiss + mirrored side dots | fu.py X-crossing template + `variant_dian` for side dots (form_catalog note) | **strong** |
| 100 见 | box aspect wrong (kou 1:1 vs 见 tall) | inline tall-rectangle from ri.py template + hand-placed descenders (form_catalog explicit) | **strong** |
| 112 欠 | heng_gou primitive x-span fixed at 190px | inline heng_gou with configurable span + shared-apex 人-shape (variant_na for the na) | **strong** |
| 113 犬 | 大 + dian, both need inline crossing | fu.py X-crossing template + `variant_dian` for the extra dot | **strong** |
| 117 手 | shou_pang works but added top 撇 changes proportions | shou_pang base + prepend `variant_pie` at top | **strong** |

The 8 retry_n=2 items from B2 also have new (b) coverage where the
new helpers map to their failure mode:

| item | v7 asset | (b) strength |
|---|---|---|
| 021 丷 | variant_dian mirror (same as 077 忄) | strong |
| 028 人 | fu.py X-crossing template + shared apex pixel; form_catalog row exists for 大-family crossing arm | strong |
| 030 入 | same as 人 (head-on-shaft junction; variant_pie + tapered_line inline) | strong |
| 046 大 | form_catalog "大-family crossing arm" row: pie head (0,+25) tail (-95,-110) bow -6, na mirror | strong |
| 053 己 | no direct helper (curl envelope; variants don't cover 弯钩) | weak |
| 038 㔾 | no direct helper (small elbow-hook) | weak |
| 061 女 | no direct helper (crossing 撇+heng; no variant_heng) | weak |
| 062 犭 | variant_dian for the dot; curl still requires fresh bezier | moderate |

## Decisions

### RETRY (13)

| # | item_id | retry_n before → after | (a) | (b) | primary rationale |
|---|---|---|---|---|---|
| 1 | p2_radical_028_人 | 2 → 3 | **strong** (pos 178) | **strong** (fu.py X + form_catalog row) | prereq for 人 char + prereq for 火/欠/犬 retries this scan; v7 helper directly targets apex-kiss failure |
| 2 | p2_radical_030_入 | 2 → 3 | **strong** (pos 184) | **strong** (same as 人) | prereq for 入 char; same helper class |
| 3 | p2_radical_021_丷 | 2 → 3 | **strong** (pos 179) | **strong** (variant_dian mirror) | prereq for 丷 char; the mirrored-dian recipe is exactly form_catalog's documented use |
| 4 | p2_radical_046_大 | 2 → 3 | strategic (needed by 犬 retry) | **strong** (form_catalog 大-family row) | keystone: solves 大 → unlocks 犬 (in this same scan) |
| 5 | p2_radical_015_刀 | 1 → 2 | **strong** (pos 200) | moderate (P11-family + refresh recipe) | cooldown expired; prospective slot at end of window; retry-1 close-but-hook-detached, refine welding |
| 6 | p2_radical_025_力 | 0 → 1 | **strong** (pos 185) | moderate (same 横折钩+crossing 撇 family as 刀; solve 刀 first, apply same recipe) | prospective; parallels 刀 |
| 7 | p2_radical_077_忄 | 0 → 1 | none | **strong** (variant_dian mirror — form_catalog documents this exact case) | pure retrospective test of the mirror-dian helper |
| 8 | p2_radical_083_丬 | 0 → 1 | none | **strong** (variant_dian w_tail≈5) | pure retrospective |
| 9 | p2_radical_088_长 | 0 → 1 | none | **strong** (variant_na bow_perp≈+12; evolution log named item) | pure retrospective |
| 10 | p2_radical_098_火 | 0 → 1 | none | **strong** (fu.py X + variant_dian side dots) | pure retrospective; depends on 人 also passing |
| 11 | p2_radical_100_见 | 0 → 1 | none | **strong** (ri.py tall-rectangle template + hand-placed descenders) | pure retrospective; validates the "inline box for non-1:1 aspect" lesson |
| 12 | p2_radical_113_犬 | 0 → 1 | none | **strong** (fu.py X + variant_dian) | pure retrospective; depends on 大 also passing |
| 13 | p2_radical_117_手 | 0 → 1 | none | **strong** (shou_pang base + prepend variant_pie) | pure retrospective; smallest incremental change |

### SKIP (rationale summary)

- **Phase-1 hook fails (7 items)**: same reasoning as scan_100. Not
  prospective; TR8 (retired) and v7 variant helpers do not address
  standalone-stroke rendering. SKIP all 7.
- **p1_stroke_26_横折折** — STALE (retry_n=2, terminal-freeze).
- **p2_radical_010_勹**, **011_匕**, **020_阝**, **032_厶**, **035_讠**,
  **036_廴**, **040_屮**, **041_彳**, **042_巛**, **047_飞**,
  **050_弓**, **055_彑**, **056_巾**, **058_马**, **059_门**: no
  prospective use in 151-200 and no new v7 helper directly addresses
  their failure modes. Defer to a window with prospective utility.
- **p2_radical_112_欠** — SKIP. Consider ONLY if 人 passes this scan;
  currently at retry_n=0, but the (b) recipe depends on shared-apex 人
  succeeding first. Better to burn 欠's first retry when 人 is verified
  a working prereq (next scan window).
- **p2_radical_053_己**, **038_㔾**, **061_女**, **062_犭** — retry_n=2,
  cooldown expired, but v7 helpers do NOT directly address their
  failure modes (curl-envelope / small-elbow-hook / crossing-heng).
  Retrying without a specific new lever would burn retry_n=3 for no
  clear reason. SKIP; wait until a curl or elbow-specific helper
  emerges.
- **All other 8 signature-restriction items already RETRIED above.**

## Summary

- **Errata items considered**: ~40 net-active.
- **RETRY**: 13 items.
- **SKIP**: ~27 items.
- **Retry rate = 13/40 ≈ 33%** — noticeably higher than scan_100's
  27% and scan_50's 18%. Justification: v7 restructure added a
  genuine new (b) axis (adaptive helpers + form_catalog); 8 of the 13
  retries are the exact items the restructure was designed to fix
  (evolution.md names them); the other 5 are Phase-3 prerequisites in
  the immediate 151-200 window OR are the retry_n=2 items whose
  cooldown just expired AND whose failure mode now has a matching
  helper.

If B3 retry pass rate < 40%, revisit the helpers themselves (they
may need per-context defaults or additional variant classes such as
`variant_shu` / `variant_heng`). If B3 retry pass rate > 60%, the
form_catalog + variant-helper direction is validated and the next
evolution move is to expand it (e.g., `variant_gou`, `variant_zhe`).

## Retry priority order (Drawer, attempt in this order)

1. **大 (046)** — solve first; unlocks 犬 later in the scan.
2. **人 (028)** — solve early; unlocks 火, 欠-later, 犬.
3. **入 (030)** — same family as 人.
4. **丷 (021)** — same variant_dian mirror as 077 忄.
5. **077 忄** — mirror-dian test.
6. **083 丬** — compact-dian test.
7. **088 长** — variant_na bow test.
8. **117 手** — smallest incremental change (shou_pang + prepend pie).
9. **100 见** — inline tall box.
10. **098 火** — depends on 人 (step 2) succeeding first.
11. **113 犬** — depends on 大 (step 1) succeeding first.
12. **刀 (015)** — cooldown-expired refinement, prospective pos 200.
13. **力 (025)** — apply the recipe validated on 刀.
