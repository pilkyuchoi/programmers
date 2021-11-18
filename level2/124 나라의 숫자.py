# 진법 변환 공부하자
def solution(n):
    result = ''

    while n > 0:
        if n % 3:
            result = str(n%3) + result
            n //= 3
        else:
            result = '4' + result
            n = n//3 - 1

    return result
