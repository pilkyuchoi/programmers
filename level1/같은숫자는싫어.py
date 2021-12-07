def solution(arr):
    l = ['a']
    for a in arr:
        if a != l[-1]:
            l.append(a)
    l.pop(0)
    return l