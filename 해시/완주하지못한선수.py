from collections import Counter

#Counter는 딕셔너리 형태로 요소를 센 key,value 쌍
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return answer

