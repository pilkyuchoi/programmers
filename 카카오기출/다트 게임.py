# isdecimal(): 문자열이 int로 변환 가능하면 True

def solution(dartResult):
    dartResult = dartResult.replace('10','X')

    l = []

    for i in range(len(dartResult)):
        if dartResult[i] == 'X':
            if dartResult[i+1] == 'S':
                l.append(10)
            elif dartResult[i+1] == 'D':
                l.append(100)
            elif dartResult[i+1] == 'T':
                l.append(1000)

        elif dartResult[i].isdecimal():
            if dartResult[i+1] == 'S':
                l.append(int(dartResult[i]))
            elif dartResult[i+1] == 'D':
                l.append(int(dartResult[i])**2)
            elif dartResult[i+1] == 'T':
                l.append(int(dartResult[i])**3)

        elif dartResult[i] == '*':
            if len(l) == 1:
                l[0] *= 2
            else:
                l[-1] *= 2
                l[-2] *= 2
        elif dartResult[i] == '#':
            l[-1] *= -1
            
        else:
            continue
            
    return sum(l)