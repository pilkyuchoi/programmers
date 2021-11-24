def solution(price, money, count):
    cnt = 1
    for i in range(count):
        money -= price*cnt
        cnt += 1

    return -money if money < 0 else 0