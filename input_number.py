# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:49:27 2018

@author: Administrator
"""
import collatz
print("请输入一个整数：")
try:
    num = int(input())

    while (num != 1):
        num = collatz.collatz(num)
except ValueError:
    print("警告，输入的必须为一个整数！")
        