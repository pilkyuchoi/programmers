# 왜 길이 순으로 정렬해야 하는지는 모르겠지만 뭔가 안 풀릴 떄는 정렬 해보자

def solution(s):
    s = s[2:-2]
    s = sorted(s.split("},{"), key = lambda x: len(x))
    
    answer = []
    for e in s:
        for n in e.split(','):
            if int(n) not in answer:
                answer.append(int(n))
                
    return answer

