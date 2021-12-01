# 리스트 인덱스로 삭제 del 리스트[인덱스]
# bin(i|j) 하면 i,j를 이진변환하고 같은 자리에 모두 0이 오면 0, 하나라도 1이 있으면 1로 출력
# '1'.ljust(5,'0') = '10000'

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

arr1 = [bin(x)[2:] for x in arr1]
arr2 = [bin(x)[2:] for x in arr2]

l1 = []
l2 = []
for a, b in zip(arr1, arr2):
    while len(a) < n:
        a = '0' + a
    while len(b) < n:
        b = '0' + b
    l1.append(a)
    l2.append(b)

answer = []
for i in range(n):
    answer.append(''.join([str(int(x)+int(y)) for x, y in zip(l1[i], l2[i])]))

answer = [x.replace('0', ' ') for x in answer]
answer = [x.replace('1', '#') for x in answer]
answer = [x.replace('2', '#') for x in answer]

answer
