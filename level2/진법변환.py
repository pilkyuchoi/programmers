# n진수 -> 10진수
int('101', 2)
int('20', 3)

# 10진수 -> 2, 8, 16진수
bin(16)[2:]
oct(16)[2:]
hex(16)[2:]

#10진수 -> n진수
def notation(n, q):
    result = ''

    while n:
        n, mod = divmod(n, q)
        result = str(mod) + result

    return result

notation(6, 3)
    
#재귀함수 이용
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]