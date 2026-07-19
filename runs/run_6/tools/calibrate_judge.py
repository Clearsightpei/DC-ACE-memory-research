"""Sweep brush_radius × recall × precision × stroke_trace_min against the
user-labeled corpus. NEAR is treated as FAIL (per user: minor errors are still errors).
Also compares against the LLM panel verdicts already in judge_results/
and measures runtime for both judges.
"""
import json
import os
import sys
import time
from itertools import product

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

from structural_judge import (
    to_binary, connected_components_tolerant,
    stroke_call_count, expected_component_count,
    gt_coverage, gt_precision, find_joints, classify,
    stroke_trace_coverage, MIN_INK_PIXELS,
)

BRUSH_RADII = [4, 6, 8, 10, 12, 14]
RECALL_THRESHOLDS = [0.15, 0.20, 0.25, 0.30, 0.35]
PRECISION_THRESHOLDS = [0.30, 0.40, 0.50, 0.60, 0.70]
TRACE_MIN_THRESHOLDS = [0.0, 0.20, 0.30, 0.40, 0.50]  # 0.0 = trace check off
TRACE_TOL = 12  # px dilation for stroke trace


def precompute_signals(cycles, brush_radii):
    """For each cycle, compute the signals at each brush_radius once."""
    sig = {}
    trace_runtimes = []
    for n in cycles:
        cycle_dir = os.path.join(ROOT, 'attempts', f'cycle_{n}')
        brief_path = os.path.join(ROOT, 'task_briefs', f'cycle_{n}_dataset.json')
        if not os.path.exists(brief_path):
            sig[n] = None
            continue
        brief = json.load(open(brief_path))
        spec = brief['characters'][0]
        char = spec['character']
        n_strokes = spec['mmh_stroke_count']
        png_path = os.path.join(cycle_dir, f'01_{char}.png')
        gen_path = os.path.join(cycle_dir, 'generated.py')
        gt_path = os.path.join(ROOT, 'ground_truths', f'cycle_{n}', f'01_{char}.png')

        if not (os.path.exists(png_path) and os.path.exists(gt_path)):
            sig[n] = None
            continue

        binary = to_binary(png_path)
        ink = int(binary.sum())
        if ink < MIN_INK_PIXELS:
            sig[n] = {'empty': True}
            continue

        joints_raw = find_joints(char)
        joints = [{'stroke_a': j['stroke_a'], 'stroke_b': j['stroke_b'],
                   'class': classify(j)} for j in joints_raw]
        expected_cc = expected_component_count(n_strokes, joints)

        actual_calls = stroke_call_count(gen_path)
        stroke_pass = (actual_calls == n_strokes)

        # stroke trace coverage (per-stroke list) — time it
        t0 = time.time()
        cov = stroke_trace_coverage(binary, char, tolerance=TRACE_TOL)
        trace_runtimes.append(time.time() - t0)
        trace_min = min(cov) if cov else 1.0
        trace_avg = sum(cov) / len(cov) if cov else 1.0

        gt_binary = to_binary(gt_path)
        per_br = {'trace_min': trace_min, 'trace_avg': trace_avg, 'cov': cov}
        for br in brush_radii:
            actual_cc = connected_components_tolerant(binary, br)
            cc_pass = (actual_cc == expected_cc)
            recall = gt_coverage(binary, gt_binary, br)
            precision = gt_precision(binary, gt_binary, br)
            per_br[br] = {
                'recall': recall, 'precision': precision,
                'stroke_pass': stroke_pass, 'cc_pass': cc_pass,
                'actual_cc': actual_cc, 'expected_cc': expected_cc,
            }
        sig[n] = per_br
    return sig, trace_runtimes


def predict(sig_n, br, rt, pt, trace_t):
    if sig_n is None or sig_n.get('empty'):
        return 'FAIL'
    s = sig_n[br]
    if not s['stroke_pass']:
        return 'FAIL'
    if not s['cc_pass']:
        return 'FAIL'
    if s['recall'] < rt:
        return 'FAIL'
    if s['precision'] < pt:
        return 'FAIL'
    if sig_n['trace_min'] < trace_t:
        return 'FAIL'
    return 'PASS'


def evaluate_config(sig, pass_cycles, fail_cycles, br, rt, pt, trace_t):
    tp = fp = tn = fn = 0
    for n in pass_cycles:
        p = predict(sig[n], br, rt, pt, trace_t)
        if p == 'PASS':
            tp += 1
        else:
            fn += 1
    for n in fail_cycles:
        p = predict(sig[n], br, rt, pt, trace_t)
        if p == 'FAIL':
            tn += 1
        else:
            fp += 1
    return tp, fp, tn, fn


def load_panel_verdicts():
    """Read judge_panel.unanimous_yes from each cycle's judge_results JSON."""
    out = {}
    jr_dir = os.path.join(ROOT, 'judge_results')
    for fn in os.listdir(jr_dir):
        if not fn.endswith('.json'):
            continue
        n = int(fn.replace('cycle_', '').replace('.json', ''))
        try:
            data = json.load(open(os.path.join(jr_dir, fn)))
            if isinstance(data, list) and data:
                jp = data[0].get('judge_panel')
                if jp and jp.get('verdicts'):
                    v = jp['verdicts']
                    # skipped panels: treat as no-verdict
                    if all(x == 'SKIPPED' for x in v):
                        continue
                    out[n] = 'PASS' if jp.get('unanimous_yes') else 'FAIL'
        except Exception:
            pass
    return out


def main():
    labels_path = os.path.join(ROOT, 'tools', 'labels.json')
    labels = json.load(open(labels_path))

    # NEAR -> FAIL per user instruction
    pass_cycles = sorted([int(k) for k, v in labels.items() if v == 'PASS'])
    fail_cycles = sorted([int(k) for k, v in labels.items()
                          if v in ('FAIL', 'NEAR')])
    print(f'Labels: {len(pass_cycles)} PASS, {len(fail_cycles)} FAIL (incl NEAR as FAIL)')

    all_cycles = pass_cycles + fail_cycles
    print(f'Precomputing signals for {len(all_cycles)} cycles × {len(BRUSH_RADII)} brush radii (incl stroke trace)...')
    t0 = time.time()
    sig, trace_runtimes = precompute_signals(all_cycles, BRUSH_RADII)
    precompute_time = time.time() - t0
    print(f'  Precompute total: {precompute_time:.1f}s')

    n_configs = len(BRUSH_RADII) * len(RECALL_THRESHOLDS) * len(PRECISION_THRESHOLDS) * len(TRACE_MIN_THRESHOLDS)
    print(f'\nSweeping {n_configs} configurations...')

    results = []
    for br, rt, pt, tr in product(BRUSH_RADII, RECALL_THRESHOLDS, PRECISION_THRESHOLDS, TRACE_MIN_THRESHOLDS):
        tp, fp, tn, fn = evaluate_config(sig, pass_cycles, fail_cycles, br, rt, pt, tr)
        agree = tp + tn
        total = tp + fn + tn + fp
        prec = tp / (tp + fp) if (tp + fp) else 0
        rec = tp / (tp + fn) if (tp + fn) else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0
        results.append({'br': br, 'rt': rt, 'pt': pt, 'tr': tr,
                        'tp': tp, 'fp': fp, 'tn': tn, 'fn': fn,
                        'agree': agree, 'agree_pct': agree / total if total else 0,
                        'f1': f1})

    # Best by agree, then F1, then prefer LOWER false-positive rate (safety)
    results.sort(key=lambda r: (-r['agree'], -r['f1'], r['fp']))
    best = results[0]
    print(f'\n=== BEST CONFIG ===')
    print(f'brush_radius={best["br"]}, recall_threshold={best["rt"]}, '
          f'precision_threshold={best["pt"]}, trace_min={best["tr"]}')
    total = len(pass_cycles) + len(fail_cycles)
    print(f'Agreement: {best["agree"]}/{total} ({100*best["agree_pct"]:.1f}%)')
    print(f'Confusion: TP={best["tp"]} FP={best["fp"]} TN={best["tn"]} FN={best["fn"]}')
    print(f'F1 (PASS-as-positive): {best["f1"]:.3f}')

    print('\nTop 15 configs:')
    print(f'  {"br":>3} {"rt":>5} {"pt":>5} {"tr":>5}  agree    F1     TP FP TN FN')
    for r in results[:15]:
        print(f'  {r["br"]:>3} {r["rt"]:>5} {r["pt"]:>5} {r["tr"]:>5}  '
              f'{r["agree_pct"]*100:>5.1f}%  {r["f1"]:.3f}  '
              f'{r["tp"]:>2} {r["fp"]:>2} {r["tn"]:>2} {r["fn"]:>2}')

    # Disagreements at best
    br, rt, pt, tr = best['br'], best['rt'], best['pt'], best['tr']
    print(f'\nDisagreements at best config:')
    for n in pass_cycles:
        if predict(sig[n], br, rt, pt, tr) != 'PASS':
            s = sig[n] if sig[n] and not sig[n].get('empty') else None
            if s:
                bs = s[br]
                print(f'  c{n}: user=PASS, judge=FAIL  (cc={bs["actual_cc"]}/{bs["expected_cc"]}, '
                      f'recall={bs["recall"]:.2f}, prec={bs["precision"]:.2f}, '
                      f'trace_min={s["trace_min"]:.2f})')
    for n in fail_cycles:
        if predict(sig[n], br, rt, pt, tr) != 'FAIL':
            s = sig[n] if sig[n] and not sig[n].get('empty') else None
            if s:
                bs = s[br]
                print(f'  c{n}: user=FAIL/NEAR, judge=PASS  (cc={bs["actual_cc"]}/{bs["expected_cc"]}, '
                      f'recall={bs["recall"]:.2f}, prec={bs["precision"]:.2f}, '
                      f'trace_min={s["trace_min"]:.2f})')

    # Compare with LLM panel
    print(f'\n=== LLM PANEL COMPARISON ===')
    panel = load_panel_verdicts()
    user_pass = set(pass_cycles)
    user_fail = set(fail_cycles)
    panel_agree = panel_tp = panel_fp = panel_tn = panel_fn = panel_total = 0
    no_panel = []
    for n in user_pass | user_fail:
        if n not in panel:
            no_panel.append(n)
            continue
        p = panel[n]
        if n in user_pass:
            if p == 'PASS':
                panel_tp += 1
            else:
                panel_fn += 1
        else:
            if p == 'FAIL':
                panel_tn += 1
            else:
                panel_fp += 1
        if (n in user_pass and p == 'PASS') or (n in user_fail and p == 'FAIL'):
            panel_agree += 1
        panel_total += 1
    print(f'Cycles with panel verdicts (not SKIPPED): {panel_total} / {len(user_pass | user_fail)}')
    print(f'Cycles without panel: {len(no_panel)} (mostly c91+ where we panel-skipped)')
    if panel_total:
        print(f'Panel agreement with user: {panel_agree}/{panel_total} '
              f'({100*panel_agree/panel_total:.1f}%)')
        print(f'  TP={panel_tp} FP={panel_fp} TN={panel_tn} FN={panel_fn}')

    # On the panel-overlap subset, how does the deterministic judge compare?
    judge_overlap_agree = judge_overlap_total = 0
    for n in user_pass | user_fail:
        if n not in panel:
            continue
        judge_overlap_total += 1
        jp = predict(sig[n], br, rt, pt, tr)
        if (n in user_pass and jp == 'PASS') or (n in user_fail and jp == 'FAIL'):
            judge_overlap_agree += 1
    print(f'\nDeterministic judge agreement (same subset): '
          f'{judge_overlap_agree}/{judge_overlap_total} ({100*judge_overlap_agree/judge_overlap_total:.1f}%)')

    # Runtime
    print(f'\n=== RUNTIME ===')
    avg_trace = sum(trace_runtimes) / len(trace_runtimes) if trace_runtimes else 0
    print(f'Deterministic judge per cycle:')
    print(f'  precompute total ({len(all_cycles)} cycles, all signals): {precompute_time:.1f}s')
    print(f'  → avg per cycle (full structural check): {precompute_time/len(all_cycles)*1000:.0f}ms')
    print(f'  stroke_trace_coverage alone: avg {avg_trace*1000:.0f}ms/cycle')
    print(f'  Once deployed (single judge_cycle call): ~{precompute_time/len(all_cycles)*1000:.0f}ms/cycle')
    print(f'\nLLM panel per cycle (from prior data):')
    print(f'  3 subagents in parallel, ~7-12s each = ~10s wall time')
    print(f'  + subagent tokens ~22k each × 3 = ~66k tokens/cycle')
    print(f'  At Sonnet pricing (~$3/Mtok in, $15/Mtok out), rough $0.20-0.50/cycle')
    print(f'\n→ Deterministic is ~{10 / (precompute_time/len(all_cycles)):.0f}× faster + ~$0/cycle')

    # Save CALIBRATION.md
    cal_path = os.path.join(ROOT, 'tools', 'CALIBRATION.md')
    with open(cal_path, 'w') as f:
        f.write(f'# Calibration ({len(pass_cycles)} PASS, {len(fail_cycles)} FAIL incl NEAR-as-FAIL)\n\n')
        f.write(f'## Best deterministic config\n')
        f.write(f'`brush_radius={br}, recall_threshold={rt}, precision_threshold={pt}, '
                f'trace_min={tr}`\n\n')
        f.write(f'- Agreement: {best["agree"]}/{total} ({100*best["agree_pct"]:.1f}%)\n')
        f.write(f'- Confusion: TP={best["tp"]} FP={best["fp"]} TN={best["tn"]} FN={best["fn"]}\n')
        f.write(f'- F1: {best["f1"]:.3f}\n\n')
        f.write(f'## LLM panel comparison\n')
        f.write(f'- Panel verdicts available: {panel_total}/{len(user_pass|user_fail)}\n')
        if panel_total:
            f.write(f'- Panel agreement: {panel_agree}/{panel_total} '
                    f'({100*panel_agree/panel_total:.1f}%)\n')
            f.write(f'- Deterministic on same subset: {judge_overlap_agree}/{judge_overlap_total} '
                    f'({100*judge_overlap_agree/judge_overlap_total:.1f}%)\n\n')
        f.write(f'## Runtime\n')
        f.write(f'- Deterministic: ~{precompute_time/len(all_cycles)*1000:.0f}ms/cycle\n')
        f.write(f'- LLM panel: ~10s wall + ~66k tokens/cycle\n')
    print(f'\nWrote {cal_path}')


if __name__ == '__main__':
    main()
