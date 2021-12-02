#정렬되어있다는 말이 없으면 정렬하고 해야 함
#for문의 iterable 객체는 처음 기준 인덱스로 도는 거라 중간에 요소를 삭제하면 
#길이가 짧아진 객체에 처음에 저장된 인덱스로 접근해서 접근 안하는 요소가 생김
#차집합하면 자동으로 sort 됨

def solution(n, lost, reserve):
    reserve.sort()
    lost.sort()

    for res in reserve.copy():
        if res in lost:
            lost.remove(res)
            reserve.remove(res)

    for res in reserve:

        if (res-1) in lost:
            lost.remove(res-1)

        elif (res+1) in lost:
            lost.remove(res+1)

    answer = n - len(lost)

    return answer 