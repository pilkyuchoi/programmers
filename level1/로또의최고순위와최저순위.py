#리스트 특정값 원소 개수는 .count(값)

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):        
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)

    correct = 0
    for lot in lottos:
        if lot in win_nums:
            correct += 1

    return [rank[correct + cnt_0], rank[correct]]