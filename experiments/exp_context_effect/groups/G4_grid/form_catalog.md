# Form Catalog (G4) — stroke class × context → anchor tuples + joint pattern

*Created at position 150 (B2 curator) as the NEW file. This is where
per-context calligraphic knowledge accumulates — indexed by stroke
class × radical/character context. The old principle_bank piled these
observations in among the meta-rules; drawers were spending context on
meta-cognition rather than form knowledge. Now the meta-rules live in
`principles_meta.md` and the concrete "how does 撇 look when it's the
left component of X" knowledge lives here.*

**How to read this file**: find your stroke class (top level), then
scan for the context that matches your current item. Each entry gives
an anchor template + typical joint pattern + a reference to a passing
Success Bank primitive if one exists.

**How this file grows**: after each batch judgment, the curator adds
new entries (or updates existing ones) with anchor patterns from
PASSing attempts, plus any lessons from FAILs.

---

## 横 (héng, horizontal)

### Context: standalone 一 or top bar of a character
- Anchors: `('ML', 0.10, 0.5)` → `('MR', 0.90, 0.5)`, width 9–10
- Row invariant (TR8/12): both endpoints in M-row.
- Reference: `yi_one.py`, `da.py` s1.

### Context: short top 横 in 士/土-family
- Shorter than the bottom horizontal (士 has top longer; 土 has bottom
  longer — check character).
- Anchors example (土 top short): `('ML', 0.829, 0.717)` →
  `('MR', 0.171, 0.579)`, width 9. B2-mastered in `tu.py`.

### Context: long middle 横 crossing a 竖 (10, 十, 木, 车)
- Full-width span: `('ML', 0.1, 0.45)` → `('MR', 0.9, 0.45)`, width 9–11.
- P-weld at C with the 竖.
- Reference: `mu.py` (B2), `che.py` (B2).

### Context: short 横 stub inside a compound stroke
- May span only 1 cell (e.g. `('C',0.15,0.5)` → `('C',0.85,0.5)`).
- Width often reduced to 7.

## 竖 (shù, vertical)

### Context: standalone 丨 or single vertical
- `('TC', 0.5, 0.10)` → `('BC', 0.5, 0.95)`, width 10.
- Column invariant: both endpoints in C-column.

### Context: 竖 as spine crossing 横 (十, 木, 车, 牛)
- Fixed x = 0.5 in TC/BC guarantees the P-weld with 横 at C.
- Reference: `mu.py`, `che.py`, `niu.py` (B2).

### Context: 竖 in enclosing left wall (口, 囗, 门)
- Anchors: `('TL', 0.30, 0.15)` → `('BL', 0.30, 0.90)`, width 8–10.
- N-joint to the horizontal at TL top corner (~7–15 px shortening
  via a helper to open the corner).
- Reference: `kou.py`, `wei_enclose.py` (B2), `men.py` (B2).

## 撇 (piě, sweep down-left)

### Context: standalone 丿 radical
- **TR9 mandatory**: `('TR', 0.85, 0.15)` → `('BL', 0.15, 0.85)`,
  head_w 14–16, curve 0.10–0.15.
- Verbatim MMH under-spans → bootstrap+B1 both FAILed 丿.

### Context: 撇 in 大 / 木 / 犬 X-crossing (left arm)
- Head near center just above the 横, tail reaches BL corner.
- Example: `('C', 0.42, 0.45)` → `('BL', 0.10, 0.95)`, curve **−0.08**
  (concave-right).
- The concave-right curve matters — flipping the sign makes the arm
  read as a diagonal, not a sweep.
- Reference: `mu.py` s3 (B2), `da.py` s2.

### Context: 撇 as left component of 亻/彳/攵-family
- Head in T*, tail in BL/BC, curve 0.09–0.12.
- Joint: T (竖/next-stroke head touches this pie's body ~50–70% along).
- Reference: `ren_side.py`, `chi_step.py`, `pu.py` (B2).

### Context: 撇 crossing 撇 (X-cross in 犭, 攵 X-portion)
- Both 撇 heads placed on upper apex; construct explicit P_cross pixel
  (line-intersect two chords, place one anchor at the intersect).
- Do NOT rely on anchors alone — 犭 bootstrap FAILed at 21 px near-cross.

## 捺 (nà, sweep down-right)

### Context: 大/犬/木 X (right arm)
- Head at center just above 横 (share y with the pie head),
  tail reaches BR corner.
- Example: `('C', 0.55, 0.45)` → `('BR', 0.90, 0.90)`,
  head_w=3 peak_w=10 tail_w=1 peak_t=0.75 curve=0.08.
- Reference: `mu.py` s4, `da.py` s3, `quan.py` (B2).

### Context: 捺 in 父/攵 X-crossing
- Head sits ABOVE-LEFT of the pie's midpoint so the na sweeps DOWN
  through the intersection region. **DO NOT** put s_na.head at same y
  as s_pie mid — makes them touch as inverted-V (Λ), not X.
  (攴 bootstrap lesson, pu.py B2 correction.)
- Example (父): `('ML', 0.84, 0.66)` → `('BR', 0.76, 0.90)`.

### Context: 平捺 (level na, as in 廴)
- Longer, more horizontal; peak_t ~0.78, curve ~0.14.
- Reference: `yin_stride.py`.

## 点 (diǎn, dot)

### Context: single 丶 radical
- Compact, head at ~TC/upper-left, tail at ~C, head_w=2 peak_w=11
  curve=0.08.
- Reference: `zhu.py`.

### Context: 3-dots-of-water 氵 (upper two)
- Small tilted dots on the LEFT column.
- Anchors: `('TC', 0.20, 0.77)` → `('C', 0.63, 0.10)` (s1);
  `('ML', 0.93, 0.40)` → `('C', 0.31, 0.69)` (s2).
- Class S — no joints. Reference: `shui.py` (B2).

### Context: 灬 (4 fire dots at bottom)
- 4 slender dots along B-row, peak_w=5–7 (narrower than a normal 点).
- s1 and s4 slant DOWN-LEFT (mirror pair); s2, s3 more vertical.
- Reference: `huo_four.py` (B2).

### Context: 忄 left/right dots
- Left dot bows RIGHTWARD (opposite of standard dian); inline it
  rather than call `draw_dian` which assumes down-right press.
- Right dot: standard `draw_dian` at `('C', 0.6, 0.37)` → `('C', 0.89, 0.63)`.
- Reference: `xin_side.py` (B2).

## 提 (tí, rising)

### Context: bottom stroke of 氵 (rising leftward-out)
- Thick head at BL, thin tip up-right to C.
- Inline `draw_ti` (not in bank yet); `head_w=14 tail_w=2 curve=-0.05`.
- Reference: `shui.py` (B2).

### Context: 弋 short heng (small horizontal top)
- Very short, thin: width 9, spans ML→MR upper-region.
- Reference: `yi_arrow.py` (B2).

## Compound strokes — form variants

### 竖弯钩 (shù wān gōu) in 儿 vs 尢
- 儿 (leg-shape standalone): bend at BOTTOM (BC corner), hook up-right
  from BR. `head=('TC',0.55,0.2), belly=('C',0.55,0.5),
  corner=('BC',0.6,0.75), hook_pt=('BR',0.2,0.7), tip=('BR',0.25,0.4)`.
  Reference: `er_legs.py`.
- 尢 (yóu, has a diagonal partner): similar corner+hook but softer knee,
  belly y further down (~0.98) for the round sweep. Reference: `you.py` (B2).
- 毛 (with two horizontals passing through): head at C(0.10,0.10),
  belly straight, corner tight, hook to BR. Reference: `mao.py` (B2).

### 横折钩 in 门 (enclosing right wall)
- Head at TC(0.15, 1.00), corner TR(0.20, 1.00), tail BR(0.20, 0.80),
  tip BR(0.05, 0.55). Compact within the right column.
- Reference: `men.py` (B2 retry).

### 撇折 (pie_zhe) as component in 幺
- Two stacked pie_zhe with the top loop smaller than the bottom.
- Top pivot at C(0.05, 0.90), bottom pivot at BC(0.10, 0.85).
- N joints at loop tips (~12–19 px).
- Reference: `yao_small.py` (B2).

---

## Contextual variants I know I'm missing (add when I see them)

- ~~撇 in 女~~ — FILLED in B3 (see 撇 section below).
- 竖钩 in 寸 (need the 点 tucked into the crotch below the hook, not
  drifting up-right — B1 failed here).
- 弓 tier-separation (top loop y_frac 0.0–0.35; mid horizontal 0.45–0.50;
  bottom sweep 0.65–1.0 — B1 failed).
- 马 as 3 strokes: 横折 top + 竖折折钩 right-descender-hook + horizontal
  through middle. Use `shu_zhe_zhe_gou.py` as the compound spine.
- 飞 as ONE inlined variable-width top piece + one small inner mark
  (fragmentation was the B1 fail mode).

Add entries above with actual anchor tuples once a PASSing render is
seen — this catalog only holds validated form/context patterns.

---

## B3 additions (positions 151-204)

### 撇 in 女 (upper-mid, PIVOT to 点 tail lower-right) — NEW

- Anchors (B3 retry PASS): `('TC', 0.35, 0.20)` head → `('C', 0.30, 0.85)`
  pivot → `('BR', 0.55, 0.75)` dian tail.
- Key: LIFT head to top (TC y=0.20), PUSH pivot DOWN (C y=0.85). Prior
  B1 attempt kept head low and pivot high, producing splayed X shape.
- Reference: `nv.py`.

### 横 in 王/韦 (multiple stacked bars around a 竖 spine) — NEW

- Middle bar shorter than top+bottom (王); use MMH anchors directly, all
  in M-row. Joint pattern: middle bar P-welded to spine; top+bottom N.
- Reference: `wang.py`, `wei_leather.py`.

### 横 in 曰 vs 日 (inner middle bar) — NEW distinction

- **曰**: inner 横 stops short of right wall (`s3_tail ('C', 0.60, 0.50)`).
- **日**: inner 横 extends wall-to-wall (`s3_tail ('MR', 0.50, 0.55)`).
- This distinction matters: 日 retry FAILed at B2 because inner bar was
  too short. B3 retry PASSed by extending it.
- Reference: `yue.py` (曰), `ri.py` (日).

### 卧钩 (wo_gou) in 心 (heart body) — NEW context

- Body spans ML→MR wide with belly deep at BC.
- Anchors: `start=('ML',0.896,0.614)`, `belly=('BC',0.50,0.40)`,
  `exit=('MR',0.024,0.849)`, `tip=('C',0.80,0.35)`.
- Tip goes clearly UP-and-LEFT of exit.
- Reference: `xin.py`.

### 撇+捺 stacked X-crossings in 爻 — NEW pattern

- Two 乂 stacked: top in y∈[0.05, 0.50], bottom in y∈[0.55, 0.98].
- Each 乂 constructed with chords that cross mid-way (fu.py pattern).
- Reference: `yao.py`.

## Phase-3 character rows (structurally simple but new catalog coverage)

Per B3 self-evolution observation: Phase-3 chars are structurally
simpler than radicals but need their own catalog rows for character-
context anchor tuples (distinct from radical-context).

### 1画 character forms

| Char | Primitive | Character-context anchor | Notes |
|------|-----------|--------------------------|-------|
| 一 | draw_heng | ML(0.10,0.5)→MR(0.90,0.5) | full M-row span |
| 丨 | draw_shu | TC(0.5,0.10)→BC(0.5,0.95) | full C-col span |
| 丶 | draw_dian | C(0.30,0.20)→C(0.65,0.55) | compact center |
| 亅 | draw_shu_gou | TC(0.5,0.10)→...→BC(0.15,0.55) | straight body, up-left tip |
| 乙 | inline | — | use yi_second bank primitive |
| 乚 | inline | — | use yi_hook bank primitive |

### 2画 character forms

| Char | Primitives | Joint | Reference |
|------|-----------|-------|-----------|
| 十 | heng + shu | P at C | shi_ten.py |
| 二 | heng + heng | S | er.py |
| 亠 | dian + heng | N | tou.py |
| 八 | pie + na | S (splayed) | ba.py |
| 入 | pie + na | T at apex | ru.py |
| 冫 | dian + dian | S | bing.py |
| 又 | heng_pie + na | P at BC | p3_char_bank.draw_p3_you |
| 儿 | pie + shu_wan_gou | none | er_legs.py |
| 亻 | pie + shu | N mid | ren_side.py |
| 七 | heng-rising + shu_wan_gou | P at C | p3_char_bank.draw_p3_qi |
| 了 | heng_pie + wan_gou | N at pivot | p3_char_bank.draw_p3_le |
| 丩 | shu_gou + wan_gou | P-cross | p3_char_bank.draw_p3_jiu_hook |
| 丷 | dian + dian | S | pian_slice.py |
| 乂 | pie + na | P at C | p3_char_bank.draw_p3_yi_lit |
| 厂 (char) | heng + pie | N (~23 px, NOT welded) | p3_char_bank.draw_p3_chang |
| 刀 (char) | heng_zhe_gou + pie | N at head | p3_char_bank.draw_p3_dao_char |

**Key P3 character finding**: 厂 as a CHARACTER should use N-gap between
横 head and 撇 head (~23 px), NOT the T-weld that the P2 radical errata
recommended. Clean-GT for the char shows visible separation. This is
the character-context vs radical-context distinction.

---

## B4 additions (positions 205-254)

### VALIDATED patterns (3+ PASS confirmations across batches)

Marking these with a bold "VALIDATED" so drawers can reuse without further check:

- **VALIDATED**: `draw_heng` full M-row span `('ML', 0.10, 0.5)` → `('MR', 0.90, 0.5)`,
  width 9-10, both endpoints row-shared. Confirmed in: 一, 三 (s1/s2/s3),
  干, 上, 于, 下.
- **VALIDATED**: `draw_shu` in enclosing left wall `('TL', 0.30, 0.15)` →
  `('BL', 0.30, 0.90)`, width 8-10, both endpoints col-shared. Confirmed
  in: 口, 囗, 门, 山, 卄.
- **VALIDATED**: 3-stroke horizontal stacking `T-row + M-row + B-row`,
  all endpoints row-shared per TR8 rule 5. Confirmed in: 三 (canonical).
- **VALIDATED**: 3-N-corner enclosure with `_shorten(4)` on corners.
  Confirmed in: 口, 囗, 曰, 日, 门, wei_enclose.
- **VALIDATED**: X-crossing with SHARED-PIXEL P at C. Confirmed in:
  大, 木, 丬 (2×P), 卄, 千, 才 candidate.

### 3-heng stacking pattern (from 三 PASS)

- Anchors: s1 `('TL', 0.90, 0.60)` → `('TR', 0.10, 0.60)` (T-row);
  s2 `('ML', 0.20, 0.50)` → `('MR', 0.80, 0.50)` (M-row, shorter);
  s3 `('BL', 0.10, 0.70)` → `('BR', 0.90, 0.70)` (B-row, longest).
- Joint spec: 2 × S (all separate; no interaction).
- Row-shared invariant honored throughout.
- Reference: `san_three.py`.

### N-apex for 亼-family (distinct from 人 T-weld apex)

- **人** (T-weld): apex shared anchor, both strokes touch at head.
- **亼** (N ~22 px): apex is a visible gap; 撇 head and 捺 head
  each in TC with x_fracs separated by 0.15+.
- Anchors (亼): s1 pie `('TC', 0.65, 0.15)` → `('BL', 0.10, 0.70)`;
  s2 na `('TC', 0.80, 0.20)` → `('BR', 0.90, 0.75)`; s3 heng in M-row.
- Do NOT weld the 亼 apex — the gap is the character's signature.
- Reference: `ji_gather.py`.

### Char-context enclosure (口 char vs 囗 radical)

- **口 char** (`kou_char.py`): reuses `kou.py` with anchors slightly
  wider than the radical to fit standalone Phase-3 usage; joint gaps
  ~15 px per _shorten helper.
- **囗 char** (`wei_enclose_char.py`): full TR9-expanded frame
  (0.05-0.95 both axes) with 3 N corners.
- Rule of thumb: 口 = compact enclosure (mouth-scale); 囗 = full frame
  (radical-scale). Choose primitive by size context.

### Straight-body override for shu_gou (于 pattern)

- When shu_gou primitive requires belly.x == head.x but MMH gives
  different x_fracs: pass `head` as both `head` and `belly` argument to
  force straight body (TR8 rule 6 hard-satisfaction).
- Example (于): `draw_shu_gou(draw, head=('TC',0.5,0.10), belly=('TC',0.5,0.10),
  hook_pt=('BC',0.5,0.85), tip=('BC',0.25,0.55))`.
- Reference: `yu_at.py`.

### Column-shared verticals piercing a horizontal (艹, 卄 pattern)

- 艹 / 卄 / 廾-family: two 竖 must be STRAIGHT (column-shared
  endpoints) and BOTH pierce a single wide 横 as P-joints.
- Anchors example (艹): s1 heng `('ML', 0.05, 0.4)` → `('MR', 0.95, 0.4)`;
  s2 left shu `('TL', 0.35, 0.15)` → `('BL', 0.35, 0.90)`;
  s3 right shu `('TR', 0.65, 0.15)` → `('BR', 0.65, 0.90)`.
- Verticals column-share (TR8 rule 6) MANDATORY; do NOT let them slant
  as diagonals (the B1 艹 failure mode).
- Reference: `cao_grass.py`, `cao_grass_radical.py`, `nian_grip.py`.

### 竖弯钩 UP-right variant (已 vs 己 distinction)

- **已** (`yi_already.py`): hook flicks UP-and-RIGHT prominently (up
  from BR corner into MR).
- **己**: (still in errata, not mastered) — hook flicks UP-and-LEFT.
- The direction is the character-distinguishing feature. When rendering
  已, force tip.x > hook_pt.x. When rendering 己, force tip.x <
  hook_pt.x.
- Reference: `yi_already.py`.

## Contextual variants still missing (updated known gaps for B5)

- ~~撇 in 女~~ FILLED B3.
- 竖钩 in 寸 — B1 still failing; needs 点 tucked into crotch below hook.
- 弓 3-tier separation — chronic; candidate for hand-written canonical
  primitive at position 300.
- 马 as 3 strokes with `shu_zhe_zhe_gou.py` spine — chronic; candidate.
- 飞 as ONE inlined variable-width polyline + inner mark — chronic;
  candidate.
- **NEW**: 丸 shu_wan_gou with belly hooking OUT-right (B4 fail).
- **NEW**: 也 with 竖弯钩 up-flick at end (B4 fail — different from
  已's up-right).
- **NEW**: 兀 = 一 + er_legs.py (NOT wu_lame.py — wrong primitive
  pick in B4).

Add entries above as PASSes accumulate.

## B5 additions (26 PASSes synthesized)

### Chronic-cluster canonical primitives (position 300)

- **丿 standalone** → `chronic/pie_radical.py`; head=('TR',0.85,0.15),
  tail=('BL',0.15,0.85), head_w=16, curve=0.15. NO tuning.
- **刀 standalone char** → `chronic/dao_char.py`; T-weld heads at
  ('ML',0.50,0.40); horiz corner ('TR',0.15,0.40); hook tip up-left.
- **冂 enclosing** → `chronic/jiong_frame.py`; 230×210 frame, strict
  verticals, TR9 span.
- **弓 3-tier** → `chronic/gong_bow.py`; s1 top on TR row, s2 middle
  heng on M row, s3 bottom on BR row; sweeps LEFT (custom).
- **马 3-stroke** → `chronic/ma_horse.py`; T-weld top, strict-
  vertical S2 walls, bottom heng ~35 px below hook_pt.

### Char-context patterns from B5 PASSes

- **Char 屮/川 (short verticals + short heng)**: verticals column-
  share, heads in T-row with 0.25 x_frac spacing.
- **Char 工 (H-shape)**: two heng row-locked (top T-row, bottom
  B-row); center shu column-locked.
- **Char 义/文 (top dot + heng + apex X-cross)**: apex shared-pixel
  (define APEX tuple, pass identical to pie head and na head).
- **Char 中 (frame + center-piercing shu)**: shu passes THROUGH
  frame mid — extend head above frame top / tail below frame bottom.
- **Char 天/太 (top-heavy 大-family)**: top heng short + mid heng long
  + apex-shared pie/na base. For 太, add tucked dot inside na body.
- **Char 仂/仃/仄 (亻 + right component)**: left half via `ren_side.py`
  in TL/ML column (x_frac 0.10-0.35); right in TR/MR/BR (x_frac 0.45-
  0.95). Two-column composition.
- **Char 心 (卧钩 + 3 dots)**: base wo_gou spanning ML→BR arc; three
  dots as bottom-inner + upper-left + upper-mid.
- **Char 冈/冘/内 (冂 frame + inner)**: enclosing frame via
  `chronic/jiong_frame.py` (VALIDATED); inner via `ren.py`,
  `er_legs.py`, or `mi_cover_char.py`.

### Contextual variants still missing (updated known gaps for B6)

- ~~丿 anti-diagonal recipe~~ SUPPLANTED by canonical primitive.
- ~~刀 T-weld + hook proportion~~ SUPPLANTED.
- ~~冂 enclosing proportion~~ SUPPLANTED.
- ~~弓 3-tier separation~~ SUPPLANTED.
- ~~马 3-stroke recipe~~ SUPPLANTED.
- **长/方/见/气/文/无 (retry_n=2 pending)**: if these fail again
  in B6, candidates for canonical primitives at position 350.
- **NEW gap 巛 3-parallel-curves**: heads T-row spacing 0.25 x_frac,
  strong 弯 curve — still not calibrated (B5 FAIL).
- **NEW gap 五 slanted-shu piercing 3-heng**: shared-pixel P at
  s2/s3 intersection needed.
- **NEW gap 亓 top-heavy 2-shu**: leg spacing at 0.30/0.70 x_frac
  with T-weld into 二 lower heng.
