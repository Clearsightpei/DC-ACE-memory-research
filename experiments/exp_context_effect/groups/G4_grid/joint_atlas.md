# Joint Atlas (G4)

*Split out of principle_bank.md at position 150. Everything about
P/T/N/S joint classification, welding, gap sizing, sanity assertions.
Consult when a joint class or gap decision is uncertain.*

## The four joint classes

- **P (Piercing / welded crossing)**: two strokes cross through a
  shared pixel. Both anchor tuples must be IDENTICAL at the crossing
  or two strokes must be constructed to pass through a shared
  P_cross point. Draw a small 顿笔 disc (r ≈ 4–6) at the vertex so
  the weld stays visible when segment widths differ.
- **T (Tangent / tip-touches-body)**: one stroke's endpoint sits ON
  another stroke's body but does not cross it. The touching endpoint
  should either share the exact anchor (weld) or land within ~15 px
  of the body along the perpendicular.
- **N (Neighbor / small natural gap)**: two endpoints intentionally
  sit within ~0.15 x_frac/y_frac of each other WITHOUT touching.
  Target pixel gap 15–25 px.
- **S (Separate)**: strokes share the character but do NOT participate
  in any joint (e.g. 氵 three drops, 二 two horizontals).

## Enforcement patterns

### P — shared pixel, not just close anchors

For 十, 木, 大, 犬, 父 X-crossings and any radical where two strokes
must visibly cross:
```python
CROSS = ('C', 0.5, 0.5)          # shared anchor tuple
draw_heng(draw, left=('ML',0.15,0.5), right=('MR',0.85,0.5))  # passes through CROSS
draw_shu(draw, top=('TC',0.5,0.15), bot=('BC',0.5,0.85))       # passes through CROSS
```

For two curved strokes crossing (犬 撇+捺; 父 pie+na X):
- Compute the intersection pixel in advance (use `_anchor.anchor_to_xy`
  + `line_intersect` or similar).
- Set one stroke's chord to pass THROUGH that pixel; construct the
  other to pass through the same pixel.
- Anchor tuples alone don't guarantee crossing — they only bracket a
  region. (犭 bootstrap lesson.)

### T — endpoint hits body

For 亻, 彳, 攵-family where 竖 head or 撇 tail touches another
stroke's body:
- Compute the body pixel where you want to touch.
- Use `_anchor` to convert back: the tuple must land at (or within
  15 px of) that pixel.
- Do NOT use a static tuple that ignores how the body curves —
  a bowed 撇 diverges from its chord midpoint by ~20–40 px. (夊
  lesson.)

### N — target pixel gap 15–25 px

- If MMH gives two N anchors in different cells producing >30 px gap,
  OVERRIDE to same-cell placement with fracs within 0.15 (near-weld).
- Bootstrap 厂/刀 failed by treating N as literal separation. **N-class
  ≠ "strokes are visually independent."**
- For N-joint on a CURVED spine (s3 head lands ON s2 curved body mid):
  compute s2's actual pixel midpoint FIRST, then derive s3.head anchor
  by inverting `anchor_to_xy` so it lands on the ink, not on the chord.

**TR10 exception (B3, p3_021_几 lesson)**: for 几-family top gaps and
the p3_char_0031_厂 char-context 横+撇 joint, a VISIBLE ~15-20 px N
gap is required — do NOT close to weld to satisfy TR10 borderline.
Closing 几's top gap from 27 px to 6 px fused the top-left into a
closed rectangle-with-notch, killing recognizability. When the char's
canonical shape shows two clearly-separated stroke heads (几, char-厂),
keep gap in [15, 22] px even if TR10 nominally says "≤25 px looks
connected."

### S — no interaction

Just render both strokes. Verify pixel gap is >30 px (so the two
don't accidentally look touched). 氵, 灬, 二, 冫 belong here.

## Sanity assertions to run BEFORE render

```python
# For P-cross at shared anchor:
assert head_A_tuple == head_B_tuple or ... # or shared point construction

# For direction invariants:
assert p_tip[1] < p_hook_pt[1]        # hook flick goes UP
assert p_tip[0] < p_hook_pt[0]        # hook flick goes LEFT (for 竖钩)
assert p_hook_pt[0] > p_corner[0]     # 横斜钩 descent goes RIGHT
assert p_hook.x == p_head.x           # shu_gou straight body
```

Assertions turn silent geometric bugs into loud failures. ~1 line per
invariant.

## Hook-as-internal-segment convention

For strokes with a hook (钩), the hook is the primitive's internal
segment, NOT a separate declared joint. Only pivots between different
stroke types (横→竖, 竖→提, 撇→点, 撇→横) count as declared joints.

## Standardized anchor convention (locked)

- Canvas 300×300, cell 100×100, 3×3 米字格.
- Cell origin TOP-LEFT; `x_frac` grows RIGHT, `y_frac` grows DOWN
  (PIL-native, y=0 at top).
- Helper: `success_bank/code/_anchor.py`. Every primitive imports it.
- Legacy math-coord note (`px = mx + 150`, `py = 150 - my`) is obsolete.

## Bezier control derivation

- When you want the body Bezier to visibly pass THROUGH a declared
  belly point: `ctrl = 2*belly - (p_start + p_end)/2`.
- CAUTION: this places `ctrl` on the far side of `belly` from the
  chord midpoint. If `belly` is far from the chord midpoint the
  control can end up off-canvas, producing wild curves.
- **Prefer raw `belly` as Bezier control** (`quad_bezier(start, belly,
  end)`) unless the shape genuinely requires a "pass through"
  guarantee. Phase-1 cross-cycle observation: raw-control attempts
  were crisp; derived-control attempts were fragile.

## Compound-stroke joint patterns validated in bootstrap + B1 + B2

| Radical family      | Joints                          | Reference       |
|---------------------|---------------------------------|-----------------|
| 十, 木, 大, 犬       | P at C (welded X-crossing)      | `shi_ten.py`    |
| 亻, 彳               | T (竖/撇 head on 撇 body)        | `ren_side.py`   |
| 口, 囗               | 3×N corners (no welds)          | `kou.py`        |
| 川, 氵, 灬, 冫, 二    | S (all separate)                | `chuan.py`      |
| 父, 攵               | P at BC (mid-body na×pie)       | `fu.py` (B2)    |
| 门, 冂 (enclosing)   | 0–1 T at TL, tight span         | `men.py` (B2)   |
