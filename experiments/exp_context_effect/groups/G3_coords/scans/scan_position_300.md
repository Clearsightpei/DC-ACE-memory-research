# G3 Curator Errata Scan — position 300 (B5)

## Decision: NO NEW RETRIES

Retry mechanism disabled per B5 evolution decision (structural ceiling
of callable-Python format for X-crossing family; retries were 0/8 →
0/13 → 1/8 → 1/17 across B2-B5). Focus curator effort on main-batch
quality only. Terminal freezes (人 / 入 / 大) already applied.

## Confirmation reference

See `evolution.md` entry:
`## 2026-07-24 @ position 300 — B5 curator: HONEST RECKONING —
helper hypothesis falsified, retry mechanism killed`

Key evidence from that entry:

- Cumulative retry pass rate under v7: **2/38 = 5.2%**.
- The two graduations (子 in B4, 丷 in B5) both PASSed by *rejecting*
  or bypassing the recommended composition helpers — neither
  validates retry as a memory-consumption channel.
- B5 checklist compliance was 17/17 with helper import ≥1 on every
  retry; retrieval was NOT the binding constraint. The
  callable-Python storage format itself is the ceiling.
- Terminal freezes on the X-crossing family (人, 入, 大) applied per
  shared_rules terminal-freeze rule; documented in the top
  `TERMINAL FREEZE` block of `errata.md`.

## Actions taken this scan

- None. Zero new retry candidates appended to any pending list.
- Retry-generation code path in the G3 curator loop is effectively
  no-op from position 301 onward.
- Head curator will apply P-HELPER-SKEPTIC principle edit to
  `principles_meta.md` (out of scope for this scan sub-agent).

## Downstream expectation

B6 (positions 301–350) will run under a no-retry regime. If main
rate stabilizes in 38–54%, the format ceiling read is confirmed;
group comparison remains valid because the Success Bank storage
unit (callable Python) is preserved.

RETRY_LIST=[]
