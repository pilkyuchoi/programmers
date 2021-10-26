import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    try:
        while min(scoville) < K:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer += 1
    except:
        answer = -1
        
    return answer
