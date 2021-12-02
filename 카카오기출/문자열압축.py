# 하나씩 차근차근 만들어서 규칙 찾기!

def solution(s):
    answer = ''
    for k in range(1, (len(s) // 2) + 1):
        result = ''
        i = 0
        while i < len(s):
            cnt = 1
            j = k
            while (i+j) < len(s) and s[i:i+k] == s[i+j:i+j+k]:
                cnt += 1
                j += k
            if cnt == 1:
                result += s[i:i+k]
            else:
                result += (str(cnt) + s[i:i+k])
            i += j
        if not answer or len(result) < len(answer):
            answer = result

    if len(s) == 1:
        answer = s
 
    return len(answer)

 