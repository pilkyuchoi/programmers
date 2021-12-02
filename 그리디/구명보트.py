#if 에서 & 쓰지 말자 . and라고 쓰자

from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse= True))
    answer = 0

    while people:
        if len(people) == 1:
            people.pop()
            answer += 1
        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1
        else:
            people.popleft()
            answer += 1

    return answer 