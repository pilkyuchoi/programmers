# DFS, BFS 그래프 만들 때 딕셔너리 고려
# 딕셔너리 get 함수 dic.get('key') 하면 그에 해당하는 value를 돌려주고, 
# 해당 키가 없으면 dic.get('key', value) 하면 key, value를 새로 넣어준다 (이미 있으면 있는 거 돌려줌)

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


from collections import deque

def solution(n, vertex):
    graph = {}
    for ver in vertex:
        graph[ver[0]] = graph.get(ver[0], []) + [ver[1]]
        graph[ver[1]] = graph.get(ver[1], []) + [ver[0]]

    queue = deque([1])
    visited = [0] * (n+1)
    visited[1] = 1

    while queue:
        length = len(queue)
        for i in range(length):
            v = queue.popleft()
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1


    return length

solution(n, vertex)
