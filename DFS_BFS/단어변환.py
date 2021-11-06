#문자열 비교할 때 같지 않은 글자 수 셀 때 len(리스트) 활용하기

begin = 'hit'
target = 'cog'

def solution(begin, target, words):
    if target not in words:
        answer = 0
