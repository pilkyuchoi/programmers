#알파벳 모듈 string, string.ascii_uppercase
#ord 함수 기억
#머리가 복잡할 땐 수학적으로 접근하자
#상하 이동, 좌우 이동 따로 생각하기
#좌우 이동은 앞으로만 이동하는 경우와 중간에 뒤돌아가는 경우 2개 밖에 없다는 것 생각하기

def solution(name):
    answer = 0
    lasta_idx = 0
    min_move = len(name)-1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        lasta_idx = i + 1
        while lasta_idx < len(name) and name[lasta_idx] == 'A' :
            lasta_idx += 1

        min_move = min(min_move, i + i + len(name) - lasta_idx)

    answer += min_move

    return answer