people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    answer = 0
    weight = limit
    while people:
        limit = weight
        boat = 0 
        while limit > 0  and len(people) > 0 and boat <= 2:
                limit - people.pop() 
                answer += 1
                boat += 1
        
    return answer

solution(people, limit)