# Success Bank — Index

Curator-owned. **Only mastered code lives here.** Entries are added
when the Curator decides a Drawer output crossed the mastery gate
(`is_correct AND ocr_confidence ≥ 0.4 AND rubric ≥ 7 no 0`, after
both skeleton and brushwork phases passed).

## How to use this bank (for the Drawer)

Two queries:

1. **By character**: looking up a whole character that's been
   mastered — copy the code from `code/<char>.py` verbatim,
   including all parameters.
2. **By component tag**: looking up a 部首 or 笔画 组合 — grep this
   INDEX for the tag (e.g. `tag:撇捺-symmetric`) and pull the cited
   entries.

**Never modify a Success Bank file by guessing.** If parameters need
adjustment for a new context (translate, scale), follow the rules in
`principle_bank.md` — but the *primitives themselves* are immutable
"hardware tools".

## Visual index

`visual/visual_index.png` — assembled grid of past wins, regenerated
by the Curator when a new entry is added. The Drawer sees this card
during render time. **This is the Drawer's only legal source of
visual reference** (it shows the Drawer's own past outputs, not GT).

## Entries

(Empty — populated as run_4 proceeds.)

<!--
Entry format:
| char | file | rubric | component tags | added in cycle |
|------|------|--------|----------------|----------------|
| 一    | code/一.py | 10/10 | tag:heng tag:atomic-stroke | c1 |
| 二    | code/二.py | 9/10  | tag:heng-pair tag:simple-char | c3 |
| 木    | code/木.py | 10/10 | tag:character tag:heng tag:shu tag:撇捺-symmetric tag:component-of(林,森,本) | c7 |
-->
