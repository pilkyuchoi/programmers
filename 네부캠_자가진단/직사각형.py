v = [[1,1],[2,2],[1,2]]

x = [i[0] for i in v]
y = [i[1] for i in v]

from collections import Counter

answer = []
for s in x, y:
    for i in s:
        if Counter(s)[i] == 1:
            answer.append(i)

answer
