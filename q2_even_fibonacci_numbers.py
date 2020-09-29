# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:39:23 2020
"""

fib_seq = [1, 2]

while True:
    if fib_seq[-2] + fib_seq[-1] <= 4000000:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
    else:
        print(sum([x for x in fib_seq if x % 2 == 0]))
        break