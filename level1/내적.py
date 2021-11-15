a = [1,2,3,4]
b = [-3,-1,0,2]

def solution(a, b):
    return sum([n1*n2 for n1, n2 in zip(a, b)])

solution(a, b)