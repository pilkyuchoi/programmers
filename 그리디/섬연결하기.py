#신장 트리: 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# Kruskal 알고리즘
#2차원 리스트를 정렬할 때는 lambda 사용

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, edges):
    v, e = n, len(edges)
    parent = [0] * (v+1) 
    answer = 0
    
    for i in range(1, v+1):
        parent[i] = i
        
    edges.sort(key = lambda x: x[2])
    
    for edge in edges:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    return answer