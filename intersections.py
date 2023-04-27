# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:06:32 2022

@author: 21650
reference
https://stackoverflow.com/questions/55816902/finding-the-intersection-of-two-circles?fbclid=IwAR3yHRwyq10aHFVHE-lQ0VeAF7XLXUSy3ramDGJTxDcibx40EGbSkKGSG2k
"""
import  math 

def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    x0=float(x0)
    x1=float(x1)
    y0=float(y0)
    y1=float(y1)
    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 
        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        return (((x3), (y3)), ((x4), (y4)))
