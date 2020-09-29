# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:51:06 2020
"""
i = 1
while True:
    next_item = False
    for x in range(1, 21):
        if i % x != 0:
            next_item = True
            break
        
    if next_item == False:
        break
    
    i += 1
    
print(i)