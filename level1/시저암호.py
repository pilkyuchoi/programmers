# chr(97)은 a, chr(48)은 0
# ord('a')은 97, ord('0')은 48
# 아스키코드 적당히 외우기 
# z에서 a로 밀려나는 종류의 문제들은 나머지 활용하기
# 대소문자 판별 isupper(), islower()

def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif c.isupper():
            answer += chr(((ord(c)-ord('A')+n)%26) + ord('A'))
        else:
            answer += chr(((ord(c)-ord('a')+n)%26) + ord('a'))

    return answer