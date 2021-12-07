def solution(arr, divisor):
    l = []
    for a in arr:
        if a % divisor == 0:
            l.append(a)
    return sorted(l) if l else [-1]