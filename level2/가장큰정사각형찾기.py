# DP 점화식 찾기!!!!!

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

def solution(board):
    n = len(board)
    m = len(board[0])
    
    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], dp[i][j-1]) + 1
    
    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(board[i])
        answer = max(answer, temp)
    
    return answer**2