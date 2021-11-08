n = 6
times = [7, 10]


from bisect import bisect_left, bisect_right

def solution(n, times):
    l = []
    for t in times:
        for i in range(1, n+1):
            l.append(t*i)

    l.sort()
    return l[n-1]

solution(n, times)