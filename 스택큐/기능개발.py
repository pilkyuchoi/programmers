#스택큐는 pop으로
#day를 저장해놓고 쓰기

def solution(progresses, speeds):
    answer = []
    cnt = 0
    day = 0
    while len(progresses) > 0:
        if progresses[0] + (speeds[0] * day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1

    answer.append(cnt)

    return answer