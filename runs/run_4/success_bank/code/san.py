"""
三 (san) — three stacked hengs (short/medium/long).

Tags: tag:character tag:3-strokes tag:heng-stacked
Mastered: run_4 cycle 16, rubric 10/10, OCR 三, visual 0.64
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import draw as draw_heng

def draw(t, ox=0.0, oy=0.0, scale=1.0):
    draw_heng(t, ox=ox-20*scale, oy=oy+90*scale, scale=0.35*scale)
    draw_heng(t, ox=ox-25*scale, oy=oy-10*scale, scale=0.38*scale)
    draw_heng(t, ox=ox+10*scale, oy=oy-120*scale, scale=0.70*scale)
