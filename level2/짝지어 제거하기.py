def solution(s):
    l = []
    for c in s:
        if l:
            if c != l[-1]:
                l.append(c)
            else:
                l.pop()
        else:
            l.append(c)
            
    return 0 if l else 1