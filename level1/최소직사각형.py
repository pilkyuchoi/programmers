# max, min 활용

def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        size.sort()
        w = max(size[0], w)
        h = max(size[1], h)
    return w*h