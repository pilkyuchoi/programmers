# 프로그래머스 numpy 존재...
# numpy 리스트 변환은 .tolist()

import numpy as np

def solution(arr1, arr2):
    return (np.array(arr1) + np.array(arr2)).tolist()

# numpy 안 쓰고
def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for j in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
        
    return answer