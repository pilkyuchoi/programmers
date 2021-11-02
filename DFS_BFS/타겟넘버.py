#인덱스로 조합을 구하는 아이디어
# list(range()) 가능
# itertools product 함수 : 곱집합
# 곱집합: 여러 집합들 간에 하나씩 뽑아 조합을 만들 수 있는 모든 수

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



from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

