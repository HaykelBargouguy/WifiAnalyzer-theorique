# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:00:11 2022

@author: 21650
"""

import matplotlib.pyplot as plt 
from intersections import get_intersections
from question3 import my_x_y_location
def mark_points(c0,c1,c2,ax): 
    x0,y0,r0=c0
    x1,y1,r1=c1
    x2,y2,r2=c2
    #p1,p2 intersections entre c0 et c1
    p1,p2 = get_intersections(x0, y0, r0, x1, y1, r1) 
    if (p1,p2) is not None:
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'x', color='purple')
    #p3,p4 intersections entre c0 et c2
    p3,p4 = get_intersections(x0, y0, r0, x2, y2, r2) 
    if (p3,p4) is not None:
        plt.plot([p3[0], p4[0]], [p3[1], p4[1]], 'x', color='brown')
    #p5,p6 intersections entre c1 et c2 
    p5,p6 = get_intersections(x1, y1, r1, x2, y2, r2) 
    if (p5,p6) is not None:
        plt.plot([p5[0], p6[0]], [p5[1], p6[1]], 'x', color='r')


    #mark my location
    my_x,my_y= my_x_y_location(c0,c1,c2)
    ax.scatter(my_x, my_y,marker ='X',color='#000000',s=200,alpha=1)