# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:28:40 2018

@author: Administrator
"""

def collatz(number):

    if (number%2==0):
        out = number//2
    else:
        out = 3*number+1
        
    print(out)
    return out
    
