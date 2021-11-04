#문자열 비교할 때 같지 않은 글자 수 셀 때 len(리스트) 활용하기

begin = 'hit'
target = 'cog'

words = ["hot", "dot", "dog", "lot", "log", "cog"]

def dfs(words, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()
        
        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != node[j]]) == 1:
                if words[i] not in visited:
                    visited.append(words[i])
                    stack.append(words[i])

        return visited

def solution(begin, target, words):
    if target not in words:
        answer = 0

    answer = len(dfs(words, begin)) - 1
    return answer

dfs(words, begin)
