left = 13
right = 17

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 1
        for j in range(1,i):
            if i % j == 0:
                cnt += 1
        print(cnt)
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

solution(left, right)
