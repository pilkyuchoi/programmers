from itertools import combinations

numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    index = []
    for j in range(len(numbers)+1):
        index += list(combinations(list(range(len(numbers))), j ))
    print(index)
    
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

solution(numbers, target)
