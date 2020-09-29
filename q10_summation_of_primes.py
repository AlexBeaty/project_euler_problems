# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:41:28 2020

Super slow brute force again
"""
my_primes = []

def isPrime(num,my_primes):
    #print(f'testing number: {num}')
    for prime in my_primes:
        if num % prime == 0:
            return False
    return True

for num in range(2, 2000000):
    if isPrime(num,my_primes):
        my_primes.append(num)
        
print(sum(my_primes))
