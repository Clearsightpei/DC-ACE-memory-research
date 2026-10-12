#!/usr/bin/env python3
"""reproduce_paper_stats.py — regenerate every statistic reported in the paper
from export/item_grades.csv alone.

Reproduces: Table 1, Table 3 (retries), Table 4 (common-window four tiers),
and the figures in Sections 3.3-3.6, plus export/fig3_matched_advantage.csv.

    python3 analysis/reproduce_paper_stats.py

Requires numpy + scipy. Read-only with respect to the experiment: it never
modifies judgments/ or item_grades.csv.

Conventions (see export/COUNTING_RULE.md):
  Success = Perfect(A) or Pass          Failure = Close(C) or Fail
  First attempt  = item_id with no __retry_N suffix
  Retry          = item_id carrying __retry_N
  Diagnostic reruns (__rerun, the B7r prompt A/B) are excluded from the
  retry accounting, matching the paper's Table 3 footnote.
  Common four-tier window = curriculum positions 419-668 (batches B9-B13).
"""
import csv, collections, math, os, re, sys
import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
EXPORT = os.path.join(ROOT, "export")

GROUPS = ["G1", "G2", "G3", "G4", "G5"]
LABEL = {"G1": "G1 no memory", "G2": "G2 notes", "G3": "G3 code bank",
         "G4": "G4 grid + supervision", "G5": "G5 code bank + supervision"}
RAD = re.compile(r"^p2_radical_(\d+)_(.*)$")
CHR_ = re.compile(r"^p3_char_(\d+)_(.*)$")
SUCC = lambda v: v in ("A", "PASS")
PERF = lambda v: v == "A"
TIER = {"A": "Perfect", "PASS": "Pass", "C": "Close", "FAIL": "Fail"}


def parse(item_id):
    """-> (absolute curriculum position, retry_n). retry_n == 0 is a first attempt."""
    m = RAD.match(item_id)
    if m:
        base, suf = int(m.group(1)), m.group(2)
    else:
        m = CHR_.match(item_id)
        if not m:
            return None, None, False
        base, suf = int(m.group(1)) + 135, m.group(2)
    r = re.search(r"__retry_(\d+)", suf)
    return base, (int(r.group(1)) if r else 0), ("__rerun" in suf)


def load():
    rows = list(csv.DictReader(open(os.path.join(EXPORT, "item_grades.csv"),
                                    encoding="utf-8")))
    first, retry = collections.defaultdict(dict), collections.defaultdict(list)
    for r in rows:
        a, rn, rerun = parse(r["item_id"])
        if a is None:
            continue                      # 32-stroke primer, not in the 668
        r["abs"], r["rerun"] = a, rerun
        r["batch_n"] = r["batch"].replace("G5_", "")
        if rn == 0:
            first[r["group"]][a] = r
        elif not rerun:                   # diagnostic reruns excluded
            retry[(r["group"], a)].append((rn, r))
    for k in retry:
        retry[k].sort(key=lambda t: t[0])
    return first, retry


def mcnemar(first, ga, gb, items, pred=SUCC):
    a = b = c = d = 0
    for i in items:
        x, y = pred(first[ga][i]["verdict"]), pred(first[gb][i]["verdict"])
        if x and y: a += 1
        elif x: b += 1
        elif y: c += 1
        else: d += 1
    n, disc = a + b + c + d, b + c
    p = stats.binomtest(b, disc, 0.5).pvalue if disc else 1.0
    pa, pb = (a + b) / n, (a + c) / n
    var = (b + c - (b - c) ** 2 / n) / n ** 2 if n else 0
    se = math.sqrt(max(var, 0))
    return dict(n=n, b=b, c=c, pa=pa, pb=pb, diff=pb - pa, p=p,
                lo=(pb - pa) - 1.96 * se, hi=(pb - pa) + 1.96 * se)


def line(tag, m, ga, gb):
    print(f"  {tag:<34} {100*m['pa']:5.1f}% vs {100*m['pb']:5.1f}%  "
          f"{100*m['diff']:+6.1f} pp [{100*m['lo']:+5.1f},{100*m['hi']:+5.1f}]  "
          f"disc {m['b']:>3} vs {m['c']:<3}  p={m['p']:.4g}")


def main():
    first, retry = load()
    ALL = sorted(first["G1"])
    BATCH = {a: first["G1"][a]["batch_n"] for a in ALL}
    ORDER = ["bootstrap"] + [f"B{i}" for i in range(1, 14)]
    WIN = sorted(a for a in ALL if BATCH[a] in ("B9","B10","B11","B12","B13"))
    TAIL = sorted(a for a in ALL if BATCH[a] in ("B8","B9","B10","B11","B12","B13"))
    assert len(ALL) == 668 and len(WIN) == 250 and len(TAIL) == 300
    for g in GROUPS:
        assert len(first[g]) == 668, f"{g} has {len(first[g])} first attempts"

    print("="*78); print("TABLE 1 — first-attempt outcomes"); print("="*78)
    print(f"{'Condition':<30}{'Success n':>10}{'rate':>9}{'Perfect n':>11}{'rate':>8}")
    for g in GROUPS:
        s = sum(1 for a in ALL if SUCC(first[g][a]["verdict"]))
        p = sum(1 for a in WIN if PERF(first[g][a]["verdict"]))
        print(f"{LABEL[g]:<30}{s:>10}{100*s/668:>8.1f}%{p:>11}{100*p/250:>7.1f}%")

    print()
    print("="*78); print("TABLE 4 — four-tier, common B9-B13 window (250 items)"); print("="*78)
    print(f"{'Condition':<30}{'Perfect':>8}{'Pass':>7}{'Close':>7}{'Fail':>7}")
    for g in GROUPS:
        c = collections.Counter(TIER[first[g][a]["verdict"]] for a in WIN)
        assert sum(c.values()) == 250
        print(f"{LABEL[g]:<30}{c['Perfect']:>8}{c['Pass']:>7}{c['Close']:>7}{c['Fail']:>7}")

    print()
    print("="*78); print("S3.3 — accumulated memory and memory design"); print("="*78)
    line("G1 vs G2 (all 668)", mcnemar(first,"G1","G2",ALL), "G1","G2")
    line("G1 vs G3 (all 668)", mcnemar(first,"G1","G3",ALL), "G1","G3")
    line("G2 vs G3 (all 668)", mcnemar(first,"G2","G3",ALL), "G2","G3")
    m = mcnemar(first,"G2","G3",WIN,PERF)
    print(f"  {'G2 vs G3 Perfect (window)':<34} {int(m['pa']*250)}/250 vs "
          f"{int(round(m['pb']*250))}/250  disc {m['b']} vs {m['c']}  p={m['p']:.4g}")

    print()
    print("="*78); print("S3.4 — relative benefit across the curriculum"); print("="*78)
    for g in GROUPS:
        s = sum(1 for a in TAIL if SUCC(first[g][a]["verdict"]))
        print(f"  {LABEL[g]:<30} B8-B13: {100*s/300:5.1f}%  ({s}/300)")
    line("G1 vs G2 (B8-B13)", mcnemar(first,"G1","G2",TAIL), "G1","G2")
    line("G1 vs G3 (B8-B13)", mcnemar(first,"G1","G3",TAIL), "G1","G3")
    line("G2 vs G3 (B8-B13)", mcnemar(first,"G2","G3",TAIL), "G2","G3")

    recs = []
    for i, bn in enumerate(ORDER):
        items = sorted(a for a in ALL if BATCH[a] == bn)
        n = len(items)
        r = {g: sum(1 for a in items if SUCC(first[g][a]["verdict"]))/n
             for g in ("G1","G2","G3")}
        recs.append(dict(idx=i, batch=bn, n=n, lo=min(items), hi=max(items),
                         g1=r["G1"], g2=r["G2"], g3=r["G3"],
                         d2=r["G2"]-r["G1"], d3=r["G3"]-r["G1"]))
    x = np.array([r["idx"] for r in recs], float)
    fits = {}
    for k in ("d2","d3"):
        y = np.array([r[k] for r in recs])*100
        n = len(x); sl, ic, rv, pv, se = stats.linregress(x, y)
        yh = ic + sl*x
        s_ = math.sqrt(((y-yh)**2).sum()/(n-2))
        sxx = ((x-x.mean())**2).sum()
        half = stats.t.ppf(.975, n-2) * s_ * np.sqrt(1/n + (x-x.mean())**2/sxx)
        rho, prho = stats.spearmanr(x, y)
        fits[k] = dict(slope=sl, p=pv, rho=rho, prho=prho, yh=yh,
                       lo=yh-half, hi=yh+half, h1=y[:7].mean(), h2=y[7:].mean())
        lab = "G2-G1" if k == "d2" else "G3-G1"
        print(f"  {lab} OLS slope {sl:+.3f} pp/batch  p={pv:.3f}   "
              f"Spearman rho={rho:+.3f} p={prho:.3f}   "
              f"1st half {y[:7].mean():+.1f} -> 2nd half {y[7:].mean():+.1f}")

    out = os.path.join(EXPORT, "fig3_matched_advantage.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["batch","batch_index","n_items","curriculum_pos_lo","curriculum_pos_hi",
                    "g1_success_rate","g2_success_rate","g3_success_rate",
                    "g2_minus_g1_pp","g3_minus_g1_pp",
                    "g2_fit_pp","g2_fit_ci_lo","g2_fit_ci_hi",
                    "g3_fit_pp","g3_fit_ci_lo","g3_fit_ci_hi"])
        for j, r in enumerate(recs):
            w.writerow([r["batch"], r["idx"], r["n"], r["lo"], r["hi"],
                        round(100*r["g1"],1), round(100*r["g2"],1), round(100*r["g3"],1),
                        round(100*r["d2"],1), round(100*r["d3"],1),
                        round(fits["d2"]["yh"][j],2), round(fits["d2"]["lo"][j],2),
                        round(fits["d2"]["hi"][j],2), round(fits["d3"]["yh"][j],2),
                        round(fits["d3"]["lo"][j],2), round(fits["d3"]["hi"][j],2)])
    print(f"  -> wrote {os.path.relpath(out, ROOT)}")

    print()
    print("="*78); print("S3.5 — target-specific structural supervision"); print("="*78)
    line("G3 vs G5 success (window)", mcnemar(first,"G3","G5",WIN), "G3","G5")
    line("G3 vs G5 Perfect (window)", mcnemar(first,"G3","G5",WIN,PERF), "G3","G5")
    line("G4 vs G5 success (window)", mcnemar(first,"G4","G5",WIN), "G4","G5")
    line("G4 vs G5 Perfect (window)", mcnemar(first,"G4","G5",WIN,PERF), "G4","G5")

    print()
    print("="*78); print("TABLE 3 — retries (diagnostic reruns excluded)"); print("="*78)
    print(f"{'Group':<30}{'Failed':>8}{'Retried':>13}{'Recovered':>14}{'Perfect':>8}{'Frozen':>12}")
    st = {}
    for g in ["G2","G3","G4","G5"]:
        failed = [a for a in ALL if not SUCC(first[g][a]["verdict"])]
        retried = [a for a in failed if (g,a) in retry]
        rec = [a for a in retried if any(SUCC(r["verdict"]) for _, r in retry[(g,a)])]
        pf = [a for a in retried if any(r["verdict"]=="A" for _, r in retry[(g,a)])]
        fr = [a for a in retried if a not in rec]
        st[g] = (len(rec), len(retried))
        print(f"{LABEL[g]:<30}{len(failed):>8}{len(retried):>8} "
              f"({100*len(retried)/len(failed):>4.1f}%){len(rec):>9} "
              f"({100*len(rec)/len(retried):>4.1f}%){len(pf):>8}{len(fr):>7} "
              f"({100*len(fr)/len(failed):>4.1f}%)")

    def fisher(g1, g2, what):
        a1, n1 = st[g1]; a2, n2 = st[g2]
        if what == "appetite":
            return None
        _, p = stats.fisher_exact([[a1, n1-a1], [a2, n2-a2]])
        print(f"  recovery {g1} vs {g2}: {100*a1/n1:.1f}% vs {100*a2/n2:.1f}%  p={p:.4g}")
    fisher("G2","G3","rec"); fisher("G4","G5","rec"); fisher("G3","G5","rec")
    print("  (reported as separate contrasts; not pooled into a format effect)")

    print()
    print("="*78); print("S3.5 — bank-import rates (explicit imports only)"); print("="*78)
    import glob
    STD = {"PIL","os","sys","math","pathlib","json","re","random","typing","itertools",
           "functools","copy","time","collections","subprocess","textwrap","string","io",
           "numpy","dataclasses","argparse","shutil","abc","enum","operator","warnings"}
    pat = re.compile(r"^\s*from\s+([A-Za-z_][A-Za-z0-9_]*)\s+import", re.M)
    for g, d in (("G3","G3_coords"),("G5","G5_code_bank_mmh")):
        files = glob.glob(os.path.join(ROOT,"groups",d,"attempts","*","generated.py"))
        if not files:
            print(f"  {g}: attempts/ not present in this checkout"); continue
        hit = 0
        for fp in files:
            s = open(fp, encoding="utf-8", errors="ignore").read()
            if [m for m in pat.findall(s) if m not in STD and m != "_anchor"]:
                hit += 1
        print(f"  {g}: {hit}/{len(files)} = {100*hit/len(files):.1f}% of attempts import a bank primitive")


if __name__ == "__main__":
    main()
