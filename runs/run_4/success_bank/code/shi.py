"""
十 (shi) — ten = heng + shu intersecting.

Tags: tag:character tag:2-strokes tag:heng+shu tag:component-of(干,千,丰,卡,...)
Mastered: run_4 cycle 17, rubric 10/10 (OCR 十, visual 0.72)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import draw as draw_heng
from shu import draw as draw_shu

def draw(t, ox=0.0, oy=0.0, scale=1.0):
    draw_heng(t, ox=ox+0*scale, oy=oy+20*scale, scale=0.75*scale)
    draw_shu(t, ox=ox+15*scale, oy=oy-10*scale, scale=0.85*scale)
