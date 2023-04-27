# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:09:19 2022

@author: 21650
"""
import matplotlib.pyplot as plt 

def draw_circles(c0,c1,c2,ax):
#get circles dimensions
    x0, y0, r0=c0
    x1, y1, r1=c1
    x2, y2, r2=c2
#define circles 
    c0=plt.Circle((x0,y0), radius=r0, color='yellow',alpha=.3)
    c1=plt.Circle((x1,y1), radius=r1, color='r',alpha=.3)
    c2=plt.Circle((x2,y2), radius=r2, color='g', alpha=.3)
       
#draw centres
    ax.scatter(x0, y0,marker ='v',color='y',s=200,alpha=1)
    ax.scatter(x1, y1,marker ='v',color='r',s=200,alpha=1)
    ax.scatter(x2, y2,marker ='v',color='g',s=200,alpha=1)

#add circles to plot
    plt.gca().add_artist(c0)
    plt.gca().add_artist(c1)
    plt.gca().add_artist(c2)
    