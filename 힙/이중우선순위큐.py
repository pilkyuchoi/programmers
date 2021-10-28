#빈리스트에 heappush, heappop하거나 아니면 만들어진 리스트를 heapify
#heap nlargest(개수, 리스트) 하면 개수만큼 내림차순 리스트 반환

import heapq

def heapsort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    
    return sorted_nums

def solution(operations):
    nums = []
    sorted_nums = []
    for oper in operations:
        r = oper.split()[0]
        n = int(oper.split()[1])
        if r == 'I':
            nums.append(n)
            sorted_nums = heapsort(nums)
        elif not sorted_nums:
            pass
        elif oper == 'D 1':
            nums.remove(sorted_nums.pop())
        else:
            nums.remove(sorted_nums.pop(0))

    if not sorted_nums:
        answer = [0, 0]
    else:
        answer = [sorted_nums[-1], sorted_nums[0]]
    return answer