# n//2까지만 봐도 됨

def solution(n):
    answer = 0
    for i in range(1, (n//2)+1):
        if n%i == 0:
            answer+=i
    return answer + n