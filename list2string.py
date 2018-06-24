# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:47:28 2018

@author: Administrator
"""

def list2string(spam):
    s = spam[0]
    for i in range(len(spam)-2):
        i += 1
        s += ', '+spam[i]
    s += ' and '+spam[len(spam)-1]
    print(s)

spam = ['apples','bananas']
list2string(spam)