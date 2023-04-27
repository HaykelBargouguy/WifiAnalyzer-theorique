# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:36:18 2022

@author: 21650
"""
from math import log10
import subprocess
import re

def read_data_from_cmd2():
    p=subprocess.Popen("netsh wlan show networks mode=bssid",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out=p.stdout.read().decode('unicode_escape').strip()
    p.communicate() 
    return out

def get_puissance(SSID):
    data=read_data_from_cmd2()
    list1=re.findall('SSID.*?:.*?([A-z0-9 ]*).*?Signal.*?:.*?([0-9]*)%',data, re.DOTALL)
    for i in list1:
        if i[0]==SSID:
        
            return i[1]
        
        
def distance_wifi(rssi):
    Pr=10*log10(rssi)-30
    P0=-30
    f=2483.5
    n=3.5
    Fm=8
    c=(P0-Fm-Pr-10*n*log10(f)+30*n-32.44)/(10*n)
    d=pow(10,c)*1000
    return float(d)