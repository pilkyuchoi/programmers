def solution(participant, completion):
    #해시는 고유한 정수를 부여하는 함수
    temp = 0
    dic = {}
    for p in participant:
        dic[hash(p)] = p
        temp += hash(p)
    for c in completion:
        temp -= hash(c)
    answer = dic[temp]
    return answer




import heapq 

l = []
heapq.heapify(l)

heapq.heappush(l, (-1, 1))
heapq.heappush(l, (-2, 2))
heapq.heappush(l, (-3, 3))

heapq.heappop(l)[1]