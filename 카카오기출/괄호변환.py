# 올바른 괄호 판별: 리스트에 ( 넣고 )나오면 삭제하는 식으로
# 1단계부터 재귀적으로 반복하라는 건 solution 써라

p = '(()())()'

def right(r):
    l = []
    for i in r:
        if i == '(':
            l.append(i)
        else:
            try:
                l.pop()
            except:
                return False

    return False if l else True

def divide(r):
    r = list(r)
    u = []
    while r:
        if u.count('(') == u.count(')') and u:
            break
        u.append(r.pop(0))
    v = r

    return u, v