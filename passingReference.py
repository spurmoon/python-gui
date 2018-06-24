# -*- coding: utf-8 -*-
"""
Created on Sun May 27 11:22:13 2018

@author: Administrator
"""

def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)