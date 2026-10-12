#!/usr/bin/env python3
"""score_reliability.py — inter-rater agreement for the second-judge study.

READ-ONLY with respect to the experiment. This script never writes to
judgments/, never modifies item_grades.csv, and never "adjudicates" a
disagreement. The reliability study measures the instrument; it does not
retroactively improve the labels.

Primary outcome (matches the paper's main outcome):
    Success = A or PASS   vs   Failure = C or FAIL
    -> raw agreement, Cohen's kappa with 95% CI, 2x2 table

Secondary:
    - four-tier agreement: raw, unweighted kappa, linear- and
      quadratic-weighted kappa (tiers ordered FAIL < C < PASS < A)
    - Perfect vs non-Perfect: raw agreement, Cohen's kappa
    - per-group breakdown, exploratory only (n=30 each)

Usage
    python3 tools/score_reliability.py
    python3 tools/score_reliability.py --dir reliability_study
"""
import argparse, json, math, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
TIERS = ["FAIL", "C", "PASS", "A"]          # ordered worst -> best
TIDX = {t: i for i, t in enumerate(TIERS)}


def kappa(pairs, cats):
    """Cohen's kappa + asymptotic 95% CI for categorical pairs."""
    n = len(pairs)
    if n == 0:
        return None
    k = len(cats)
    ci = {c: i for i, c in enumerate(cats)}
    obs = [[0] * k for _ in range(k)]
    for a, b in pairs:
        obs[ci[a]][ci[b]] += 1
    po = sum(obs[i][i] for i in range(k)) / n
    r = [sum(obs[i]) / n for i in range(k)]
    c = [sum(obs[i][j] for i in range(k)) / n for j in range(k)]
    pe = sum(r[i] * c[i] for i in range(k))
    kap = (po - pe) / (1 - pe) if pe != 1 else float("nan")
    se = math.sqrt(po * (1 - po) / (n * (1 - pe) ** 2)) if pe != 1 else float("nan")
    return dict(n=n, po=po, pe=pe, kappa=kap, se=se,
                lo=kap - 1.96 * se, hi=kap + 1.96 * se, table=obs, cats=cats)


def weighted_kappa(pairs, cats, power=1):
    """Linear (power=1) or quadratic (power=2) weighted kappa."""
    n = len(pairs)
    k = len(cats)
    ci = {c: i for i, c in enumerate(cats)}
    obs = [[0.0] * k for _ in range(k)]
    for a, b in pairs:
        obs[ci[a]][ci[b]] += 1
    r = [sum(obs[i]) for i in range(k)]
    c = [sum(obs[i][j] for i in range(k)) for j in range(k)]
    w = [[(abs(i - j) / (k - 1)) ** power for j in range(k)] for i in range(k)]
    num = sum(w[i][j] * obs[i][j] for i in range(k) for j in range(k))
    den = sum(w[i][j] * r[i] * c[j] / n for i in range(k) for j in range(k))
    return 1 - num / den if den else float("nan")


def interpret(k):
    if k != k:      return "undefined"
    if k < 0:       return "worse than chance"
    if k < .20:     return "slight"
    if k < .40:     return "fair"
    if k < .60:     return "moderate"
    if k < .80:     return "substantial"
    return "almost perfect"


def show(res, title):
    print(f"\n{title}")
    print(f"  n                 : {res['n']}")
    print(f"  raw agreement     : {100*res['po']:.1f}%  "
          f"({int(round(res['po']*res['n']))}/{res['n']})")
    print(f"  expected by chance: {100*res['pe']:.1f}%")
    print(f"  Cohen's kappa     : {res['kappa']:.3f}  95% CI "
          f"[{res['lo']:.3f}, {res['hi']:.3f}]   ({interpret(res['kappa'])})")
    if res["hi"] > 1 or res["lo"] < -1:
        print("    (CI exceeds kappa's range: the asymptotic SE is unreliable "
              "here because\n     at least one category is sparse — read the raw "
              "agreement and table instead)")
    cats = res["cats"]
    lw = max(len(c) for c in cats) + 2
    w = max(7, lw)
    print(f"  contingency (rows = original judge, cols = second judge)")
    print("    " + " " * lw + "".join(f"{c:>{w}}" for c in cats))
    for i, c in enumerate(cats):
        print(f"    {c:<{lw}}" + "".join(f"{res['table'][i][j]:>{w}}"
                                        for j in range(len(cats))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.join(ROOT, "reliability_study"))
    args = ap.parse_args()

    key_path = os.path.join(args.dir, "ANSWER_KEY.json")
    lab_path = os.path.join(args.dir, "labels.json")
    spec_path = os.path.join(args.dir, "SAMPLE_SPEC.json")
    if not os.path.exists(lab_path):
        sys.exit(f"No labels yet at {lab_path}\n"
                 f"The second judge has not run judge_blind.py on this manifest.")

    key = json.load(open(key_path, encoding="utf-8"))
    labels = json.load(open(lab_path, encoding="utf-8"))
    spec = json.load(open(spec_path)) if os.path.exists(spec_path) else {}

    print("=" * 68)
    print("SECOND-JUDGE RELIABILITY")
    print("=" * 68)
    if spec:
        print(f"seed {spec.get('seed')} · {spec.get('sampling')}")
        print(f"window: {spec.get('window')}")
        print(f"selection sha256: {spec.get('selection_sha256','')[:16]}...")

    pairs, skipped, per_group = [], 0, collections.defaultdict(list)
    for token, meta in key.items():
        rec = labels.get(f"{token}__att0")
        v2 = rec.get("verdict") if isinstance(rec, dict) else rec
        if v2 is None or v2 == "SKIP":
            skipped += 1
            continue
        v1 = meta["original_verdict"]
        if v1 not in TIDX or v2 not in TIDX:
            skipped += 1
            continue
        pairs.append((v1, v2))
        per_group[meta["group"]].append((v1, v2))

    print(f"\njudged pairs: {len(pairs)}   skipped/unjudged: {skipped}")
    if not pairs:
        sys.exit("No usable pairs.")

    SUCC = lambda v: "Success" if v in ("A", "PASS") else "Failure"
    PERF = lambda v: "Perfect" if v == "A" else "non-Perfect"

    print("\n" + "=" * 68)
    print("PRIMARY — Success (A+PASS) vs Failure (C+FAIL)")
    print("=" * 68)
    prim = kappa([(SUCC(a), SUCC(b)) for a, b in pairs], ["Success", "Failure"])
    show(prim, "binary success agreement")

    print("\n" + "=" * 68)
    print("SECONDARY")
    print("=" * 68)
    four = kappa(pairs, TIERS)
    show(four, "four-tier agreement (unweighted)")
    kl = weighted_kappa(pairs, TIERS, 1)
    kq = weighted_kappa(pairs, TIERS, 2)
    print(f"\n  linear-weighted kappa    : {kl:.3f}   ({interpret(kl)})")
    print(f"  quadratic-weighted kappa : {kq:.3f}   ({interpret(kq)})")
    print(f"  (tiers ordered FAIL < C < PASS < A; weights penalise distant "
          f"disagreements more)")

    perf = kappa([(PERF(a), PERF(b)) for a, b in pairs], ["Perfect", "non-Perfect"])
    show(perf, "Perfect vs non-Perfect agreement")

    print("\n" + "=" * 68)
    print("EXPLORATORY — per-group (n=30 each; not powered, do not test)")
    print("=" * 68)
    print(f"  {'group':<7}{'n':>4}{'raw agr':>10}{'kappa':>9}   (binary success)")
    for g in ["G1", "G2", "G3", "G4", "G5"]:
        gp = per_group.get(g, [])
        if not gp:
            continue
        r = kappa([(SUCC(a), SUCC(b)) for a, b in gp], ["Success", "Failure"])
        print(f"  {g:<7}{r['n']:>4}{100*r['po']:>9.1f}%{r['kappa']:>9.3f}")

    print("\n" + "=" * 68)
    print("MARGINALS — did the two judges use the tiers at different rates?")
    print("=" * 68)
    c1 = collections.Counter(a for a, _ in pairs)
    c2 = collections.Counter(b for _, b in pairs)
    print(f"  {'tier':<6}{'original':>10}{'second':>9}")
    for t in TIERS:
        print(f"  {t:<6}{c1[t]:>10}{c2[t]:>9}")
    s1 = sum(c1[t] for t in ("A", "PASS"))
    s2 = sum(c2[t] for t in ("A", "PASS"))
    print(f"\n  success rate  original {100*s1/len(pairs):.1f}%   "
          f"second {100*s2/len(pairs):.1f}%")
    print("\nNOTE: this script is read-only. Disagreements are not adjudicated and")
    print("      the experiment's original labels are unchanged, by design.")


if __name__ == "__main__":
    main()
