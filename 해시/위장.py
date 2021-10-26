#경우의 수 푸는 문제
#갯수만큼 다 곱해주면 된다(안 입을 수도 있으니 종류별+1, 아무것도 안 입는 경우는 없으니 최종-1)

from collections import Counter

def solution(clothes):
    answer = 1
    cnt = Counter([cat for name, cat in clothes])
    for cat in cnt:
        answer *= cnt[cat]+1
    return answer - 1 
