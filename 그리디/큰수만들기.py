#순서가 있을 땐 스택활용 고려하기!

def solution(number, k):
    answer = [] 
    
    for num in number:

        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
                
        answer.append(num)

    return ''.join(answer[:len(number)-k]) 