# divmod(a, b) 하면 (a//b, a%b) 반환
# 몫 = quotient, 나머지 = remainder
# n진법 -> 10진법: int(숫자, n)

def solution(n):
    new = ''
    while n:
        n, r = divmod(n,3)
        new += str(r)

    return int(new,3)