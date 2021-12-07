def solution(s):
    answer = ''
    for w in s.split(' '):
        for i in range(len(w)):
            if i%2==0:
                answer += w[i].upper()
            else:
                answer += w[i].lower()
        answer += ' '
        
    return answer[:-1]