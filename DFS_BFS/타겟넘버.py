#인덱스로 조합을 구하는 아이디어
# list(range()) 가능

from itertools import combinations

def solution(numbers, target):
    index = []
    for j in range(len(numbers)+1):
        index += list(combinations(list(range(len(numbers))), j ))
    
    answer = 0
    for idx in index[1:]:
        total = 0
        for i, n in enumerate(numbers):
            if i in idx:
                total += n
            elif i not in idx:
                total -= n
                
        if total == target:
            answer += 1

    return answer