# dfs 함수 커스터마이징 잘하기

def dfs(computers, v, visited):
    visited[v] = True

    for idx, computer in enumerate(computers[v]):
        if not visited[idx] and computer == 1:
            dfs(computers, idx, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for v in range(n):
        if visited[v] == False:
            dfs(computers, v, visited)
            answer += 1

    return answer
