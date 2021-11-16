# 이중 포문 break는 break 들어있는 해당 포문 하나만 빠져나감

def solution(board, moves):
    answer = 0
    l = []
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                l.append(b[m-1])
                b[m-1] = 0
                if len(l) >= 2:
                    if l[-1] == l[-2]:
                        l = l[:-2]
                        answer += 2
                break

    return answer
