"""
八 (ba) — 撇 + 捺 separated with top gap.

Tags: tag:character tag:2-strokes tag:撇捺-separated
Mastered: run_4 cycle 18, rubric 10/10 (OCR 八, visual 0.42)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pie import draw as draw_pie
from na import draw as draw_na

def draw(t, ox=0.0, oy=0.0, scale=1.0):
    draw_pie(t, ox=ox-115*scale, oy=oy-25*scale, scale=0.55*scale)
    draw_na(t, ox=ox+130*scale, oy=oy-20*scale, scale=0.55*scale)
