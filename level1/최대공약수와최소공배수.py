# 최대공약수 gcd, 최소공배수 lcm
# 프로그래머스는 파이썬 3.8이라 lcm은 직접 구현

# 직접 구현도 기억해두기
def gcd(x,y):
    while y:
        x, y = y, x%y
    return x
    
from math import gcd

def lcm(x,y):
    return x*y // gcd(x,y)

def solution(n, m):
    return [gcd(n,m), lcm(n,m)]

