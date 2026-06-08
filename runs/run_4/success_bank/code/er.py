"""
二 (er) — two horizontal strokes, short top + long bottom.

Tags: tag:character tag:2-strokes tag:heng-stacked tag:component-of(三,王,工,...)
Mastered: run_4 cycle 15, rubric 10/10 (OCR 二, visual 0.73)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import draw as draw_heng

def draw(t, ox=0.0, oy=0.0, scale=1.0):
    draw_heng(t, ox=ox-20*scale, oy=oy+50*scale, scale=0.35*scale)
    draw_heng(t, ox=ox+0*scale, oy=oy-100*scale, scale=0.65*scale)
