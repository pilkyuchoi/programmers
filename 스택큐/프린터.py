#deque.rotate는 숫자만큼 이동, ex) deque.rotate(1)하면 [1,2,3,4] -> [4,1,2,3]
#음수는 반대방향
#deq도 len, max된다. tuple에 max하면 앞 숫자 기준


from collections import deque

def solution(priorities, location):
    deq = deque([(priority, index) for index, priority in enumerate(priorities)])

    answer = 1
    while len(deq) > 0:
        if deq[0][0] != max(deq)[0]:
            deq.rotate(-1)
        else:
            if deq[0][1] == location:
                break
            deq.popleft()
            answer += 1
            
    return answer

