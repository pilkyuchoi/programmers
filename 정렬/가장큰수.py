#sort()에 reverse 하면 내림차순, key=lambda x: x 전달하면 해당 함수 기준으로 정렬해준다
#문자열 곱하면 반복
#0000같은 경우를 0으로 만들어주기 위해 마지막에 str(int) 작업 필요

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(numbers)))