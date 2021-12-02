# dic['a'] = 1, dic['a'] = 2하면 마지막으로 한 것만 남음

def solution(record):
    dic = {}
    for rec in record:
        words = rec.split()
        if words[0] in ['Enter', 'Change']:
            dic[words[1]] = words[2]

    answer = []
    for rec in record:
        words = rec.split()
        if words[0] == 'Enter':
            answer.append(f'{dic[words[1]]}님이 들어왔습니다')
        elif words[0] == 'Leave':
            answer.append(f'{dic[words[1]]}님이 나갔습니다.')

    return answer 