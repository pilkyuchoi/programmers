# 규칙에 최대공약수, 최소공약수 고려하기
#math.gcd,lcm 

import math

def solution(w,h):
    return w*h  - (w+h - math.gcd(w,h))