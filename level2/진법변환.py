# n진수 -> 10진수
int('101', 2)
int('202', 3)

# 10진수 -> 2, 8, 16진수
bin(16)[2:]
oct(16)[2:]
hex(16)[2:]

#10진수 -> n진수
def notation(n, q):
    rev_based = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_based += str(mod)

    return rev_based[::-1]
    #역순인 진수를 뒤집어 줘야 원래 변환하고자 하는 base가 출력

