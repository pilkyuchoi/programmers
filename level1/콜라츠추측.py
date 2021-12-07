def solution(num):
    if num==1:
        return 0
    
    cnt = 0
    for i in range(500):
        if num%2==0:
            num /= 2
        else:
            num *= 3
            num += 1
        cnt +=1
        if num == 1:
            break
            
    return cnt if cnt != 500 else -1