# 이거랑은 상관없지만 정규식 외우자

l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dic = {}
for a, i in zip(l, range(10)):
    dic[a] = str(i)

def solution(s):
    for a in l:
        if a in s:
            s = s.replace(a, dic[a])
    
    return int(s)

