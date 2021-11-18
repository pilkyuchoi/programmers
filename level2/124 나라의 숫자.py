# 진법 변환 공부하자

def notation(n, q):
    rev_based = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_based += str(mod)

    return rev_based[::-1]
