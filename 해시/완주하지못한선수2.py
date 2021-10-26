def solution(participant, completion):
    temp = 0
    dic = {}
    for p in participant:
        dic[hash(p)] = p
        temp += hash(p)
    for c in completion:
        temp -= hash(c)
    answer = dic[temp]
    return answer