# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:23:06 2020

super slow brute force
"""

for a in range(1000):
    for b in range(a + 1, 1000):
        for c in range(b + 1, 1000):
            if (a**2 + b**2 == c**2) and (a + b + c == 1000):
                print(a*b*c)

