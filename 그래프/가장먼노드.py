n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


from collections import deque

def solution(n, vertex):
    graph = []
    for i in range(n+1):
        graph.append(set())

    for ver in vertex:
        for i in range(1, n+1):
            if i in ver:
                for ve in ver:
                    if ve != i:
                        graph[i].add(ve)

    queue = deque([1])
    visited = [False] * (n+1)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return 

solution(n, vertex)