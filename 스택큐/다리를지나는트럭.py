# 리스트 숫자 곱하면 문자열처럼 증식
#list.pop()은 시간복잡도 O(1), list.pop(0)은 시간복잡도 O(n)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    time = 0

    while truck_weights:
        bridge_weight -= bridge.popleft()
        if bridge_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.popleft()
            bridge.append(truck)
            bridge_weight += truck
        time += 1

    time += bridge_length

    return time
