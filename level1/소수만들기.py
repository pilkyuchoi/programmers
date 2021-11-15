from itertools import combinations
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1): 
        if n % i == 0:
            return False

    return True

def solution(nums):
    return len([sum(e) for e in list(combinations(nums, 3)) if isPrime(sum(e))])