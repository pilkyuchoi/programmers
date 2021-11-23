# 안 되면 sort 해보기
# 맘대로 정렬하지 말고 sort를 쓰자

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        l = []
        for order in orders:
            l.extend(list(combinations(sorted(order),c)))

        l_counts = Counter(l).most_common()
        minus = [l_count[0] for l_count in l_counts if l_count[1] == 1]
        l = [e for e in l if e not in minus]

        try:
            top = [Counter(l).most_common()[0]]
            for combi in Counter(l).most_common()[1:]:
                if combi[1] == top[-1][1]:
                    top.append(combi)
                else:
                    break

            for t in top:
                answer.append(''.join(t[0]))

        except:
            pass
        
    return sorted(answer)

