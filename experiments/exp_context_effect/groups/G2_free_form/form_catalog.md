# Form Catalog — stroke forms indexed by (class × context)

*Created 2026-07-18 @ position 168 as the first self-evolution response.
The trajectory 83% → 70% → 40% told us that global stroke rules
("draw the flick", "share joints") were not enough — drawers needed
to know **what a stroke looks like in THIS position**, not "in general".
Each entry below encodes concrete form knowledge grounded in an
observed target (GT PNG), NOT a recipe to copy verbatim. When a new
item has an approximately-matching context, consult the relevant
entry to prime your visual expectation before drawing.*

**How to read an entry**: `class` = canonical stroke name; `context` =
what role/position the stroke plays; `form` = the visual/geometric
gist as observed in real GTs; `avoid` = the wrong sibling this
context tends to slide into.

---

## 撇 (pie)

### 撇 as top-of-radical single flick (夕, 力, 勹, 匕, 犭 top)
- **form**: SHORT-to-medium (~60–100 px), STEEP (75–80° from
  horizontal), starts upper-right ~x=170–190 y=55–75, throws
  down-left to ~x=100–130 y=130–160. Thick→thin taper with visible
  顿 dab at start. Body is nearly straight with just a hair of
  rightward bow.
- **avoid**: don't make it a long sweeping 撇 that dominates the
  glyph — that reads as a 撇-radical standalone, not a component
  hat.

### 撇 as body-crossing diagonal (刀, 力, 匕 body-crosser)
- **form**: LONG (~150–180 px), MODERATE slope (55–65°), MUST cross
  through another stroke (top 横 or 竖) with its top pixel visibly
  ABOVE the crossed line. Starts at ~y=60–75 above the crossing
  line, ends at ~y=250–270 in the lower-left. Gentle rightward bow.
- **avoid**: starting the 撇 INSIDE the top stroke's bounding box —
  loses the "crossing visible" signature, the whole item degrades
  toward the sibling glyph (力→几, 刀→乃).

### 撇 as left-position radical component (亻, 彳 top, 犭 top, 攵 top-left)
- **form**: SHORTER than a standalone 撇 (~80–110 px), starts near
  x=130–150 (left of center), throws down-left to x=70–90. Steeper
  than a body-crossing 撇 (70–80°). Leaves horizontal room to the
  right for the rest of the radical.
- **avoid**: full-width 撇 that would cross the whole canvas — pins
  the rest of the radical against the right wall and makes the
  glyph unreadable.

### 撇 as top-lid (dot-撇, as in 亠, 户 top, 方 top)
- **form**: VERY SHORT (~35–50 px), acts like a stubby diagonal
  bar; starts ~x=140 y=50, ends ~x=110 y=80. Basically a slightly-
  elongated 点 that tilts. Not a full 撇 — length is the giveaway.
- **avoid**: rendering a full 撇 here pushes the following 横 off
  the top of the canvas.

### 撇 as parallel-repetition (彡, 巛, 川 middle, 氵-strokes ARE 点 not 撇 — see below)
- **form**: three copies at ~consistent x-offset (~40 px apart),
  each SHORT (~60 px), moderate slope (~60°), aligned diagonally
  so the three tips stack roughly on a diagonal line.
- **avoid**: making them parallel-vertical (reads as 川); making
  them the same y-position (reads as 三 tilted).

---

## 点 (dian) — teardrop dot family

### 点 as 氵 water-radical component
- **form**: THREE teardrops stacked at INCREASING size top-to-
  bottom; top two thin→thick short flicks going down-right (~40 px,
  angle ~45°), bottom one is a rising 提 (thin end points up-right).
  x-positions form a slight leftward curve: top ~x=140, middle
  ~x=110, bottom ~x=125 (rises back). y-positions: ~90, ~150, ~215.
- **avoid**: three uniform round dots (loses calligraphic feel);
  bottom as a plain 点 instead of a 提 (loses water-radical signature).

### 点 as 忄 heart-radical side dot
- **form**: SHORT (~35 px) teardrop, thin at top → thick at bottom,
  angled ~50–60° down-right, sits at ~(90, 130) LEFT of the 竖钩.
  The paired right dot is a SHORT 横 or 点 flicking rightward at
  ~(160, 125), also short.
- **avoid**: making the left dot too long — it starts to read as a
  full 撇 and the radical degrades toward 忄 body but wrong scale.

### 点 as 灬 fire-bottom (four legs)
- **form**: four teardrops spaced evenly along the baseline
  (y=~180–220), each ~40 px. Leftmost tilts LEFT (up-left flick end),
  rightmost tilts RIGHT, middle two are near-vertical or slight-splay.
  Alternating outward direction.
- **avoid**: four identical vertical drops (reads as 川 not 灬).

### 点 as 宀 roof-cap dot
- **form**: SINGLE small teardrop at ~(150, 55), pointing straight
  down or slightly down-right, ~30 px long, sits ABOVE the 冖 lid
  with a small gap.

---

## 竖 (shu)

### 竖 as through-going axis (士, 土, 干, 车, 手, 木, 未, 未)
- **form**: STRAIGHT vertical passing THROUGH all horizontals,
  extending ~10–20 px above the top 横 and ~10–20 px below the
  bottom 横. Uniform width, 顿 dab at start (top). No hook unless
  the label says one (亅, 千, 才).
- **avoid**: floating between the horizontals with no protrusion —
  makes the glyph look like a stack of unrelated bars.

### 竖 as left-wall of a box (口, 囗, 日, 目, 田, 车 body)
- **form**: starts at the TOP-LEFT corner (shared pixel with the
  top 横's LEFT end), descends to the BOTTOM-LEFT corner. No hook.
  Uniform width. Length matches the box height.
- **avoid**: leaving a gap at the top-left corner — box no longer
  reads as closed.

### 竖 as central hanging drop (巾, 中, 甲)
- **form**: LONG vertical (~180 px), starts at the middle of the
  top 冂/口 base and extends WELL BELOW the base (~100 px below).
  Slight terminal press (blunt). Middle-hanging is the signature.
- **avoid**: short 竖 that stops at the box's base — loses the
  "hanging cloth" reading (see 巾 fail in errata).

---

## 横 (heng)

### 横 as top-lid over a hanging body (宀, 冖, 亠 top)
- **form**: MEDIUM (~140–160 px), y ≈ 70–90, slight up-tilt (3°),
  small 顿 dabs both ends. NO hook.
- **avoid**: too-long 横 that crowds the canvas edges — leaves no
  room for the body below.

### 横 as top-vs-bottom length-differentiator (士 vs 土, 干 vs 千, 上 vs 下)
- **士**: top LONGER (~150), bottom SHORTER (~110).
- **土**: top SHORTER (~110), bottom LONGER (~150).
- **干**: top SHORTER (~65% of bottom, ~110), bottom LONGER (~170).
- **千**: top has a 撇-lid replacing straight 横; bottom LONGER.
- Rule: the LONGER 横 always sits on the side that is the "base"
  of the glyph. When in doubt, look at the GT and measure.

### 横 as internal cross-bar inside a box (日, 目, 田)
- **form**: spans left-wall to right-wall exactly, touching both
  verticals. Length ~= box width. y-position determined by whether
  it's the single divider (日: middle) or one of two (目: thirds).

---

## 折 shoulder placement

### 横折 as top-right corner of a box (口, 日, 目, 田, 门 right, 巾 top)
- **form**: 横 spans top, shoulder dab at TOP-RIGHT, 竖 descends
  along right wall. The 竖 length equals the box height.
- **avoid**: shoulder inset from the box's actual right edge —
  produces a "notched" box that reads as broken.

### 横折 followed by 撇 tail (as in 又, 攵, 皮)
- **form**: 横 short (~80 px), shoulder, tail 撇 sweeps down-left
  and OUT past the 横's left end. The tail dominates in length.
- **avoid**: keeping the tail inside the 横's x-range — the whole
  glyph reads compressed and boxy.

---

## 捺 (na)

### 捺 as right-leg of two-stroke apex (人, 大, 天, 木-lower)
- **form**: starts THIN at the apex (upper-left), ends THICK at
  lower-right with a broad flat terminal foot (~10 px radius end
  press). Length matches 撇 partner. In 人 the two strokes meet at
  a single apex; in 入 the 捺 STARTS HIGHER and overhangs.
- **avoid**: uniform-width diagonal line (reads as second 撇, so
  人→∧, 大→六).

### 捺 as terminal splay under a body (走, 之, 辶)
- **form**: sweeping horizontal-tending 捺 that starts thin under
  the body and thickens over ~120–150 px to a broad rightward foot.
  y-position on the baseline (~y=240). Almost horizontal — the
  splay is what carries the character's ground.

### 捺 replaced by 点 (contextual substitution)
- When a 捺 sits UNDER another 捺 in the same glyph (e.g. lower-
  right of 从, or in some radical stacks), it degrades to a short
  反捺 (dot flicking down-right ~50 px). Common in 木 as radical
  (木 alone keeps 捺; 木 as left-radical replaces 捺 with 点).

---

## Sibling-pair topology signatures

These are the "one-bit" differences between visually adjacent glyphs.
When drawing item A, always ask "is there a nearby B I could
accidentally render?" and check the signature bit.

| pair | signature bit |
|------|--------------|
| 人 vs 入 | 人: apex at same y; 入: 捺 starts HIGHER, overhangs 撇 |
| 八 vs 儿 | 八: two disjoint 撇+捺 with top gap; 儿: 撇 + 竖弯钩 meeting near top-left |
| 士 vs 土 | 士: top 横 LONGER; 土: bottom 横 LONGER |
| 干 vs 千 | 干: two 横 + straight 竖 no hook; 千: 撇-lid top + straight 竖 no hook |
| 己 vs 已 vs 巳 | 己: middle 横 FLOATS (doesn't touch left wall); 已: middle 横 TOUCHES left wall midway; 巳: middle 横 TOUCHES at top |
| 匕 vs 七 | 匕: top stroke is a 撇 (upper-right→lower-left); 七: top is a 横 (left→right) |
| 大 vs 太 vs 犬 | 大: 一 + 人; 太: 大 + inside 点; 犬: 大 + upper-right 点 |
| 户 vs 尸 | 户: top starts with 丶 dot ABOVE the 一; 尸: top starts with 一 directly |
| 贝 vs 见 | both are 冂+人-legs; 贝 has TWO horizontal cross-bars inside, 见 has ONE horizontal + ㄦ legs (儿 style) |
| 木 vs 术 vs 未 vs 末 | 木: 一+竖+人; 未 has short top 横+longer bottom 横 (short-over-long); 末 has long top+short bottom (opposite); 术 = 木 + extra 点 upper-right |

---

## Left-position radical scaling (compression rules)

When a radical serves as the LEFT component of a compound character,
its horizontal extent compresses to ~35–45% of canvas width, and
its right-facing strokes (捺, 横 tails) shorten or degrade to 点/提.
Known instances:

- **木 → 木-left** (as in 林, 树): 捺 → 点; overall x-extent → 40%.
- **人 → 亻**: 撇 shortens, 捺 becomes a plain 竖.
- **火 → 火-left** (as in 灯): right-side 捺 degrades to 点.
- **土 → 土-left** (as in 地): bottom 横 stops SHORT of the right
  edge (~70% width) to leave room for the right component.

Rule of thumb: **a radical drawn as a standalone glyph fills the
canvas; the SAME radical drawn as a left-component compresses
horizontally and its outward-flicking strokes tuck inward.**

---

## B3 additions — new (class × context) entries + char × structural_role

### 卧钩 as 心-bowl base
- **form**: shallow smile-arc bowl (concave-up) whose belly sits at the
  bottom-middle of the canvas; two entrance/exit points at roughly the
  same y at upper-left and upper-right. Hook flicks up-and-left (~145°)
  from the right end. Bowl is noticeably shallower than 弯钩.
- **context**: only used as 心's base bowl (and 必's base). Three dots
  hover above/around it in 心 — left dot outside the bowl on the far
  left, center dot upper-middle inside the bowl, right dot upper-right
  (short rightward flick). Do NOT close the bowl into an oval.
- **avoid**: rendering as a full-depth 弯钩 arc (too tall — reads as 忄
  or unrelated hook), or losing the up-left flick (reads as ㄩ).

### 二 as top-of-radical stacked pair (无 / 旡 / 云-top)
- **form**: two 横 stacked at y≈70 and y≈110 (~40 px vertical gap).
  Top 横 is slightly SHORTER than the bottom 横 (mirror of 二 standalone
  where bottom is longer). Both spans ~120–140 px. Together they form
  the "roof plate" the 撇 + 竖弯钩 legs hang from.
- **avoid**: single 横 (reads as 尢/大); or three-横 stack (reads as
  三 or a fragment of 王).

### 撇 + 竖弯钩 as leg-pair under a lid (无 / 旡 / 兀 / 尢)
- **form**: 撇 starts at the top-lid's left-middle area (~x=110, y=95),
  throws down-left to (~x=60, y=245). 竖弯钩 starts at the top-lid's
  right-middle area (~x=180, y=95), descends and arcs rightward at
  the baseline, hooks up-and-left. The two legs SPLAY OUTWARD so the
  glyph reads bottom-heavy.
- **avoid**: parallel-vertical legs (reads as 冂 with lid); 撇 too
  short (reads as 大 mis-scaled).

### 内-square box + internal 横 (曰 / 日)
- **form**: 曰 is WIDER than 日 (x ~85% vs x ~55%); both have ONE
  internal 横 spanning wall-to-wall at ~y=middle. 曰's aspect is
  wide-flat; 日's is tall-narrow.
- **avoid**: swapping aspect ratios silently converts 曰 into 日.
  Sibling table entry.

### 月 as left-position box-with-撇 (月 standalone or in 明, 期)
- **form**: 4 strokes — 撇 down-left forming left wall (curved,
  not vertical); 横折钩 forming top+right+bottom of the box; two
  internal 横 bars spanning the interior. Aspect: tall-narrow when
  used as left-radical, near-square when standalone.
- **avoid**: rendering left wall as a straight 竖 (loses moon
  signature; reads as 目 or 用).

### 又 as two-stroke fork (又, or bottom of 支 / 攴 / 皮)
- **form**: 横撇 top (short 横 → shoulder → long down-left 撇) +
  捺 crossing from the shoulder area down-right past the 撇's tip.
  Overall silhouette is a wide-splayed V-with-cap. The 捺 dominates
  in length.
- **avoid**: 撇 and 捺 not crossing (reads as 人 with a hat); or
  the shoulder not visible (reads as a plain 乂).

### 乂 as body-cross (乂 standalone, inside 文 / 父 / 爻)
- **form**: 撇 + 捺 crossing near the vertical middle. In 爻 the
  pattern REPEATS — two 乂s stacked vertically. In 文 sits under
  the 亠 lid. In 父 sits under two top splay-dots.
- **avoid**: crossing off-center (reads as 义 or ambiguous); 捺
  as uniform diagonal instead of thin→thick with terminal foot.

---

## Char × structural_role (starts with B3 P3)

*New in B3: as Phase-3 begins, we can now index BY CHARACTER + role
in a compound. Each entry names the whole-glyph structural template
so future P3 chars sharing structural role can inherit it.*

| char | role in compounds | one-line template |
|------|-------------------|-------------------|
| 一 | anywhere as 横 | uniform bar; length differentiator when stacked |
| 丨 | anywhere as 竖 | uniform vertical; may or may not through-cross |
| 亻 | LEFT | tall-narrow 40% width; 撇+竖 leaves right room |
| 儿 | BOTTOM | legs splay outward; 撇+竖弯钩 meeting near top-left |
| 冂 | ENCLOSE (top+sides) | 3-sided open bottom; shared corners |
| 凵 | ENCLOSE (bottom+sides) | 3-sided open top; shared bottom corners |
| 冖 | TOP | wide-flat lid, NO top dot (distinguishes from 宀) |
| 亠 | TOP | small dot ABOVE a 横 lid |
| 冫 | LEFT | 2 dots stacked; tall-narrow 30% width |
| 八 | ANYWHERE | disjoint 撇+捺 with TOP GAP (distinguishes from 儿) |
| 力 | RIGHT or BOTTOM | 横折钩 + body-crossing 撇 (retry-learned) |
| 又 | RIGHT or BOTTOM | 横撇 + 捺 fork |
| 十 | ANYWHERE | horizontal + vertical cross |
| 心 | BOTTOM | 卧钩 bowl + 3 dots; four strokes |
| 月 | LEFT | tall-narrow box with 撇 left wall + 2 internal 横 |
| 王 | LEFT or BOTTOM | 3 stacked 横 + through-going 竖 |
| 文 | STANDALONE | 亠 lid + 乂 body |
| 无 | STANDALONE | 二 top-plate + 撇/竖弯钩 splay legs |
| 曰 | ANYWHERE | wide-flat box + internal 横 |
| 爻 | BOTTOM or ANYWHERE | two 乂 stacked |
| 厂 | TOP-LEFT enclose | shared corner, off-center L family |
| 七 | STANDALONE | 横 top (NOT 撇) + 竖弯钩 |
| 乂 | ANYWHERE | 撇+捺 crossing X |

---

## B4 additions

### 撇 as top-flick over enclose (刁, 习, 刀-family top)
- **form**: single short 撇 (~40–60 px) angled steeply down-left,
  starting AT or slightly ABOVE the top-right shoulder of the 横折钩
  or 横折 that forms the enclose. Tip lands just left of the top
  shoulder. Acts as a bracket-marker, not a body stroke.
- **avoid**: full-length 撇 that dominates (pushes glyph toward 力/勿/丐);
  making it a 点 instead (loses the "top-flick" signature that
  distinguishes 刁 from 丁 and 习 from 刁).

### 竖 as central-hanging axis under a 人-lid (个, 兀, 亍)
- **form**: single straight 竖 hanging from the apex of a 人-lid or
  from the middle of a 二 top-plate. Starts at the visual apex, drops
  ~120–160 px. No hook. Length matches or exceeds the lid width for
  visual balance.
- **avoid**: putting the 竖 to the SIDE of the apex (glyph reads as
  broken); making the 竖 too short (reads as 人 with a stub).

### 三 as three parallel 横 with length gradient
- **form**: top and middle 横 SHORTER (~90 px), bottom 横 LONGEST (~150 px).
  Even vertical spacing (~50 px between). This is the length hierarchy —
  bottom base is dominant.
- **avoid**: equal-length bars (reads as a musical staff, loses
  character identity).

### 山 as three verticals on a 凵 base
- **form**: 凵 base (short left 竖 + wide bottom 横 + right 竖) with a
  taller MIDDLE 竖 rising from the base's center, extending well above
  the two side verticals. Middle 竖 is ~1.6× the side verticals.
- **avoid**: three equal verticals (reads as 冚 or fence); middle 竖
  same height (loses mountain-peak signature).

### 卄/艹 as two verticals through a 一 (grass-family)
- **form**: single 一 spanning ~180 px + two 竖 crossing THROUGH the
  一 at ~30% and ~70% of its length. 竖s extend both above and below
  the 一. Symmetric wide-flat aspect.
- **avoid**: verticals only on one side (reads as 卅 or partial);
  verticals not crossing (reads as 十十).

### 门 as bracket enclose (门 with top dot)
- **form**: 3-stroke bracket — top-left dot (short 撇, ~30 px, angled
  down-left, above the left 竖) + left 竖 (straight vertical) + right
  横折钩 (top 横 spanning to left 竖, shoulder at right, 竖 descending
  right wall, terminal hook flicks UP-and-LEFT). The gap between the
  dot and the 横 is a signature — dot floats ABOVE.
- **avoid**: hook flicking down-right (reads as broken); dot placed
  ON the 横 instead of above (reads as 冂 with tick).

### 叉 as 又 with internal 点
- **form**: standard 又 fork (横撇 + 捺) with a single 点 dot placed
  INSIDE the shoulder angle (upper-middle of the interior). The 点
  is small (~30 px), acting as a fill-mark, not a body stroke.
- **avoid**: forgetting the 点 (reads as plain 又); making the 点 too
  large (reads as 支 or overloaded).

### 囗/口 as pure box
- **form**: 3-stroke rectangle — left 竖 + 横折 (top+right corner) +
  bottom 一. Corners must meet cleanly. 囗 is TALL-square (~180×180);
  口 as standalone can be near-square or slightly wider. Uniform
  stroke weight.
- **avoid**: gaps at corners (reads as broken); slanted walls (reads
  as 冂 hybrid).

### 下 as 一 + 卜 body
- **form**: top 一 (~140 px) at y≈100, then a 竖 descending from the
  一's middle, and a single 点 on the right side of the 竖 at mid-height.
  Compact silhouette.
- **avoid**: 点 to the LEFT of 竖 (reads as 卞); 竖 with a hook
  (reads as 亍 hybrid).

### 上 as 卜 + 一
- **form**: mirror of 下 — bottom 一 (LONGEST) + central 竖 rising
  from its middle + short 一 tick on the right side of the 竖.
  The bottom 一 is the base, always longer than the side tick.
- **avoid**: tick on left (reads as 卞 mirror); missing 一 base (reads
  as 卜).

### 于/亍 as 一 + 一 + 亅
- **form**: top 一 (short) + middle 一 (LONGER) + a 亅 (straight 竖
  with terminal hook up-left) dropping from the middle 一's midpoint.
  亍 has the two 一s close together at top with the hook long; 于 is
  the same skeleton, top 一 slightly shorter.
- **avoid**: dropping the terminal hook (reads as 干); reversing 横
  lengths (reads as 干).

### 才 as 一 + 亅 + 撇
- **form**: horizontal 一 (long, ~180 px, slight up-tilt) at y≈120,
  central 亅 (through-竖 with terminal hook) crossing the 一 at
  midpoint, and a short 撇 on the top-left of the 亅 sweeping down-left
  from just above the 一. The 撇 does NOT cross the 一 — it starts
  from the 亅's upper region.
- **avoid**: 撇 too long (reads as 木 sibling); missing hook on 亅
  (reads as 十).

### 大 as 一 + 人-body
- **form**: top 一 (long ~150 px, slight up-tilt) + 撇 + 捺 both
  starting from the horizontal's midpoint and splaying outward. 捺
  has the thick foot; 撇 tapers thin. Apex is on the 一.
- **avoid**: uniform diagonals (reads as 六); 撇 and 捺 starting
  from separate points (loses apex).

### 亡 as 亠 + L body
- **form**: top 点 (tiny teardrop) above a short 一 lid; below the 一,
  a left-descending 竖 turning into a rightward bottom 一 (forming an
  L shape open to the upper-right).
- **avoid**: closing the L into a full box (reads as 匚); missing top
  点 (reads as 匕 or 亾).

### 宀 as roof-cap + wide lid
- **form**: single top 点 (~30 px, teardrop pointing down) at y≈50
  centered, then a wide 横 (~180 px) at y≈95 with SHORT 竖-drops on
  BOTH ends (each ~25 px hanging down from the 横 corners). The
  短-竖 drops on both ends distinguish 宀 from 冖 (冖 has none).
- **avoid**: no drop-verticals (reads as 冖 + 点 = 亠-hybrid);
  drops too long (reads as ⺪ or as 冂+一).

### 亼 as inverted V + 一
- **form**: 人-style V-shape (撇 + 捺 meeting at apex, thick 捺 foot)
  at the top; below, a separate short 一 crossing horizontally
  under the V's apex. Two-part vertical composition.
- **avoid**: 一 touching the V feet (reads as 合); 一 above V
  (reads as 亽 or scrambled).

### 勹 as wrap-around bracket
- **form**: short top-left 撇 + 横折钩 with a wide belly-on-right arc.
  The 撇 sits at the top-left, and the 横折钩's hook flicks UP-and-LEFT
  at the belly's bottom. The interior is empty (contrast 勺 has 点
  inside, 勿 has 撇 pair inside).
- **avoid**: closing the belly (reads as 力 or 匀); dropping the
  terminal hook (reads as 勹-stub).

### 之 as 丶 + 横撇 + 平捺
- **form**: 3 strokes — top 点 (small teardrop y≈50 centered), then
  a short 横撇 (short 横 + shoulder + down-left 撇 to mid-canvas),
  then a wide horizontal 平捺 sweeping from lower-left rising to
  a broad rightward terminal foot. The 平捺 dominates as the base.
- **avoid**: 平捺 without terminal thick foot (reads as underline);
  missing top dot (reads as 乏 or scrambled).

### 丫 as two-splay top + 竖
- **form**: two short top strokes (left 撇 + right 捺/点) splaying
  outward from a central apex, with a long 竖 hanging straight
  down from the apex. Silhouette resembles a "Y".
- **avoid**: 竖 offset from apex (reads as fork); top strokes
  parallel (reads as 丨with ticks).

### 兀 as 一 + 儿-legs
- **form**: top wide 一 (~200 px at y≈70) + 撇 (left leg from lid's
  left-middle throwing down-left) + 竖弯钩 (right leg descending
  and arcing rightward with terminal hook). Cross-ref 无 template.
- **avoid**: legs meeting at top (reads as 大); missing hook (reads
  as 兀-stub).

### 乇 as 一-flick + 一 + 竖弯钩
- **form**: top 撇-flick (short down-left) + wide middle 一 crossing
  through the 撇's base + terminal 竖弯钩 body descending from the
  right of the 一 and hooking up-left at the base.
- **avoid**: missing top flick (reads as 也); straight 竖 with no
  arc (reads as 屯-hybrid).

### 于 vs 亍 vs 千 length signature
- 于/亍 both have TWO 横 + central 亅. 于's top 横 is shorter than
  middle; 亍's top-一 is separated further from middle. 千 replaces
  the top 一 with a 撇-lid.
- **avoid**: rendering 于 with 撇-lid (that's 千); rendering 亍 with
  single 横 (that's 于 mis-drawn).

### 三 vs 亖 (three-horizontals vs four-horizontals)
- 三 has bottom 一 LONGEST; internal spacing equal. Middle & top
  match in length.

---

## Char × structural_role — B4 additions

*New rows from B4 P3 passes. Each is a template future compounds
can inherit.*

| char | role in compounds | one-line template |
|------|-------------------|-------------------|
| 刁 | STANDALONE / TOP-flick family | 横折钩 body + short top-flick 撇 sitting on shoulder |
| 丁 | STANDALONE | 一 top + central 亅 (through-竖 with terminal hook up-left) |
| 刂 | RIGHT | two vertical strokes; right one is 亅 (竖钩), left is plain 短竖 |
| 勹 | ENCLOSE (top+right) | wrap-bracket; short 撇 + 横折钩 with belly-on-right; interior open |
| 匕 | STANDALONE | 撇 upper (upper-right→lower-left) crossing 竖弯钩 body; hook up-left |
| 之 | STANDALONE / BOTTOM | 丶 + 横撇 + 平捺 base with thick terminal foot |
| 丫 | STANDALONE | two-splay top + central 竖 hanging (Y-shape) |
| 大 | STANDALONE / ANYWHERE | 一 top + 撇+捺 splay body sharing apex on the 一 |
| 上 | STANDALONE | bottom 一 base + central 竖 rising + right-side tick 一 |
| 乇 | STANDALONE | 撇 flick + 一 + 竖弯钩 (托-family root) |
| 亍 | STANDALONE | short 一 + longer 一 + terminal 亅 hook |
| 于 | STANDALONE | 一 top + 一 middle + central 亅 hook |
| 亡 | STANDALONE | 亠 top + L-body (竖 into rightward 一) open upper-right |
| 下 | STANDALONE | 一 top + central 竖 + right-side 点 |
| 亼 | STANDALONE | inverted-V top (人-body) + short 一 below apex |
| 三 | STANDALONE / ANYWHERE | three 横 with length gradient (bottom longest) |
| 小 | STANDALONE / BOTTOM | central 竖钩 + two flanking dots (left down-left, right down-right) |
| 兀 | STANDALONE / TOP | 一 + 儿-legs (leg-pair splay under lid) |
| 卄 | STANDALONE (rare) | two 竖 crossing a 一 (grass-family precursor) |
| 门 | ENCLOSE (bracket) | top-left dot + left 竖 + right 横折钩 with hook up-left |
| 叉 | STANDALONE | 又 body + interior 点 |
| 囗 | ENCLOSE (full box) | 3-stroke rectangle; corners meet |
| 山 | STANDALONE / BOTTOM | 凵 base + tall middle 竖 rising above sides |
| 夂 | TOP-LEFT / STANDALONE | 撇 + 横撇 crossing + 捺 with broad foot |
| 口 | STANDALONE / ANYWHERE | 3-stroke box, square/near-square aspect |
| 千 | STANDALONE / TOP | 撇-lid top + 一 + through-going 竖 (no hook) |
| 艹 | TOP | wide 一 + two crossing 竖 |
| 宀 | TOP | roof dot + wide 横 with short 竖-drops on both ends |
| 才 | LEFT / STANDALONE | 一 + 亅 through + top-left short 撇 (does not cross 一) |

---

## B4 additions — sibling-pair table extensions

| pair | signature bit |
|------|--------------|
| 刁 vs 丁 | 刁: 横折钩 + top-flick 撇; 丁: 一 + straight 亅 (no top flick) |
| 亍 vs 于 vs 千 | 亍/于: two 一 + 亅; 千: 撇-lid + one 一 + 竖 (no hook) |
| 大 vs 六 | 大: 撇+捺 with thick 捺 foot sharing apex on 一; 六: 亠 lid + 八 legs (disjoint apex) |
| 山 vs 凵 | 山: middle 竖 rises ABOVE sides on a 凵 base; 凵 alone: no middle 竖 |
| 个 vs 亇 | 个: 人-lid (proper thin-thick 捺) + hanging 竖; 亇: two 撇 lid + hanging 竖 (捺 degenerate to 撇 = fail) |
| 丸 vs 九 | 丸: 九 body + interior 丶; 九: 撇 + 横折弯钩 only |
| 孑 vs 孓 vs 子 | 孑: horizontal tick to LEFT of 竖钩; 孓: horizontal tick to RIGHT; 子: full 一 crossing 竖钩 |
| 尢 vs 九 | 尢: 一 top + 撇 + 竖弯钩 (three strokes with lid); 九: no lid, just 撇 + 横折弯钩 |
| 之 vs 乏 | 之: 丶 + 横撇 + 平捺 (3 strokes, top dot); 乏: 丿 + 之 (4 strokes with top 撇) |
| 于 vs 亍 | 于: two 一 stacked close then 亅; 亍: same skeleton but strokes vertically further apart |

---

---

## B5 additions — new (char × structural_role) entries from PASS cohort

| char | structural role / form entry |
|------|-------------------------------|
| 屮 | STANDALONE — central 竖 + wide bottom 一 + short flanking 撇 (3-stroke sprout) |
| 工 | STANDALONE — top 一 + through-竖 + bottom 一 with matched 横 lengths |
| 川 | STANDALONE — left 撇 + two 竖 (middle slightly shorter than right) |
| 义 | STANDALONE — top 丶 + long 撇+捺 crossing UNDER the dot (X-topology) |
| 乡 | STANDALONE — two 撇折 stacked + terminal 撇 (zigzag column) |
| 廾 | BOTTOM / STANDALONE — two vertical + two crossing 横 (distinct from 井 by no top-crossing) |
| 弋 | STANDALONE — 一 + 斜钩 (diagonal hook body) + top-right 丶 |
| 不 | STANDALONE — 一 lid + 丨 + 撇 + 丶 (4-stroke fork) |
| 丹 | STANDALONE — 冂-box + through-横 + interior 丶 |
| 为 | STANDALONE — top 丶 + 撇 + 横折钩 + interior 丶 (4-stroke) |
| 以 | STANDALONE — left 竖提 + 丶 + 人-legs on right |
| 中 | STANDALONE — 口-box + through-竖 (center-crossing signature bit) |
| 亓 | STANDALONE — 一 lid + 一 + 撇 + 竖 |
| 日 | STANDALONE / RADICAL — closed 口-box with interior 一 (sun) |
| 仄 | STANDALONE — 厂 lid + 人 inside (人-inside-enclose) |
| 心 | STANDALONE / BOTTOM — 卧钩 + three 丶 in canonical positions (dot placement: interior + top-left + top-right) |
| 文 | STANDALONE — 亠 lid + 撇+捺 sharing apex cleanly under lid |
| 冈 | STANDALONE / ENCLOSE — 冂-box + 乂 interior (distinct from 网 which has more interior detail) |
| 太 | STANDALONE — 大 skeleton + interior 丶 under apex |
| 龶 | TOP-radical variant — 士-top + 一 base (士-family) |

## B5 additions — sibling-pair table extensions

| pair | signature bit |
|------|--------------|
| 士 vs 土 | 士: TOP 横 LONGER (~1.5x bottom); 土: TOP 横 SHORTER (bottom 横 dominates) |
| 中 vs 口 | 中: 口-box + through-竖 (crosses BOTH lid and floor); 口: box only |
| 义 vs 乂 | 义: top 丶 above the X crossing; 乂 alone: no dot |
| 冈 vs 冂 | 冈: 冂 + 乂 interior; 冂 alone: no interior |
| 太 vs 大 | 太: 大 + interior 丶 under apex; 大 alone: no dot |
| 廾 vs 井 | 廾: two 竖 + two crossing 横 (verticals do NOT extend above); 井: full grid with 竖 rising above |
| 亓 vs 元 | 亓: 一 lid + 一 + 撇+竖 (4 strokes, 竖 straight); 元: 亠 lid + 儿 legs (4 strokes, right leg is 竖弯钩) |

*This catalog grows entry-by-entry as the curator observes new
context/form pairs. Additions should ground each entry in an
observed GT (not memorized recipes).*

## B10 additions (curator @ pos 550)

### 疒 as compound-left-wrap (sickness radical) — 5 strokes, NOT 3

疒 is NOT 广. B7's 疔 fail and B10's 疙/疟/疠 FAILs + 疚/疝 C's all
rendered it as 广 (3 strokes: 丶 + 一 + 丿), which drops the interior
冫 identity bit.

Correct 5-stroke inventory:

1. **丶 top-dot** at the crown (small teardrop, ~x=110, y=45 at 300×300).
2. **一 short horizontal** running rightward from top area of the dot
   toward ~x=175, y=65. Short, ~50-60 px.
3. **丿 long down-left 撇** starting from the right end of the 一
   (~x=175, y=65), sweeping down-and-left to a tail at ~x=60, y=245.
   Bezier belly bows outward (control point pulled down-left of chord
   midpoint).
4. **丶 inner dot** (upper of the 冫 pair) sitting INSIDE the wedge
   formed by the 一 and the 丿, upper-left region. Anchor ~x=105,
   y=110. Small teardrop, slants down-right (top narrower).
5. **提 inner rising tick** (lower of the 冫 pair) below the inner
   dot. Anchor start ~x=90, y=160, tip ~x=140, y=140. Thick→thin,
   rising ~25° above horizontal.

The compound's right-side radical (乞 in 疙, 虐 in 疟, 万 in 疠, 久
in 疚, 山 in 疝, 疋 in 疌 as second layer) sits inside the wedge to
the right of the 冫 pair, spanning roughly x=140-260, y=90-250.

**Retrieval trigger**: any target character containing 疒 (病 症 疙
疟 疠 疚 疝 疔 疖 疋(as component under 疒 wedge) etc.). Do NOT
default to 广 body.

### 勺-wrap (as in 的, 匀, 勺 itself)

Rendered as **3 primitives**, not as an oval loop:

1. **丿 short down-left 撇** starting at top-left of the wrap.
2. **横折钩** — the semi-circular wrap. 横 running rightward from the
   撇 tip, shoulder-dab, 竖 curving down-and-inward, hook flicking
   UP-and-LEFT at the bottom-left endpoint (INTO the wrap interior).
3. **丶 inner dot** sitting inside the wrap, upper-center.

B10's 的 C rendered the wrap as a single loose ellipse — this loses
the hook flick and the inner dot, dropping the character's identity.

## B10 additions — sibling-pair table extensions

| pair | signature bit |
|------|--------------|
| 疒 vs 广 | 疒: 3-stroke 广 outline + INTERIOR 冫 pair (丶+提) inside upper-left wedge; 广: no interior 冫 |
| 氵 vs 冫 vs 三点 | 氵: 丶+丶+**提** (bottom is rising, not down-teardrop); 冫: 丶+丶 (only 2 marks); three plain dots stacked reads as neither |
| 勺 vs 匀 | 勺: 3-primitive wrap (撇+横折钩+丶); 匀: wrap + interior 二 (two horizontal 一) instead of single 丶 |
| 定 vs 元/兄 | 定: 宀 lid + 疋 body (5-stroke 疋 = 一+丨+龰-like: 横 above then 3-way splay); 元/兄: 亠/口 + 儿 legs (only 2 leg-strokes) |
| 学 vs 半 | 学: 3 top ticks + 冖 + 子 (with **hook**+横 signature); 半: 丷 + 半-body (无 hook) |

