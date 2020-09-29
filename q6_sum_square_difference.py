# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:51:51 2020
"""

sum_square = sum([x**2 for x in range(1,101)])
square_sum = sum([x for x in range(1,101)])**2
print(abs(square_sum - sum_square))