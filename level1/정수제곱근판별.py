# 실수가 정수인지 판별하려면 1로 나눠보면 됨

import math

def solution(n):
    return (math.sqrt(n)+1)**2 if math.sqrt(n)%1 == 0 else -1