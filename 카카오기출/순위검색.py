# lower-bound search

def find(s):
    idx = []
    for i in range(len(s)):
        if s[i] == '-':
            idx.append(i)
    return idx

def solution(info, query):
    answer = []
    qs = []
    for q in query:
        q = q.replace(' and','')
        qs.append(q.split(' '))
    infs = []
    for inf in info:
        infs.append(inf.split(' '))
    
    for q in qs:
        cnt = 0
        idxs = find(q)
        for inf in infs:
            for idx in idxs:
                inf[idx] = '-'
            if inf[:-1] == q[:-1] and int(inf[-1]) >= int(q[-1]):
                cnt += 1
                
        answer.append(cnt)
        
    return answer