# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:39:15 2022

@author: 21650
"""
from intersections import get_intersections
from math import sqrt
from itertools import combinations

def comb(sample_list):
    list_combinations = list()
    list_combinations += list(combinations(sample_list, 3))
    return(list_combinations)

def centre_grav(t):
    p1,p2,p3=t
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (((x1+x2+x3)/3),((y1+y2+y3)/3))

def dist(t):
    p1,p2,p3=t
    x1, y1 = p1
    cg = centre_grav((p1,p2,p3))
    dis = sqrt((x1-cg[0])**2 + (y1-cg[1])**2)
    return dis

def my_x_y_location(c0,c1,c2):
    c0=tuple(c0)
    c1=tuple(c1)
    c2=tuple(c2)
    p1,p2=get_intersections(c0[0],c0[1],c0[2],c1[0],c1[1],c1[2])
    p3,p4=get_intersections(c0[0],c0[1],c0[2],c2[0],c2[1],c2[2])
    p5,p6=get_intersections(c1[0],c1[1],c1[2],c2[0],c2[1],c2[2])
    points=[p1,p2,p3,p4,p5,p6]
    triples=comb(points)
    min_t=triples[0]
    for i in triples:
        if dist(i)<dist(min_t):
            min_t=i
    return(centre_grav(min_t))
