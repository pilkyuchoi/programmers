import heapq

#파이썬 heapq는 min heap
#max heap으로 하고 싶으면 (h, -h) 쌍으로 처리하고 [1] 인덱스로 호출하기

#min같은 함수는 시간복잡도가 높음
#최소힙의 첫번째 인자가 곧 최솟값

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    try:
        while scoville[0] < K:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer += 1
    except:
        answer = -1
        
    return answer
