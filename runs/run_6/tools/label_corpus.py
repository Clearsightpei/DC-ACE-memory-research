"""Side-by-side PNG labeling tool for calibration.

Shows each cycle's attempt PNG vs MMH ground-truth PNG. User presses:
  p = pass (reads as the character — even if imperfect, it's still the character)
  f = fail (does not read as the character / has obvious errors)
  s = skip (unsure / not calibration-useful)
  b = back (one cycle)
  q = quit and save

Resumable: re-runs pick up where the user left off (skips already-labeled).
Saves to tools/labels.json after every keypress.

Usage:
    python3 tools/label_corpus.py [--start CYCLE] [--end CYCLE]
"""
import argparse
import json
import os
import re
import sys
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABELS_PATH = os.path.join(ROOT, 'tools', 'labels.json')


def find_cycle_pairs(start=1, end=200):
    """Return list of (cycle_n, char, attempt_path, gt_path) for all labelable cycles."""
    pairs = []
    attempts_dir = os.path.join(ROOT, 'attempts')
    gt_dir = os.path.join(ROOT, 'ground_truths')
    for name in sorted(os.listdir(attempts_dir), key=lambda x: int(re.search(r'(\d+)', x).group(1)) if re.search(r'(\d+)', x) else 0):
        m = re.match(r'cycle_(\d+)$', name)
        if not m:
            continue
        n = int(m.group(1))
        if n < start or n > end:
            continue
        a_dir = os.path.join(attempts_dir, name)
        g_dir = os.path.join(gt_dir, name)
        if not os.path.isdir(a_dir) or not os.path.isdir(g_dir):
            continue
        a_pngs = [f for f in os.listdir(a_dir) if f.endswith('.png')]
        g_pngs = [f for f in os.listdir(g_dir) if f.endswith('.png')]
        if not a_pngs or not g_pngs:
            continue
        a_path = os.path.join(a_dir, a_pngs[0])
        g_path = os.path.join(g_dir, g_pngs[0])
        # extract char from filename like 01_力.png
        char_m = re.search(r'\d+_(.+)\.png$', a_pngs[0])
        char = char_m.group(1) if char_m else '?'
        pairs.append((n, char, a_path, g_path))
    return pairs


def load_labels():
    if os.path.exists(LABELS_PATH):
        with open(LABELS_PATH) as f:
            return json.load(f)
    return {}


def save_labels(labels):
    with open(LABELS_PATH, 'w') as f:
        json.dump(labels, f, ensure_ascii=False, indent=2, sort_keys=True)


class Labeler:
    def __init__(self, pairs, labels):
        self.pairs = pairs
        self.labels = labels
        self.idx = 0
        # skip ones already labeled (resume)
        while self.idx < len(pairs) and str(pairs[self.idx][0]) in labels:
            self.idx += 1

        self.root = tk.Tk()
        self.root.title('DC-ACE calibration labeling')
        self.root.geometry('1200x700')
        self.root.bind('<Key>', self.on_key)

        # status bar
        self.status = tk.Label(self.root, text='', font=('Helvetica', 16))
        self.status.pack(side=tk.TOP, fill=tk.X, pady=8)

        # image frames
        img_frame = tk.Frame(self.root)
        img_frame.pack(expand=True, fill=tk.BOTH)

        self.attempt_label = tk.Label(img_frame, text='ATTEMPT', font=('Helvetica', 12, 'bold'))
        self.attempt_label.grid(row=0, column=0, padx=10)
        self.gt_label = tk.Label(img_frame, text='GROUND TRUTH', font=('Helvetica', 12, 'bold'))
        self.gt_label.grid(row=0, column=1, padx=10)

        self.attempt_img = tk.Label(img_frame)
        self.attempt_img.grid(row=1, column=0, padx=10)
        self.gt_img = tk.Label(img_frame, )
        self.gt_img.grid(row=1, column=1, padx=10)

        # help bar
        help_text = 'p = PASS    f = FAIL    s = SKIP    b = BACK    q = QUIT (auto-save)'
        tk.Label(self.root, text=help_text, font=('Helvetica', 13), fg='blue').pack(side=tk.BOTTOM, pady=8)

        self.show_current()

    def show_current(self):
        if self.idx >= len(self.pairs):
            self.status.config(text=f'DONE — all {len(self.pairs)} labeled. Press q to quit.')
            return
        n, char, a_path, g_path = self.pairs[self.idx]
        a_img = Image.open(a_path)
        g_img = Image.open(g_path)
        # resize to fit (max 500x500 each)
        a_img.thumbnail((500, 500))
        g_img.thumbnail((500, 500))
        a_tk = ImageTk.PhotoImage(a_img)
        g_tk = ImageTk.PhotoImage(g_img)
        self.attempt_img.config(image=a_tk); self.attempt_img.image = a_tk
        self.gt_img.config(image=g_tk); self.gt_img.image = g_tk

        p_n = sum(1 for v in self.labels.values() if v == 'PASS')
        f_n = sum(1 for v in self.labels.values() if v == 'FAIL')
        self.status.config(text=f'Cycle {n} — {char} — [{self.idx+1}/{len(self.pairs)}, PASS:{p_n} FAIL:{f_n}]')

    def on_key(self, event):
        key = event.keysym.lower()
        if self.idx >= len(self.pairs):
            if key == 'q':
                save_labels(self.labels)
                self.root.destroy()
            return
        n = self.pairs[self.idx][0]
        if key == 'p':
            self.labels[str(n)] = 'PASS'
            save_labels(self.labels)
            self.idx += 1
            self.show_current()
        elif key == 'f':
            self.labels[str(n)] = 'FAIL'
            save_labels(self.labels)
            self.idx += 1
            self.show_current()
        elif key == 's':
            self.labels[str(n)] = 'SKIP'
            save_labels(self.labels)
            self.idx += 1
            self.show_current()
        elif key == 'b':
            if self.idx > 0:
                self.idx -= 1
                self.show_current()
        elif key == 'q':
            save_labels(self.labels)
            self.root.destroy()

    def run(self):
        self.root.mainloop()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--start', type=int, default=1, help='first cycle to consider')
    ap.add_argument('--end', type=int, default=200, help='last cycle to consider')
    args = ap.parse_args()

    pairs = find_cycle_pairs(args.start, args.end)
    labels = load_labels()
    print(f'Found {len(pairs)} cycle pairs in [{args.start}, {args.end}].')
    print(f'Labels file: {LABELS_PATH}')
    print(f'Already labeled: {len(labels)}')
    print('Opening GUI — press p / f / s / b / q')

    Labeler(pairs, labels).run()

    labels = load_labels()
    pass_n = sum(1 for v in labels.values() if v == 'PASS')
    fail_n = sum(1 for v in labels.values() if v == 'FAIL')
    skip_n = sum(1 for v in labels.values() if v == 'SKIP')
    total = pass_n + fail_n + skip_n
    print(f'\nDone. {pass_n} PASS / {fail_n} FAIL / {skip_n} SKIP. Total {total}.')


if __name__ == '__main__':
    main()
