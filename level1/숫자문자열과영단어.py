numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

def solution(numbers, hand):
    answer = ''

    hand = 'L' if hand == 'left' else 'R'

    left = '*'
    right = '#'
    for n in numbers:
        if n in [1, 4, 7]:
            answer + 'L'
            left = n
        elif n in [3, 6, 9]:
            answer + 'R'
            right = n
        elif n == 2:
            if left in [1, 5]:
                if right == 3:

    return answer