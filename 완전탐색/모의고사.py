#인덱스를 벗어날 땐 나머지를 잘 사용하자
#itertools cycle은 cycle('ABCD') --> A B C D A B C D ...

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            scores[2] += 1

    for idx, score in enumerate(scores, 1):
        if max(scores) == score:
            result.append(idx)

    return result