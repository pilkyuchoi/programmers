# 2진법, 3진법 공부하자

from itertools import product

onetwofour = [1, 2, 4]

def solution(n):
    length = 0
    i = 1

    while length < n:
        idx = length
        length += 3**i
        i += 1

    answer = ''
    for j in list(product(onetwofour, repeat=(i-1)))[n-idx-1]:
        answer += str(j)

    return answer

# 효율성 틀림