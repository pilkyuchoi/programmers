#sorted 정렬 조건 sorted(a, key=lambda x: (x[0], -x[1]))

def solution(N, stages):
    rate = []
    for i in range(1, N+1):
        success = 0
        fail = 0
        for s in stages:
            if s >= i:
                success += 1
            if s == i:
                fail += 1

        if not success:
            rate.append((0,i))
        else:
            rate.append((fail / success, i)) 
            
    return [rank[1] for rank in sorted(rate, reverse=True, key=lambda x: (x[0], -x[1]))]