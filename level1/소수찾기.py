import math

def solution(n):
    array = [True for i in range(n+1)]

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i*j <= n:
                array[i*j] = False
                j+=1 

    return len([i for i in range(2, n+1) if array[i]])