#빈리스트에 heappush, heappop하거나 아니면 만들어진 리스트를 heapify
#heap nlargest(개수, 리스트) 하면 개수만큼 내림차순 리스트 반환

import heapq

def solution(operations):
    heap = []
    for oper in operations:
        r = oper.split()[0]
        n = int(oper.split()[1])
        if r == 'I':
            heapq.heappush(heap, n)
        elif not heap:
            pass
        elif oper == 'D 1':
            heap = heapq.nlargest(len(heap), heap)[1:]
            heapq.heapify(heap)
        else:
            heapq.heappop(heap)
            
    if not heap:
        answer = [0, 0]
    else:
        answer = [heapq.nlargest(1, heap)[0], heap[0]]
    return answer