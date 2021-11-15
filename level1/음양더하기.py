absolutes = [4,7,12]
signs = [True, False, True]

def solution(absolutes, signs):
    answer = 0
    for n, sign in zip(absolutes, signs):
        if sign:
            answer += n
        else:
            answer -= n
    return answer