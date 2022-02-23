# 하나씩 차근차근 만들어서 규칙 찾기!

def solution(s):
    length = len(s)

    # 글자 개수가 1이면 바로 1 리턴
    if length == 1:
        return 1

    answer = 0
    #반복크기 1부터 돌기
    for n_repeat in range(1, (length // 2) + 1):
        temp = ''
        idx = 0 # 반복문자열 시작 idx
        while idx < length:
            cnt = 1
            move = n_repeat # idx위치를 반복크기만큼 이동시켜주기 위한 변수
            # 몇번 같은지 세기
            while (idx+move) < length and s[idx:idx+n_repeat] == s[idx+move:idx+move+n_repeat]:
                cnt += 1
                move += n_repeat
            if cnt == 1:
                temp += s[idx:idx+n_repeat]
            else:
                temp += (str(cnt) + s[idx:idx+n_repeat])
            #반복크기만큼 이동시켜주기
            idx += move

        # 길이 세서 지금까지 값보다 작으면 업데이트
        len_temp = len(temp)
        if not answer or len_temp < answer:
            answer = len_temp
 
    return answer
