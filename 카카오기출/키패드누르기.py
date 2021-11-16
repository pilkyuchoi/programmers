def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = n
        elif n in [3, 6, 9]:
            answer += 'R'
            right = n
        else:
            if n == 0:
                n = 11

            l_dis = abs(left - n) // 3 + abs(left - n) % 3
            r_dis = abs(right - n) // 3 + abs(right - n) % 3

            if l_dis < r_dis:
                answer += 'L'
                left = n
            elif r_dis < l_dis:
                answer += 'R'
                right = n
            else:
                if hand == 'left':
                    answer += 'L'
                    left = n
                else:
                    answer += 'R'
                    right = n

    return answer