#재귀
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end = ' ')
    #현재노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#각 노드(인덱스)가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)


# 스택을 활용한 dfs 구현
def dfs(graph, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node]) # 앞에서부터 순회하고 싶으면 reversed

    return visited

dfs(graph, 1)