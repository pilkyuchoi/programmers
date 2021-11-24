n = 10

def solution(n):
    i = 1
    while True:
        if n % i == 1:
            return i
        i += 1