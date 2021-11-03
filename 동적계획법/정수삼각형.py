# 점화식 구하기!!
# 원래는 dp에 저장해야 하지만 이번엔 triangel 자체를 수정

def solution(triangle):
    answer = 0
    return answer
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])
    