def solution(phone_book):
    #문자열을 정렬하면 같은 문자열을 포함하고 있는 애들이 바로 뒤에 정렬됨
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
    return answer