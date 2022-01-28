#map, reduce, lambda 알아두자
# a = [1.2,2.3,3.4]
# list(map(int,a)) 하면 [1,2,3]

#from functools import reduce
# reduce(lambda x, y: x+y, [1,2,3,4,5], 100) 하면 115



def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

 