# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:11:58 2020
"""

largest_pal = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        temp = str(x * y)
        if temp == temp[::-1] and int(temp) > largest_pal:
            largest_pal = int(temp)
print(largest_pal)